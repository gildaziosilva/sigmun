#!/usr/bin/env python
"""Executa o seed de dados DEMO do dominio Gestao Territorial (DOM-TEL).

Uso:
    .venv/bin/python scripts/seed_tel.py            # popula (idempotente)
    .venv/bin/python scripts/seed_tel.py --dry-run  # apenas simula
    .venv/bin/python scripts/seed_tel.py --limpar   # remove os dados do seed

O seed cria somente dados ficticios para demonstracao das telas:
- bairros, distritos, setores e zona rural
- logradouros publicos vinculados aos bairros
- plantas genericas de valores (rascunho, vigente e revogada)
- georreferencias territoriais (ponto, linha e poligono)

O seed e executado sob demanda e nao no startup da API.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execucao direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_territorial.infrastructure.database.seeds import (  # noqa: E402
    BAIRROS_DEMO,
    GEORREFERENCIAS_DEMO,
    LOGRADOUROS_DEMO,
    PLANTAS_DEMO,
    limpar_seed_tel,
    popular_seed_tel,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-TEL (territorio, planta de valores)."
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
            removidos = limpar_seed_tel(session)
            session.commit()
            print("Dados do seed do DOM-TEL removidos com sucesso.")
            for chave in ("georreferencias", "plantas", "logradouros", "bairros"):
                print(f"  {chave.capitalize():<18} removidos: {removidos[chave]}")
            return 0

        resultado = popular_seed_tel(session)

        if args.dry_run:
            session.rollback()
            print("[dry-run] Alteracoes revertidas (nenhum dado gravado).")
        else:
            session.commit()
            print("Seed do DOM-TEL aplicado com sucesso.")

        print(
            f"  Bairros criados:         {resultado['bairros_criados']}"
            f" (total demo: {len(BAIRROS_DEMO)})"
        )
        print(
            f"  Logradouros criados:      {resultado['logradouros_criados']} "
            f"(total demo: {len(LOGRADOUROS_DEMO)})"
        )
        print(
            f"  Plantas criadas:         {resultado['plantas_criadas']}"
            f" (total demo: {len(PLANTAS_DEMO)})"
        )
        print(
            f"  Georreferencias criadas: {resultado['georreferencias_criadas']} "
            f"(total demo: {len(GEORREFERENCIAS_DEMO)})"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
