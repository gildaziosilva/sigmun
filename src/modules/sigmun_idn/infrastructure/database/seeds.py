"""
Seeds do DOM-IDN — Identidade e Acesso.

Este módulo contém os dados de RBAC (papéis e permissões) do DOM-IDN,
consumidos pelos demais domínios do SIGMUN.

IMPORTANTE:
- Os dados `PERMISSOES_DEMO_COMPRAS` / `ROLES_DEMO_COMPRAS` são DEMONSTRATIVOS:
  servem apenas para validação técnica do mecanismo RBAC e não representam
  catálogo institucional oficial do SIGMUN.
- Os dados `PERMISSOES_OUV` / `ROLES_OUV` são papéis **funcionais** do DOM-OUV,
  definidos conforme ADR-0008 (autorização e sigilo de dados de Ouvidoria).
  A matriz reflete decisão de negócio e deve ser revisada pela Ouvidoria antes
  da promoção a produção.
- Não criar usuários, sessões ou registros de auditoria neste seed.
- Todas as funções são idempotentes.

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
            "Role demonstrativa para validação de acesso de consulta no domínio de Compras."
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
            "Role demonstrativa para validação de operações de execução no domínio de Compras."
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
            "Role demonstrativa para validação de operações de gestão no domínio de Compras."
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
# PERMISSÕES DO DOM-OUV (Ouvidoria)
# ============================================================================
#
# Definidas em ADR-0008 (autorização e sigilo de dados de Ouvidoria).
# A separação entre `*.CONSULTAR` e `*.SENSITIVOS_CONSULTAR` materializa a
# decisão 2.3 do ADR: papéis funcionais de proteção ao cidadão acessam o dado
# sensível; a administração técnica não.

PERMISSOES_OUV: tuple[PermissaoSeed, ...] = (
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.CRIAR",
        nome="Registrar manifestação",
        descricao="Permite registrar manifestação, denúncia e pedido de acesso à informação.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.CONSULTAR",
        nome="Consultar manifestação",
        descricao="Permite consultar manifestações, denúncias e pedidos de acesso à informação.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.RESPONDER",
        nome="Responder manifestação",
        descricao="Permite registrar resposta ao cidadão.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.ALTERAR_STATUS",
        nome="Alterar status de manifestação",
        descricao="Permite alterar o status conforme as transições do fluxo FalaBR.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.PRAZOS",
        nome="Prorrogar prazo de resposta",
        descricao="Permite prorrogar o prazo de resposta da manifestação.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.MANIFESTACAO.AVALIAR",
        nome="Avaliar atendimento",
        descricao="Permite registrar a avaliação de satisfação do cidadão.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.DENUNCIA.ENCAMINHAR",
        nome="Encaminhar denúncia",
        descricao="Permite encaminhar denúncia a órgão externo (MP, PF, TCE, TCU, CGU).",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.LAI.DECIDIR_RECURSO",
        nome="Decidir recurso de pedido de acesso",
        descricao="Permite decidir recurso contra pedido de acesso negado (LAI art. 15).",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.INDICADORES.CONSULTAR",
        nome="Consultar indicadores da ouvidoria",
        descricao="Permite consultar estatísticas e indicadores institucionais.",
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
    PermissaoSeed(
        codigo="OUV.DENUNCIA.SENSITIVOS_CONSULTAR",
        nome="Consultar dados sensíveis de denúncia",
        descricao=(
            "Permite acessar os dados de identificação do denunciante (CPF, e-mail, "
            "servidor envolvido). Exclusivo de papéis funcionais de proteção ao "
            "cidadão, conforme ADR-0008 seção 2.3."
        ),
        modulo="ouvidoria",
        escopo=PermissaoEscopo.DOMINIO,
    ),
)


# ============================================================================
# ROLES DO DOM-OUV
# ============================================================================
#
# Matriz de papéis conforme ADR-0008 seções 2.3 e 2.6.
#
# Decisão-chave: ROLE_ADMIN **não** recebe OUV.DENUNCIA.SENSITIVOS_CONSULTAR.
# A administração técnica do sistema não é autoridade funcional sobre a
# identificação de um denunciante.

ROLES_OUV: tuple[RoleSeed, ...] = (
    RoleSeed(
        codigo="ROLE_OUVIDOR",
        nome="Ouvidor",
        descricao=(
            "Responsável pelo tratamento de manifestações, denúncias e pedidos de acesso "
            "à informação. Acesso integral aos dados do denunciante."
        ),
        permissoes=(
            "OUV.MANIFESTACAO.CRIAR",
            "OUV.MANIFESTACAO.CONSULTAR",
            "OUV.MANIFESTACAO.RESPONDER",
            "OUV.MANIFESTACAO.ALTERAR_STATUS",
            "OUV.MANIFESTACAO.PRAZOS",
            "OUV.MANIFESTACAO.AVALIAR",
            "OUV.DENUNCIA.ENCAMINHAR",
            "OUV.LAI.DECIDIR_RECURSO",
            "OUV.INDICADORES.CONSULTAR",
            "OUV.DENUNCIA.SENSITIVOS_CONSULTAR",
        ),
    ),
    RoleSeed(
        codigo="ROLE_CORREGEDOR",
        nome="Corregedor",
        descricao=(
            "Responsável pela corregedoria e pelo controle interno das manifestações. "
            "Acesso integral aos dados do denunciante."
        ),
        permissoes=(
            "OUV.MANIFESTACAO.CRIAR",
            "OUV.MANIFESTACAO.CONSULTAR",
            "OUV.MANIFESTACAO.RESPONDER",
            "OUV.MANIFESTACAO.ALTERAR_STATUS",
            "OUV.MANIFESTACAO.PRAZOS",
            "OUV.MANIFESTACAO.AVALIAR",
            "OUV.DENUNCIA.ENCAMINHAR",
            "OUV.LAI.DECIDIR_RECURSO",
            "OUV.INDICADORES.CONSULTAR",
            "OUV.DENUNCIA.SENSITIVOS_CONSULTAR",
        ),
    ),
    RoleSeed(
        codigo="ROLE_AUDITOR",
        nome="Auditor interno",
        descricao=(
            "Responsável pela auditoria das manifestações. Acesso aos dados do denunciante "
            "para fins de verificação, sem permissão de escrita."
        ),
        permissoes=(
            "OUV.MANIFESTACAO.CONSULTAR",
            "OUV.INDICADORES.CONSULTAR",
            "OUV.DENUNCIA.SENSITIVOS_CONSULTAR",
        ),
    ),
    RoleSeed(
        codigo="ROLE_ADMIN",
        nome="Administrador do sistema",
        descricao=(
            "Administração técnica do SIGMUN. Acesso a metadados agregados da ouvidoria. "
            "NÃO possui acesso aos dados sensíveis do denunciante, conforme ADR-0008 "
            "seção 2.3 (separação entre função técnica e funcional)."
        ),
        permissoes=(
            "OUV.MANIFESTACAO.CONSULTAR",
            "OUV.INDICADORES.CONSULTAR",
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
    seeds: tuple[PermissaoSeed, ...],
) -> tuple[dict[str, PermissaoModel], int]:
    """
    Cria as permissões ausentes declaradas em ``seeds``.

    A operação é idempotente: permissões já existentes são reaproveitadas,
    e apenas as ausentes são inseridas.

    Retorna:
        mapa codigo -> model
        quantidade criada
    """
    permissoes: dict[str, PermissaoModel] = {}
    criadas = 0

    for item in seeds:
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
    existentes = set(
        session.scalars(
            select(RolePermissaoModel.permissao_id).where(
                RolePermissaoModel.role_id == role_model.id
            )
        ).all()
    )

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
    seeds: tuple[RoleSeed, ...],
) -> tuple[int, int]:
    """
    Cria as roles ausentes declaradas em ``seeds`` e sincroniza as permissões.

    A criação de roles é idempotente: roles já existentes são reaproveitadas.
    A sincronização de permissões é aditiva (não remove associações), evitando
    que um seed apague alterações feitas por outro processo.

    Retorna:
        quantidade de roles criadas
        quantidade de associações role-permissão criadas
    """
    roles_criadas = 0
    associacoes_criadas = 0

    for item in seeds:
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
    Popula os dados de RBAC do DOM-IDN.

    Cria permissões e roles de dois conjuntos:

    * ``PERMISSOES_DEMO_COMPRAS`` / ``ROLES_DEMO_COMPRAS`` — dados demonstrativos
      de validação do mecanismo RBAC no domínio de Compras;
    * ``PERMISSOES_OUV`` / ``ROLES_OUV`` — papéis funcionais do DOM-OUV,
      definidos conforme ADR-0008 (autorização e sigilo de dados de Ouvidoria).

    A função é **idempotente**: reexecutar não duplica registros. Ela não realiza
    commit; o controle transacional pertence ao chamador.

    Retorna um resumo com:
        permissoes_criadas
        roles_criadas
        associacoes_criadas
    """
    permissoes, permissoes_criadas = _criar_permissoes(
        session,
        PERMISSOES_DEMO_COMPRAS + PERMISSOES_OUV,
    )

    roles_criadas, associacoes_criadas = _criar_roles(
        session=session,
        permissoes=permissoes,
        seeds=ROLES_DEMO_COMPRAS + ROLES_OUV,
    )

    return {
        "permissoes_criadas": permissoes_criadas,
        "roles_criadas": roles_criadas,
        "associacoes_criadas": associacoes_criadas,
    }
