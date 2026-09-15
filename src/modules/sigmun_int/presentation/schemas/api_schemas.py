"""Schemas Pydantic do catálogo de APIs externas (DOM-INT)."""

from datetime import datetime

from pydantic import BaseModel, Field


class ApiPayload(BaseModel):
    """Payload de criação/atualização de uma API externa."""

    codigo: str = Field(..., min_length=2, max_length=50, description="Código único (ej.: API-GOVBR)")
    nome: str = Field(..., min_length=1, description="Nome da API")
    descricao: str = Field(default="", description="Descrição")
    provedor: str = Field(default="", description="Proveedor/expositor da API")
    url_base: str = Field(default="", description="URL base (http/https)")
    tipo: str = Field(default="rest", description="tipo: rest, soap, graphql")
    autenticacao: str = Field(default="oauth2", description="nenhuma, api_key, basic, oauth2, mtls")
    estado: str = Field(default="rascunho", description="rascunho, testes, ativa, inativa, retirada")
    version: str = Field(default="1.0", description="Versão do contrato")
    limite_por_minuto: int = Field(default=300, ge=1, description="Límite de peticiones por minuto")
    timeout_seg: int = Field(default=30, ge=1, le=600, description="Timeout em segundos")


class ApiResponse(BaseModel):
    """Resposta de uma API externa do catálogo."""

    id: str
    codigo: str
    nome: str
    descricao: str = ""
    provedor: str = ""
    url_base: str = ""
    tipo: str
    autenticacao: str
    estado: str
    version: str
    limite_por_minuto: int
    timeout_seg: int
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
    is_deleted: bool = False