#!/usr/bin/env python
"""Executa o seed de dados DEMO do dominio Obras e Infraestrutura (DOM-OBR).

Uso:
    .venv/bin/python scripts/seed_obr.py            # popula (idempotente)
    .venv/bin/python scripts/seed_obr.py --dry-run  # apenas simula
    .venv/bin/python scripts/seed_obr.py --limpar   # remove os dados do seed

O seed cria somente dados ficticios para demonstracao das telas:
- obras publicas em todas as situacoes do ciclo (planejada, licitacao,
  contratada, em execucao e concluida)
- etapas de execucao, com avanco fisico
- medicoes fisico-financeiras (registradas e aprovadas)
- despesas financeiras (repasses e materiais)
- vistorias fiscalizadoras

O seed e executado sob demanda e nao no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execucao direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_obras.infrastructure.database.seeds import (  # noqa: E402
    DESPESAS_DEMO,
    ETAPAS_DEMO,
    MEDICOES_DEMO,
    OBRAS_DEMO,
    VISTORIAS_DEMO,
    limpar_seed_obr,
    popular_seed_obr,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-OBR (obras, medicoes, despesas)."
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
            removidos = limpar_seed_obr(session)
            session.commit()
            print("Dados do seed do DOM-OBR removidos com sucesso.")
            for chave in ("despesas", "vistorias", "medicoes", "etapas", "obras"):
                print(f"  {chave.capitalize():<18} removidos: {removidos[chave]}")
            return 0

        resultado = popular_seed_obr(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alteracoes revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-OBR aplicado com sucesso.")

        print(
            f"  Obras criadas:      {resultado['obras_criadas']}"
            f" (total demo: {len(OBRAS_DEMO)})"
        )
        print(
            f"  Etapas criadas:     {resultado['etapas_criadas']}"
            f" (total demo: {len(ETAPAS_DEMO)})"
        )
        print(
            f"  Medicoes criadas:   {resultado['medicoes_criadas']}"
            f" (total demo: {len(MEDICOES_DEMO)})"
        )
        print(
            f"  Despesas criadas:   {resultado['despesas_criadas']}"
            f" (total demo: {len(DESPESAS_DEMO)})"
        )
        print(
            f"  Vistorias criadas:  {resultado['vistorias_criadas']}"
            f" (total demo: {len(VISTORIAS_DEMO)})"
        )
        print(f"  Obras concluidas:   {resultado['obras_concluidas']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
