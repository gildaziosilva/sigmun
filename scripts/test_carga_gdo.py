"""Teste de carga para os endpoints do DOM-GDO.

Executa requisições concorrentes usando httpx.AsyncClient + threading,
validando performance e estabilidade dos endpoints de tipos, classificações,
processos e temporalidades.

Uso:
    .venv/bin/python scripts/test_carga_gdo.py
"""

from __future__ import annotations

import asyncio
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "SIGMUN-Docs" / "DOM-GDO" / "evidencias"

BASE = "http://localhost:8010/api/v1/gdo"
ENDPOINTS_GET = [
    "/tipos-documentais",
    "/classificacoes",
    "/temporalidades/TEMP-001",
]
# Payload alinhado ao seed real do DOM-GDO (código TD-OFICIO e unidade SECADM-01).
ENDPOINTS_POST = [
    ("/documentos", {
        "codigo": "DOC-CARGA-001",
        "numero": "0001",
        "ano": 2026,
        "tipo_documental_id": "TD-OFICIO",
        "titulo": "Documento de teste de carga",
        "descricao": "Carga",
        "unidade_autor_id": "SECADM-01",
    }),
]


async def hit_get(client: httpx.AsyncClient, ep: str) -> int:
    r = await client.get(f"{BASE}{ep}", timeout=10)
    return r.status_code


async def hit_post(client: httpx.AsyncClient, ep: str, payload: dict) -> int:
    r = await client.post(f"{BASE}{ep}", json=payload, timeout=10)
    return r.status_code


async def run_concurrent(fn, n: int, c: int) -> tuple[list[float], int, float]:
    """Executa `n` chamadas com `c` concorrentes, retorna latências, erros e duração."""
    latencias: list[float] = []
    errors = 0
    t0 = time.perf_counter()

    sem = asyncio.Semaphore(c)

    async def guarded():
        nonlocal errors
        async with sem:
            start = time.perf_counter()
            try:
                status = await fn()
                lat = (time.perf_counter() - start) * 1000
                if 200 <= status < 300:
                    latencias.append(lat)
                else:
                    errors += 1
            except Exception:
                errors += 1
            await asyncio.sleep(0)

    await asyncio.gather(*(guarded() for _ in range(n)))
    duracao = time.perf_counter() - t0
    return latencias, errors, duracao


async def load_test_get(ep: str, n: int = 50, c: int = 10) -> dict:
    async with httpx.AsyncClient() as client:
        latencias, errors, duracao = await run_concurrent(
            lambda: hit_get(client, ep), n, c
        )
    return {
        "method": "GET",
        "endpoint": ep,
        "requests": n,
        "concurrency": c,
        "ok": n - errors,
        "errors": errors,
        "throughput_rps": round(n / duracao, 2) if duracao else 0,
        "latencia_media_ms": round(statistics.mean(latencias), 2) if latencias else 0,
        "latencia_p95_ms": round(
            statistics.quantiles(latencias, n=20)[18] if len(latencias) >= 20 else (
                max(latencias) if latencias else 0
            ),
            2,
        ),
        "latencia_max_ms": round(max(latencias), 2) if latencias else 0,
    }


async def load_test_post(ep: str, payload: dict, n: int = 20, c: int = 5) -> dict:
    async with httpx.AsyncClient() as client:
        latencias, errors, duracao = await run_concurrent(
            lambda: hit_post(client, ep, payload), n, c
        )
    return {
        "method": "POST",
        "endpoint": ep,
        "requests": n,
        "concurrency": c,
        "ok": n - errors,
        "errors": errors,
        "throughput_rps": round(n / duracao, 2) if duracao else 0,
        "latencia_media_ms": round(statistics.mean(latencias), 2) if latencias else 0,
        "latencia_p95_ms": round(
            statistics.quantiles(latencias, n=20)[18] if len(latencias) >= 20 else (
                max(latencias) if latencias else 0
            ),
            2,
        ),
        "latencia_max_ms": round(max(latencias), 2) if latencias else 0,
    }


def gerar_evidencia(
    resultados: list[dict],
    duracao_total_s: float,
    sucesso: bool,
    falhas_p95: list[dict],
) -> Path:
    """Grava evidência do teste de carga em SIGMUN-Docs/DOM-GDO/evidencias/."""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    agora = datetime.now()
    arquivo = EVIDENCE_DIR / f"{agora.strftime('%Y-%m-%d')}-teste-carga-gdo.md"
    avg_lat = round(statistics.mean(r["latencia_media_ms"] for r in resultados), 2)
    linhas = [
        "# Evidência de Teste de Carga — DOM-GDO (Gestão Documental)",
        "",
        "**Domínio:** DOM-GDO — Gestão Documental",
        f"**Data:** {agora.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Duração total:** {duracao_total_s:.2f}s",
        f"**Base URL:** {BASE}",
        f"**Resultado:** {'SUCESSO' if sucesso else 'FALHA'}",
        "",
        "## Resultados por endpoint",
        "",
        "| Método | Endpoint | Requisições | OK | Erros | Lat. média (ms) | p95 (ms) | Máx "
        "(ms) | Throughput (req/s) |",
        "|--------|----------|-------------|----|-------|-----------------|----------|-----"
        "-----|--------------------|",
    ]
    for r in resultados:
        linhas.append(
            f"| {r['method']} | {r['endpoint']} | {r['requests']} | {r['ok']} | "
            f"{r['errors']} | {r['latencia_media_ms']} | {r['latencia_p95_ms']} | "
            f"{r['latencia_max_ms']} | {r.get('throughput_rps', '-')} |"
        )
    linhas += [
        "",
        f"**Latência média geral:** {avg_lat}ms",
        f"**Total de testes:** {len(resultados)} | **Falhas:** "
        + str(sum(1 for r in resultados if r['errors'] > 0)),
        "",
        "## Critérios de aceitação (018-Plano-de-Testes)",
        "",
        "- SLA GET p95 < 500ms: "
        + ("CUMPRIDO" if not falhas_p95 else f"INCUMPRIDO ({len(falhas_p95)} endpoints)"),
        "- Erros HTTP: " + ("0" if sucesso else "presentes"),
        "",
        "---",
        "",
        "**Documento:** " + arquivo.name,
        "**Última atualização:** " + agora.strftime('%Y-%m-%d'),
        "**Responsável:** Equipe SIGMUN",
        "**Status:** " + ("Concluído" if sucesso else "Pendente"),
        "",
    ]
    arquivo.write_text("\n".join(linhas), encoding="utf-8")
    return arquivo


async def main():
    print("=== TESTE DE CARGA DOM-GDO ===")
    print(f"Base URL: {BASE}")
    print()

    inicio = time.perf_counter()
    resultados = []

    # Testes GET
    for ep in ENDPOINTS_GET:
        r = await load_test_get(ep)
        resultados.append(r)
        status = "✅" if r["errors"] == 0 else "❌"
        print(
            f"{status} {r['method']} {r['endpoint']:30} "
            f"{r['ok']}/{r['requests']} ok | {r['errors']} errors | "
            f"avg={r['latencia_media_ms']}ms p95={r['latencia_p95_ms']}ms "
            f"max={r['latencia_max_ms']}ms | {r['throughput_rps']} req/s"
        )

    # Testes POST (carga menor para não poluir o BD)
    # Sufixo por execução: garante códigos únicos entre corridas (evita 409).
    sufixo = int(time.time()) % 100000
    for ep, payload in ENDPOINTS_POST:
        # Código único por iteração para evitar 409 (uniqueness)
        for i in range(20):
            payload_unique = {**payload, "codigo": f"DOC-CARGA-{sufixo}-{i:04d}"}
            r = await load_test_post(ep, payload_unique, n=1, c=1)
            resultados.append(r)
            ok = "✅" if r["errors"] == 0 else "❌"
            print(
                f"{ok} {r['method']} {r['endpoint']:30} "
                f"{r['ok']}/{r['requests']} ok | {r['errors']} errors | "
                f"avg={r['latencia_media_ms']}ms"
            )

    duracao_total = time.perf_counter() - inicio

    print()
    print("=== RESUMO ===")
    total = len(resultados)
    falhas = sum(1 for r in resultados if r["errors"] > 0)
    avg_lat = statistics.mean(r["latencia_media_ms"] for r in resultados)
    print(f"Total de testes: {total}")
    print(f"Falhas: {falhas}")
    print(f"Latência média geral: {round(avg_lat, 2)}ms")
    print(f"Duração total: {duracao_total:.2f}s")

    # Critérios de aceitação do 018-Plano-de-Testes
    threshold_p95_get = 500
    falhas_p95 = [
        r for r in resultados
        if r["method"] == "GET"
        and r["latencia_p95_ms"] > threshold_p95_get
        and r["errors"] == 0
    ]
    sucesso = falhas == 0 and len(falhas_p95) == 0
    if falhas_p95:
        print(f"⚠️  {len(falhas_p95)} endpoint(s) com p95 > {threshold_p95_get}ms")
    else:
        print("✅ Todos os endpoints GET atendem ao SLA (p95 < 500ms)")

    arquivo = gerar_evidencia(resultados, duracao_total, sucesso, falhas_p95)
    print(f"Evidência gerada: {arquivo}")

    return {
        "total": total,
        "falhas": falhas,
        "avg_latencia_ms": round(avg_lat, 2),
        "resultado": "SUCESSO" if sucesso else "FALHA",
        "evidencia": str(arquivo),
    }


if __name__ == "__main__":
    resultado = asyncio.run(main())
    sys.exit(0 if resultado["resultado"] == "SUCESSO" else 1)
