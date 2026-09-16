#!/usr/bin/env python
"""Executa o seed de dados iniciais do domínio Integração (DOM-INT).

Uso:
    .venv/bin/python scripts/seed_int.py
    .venv/bin/python scripts/seed_int.py --dry-run

O seed é executado sob demanda e não no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execução direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_int.infrastructure.database.seeds import (  # noqa: E402
    popular_seed_int,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados iniciais do DOM-INT."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executa sem confirmar alterações (rollback ao final).",
    )
    args = parser.parse_args()

    with SessionLocal() as session:
        resultado = popular_seed_int(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alterações revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-INT aplicado com sucesso.")

        print(
            f"  Conectores criados:    "
            f"{resultado['conectores_criados']}"
        )
        print(
            f"  Conectores existentes: "
            f"{resultado['conectores_existentes']}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
