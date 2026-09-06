"""Endpoints REST de Gestão Documental (DOM-GDO)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_gdo.application.interfaces import (
    RepositorioDocumento,
    RepositorioVersaoDocumento,
    RepositorioTramitacao,
    RepositorioProcessoDocumento,
    RepositorioClassificacaoDocumental,
    RepositorioTabelaTemporalidade,
    RepositorioArquivamento,
    RepositorioAssinatura,
    RepositorioTipoDocumental,
    PublicadorEventos,
)
from src.modules.sigmun_gdo.application.use_cases import (
    CriarDocumentoUseCase,
    ClassificarDocumentoUseCase,
    TramitarDocumentoUseCase,
    ArquivarDocumentoUseCase,
    ArquivarDocumentoInputDTO,
    AssinarDocumentoUseCase,
    AssinarDocumentoInputDTO,
    CriarVersaoDocumentoUseCase,
    CriarVersaoInputDTO,
    AvaliarDestinacaoUseCase,
    AvaliarDestinacaoInputDTO,
    TipoDestinacaoAplicada,
    CriarTipoDocumentoUseCase,
    CriarTipoDocumentoInputDTO,
    AtivarTipoDocumentoUseCase,
    InativarTipoDocumentoUseCase,
    BuscarTipoDocumentoUseCase,
    ListarTiposDocumentoUseCase,
)
from src.modules.sigmun_gdo.domain.exceptions import (
    DocumentoNaoEncontradoError,
    DocumentoJaExisteError,
    CodigoDocumentalDuplicadoError,
    IntegridadeInvalidaError,
    ClassificacaoDocumentalNaoEncontradaError,
    PermissaoNegadaError,
    ArquivamentoInvalidoError,
    EliminacaoNaoAutorizadaError,
    TipoDocumentalInvalidoError,
)
from src.modules.sigmun_gdo.infrastructure.repositories import (
    SQLAlchemyDocumentoRepository,
    SQLAlchemyVersaoDocumentoRepository,
    SQLAlchemyTramitacaoRepository,
    SQLAlchemyProcessoDocumentoRepository,
    SQLAlchemyClassificacaoDocumentalRepository,
    SQLAlchemyTabelaTemporalidadeRepository,
    SQLAlchemyArquivamentoRepository,
    SQLAlchemyAssinaturaRepository,
    SQLAlchemyTipoDocumentalRepository,
)
from src.modules.sigmun_gdo.infrastructure.messaging import (
    PublicadorOutboxGDO,
    TopicosGDO,
)
from src.modules.sigmun_gdo.presentation.schemas import (
    DocumentoCreateRequest,
    DocumentoResponse,
    DocumentoListResponse,
    DocumentoCapturaRequest,
    TramitacaoCreateRequest,
    TramitacaoResponse,
    ClassificacaoCreateRequest,
    ClassificacaoResponse,
    ClassificacaoListResponse,
    ProcessoDocumentoCreateRequest,
    ProcessoDocumentoResponse,
    TabelaTemporalidadeCreateRequest,
    TabelaTemporalidadeResponse,
    ArquivamentoCreateRequest,
    ArquivamentoResponse,
    AssinaturaCreateRequest,
    AssinaturaResponse,
    VersaoCreateRequest,
    VersaoDocumentoResponse,
    DestinacaoRequest,
    TipoDocumentoCreateRequest,
    TipoDocumentoResponse,
    ErrorResponse,
)
from src.modules.sigmun_gdo.domain.entities import TramitacaoDocumento

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/gdo", tags=["Gestão Documental"])


# =============================================================================
# Dependency Injection
# =============================================================================


def get_documento_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioDocumento:
    return SQLAlchemyDocumentoRepository(session)


def get_tramitacao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioTramitacao:
    return SQLAlchemyTramitacaoRepository(session)


def get_classificacao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioClassificacaoDocumental:
    return SQLAlchemyClassificacaoDocumentalRepository(session)


def get_processo_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioProcessoDocumento:
    return SQLAlchemyProcessoDocumentoRepository(session)


def get_temporalidade_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioTabelaTemporalidade:
    return SQLAlchemyTabelaTemporalidadeRepository(session)


def get_arquivamento_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioArquivamento:
    return SQLAlchemyArquivamentoRepository(session)


def get_assinatura_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioAssinatura:
    return SQLAlchemyAssinaturaRepository(session)


def get_versao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioVersaoDocumento:
    return SQLAlchemyVersaoDocumentoRepository(session)


def get_tipo_documental_repository(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioTipoDocumental:
    return SQLAlchemyTipoDocumentalRepository(session)


def get_publicador_eventos(
    session: Annotated[Session, Depends(get_db)],
) -> PublicadorEventos:
    """Publicador Transactional Outbox — evento gravado na mesma transação."""
    return PublicadorOutboxGDO(session)


# =============================================================================

# =============================================================================
# Publicação de eventos de integração (Transactional Outbox)
# =============================================================================


def _publicar_evento(
    publicador: PublicadorEventos,
    *,
    topico: str,
    evento_nome: str,
    agregado_id: str,
    documento,
    extras: dict | None = None,
) -> None:
    """Registra um evento de integração na outbox (mesma transação do negócio).

    O envio efetivo ao barramento (Redis Streams) é feito depois pelo
    `DespachadorRedisStreams` (014-Modelo-de-Integracao, seção 6).
    """
    payload = {
        "documento_id": documento.id,
        "codigo": documento.codigo,
        "numero": documento.numero,
        "ano": documento.ano,
        "titulo": documento.titulo,
        "status": (
            documento.status.value
            if hasattr(documento.status, "value")
            else str(documento.status)
        ),
        "unidade_autor_id": documento.unidade_autor_id,
        **(extras or {}),
    }
    publicador.publicar(
        topico=topico,
        evento_nome=evento_nome,
        agregado_tipo="documento",
        agregado_id=agregado_id,
        payload=payload,
    )


def _publicar_documento_criado(publicador: PublicadorEventos, documento) -> None:
    """Publica `gdo.documento.criado`."""
    _publicar_evento(
        publicador,
        topico=TopicosGDO.DOCUMENTO_CRIADO,
        evento_nome="DocumentoCriado",
        agregado_id=documento.id,
        documento=documento,
    )


def _publicar_documento_vinculado_processo(
    publicador: PublicadorEventos, documento
) -> None:
    """Publica `gdo.documento.vinculado_processo`."""
    _publicar_evento(
        publicador,
        topico=TopicosGDO.DOCUMENTO_VINCULADO_PROCESSO,
        evento_nome="DocumentoVinculadoProcesso",
        agregado_id=documento.id,
        documento=documento,
        extras={"processo_id": documento.processo_id},
    )


# =============================================================================
# Endpoints de Documento
# =============================================================================
# Endpoints de Documento
# =============================================================================


@router.post(
    "/documentos",
    response_model=DocumentoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo documento digital",
    responses={400: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
def criar_documento(
    payload: DocumentoCreateRequest,
    repo: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_tipo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
    publicador: Annotated[PublicadorEventos, Depends(get_publicador_eventos)],
    session: Annotated[Session, Depends(get_db)],
) -> DocumentoResponse:
    """Cria um novo documento digital no sistema."""
    try:
        use_case = CriarDocumentoUseCase(repo, repo_tipo)
        from src.modules.sigmun_gdo.application.use_cases import CriarDocumentoInputDTO
        dto = CriarDocumentoInputDTO(
            codigo=payload.codigo,
            numero=payload.numero,
            ano=payload.ano,
            tipo_documental_id=payload.tipo_documental_id,
            titulo=payload.titulo,
            descricao=payload.descricao or "",
            unidade_autor_id=payload.unidade_autor_id,
            unidade_arquivo_id=payload.unidade_arquivo_id or "",
            processo_id=payload.processo_id or "",
            is_sigiloso=payload.is_sigiloso,
            conteudo_ref=payload.conteudo_ref or "",
            hash_integridade=payload.hash_integridade or "",
            created_by="",
        )
        result = use_case.execute(dto)
        # Recarrega a entidade persistida para montar a resposta completa
        documento = repo.get_by_id(result.id)
        if not documento:  # pragma: no cover - defensivo
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Documento criado mas não encontrado",
            )
        # Eventos de integração (Transactional Outbox — mesma transação)
        _publicar_documento_criado(publicador, documento)
        if documento.processo_id:
            _publicar_documento_vinculado_processo(publicador, documento)
        return _documento_to_response(documento)
    except CodigoDocumentalDuplicadoError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except IntegridadeInvalidaError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except TipoDocumentalInvalidoError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except IntegrityError as exc:
        # RN-GDO-001 (race): o constraint expresso `documentos_codigo_key`
        # é a fonte de verdade da unicidade. Torna o conflito determinístico
        # e retorna 409 mesmo quando a checagem prévia perde a corrida.
        session.rollback()
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail="Código documental já utilizado por outro documento (RN-GDO-001)",
        ) from exc


@router.get(
    "/documentos",
    response_model=DocumentoListResponse,
    summary="Lista documentos",
)
def listar_documentos(
    repo: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    page: int = 0,
    page_size: int = 50,
) -> DocumentoListResponse:
    """Lista documentos ativos."""
    documentos = repo.find_ativos()
    start = page * page_size
    end = start + page_size
    items = documentos[start:end]
    return DocumentoListResponse(
        total=len(documentos),
        page=page,
        page_size=page_size,
        items=[_documento_to_response(d) for d in items],
    )


@router.get(
    "/documentos/{documento_id}",
    response_model=DocumentoResponse,
    summary="Busca um documento por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_documento(
    documento_id: str,
    repo: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
) -> DocumentoResponse:
    """Busca um documento por ID."""
    documento = repo.get_by_id(documento_id)
    if not documento:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Documento {documento_id} não encontrado"
        )
    return _documento_to_response(documento)


@router.get(
    "/documentos/processo/{processo_id}",
    response_model=list[DocumentoResponse],
    summary="Lista documentos de um processo",
)
def documentos_do_processo(
    processo_id: str,
    repo: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
) -> list[DocumentoResponse]:
    """Lista documentos vinculados a um processo."""
    documentos = repo.find_by_processo(processo_id)
    return [_documento_to_response(d) for d in documentos]


# =============================================================================
# Endpoints de Tramitação
# =============================================================================


@router.post(
    "/documentos/{documento_id}/tramitar",
    response_model=TramitacaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Tramita um documento entre unidades",
    responses={404: {"model": ErrorResponse}},
)
def tramitar_documento(
    documento_id: str,
    payload: TramitacaoCreateRequest,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_tram: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repository)],
    publicador: Annotated[PublicadorEventos, Depends(get_publicador_eventos)],
) -> TramitacaoResponse:
    """Tramita um documento entre unidades."""
    documento = repo_doc.get_by_id(documento_id)
    if not documento:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Documento não encontrado")

    try:
        use_case = TramitarDocumentoUseCase(repo_doc, repo_tram)
        from src.modules.sigmun_gdo.application.use_cases.tramitar_documento_use_case import TramitarDocumentoInputDTO
        dto = TramitarDocumentoInputDTO(
            documento_id=documento_id,
            unidade_origem_id=payload.unidade_origem_id,
            unidade_destino_id=payload.unidade_destino_id,
            tipo=payload.tipo,
            motivo=payload.motivo or "",
            observacao=payload.observacao or "",
            autor_id="",
        )
        tramitacao = use_case.execute(dto)
        _publicar_evento(
            publicador,
            topico=TopicosGDO.DOCUMENTO_TRAMITADO,
            evento_nome="DocumentoTramitado",
            agregado_id=documento_id,
            documento=documento,
            extras={
                "tramitacao_id": tramitacao.id,
                "unidade_origem_id": tramitacao.unidade_origem_id,
                "unidade_destino_id": tramitacao.unidade_destino_id,
                "tipo": tramitacao.tipo.value,
            },
        )
        return _tramitacao_to_response(tramitacao)
    except DocumentoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/documentos/{documento_id}/tramitacoes",
    response_model=list[TramitacaoResponse],
    summary="Lista tramitações de um documento",
)
def listar_tramitacoes(
    documento_id: str,
    repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repository)],
) -> list[TramitacaoResponse]:
    """Lista tramitações de um documento."""
    tramitacoes = repo.find_by_documento(documento_id)
    return [_tramitacao_to_response(t) for t in tramitacoes]


# =============================================================================
# Endpoints de Classificação
# =============================================================================


@router.get(
    "/classificacoes",
    response_model=ClassificacaoListResponse,
    summary="Lista classificações documentais",
)
def listar_classificacoes(
    repo: Annotated[RepositorioClassificacaoDocumental, Depends(get_classificacao_repository)],
    page: int = 0,
    page_size: int = 50,
) -> ClassificacaoListResponse:
    """Lista classificações documentais."""
    classificacoes = repo.find_all()
    start = page * page_size
    end = start + page_size
    items = classificacoes[start:end]
    return ClassificacaoListResponse(
        total=len(classificacoes),
        page=page,
        page_size=page_size,
        items=[_classificacao_to_response(c) for c in items],
    )


@router.get(
    "/classificacoes/{classificacao_id}",
    response_model=ClassificacaoResponse,
    summary="Busca uma classificação por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_classificacao(
    classificacao_id: str,
    repo: Annotated[RepositorioClassificacaoDocumental, Depends(get_classificacao_repository)],
) -> ClassificacaoResponse:
    """Busca uma classificação por ID."""
    classificacao = repo.get_by_id(classificacao_id)
    if not classificacao:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Classificação {classificacao_id} não encontrada"
        )
    return _classificacao_to_response(classificacao)


# =============================================================================
# Endpoints de Processo
# =============================================================================


@router.get(
    "/processos/{processo_id}",
    response_model=ProcessoDocumentoResponse,
    summary="Busca um processo documental por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_processo(
    processo_id: str,
    repo: Annotated[RepositorioProcessoDocumento, Depends(get_processo_repository)],
) -> ProcessoDocumentoResponse:
    """Busca um processo documental por ID."""
    processo = repo.get_by_id(processo_id)
    if not processo:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Processo {processo_id} não encontrado"
        )
    return _processo_to_response(processo)


# =============================================================================
# Endpoints de Temporalidade
# =============================================================================


@router.get(
    "/temporalidades/{codigo}",
    response_model=TabelaTemporalidadeResponse,
    summary="Busca uma tabela de temporalidade por código",
    responses={404: {"model": ErrorResponse}},
)
def buscar_temporalidade(
    codigo: str,
    repo: Annotated[RepositorioTabelaTemporalidade, Depends(get_temporalidade_repository)],
) -> TabelaTemporalidadeResponse:
    """Busca uma tabela de temporalidade por código."""
    tabela = repo.get_by_codigo(codigo)
    if not tabela:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Temporalidade {codigo} não encontrada"
        )
    return TabelaTemporalidadeResponse(
        id=tabela.id,
        codigo=tabela.codigo,
        nome=tabela.nome,
        prazo_tempo=tabela.prazo_tempo,
        unidade_tempo=tabela.unidade_tempo,
        evento_fim=tabela.evento_fim,
        tipo_destinacao=tabela.tipo_destinacao.value,
        is_ativo=tabela.is_ativo,
        created_at=tabela.created_at,
    )


# =============================================================================
# =============================================================================
# Endpoints de Arquivamento e Assinatura
# =============================================================================


@router.post(
    "/documentos/{documento_id}/arquivar",
    response_model=ArquivamentoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Arquiva um documento corrente",
    responses={404: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
def arquivar_documento(
    documento_id: str,
    payload: ArquivamentoCreateRequest,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_arq: Annotated[RepositorioArquivamento, Depends(get_arquivamento_repository)],
    publicador: Annotated[PublicadorEventos, Depends(get_publicador_eventos)],
) -> ArquivamentoResponse:
    """Arquiva um documento corrente (RN-GDO-008: somente documentos ativos)."""
    documento = repo_doc.get_by_id(documento_id)
    if not documento:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Documento não encontrado")
    try:
        use_case = ArquivarDocumentoUseCase(repo_doc, repo_arq)
        arquivamento = use_case.execute(
            ArquivarDocumentoInputDTO(
                documento_id=documento_id,
                unidade_arquivo_id=payload.unidade_arquivo_id,
                autor_id=payload.autor_id,
                observacao=payload.observacao or "",
            )
        )
        # Re-fetch para refletir status atualizado (arquivado) no evento
        documento = repo_doc.get_by_id(documento_id)
        _publicar_evento(
            publicador,
            topico=TopicosGDO.DOCUMENTO_ARQUIVADO,
            evento_nome="DocumentoArquivado",
            agregado_id=documento_id,
            documento=documento,
            extras={
                "arquivamento_id": arquivamento.id,
                "unidade_arquivo_id": payload.unidade_arquivo_id,
            },
        )
        return _arquivamento_to_response(arquivamento)
    except DocumentoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ArquivamentoInvalidoError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post(
    "/documentos/{documento_id}/assinar",
    response_model=AssinaturaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Assina digitalmente um documento",
    responses={404: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
def assinar_documento(
    documento_id: str,
    payload: AssinaturaCreateRequest,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_ass: Annotated[RepositorioAssinatura, Depends(get_assinatura_repository)],
    publicador: Annotated[PublicadorEventos, Depends(get_publicador_eventos)],
) -> AssinaturaResponse:
    """Registra assinatura digital e fixa a integridade do documento (RN-GDO-005)."""
    documento = repo_doc.get_by_id(documento_id)
    if not documento:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Documento não encontrado")
    try:
        use_case = AssinarDocumentoUseCase(repo_doc, repo_ass)
        assinatura = use_case.execute(
            AssinarDocumentoInputDTO(
                documento_id=documento_id,
                signatario_id=payload.signatario_id,
                conteudo=payload.conteudo,
                autor_id=payload.autor_id,
                certificado_id=payload.certificado_id or "",
            )
        )
        _publicar_evento(
            publicador,
            topico=TopicosGDO.DOCUMENTO_ASSINADO,
            evento_nome="DocumentoAssinado",
            agregado_id=documento_id,
            documento=documento,
            extras={
                "assinatura_id": assinatura.id,
                "signatario_id": assinatura.signatario_id,
                "hash_assinatura": assinatura.hash_assinatura,
            },
        )
        return _assinatura_to_response(assinatura)
    except DocumentoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except (ArquivamentoInvalidoError, DocumentoJaExisteError) as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Versões e Destinação
# =============================================================================


@router.post(
    "/documentos/{documento_id}/versoes",
    response_model=VersaoDocumentoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma nova versão do documento",
    responses={404: {"model": ErrorResponse}},
)
def criar_versao_documento(
    documento_id: str,
    payload: VersaoCreateRequest,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_ver: Annotated[RepositorioVersaoDocumento, Depends(get_versao_repository)],
) -> VersaoDocumentoResponse:
    """Cria uma nova versão imutável do documento (RN-GDO-005)."""
    try:
        use_case = CriarVersaoDocumentoUseCase(repo_doc, repo_ver)
        versao = use_case.execute(
            CriarVersaoInputDTO(
                documento_id=documento_id,
                conteudo_ref=payload.conteudo_ref,
                autor_id=payload.autor_id,
                hash_integridade=payload.hash_integridade or "",
            )
        )
        return _versao_to_response(versao)
    except DocumentoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/documentos/{documento_id}/versoes",
    response_model=list[VersaoDocumentoResponse],
    summary="Lista as versões de um documento",
    responses={404: {"model": ErrorResponse}},
)
def listar_versoes_documento(
    documento_id: str,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    repo_ver: Annotated[RepositorioVersaoDocumento, Depends(get_versao_repository)],
) -> list[VersaoDocumentoResponse]:
    """Retorna o histórico de versões do documento (mais recente primeiro)."""
    if not repo_doc.get_by_id(documento_id):
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Documento {documento_id} não encontrado",
        )
    versoes = repo_ver.find_by_documento(documento_id)
    return [_versao_to_response(v) for v in versoes]


@router.post(
    "/documentos/{documento_id}/destinacao",
    response_model=DocumentoResponse,
    summary="Aplica a destinação final ao documento",
    responses={
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
    },
)
def aplicar_destinacao(
    documento_id: str,
    payload: DestinacaoRequest,
    repo_doc: Annotated[RepositorioDocumento, Depends(get_documento_repository)],
    publicador: Annotated[PublicadorEventos, Depends(get_publicador_eventos)],
) -> DocumentoResponse:
    """Aplica destinação final: eliminação (RN-GDO-010/011) ou guarda permanente."""
    try:
        use_case = AvaliarDestinacaoUseCase(repo_doc)
        tipo_aplicado = TipoDestinacaoAplicada(payload.tipo_destinacao)
        use_case.execute(
            AvaliarDestinacaoInputDTO(
                documento_id=documento_id,
                tipo_destinacao=tipo_aplicado,
                autor_id=payload.autor_id,
                autoridade_homologadora_id=payload.autoridade_homologadora_id or "",
                justificativa=payload.justificativa or "",
            )
        )
        documento = repo_doc.get_by_id(documento_id)
        if not documento:  # pragma: no cover - defensivo
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Documento não encontrado após destinação",
            )
        if tipo_aplicado == TipoDestinacaoAplicada.ELIMINACAO:
            _publicar_evento(
                publicador,
                topico=TopicosGDO.DOCUMENTO_ELIMINADO,
                evento_nome="DocumentoEliminado",
                agregado_id=documento_id,
                documento=documento,
                extras={
                    "autoridade_homologadora_id": payload.autoridade_homologadora_id or "",
                    "justificativa": payload.justificativa or "",
                },
            )
        return _documento_to_response(documento)
    except DocumentoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except EliminacaoNaoAutorizadaError as exc:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except ArquivamentoInvalidoError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Tipos Documentais
# =============================================================================


@router.post(
    "/tipos-documentais",
    response_model=TipoDocumentoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um tipo documental",
    responses={409: {"model": ErrorResponse}},
)
def criar_tipo_documento(
    payload: TipoDocumentoCreateRequest,
    repo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
) -> TipoDocumentoResponse:
    """Cria um novo tipo documental."""
    try:
        use_case = CriarTipoDocumentoUseCase(repo)
        resultado = use_case.execute(
            CriarTipoDocumentoInputDTO(
                codigo=payload.codigo,
                nome=payload.nome,
                descricao=payload.descricao or "",
            )
        )
        return _tipo_documento_to_response(resultado)
    except CodigoDocumentalDuplicadoError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/tipos-documentais",
    response_model=list[TipoDocumentoResponse],
    summary="Lista tipos documentais ativos",
)
def listar_tipos_documento(
    repo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
) -> list[TipoDocumentoResponse]:
    """Lista todos os tipos documentais ativos."""
    use_case = ListarTiposDocumentoUseCase(repo)
    return [_tipo_documento_to_response(t) for t in use_case.execute()]


@router.get(
    "/tipos-documentais/{codigo}",
    response_model=TipoDocumentoResponse,
    summary="Busca tipo documental por código",
    responses={404: {"model": ErrorResponse}},
)
def buscar_tipo_documento(
    codigo: str,
    repo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
) -> TipoDocumentoResponse:
    """Busca um tipo documental pelo código."""
    try:
        use_case = BuscarTipoDocumentoUseCase(repo)
        resultado = use_case.execute(codigo)
        return _tipo_documento_to_response(resultado)
    except TipoDocumentalInvalidoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/tipos-documentais/{codigo}/ativar",
    response_model=TipoDocumentoResponse,
    summary="Ativa um tipo documental",
    responses={404: {"model": ErrorResponse}},
)
def ativar_tipo_documento(
    codigo: str,
    repo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
) -> TipoDocumentoResponse:
    """Ativa um tipo documental previamente inativado."""
    try:
        use_case = AtivarTipoDocumentoUseCase(repo)
        resultado = use_case.execute(codigo)
        return _tipo_documento_to_response(resultado)
    except TipoDocumentalInvalidoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/tipos-documentais/{codigo}/inativar",
    response_model=TipoDocumentoResponse,
    summary="Inativa um tipo documental",
    responses={404: {"model": ErrorResponse}},
)
def inativar_tipo_documento(
    codigo: str,
    repo: Annotated[RepositorioTipoDocumental, Depends(get_tipo_documental_repository)],
) -> TipoDocumentoResponse:
    """Inativa um tipo documental (não permite exclusão física)."""
    try:
        use_case = InativarTipoDocumentoUseCase(repo)
        resultado = use_case.execute(codigo)
        return _tipo_documento_to_response(resultado)
    except TipoDocumentalInvalidoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc




# Mappers
# =============================================================================


def _documento_to_response(documento) -> DocumentoResponse:
    """Converte entidade de domínio para response."""
    return DocumentoResponse(
        id=documento.id,
        codigo=documento.codigo,
        numero=documento.numero,
        ano=documento.ano,
        tipo_documental_id=documento.tipo_documental_id,
        titulo=documento.titulo,
        descricao=documento.descricao if documento.descricao else None,
        data_criacao=documento.data_criacao,
        data_recebimento=documento.data_recebimento,
        data_arquivamento=documento.data_arquivamento,
        data_encerramento=documento.data_encerramento,
        data_eliminacao=documento.data_eliminacao,
        unidade_autor_id=documento.unidade_autor_id,
        unidade_arquivo_id=documento.unidade_arquivo_id if documento.unidade_arquivo_id else None,
        processo_id=documento.processo_id if documento.processo_id else None,
        status=documento.status.value,
        is_sigiloso=documento.is_sigiloso,
        conteudo_ref=documento.conteudo_ref if documento.conteudo_ref else None,
        hash_integridade=documento.hash_integridade if documento.hash_integridade else None,
        created_at=documento.created_at,
        updated_at=documento.updated_at,
        created_by=documento.created_by if documento.created_by else None,
        updated_by=documento.updated_by if documento.updated_by else None,
    )


def _arquivamento_to_response(arquivamento) -> ArquivamentoResponse:
    """Converte entidade de arquivamento para response."""
    return ArquivamentoResponse(
        id=arquivamento.id,
        documento_id=arquivamento.documento_id,
        data_arquivamento=arquivamento.data_arquivamento,
        data_restauracao=arquivamento.data_restauracao,
        created_by=arquivamento.created_by or None,
        observacao=arquivamento.observacao or None,
        is_restaurado=arquivamento.is_restaurado,
    )


def _assinatura_to_response(assinatura) -> AssinaturaResponse:
    """Converte entidade de assinatura para response."""
    return AssinaturaResponse(
        id=assinatura.id,
        documento_id=assinatura.documento_id,
        signatario_id=assinatura.signatario_id,
        data_assinatura=assinatura.data_assinatura,
        hash_assinatura=assinatura.hash_assinatura,
        certificado_id=assinatura.certificado_id or None,
        is_valida=assinatura.is_valida,
        is_revogada=assinatura.is_revogada,
    )


def _versao_to_response(versao) -> VersaoDocumentoResponse:
    """Converte entidade de versão para response."""
    return VersaoDocumentoResponse(
        id=versao.id,
        documento_id=versao.documento_id,
        numero_versao=versao.numero_versao,
        conteudo_ref=versao.conteudo_ref or None,
        hash_integridade=versao.hash_integridade or None,
        data_versao=versao.data_versao,
        created_by=versao.created_by or None,
    )


def _tramitacao_to_response(tramitacao) -> TramitacaoResponse:
    """Converte entidade de tramitação para response."""
    return TramitacaoResponse(
        id=tramitacao.id,
        documento_id=tramitacao.documento_id,
        unidade_origem_id=tramitacao.unidade_origem_id,
        unidade_destino_id=tramitacao.unidade_destino_id,
        tipo=tramitacao.tipo.value,
        data_envio=tramitacao.data_envio,
        data_recebimento=tramitacao.data_recebimento,
        data_devolucao=tramitacao.data_devolucao,
        motivo=tramitacao.motivo if tramitacao.motivo else None,
        observacao=tramitacao.observacao if tramitacao.observacao else None,
        created_at=tramitacao.created_at,
    )


def _classificacao_to_response(classificacao) -> ClassificacaoResponse:
    """Converte entidade de classificação para response."""
    return ClassificacaoResponse(
        id=classificacao.id,
        codigo=classificacao.codigo,
        nome=classificacao.nome,
        descricao=classificacao.descricao,
        nivel=classificacao.nivel,
        classificacao_pai_id=classificacao.classificacao_pai_id or None,
        prazo_retencao=classificacao.prazo_retencao,
        unidade_destino_id=classificacao.unidade_destino_id or None,
        created_at=classificacao.created_at,
        is_active=classificacao.is_active,
    )


def _processo_to_response(processo) -> ProcessoDocumentoResponse:
    """Converte entidade de processo para response."""
    return ProcessoDocumentoResponse(
        id=processo.id,
        numero=processo.numero,
        ano=processo.ano,
        tipo_processo_id=processo.tipo_processo_id,
        titulo=processo.titulo,
        descricao=processo.descricao or None,
        unidade_autor_id=processo.unidade_autor_id,
        data_abertura=processo.data_abertura,
        data_encerramento=processo.data_encerramento,
        status=processo.status,
        created_at=processo.created_at,
        is_active=processo.is_active,
    )


def _tipo_documento_to_response(tipo) -> TipoDocumentoResponse:
    """Converte DTO/output de tipo documental para response."""
    return TipoDocumentoResponse(
        id=tipo.id,
        codigo=tipo.codigo,
        nome=tipo.nome,
        descricao=tipo.descricao or None,
        is_ativo=tipo.is_ativo,
    )


__all__ = ["router"]
