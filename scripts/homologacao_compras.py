"""Roteiro de Homologação — Gestão de Compras e Contratações (DOM-COMPRAS-001).

Executa o roteiro de aceitação da Fase 7 – Homologação
(020-Plano-de-Implantacao, seção 16; ROADMAP item 17) contra a aplicação
real (FastAPI + uvicorn) via HTTP, cobrindo os aspectos exigidos:

  funcionalidades | processos | regras de negócio | permissões |
  integrações | dados | auditoria | critérios de aceitação

AMBIENTES:
    padrão  – aplicação real com repositórios em memória (não requer banco);
    --pg    – pilha 100% real: PostgreSQL 15 do docker-compose (porta 5433),
              migrações Alembic aplicadas e repositórios SQLAlchemy sem
              overrides. Executar antes: docker compose up -d postgres redis
              && alembic upgrade head.

Uso:
    .venv/bin/python scripts/homologacao_compras.py [--pg]

Saída:
    Verificações [PASS/FAIL] numeradas (H-01..H-nn) + resumo;
    código de saída 0 quando todas passam, 1 em caso de falha.
"""

from __future__ import annotations

import os
import sys
import threading
import time
from datetime import date, timedelta
from pathlib import Path
from uuid import UUID, uuid4

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYTHONPYCACHEPREFIX", "/tmp/pycache")

import httpx  # noqa: E402
import uvicorn  # noqa: E402

from src.main import app  # noqa: E402
from src.modules.sigmun_compras.presentation.api.auditoria_router import (  # noqa: E402
    get_trilha_auditoria_repository as auditoria_trilha_dep,
)
from src.modules.sigmun_compras.presentation.api.compras_router import (  # noqa: E402
    get_compra_repository as compras_repo_dep,
)
from src.modules.sigmun_compras.presentation.api.contratos_router import (  # noqa: E402
    get_compra_repository as compras_repo_dep_formalizar,
    get_contrato_repository as contratos_repo_dep,
    get_trilha_auditoria_repository as contratos_trilha_dep,
)
from src.modules.sigmun_compras.presentation.api.fornecedores_router import (  # noqa: E402
    get_fornecedor_repository as fornecedores_repo_dep,
)
from src.modules.sigmun_compras.presentation.api.itens_compras_router import (  # noqa: E402
    get_item_compra_repository as itens_repo_dep,
)
from src.modules.sigmun_compras.presentation.api.processo_documental_router import (  # noqa: E402
    get_processo_documental_repository as processos_repo_dep,
)
from tests.unit.test_compra_use_cases import InMemoryCompraRepository  # noqa: E402
from tests.unit.test_contrato_use_cases import InMemoryContratoRepository  # noqa: E402
from tests.unit.test_fornecedor_use_cases import InMemoryFornecedorRepository  # noqa: E402
from tests.unit.test_item_compra_use_cases import InMemoryItemCompraRepository  # noqa: E402
from tests.unit.test_processo_documental_use_cases import (  # noqa: E402
    InMemoryProcessoRepository,
)
from tests.unit.test_registro_auditoria import (  # noqa: E402
    InMemoryTrilhaAuditoriaRepository,
)

PORTA = 8765

#: Modo de execução: --pg exercita a pilha real sobre PostgreSQL (sem overrides).
MODO_PG = "--pg" in sys.argv

#: UUIDs fixos da semeadura mínima do domínio core (execução idempotente).
UNIDADE_ID = UUID("00000000-0000-0000-0000-0000000000a1")
PESSOA_ID = UUID("00000000-0000-0000-0000-0000000000b1")
PESSOA_JURIDICA_ID = UUID("00000000-0000-0000-0000-0000000000c1")

#: Usuários de homologação (autenticação provisória por headers até DOM-IDN).
USUARIO_OPERADOR_ID = uuid4()
USUARIO_AUDITOR_ID = uuid4()
OPERADOR = {
    "X-Usuario-Id": str(USUARIO_OPERADOR_ID),
    "X-Usuario-Papel": "operador_compras",
}
AUDITOR = {
    "X-Usuario-Id": str(USUARIO_AUDITOR_ID),
    "X-Usuario-Papel": "auditor",
}

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


def semear_postgresql() -> None:
    """Limpa as tabelas de domínio e semeia o mínimo do domínio core.

    Cadeia de FKs necessária: unidades_administrativas -> pessoas ->
    pessoas_juridicas -> (fornecedores criado pela própria API).
    """
    import psycopg2

    conn = psycopg2.connect(
        host="localhost", port=5433, dbname="sigmun",
        user="sigmun", password="sigmun",
    )
    try:
        cur = conn.cursor()
        cur.execute("TRUNCATE compras.itens_compras, compras.contratos,"
                    " compras.compras CASCADE")
        cur.execute("TRUNCATE auditoria.eventos CASCADE")
        cur.execute("DELETE FROM core.processos_documentais")
        cur.execute("DELETE FROM core.fornecedores")
        cur.execute(
            "INSERT INTO core.unidades_administrativas (id, nome)"
            " VALUES (%s, %s) ON CONFLICT (id) DO NOTHING",
            (str(UNIDADE_ID), "Secretaria Municipal de Administração"),
        )
        cur.execute(
            "INSERT INTO core.pessoas (id, tipo, categoria, unidade_id)"
            " VALUES (%s, 'JURIDICA', 'FORNECEDOR', %s) ON CONFLICT (id) DO NOTHING",
            (str(PESSOA_ID), str(UNIDADE_ID)),
        )
        cur.execute(
            "INSERT INTO core.pessoas_juridicas (id, pessoa_id, razao_social)"
            " VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
            (str(PESSOA_JURIDICA_ID), str(PESSOA_ID), "Empresa de Suprimentos LTDA"),
        )
        conn.commit()
        cur.close()
    finally:
        conn.close()
def executar_roteiro(
    http: httpx.Client,
    compras_repo: InMemoryCompraRepository | None,
    itens_repo: InMemoryItemCompraRepository | None,
    contratos_repo: InMemoryContratoRepository | None,
) -> None:
    """Executa o roteiro de homologação ponta a ponta."""
    hoje = date.today()

    # ================= A. Funcionalidades (infraestrutura da API) ==========
    print("\n--- A. Funcionalidades (infraestrutura da API) ---")
    r = http.get("/health")
    verificar("H-01", "GET /health responde 200", r.status_code == 200,
              f"HTTP {r.status_code}")
    r = http.get("/docs")
    verificar("H-02", "Documentação interativa (/docs) disponível",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.get("/openapi.json")
    paths = list(r.json().get("paths", {})) if r.status_code == 200 else []
    verificar("H-03", "OpenAPI publica o contrato dos endpoints",
              r.status_code == 200 and len(paths) >= 17, f"{len(paths)} paths")

    # ================= B. Cadastro de Fornecedores (RN-030/031) ============
    print("\n--- B. Cadastro de Fornecedores (RN-COMPRAS-030/031) ---")
    pj_id = str(PESSOA_JURIDICA_ID if MODO_PG else uuid4())
    r = http.post("/api/v1/fornecedores", json={"pessoa_juridica_id": pj_id},
                  headers=OPERADOR)
    fornecedor_id = ""
    if verificar("H-04", "POST /fornecedores registra fornecedor ativo",
                 r.status_code == 201, f"HTTP {r.status_code}"):
        fornecedor_id = r.json()["id"]
    verificar("H-05", "Fornecedor criado com situação ATIVO",
              bool(fornecedor_id) and r.json().get("situacao_cadastro") == "ATIVO")
    r = http.post("/api/v1/fornecedores", json={"pessoa_juridica_id": pj_id},
                  headers=OPERADOR)
    verificar("H-06", "Fornecedor duplicado para a mesma PJ bloqueado (RN-031)",
              r.status_code == 409, f"HTTP {r.status_code}")

    # ================= C. Processos Documentais (RN-028/029) ===============
    print("\n--- C. Processos Documentais (RN-COMPRAS-028/029) ---")
    processo_payload = {
        "unidade_id": str(UNIDADE_ID),
        "numero": "001",
        "ano": 2026,
        "assunto": "Aquisição de material de escritório",
    }
    r = http.post("/api/v1/processos-documentais", json=processo_payload,
                  headers=OPERADOR)
    processo_id = ""
    if verificar("H-07", "POST /processos-documentais abre o processo",
                 r.status_code == 201, f"HTTP {r.status_code}"):
        processo_id = r.json()["id"]
    r = http.post("/api/v1/processos-documentais", json=processo_payload,
                  headers=OPERADOR)
    verificar("H-08", "Número/ano duplicado bloqueado (RN-029)",
              r.status_code == 409, f"HTTP {r.status_code}")

    # Registra os vínculos nos repositórios de consulta (exists_*) usados
    # pelas validações de negócio dos casos de uso. No modo --pg a pilha
    # real consulta o PostgreSQL e os vínculos nascem das próprias chamadas.
    if compras_repo is not None and processo_id and fornecedor_id:
        compras_repo.add_processo(UUID(processo_id))
        compras_repo.add_fornecedor_ativo(UUID(fornecedor_id))
        compras_repo.add_unidade(UNIDADE_ID)
        if contratos_repo is not None:
            contratos_repo.add_processo_documental(UUID(processo_id))
            contratos_repo.add_fornecedor_ativo(UUID(fornecedor_id))
            contratos_repo.add_unidade(UNIDADE_ID)

    # ================= D. Compras e Itens (RN-011/012/025/030) =============
    print("\n--- D. Registro de Compras e Itens (RN-COMPRAS-011/012/025/030) ---")
    compra_payload = {
        "processo_documental_id": processo_id,
        "fornecedor_id": fornecedor_id,
        "unidade_id": str(UNIDADE_ID),
        "numero": "001/2026",
        "data": hoje.isoformat(),
        "valor_total": "45000.00",
    }
    r = http.post("/api/v1/compras", json=compra_payload, headers=OPERADOR)
    compra_id = ""
    if verificar("H-09", "POST /compras registra compra em RASCUNHO (RN-025)",
                 r.status_code == 201 and r.json().get("situacao") == "RASCUNHO",
                 f"HTTP {r.status_code}"):
        compra_id = r.json()["id"]
        if itens_repo is not None:
            itens_repo.add_compra(UUID(compra_id))
    r = http.post("/api/v1/compras",
                  json={**compra_payload, "fornecedor_id": str(uuid4())},
                  headers=OPERADOR)
    verificar("H-10", "Compra com fornecedor inexistente rejeitada (RN-030)",
              r.status_code == 404, f"HTTP {r.status_code}")

    r = http.post(f"/api/v1/compras/{compra_id}/itens",
                  json={"descricao": "Serviço de manutenção de impressoras",
                        "quantidade": "2", "valor_unitario": "22500.00"},
                  headers=OPERADOR)
    item_id = ""
    if verificar("H-11", "POST itens registra o item da compra",
                 r.status_code == 201, f"HTTP {r.status_code}"):
        item_id = r.json()["id"]
    verificar("H-12", "Valor total do item = quantidade x unitário (RN-012)",
              bool(item_id) and float(r.json()["valor_total"]) == 45000.0)
    r = http.post(f"/api/v1/compras/{compra_id}/itens",
                  json={"descricao": "Caneta", "quantidade": "0",
                        "valor_unitario": "10.00"},
                  headers=OPERADOR)
    verificar("H-13", "Item com quantidade zero rejeitado (RN-012)",
              r.status_code == 422, f"HTTP {r.status_code}")

    # ================= E. Ciclo processual da Compra (RN-026/027) ==========
    print("\n--- E. Ciclo processual da Compra (RN-COMPRAS-026/027) ---")
    situacao_url = f"/api/v1/compras/{compra_id}/situacao"
    r = http.patch(situacao_url, json={"situacao": "EM_INSTRUCAO"},
                   headers=OPERADOR)
    verificar("H-14", "Transição RASCUNHO -> EM_INSTRUCAO",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.patch(situacao_url, json={"situacao": "HOMOLOGADO"},
                   headers=OPERADOR)
    verificar("H-15", "Salto de fase processual bloqueado (RN-026)",
              r.status_code == 400, f"HTTP {r.status_code}")
    for situacao, codigo in (("EM_ANALISE", "H-16"),
                             ("EM_PROCEDIMENTO", "H-17"),
                             ("EM_JULGAMENTO", "H-18")):
        r = http.patch(situacao_url, json={"situacao": situacao},
                       headers=OPERADOR)
        verificar(codigo, f"Transição para {situacao}", r.status_code == 200,
                  f"HTTP {r.status_code}")
    r = http.patch(f"/api/v1/compras/{compra_id}/pendencias",
                   json={"pendencias_impeditivas": True,
                         "justificativa": "Documentação pendente"},
                   headers=OPERADOR)
    verificar("H-19", "Pendência impeditiva registrada (RN-027)",
              r.status_code == 200
              and r.json().get("pendencias_impeditivas") is True,
              f"HTTP {r.status_code}")
    r = http.patch(situacao_url, json={"situacao": "HOMOLOGADO"},
                   headers=OPERADOR)
    verificar("H-20", "Avanço com pendência impeditiva bloqueado (RN-027)",
              r.status_code == 400, f"HTTP {r.status_code}")
    r = http.patch(f"/api/v1/compras/{compra_id}/pendencias",
                   json={"pendencias_impeditivas": False}, headers=OPERADOR)
    verificar("H-21", "Pendências resolvidas",
              r.status_code == 200
              and r.json().get("pendencias_impeditivas") is False,
              f"HTTP {r.status_code}")
    r = http.patch(situacao_url, json={"situacao": "HOMOLOGADO"},
                   headers=OPERADOR)
    verificar("H-22", "Compra avança para HOMOLOGADO",
              r.status_code == 200 and r.json().get("situacao") == "HOMOLOGADO",
              f"HTTP {r.status_code}")
    r = http.get("/api/v1/compras", headers=OPERADOR)
    verificar("H-23", "Listagem de compras inclui a compra homologada",
              r.status_code == 200
              and any(c["id"] == compra_id for c in r.json().get("items", [])),
              f"HTTP {r.status_code}")

    # ============ F. Integração: Formalização da Contratação ===============
    print("\n--- F. Integração: Formalização da Contratação "
          "(UC-COMPRAS-022 / RN-036/038) ---")
    formalizar_url = f"/api/v1/contratos/formalizar?compra_id={compra_id}"
    contrato_payload = {
        "numero": "001/2026-CONTRATO",
        "data_inicio": hoje.isoformat(),
        "data_fim": (hoje + timedelta(days=365)).isoformat(),
        "valor": "45000.00",
        "objeto": "Aquisição de material de escritório",
        "data_assinatura": hoje.isoformat(),
    }
    r = http.post(formalizar_url, json=contrato_payload)
    verificar("H-24", "Formalização sem autenticação rejeitada (401)",
              r.status_code == 401, f"HTTP {r.status_code}")
    r = http.post(formalizar_url, json=contrato_payload, headers=OPERADOR)
    contrato_id = ""
    if verificar("H-24a", "Formalização cria contrato ASSINADO a partir da "
                          "compra homologada (RN-038)",
                 r.status_code == 201
                 and r.json().get("situacao") == "ASSINADO",
                 f"HTTP {r.status_code}"):
        contrato_id = r.json()["id"]
    r = http.get(f"/api/v1/compras/{compra_id}")
    verificar("H-25", "Compra avançou para CONTRATADO na formalização "
                      "(RN-026)",
              r.status_code == 200
              and r.json().get("situacao") == "CONTRATADO",
              f"HTTP {r.status_code}")
    r = http.post(formalizar_url, json=contrato_payload, headers=OPERADOR)
    verificar("H-26", "Número de contrato duplicado bloqueado (RN-036)",
              r.status_code == 409, f"HTTP {r.status_code}")

    # ================= G. Ciclo de vida do Contrato (RN-046/106) ===========
    print("\n--- G. Ciclo de vida do Contrato (RN-COMPRAS-046/106) ---")
    situacao_url_c = f"/api/v1/contratos/{contrato_id}/situacao"
    r = http.patch(situacao_url_c, json={"situacao": "VIGENTE"},
                   headers=OPERADOR)
    verificar("H-27", "ASSINADO -> VIGENTE dentro da vigência (RN-046)",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.patch(situacao_url_c, json={"situacao": "RESCINDIDO"},
                   headers=OPERADOR)
    verificar("H-28", "VIGENTE -> RESCINDIDO", r.status_code == 200,
              f"HTTP {r.status_code}")
    r = http.patch(situacao_url_c, json={"situacao": "EM_ELABORACAO"},
                   headers=OPERADOR)
    verificar("H-29", "Estado terminal não admite transição (RN-106)",
              r.status_code == 400, f"HTTP {r.status_code}")

    r = http.post("/api/v1/contratos", json={
        "processo_documental_id": processo_id,
        "fornecedor_id": fornecedor_id,
        "unidade_id": str(UNIDADE_ID),
        "numero": "003/2026-CONTRATO",
        "data_inicio": hoje.isoformat(),
        "valor": "1000.00",
        "objeto": "Contrato direto de teste",
    }, headers=OPERADOR)
    contrato2_id = ""
    if verificar("H-30", "POST /contratos registra contrato direto",
                 r.status_code == 201, f"HTTP {r.status_code}"):
        contrato2_id = r.json()["id"]
    r = http.delete(f"/api/v1/contratos/{contrato2_id}")
    verificar("H-31", "Exclusão sem X-Usuario-Id rejeitada (400)",
              r.status_code == 400, f"HTTP {r.status_code}")
    r = http.delete(f"/api/v1/contratos/{contrato2_id}", headers=OPERADOR)
    verificar("H-32", "Exclusão lógica (soft-delete) do contrato",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.get(f"/api/v1/contratos/{contrato2_id}")
    verificar("H-33", "Contrato excluído não é mais servido (RN-004)",
              r.status_code == 404, f"HTTP {r.status_code}")

    # ========== H. Permissões, Auditoria e Integridade dos Dados ===========
    print("\n--- H. Permissões, Auditoria e Integridade (017 seções 40/41/44) ---")
    r = http.get("/api/v1/auditoria")
    verificar("H-34", "Consulta de auditoria sem autenticação rejeitada (401)",
              r.status_code == 401, f"HTTP {r.status_code}")
    r = http.get("/api/v1/auditoria", headers=OPERADOR)
    verificar("H-35", "Perfil sem permissão à auditoria rejeitado (403)",
              r.status_code == 403, f"HTTP {r.status_code}")
    r = http.get("/api/v1/auditoria", headers=AUDITOR)
    eventos = r.json().get("items", []) if r.status_code == 200 else []
    verificar("H-36", "Perfil auditor consulta a trilha",
              r.status_code == 200 and r.json().get("total", 0) >= 5,
              f"HTTP {r.status_code}; {r.json().get('total', 0)} eventos")
    # Segunda consulta: o snapshot agora inclui o evento ACESSO registrado
    # pela consulta anterior (a própria consulta é auditada, seção 41).
    r = http.get("/api/v1/auditoria", headers=AUDITOR)
    eventos = r.json().get("items", []) if r.status_code == 200 else eventos
    categorias = {evento["categoria"] for evento in eventos}
    verificar("H-37", "Eventos de CRIACAO registrados na trilha",
              "CRIACAO" in categorias)
    verificar("H-38", "Eventos de ALTERACAO registrados na trilha",
              "ALTERACAO" in categorias)
    verificar("H-39", "Eventos de EXCLUSAO registrados na trilha",
              "EXCLUSAO" in categorias)
    verificar("H-40", "Acesso à própria auditoria é auditado (seção 41)",
              "ACESSO" in categorias)

    r = http.get(f"/api/v1/compras/{uuid4()}")
    verificar("H-41", "Consulta de compra inexistente responde 404",
              r.status_code == 404, f"HTTP {r.status_code}")
    r = http.delete(f"/api/v1/compras/{compra_id}", headers=OPERADOR)
    verificar("H-42", "Exclusão lógica (soft-delete) da compra",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.get(f"/api/v1/compras/{compra_id}")
    verificar("H-43", "Compra excluída não é mais servida (RN-004)",
              r.status_code == 404, f"HTTP {r.status_code}")
    r = http.patch(f"/api/v1/compras/{compra_id}/situacao",
                   json={"situacao": "EM_INSTRUCAO"}, headers=OPERADOR)
    verificar("H-44", "Compra excluída não opera (RN-004)",
              r.status_code == 404, f"HTTP {r.status_code}")
    r = http.delete(f"/api/v1/itens-compras/{item_id}",
                    headers=OPERADOR)
    verificar("H-45", "Remoção lógica do item da compra",
              r.status_code == 200, f"HTTP {r.status_code}")
    r = http.get(f"/api/v1/itens-compras/{item_id}")
    verificar("H-46", "Item removido não é mais servido (RN-004)",
              r.status_code == 404, f"HTTP {r.status_code}")


def main() -> int:
    """Prepara o ambiente, executa o roteiro e emite o resumo."""
    if MODO_PG:
        # Pilha 100% real: repositórios SQLAlchemy sobre o PostgreSQL do
        # docker-compose (porta 5433); nenhum override de dependência.
        compras_repo = itens_repo = contratos_repo = None
        semear_postgresql()
    else:
        # --- Composição da homologação: repositórios em memória compartilhados ---
        processos_repo = InMemoryProcessoRepository()
        fornecedores_repo = InMemoryFornecedorRepository()
        compras_repo = InMemoryCompraRepository()
        itens_repo = InMemoryItemCompraRepository()
        contratos_repo = InMemoryContratoRepository()
        trilha_repo = InMemoryTrilhaAuditoriaRepository()

        processos_repo.add_unidade(UNIDADE_ID)

        app.dependency_overrides[processos_repo_dep] = lambda: processos_repo
        app.dependency_overrides[fornecedores_repo_dep] = lambda: fornecedores_repo
        app.dependency_overrides[compras_repo_dep] = lambda: compras_repo
        # O router de contratos define seu próprio get_compra_repository para a
        # formalização; ambos apontam para o mesmo repositório em memória.
        app.dependency_overrides[compras_repo_dep_formalizar] = lambda: compras_repo
        app.dependency_overrides[itens_repo_dep] = lambda: itens_repo
        app.dependency_overrides[contratos_repo_dep] = lambda: contratos_repo
        app.dependency_overrides[auditoria_trilha_dep] = lambda: trilha_repo
        app.dependency_overrides[contratos_trilha_dep] = lambda: trilha_repo

    ambiente = (
        "aplicação real + PostgreSQL 15 (schemas core/compras/auditoria)"
        if MODO_PG else "aplicação real, repositórios em memória"
    )
    print("=" * 78)
    print("HOMOLOGAÇÃO DOM-COMPRAS-001 - Gestão de Compras e Contratações")
    print(f"Versão alvo: {app.version} | Ambiente: {ambiente}")
    print("=" * 78)

    # --- Aplicação real servida por uvicorn (HTTP real, não TestClient) ---
    server = uvicorn.Server(
        uvicorn.Config(app, host="127.0.0.1", port=PORTA, log_level="warning")
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    for _ in range(150):
        if server.started:
            break
        time.sleep(0.1)
    if not server.started:
        print("ERRO FATAL: o servidor de homologação não inicializou.")
        return 1

    try:
        with httpx.Client(
            base_url=f"http://127.0.0.1:{PORTA}", timeout=15.0
        ) as http:
            executar_roteiro(http, compras_repo, itens_repo, contratos_repo)
    finally:
        server.should_exit = True
        thread.join(timeout=10)
        app.dependency_overrides.clear()

    # --- Resumo (Termo de Homologação, 020 seção 17) ---
    aprovadas = sum(1 for _codigo, _desc, marcador, _d in resultados
                    if marcador == "PASS")
    reprovadas = len(resultados) - aprovadas
    print("\n" + "=" * 78)
    print("RESUMO DA HOMOLOGAÇÃO")
    print("=" * 78)
    for codigo, descricao, marcador, detalhe in resultados:
        print(f"  {marcador}  {codigo}  {descricao}"
              + (f"  [{detalhe}]" if detalhe else ""))
    print("-" * 78)
    print(f"Total: {len(resultados)} | Aprovadas: {aprovadas} | "
          f"Reprovadas: {reprovadas}")
    if reprovadas:
        print("\nRESULTADO: HOMOLOGAÇÃO REPROVADA - "
              "corrigir pendências antes do piloto.")
    else:
        print("\nRESULTADO: HOMOLOGAÇÃO APROVADA nos critérios automatizáveis.")
    return 0 if reprovadas == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
