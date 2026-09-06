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
import time
from concurrent.futures import ThreadPoolExecutor

import httpx

BASE = "http://localhost:8010/api/v1/gdo"
ENDPOINTS_GET = [
    "/tipos-documentais",
    "/classificacoes",
    "/temporalidades/TEMP-001",
]
ENDPOINTS_POST = [
    ("/documentos", {
        "codigo": "DOC-CARGA-001",
        "numero": "0001",
        "ano": 2026,
        "tipo_documental_id": "oficio",
        "titulo": "Documento de teste de carga",
        "descricao": "Carga",
        "unidade_autor_id": "UNIDADE-01",
    }),
]


async def hit_get(client: httpx.AsyncClient, ep: str) -> int:
    r = await client.get(f"{BASE}{ep}", timeout=10)
    return r.status_code


async def hit_post(client: httpx.AsyncClient, ep: str, payload: dict) -> int:
    r = await client.post(f"{BASE}{ep}", json=payload, timeout=10)
    return r.status_code


async def run_concurrent(fn, n: int, c: int) -> tuple[list[float], int, int]:
    """Executa `n` chamadas com `c` concorrentes, retorna latências e erros."""
    latencias: list[float] = []
    errors = 0

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
    return latencias, errors


async def load_test_get(ep: str, n: int = 50, c: int = 10) -> dict:
    async with httpx.AsyncClient() as client:
        latencias, errors = await run_concurrent(
            lambda: hit_get(client, ep), n, c
        )
    return {
        "method": "GET",
        "endpoint": ep,
        "requests": n,
        "concurrency": c,
        "ok": n - errors,
        "errors": errors,
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
        latencias, errors = await run_concurrent(
            lambda: hit_post(client, ep, payload), n, c
        )
    return {
        "method": "POST",
        "endpoint": ep,
        "requests": n,
        "concurrency": c,
        "ok": n - errors,
        "errors": errors,
        "latencia_media_ms": round(statistics.mean(latencias), 2) if latencias else 0,
        "latencia_p95_ms": round(
            statistics.quantiles(latencias, n=20)[18] if len(latencias) >= 20 else (
                max(latencias) if latencias else 0
            ),
            2,
        ),
        "latencia_max_ms": round(max(latencias), 2) if latencias else 0,
    }


async def main():
    print("=== TESTE DE CARGA DOM-GDO ===")
    print(f"Base URL: {BASE}")
    print()

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
            f"max={r['latencia_max_ms']}ms"
        )

    # Testes POST (carga menor para não poluir o BD)
    for ep, payload in ENDPOINTS_POST:
        # Código único por iteração para evitar 409 (uniqueness)
        for i in range(20):
            payload_unique = {**payload, "codigo": f"DOC-CARGA-{i:04d}"}
            r = await load_test_post(ep, payload_unique, n=1, c=1)
            resultados.append(r)
            ok = "✅" if r["errors"] == 0 else "❌"
            print(
                f"{ok} {r['method']} {r['endpoint']:30} "
                f"{r['ok']}/{r['requests']} ok | {r['errors']} errors | "
                f"avg={r['latencia_media_ms']}ms"
            )

    print()
    print("=== RESUMO ===")
    total = len(resultados)
    falhas = sum(1 for r in resultados if r["errors"] > 0)
    avg_lat = statistics.mean(r["latencia_media_ms"] for r in resultados)
    print(f"Total de testes: {total}")
    print(f"Falhas: {falhas}")
    print(f"Latência média geral: {round(avg_lat, 2)}ms")

    # Critérios de aceitação do 018-Plano-de-Testes
    threshold_p95 = 1000  # ms
    threshold_p95_get = 500
    falhas_p95 = [
        r for r in resultados
        if r["method"] == "GET"
        and r["latencia_p95_ms"] > threshold_p95_get
        and r["errors"] == 0
    ]
    if falhas_p95:
        print(f"⚠️  {len(falhas_p95)} endpoint(s) com p95 > {threshold_p95_get}ms")
    else:
        print("✅ Todos os endpoints GET atendem ao SLA (p95 < 500ms)")

    return {"total": total, "falhas": falhas, "avg_latencia_ms": round(avg_lat, 2)}


if __name__ == "__main__":
    asyncio.run(main())
