#!/usr/bin/env python3
"""
Script de Backup do PostgreSQL para o SIGMUN.

Realiza backup completo do banco de dados com:
- Compressão gzip
- Retenção configurável
- Verificação de integridade
- Logging estruturado

Referência: Pendência P-004 (Seção 41 do Checklist de Prontidão)
"""

import argparse
import gzip
import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Configurações (via variáveis de ambiente)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "sigmun")
DB_USER = os.getenv("DB_USER", "sigmun")
DB_PASSWORD = os.getenv("DB_PASSWORD", "sigmun")
BACKUP_DIR = os.getenv("BACKUP_DIR", "/var/backups/sigmun")
RETENTION_DAYS = int(os.getenv("BACKUP_RETENTION_DAYS", "30"))
USE_DOCKER = os.getenv("USE_DOCKER", "false").lower() == "true"
DOCKER_CONTAINER = os.getenv("DOCKER_CONTAINER", "sigmun-postgres")


def ensure_backup_dir() -> Path:
    """Garante que o diretório de backup existe."""
    backup_path = Path(BACKUP_DIR)
    backup_path.mkdir(parents=True, exist_ok=True)
    return backup_path


def generate_backup_filename() -> str:
    """Gera nome do arquivo de backup com timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"sigmun_backup_{timestamp}.sql"


def run_pg_backup_sql(backup_file: Path) -> bool:
    """
    Executa pg_dump via subprocess para backup SQL.
    
    Returns:
        True se o backup foi bem-sucedido
    """
    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    cmd = [
        "pg_dump",
        "-h", DB_HOST,
        "-p", str(DB_PORT),
        "-U", DB_USER,
        "-d", DB_NAME,
        "-F", "p",
        "-v",
        "--no-owner",
        "--no-privileges",
        "-f", str(backup_file),
    ]

    if USE_DOCKER:
        cmd = [
            "docker", "exec", DOCKER_CONTAINER,
            "pg_dump",
            "-U", DB_USER,
            "-d", DB_NAME,
            "-F", "p",
            "--no-owner",
            "--no-privileges",
        ]

    logger.info(f"Iniciando backup do banco {DB_NAME} em {backup_file}")

    try:
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Erro no pg_dump: {result.stderr}")
            return False
        return True
    except FileNotFoundError:
        logger.error("pg_dump não encontrado. Verifique a instalação do PostgreSQL client.")
        return False


def compress_backup(backup_file: Path) -> Path:
    """Comprime o arquivo de backup com gzip."""
    compressed_file = backup_file.with_suffix(".sql.gz")
    logger.info(f"Comprimindo backup para {compressed_file}")
    
    with open(backup_file, "rb") as f_in:
        with gzip.open(compressed_file, "wb", compresslevel=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    backup_file.unlink()
    return compressed_file


def verify_backup(backup_file: Path) -> bool:
    """Verifica a integridade do backup comprimido."""
    logger.info(f"Verificando integridade do backup {backup_file}")
    try:
        result = subprocess.run(["gzip", "-t", str(backup_file)], capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Falha na verificação: {result.stderr}")
            return False
        return True
    except FileNotFoundError:
        logger.warning("gzip não encontrado para verificação")
        return True

def restore_backup(backup_file: Path, target_db: str = None) -> bool:
    """
    Restaura um backup no banco de dados.
    
    Args:
        backup_file: Caminho do arquivo de backup (.sql.gz)
        target_db: Nome do banco de destino
        
    Returns:
        True se a restauração foi bem-sucedida
    """
    db_name = target_db or DB_NAME
    logger.info(f"Iniciando restauração do backup {backup_file} no banco {db_name}")
    
    sql_file = backup_file.with_suffix("")
    try:
        with gzip.open(backup_file, "rb") as f_in:
            with open(sql_file, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
    except Exception as e:
        logger.error(f"Erro ao descomprimir backup: {e}")
        return False
    
    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD
    
    cmd = [
        "psql", "-h", DB_HOST, "-p", str(DB_PORT),
        "-U", DB_USER, "-d", db_name,
        "-f", str(sql_file), "-v", "ON_ERROR_STOP=1",
    ]
    
    try:
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        success = result.returncode == 0
        if not success:
            logger.error(f"Erro na restauração: {result.stderr}")
        else:
            logger.info("Restauração concluída com sucesso")
        return success
    finally:
        if sql_file.exists():
            sql_file.unlink()


def run_backup() -> bool:
    """Executa o fluxo completo de backup."""
    logger.info("=" * 60)
    logger.info("INICIANDO BACKUP DO BANCO DE DADOS - SIGMUN")
    logger.info(f"Banco: {DB_NAME} em {DB_HOST}:{DB_PORT}")
    logger.info(f"Diretório: {BACKUP_DIR}")
    logger.info(f"Retenção: {RETENTION_DAYS} dias")
    logger.info("=" * 60)
    
    backup_dir = ensure_backup_dir()
    backup_filename = generate_backup_filename()
    backup_file = backup_dir / backup_filename
    
    if not run_pg_backup_sql(backup_file):
        logger.error("FALHA NO BACKUP")
        return False
    
    compressed_file = compress_backup(backup_file)
    
    if not verify_backup(compressed_file):
        logger.error("FALHA NA VERIFICAÇÃO DO BACKUP")
        return False
    
    file_size = compressed_file.stat().st_size
    logger.info(f"Backup concluído: {compressed_file.name}")
    logger.info(f"Tamanho: {file_size / 1024 / 1024:.2f} MB")
    
    cleanup_old_backups(backup_dir)
    
    logger.info("BACKUP CONCLUÍDO COM SUCESSO")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup do banco de dados SIGMUN")
    parser.add_argument("--restore", type=str, help="Restaura um backup específico")
    parser.add_argument("--target-db", type=str, help="Banco de destino para restauração")
    parser.add_argument("--list", action="store_true", help="Lista backups disponíveis")
    
    args = parser.parse_args()
    
    if args.list:
        backup_dir = Path(BACKUP_DIR)
        if backup_dir.exists():
            backups = sorted(backup_dir.glob("sigmun_backup_*.sql.gz"))
            print(f"Backups disponíveis ({len(backups)}):")
            for b in backups:
                size = b.stat().st_size / 1024 / 1024
                mtime = datetime.fromtimestamp(b.stat().st_mtime)
                print(f"  {b.name} ({size:.2f} MB) - {mtime}")
        else:
            print(f"Diretório de backup não encontrado: {BACKUP_DIR}")
        sys.exit(0)
    
    if args.restore:
        success = restore_backup(Path(args.restore), args.target_db)
        sys.exit(0 if success else 1)
    
    success = run_backup()
    sys.exit(0 if success else 1)



def cleanup_old_backups(backup_dir: Path) -> None:
    """Remove backups mais antigos que o período de retenção."""
    cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    removed = 0
    for backup_file in backup_dir.glob("sigmun_backup_*.sql.gz"):
        try:
            file_mtime = datetime.fromtimestamp(backup_file.stat().st_mtime)
            if file_mtime < cutoff_date:
                backup_file.unlink()
                removed += 1
                logger.info(f"Backup removido: {backup_file.name}")
        except Exception as e:
            logger.warning(f"Erro ao processar {backup_file.name}: {e}")
    if removed > 0:
        logger.info(f"{removed} backup(s) removido(s) por política de retenção")
