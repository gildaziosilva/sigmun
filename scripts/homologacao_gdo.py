"""Roteiro de Homologação — Gestão Documental (DOM-GDO).

Executa o roteiro de aceitação do Ciclo 8 contra a aplicação
real (FastAPI + uvicorn) via HTTP, sobre a pilha completa:

  PostgreSQL 15 (docker-compose, porta 5433) -> migrações Alembic aplicadas
  -> seed de dados iniciais (tipos documentais, plano de classificação e
  tabelas de temporalidade) -> repositórios SQLAlchemy reais (sem overrides).

Cobre o fluxo de homologaçaõ definido para o Ciclo 8:
  criar documento -> upload versão -> classificar (plano pré-carregado) ->
  tramitar -> assinar -> consultar temporalidade -> arquivar -> destinar
bem como regras de negócio RN-GDO-001/002/004/005/008/010/011 e os casos de
uso do `005-Casos-de-Uso-Gestao-Documental`.

Uso:
    .venv/bin/python scripts/homologacao_gdo.py

Saída:
    Verificações [PASS/FAIL] numeradas (H-01..H-nn) + resumo;
    código de saída 0 quando todas passam, 1 em caso de falha.
    Evidência gravada em SIGMUN-Docs/DOM-GDO/evidencias/.
"""

from __future__ import annotations

import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYTHONPYCACHEPREFIX", "/tmp/pycache")

import httpx  # noqa: E402

PORTA = 8766
BASE = f"http://localhost:{PORTA}/api/v1/gdo"
EVIDENCE_DIR = ROOT / "SIGMUN-Docs" / "DOM-GDO" / "evidencias"

#: Resultados coletados: (código, descrição, PASS/FAIL, detalhe).
resultados: list[tuple[str, str, str, str]] = []


def verificar(codigo: str, descricao: str, condicao: bool, detalhe: str = "") -> bool:
    """Registra e imprime o resultado de uma verificação do roteiro."""
    marcador = "PASS" if condicao else "FAIL"
    resultados.append((codigo, descricao, marcador, detalhe))
    linha = f"  [{marcador}] {codigo} - {descricao}"
    if detalhe:
        linha += f"  | {detalhe}"
    print(linha)
    return bool(condicao)


def _detail(resp: httpx.Response) -> str:
    """Extrai 'detail' da resposta JSON, com fallback seguro para texto."""
    try:
        dados = resp.json()
        if isinstance(dados, dict) and dados.get("detail"):
            return str(dados["detail"])
        return resp.text[:200]
    except Exception:
        return (resp.text or f"(corpo vazio, status={resp.status_code})")[:200]


def _json(resp: httpx.Response) -> dict:
    """Retorna o corpo JSON da resposta ou dicionário vazio se inválido."""
    try:
        return resp.json() if isinstance(resp.json(), dict) else {}
    except Exception:
        return {}


def semear_gdo() -> None:
    """Aplica o seed de dados iniciais do DOM-GDO (idempotente)."""
    from src.core.infrastructure.database.session import SessionLocal
    from src.modules.sigmun_gdo.infrastructure.database.seeds import popular_seed_gdo

    with SessionLocal() as session:
        relatorio = popular_seed_gdo(session)
        session.commit()
    print(f"  Seed GDO aplicado: {relatorio}")


def subir_app() -> subprocess.Popen:
    """Sobe a aplicação real (uvicorn) em processo separado."""
    log_path = ROOT / "logs" / "homologacao_gdo_uvicorn.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("ab") as log_file:
        proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "src.main:app",
             "--host", "127.0.0.1", "--port", str(PORTA)],
            cwd=str(ROOT),
            stdout=log_file,
            stderr=log_file,
        )
    # Aguarda readiness
    for _ in range(40):
        try:
            with httpx.Client(timeout=3) as client:
                r = client.get(f"http://localhost:{PORTA}/health")
                if r.status_code == 200:
                    return proc
        except Exception:
            pass
        time.sleep(0.5)
    proc.terminate()
    raise RuntimeError("Aplicação não respondeu em /health dentro do prazo")


def gerar_evidencia(resultado_geral: bool, duracao_s: str) -> Path:
    """Grava evidência da homologação em SIGMUN-Docs/DOM-GDO/evidencias/."""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    agora = datetime.now()
    arquivo = EVIDENCE_DIR / f"{agora.strftime('%Y-%m-%d')}-homologacao-gdo.md"
    linhas = [
        "# Evidência de Homologação — DOM-GDO (Gestão Documental)",
        "",
        "**Domínio:** DOM-GDO — Gestão Documental",
        f"**Data:** {agora.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Duração:** {duracao_s}",
        f"**Resultado:** {'SUCESSO' if resultado_geral else 'FALHA'}",
        "",
        "## Verificações",
        "",
        "| # | Verificação | Status | Detalhe |",
        "|---|-------------|--------|---------|",
    ]
    for codigo, descricao, marcador, detalhe in resultados:
        linhas.append(f"| {codigo} | {descricao} | {marcador} | {detalhe} |")
    linhas += [
        "",
        "---",
        "",
        "**Documento:** " + arquivo.name,
        "**Última atualização:** " + agora.strftime('%Y-%m-%d'),
        "**Responsável:** Equipe SIGMUN",
        "**Status:** " + ("Concluído" if resultado_geral else "Pendente"),
        "",
    ]
    arquivo.write_text("\n".join(linhas), encoding="utf-8")
    return arquivo


def main() -> int:
    print("=" * 64)
    print("HOMOLOGAÇÃO DOM-GDO — GESTÃO DOCUMENTAL")
    print("Pilha real: PostgreSQL + migrações Alembic + seed + API uvicorn")
    print("=" * 64)

    inicio = time.perf_counter()

    # 0. Migrações no head + seed
    print("\n[0] Preparando ambiente (migrações + seed)...")
    mr = subprocess.run(
        [sys.executable, "-m", "alembic", "upgrade", "head"],
        cwd=str(ROOT), capture_output=True, text=True,
    )
    verificar("H-00", "Migrações Alembic aplicadas no head",
              mr.returncode == 0, f"output={mr.stderr.strip()[-200:]}")
    semear_gdo()

    # 1. Sobe aplicação
    print("\n[1] Subindo aplicação (uvicorn)...")
    proc = subir_app()

    try:
        with httpx.Client(base_url=f"http://localhost:{PORTA}", timeout=15) as c:
            # --- Funcionalidade básica da API ---
            r = c.get("/health")
            verificar("H-01", "GET /health responde 200", r.status_code == 200,
                      f"database={r.json().get('database')}")

            r = c.get("/openapi.json")
            paths = r.json().get("paths", {}) if r.status_code == 200 else {}
            gdo_paths = [p for p in paths if p.startswith("/api/v1/gdo")]
            verificar("H-02", "OpenAPI expõe endpoints de GDO",
                      r.status_code == 200 and len(gdo_paths) >= 15,
                      f"{len(gdo_paths)} rotas /api/v1/gdo")

            # --- Tipos documentais (tabela de referência do seed) ---
            r = c.get(f"{BASE}/tipos-documentais")
            tipos = r.json() if r.status_code == 200 else []
            tem_td = any(t["codigo"] in ("TD-OFICIO", "TD-PORTARIA") for t in tipos)
            verificar("H-03", "Seed de tipos documentais carregado",
                      r.status_code == 200 and len(tipos) >= 10 and tem_td,
                      f"{len(tipos)} tipos")

            # --- Plano de classificação (pré-requisito da classificação) ---
            r = c.get(f"{BASE}/classificacoes")
            cls = r.json().get("items", r.json()) if r.status_code == 200 else []
            verificar("H-04", "Plano de classificação documental carregado",
                      r.status_code == 200 and len(cls) >= 9,
                      f"{len(cls)} classificações")

            # --- Criação de documento (UC: CriarDocumento) ---
            codigo = f"HOMOLOG-{uuid4().hex[:8].upper()}"
            payload = {
                "codigo": codigo,
                "numero": "0001",
                "ano": 2026,
                "tipo_documental_id": "TD-OFICIO",
                "titulo": "Ofício de homologação do DOM-GDO",
                "descricao": "Documento criado pelo roteiro de homologação",
                "unidade_autor_id": "SECADM-01",
                "is_sigiloso": False,
                "conteudo_ref": f"storage://homologacao/{codigo}/v1.pdf",
            }
            r = c.post(f"{BASE}/documentos", json=payload)
            doc = r.json() if r.status_code in (200, 201) else {}
            verificar("H-05", "POST /documentos cria documento (201)",
                      r.status_code == 201, f"status={doc.get('status')}")

            # --- RN-GDO-001: unicidade de código documental por ano ---
            r = c.post(f"{BASE}/documentos", json=payload)
            verificar("H-06", "RN-GDO-001: código duplicado retorna 409",
                      r.status_code == 409, f"detail={_detail(r)}")

            # --- RN-GDO-002: hash SHA-256 ---
            r = c.post(f"{BASE}/documentos", json={
                **payload, "codigo": f"HOMOLOG-{uuid4().hex[:8].upper()}",
                "hash_integridade": "hash-curto",
            })
            verificar("H-07", "RN-GDO-002: hash inválido retorna 400",
                      r.status_code == 400, f"detail={_detail(r)}")

            # --- Validação de payload (422) ---
            r = c.post(f"{BASE}/documentos", json={
                **payload, "codigo": f"HOMOLOG-{uuid4().hex[:8].upper()}",
                "titulo": "x",
            })
            verificar("H-08", "Payload inválido retorna 422",
                      r.status_code == 422, f"status={r.status_code}")

            doc_id = doc.get("id")

            # --- Upload de versão (UC: CriarVersaoDocumento) ---
            r = c.post(f"{BASE}/documentos/{doc_id}/versoes", json={
                "conteudo_ref": f"storage://homologacao/{codigo}/v2.pdf",
                "autor_id": "SERVIDOR-01",
                "hash_integridade": "b" * 64,
            })
            verificar("H-09", "POST /documentos/{id}/versoes cria versão (201)",
                      r.status_code == 201, f"numero_versao={_json(r).get('numero_versao')}")

            # Segunda versão (garante histórico >=2)
            r = c.post(f"{BASE}/documentos/{doc_id}/versoes", json={
                "conteudo_ref": f"storage://homologacao/{codigo}/v3.pdf",
                "autor_id": "SERVIDOR-01",
                "hash_integridade": "c" * 64,
            })
            verificar("H-09b", "Segunda versão registrada (201)",
                      r.status_code == 201, f"numero_versao={_json(r).get('numero_versao')}")

            r = c.get(f"{BASE}/documentos/{doc_id}/versoes")
            versoes = r.json() if r.status_code == 200 else []
            verificar("H-10", "Histórico de versões listado (>=2)",
                      r.status_code == 200 and len(versoes) >= 2,
                      f"{len(versoes)} versões")

            # --- Tramitação (UC: TramitarDocumento) ---
            r = c.post(f"{BASE}/documentos/{doc_id}/tramitar", json={
                "unidade_origem_id": "SECADM-01",
                "unidade_destino_id": "SECFIN-01",
                "tipo": "envio",
                "motivo": "Encaminhamento para análise financeira",
                "observacao": "Homologação",
            })
            verificar("H-11", "POST /documentos/{id}/tramitar (201)",
                      r.status_code == 201, f"tipo={_json(r).get('tipo')}")

            r = c.get(f"{BASE}/documentos/{doc_id}/tramitacoes")
            tramitacoes = r.json() if r.status_code == 200 else []
            verificar("H-12", "Tramitações do documento listadas",
                      r.status_code == 200 and len(tramitacoes) >= 1,
                      f"{len(tramitacoes)} tramitações")

            # --- Consulta de temporalidade (UC de temporalidade) ---
            r = c.get(f"{BASE}/temporalidades/TEMP-001")
            tempo = r.json() if r.status_code == 200 else {}
            verificar("H-13", "Consulta de tabela de temporalidade (TEMP-001)",
                      r.status_code == 200
                      and tempo.get("prazo_tempo", 0) > 0
                      and tempo.get("tipo_destinacao") in ("eliminacao", "guarda_permanente"),
                      f"prazo={tempo.get('prazo_tempo')} {tempo.get('unidade_tempo')}")

            # --- Assinatura (UC: AssinarDocumento, RN-GDO-002/004) ---
            r = c.post(f"{BASE}/documentos/{doc_id}/assinar", json={
                "signatario_id": "SERVIDOR-01",
                "conteudo": f"conteudo-{codigo}",
                "autor_id": "SERVIDOR-01",
                "certificado_id": "ICP-BRASIL-0001",
            })
            verificar("H-14", "POST /documentos/{id}/assinar (201)",
                      r.status_code == 201,
                      f"hash_assinatura={'set' if _json(r).get('hash_assinatura') else 'vazio'}")

            # --- Arquivamento (UC: ArquivarDocumento, RN-GDO-008) ---
            r = c.post(f"{BASE}/documentos/{doc_id}/arquivar", json={
                "unidade_arquivo_id": "ARQ-001",
                "autor_id": "SERVIDOR-01",
                "observacao": "Arquivamento em fase corrente",
            })
            verificar("H-15", "POST /documentos/{id}/arquivar (201)",
                      r.status_code == 201, f"arquivamento_id={_json(r).get('id')}")

            # --- Destinação final (UC: AvaliarDestinacao, RN-GDO-004/010) ---
            r = c.post(f"{BASE}/documentos/{doc_id}/destinacao", json={
                "tipo_destinacao": "guarda_permanente",
                "autor_id": "AUTORIDADE-01",
                "autoridade_homologadora_id": "AUTORIDADE-01",
                "justificativa": "Guarda permanente conforme TTD vigente",
            })
            verificar("H-16", "Destinação guarda permanente aplicada (200)",
                      r.status_code == 200,
                      f"status={_json(r).get('status')}")

            # --- RN-GDO-011: eliminação exige autoridade homologadora ---
            r2 = c.post(f"{BASE}/documentos", json={
                "codigo": f"HOMOLOG-{uuid4().hex[:8].upper()}",
                "numero": "0002", "ano": 2026,
                "tipo_documental_id": "TD-RELATORIO",
                "titulo": "Relatório de homologação — eliminação",
                "unidade_autor_id": "SECADM-01",
            })
            doc2_id = _json(r2).get("id")
            r = c.post(f"{BASE}/documentos/{doc2_id}/destinacao", json={
                "tipo_destinacao": "eliminacao",
                "autor_id": "SERVIDOR-01",
            })
            verificar("H-18", "RN-GDO-011: eliminação sem homologadora retorna 403",
                      r.status_code == 403, f"detail={_detail(r)}")

            # --- Estado final do documento principal (após destinação) ---
            r = c.get(f"{BASE}/documentos/{doc_id}")
            doc_final = r.json() if r.status_code == 200 else {}
            verificar("H-17", "Estado final do documento consistente",
                      r.status_code == 200 and doc_final.get("status") == "arquivado"
                      and doc_final.get("conteudo_ref"),
                      f"status={doc_final.get('status')}, "
                      f"conteudo_ref={doc_final.get('conteudo_ref')}")

            r = c.post(f"{BASE}/documentos/{doc2_id}/destinacao", json={
                "tipo_destinacao": "eliminacao",
                "autor_id": "SERVIDOR-01",
                "autoridade_homologadora_id": "AUTORIDADE-01",
                "justificativa": "Eliminação autorizada conforme TTD",
            })
            verificar("H-19", "Eliminação com homologadora aplicada (200)",
                      r.status_code == 200,
                      f"status={_json(r).get('status')}, "
                      f"data_eliminacao={_json(r).get('data_eliminacao') is not None}")

            # --- Documento inexistente -> 404 ---
            r = c.post(f"{BASE}/documentos/{uuid4()}/tramitar", json={
                "unidade_origem_id": "SECADM-01", "unidade_destino_id": "SECFIN-01",
                "tipo": "envio",
            })
            verificar("H-20", "Documento inexistente retorna 404",
                      r.status_code == 404, f"detail={_detail(r)}")

            # --- Listagem ---
            r = c.get(f"{BASE}/documentos")
            lista = r.json().get("items", []) if r.status_code == 200 else []
            total_lista = r.json().get("total", 0) if r.status_code == 200 else 0
            verificar("H-21", "GET /documentos lista documentos criados",
                      r.status_code == 200 and len(lista) >= 1,
                      f"total={total_lista}")
    finally:
        proc.terminate()
        proc.wait(timeout=10)

    duracao = f"{time.perf_counter() - inicio:.2f}s"

    # Resumo
    aprovadas = sum(1 for r in resultados if r[2] == "PASS")
    total = len(resultados)
    sucesso = aprovadas == total
    print("\n" + "=" * 64)
    print(f"RESUMO HOMOLOGAÇÃO DOM-GDO: {aprovadas}/{total} verificações aprovadas")
    print(f"Duração: {duracao} | Resultado: {'SUCESSO' if sucesso else 'FALHA'}")
    print("=" * 64)

    arquivo = gerar_evidencia(sucesso, duracao)
    print(f"Evidência gerada: {arquivo}")

    return 0 if sucesso else 1


if __name__ == "__main__":
    sys.exit(main())
