#!/usr/bin/env python3
"""
Script de Avaliação de Performance do SIGMUN.
Referência: Pendência P-006 (Seção 41 do Checklist de Prontidão)
"""

import argparse
import asyncio
import logging
import os
import statistics
import sys
import time
from dataclasses import dataclass, field
from typing import Optional

import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = os.getenv("SIGMUN_API_URL", "http://localhost:8000")
DEFAULT_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "30"))


@dataclass
class PerformanceResult:
    endpoint: str
    method: str
    total_requests: int = 0
    successful: int = 0
    failed: int = 0
    latencies: list[float] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def avg_latency(self) -> float:
        return statistics.mean(self.latencies) if self.latencies else 0

    @property
    def p50_latency(self) -> float:
        return statistics.median(self.latencies) if self.latencies else 0

    @property
    def p95_latency(self) -> float:
        if not self.latencies:
            return 0
        s = sorted(self.latencies)
        return s[min(int(len(s) * 0.95), len(s) - 1)]

    @property
    def p99_latency(self) -> float:
        if not self.latencies:
            return 0
        s = sorted(self.latencies)
        return s[min(int(len(s) * 0.99), len(s) - 1)]

    @property
    def rps(self) -> float:
        return self.total_requests / sum(self.latencies) if self.latencies else 0


async def make_request(client, method, endpoint, data=None):
    url = f"{BASE_URL}{endpoint}"
    start = time.monotonic()
    try:
        if method.upper() == "GET":
            resp = await client.get(url, timeout=DEFAULT_TIMEOUT)
        elif method.upper() == "POST":
            resp = await client.post(url, json=data, timeout=DEFAULT_TIMEOUT)
        else:
            return False, 0, f"Metodo nao suportado: {method}"
        latency = time.monotonic() - start
        ok = 200 <= resp.status_code < 500
        return ok, latency, None if ok else f"HTTP {resp.status_code}"
    except Exception as e:
        return False, time.monotonic() - start, str(e)


async def run_endpoint_test(endpoint, method="GET", total=100, concurrency=10, data=None):
    result = PerformanceResult(endpoint=endpoint, method=method)
    sem = asyncio.Semaphore(concurrency)

    async def bounded(client):
        async with sem:
            return await make_request(client, method, endpoint, data)

    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(*[bounded(client) for _ in range(total)])

    for ok, lat, err in results:
        result.total_requests += 1
        result.latencies.append(lat)
        if ok:
            result.successful += 1
        else:
            result.failed += 1
            if err:
                result.errors.append(err)
    return result


def print_result(r):
    print(f"\nEndpoint: {r.method} {r.endpoint}")
    print(f"  Total: {r.total_requests} | Sucesso: {r.successful} | Falha: {r.failed}")
    print(f"  Latencia media: {r.avg_latency*1000:.2f}ms | p50: {r.p50_latency*1000:.2f}ms")
    print(f"  p95: {r.p95_latency*1000:.2f}ms | p99: {r.p99_latency*1000:.2f}ms")
    print(f"  RPS: {r.rps:.2f}")


async def run_full_test(req_per_ep=50, concurrency=5):
    print("=" * 60)
    print("TESTE DE PERFORMANCE - SIGMUN API")
    print(f"URL: {BASE_URL}")
    print("=" * 60)

    endpoints = [
        ("/health", "GET", None),
        ("/", "GET", None),
        ("/api/v1/fornecedores?page=1&page_size=10", "GET", None),
        ("/api/v1/itens?page=1&page_size=10", "GET", None),
        ("/api/v1/compras?page=1&page_size=10", "GET", None),
        ("/api/v1/contratos?page=1&page_size=10", "GET", None),
    ]

    all_results = []
    for ep, method, data in endpoints:
        r = await run_endpoint_test(ep, method, req_per_ep, concurrency, data)
        print_result(r)
        all_results.append(r)

    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    total = sum(r.total_requests for r in all_results)
    success = sum(r.successful for r in all_results)
    failed = sum(r.failed for r in all_results)
    lats = [l for r in all_results for l in r.latencies]
    print(f"Total: {total} | Sucesso: {success} | Falha: {failed}")
    if lats:
        print(f"Latencia media global: {statistics.mean(lats)*1000:.2f}ms")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Teste de Performance SIGMUN")
    parser.add_argument("--requests", type=int, default=50)
    parser.add_argument("--concurrency", type=int, default=5)
    parser.add_argument("--url", type=str)
    args = parser.parse_args()
    if args.url:
        BASE_URL = args.url
    asyncio.run(run_full_test(args.requests, args.concurrency))
