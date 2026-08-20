"""
SIGMUN — Sistema Integrado de Gestão Municipal
Ponto de entrada da aplicação backend.

Baseado na arquitetura definida em:
SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.shared.config.settings import settings

app = FastAPI(
    title="SIGMUN API",
    description="API do Sistema Integrado de Gestão Municipal da Prefeitura Municipal de Camacan-BA",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict:
    """Endpoint de verificação de saúde da aplicação."""
    return {"status": "healthy", "service": "SIGMUN", "version": "0.1.0"}


@app.get("/")
async def root() -> dict:
    """Endpoint raiz da API."""
    return {
        "service": "SIGMUN",
        "description": "Sistema Integrado de Gestão Municipal",
        "version": "0.1.0",
        "documentation": "/docs",
    }
