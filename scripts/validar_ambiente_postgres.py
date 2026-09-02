"""Validação do ambiente de homologação com PostgreSQL real (docker-compose).

Sobe a aplicação FastAPI REAL (sem overrides de dependência), apontando para
o PostgreSQL do docker-compose (localhost:5433), semeia os dados de apoio do
núcleo corporativo (unidade, pessoa jurídica, processo documental) e exercita
o ciclo de negócio completo pela API, verificando a gravação física:

  fornecedor -> compra -> homologação -> formalização -> auditoria

Uso:  .venv/bin/python scripts/validar_ambiente_postgres.py
"""

from __future__ import annotations

import sys
import threading
import time
from pathlib import Path
from uuid import UUID

import httpx
import psycopg2
import psycopg2.extras
import uvicorn

psycopg2.extras.register_uuid()

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

PORTA = 8766
BASE = f"http://127.0.0.1:{PORTA}"

# IDs fixos de semeadura (idempotente entre execuções).
UNIDADE_ID = UUID("00000000-0000-0000-0000-00000000c001")
PESSOA_ID = UUID("00000000-0000-0000-0000-00000000c002")
PJ_ID = UUID("00000000-0000-0000-0000-00000000c003")
PROCESSO_ID = UUID("00000000-0000-0000-0000-00000000c004")
USUARIO_ID = UUID("00000000-0000-0000-0000-00000000c0ff")

OPERADOR = {"X-Usuario-Id": str(USUARIO_ID), "X-Usuario-Papel": "operador_compras"}
AUDITOR = {"X-Usuario-Id": str(USUARIO_ID), "X-Usuario-Papel": "auditor"}

resultados: list[tuple[str, bool, str]] = []


def verificar(codigo: str, condicao: bool, detalhe: str = "") -> bool:
    marcador = "PASS" if condicao else "FAIL"
    resultados.append((codigo, bool(condicao), detalhe))
    linha = f"  [{marcador}] {codigo}"
    if detalhe:
        linha += f" - {detalhe}"
    print(linha)
    return bool(condicao)


def conectar_pg():
    return psycopg2.connect(
        host="localhost", port=5433, dbname="sigmun", user="sigmun", password="sigmun"
    )


def semear() -> None:
    """Semeia dados de apoio do núcleo corporativo (idempotente)."""
    conn = conectar_pg()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("DELETE FROM compras.contratos WHERE processo_documental_id = %s", (PROCESSO_ID,))
            cur.execute("DELETE FROM compras.itens_compras WHERE compra_id IN "
                        "(SELECT id FROM compras.compras WHERE processo_documental_id = %s)", (PROCESSO_ID,))
            cur.execute("DELETE FROM compras.compras WHERE processo_documental_id = %s", (PROCESSO_ID,))
            cur.execute("DELETE FROM core.fornecedores WHERE pessoa_juridica_id = %s", (PJ_ID,))
            cur.execute("DELETE FROM core.processos_documentais WHERE id = %s", (PROCESSO_ID,))
            cur.execute("DELETE FROM core.pessoas_juridicas WHERE id = %s", (PJ_ID,))
            cur.execute("DELETE FROM core.pessoas WHERE id = %s", (PESSOA_ID,))
            cur.execute("DELETE FROM core.unidades_administrativas WHERE id = %s", (UNIDADE_ID,))

            cur.execute(
                "INSERT INTO core.unidades_administrativas (id, nome, sigla) "
                "VALUES (%s, %s, %s)",
                (UNIDADE_ID, "Secretaria Municipal de Administração", "SMAD"),
            )
            cur.execute(
                "INSERT INTO core.pessoas (id, tipo, categoria, unidade_id) "
                "VALUES (%s, 'JURIDICA', 'FORNECEDOR', %s)",
                (PESSOA_ID, UNIDADE_ID),
            )
            cur.execute(
                "INSERT INTO core.pessoas_juridicas (id, pessoa_id, razao_social) "
                "VALUES (%s, %s, %s)",
                (PJ_ID, PESSOA_ID, "Empresa de Homologação LTDA"),
            )
            cur.execute(
                "INSERT INTO core.processos_documentais (id, unidade_id, numero, ano, assunto) "
                "VALUES (%s, %s, %s, %s, %s)",
                (PROCESSO_ID, UNIDADE_ID, "SMOKE-001", 2026, "Validação do ambiente de homologação"),
            )
    finally:
        conn.close()


def consultar_valor(sql: str, params=()):
    conn = conectar_pg()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    finally:
        conn.close()


def subir_app() -> uvicorn.Server:
    """Sobe a aplicação real (composição padrão, sem overrides)."""
    from src.main import app  # noqa: PLC0415 – import tardio após semear ambiente

    config = uvicorn.Config(app, host="127.0.0.1", port=PORTA, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    for _ in range(100):
        if server.started:
            break
        time.sleep(0.2)
    else:
        raise RuntimeError("Aplicação não iniciou em tempo hábil")
    return server


def executar() -> None:
    with httpx.Client(base_url=BASE, timeout=30) as http:
        print("--- A. Infraestrutura ---")
        r = http.get("/health")
        verificar("PG-01", r.status_code == 200, f"GET /health -> HTTP {r.status_code}")

        print("--- B. Fornecedor persistido no PostgreSQL (core.fornecedores) ---")
        r = http.post(
            "/api/v1/fornecedores",
            json={"pessoa_juridica_id": str(PJ_ID), "situacao_cadastro": "ATIVO"},
            headers=OPERADOR,
        )
        fornecedor_criado = r.status_code == 201
        verificar("PG-02", fornecedor_criado, f"POST /fornecedores -> HTTP {r.status_code}")
        if not fornecedor_criado:
            print(r.text)
            return
        fornecedor_id = r.json()["id"]
        row = consultar_valor(
            "SELECT situacao_cadastro FROM core.fornecedores WHERE id = %s", (fornecedor_id,)
        )
        verificar("PG-03", row is not None and row[0] == "ATIVO",
                  f"Linha física em core.fornecedores "
                  f"(situacao_cadastro={row[0] if row else None})")

        print("--- C. Compra persistida no PostgreSQL (compras.compras) ---")
        r = http.post(
            "/api/v1/compras",
            json={
                "processo_documental_id": str(PROCESSO_ID),
                "fornecedor_id": fornecedor_id,
                "unidade_id": str(UNIDADE_ID),
                "numero": "SMOKE-001",
                "valor_total": "150000.00",
            },
            headers=OPERADOR,
        )
        compra_ok = r.status_code == 201
        verificar("PG-04", compra_ok, f"POST /compras -> HTTP {r.status_code}")
        if not compra_ok:
            print(r.text)
            return
        compra_id = r.json()["id"]

        for etapa in ("EM_INSTRUCAO", "EM_ANALISE", "EM_PROCEDIMENTO",
                      "EM_JULGAMENTO", "HOMOLOGADO"):
            r = http.patch(
                f"/api/v1/compras/{compra_id}/situacao",
                json={"situacao": etapa},
                headers=OPERADOR,
            )
            if not verificar(f"PG-05.{etapa}", r.status_code == 200,
                             f"Transição -> {etapa} -> HTTP {r.status_code}"):
                print(r.text)
                return

        print("--- D. Formalização e integridade referencial ---")
        r = http.post(
            "/api/v1/contratos/formalizar",
            params={"compra_id": compra_id},
            json={
                "numero": "CT-SMOKE-001/2026",
                "data_inicio": "2026-01-01",
                "data_fim": "2026-12-31",
                "valor": "150000.00",
                "objeto": "Objeto da validação do ambiente",
            },
            headers=OPERADOR,
        )
        formalizou = r.status_code == 201
        verificar("PG-06", formalizou, f"POST /contratos/formalizar -> HTTP {r.status_code}")
        if not formalizou:
            print(r.text)
            return
        contrato_id = r.json()["id"]

        row = consultar_valor("SELECT situacao FROM compras.compras WHERE id = %s", (compra_id,))
        verificar("PG-07", row is not None and row[0] == "CONTRATADO",
                  f"compras.compras.situacao={row[0] if row else None} (esperado CONTRATADO)")

        row = consultar_valor(
            "SELECT numero, compra_id FROM compras.contratos WHERE id = %s", (contrato_id,)
        )
        verificar("PG-08",
                  row is not None and row[0] == "CT-SMOKE-001/2026" and str(row[1]) == compra_id,
                  f"compras.contratos: numero={row[0] if row else None}, compra_id vinculado")

        row = consultar_valor("SELECT count(*) FROM auditoria.eventos")
        verificar("PG-09", row is not None and row[0] >= 5,
                  f"auditoria.eventos contém {row[0] if row else 0} eventos da trilha")

        print("--- E. Soft-delete verificado no banco (RN-COMPRAS-004) ---")
        r = http.delete(f"/api/v1/contratos/{contrato_id}", headers=OPERADOR)
        verificar("PG-10", r.status_code == 200, f"DELETE /contratos/{{id}} -> HTTP {r.status_code}")
        r = http.get(f"/api/v1/contratos/{contrato_id}")
        verificar("PG-11", r.status_code == 404, f"GET após exclusão -> HTTP {r.status_code}")
        row = consultar_valor(
            "SELECT deleted_at IS NOT NULL FROM compras.contratos WHERE id = %s", (contrato_id,)
        )
        verificar("PG-12", row is not None and row[0] is True,
                  "compras.contratos.deleted_at preenchido (histórico preservado)")


def main() -> int:
    print("=" * 78)
    print("VALIDAÇÃO DO AMBIENTE - PostgreSQL real (docker-compose) + aplicação real")
    print("=" * 78)

    try:
        conectar_pg().close()
    except Exception as exc:  # noqa: BLE001
        print(f"PostgreSQL indisponível em localhost:5433: {exc}")
        return 2

    semear()
    server = subir_app()
    try:
        executar()
    finally:
        server.should_exit = True
        time.sleep(1.0)

    aprovadas = sum(1 for _, ok, _ in resultados if ok)
    total = len(resultados)
    print("-" * 78)
    print(f"Total: {total} | Aprovadas: {aprovadas} | Reprovadas: {total - aprovadas}")
    return 0 if aprovadas == total else 1


if __name__ == "__main__":
    sys.exit(main())
