#!/usr/bin/env python
"""Executa o seed de dados DEMO do dominio Cadastro Imobiliario (DOM-IMO).

Uso:
    .venv/bin/python scripts/seed_imo.py            # popula (idempotente)
    .venv/bin/python scripts/seed_imo.py --dry-run  # apenas simula
    .venv/bin/python scripts/seed_imo.py --limpar   # remove os dados do seed

O seed cria somente dados ficticios para demonstracao das telas:
- imoveis (lotes) com inscricao imobiliaria
- vinculos de propriedade (titulares e parceiros)
- caracteristicas construtivas
- geometrias georreferenciadas dos lotes
- avaliacoes de valor venal (concluidas, em rascunho e canceladas)

PRE-REQUISITO: o seed do DOM-TEL deve estar aplicado, pois os imoveis
referenciam logradouros e bairros cadastrados.

O seed e executado sob demanda e nao no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execucao direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_cadastro_imobiliario.infrastructure.database.seeds import (  # noqa: E402
    AVALIACOES_DEMO,
    CARACTERISTICAS_DEMO,
    GEOMETRIAS_DEMO,
    IMOVEIS_DEMO,
    PROPRIETARIOS_DEMO,
    limpar_seed_imo,
    popular_seed_imo,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-IMO (cadastro imobilario)."
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
            removidos = limpar_seed_imo(session)
            session.commit()
            print("Dados do seed do DOM-IMO removidos com sucesso.")
            for chave in (
                "avaliacoes",
                "geometrias",
                "caracteristicas",
                "proprietarios",
                "imoveis",
            ):
                print(f"  {chave.capitalize():<18} removidos: {removidos[chave]}")
            return 0

        resultado = popular_seed_imo(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alteracoes revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-IMO aplicado com sucesso.")

        print(
            f"  Imoveis criados:        {resultado['imoveis_criados']}"
            f" (total demo: {len(IMOVEIS_DEMO)})"
        )
        print(
            f"  Proprietarios criados:  {resultado['proprietarios_criados']} "
            f"(total demo: {len(PROPRIETARIOS_DEMO)})"
        )
        print(
            f"  Caracteristicas criadas: {resultado['caracteristicas_criadas']} "
            f"(total demo: {len(CARACTERISTICAS_DEMO)})"
        )
        print(
            f"  Geometrias criadas:     {resultado['geometrias_criadas']} "
            f"(total demo: {len(GEOMETRIAS_DEMO)})"
        )
        print(
            f"  Avaliacoes criadas:     {resultado['avaliacoes_criadas']} "
            f"(total demo: {len(AVALIACOES_DEMO)})"
        )
        print(f"  Avaliacoes canceladas:  {resultado['avaliacoes_canceladas']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
