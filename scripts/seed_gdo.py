#!/usr/bin/env python
"""Executa o seed de dados iniciais do domínio Gestão Documental (DOM-GDO).

Uso:
    .venv/bin/python scripts/seed_gdo.py            # popula (idempotente)
    .venv/bin/python scripts/seed_gdo.py --dry-run  # apenas simula

Conforme `020-Plano-de-Implantacao` (Onda 1 — Fundação): o seed é um passo
de implantação explícito, executado sob demanda e não no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execução direta (python scripts/seed_gdo.py) a partir da raiz
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_gdo.infrastructure.database.seeds import (  # noqa: E402
    popular_seed_gdo,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados iniciais do DOM-GDO (plano de classificação "
        "e tabelas de temporalidade)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executa sem confirmar alterações (rollback ao final).",
    )
    args = parser.parse_args()

    with SessionLocal() as session:
        resultado = popular_seed_gdo(session)
        if args.dry_run:
            session.rollback()
            print("[dry-run] Alterações revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-GDO aplicado com sucesso.")

        print(f"  Classificações criadas:    {resultado['classificacoes_criadas']}")
        print(f"  Classificações existentes: {resultado['classificacoes_existentes']}")
        print(f"  Temporalidades criadas:    {resultado['temporalidades_criadas']}")
        print(f"  Temporalidades existentes: {resultado['temporalidades_existentes']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
