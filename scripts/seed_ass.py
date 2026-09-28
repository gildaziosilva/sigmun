#!/usr/bin/env python
"""Executa o seed de dados DEMO do dominio Assistencia Social (DOM-ASS).

Uso:
    .venv/bin/python scripts/seed_ass.py            # popula (idempotente)
    .venv/bin/python scripts/seed_ass.py --dry-run  # apenas simula
    .venv/bin/python scripts/seed_ass.py --limpar   # remove os dados do seed

O seed cria somente dados ficticios para demonstracao das telas:
- unidades CRAS/CREAS/Centro Pop/Abrigo
- familias e pessoas do CadUnico local
- beneficios eventuais em todos os status
- atendimentos sociais

O seed e executado sob demanda e nao no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execucao direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_assistencia_social.infrastructure.database.seeds import (  # noqa: E402
    ATENDIMENTOS_DEMO,
    BENEFICIOS_DEMO,
    FAMILIAS_DEMO,
    UNIDADES_DEMO,
    limpar_seed_ass,
    popular_seed_ass,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-ASS (CadUnico local, CRAS/CREAS)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executa sem confirmar alteracoes (rollback ao final).",
    )
    parser.add_argument(
        "--limpar",
        action="store_true",
        help="Remove os dados criados pelo seed (nao popula).",
    )
    args = parser.parse_args()

    with SessionLocal() as session:
        if args.limpar:
            removidos = limpar_seed_ass(session)
            session.commit()
            print("Dados do seed do DOM-ASS removidos com sucesso.")
            print(f"  Atendimentos removidos: {removidos['atendimentos']}")
            print(f"  Beneficios removidos:   {removidos['beneficios']}")
            print(f"  Pessoas removidas:      {removidos['pessoas']}")
            print(f"  Familias removidas:     {removidos['familias']}")
            print(f"  Unidades removidas:     {removidos['unidades']}")
            return 0

        resultado = popular_seed_ass(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alteracoes revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-ASS aplicado com sucesso.")

        print(
            f"  Unidades criadas:     {resultado['unidades_criadas']}"
            f" (total demo: {len(UNIDADES_DEMO)})"
        )
        print(
            f"  Familias criadas:     {resultado['familias_criadas']}"
            f" (total demo: {len(FAMILIAS_DEMO)})"
        )
        print(
            f"  Pessoas criadas:       {resultado['pessoas_criadas']}"
            f" (total demo: {sum(len(f.pessoas) for f in FAMILIAS_DEMO)})"
        )
        print(
            f"  Beneficios criados:   {resultado['beneficios_criados']}"
            f" (total demo: {len(BENEFICIOS_DEMO)})"
        )
        print(
            f"  Atendimentos criados:  {resultado['atendimentos_criados']}"
            f" (total demo: {len(ATENDIMENTOS_DEMO)})"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
