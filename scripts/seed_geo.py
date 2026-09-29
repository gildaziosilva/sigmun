#!/usr/bin/env python
"""Executa o seed de dados DEMO do dominio Geoinformacao Municipal (DOM-GEO).

Uso:
    .venv/bin/python scripts/seed_geo.py            # popula (idempotente)
    .venv/bin/python scripts/seed_geo.py --dry-run  # apenas simula
    .venv/bin/python scripts/seed_geo.py --limpar   # remove os dados do seed

O seed cria somente dados ficticios para demonstracao das telas:
- camadas cartograficas (ortofoto, hipsometria, hidrografia, uso do solo)
- mapas SIG com composicao de camadas (rascunho e publicado)
- elementos geoespaciais (pontos de interesse)
- servicos geoespaciais publicados (WMS, XYZ)

O seed e executado sob demanda e nao no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execucao direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_geoinformacao.infrastructure.database.seeds import (  # noqa: E402
    CAMADAS_DEMO,
    FEATURES_DEMO,
    MAPAS_DEMO,
    SERVICOS_DEMO,
    limpar_seed_geo,
    popular_seed_geo,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-GEO (camadas, mapas SIG, servicos)."
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
            removidos = limpar_seed_geo(session)
            session.commit()
            print("Dados do seed do DOM-GEO removidos com sucesso.")
            for chave in ("features", "servicos", "composicoes", "mapas", "camadas"):
                print(f"  {chave.capitalize():<18} removidos: {removidos[chave]}")
            return 0

        resultado = popular_seed_geo(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alteracoes revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-GEO aplicado com sucesso.")

        print(
            f"  Camadas criadas:    {resultado['camadas_criadas']}"
            f" (total demo: {len(CAMADAS_DEMO)})"
        )
        print(
            f"  Mapas criados:      {resultado['mapas_criados']}"
            f" (total demo: {len(MAPAS_DEMO)})"
        )
        print(f"  Mapas publicados:   {resultado['mapas_publicados']}")
        print(
            f"  Elementos criados:  {resultado['features_criados']}"
            f" (total demo: {len(FEATURES_DEMO)})"
        )
        print(
            f"  Servicos criados:   {resultado['servicos_criados']}"
            f" (total demo: {len(SERVICOS_DEMO)})"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
