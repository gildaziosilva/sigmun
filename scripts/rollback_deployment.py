#!/usr/bin/env python3
"""
Script de Rollback de Implantação do SIGMUN.

Procedimento de reversão para ambiente controlado.
Permite rollback de:
- Código (versão anterior via git)
- Banco de dados (downgrade de migrações)
- Configuração (restauração de .env anterior)

Referência: Pendência P-005 (Seção 41 do Checklist de Prontidão)
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(os.getenv("SIGMUN_ROOT", "."))
ALEMBIC_INI = PROJECT_ROOT / "alembic.ini"
BACKUP_DIR = Path(os.getenv("BACKUP_DIR", "/var/backups/sigmun"))


def run_command(cmd: list[str], cwd: Path = None) -> tuple[bool, str]:
    """Executa um comando e retorna (sucesso, output)."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd or PROJECT_ROOT,
            capture_output=True, text=True,
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def get_current_version() -> str:
    """Obtém a versão atual da aplicação via git tag ou commit."""
    success, output = run_command(["git", "describe", "--tags", "--always"])
    return output.strip() if success else "desconhecida"


def get_current_migration() -> str:
    """Obtém a migration atual do banco de dados."""
    success, output = run_command([
        "python", "-m", "alembic", "current", "-c", str(ALEMBIC_INI),
    ])
    return output.strip() if success else "desconhecida"


def rollback_code(target_version: str) -> bool:
    """Faz rollback do código para uma versão anterior."""
    logger.info(f"Iniciando rollback de código para: {target_version}")
    success, _ = run_command(["git", "rev-parse", target_version])
    if not success:
        logger.error(f"Versão {target_version} não encontrada")
        return False
    run_command(["git", "checkout", "-b", f"rollback-{target_version}"])
    success, output = run_command(["git", "checkout", target_version])
    if not success:
        logger.error(f"Erro no checkout: {output}")
        return False
    logger.info(f"Código revertido para: {target_version}")
    return True


def rollback_database(steps: int = 1) -> bool:
    """Faz rollback de migrações do banco de dados."""
    logger.info(f"Iniciando rollback de {steps} migração(ões)")
    current = get_current_migration()
    logger.info(f"Migration atual: {current}")
    success, output = run_command([
        "python", "-m", "alembic", "downgrade", f"-{steps}",
        "-c", str(ALEMBIC_INI),
    ])
    if not success:
        logger.error(f"Erro no rollback do banco: {output}")
        return False
    new_current = get_current_migration()
    logger.info(f"Nova migration: {new_current}")
    logger.info("Rollback do banco concluído com sucesso")
    return True


def rollback_full(target_version: str, db_steps: int = 1) -> bool:
    """Executa rollback completo (código + banco)."""
    logger.info("=" * 60)
    logger.info("INICIANDO ROLLBACK COMPLETO DO SIGMUN")
    logger.info("=" * 60)
    logger.info("Verificando backup disponível...")
    backups = sorted(BACKUP_DIR.glob("sigmun_backup_*.sql.gz"))
    if backups:
        latest = backups[-1]
        size = latest.stat().st_size / 1024 / 1024
        logger.info(f"Último backup: {latest.name} ({size:.2f} MB)")
    else:
        logger.warning("NENHUM BACKUP DISPONÍVEL")
    if db_steps > 0:
        if not rollback_database(db_steps):
            return False
    if not rollback_code(target_version):
        return False
    logger.info("ROLLBACK CONCLUÍDO - Reinicie os serviços")
    return True


def list_rollback_points() -> None:
    """Lista pontos de rollback disponíveis."""
    success, output = run_command(["git", "tag", "-l", "--sort=-version:refname"])
    if success:
        tags = [t for t in output.strip().split("\n") if t]
        print("Tags disponíveis:")
        for tag in tags[:10]:
            print(f"  - {tag}")
    success, output = run_command([
        "python", "-m", "alembic", "history", "-c", str(ALEMBIC_INI),
    ])
    if success:
        print("\nHistórico de migrações:")
        print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rollback de implantação SIGMUN")
    parser.add_argument("--code", type=str, help="Versão do código para rollback")
    parser.add_argument("--db-steps", type=int, default=1, help="Migrações a reverter")
    parser.add_argument("--full", type=str, help="Rollback completo para versão")
    parser.add_argument("--list", action="store_true", help="Lista pontos de rollback")
    args = parser.parse_args()
    if args.list:
        list_rollback_points()
        sys.exit(0)
    if args.full:
        success = rollback_full(args.full, args.db_steps)
    elif args.code:
        success = rollback_code(args.code)
    elif args.db_steps:
        success = rollback_database(args.db_steps)
    else:
        parser.print_help()
        sys.exit(1)
    sys.exit(0 if success else 1)
