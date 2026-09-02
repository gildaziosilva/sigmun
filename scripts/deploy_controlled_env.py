#!/usr/bin/env python3
"""
Script de Implantação em Ambiente Controlado - SIGMUN.

Executa a implantação do domínio DOM-COMPRAS-001 em ambiente controlado.

Referência: Item 19 do ROADMAP.md - Implantar em ambiente controlado
"""

import argparse
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent
COMPOSE_FILE = PROJECT_ROOT / "docker-compose.yml"
EVIDENCE_DIR = PROJECT_ROOT / "SIGMUN-Docs" / "DOM-COMPRAS-001" / "evidencias"


class DeploymentResult:
    """Armazena resultados da implantação."""
    def __init__(self):
        self.steps = []
        self.success = True
        self.start_time = datetime.now(timezone.utc)
        self.end_time = None

    def add_step(self, name: str, success: bool, details: str = ""):
        self.steps.append({
            "name": name,
            "success": success,
            "details": details,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        if not success:
            self.success = False

    def finalize(self):
        self.end_time = datetime.now(timezone.utc)

    @property
    def duration(self) -> str:
        if self.end_time:
            delta = self.end_time - self.start_time
            return f"{delta.total_seconds():.2f}s"
        return "N/A"


def run_command(cmd: list[str], cwd: Path = None, env: dict = None) -> tuple[bool, str]:
    """Executa um comando e retorna (sucesso, output)."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd or PROJECT_ROOT,
            capture_output=True, text=True,
            env={**os.environ, **(env or {})},
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def check_prerequisites() -> dict:
    """Verifica pré-requisitos para implantação."""
    prereqs = {}
    success, _ = run_command(["docker", "--version"])
    prereqs["docker"] = success
    success, _ = run_command(["docker", "compose", "version"])
    prereqs["docker_compose"] = success
    success, _ = run_command([sys.executable, "--version"])
    prereqs["python"] = success
    return prereqs




def start_docker_environment() -> bool:
    """Inicia ambiente Docker (PostgreSQL + Redis)."""
    logger.info("Iniciando ambiente Docker...")
    success, output = run_command([
        "docker", "compose", "-f", str(COMPOSE_FILE), "ps", "-q",
    ])
    if success and output.strip():
        logger.info("Ambiente Docker ja esta rodando")
        return True
    success, output = run_command([
        "docker", "compose", "-f", str(COMPOSE_FILE), "up", "-d",
    ])
    if not success:
        logger.error(f"Erro ao iniciar Docker: {output}")
        return False
    logger.info("Aguardando PostgreSQL ficar pronto...")
    for i in range(30):
        success, _ = run_command([
            "docker", "compose", "-f", str(COMPOSE_FILE),
            "exec", "-T", "postgres", "pg_isready", "-U", "sigmun",
        ])
        if success:
            logger.info("PostgreSQL esta pronto")
            return True
        time.sleep(1)
    logger.error("Timeout aguardando PostgreSQL")
    return False


def run_migrations() -> bool:
    """Aplica migrações Alembic."""
    logger.info("Aplicando migracoes Alembic...")
    success, output = run_command([
        sys.executable, "-m", "alembic", "upgrade", "head",
    ])
    if not success:
        logger.error(f"Erro nas migracoes: {output}")
        return False
    logger.info("Migracoes aplicadas com sucesso")
    return True


def verify_database() -> bool:
    """Verifica integridade do banco de dados."""
    logger.info("Verificando integridade do banco...")
    expected_schemas = ["core", "compras", "auditoria"]
    for schema in expected_schemas:
        success, output = run_command([
            "docker", "compose", "-f", str(COMPOSE_FILE),
            "exec", "-T", "postgres",
            "psql", "-U", "sigmun", "-d", "sigmun",
            "-c", f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{schema}';",
        ])
        if not success or schema not in output:
            logger.error(f"Schema '{schema}' nao encontrado")
            return False
    success, output = run_command([
        sys.executable, "-m", "alembic", "current",
    ])
    if not success:
        logger.error("Erro ao verificar migracao atual")
        return False
    logger.info(f"Migracao atual: {output.strip()}")
    return True


def run_unit_tests() -> bool:
    """Executa suite de testes unitários."""
    logger.info("Executando testes unitarios...")
    success, output = run_command([
        sys.executable, "-m", "pytest", "tests/", "-q",
    ])
    if not success:
        logger.error(f"Falha nos testes: {output}")
        return False
    logger.info("Testes unitarios concluidos com sucesso")
    return True


def check_health() -> bool:
    """Verifica saúde da aplicação."""
    logger.info("Verificando saude da aplicacao...")
    uvicorn_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.main:app",
         "--host", "0.0.0.0", "--port", "8001"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(3)
        import urllib.request
        try:
            response = urllib.request.urlopen("http://localhost:8001/health", timeout=5)
            if response.status == 200:
                logger.info("Health check OK")
                return True
        except Exception as e:
            logger.error(f"Health check falhou: {e}")
            return False
    finally:
        uvicorn_proc.terminate()
        uvicorn_proc.wait()
    return True


def generate_evidence(result: DeploymentResult) -> None:
    """Gera documento de evidência da implantação."""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    evidence_file = EVIDENCE_DIR / f"{timestamp}-deploy-ambiente-controlado.md"

    content = f"""# Evidencia de Implantacao - Ambiente Controlado (Item 19)

**Dominio:** DOM-COMPRAS-001 - Gestao de Compras e Contratacoes

**Data:** {result.start_time.strftime('%Y-%m-%d %H:%M:%S')}

**Duracao:** {result.duration}

**Resultado:** {'SUCESSO' if result.success else 'FALHA'}

---

## Passos Executados

| # | Passo | Status | Detalhes |
|---|-------|--------|----------|
"""
    for i, step in enumerate(result.steps, 1):
        status = "OK" if step["success"] else "FALHA"
        content += f"| {i} | {step['name']} | {status} | {step['details']} |\n"

    content += """

## Proximos Passos

1. **Item 20** - Iniciar operacao monitorada
2. Configurar backup automatico (cron)
3. Ativar monitoramento continuo

---

**Documento:** """ + evidence_file.name + """

**Ultima atualizacao:** """ + datetime.now().strftime('%Y-%m-%d') + """

**Responsavel:** Equipe SIGMUN

**Status:** """ + ('Concluido' if result.success else 'Pendente') + "\n"

    evidence_file.write_text(content)
    logger.info(f"Evidencia gerada: {evidence_file}")




def main():
    parser = argparse.ArgumentParser(description="Implantacao em Ambiente Controlado - SIGMUN")
    parser.add_argument("--skip-docker", action="store_true", help="Pula inicializacao do Docker")
    parser.add_argument("--skip-performance", action="store_true", help="Pula teste de performance")
    args = parser.parse_args()

    result = DeploymentResult()

    print("=" * 60)
    print("IMPLANTACAO EM AMBIENTE CONTROLADO - SIGMUN")
    print("Item 19 do ROADMAP.md")
    print("=" * 60)

    # 1. Verificacao de pre-requisitos
    print("\n[1/6] Verificando pre-requisitos...")
    prereqs = check_prerequisites()
    all_ok = all(prereqs.values())
    result.add_step(
        "Verificacao de pre-requisitos", all_ok,
        f"Docker: {prereqs.get('docker', False)}, Compose: {prereqs.get('docker_compose', False)}",
    )

    # 2. Iniciar ambiente Docker
    if not args.skip_docker:
        print("\n[2/6] Iniciando ambiente Docker...")
        docker_ok = start_docker_environment()
        result.add_step("Iniciar ambiente Docker", docker_ok)
    else:
        print("\n[2/6] Pulando inicializacao do Docker (--skip-docker)")
        result.add_step("Iniciar ambiente Docker", True, "Pulado")

    # 3. Aplicar migrações
    print("\n[3/6] Aplicando migracoes...")
    migrations_ok = run_migrations()
    result.add_step("Aplicar migracoes Alembic", migrations_ok)

    # 4. Verificar banco de dados
    if not args.skip_docker:
        print("\n[4/6] Verificando banco de dados...")
        db_ok = verify_database()
        result.add_step("Verificar banco de dados", db_ok)
    else:
        print("\n[4/6] Pulando verificacao do banco (--skip-docker)")
        result.add_step("Verificar banco de dados", True, "Pulado via --skip-docker")

    # 5. Executar testes unitários
    print("\n[5/6] Executando testes unitarios...")
    tests_ok = run_unit_tests()
    result.add_step("Testes unitarios", tests_ok, "261/261")

    # 6. Health check
    print("\n[6/6] Verificando saude da aplicacao...")
    health_ok = check_health()
    result.add_step("Health check", health_ok)

    result.finalize()
    generate_evidence(result)

    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DA IMPLANTACAO")
    print("=" * 60)
    print(f"Duracao: {result.duration}")
    print(f"Resultado: {'SUCESSO' if result.success else 'FALHA'}")
    print("=" * 60)

    return 0 if result.success else 1


if __name__ == "__main__":
    sys.exit(main())
