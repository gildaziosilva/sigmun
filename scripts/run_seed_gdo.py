"""Script rápido para executar o seed GDO contra o banco PostgreSQL ativo."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_gdo.infrastructure.database.seeds import popular_seed_gdo

if __name__ == "__main__":
    db = SessionLocal()
    try:
        r = popular_seed_gdo(db)
        db.commit()
        print("Seed executado:", r)
    finally:
        db.close()
