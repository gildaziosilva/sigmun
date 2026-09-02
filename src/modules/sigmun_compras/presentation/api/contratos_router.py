"""Endpoints REST para Contratos.

Baseado em:
  - UC-COMPRAS-024 – Registrar Contrato
  - ENT-COMPRAS-009 – Contrato
  - RN-COMPRAS-035 a 039

Rotas:
  POST   /api/v1/contratos                    – registra
  GET    /api/v1/contratos                    – lista com filtros
  GET    /api/v1/contratos/{id}               – consulta
  PATCH  /api/v1/contratos/{id}               – atualiza dados cadastrais
  PATCH  /api/v1/contratos/{id}/situacao      – transição de situação
  DELETE /api/v1/contratos/{id}               – exclui (soft-delete)
"""

from __future__ import annotations

import logging
from typing import Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_compras.application.commands.alterar_situacao_contrato_command import (
    AlterarSituacaoContratoCommand,
)
from src.modules.sigmun_compras.application.commands.atualizar_contrato_command import (
    AtualizarContratoCommand,
)
from src.modules.sigmun_compras.application.commands.criar_contrato_command import (
    CriarContratoCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_contrato_command import (
    ExcluirContratoCommand,
)
from src.modules.sigmun_compras.application.commands.formalizar_contratacao_command import (
    FormalizarContratacaoCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_contrato_query import (
    ConsultarContratoQuery,
)
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.application.use_cases.alterar_situacao_contrato import (
    AlterarSituacaoContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_contrato import (
    AtualizarContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_contrato import (
    ConsultarContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_contrato import (
    ExcluirContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.formalizar_contratacao import (
    FormalizarContratacaoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_contratos import (
    ListarContratosUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_contrato import (
    RegistrarContratoUseCase,
)
from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
)
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    ContratoDuplicadoError,
    ContratoNaoEncontradoError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)
from src.modules.sigmun_compras.presentation.schemas.contrato_schemas import (
    ContratoCreateRequest,
    ContratoListResponse,
    ContratoResponse,
    ContratoSituacaoRequest,
    ContratoUpdateRequest,
    FormalizarContratacaoRequest,
)

from src.shared.security import (
    UsuarioContexto,
    exigir_autenticacao,
    extrair_usuario_id_header,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/contratos", tags=["Compras - Contratos"])


def get_contrato_repository(
    session: Annotated[Session, Depends(get_db)],
) -> ContratoRepository:
    """Fornece o repositório concreto de contratos por requisição."""
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyContratoRepository,
    )

    return SqlAlchemyContratoRepository(session)


def get_compra_repository(
    session: Annotated[Session, Depends(get_db)],
) -> CompraRepository:
    """Fornece o repositório concreto de compras por requisição.

    Necessário para a integração de Formalização da Contratação
    (Compra -> Contrato) sem acoplar a persistência entre os domínios.
    """
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyCompraRepository,
    )

    return SqlAlchemyCompraRepository(session)


def get_servico_de_auditoria(
    repository: Annotated[
        TrilhaAuditoriaRepository, Depends(get_trilha_auditoria_repository)
    ],
) -> ServicoDeAuditoria:
    """Fornece o ServicoDeAuditoria (025-Estrutura-Tecnica, seção 18)."""
    return ServicoDeAuditoria(repository)


def get_trilha_auditoria_repository(
    session: Annotated[Session, Depends(get_db)],
) -> TrilhaAuditoriaRepository:
    """Fornece o repositório da trilha de auditoria por requisição."""
    from src.modules.sigmun_compras.infrastructure.repositories import (
        SqlAlchemyTrilhaAuditoriaRepository,
    )

    return SqlAlchemyTrilhaAuditoriaRepository(session)


# -- Endpoints ----------------------------------------------------------------


@router.post(
    "",
    response_model=ContratoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra um novo contrato",
    responses={
        404: {"description": "Processo documental, fornecedor ou unidade não encontrados"},
        409: {"description": "Já existe contrato com o mesmo numero (RN-COMPRAS-036)"},
    },
)
def criar_contrato(
    payload: ContratoCreateRequest,
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    auditoria: Annotated[ServicoDeAuditoria, Depends(get_servico_de_auditoria)],
    usuario_id: Annotated[UUID | None, Depends(extrair_usuario_id_header)] = None,
) -> Contrato:
    use_case = RegistrarContratoUseCase(repository)
    try:
        contrato = use_case.execute(
            CriarContratoCommand(
                processo_documental_id=payload.processo_documental_id,
                fornecedor_id=payload.fornecedor_id,
                unidade_id=payload.unidade_id,
                numero=payload.numero,
                data_inicio=payload.data_inicio,
                data_fim=payload.data_fim,
                valor=payload.valor,
                objeto=payload.objeto,
                licitacao_master_id=payload.licitacao_master_id,
                situacao=payload.situacao or SituacaoContrato.EM_ELABORACAO,
                usuario_id=usuario_id,
            )
        )
    except (
        ProcessoDocumentalNaoEncontradoError,
        FornecedorNaoEncontradoError,
        UnidadeNaoEncontradaError,
    ) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContratoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    # Auditoria reforçada de contratos (017-Modelo-de-Auditoria, seção 44).
    auditoria.registrar(
        categoria=CategoriaEventoAuditoria.CRIACAO,
        tipo_evento="ContratoCriado",
        operacao="criarContrato",
        recurso_tipo="Contrato",
        recurso_id=contrato.id,
        chave_negocio=contrato.numero,
        ator_id=usuario_id,
        detalhes={"situacao_inicial": contrato.situacao.value},
    )
    return contrato


@router.post(
    "/formalizar",
    response_model=ContratoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Formalizar a contratação (Compra -> Contrato)",
    description=(
        "Integração Compra -> Contrato (UC-COMPRAS-022 / RN-COMPRAS-038). "
        "Requer autenticação (header X-Usuario-Id) e uma compra em situação "
        "HOMOLOGADO/CONTRATADO. O contrato herda processo documental, "
        "fornecedor e unidade da compra referenciada."
    ),
    responses={
        401: {"description": "Autenticação obrigatória"},
        404: {"description": "Compra, processo, fornecedor ou unidade não encontrados"},
        409: {"description": "Já existe contrato com o mesmo numero"},
        400: {"description": "Compra não homologada ou payload inválido"},
    },
)
def formalizar_contratacao(
    compra_id: Annotated[UUID, Query(description="Compra (processo) a formalizar")],
    payload: FormalizarContratacaoRequest,
    usuario: Annotated[UsuarioContexto, Depends(exigir_autenticacao)],
    contratos_repo: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    compras_repo: Annotated[CompraRepository, Depends(get_compra_repository)],
    auditoria: Annotated[ServicoDeAuditoria, Depends(get_servico_de_auditoria)],
) -> Contrato:
    use_case = FormalizarContratacaoUseCase(contratos_repo, compras_repo)
    try:
        contrato = use_case.execute(
            FormalizarContratacaoCommand(
                compra_id=compra_id,
                numero=payload.numero,
                data_inicio=payload.data_inicio,
                data_fim=payload.data_fim,
                valor=payload.valor,
                objeto=payload.objeto,
                data_assinatura=payload.data_assinatura,
                usuario_id=usuario.usuario_id,
            )
        )
    except CompraNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except (
        ProcessoDocumentalNaoEncontradoError,
        FornecedorNaoEncontradoError,
        UnidadeNaoEncontradaError,
    ) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContratoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    # 017-Modelo-de-Auditoria, seção 44: origem da formalização na trilha.
    auditoria.registrar(
        categoria=CategoriaEventoAuditoria.CRIACAO,
        tipo_evento="ContratacaoFormalizada",
        operacao="formalizarContratacao",
        recurso_tipo="Contrato",
        recurso_id=contrato.id,
        chave_negocio=contrato.numero,
        ator_id=usuario.usuario_id,
        ator_perfil=",".join(usuario.papeis) or None,
        detalhes={
            "compra_id": str(compra_id),
            "assinado": payload.data_assinatura is not None,
        },
    )
    return contrato


@router.get(
    "",
    response_model=ContratoListResponse,
    summary="Lista contratos com filtros opcionais",
)
def listar_contratos(
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    situacao: Annotated[
        str | None, Query(description="Filtrar por situação")
    ] = None,
    fornecedor_id: Annotated[UUID | None, Query(description="Filtrar por fornecedor")] = None,
    unidade_id: Annotated[UUID | None, Query(description="Filtrar por unidade")] = None,
    include_inativos: Annotated[bool, Query(description="Incluir excluídos")] = False,
    page: Annotated[int, Query(ge=0)] = 0,
    page_size: Annotated[int, Query(ge=1, le=200)] = 50,
) -> ContratoListResponse:
    from src.modules.sigmun_compras.application.queries.listar_contratos_query import (
        ListarContratosQuery,
    )

    situacao_filtro: SituacaoContrato | None = None
    if situacao is not None:
        try:
            situacao_filtro = SituacaoContrato(situacao.upper())
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Situação inválida: {situacao}. "
                f"Valores aceitos: {[s.value for s in SituacaoContrato]}",
            ) from exc

    query = ListarContratosQuery(
        situacao=situacao_filtro,
        fornecedor_id=fornecedor_id,
        unidade_id=unidade_id,
        include_inativos=include_inativos,
        page=page,
        page_size=page_size,
    )
    contratos = ListarContratosUseCase(repository).execute(query)

    todos = repository.list(
        situacao=situacao_filtro,
        fornecedor_id=fornecedor_id,
        unidade_id=unidade_id,
        include_deleted=False,
    )
    items = [ContratoResponse.model_validate(c) for c in contratos]
    return ContratoListResponse(total=len(todos), page=page, page_size=page_size, items=items)


@router.get(
    "/{contrato_id}",
    response_model=ContratoResponse,
    summary="Consulta um contrato pelo ID",
    responses={404: {"description": "Contrato não encontrado"}},
)
def consultar_contrato(
    contrato_id: UUID,
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
) -> Contrato:
    use_case = ConsultarContratoUseCase(repository)
    try:
        return use_case.execute(ConsultarContratoQuery(contrato_id=contrato_id))
    except ContratoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/{contrato_id}",
    response_model=ContratoResponse,
    summary="Atualiza dados cadastrais de um contrato",
    responses={
        404: {"description": "Contrato não encontrado"},
        400: {"description": "Requisição inválida"},
        409: {"description": "Já existe contrato com o mesmo numero"},
    },
)
def atualizar_contrato(
    contrato_id: UUID,
    payload: ContratoUpdateRequest,
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    auditoria: Annotated[ServicoDeAuditoria, Depends(get_servico_de_auditoria)],
    usuario_id: Annotated[UUID | None, Depends(extrair_usuario_id_header)] = None,
) -> Contrato:
    use_case = AtualizarContratoUseCase(repository)
    try:
        contrato = use_case.execute(
            AtualizarContratoCommand(
                contrato_id=contrato_id,
                numero=payload.numero,
                data_inicio=payload.data_inicio,
                data_fim=payload.data_fim,
                valor=payload.valor,
                objeto=payload.objeto,
                usuario_id=usuario_id,
            )
        )
    except ContratoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ContratoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    # 017-Modelo-de-Auditoria, seção 35: campos alterados na trilha.
    campos_alterados = [
        campo
        for campo in ("numero", "data_inicio", "data_fim", "valor", "objeto")
        if getattr(payload, campo) is not None
    ]
    auditoria.registrar(
        categoria=CategoriaEventoAuditoria.ALTERACAO,
        tipo_evento="ContratoAlterado",
        operacao="atualizarContrato",
        recurso_tipo="Contrato",
        recurso_id=contrato.id,
        chave_negocio=contrato.numero,
        ator_id=usuario_id,
        detalhes={"campos": campos_alterados},
    )
    return contrato


@router.patch(
    "/{contrato_id}/situacao",
    response_model=ContratoResponse,
    summary="Altera a situação do contrato",
    description=(
        "Transições válidas: EM_ELABORACAO -> ASSINADO -> VIGENTE -> "
        "(SUSPENSO | ENCERRADO | RESCINDIDO); SUSPENSO pode voltar a VIGENTE "
        "ou ir para ENCERRADO/RESCINDIDO/EXTINTO."
    ),
    responses={
        404: {"description": "Contrato não encontrado"},
        400: {"description": "Transição não permitida"},
    },
)
def alterar_situacao(
    contrato_id: UUID,
    payload: ContratoSituacaoRequest,
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    auditoria: Annotated[ServicoDeAuditoria, Depends(get_servico_de_auditoria)],
    usuario_id: Annotated[UUID | None, Depends(extrair_usuario_id_header)] = None,
) -> Contrato:
    use_case = AlterarSituacaoContratoUseCase(repository)
    try:
        contrato = use_case.execute(
            AlterarSituacaoContratoCommand(
                contrato_id=contrato_id,
                nova_situacao=payload.situacao,
                usuario_id=usuario_id,
            )
        )
    except ContratoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    # Assinatura é evento próprio (017-Modelo-de-Auditoria, seção 44).
    if payload.situacao == SituacaoContrato.ASSINADO:
        categoria_evento = CategoriaEventoAuditoria.ASSINATURA
        tipo_evento = "ContratoAssinado"
    else:
        categoria_evento = CategoriaEventoAuditoria.ALTERACAO
        tipo_evento = "ContratoSituacaoAlterada"

    auditoria.registrar(
        categoria=categoria_evento,
        tipo_evento=tipo_evento,
        operacao="alterarSituacaoContrato",
        recurso_tipo="Contrato",
        recurso_id=contrato.id,
        chave_negocio=contrato.numero,
        ator_id=usuario_id,
        detalhes={"situacao_nova": payload.situacao.value},
    )
    return contrato


@router.delete(
    "/{contrato_id}",
    response_model=ContratoResponse,
    summary="Exclui (soft-delete) um contrato",
    responses={404: {"description": "Contrato não encontrado"}},
)
def excluir_contrato(
    contrato_id: UUID,
    repository: Annotated[ContratoRepository, Depends(get_contrato_repository)],
    auditoria: Annotated[ServicoDeAuditoria, Depends(get_servico_de_auditoria)],
    usuario_id: Annotated[UUID | None, Depends(extrair_usuario_id_header)] = None,
) -> Contrato:
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para exclusão.",
        )

    use_case = ExcluirContratoUseCase(repository)
    try:
        contrato = use_case.execute(ExcluirContratoCommand(contrato_id=contrato_id, usuario_id=usuario_id))
    except ContratoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

    # 017-Modelo-de-Auditoria, seção 36: exclusão lógica auditada.
    auditoria.registrar(
        categoria=CategoriaEventoAuditoria.EXCLUSAO,
        tipo_evento="ContratoExcluido",
        operacao="excluirContrato",
        recurso_tipo="Contrato",
        recurso_id=contrato.id,
        chave_negocio=contrato.numero,
        ator_id=usuario_id,
    )
    return contrato


__all__ = [
    "router",
    "get_contrato_repository",
    "get_compra_repository",
    "get_trilha_auditoria_repository",
    "get_servico_de_auditoria",
]
