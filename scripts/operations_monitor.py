#!/usr/bin/env python3
"""
Sistema de Monitoramento Operacional do SIGMUN.
Referencia: Item 20 do ROADMAP.md - Iniciar operacao monitorada
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = os.getenv("SIGMUN_API_URL", "http://localhost:8000")
MONITORING_INTERVAL = int(os.getenv("MONITORING_INTERVAL", "60"))
WEBHOOK_URL = os.getenv("ALERT_WEBHOOK_URL", "")
EVIDENCE_DIR = Path(__file__).parent.parent / "SIGMUN-Docs" / "DOM-COMPRAS-001" / "evidencias"
INCIDENT_LOG = EVIDENCE_DIR / "incidents.json"


class Incident:
    """Representa um incidente operacional."""
    def __init__(self, severity: str, component: str, description: str):
        self.id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.severity = severity
        self.component = component
        self.description = description
        self.status = "open"
        self.resolution = None
        self.resolved_at = None

    def to_dict(self) -> dict:
        return {
            "id": self.id, "timestamp": self.timestamp,
            "severity": self.severity, "component": self.component,
            "description": self.description, "status": self.status,
            "resolution": self.resolution, "resolved_at": self.resolved_at,
        }

    def resolve(self, resolution: str):
        self.status = "resolved"
        self.resolution = resolution
        self.resolved_at = datetime.now(timezone.utc).isoformat()


class OperationsManager:
    """Gerenciador de operacao monitorada."""
    def __init__(self):
        self.incidents: list[Incident] = []
        self.health_history: list[dict] = []
        self.consecutive_failures = 0
        self.max_failures_before_alert = 3

    def check_health(self) -> dict:
        """Verifica saude do sistema."""
        health = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "api": self._check_api(),
            "database": self._check_database(),
            "openapi": self._check_openapi(),
            "disk_space": self._check_disk_space(),
        }
        health["overall"] = all(
            v.get("healthy", False) for k, v in health.items()
            if k not in ["timestamp", "overall"]
        )
        return health

    def _check_api(self) -> dict:
        """Verifica saude da API."""
        try:
            req = urllib.request.Request(f"{BASE_URL}/health", method="GET")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                return {"healthy": resp.status == 200, "version": data.get("version", "unknown")}
        except Exception as e:
            return {"healthy": False, "error": str(e)}

    def _check_database(self) -> dict:
        """Verifica conexao com banco via API."""
        try:
            req = urllib.request.Request(f"{BASE_URL}/api/v1/fornecedores?page=1&page_size=1", method="GET")
            with urllib.request.urlopen(req, timeout=10) as resp:
                return {"healthy": resp.status in (200, 401, 403), "status_code": resp.status}
        except Exception as e:
            return {"healthy": False, "error": str(e)}

    def _check_openapi(self) -> dict:
        """Verifica disponibilidade do OpenAPI."""
        try:
            req = urllib.request.Request(f"{BASE_URL}/openapi.json", method="GET")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                return {"healthy": resp.status == 200, "endpoints": len(data.get("paths", {}))}
        except Exception as e:
            return {"healthy": False, "error": str(e)}

    def _check_disk_space(self) -> dict:
        """Verifica espaco em disco."""
        try:
            stat = os.statvfs("/")
            total = stat.f_blocks * stat.f_frsize
            free = stat.f_bfree * stat.f_frsize
            used_percent = ((total - free) / total) * 100
            return {"healthy": used_percent < 90, "used_percent": round(used_percent, 2)}
        except Exception:
            return {"healthy": True}

    def record_health(self, health: dict):
        """Registro historico de saude."""
        self.health_history.append(health)
        if len(self.health_history) > 1440:
            self.health_history = self.health_history[-1440:]

    def process_health_result(self, health: dict):
        """Processa resultado de saude e gera alertas."""
        self.record_health(health)
        if not health["overall"]:
            self.consecutive_failures += 1
            if self.consecutive_failures >= self.max_failures_before_alert:
                self._create_incident(health)
        else:
            if self.consecutive_failures >= self.max_failures_before_alert:
                self._resolve_incidents("Sistema recuperado")
            self.consecutive_failures = 0

    def _create_incident(self, health: dict):
        """Cria novo incidente."""
        unhealthy = [k for k, v in health.items()
                     if k not in ["timestamp", "overall"] and isinstance(v, dict) and not v.get("healthy", True)]
        incident = Incident(
            severity="high" if self.consecutive_failures > 5 else "medium",
            component=", ".join(unhealthy),
            description=f"Componentes indisponiveis apos {self.consecutive_failures} verificacoes",
        )
        self.incidents.append(incident)
        self._send_alert(incident)
        self._save_incidents()

    def _resolve_incidents(self, resolution: str):
        """Resolve incidentes abertos."""
        for incident in self.incidents:
            if incident.status == "open":
                incident.resolve(resolution)
        self._save_incidents()

    def _send_alert(self, incident: Incident):
        """Envia alerta de incidente."""
        logger.warning(f"ALERTA: Incidente {incident.id} - {incident.description}")
        if WEBHOOK_URL:
            try:
                payload = json.dumps({"text": f"SIGMUN Alerta: {incident.description}",
                                      "incident": incident.to_dict()}).encode()
                req = urllib.request.Request(WEBHOOK_URL, data=payload,
                                            headers={"Content-Type": "application/json"}, method="POST")
                urllib.request.urlopen(req, timeout=10)
            except Exception as e:
                logger.error(f"Erro ao enviar webhook: {e}")

    def _save_incidents(self):
        """Salva incidentes em arquivo."""
        EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
        data = [i.to_dict() for i in self.incidents[-100:]]
        INCIDENT_LOG.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    def run_backup(self) -> bool:
        """Executa backup do banco de dados."""
        logger.info("Executando backup operacional...")
        try:
            result = subprocess.run([sys.executable, "scripts/backup_postgres.py"],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                logger.info("Backup concluido com sucesso")
                return True
            else:
                logger.error(f"Falha no backup: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"Erro ao executar backup: {e}")
            return False

    def generate_dashboard(self) -> str:
        """Gera dashboard operacional."""
        now = datetime.now(timezone.utc)
        total_checks = len(self.health_history)
        healthy_checks = sum(1 for h in self.health_history if h.get("overall", False))
        uptime = (healthy_checks / total_checks * 100) if total_checks > 0 else 100
        open_inc = sum(1 for i in self.incidents if i.status == "open")
        resolved_inc = sum(1 for i in self.incidents if i.status == "resolved")

        dash = f"""
============================================================
DASHBOARD OPERACIONAL - SIGMUN DOM-COMPRAS-001
============================================================
Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}

DISPONIBILIDADE
  Uptime: {uptime:.2f}%
  Verificacoes: {total_checks}
  Saudaveis: {healthy_checks}
  Com falhas: {total_checks - healthy_checks}

INCIDENTES
  Abertos: {open_inc}
  Resolvidos: {resolved_inc}
  Total: {len(self.incidents)}
============================================================
"""
        return dash


def run_daemon(manager: OperationsManager, interval: int):
    """Executa monitoramento continuo."""
    logger.info(f"Iniciando monitoramento operacional (intervalo: {interval}s)")
    backup_counter = 0
    backup_interval = 1440 // interval

    while True:
        try:
            health = manager.check_health()
            manager.process_health_result(health)
            if health["overall"]:
                logger.info("Sistema saudavel")
            else:
                logger.warning("Sistema com problemas")

            backup_counter += 1
            if backup_counter >= backup_interval:
                manager.run_backup()
                backup_counter = 0
        except Exception as e:
            logger.error(f"Erro no monitoramento: {e}")
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Monitoramento Operacional SIGMUN")
    parser.add_argument("--daemon", action="store_true", help="Modo daemon")
    parser.add_argument("--interval", type=int, default=MONITORING_INTERVAL, help="Intervalo (s)")
    parser.add_argument("--backup", action="store_true", help="Executa backup")
    parser.add_argument("--dashboard", action="store_true", help="Exibe dashboard")
    args = parser.parse_args()

    manager = OperationsManager()

    if args.backup:
        success = manager.run_backup()
        return 0 if success else 1

    if args.dashboard or not args.daemon:
        health = manager.check_health()
        manager.record_health(health)
        print(manager.generate_dashboard())
        return 0 if health["overall"] else 1

    run_daemon(manager, args.interval)


if __name__ == "__main__":
    sys.exit(main())
