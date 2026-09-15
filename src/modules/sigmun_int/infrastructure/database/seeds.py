"""Seed de dados iniciais do domínio de Integração e Interoperabilidade (DOM-INT).

Popula os conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP) definidos
na referência canônica do DOM-INT (020-Plano-de-Implantacao), de forma
idempotente: os registros já existentes (por código) não são recriados.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from src.modules.sigmun_int.application.use_cases.conector_use_cases import (
    CONECTORES_OFICIAIS,
)

from .models import ConectorModel

__all__ = ["popular_seed_int", "executar_seed_int"]


def popular_seed_int(session: Session) -> dict:
    """Popula o schema ``integracao`` com os conectores oficiais.

    Retorna um relatório com a quantidade de registros criados e já existentes.
    O ``commit`` fica a cargo do chamador.
    """
    resultado = {"conectores_criados": 0, "conectores_existentes": 0}

    codigos_existentes = {codigo for (codigo,) in session.query(ConectorModel.codigo).all()}
    for dados in CONECTORES_OFICIAIS:
        if dados["codigo"] in codigos_existentes:
            resultado["conectores_existentes"] += 1
            continue
        session.add(
            ConectorModel(
                codigo=dados["codigo"],
                nome=dados["nome"],
                descricao=dados["descricao"],
                provedor=dados["provedor"],
                url_base=dados["url_base"],
                autenticacao_tipo=dados["autenticacao_tipo"],
                estado="sem_configuracao",
                config=dados["config"],
                is_deleted=False,
            )
        )
        resultado["conectores_criados"] += 1

    session.flush()
    return resultado


def executar_seed_int(session: Session) -> dict:
    """Executa o seed e confirma a transação."""
    resultado = popular_seed_int(session)
    session.commit()
    return resultado