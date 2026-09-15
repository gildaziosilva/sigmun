"""API REST de Integração e Interoperabilidade (DOM-INT).

Endpoints para:
- Catálogo de APIs externas e contratos de integração.
- Conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP).
- Webhooks inscritos no barramento e suas entregas (retry/DLQ).
- Barramento de eventos: consumo do outbox de GDO/Compras e despacho para
  webhooks (014-Modelo-de-Integracao).
"""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_int.application.use_cases import (
    AprovarContratoIntegracaoUseCase,
    AtualizarApiExternaUseCase,
    AtualizarConectorUseCase,
    AtualizarContratoIntegracaoUseCase,
    AtualizarWebhookUseCase,
    BuscarApiExternaUseCase,
    BuscarConectorUseCase,
    BuscarContratoIntegracaoUseCase,
    BuscarEntregaWebhookUseCase,
    BuscarWebhookUseCase,
    MudarEstadoApiUseCase,
    MudarEstadoConectorUseCase,
    MudarEstadoWebhookUseCase,
    ConsumirOutboxUseCase,
    CriarApiExternaUseCase,
    CriarConectorUseCase,
    CriarContratoIntegracaoUseCase,
    DeletarApiExternaUseCase,
    DeletarConectorUseCase,
    DeletarContratoIntegracaoUseCase,
    DeletarWebhookUseCase,
    DespacharWebhooksUseCase,
    RegistrarWebhookUseCase,
    RetryEntregaWebhookUseCase,
    RetirarContratoIntegracaoUseCase,
)
from src.modules.sigmun_int.domain.entities import (
    ApiExterna,
    Conector,
    ContratoIntegracao,
    EntregaWebhook,
    EventoProcessado,
    Webhook,
)
from src.modules.sigmun_int.domain.exceptions import (
    ApiExternaJaExisteError,
    ApiExternaNaoEncontradaError,
    ConectorJaExisteError,
    ConectorNaoEncontradoError,
    ContratoIntegracaoJaExisteError,
    ContratoIntegracaoNaoEncontradoError,
    EntregaEstadoInvalidoError,
    EntregaNaoEncontradaError,
    FonteOutboxInvalidaError,
    IntegracaoError,
    OperacaoNaoPermitidaError,
    UrlWebhookInvalidaError,
    WebhookJaExisteError,
    WebhookNaoEncontradoError,
)
from src.modules.sigmun_int.infrastructure.messaging import (
    OutboxSQLAlchemySource,
    TransporteWebhookHTTP,
)
from src.modules.sigmun_int.infrastructure.repositories import (
    SqlAlchemyApiExternaRepository,
    SqlAlchemyConectorRepository,
    SqlAlchemyContratoIntegracaoRepository,
    SqlAlchemyEntregaWebhookRepository,
    SqlAlchemyEventoProcessadoRepository,
    SqlAlchemyWebhookRepository,
)
from src.modules.sigmun_int.presentation.schemas import (
    ApiPayload,
    ApiResponse,
    ConectorEstadoPayload,
    ConectorPayload,
    ConectorResponse,
    ConsumirOutboxPayload,
    ContratoPayload,
    ContratoResponse,
    DespacharPayload,
    EntregaResponse,
    EventoProcessadoResponse,
    ReenfileirarPayload,
    ResumoBarramento,
    WebhookEstadoPayload,
    WebhookPayload,
    WebhookResponse,
)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/int", tags=["Integraci\u00f3n e Interoperabilidade"])


# =============================================================================
# Dependency Injection (repositorios reales sobre a sesión da petición)
# =============================================================================


def get_api_repo(session: Annotated[Session, Depends(get_db)]) -> SqlAlchemyApiExternaRepository:
    return SqlAlchemyApiExternaRepository(session)


def get_contrato_repo(
    session: Annotated[Session, Depends(get_db)],
) -> SqlAlchemyContratoIntegracaoRepository:
    return SqlAlchemyContratoIntegracaoRepository(session)


def get_conector_repo(session: Annotated[Session, Depends(get_db)]) -> SqlAlchemyConectorRepository:
    return SqlAlchemyConectorRepository(session)


def get_webhook_repo(session: Annotated[Session, Depends(get_db)]) -> SqlAlchemyWebhookRepository:
    return SqlAlchemyWebhookRepository(session)


def get_entrega_repo(
    session: Annotated[Session, Depends(get_db)],
) -> SqlAlchemyEntregaWebhookRepository:
    return SqlAlchemyEntregaWebhookRepository(session)


def get_evento_processado_repo(
    session: Annotated[Session, Depends(get_db)],
) -> SqlAlchemyEventoProcessadoRepository:
    return SqlAlchemyEventoProcessadoRepository(session)
# =============================================================================
# Helpers de mapeamento para respostas
# =============================================================================


def _api_to_response(api: ApiExterna) -> ApiResponse:
    return ApiResponse(
        id=api.id,
        codigo=api.codigo,
        nome=api.nome,
        descricao=api.descricao,
        provedor=api.provedor,
        url_base=api.url_base,
        tipo=api.tipo.value,
        autenticacao=api.autenticacao.value,
        estado=api.estado.value,
        version=api.versao,
        limite_por_minuto=api.limite_por_minuto,
        timeout_seg=api.timeout_seg,
        criado_em=api.criado_em,
        atualizado_em=api.atualizado_em,
        is_deleted=api.is_deleted,
    )


def _contrato_to_response(contrato: ContratoIntegracao) -> ContratoResponse:
    return ContratoResponse(
        id=contrato.id,
        codigo=contrato.codigo,
        nome=contrato.nome,
        descricao=contrato.descricao,
        version_formato=contrato.version_formato,
        esquema_ref=contrato.esquema_ref,
        api_externa_id=contrato.api_externa_id or None,
        estado=contrato.estado.value,
        criado_em=contrato.criado_em,
        atualizado_em=contrato.atualizado_em,
        is_deleted=contrato.is_deleted,
    )


def _conector_to_response(conector: Conector) -> ConectorResponse:
    return ConectorResponse(
        id=conector.id,
        codigo=conector.codigo,
        nome=conector.nome,
        descricao=conector.descricao,
        provedor=conector.provedor,
        url_base=conector.url_base,
        autenticacao_tipo=conector.autenticacao_tipo,
        estado=conector.estado.value,
        config=conector.config,
        criado_em=conector.criado_em,
        atualizado_em=conector.atualizado_em,
        is_deleted=conector.is_deleted,
    )


def _webhook_to_response(webhook: Webhook) -> WebhookResponse:
    return WebhookResponse(
        id=webhook.id,
        nome=webhook.nome,
        url_destino=webhook.url_destino,
        segredo_ref=webhook.segredo_ref,
        topicos=webhook.topicos,
        cabecalhos=webhook.cabecalhos,
        estado=webhook.estado.value,
        max_tentativas=webhook.max_tentativas,
        backoff_base_seg=webhook.backoff_base_seg,
        criado_em=webhook.criado_em,
        atualizado_em=webhook.atualizado_em,
        is_deleted=webhook.is_deleted,
    )


def _entrega_to_response(entrega: EntregaWebhook) -> EntregaResponse:
    return EntregaResponse(
        id=entrega.id,
        webhook_id=entrega.webhook_id,
        url_destino=entrega.url_destino,
        topico=entrega.topico,
        evento_nome=entrega.evento_nome,
        agregado_tipo=entrega.agregado_tipo,
        agregado_id=entrega.agregado_id,
        payload=entrega.payload,
        estado=entrega.estado.value,
        tentativas=entrega.tentativas,
        max_tentativas=entrega.max_tentativas,
        ultimo_http_status=entrega.ultimo_http_status,
        ultimo_erro=entrega.ultimo_erro,
        proximo_retry=entrega.proximo_retry,
        criado_em=entrega.criado_em,
        entregue_em=entrega.entregue_em,
        is_deleted=entrega.is_deleted,
    )


def _evento_processado_to_response(evento: EventoProcessado) -> EventoProcessadoResponse:
    return EventoProcessadoResponse(
        id=evento.id,
        fonte=evento.fonte,
        evento_outbox_id=evento.evento_outbox_id,
        topico=evento.topico,
        evento_nome=evento.evento_nome,
        agregado_tipo=evento.agregado_tipo,
        agregado_id=evento.agregado_id,
        payload=evento.payload,
        recebido_em=evento.recebido_em,
        is_deleted=evento.is_deleted,
    )


def _error_http(exc: Exception, default: int = status.HTTP_400_BAD_REQUEST) -> HTTPException:
    """Mapeia exceções de domínio/aplicação para HTTP determinístico."""
    if isinstance(exc, (UrlWebhookInvalidaError, ValueError)):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    if isinstance(
        exc,
        (
            ApiExternaJaExisteError,
            ContratoIntegracaoJaExisteError,
            ConectorJaExisteError,
            WebhookJaExisteError,
            OperacaoNaoPermitidaError,
            EntregaEstadoInvalidoError,
        ),
    ):
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    if isinstance(
        exc,
        (
            ApiExternaNaoEncontradaError,
            ContratoIntegracaoNaoEncontradoError,
            ConectorNaoEncontradoError,
            WebhookNaoEncontradoError,
            EntregaNaoEncontradaError,
        ),
    ):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    if isinstance(exc, FonteOutboxInvalidaError):
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc))
    if isinstance(exc, IntegracaoError):
        return HTTPException(status_code=default, detail=str(exc))
    return HTTPException(status_code=default, detail=str(exc))
# =============================================================================
# APIs externas do catálogo
# =============================================================================


@router.get("/apis", response_model=list[ApiResponse], summary="Lista APIs externas do catálogo")
def listar_apis(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    estado: str | None = Query(default=None),
    tipo: str | None = Query(default=None),
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> list[ApiResponse]:
    items, _ = BuscarApiExternaUseCase(repo).list_all(page, page_size, estado, tipo)
    return [_api_to_response(a) for a in items]


@router.post(
    "/apis",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma API externa no catálogo",
)
def criar_api(
    payload: ApiPayload,
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> ApiResponse:
    try:
        api = CriarApiExternaUseCase(repo).execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao,
            provedor=payload.provedor,
            url_base=payload.url_base,
            tipo=payload.tipo,
            autenticacao=payload.autenticacao,
            estado=payload.estado,
            versao=payload.version,
            limite_por_minuto=payload.limite_por_minuto,
            timeout_seg=payload.timeout_seg,
        )
    except Exception as exc:  # noqa: BLE001 — mapeo centralizado de excepciones de dominio
        raise _error_http(exc) from exc
    return _api_to_response(api)


@router.get("/apis/{api_id}", response_model=ApiResponse, summary="Busca uma API externa por ID")
def obter_api(
    api_id: str,
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> ApiResponse:
    try:
        api = BuscarApiExternaUseCase(repo).get_by_id(api_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _api_to_response(api)


@router.patch("/apis/{api_id}", response_model=ApiResponse, summary="Atualiza uma API externa")
def atualizar_api(
    api_id: str,
    payload: ApiPayload,
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> ApiResponse:
    try:
        api = AtualizarApiExternaUseCase(repo).execute(
            api_id=api_id,
            nome=payload.nome,
            descricao=payload.descricao,
            provedor=payload.provedor,
            url_base=payload.url_base,
            tipo=payload.tipo,
            autenticacao=payload.autenticacao,
            versao=payload.version,
            limite_por_minuto=payload.limite_por_minuto,
            timeout_seg=payload.timeout_seg,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _api_to_response(api)


@router.post("/apis/{api_id}/estado", response_model=ApiResponse, summary="Muda o estado de uma API")
def mudar_estado_api(
    api_id: str,
    estado: str,
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> ApiResponse:
    try:
        api = MudarEstadoApiUseCase(repo).execute(api_id, estado)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _api_to_response(api)


@router.delete(
    "/apis/{api_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Exclui (exclusão lógica) uma API externa",
)
def deletar_api(
    api_id: str,
    repo: Annotated[object, Depends(get_api_repo)] = None,
) -> None:
    try:
        DeletarApiExternaUseCase(repo).execute(api_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
# =============================================================================
# Contratos de integração
# =============================================================================


@router.get(
    "/contratos",
    response_model=list[ContratoResponse],
    summary="Lista contratos de integração",
)
def listar_contratos(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    estado: str | None = Query(default=None),
    api_externa_id: str | None = Query(default=None),
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> list[ContratoResponse]:
    items, _ = BuscarContratoIntegracaoUseCase(repo).list_all(
        page, page_size, estado, api_externa_id
    )
    return [_contrato_to_response(c) for c in items]


@router.post(
    "/contratos",
    response_model=ContratoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crea um contrato de integração",
)
def criar_contrato(
    payload: ContratoPayload,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
    repo_apis: Annotated[object, Depends(get_api_repo)] = None,
) -> ContratoResponse:
    try:
        contrato = CriarContratoIntegracaoUseCase(repo, repo_apis).execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao,
            version_formato=payload.version_formato,
            esquema_ref=payload.esquema_ref,
            api_externa_id=payload.api_externa_id or "",
            estado=payload.estado,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _contrato_to_response(contrato)


@router.get(
    "/contratos/{contrato_id}",
    response_model=ContratoResponse,
    summary="Busca um contrato por ID",
)
def obter_contrato(
    contrato_id: str,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> ContratoResponse:
    try:
        contrato = BuscarContratoIntegracaoUseCase(repo).get_by_id(contrato_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _contrato_to_response(contrato)


@router.patch(
    "/contratos/{contrato_id}",
    response_model=ContratoResponse,
    summary="Atualiza um contrato de integração",
)
def atualizar_contrato(
    contrato_id: str,
    payload: ContratoPayload,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> ContratoResponse:
    try:
        contrato = AtualizarContratoIntegracaoUseCase(repo).execute(
            contrato_id=contrato_id,
            nome=payload.nome,
            descricao=payload.descricao,
            version_formato=payload.version_formato,
            esquema_ref=payload.esquema_ref,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _contrato_to_response(contrato)


@router.post(
    "/contratos/{contrato_id}/aprovar",
    response_model=ContratoResponse,
    summary="Aprova um contrato (rascunho -> vigente)",
)
def aprovar_contrato(
    contrato_id: str,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> ContratoResponse:
    try:
        contrato = AprovarContratoIntegracaoUseCase(repo).execute(contrato_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _contrato_to_response(contrato)


@router.post(
    "/contratos/{contrato_id}/retirar",
    response_model=ContratoResponse,
    summary="Retira um contrato (vigente -> retirado)",
)
def retirar_contrato(
    contrato_id: str,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> ContratoResponse:
    try:
        contrato = RetirarContratoIntegracaoUseCase(repo).execute(contrato_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _contrato_to_response(contrato)


@router.delete(
    "/contratos/{contrato_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Exclui (exclusão lógica) um contrato",
)
def deletar_contrato(
    contrato_id: str,
    repo: Annotated[object, Depends(get_contrato_repo)] = None,
) -> None:
    try:
        DeletarContratoIntegracaoUseCase(repo).execute(contrato_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
# =============================================================================
# Conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP)
# =============================================================================


@router.get(
    "/conectores", response_model=list[ConectorResponse], summary="Lista conectores oficiais"
)
def listar_conectores(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    estado: str | None = Query(default=None),
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> list[ConectorResponse]:
    items, _ = BuscarConectorUseCase(repo).list_all(page, page_size, estado)
    return [_conector_to_response(c) for c in items]


@router.post(
    "/conectores",
    response_model=ConectorResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra um conector oficial",
)
def criar_conector(
    payload: ConectorPayload,
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> ConectorResponse:
    try:
        conector = CriarConectorUseCase(repo).execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao,
            provedor=payload.provedor,
            url_base=payload.url_base,
            autenticacao_tipo=payload.autenticacao_tipo,
            config=payload.config,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _conector_to_response(conector)


@router.get(
    "/conectores/{conector_id}", response_model=ConectorResponse, summary="Busca um conector por ID"
)
def obter_conector(
    conector_id: str,
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> ConectorResponse:
    try:
        conector = BuscarConectorUseCase(repo).get_by_id(conector_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _conector_to_response(conector)


@router.patch(
    "/conectores/{conector_id}", response_model=ConectorResponse, summary="Atualiza um conector"
)
def atualizar_conector(
    conector_id: str,
    payload: ConectorPayload,
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> ConectorResponse:
    try:
        conector = AtualizarConectorUseCase(repo).execute(
            conector_id=conector_id,
            nome=payload.nome,
            descricao=payload.descricao,
            provedor=payload.provedor,
            url_base=payload.url_base,
            autenticacao_tipo=payload.autenticacao_tipo,
            config=payload.config,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _conector_to_response(conector)


@router.post(
    "/conectores/{conector_id}/estado",
    response_model=ConectorResponse,
    summary="Muda o estado de um conector (RN-INT-004)",
)
def mudar_estado_conector(
    conector_id: str,
    payload: ConectorEstadoPayload,
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> ConectorResponse:
    try:
        conector = MudarEstadoConectorUseCase(repo).execute(conector_id, payload.estado)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _conector_to_response(conector)


@router.delete(
    "/conectores/{conector_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Exclui (exclusão lógica) um conector",
)
def deletar_conector(
    conector_id: str,
    repo: Annotated[object, Depends(get_conector_repo)] = None,
) -> None:
    try:
        DeletarConectorUseCase(repo).execute(conector_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
# =============================================================================
# Webhooks inscritos do barramento
# =============================================================================


@router.get("/webhooks", response_model=list[WebhookResponse], summary="Lista webhooks")
def listar_webhooks(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    estado: str | None = Query(default=None),
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> list[WebhookResponse]:
    items, _ = BuscarWebhookUseCase(repo).list_all(page, page_size, estado)
    return [_webhook_to_response(w) for w in items]


@router.post(
    "/webhooks",
    response_model=WebhookResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra um webhook inscrito no barramento",
)
def registrar_webhook(
    payload: WebhookPayload,
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> WebhookResponse:
    try:
        webhook = RegistrarWebhookUseCase(repo).execute(
            nome=payload.nome,
            url_destino=payload.url_destino,
            topicos=payload.topicos,
            segredo_ref=payload.segredo_ref,
            cabecalhos=payload.cabecalhos,
            max_tentativas=payload.max_tentativas,
            backoff_base_seg=payload.backoff_base_seg,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _webhook_to_response(webhook)


@router.get("/webhooks/{webhook_id}", response_model=WebhookResponse, summary="Busca um webhook por ID")
def obter_webhook(
    webhook_id: str,
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> WebhookResponse:
    try:
        webhook = BuscarWebhookUseCase(repo).get_by_id(webhook_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _webhook_to_response(webhook)


@router.patch(
    "/webhooks/{webhook_id}", response_model=WebhookResponse, summary="Atualiza um webhook"
)
def atualizar_webhook(
    webhook_id: str,
    payload: WebhookPayload,
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> WebhookResponse:
    try:
        webhook = AtualizarWebhookUseCase(repo).execute(
            webhook_id=webhook_id,
            url_destino=payload.url_destino,
            segredo_ref=payload.segredo_ref,
            topicos=payload.topicos,
            cabecalhos=payload.cabecalhos,
            max_tentativas=payload.max_tentativas,
            backoff_base_seg=payload.backoff_base_seg,
        )
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _webhook_to_response(webhook)


@router.post(
    "/webhooks/{webhook_id}/estado",
    response_model=WebhookResponse,
    summary="Ativa ou desativa um webhook",
)
def mudar_estado_webhook(
    webhook_id: str,
    payload: WebhookEstadoPayload,
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> WebhookResponse:
    try:
        webhook = MudarEstadoWebhookUseCase(repo).execute(webhook_id, payload.estado)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _webhook_to_response(webhook)


@router.delete(
    "/webhooks/{webhook_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Exclui (exclusão lógica) um webhook",
)
def deletar_webhook(
    webhook_id: str,
    repo: Annotated[object, Depends(get_webhook_repo)] = None,
) -> None:
    try:
        DeletarWebhookUseCase(repo).execute(webhook_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc


# =============================================================================
# Entregas de mensagens (retry / DLQ)
# =============================================================================


@router.get("/entregas", response_model=list[EntregaResponse], summary="Lista entregas de mensagens")
def listar_entregas(
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    estado: str | None = Query(default=None),
    repo: Annotated[object, Depends(get_entrega_repo)] = None,
) -> list[EntregaResponse]:
    items, _ = BuscarEntregaWebhookUseCase(repo).list_all(page, page_size, estado)
    return [_entrega_to_response(e) for e in items]


@router.get(
    "/webhooks/{webhook_id}/entregas",
    response_model=list[EntregaResponse],
    summary="Lista entregas de um webhook",
)
def listar_entregas_por_webhook(
    webhook_id: str,
    page: int = Query(default=0, ge=0),
    page_size: int = Query(default=50, ge=1, le=200),
    repo: Annotated[object, Depends(get_entrega_repo)] = None,
) -> list[EntregaResponse]:
    items, _ = BuscarEntregaWebhookUseCase(repo).list_by_webhook(webhook_id, page, page_size)
    return [_entrega_to_response(e) for e in items]


@router.get(
    "/entregas/{entrega_id}", response_model=EntregaResponse, summary="Busca uma entrega por ID"
)
def obter_entrega(
    entrega_id: str,
    repo: Annotated[object, Depends(get_entrega_repo)] = None,
) -> EntregaResponse:
    try:
        entrega = BuscarEntregaWebhookUseCase(repo).get_by_id(entrega_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _entrega_to_response(entrega)


@router.post(
    "/entregas/{entrega_id}/reenfileirar",
    response_model=EntregaResponse,
    summary="Reenfileira uma entrega da fila de mensagens mortas",
)
def reenfileirar_entrega(
    entrega_id: str,
    payload: ReenfileirarPayload,
    repo: Annotated[object, Depends(get_entrega_repo)] = None,
) -> EntregaResponse:
    try:
        entrega = RetryEntregaWebhookUseCase(repo).execute(entrega_id)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    return _entrega_to_response(entrega)


# =============================================================================
# Barramento de eventos (consumo do Outbox + despacho para webhooks)
# =============================================================================


def get_outbox_source(
    session: Annotated[Session, Depends(get_db)],
) -> OutboxSQLAlchemySource:
    return OutboxSQLAlchemySource(session)


def get_transporte_webhook() -> TransporteWebhookHTTP:
    return TransporteWebhookHTTP()


@router.post(
    "/barras/eventos/consumir",
    summary="Consome eventos pendentes do outbox de um domínio produtor",
    description=(
        "Lê até ``lote`` eventos com status ``pendente`` do schema "
        "``<fonte>.eventos_outbox``, cria entregas para os webhooks inscritos "
        "e marca os eventos como ``publicado`` (RN-INT-003)."
    ),
)
def consumir_outbox(
    payload: ConsumirOutboxPayload,
    outbox: Annotated[OutboxSQLAlchemySource, Depends(get_outbox_source)] = None,
    repo_webhooks: Annotated[object, Depends(get_webhook_repo)] = None,
    repo_entregas: Annotated[object, Depends(get_entrega_repo)] = None,
    repo_eventos: Annotated[object, Depends(get_evento_processado_repo)] = None,
) -> dict:
    try:
        uc = ConsumirOutboxUseCase(outbox, repo_webhooks, repo_entregas, repo_eventos)
        resumo = uc.execute(fonte=payload.fonte, lote=payload.lote)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    logger.info("Outbox consumido [%s]: %s", payload.fonte, resumo)
    return resumo


@router.post(
    "/barras/webhooks/despachar",
    response_model=ResumoBarramento,
    summary="Despacha entregas pendentes para webhooks com retry e backoff",
    description=(
        "Processa as entregas em estado ``pendente`` cujo atraso de retry "
        "expirou, enviando a mensagem HTTP ao webhook de destino. Ao esgotar "
        "``max_tentativas``, a entrega vai para a fila de mensagens mortas (DLQ)."
    ),
)
def despachar_webhooks(
    payload: DespacharPayload,
    repo_entregas: Annotated[object, Depends(get_entrega_repo)] = None,
    transporte: Annotated[TransporteWebhookHTTP, Depends(get_transporte_webhook)] = None,
) -> ResumoBarramento:
    try:
        uc = DespacharWebhooksUseCase(repo_entregas, transporte)
        resumo = uc.execute(lote=payload.lote)
    except Exception as exc:  # noqa: BLE001
        raise _error_http(exc) from exc
    logger.info("Webhooks despachados: %s", resumo)
    return ResumoBarramento(
        processados=resumo["processadas"],
        sucessos=resumo["sucessos"],
        falhas=resumo["falhas"],
        fila_morta=resumo["fila_morta"],
    )