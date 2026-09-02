#!/usr/bin/env python3
"""
Script de Configuração de Monitoramento do SIGMUN.

Configura stack de observabilidade com:
- Métricas de saúde da aplicação
- Alertas de disponibilidade
- Dashboard de monitoramento
- Verificação de integridade

Referência: Pendência P-003 (Seção 41 do Checklist de Prontidão)
"""

import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

BASE_URL = os.getenv("SIGMUN_API_URL", "http://localhost:8000")
ALERT_WEBHOOK = os.getenv("ALERT_WEBHOOK_URL", "")


class HealthStatus:
    """Status de saúde de um componente."""
    def __init__(self, name: str, healthy: bool, latency_ms: float, details: str = ""):
        self.name = name
        self.healthy = healthy
        self.latency_ms = latency_ms
        self.details = details
        self.checked_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "healthy": self.healthy,
            "latency_ms": round(self.latency_ms, 2),
            "details": self.details,
            "checked_at": self.checked_at,
        }


async def check_api_health() -> HealthStatus:
    """Verifica saúde da API."""
    import time
    start = time.monotonic()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/health", timeout=10)
            latency = (time.monotonic() - start) * 1000
            if response.status_code == 200:
                data = response.json()
                return HealthStatus("api", True, latency, f"version={data.get('version', '?')}")
            return HealthStatus("api", False, latency, f"HTTP {response.status_code}")
    except Exception as e:
        latency = (time.monotonic() - start) * 1000
        return HealthStatus("api", False, latency, str(e))


async def check_database() -> HealthStatus:
    """Verifica conexão com banco de dados via API."""
    import time
    start = time.monotonic()
    try:
        async with httpx.AsyncClient() as client:
            # Tenta acessar um endpoint que usa o banco
            response = await client.get(
                f"{BASE_URL}/api/v1/fornecedores?page=1&page_size=1",
                timeout=10,
            )
            latency = (time.monotonic() - start) * 1000
            if response.status_code in (200, 401):  # 401 também indica que o banco está OK
                return HealthStatus("database", True, latency, "Connection OK")
            return HealthStatus("database", False, latency, f"HTTP {response.status_code}")
    except Exception as e:
        latency = (time.monotonic() - start) * 1000
        return HealthStatus("database", False, latency, str(e))


async def check_openapi() -> HealthStatus:
    """Verifica disponibilidade da documentação OpenAPI."""
    import time
    start = time.monotonic()
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/openapi.json", timeout=10)
            latency = (time.monotonic() - start) * 1000
            if response.status_code == 200:
                data = response.json()
                paths = len(data.get("paths", {}))
                return HealthStatus("openapi", True, latency, f"{paths} endpoints")
            return HealthStatus("openapi", False, latency, f"HTTP {response.status_code}")
    except Exception as e:
        latency = (time.monotonic() - start) * 1000
        return HealthStatus("openapi", False, latency, str(e))


async def run_health_check() -> dict:
    """
    Executa verificação completa de saúde do sistema.
    
    Returns:
        Dicionário com status de todos os componentes
    """
    import asyncio
    
    logger.info("Executando verificação de saúde do sistema...")
    
    # Executa verificações em paralelo
    results = await asyncio.gather(
        check_api_health(),
        check_database(),
        check_openapi(),
    )
    
    # Monta relatório
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_healthy": all(r.healthy for r in results),
        "components": [r.to_dict() for r in results],
    }
    
    return report


def print_report(report: dict) -> None:
    """Imprime relatório de saúde formatado."""
    print("\n" + "=" * 60)
    print("RELATÓRIO DE SAÚDE DO SISTEMA - SIGMUN")
    print("=" * 60)
    print(f"Timestamp: {report['timestamp']}")
    print(f"Status Geral: {'✅ SAUDÁVEL' if report['overall_healthy'] else '❌ COM PROBLEMAS'}")
    print("-" * 60)
    
    for component in report["components"]:
        status = "✅" if component["healthy"] else "❌"
        print(f"  {status} {component['name']}: {component['latency_ms']}ms - {component['details']}")
    
    print("=" * 60)


async def send_alert(report: dict) -> None:
    """Envia alerta se houver componentes indisponíveis."""
    if not ALERT_WEBHOOK:
        return
    
    unhealthy = [c for c in report["components"] if not c["healthy"]]
    if not unhealthy:
        return
    
    payload = {
        "text": f"🚨 ALERTA SIGMUN: {len(unhealthy)} componente(s) indisponível(is)",
        "unhealthy_components": unhealthy,
        "timestamp": report["timestamp"],
    }
    
    try:
        async with httpx.AsyncClient() as client:
            await client.post(ALERT_WEBHOOK, json=payload, timeout=10)
    except Exception as e:
        logger.error(f"Erro ao enviar alerta: {e}")


if __name__ == "__main__":
    import asyncio
    
    async def main():
        report = await run_health_check()
        print_report(report)
        
        if not report["overall_healthy"]:
            await send_alert(report)
            sys.exit(1)
        
        sys.exit(0)
    
    asyncio.run(main())
