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
from src.modules.sigmun_compras.presentation.api.compras_router import (
    router as compras_router,
)
from src.modules.sigmun_compras.presentation.api.auditoria_router import (
    router as auditoria_router,
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
from src.modules.sigmun_cadastro.presentation.api.pessoas_router import (
    router as pessoas_router,
)
from src.modules.sigmun_cadastro.presentation.api.unidades_router import (
    router as unidades_router,
)
from src.modules.sigmun_dad.presentation.api import (
    router as dad_router,
)
from src.modules.sigmun_idn.presentation.api import (
    router as idn_router,
)
from src.modules.sigmun_met.presentation.api import (
    router as met_router,
)
from src.shared.config.logging_config import setup_logging
from src.shared.config.settings import settings
from src.shared.middleware.correlation_id_middleware import CorrelationIDMiddleware

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
        "Domínio-piloto: Gestão de Compras e Contratações (DOM-COMPRAS-001)."
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
            "description": (
                "Estrutura organizacional hierárquica do município (DOM-CUM)."
            ),
        },
        {
            "name": "Identidade e Acesso",
            "description": (
                "Gerenciamento de usuários, roles, permissões e autenticação (DOM-IDN)."
            ),
        },
        {
            "name": "Dados Corporativos",
            "description": (
                "Catálogo de dados, linhagem, políticas e qualidade (DOM-DAD)."
            ),
        },
        {
            "name": "Metadados Corporativos",
            "description": (
                "Metadados, classificações e taxonomias corporativas (DOM-MET)."
            ),
        },
    ],
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correlation ID Middleware (P-002)
app.add_middleware(CorrelationIDMiddleware)


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
async def startup_event():
    """Executado na inicialização da aplicação."""
    status_banco = _verificar_banco()
    logger.info("SIGMUN API iniciada", extra={"extra_data": {
        "version": "0.1.0",
        "environment": settings.APP_ENV,
        "database": status_banco,
    }})


@app.on_event("shutdown")
async def shutdown_event():
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
app.include_router(dad_router)
app.include_router(met_router)


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
