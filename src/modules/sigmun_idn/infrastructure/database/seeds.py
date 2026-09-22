"""
Seeds do DOM-IDN — Identidade e Acesso.

Este módulo contém dados demonstrativos para validação técnica
do mecanismo RBAC do DOM-IDN.

IMPORTANTE:
- Os dados aqui definidos são DEMONSTRATIVOS.
- Não representam catálogo institucional oficial do SIGMUN.
- Não criar usuários, sessões ou registros de auditoria neste seed.
- Permissões de domínio utilizadas neste seed são provenientes do
  domínio de Compras e servem apenas para validação do RBAC.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.sigmun_idn.domain.entities.usuario import Permissao, PermissaoEscopo, Role
from src.modules.sigmun_idn.infrastructure.database.models import (
    PermissaoModel,
    RoleModel,
    RolePermissaoModel,
)


# ============================================================================
# PERMISSÕES DEMONSTRATIVAS
# ============================================================================

@dataclass(frozen=True)
class PermissaoSeed:
    codigo: str
    nome: str
    descricao: str
    modulo: str
    escopo: PermissaoEscopo


PERMISSOES_DEMO_COMPRAS: tuple[PermissaoSeed, ...] = (
    PermissaoSeed(
        codigo="COMPRAS.DEMANDA.CRIAR",
        nome="Criar demanda de compras",
        descricao="Permite criar demandas de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.DEMANDA.CONSULTAR",
        nome="Consultar demanda de compras",
        descricao="Permite consultar demandas de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.DEMANDA.APROVAR",
        nome="Aprovar demanda de compras",
        descricao="Permite aprovar demandas de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.PROCESSO.CRIAR",
        nome="Criar processo de compras",
        descricao="Permite criar processos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.PROCESSO.CONSULTAR",
        nome="Consultar processo de compras",
        descricao="Permite consultar processos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.PROCESSO.EDITAR",
        nome="Editar processo de compras",
        descricao="Permite editar processos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.PROCESSO.ENCERRAR",
        nome="Encerrar processo de compras",
        descricao="Permite encerrar processos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.CONTRATO.CRIAR",
        nome="Criar contrato de compras",
        descricao="Permite criar contratos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.CONTRATO.CONSULTAR",
        nome="Consultar contrato de compras",
        descricao="Permite consultar contratos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.CONTRATO.EDITAR",
        nome="Editar contrato de compras",
        descricao="Permite editar contratos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.CONTRATO.ASSINAR",
        nome="Assinar contrato de compras",
        descricao="Permite executar a operação de assinatura de contratos.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="COMPRAS.CONTRATO.ENCERRAR",
        nome="Encerrar contrato de compras",
        descricao="Permite encerrar contratos de compras.",
        modulo="compras",
        escopo=PermissaoEscopo.DOMINIO,
    ),
)


# ============================================================================
# ROLES DEMONSTRATIVAS
# ============================================================================

@dataclass(frozen=True)
class RoleSeed:
    codigo: str
    nome: str
    descricao: str
    permissoes: tuple[str, ...]


ROLES_DEMO_COMPRAS: tuple[RoleSeed, ...] = (
    RoleSeed(
        codigo="ROLE_DEMO_COMPRAS_CONSULTA",
        nome="Consulta de Compras — Demo",
        descricao=(
            "Role demonstrativa para validação de acesso de consulta "
            "no domínio de Compras."
        ),
        permissoes=(
            "COMPRAS.DEMANDA.CONSULTAR",
            "COMPRAS.PROCESSO.CONSULTAR",
            "COMPRAS.CONTRATO.CONSULTAR",
        ),
    ),
    RoleSeed(
        codigo="ROLE_DEMO_COMPRAS_OPERADOR",
        nome="Operador de Compras — Demo",
        descricao=(
            "Role demonstrativa para validação de operações "
            "de execução no domínio de Compras."
        ),
        permissoes=(
            "COMPRAS.DEMANDA.CRIAR",
            "COMPRAS.DEMANDA.CONSULTAR",
            "COMPRAS.PROCESSO.CRIAR",
            "COMPRAS.PROCESSO.CONSULTAR",
            "COMPRAS.PROCESSO.EDITAR",
            "COMPRAS.CONTRATO.CRIAR",
            "COMPRAS.CONTRATO.CONSULTAR",
            "COMPRAS.CONTRATO.EDITAR",
        ),
    ),
    RoleSeed(
        codigo="ROLE_DEMO_COMPRAS_GESTOR",
        nome="Gestão de Compras — Demo",
        descricao=(
            "Role demonstrativa para validação de operações de gestão "
            "no domínio de Compras."
        ),
        permissoes=(
            "COMPRAS.DEMANDA.CRIAR",
            "COMPRAS.DEMANDA.CONSULTAR",
            "COMPRAS.DEMANDA.APROVAR",
            "COMPRAS.PROCESSO.CRIAR",
            "COMPRAS.PROCESSO.CONSULTAR",
            "COMPRAS.PROCESSO.EDITAR",
            "COMPRAS.PROCESSO.ENCERRAR",
            "COMPRAS.CONTRATO.CRIAR",
            "COMPRAS.CONTRATO.CONSULTAR",
            "COMPRAS.CONTRATO.EDITAR",
            "COMPRAS.CONTRATO.ASSINAR",
            "COMPRAS.CONTRATO.ENCERRAR",
        ),
    ),
)


# ============================================================================
# HELPERS
# ============================================================================

def _obter_permissao_model(
    session: Session,
    codigo: str,
) -> PermissaoModel | None:
    """Obtém uma permissão ativa pelo código."""
    return session.scalar(
        select(PermissaoModel).where(
            PermissaoModel.codigo == codigo,
            PermissaoModel.deleted_at.is_(None),
        )
    )


def _obter_role_model(
    session: Session,
    codigo: str,
) -> RoleModel | None:
    """Obtém uma role ativa pelo código."""
    return session.scalar(
        select(RoleModel).where(
            RoleModel.codigo == codigo,
            RoleModel.deleted_at.is_(None),
        )
    )


def _criar_permissoes(
    session: Session,
) -> tuple[dict[str, PermissaoModel], int]:
    """
    Cria as permissões demonstrativas ausentes.

    Retorna:
        mapa codigo -> model
        quantidade criada
    """
    permissoes: dict[str, PermissaoModel] = {}
    criadas = 0

    for item in PERMISSOES_DEMO_COMPRAS:
        existente = _obter_permissao_model(session, item.codigo)

        if existente is not None:
            permissoes[item.codigo] = existente
            continue

        entidade = Permissao(
            codigo=item.codigo,
            nome=item.nome,
            descricao=item.descricao,
            escopo=item.escopo,
            modulo=item.modulo,
        )

        model = PermissaoModel(
            id=UUID(entidade.id),
            codigo=entidade.codigo,
            nome=entidade.nome,
            descricao=entidade.descricao,
            escopo=entidade.escopo.value.upper(),
            modulo=entidade.modulo,
        )

        session.add(model)
        permissoes[item.codigo] = model
        criadas += 1

    session.flush()

    return permissoes, criadas


def _sincronizar_permissoes_role(
    session: Session,
    role_model: RoleModel,
    codigos_permissoes: tuple[str, ...],
    permissoes: dict[str, PermissaoModel],
) -> int:
    """
    Garante que a role possua todas as permissões declaradas.

    A operação é aditiva: não remove associações existentes.
    Isso evita que um seed demonstrativo apague alterações realizadas
    posteriormente por outro processo.
    """
    existentes = {
        permissao_id
        for permissao_id in session.scalars(
            select(RolePermissaoModel.permissao_id).where(
                RolePermissaoModel.role_id == role_model.id
            )
        ).all()
    }

    adicionadas = 0

    for codigo in codigos_permissoes:
        permissao = permissoes[codigo]

        if permissao.id in existentes:
            continue

        session.add(
            RolePermissaoModel(
                role_id=role_model.id,
                permissao_id=permissao.id,
            )
        )

        existentes.add(permissao.id)
        adicionadas += 1

    return adicionadas


def _criar_roles(
    session: Session,
    permissoes: dict[str, PermissaoModel],
) -> tuple[int, int]:
    """
    Cria as roles demonstrativas ausentes e sincroniza suas permissões.

    Retorna:
        quantidade de roles criadas
        quantidade de associações role-permissão criadas
    """
    roles_criadas = 0
    associacoes_criadas = 0

    for item in ROLES_DEMO_COMPRAS:
        role_model = _obter_role_model(session, item.codigo)

        if role_model is None:
            entidade = Role(
                codigo=item.codigo,
                nome=item.nome,
                descricao=item.descricao,
            )

            role_model = RoleModel(
                id=UUID(entidade.id),
                codigo=entidade.codigo,
                nome=entidade.nome,
                descricao=entidade.descricao,
            )

            session.add(role_model)
            session.flush()

            roles_criadas += 1

        associacoes_criadas += _sincronizar_permissoes_role(
            session=session,
            role_model=role_model,
            codigos_permissoes=item.permissoes,
            permissoes=permissoes,
        )

    session.flush()

    return roles_criadas, associacoes_criadas


# ============================================================================
# API PÚBLICA DO SEED
# ============================================================================

def popular_seed_idn(session: Session) -> dict[str, int]:
    """
    Popula os dados demonstrativos do DOM-IDN.

    A função não realiza commit. O controle transacional pertence
    ao chamador.

    Retorna um resumo com:
        permissoes_criadas
        roles_criadas
        associacoes_criadas
    """
    permissoes, permissoes_criadas = _criar_permissoes(session)

    roles_criadas, associacoes_criadas = _criar_roles(
        session=session,
        permissoes=permissoes,
    )

    return {
        "permissoes_criadas": permissoes_criadas,
        "roles_criadas": roles_criadas,
        "associacoes_criadas": associacoes_criadas,
    }
