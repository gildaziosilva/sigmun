"""
SIGMUN — Sistema Integrado de Gestão Municipal
Ponto de entrada da aplicação backend.

Baseado na arquitetura definida em:
SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md
"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from src.core.infrastructure.database.session import engine
from src.modules.sigmun_assistencia_social.presentation.api import (
    routers as ass_routers,
)
from src.modules.sigmun_ate.presentation.api import (
    router as ate_router,
)
from src.modules.sigmun_cadastro.presentation.api.pessoas_router import (
    router as pessoas_router,
)
from src.modules.sigmun_cadastro.presentation.api.unidades_router import (
    router as unidades_router,
)
from src.modules.sigmun_cadastro_imobiliario.presentation.api import (
    routers as imo_routers,
)
from src.modules.sigmun_compras.presentation.api.auditoria_router import (
    router as auditoria_router,
)
from src.modules.sigmun_compras.presentation.api.compras_router import (
    router as compras_router,
)
from src.modules.sigmun_compras.presentation.api.contratos_router import (
    router as contratos_router,
)
from src.modules.sigmun_compras.presentation.api.fornecedores_router import (
    router as fornecedores_router,
)
from src.modules.sigmun_compras.presentation.api.itens_compras_router import (
    router as itens_compras_router,
)
from src.modules.sigmun_compras.presentation.api.processo_documental_router import (
    router as processo_documental_router,
)
from src.modules.sigmun_con.presentation.api import routers as con_routers
from src.modules.sigmun_dad.presentation.api import (
    router as dad_router,
)
from src.modules.sigmun_dia.presentation.api import (
    router as dia_router,
)
from src.modules.sigmun_educacao.presentation.api import (
    routers as edu_routers,
)
from src.modules.sigmun_frotas.presentation.api import (
    routers as fro_routers,
)
from src.modules.sigmun_gdo.presentation.api import (
    router as gdo_router,
)
from src.modules.sigmun_geoinformacao.presentation.api import (
    routers as geo_routers,
)
from src.modules.sigmun_idn.presentation.api import (
    router as idn_router,
)
from src.modules.sigmun_int.presentation.api import (
    router as int_router,
)
from src.modules.sigmun_met.presentation.api import (
    router as met_router,
)
from src.modules.sigmun_obras.presentation.api import (
    routers as obr_routers,
)
from src.modules.sigmun_orc.presentation.api import routers as orc_routers
from src.modules.sigmun_ouvidoria.presentation.api import (
    router as ouv_router,
)
from src.modules.sigmun_patrimonio.presentation.api import (
    routers as pat_routers,
)
from src.modules.sigmun_rh.presentation.api import routers as pes_routers
from src.modules.sigmun_saude.presentation.api import (
    routers as sau_routers,
)
from src.modules.sigmun_seg.presentation.api import (
    router as seg_router,
)
from src.modules.sigmun_territorial.presentation.api import (
    routers as tel_routers,
)
from src.modules.sigmun_tributos.presentation.api import (
    routers as tri_routers,
)
from src.shared.config.logging_config import setup_logging
from src.shared.config.settings import settings
from src.shared.middleware.correlation_id_middleware import CorrelationIDMiddleware
from src.shared.middleware.rate_limit_middleware import RateLimitMiddleware
from src.shared.presentation.erros import (
    ErrorCodes,
    ErrorDetail,
    ErrorEnvelope,
    ErrorResponse,
)
from src.shared.config.logging_config import get_correlation_id

# Configura logging estruturado (P-002)
setup_logging(
    log_level=settings.LOG_LEVEL,
    log_file=os.getenv("LOG_FILE", "logs/app.log"),
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SIGMUN API",
    description=(
        "API do Sistema Integrado de Gestão Municipal da Prefeitura Municipal de Camacan-BA. "
        "Domínio-piloto: Gestão de Compras e Contratações (DOM-COM)."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "Equipe SIGMUN",
        "url": "https://camacan.ba.gov.br",
        "email": "ti@camacan.ba.gov.br",
    },
    license_info={
        "name": "Proprietário - Prefeitura Municipal de Camacan/BA",
        "identifier": "PROPRIETARY",
    },
    openapi_tags=[
        {
            "name": "Compras - Fornecedores",
            "description": "Cadastro e gestão de fornecedores (ENT-COMPRAS-007).",
        },
        {
            "name": "Compras - Itens",
            "description": "Itens e produtos/serviços das compras (ENT-COMPRAS-005).",
        },
        {
            "name": "Compras - Processos",
            "description": "Processos de compras com máquina de estados (ENT-COMPRAS-003).",
        },
        {
            "name": "Compras - Contratos",
            "description": "Contratos da formalização da contratação (ENT-COMPRAS-009).",
        },
        {
            "name": "Compras - Processos Documentais",
            "description": "Processos documentais administrativos (core.processos_documentais).",
        },
        {
            "name": "Compras - Auditoria",
            "description": (
                "Trilha de auditoria do domínio (017-Modelo-de-Auditoria). "
                "Acesso restrito aos perfis autorizados."
            ),
        },
        {
            "name": "Cadastro - Pessoas",
            "description": (
                "Cadastro Único Municipal: pessoas físicas/jurídicas com "
                "endereços, documentos e contatos (DOM-CUM)."
            ),
        },
        {
            "name": "Cadastro - Unidades Administrativas",
            "description": ("Estrutura organizacional hierárquica do município (DOM-CUM)."),
        },
        {
            "name": "Identidade e Acesso",
            "description": (
                "Gerenciamento de usuários, roles, permissões e autenticação (DOM-IDN)."
            ),
        },
        {
            "name": "Dados Corporativos",
            "description": ("Catálogo de dados, linhagem, políticas e qualidade (DOM-DAD)."),
        },
        {
            "name": "Metadados Corporativos",
            "description": ("Metadados, classificações e taxonomias corporativas (DOM-MET)."),
        },
        {
            "name": "Gestão Documental",
            "description": (
                "Documentos digitais, tramitação, processos documentais, "
                "classificação e temporalidade (DOM-GDO)."
            ),
        },
        {
            "name": "Integração e Interoperabilidade",
            "description": (
                "Catálogo de APIs, contratos, conectores oficiais, "
                "webhooks e barramento de eventos (DOM-INT)."
            ),
        },
        {
            "name": "Gestão de Diárias, Viagens e Deslocamentos",
            "description": (
                "Diárias oficiais, viagens, deslocamentos e prestação de contas (DOM-DIA)."
            ),
        },
        {
            "name": "Gestão de Pessoas",
            "description": (
                "Servidores, cargos, lotações, folha de pagamento, férias e frequência (DOM-PES)."
            ),
        },
        {
            "name": "Administracao Tributaria",
            "description": (
                "IPTU, ISSQN, ITBI, taxas municipais, certidões, "
                "contribuintes e dívida ativa (DOM-TRI)."
            ),
        },
        {
            "name": "Gestao Patrimonial",
            "description": (
                "Bens móveis/imóveis, tombamento, depreciação e transferências (DOM-PAT)."
            ),
        },
        {
            "name": "Gestao de Frota",
            "description": ("Veículos, abastecimento, manutenções e rotas (DOM-FRO)."),
        },
        {
            "name": "Saude Municipal",
            "description": (
                "Pacientes, prontuário, agendamento SUS, regulação e farmácia básica (DOM-SAU)."
            ),
        },
        {
            "name": "Educacao Municipal",
            "description": (
                "Matrícula escolar, diário de classe digital, transporte "
                "escolar e merenda (DOM-EDU)."
            ),
        },
        {
            "name": "Assistência Social",
            "description": ("CadÚnico local, benefícios eventuais, CRAS/CREAS (DOM-ASS)."),
        },
        {
            "name": "Geoinformação Municipal",
            "description": (
                "Camadas cartográficas, mapas SIG, composição de camadas, "
                "elementos geoespaciais e serviços publicados (DOM-GEO)."
            ),
        },
        {
            "name": "Obras e Infraestrutura",
            "description": (
                "Obras públicas com acompanhamento físico-financeiro: medições, "
                "despesas, etapas e vistorias (DOM-OBR)."
            ),
        },
    ],
)

# CORS Middleware — T-0.3: origens explícitas; `*` com credenciais é rejeitado.
_CORS_ORIGINS = [o for o in settings.ALLOWED_HOSTS if o != "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_CORS_ORIGINS,
    allow_credentials=bool(_CORS_ORIGINS),
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Correlation-ID"],
)

# Rate limiting + limite de payload — T-0.4.
app.add_middleware(RateLimitMiddleware)

# Correlation ID Middleware (P-002)
app.add_middleware(CorrelationIDMiddleware)


# =============================================================================
# Exception Handlers — T-3.2: Envelope de erro padronizado com correlation_id
# =============================================================================

from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError
from starlette.exceptions import HTTPException as StarletteHTTPException


def _error_envelope(
    code: str,
    message: str,
    status_code: int,
    request: Request,
    details: list[ErrorDetail] | None = None,
) -> JSONResponse:
    """Cria envelope de erro padronizado com correlation_id."""
    corr_id = get_correlation_id()
    if not corr_id or corr_id == "unknown":
        # Fallback: tenta obter do header da requisição
        corr_id = request.headers.get("X-Correlation-ID", "unknown")
    error_response = ErrorResponse(
        error=ErrorEnvelope(
            code=code,
            message=message,
            details=details,
            correlation_id=corr_id,
        )
    )
    return JSONResponse(
        status_code=status_code,
        content=error_response.model_dump(mode="json"),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Trata erros de validação do Pydantic/FastAPI (422)."""
    details = [
        ErrorDetail(
            field=".".join(str(loc) for loc in err["loc"] if loc != "body"),
            issue=err["msg"],
            code=err.get("type"),
        )
        for err in exc.errors()
    ]
    return _error_envelope(
        code=ErrorCodes.VALIDATION_ERROR,
        message="Dados de entrada inválidos",
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        request=request,
        details=details,
    )


@app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
    """Trata erros de validação do Pydantic (model validation)."""
    details = [
        ErrorDetail(
            field=".".join(str(loc) for loc in err["loc"]),
            issue=err["msg"],
            code=err.get("type"),
        )
        for err in exc.errors()
    ]
    return _error_envelope(
        code=ErrorCodes.VALIDATION_ERROR,
        message="Erro de validação",
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        request=request,
        details=details,
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Trata HTTPException genéricos (401, 403, 404, etc.)."""
    # Mapeia status code para código de erro
    code_map = {
        401: ErrorCodes.UNAUTHORIZED,
        403: ErrorCodes.FORBIDDEN,
        404: ErrorCodes.NOT_FOUND,
        409: ErrorCodes.CONFLICT,
        422: ErrorCodes.VALIDATION_ERROR,
    }
    code = code_map.get(exc.status_code, ErrorCodes.INTERNAL_ERROR)
    return _error_envelope(
        code=code,
        message=str(exc.detail),
        status_code=exc.status_code,
        request=request,
    )


@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    """Trata erros de integridade do banco (unique constraint, FK, etc.)."""
    # Tenta extrair detalhe da constraint
    detail = str(exc.orig) if exc.orig else "Violação de integridade"
    return _error_envelope(
        code=ErrorCodes.ALREADY_EXISTS,
        message="Conflito de dados: registro duplicado ou violação de restrição",
        status_code=status.HTTP_409_CONFLICT,
        request=request,
        details=[ErrorDetail(field=None, issue=detail, code="INTEGRITY_ERROR")],
    )


@app.exception_handler(OperationalError)
async def operational_exception_handler(request: Request, exc: OperationalError):
    """Trata erros operacionais do banco (conexão, timeout, etc.)."""
    return _error_envelope(
        code=ErrorCodes.DATABASE_ERROR,
        message="Erro de conexão com o banco de dados",
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        request=request,
        details=[ErrorDetail(field=None, issue=str(exc.orig) if exc.orig else "DB error", code="OPERATIONAL_ERROR")],
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """Trata qualquer exceção não capturada (500)."""
    # Log do erro com stack trace
    logger.error(
        "Erro interno não tratado",
        exc_info=True,
        extra={
            "extra_data": {
                "method": request.method,
                "path": str(request.url.path),
                "error": str(exc),
                "correlation_id": get_correlation_id(),
            }
        },
    )
    return _error_envelope(
        code=ErrorCodes.INTERNAL_ERROR,
        message="Erro interno do servidor",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        request=request,
        details=[ErrorDetail(field=None, issue=str(exc), code="INTERNAL_ERROR")],
    )


def _verificar_banco() -> str:
    """Verifica a conectividade com o PostgreSQL ('up'/'down').

    Usada no startup (log operacional) e no /health. Nunca propaga
    exceção: a API continua de pé mesmo sem banco, reportando 'down'.
    """
    try:
        with engine.connect() as conexao:
            conexao.execute(text("SELECT 1"))
    except Exception:
        logger.warning("Banco de dados inacessível", exc_info=True)
        return "down"
    return "up"


@app.on_event("startup")
async def startup_event() -> None:
    """Executado na inicialização da aplicação."""
    # T-0.3: sem SECRET_KEY válida, o app falha no startup com erro claro.
    settings.validar_para_startup()
    status_banco = _verificar_banco()
    logger.info(
        "SIGMUN API iniciada",
        extra={
            "extra_data": {
                "version": "0.1.0",
                "environment": settings.APP_ENV,
                "database": status_banco,
            }
        },
    )


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Executado no encerramento da aplicação."""
    logger.info("SIGMUN API encerrada")
    try:
        engine.dispose()
    except Exception:  # pragma: no cover - apenas higiene de encerramento
        logger.warning("Falha ao encerrar o pool de conexões", exc_info=True)


app.include_router(fornecedores_router)
app.include_router(itens_compras_router)
app.include_router(compras_router)
app.include_router(processo_documental_router)
app.include_router(contratos_router)
app.include_router(auditoria_router)
app.include_router(pessoas_router)
app.include_router(unidades_router)
app.include_router(idn_router)
app.include_router(seg_router)
app.include_router(dad_router)
app.include_router(met_router)
app.include_router(gdo_router)
app.include_router(int_router)
app.include_router(dia_router)
app.include_router(ate_router)
for _con_router in con_routers:
    app.include_router(_con_router)
for _orc_router in orc_routers:
    app.include_router(_orc_router)
for _pes_router in pes_routers:
    app.include_router(_pes_router)
for _tri_router in tri_routers:
    app.include_router(_tri_router)
for _pat_router in pat_routers:
    app.include_router(_pat_router)
for _fro_router in fro_routers:
    app.include_router(_fro_router)
for _sau_router in sau_routers:
    app.include_router(_sau_router)
app.include_router(ouv_router)
for _edu_router in edu_routers:
    app.include_router(_edu_router)
for _ass_router in ass_routers:
    app.include_router(_ass_router)
for _tel_router in tel_routers:
    app.include_router(_tel_router)
for _imo_router in imo_routers:
    app.include_router(_imo_router)
for _geo_router in geo_routers:
    app.include_router(_geo_router)
for _obr_router in obr_routers:
    app.include_router(_obr_router)


@app.get("/health")
async def health_check() -> dict:
    """Endpoint de verificação de saúde da aplicação.

    ``status`` reflete a saúde do processo da API; ``database`` informa
    a conectividade com o PostgreSQL ('up'/'down') de forma informativa.
    """
    return {
        "status": "healthy",
        "service": "SIGMUN",
        "version": "0.1.0",
        "database": _verificar_banco(),
    }


@app.get("/")
async def root() -> dict:
    """Endpoint raiz da API."""
    return {
        "service": "SIGMUN",
        "description": "Sistema Integrado de Gestão Municipal",
        "version": "0.1.0",
        "documentation": "/docs",
    }
