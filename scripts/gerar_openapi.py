"""Gera openapi.json versionado — T-3.3.

Uso:
    python scripts/gerar_openapi.py [--output DIR] [--version VERSAO]

Gera arquivo: openapi/v{VERSION}/openapi.json
Também atualiza openapi/latest/openapi.json (symlink ou cópia)
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Adiciona o diretório raiz ao path para importar a app
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.main import app


def gerar_openapi(versao: str, output_dir: Path) -> Path:
    """Gera o openapi.json para a versão especificada."""
    version_dir = output_dir / f"v{versao}"
    version_dir.mkdir(parents=True, exist_ok=True)

    openapi_path = version_dir / "openapi.json"

    # Gera schema do FastAPI
    schema = app.openapi()

    # Adiciona metadados de versão
    schema["info"]["version"] = versao
    schema["info"]["x-generated-at"] = datetime.utcnow().isoformat() + "Z"
    schema["info"]["x-generated-by"] = "scripts/gerar_openapi.py"

    # Escreve arquivo
    openapi_path.write_text(
        json.dumps(schema, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )

    return openapi_path


def atualizar_latest(output_dir: Path, versao: str) -> None:
    """Atualiza o diretório latest para apontar para a versão atual."""
    latest_dir = output_dir / "latest"
    if latest_dir.exists() or latest_dir.is_symlink():
        if latest_dir.is_symlink():
            latest_dir.unlink()
        else:
            shutil.rmtree(latest_dir)

    # Cria symlink relativo (mais limpo) ou copia se não suportado
    try:
        latest_dir.symlink_to(f"v{versao}", target_is_directory=True)
    except (OSError, NotImplementedError):
        # Fallback: copia os arquivos
        shutil.copytree(output_dir / f"v{versao}", latest_dir)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Gera openapi.json versionado")
    parser.add_argument(
        "--output",
        default="openapi",
        help="Diretório de saída (padrão: openapi/)",
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Versão (padrão: lido de src/shared/config/settings.py ou timestamp)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output).resolve()
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir

    # Determina versão
    if args.version:
        versao = args.version
    else:
        # Tenta ler do settings
        try:
            from src.shared.config.settings import settings

            versao = settings.APP_VERSION
        except Exception:
            versao = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    print(f"Gerando OpenAPI versão {versao} em {output_dir}...")
    openapi_path = gerar_openapi(versao, output_dir)
    print(f"  -> {openapi_path}")

    atualizar_latest(output_dir, versao)
    print(f"  -> latest atualizado para v{versao}")

    return 0


if __name__ == "__main__":
    sys.exit(main())