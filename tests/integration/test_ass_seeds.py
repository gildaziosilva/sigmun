"""Testes de integração do seed de dados DEMO do DOM-ASS.

Validam a populacao do CadUnico local, unidades CRAS/CREAS, beneficios
eventuais e atendimentos sociais, alem da idempotencia da execucao
repetida e da limpeza dos dados.
"""

import pytest
from sqlalchemy import select, text

from src.core.infrastructure.database.session import SessionLocal
from src.modules.sigmun_assistencia_social.infrastructure.database.models import (
    AtendimentoSocialModel,
    BeneficioEventualModel,
    FamiliaCadUnicoModel,
    PessoaCadUnicoModel,
    UnidadeAssistenciaModel,
)
from src.modules.sigmun_assistencia_social.infrastructure.database.seeds import (
    ATENDIMENTOS_DEMO,
    BENEFICIOS_DEMO,
    FAMILIAS_DEMO,
    UNIDADES_DEMO,
    limpar_seed_ass,
    popular_seed_ass,
)

TABELAS_ASS_SEED = (
    "ass.atendimentos_sociais",
    "ass.beneficios_eventuais",
    "ass.pessoas_cadunico",
    "ass.familias_cadunico",
    "ass.unidades_assistencia",
)


def _total_pessoas_demo() -> int:
    return sum(len(f.pessoas) for f in FAMILIAS_DEMO)


@pytest.fixture(autouse=True)
def _limpar_tabelas_seed():
    """Isolamento: limpa as tabelas afetadas pelo seed antes/depois."""
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_ASS_SEED)} CASCADE"))
        session.commit()
    yield
    with SessionLocal() as session:
        session.execute(text(f"TRUNCATE TABLE {', '.join(TABELAS_ASS_SEED)} CASCADE"))
        session.commit()


def test_seed_popula_todas_as_tabelas():
    with SessionLocal() as session:
        resultado = popular_seed_ass(session)
        session.commit()

        total_unidades = len(session.scalars(select(UnidadeAssistenciaModel)).all())
        total_familias = len(session.scalars(select(FamiliaCadUnicoModel)).all())
        total_pessoas = len(session.scalars(select(PessoaCadUnicoModel)).all())
        total_beneficios = len(session.scalars(select(BeneficioEventualModel)).all())
        total_atendimentos = len(session.scalars(select(AtendimentoSocialModel)).all())

    assert resultado["unidades_criadas"] == len(UNIDADES_DEMO)
    assert resultado["familias_criadas"] == len(FAMILIAS_DEMO)
    assert resultado["pessoas_criadas"] == _total_pessoas_demo()
    assert resultado["beneficios_criados"] == len(BENEFICIOS_DEMO)
    assert resultado["atendimentos_criados"] == len(ATENDIMENTOS_DEMO)

    assert total_unidades == len(UNIDADES_DEMO)
    assert total_familias == len(FAMILIAS_DEMO)
    assert total_pessoas == _total_pessoas_demo()
    assert total_beneficios == len(BENEFICIOS_DEMO)
    assert total_atendimentos == len(ATENDIMENTOS_DEMO)


def test_seed_eh_idempotente():
    """Segunda execucao nao deve criar registros (em especial atendimentos,
    que sao append-only e nao possuem chave natural unica)."""
    with SessionLocal() as session:
        popular_seed_ass(session)
        session.commit()

        segunda = popular_seed_ass(session)
        session.commit()

    assert segunda["unidades_criadas"] == 0
    assert segunda["familias_criadas"] == 0
    assert segunda["pessoas_criadas"] == 0
    assert segunda["beneficios_criados"] == 0
    assert segunda["atendimentos_criados"] == 0


def test_seed_cobre_todos_os_status_de_beneficio():
    """O seed deve gerar dados para cada status exibido na visao geral."""
    with SessionLocal() as session:
        popular_seed_ass(session)
        session.commit()

        status = {
            b.status
            for b in session.scalars(select(BeneficioEventualModel)).all()
        }

    assert {"solicitado", "aprovado", "entregue", "negado", "cancelado"} <= status


def test_seed_respeita_regras_de_negocio():
    """NIS e CPF unicos, 11 digitos, e referencias validas."""
    with SessionLocal() as session:
        popular_seed_ass(session)
        session.commit()

        familias = session.scalars(select(FamiliaCadUnicoModel)).all()
        pessoas = session.scalars(select(PessoaCadUnicoModel)).all()
        familias_ids = {str(f.id) for f in familias}

    assert all(len(f.nis) == 11 and f.nis.isdigit() for f in familias)
    assert all(len(p.cpf) == 11 and p.cpf.isdigit() for p in pessoas)
    assert len({f.nis for f in familias}) == len(familias)
    assert len({p.cpf for p in pessoas}) == len(pessoas)
    # Toda pessoa pertence a uma familia populada.
    assert all(str(p.familia_id) in familias_ids for p in pessoas)


def test_limpar_seed_remove_os_dados():
    with SessionLocal() as session:
        popular_seed_ass(session)
        session.commit()

        removidos = limpar_seed_ass(session)
        session.commit()

        assert session.scalars(select(FamiliaCadUnicoModel)).all() == []
        assert session.scalars(select(PessoaCadUnicoModel)).all() == []
        assert session.scalars(select(UnidadeAssistenciaModel)).all() == []
        assert session.scalars(select(BeneficioEventualModel)).all() == []
        assert session.scalars(select(AtendimentoSocialModel)).all() == []

    assert removidos["familias"] == len(FAMILIAS_DEMO)
    assert removidos["pessoas"] == _total_pessoas_demo()
    assert removidos["unidades"] == len(UNIDADES_DEMO)
    assert removidos["beneficios"] == len(BENEFICIOS_DEMO)
    assert removidos["atendimentos"] == len(ATENDIMENTOS_DEMO)
