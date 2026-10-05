#!/usr/bin/env python
"""Executa o seed de RBAC do domínio Identidade e Acesso (DOM-IDN).

Uso:
    .venv/bin/python scripts/seed_idn.py
    .venv/bin/python scripts/seed_idn.py --dry-run

O seed cria permissões e roles de dois conjuntos:

- Demonstrativos (validação técnica do mecanismo RBAC):
  - permissões COMPRAS.*
  - roles ROLE_DEMO_COMPRAS_*

- Papéis funcionais do DOM-OUV (ADR-0008 — autorização e sigilo de dados):
  - permissões OUV.*
  - roles ROLE_OUVIDOR, ROLE_CORREGEDOR, ROLE_AUDITOR, ROLE_ADMIN

  A matriz de papéis reflete decisão de negócio e deve ser revisada pela
  Ouvidoria antes da promoção a produção.

Não cria usuários, sessões ou auditoria de login.
O seed é executado sob demanda e não no startup da API.
É idempotente: reexecutar não duplica registros.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite execução direta a partir da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.infrastructure.database.session import SessionLocal  # noqa: E402
from src.modules.sigmun_idn.infrastructure.database.seeds import (  # noqa: E402
    popular_seed_idn,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed de dados DEMO do DOM-IDN."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executa sem confirmar alterações (rollback ao final).",
    )
    args = parser.parse_args()

    with SessionLocal() as session:
        try:
            resultado = popular_seed_idn(session)

            if args.dry_run:
                session.rollback()
                print("[dry-run] Alterações revertidas (nenhum dado gravado).")
            else:
                session.commit()
                print("Seed DEMO do DOM-IDN aplicado com sucesso.")

            print(
                f"  Permissões criadas:      "
                f"{resultado['permissoes_criadas']}"
            )
            print(
                f"  Roles criadas:           "
                f"{resultado['roles_criadas']}"
            )
            print(
                f"  Associações criadas:     "
                f"{resultado['associacoes_criadas']}"
            )

        except Exception:
            session.rollback()
            raise

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
