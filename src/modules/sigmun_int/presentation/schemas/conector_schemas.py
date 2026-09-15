"""Schemas Pydantic de conectores oficiais (DOM-INT)."""

from datetime import datetime

from pydantic import BaseModel, Field


class ConectorPayload(BaseModel):
    """Payload de criação/atualização de um conector oficial."""

    codigo: str = Field(
        ..., min_length=2, max_length=50, description="GOVBR, ESOCIAL, SIAFIC, PNCP..."
    )
    nome: str = Field(default="", description="Nome (se autocompleta si é oficial)")
    descricao: str = Field(default="", description="Descrição")
    provedor: str = Field(default="", description="Proveedor da plataforma")
    url_base: str = Field(default="", description="URL base")
    autenticacao_tipo: str = Field(
        default="oauth2", description="ninguno, api_key, basic, oauth2, mtls"
    )
    config: dict = Field(default_factory=dict, description="Configuración (sin secretos em claro)")


class ConectorEstadoPayload(BaseModel):
    """Payload de cambio de estado de um conector."""

    estado: str = Field(..., description="sem_configuracao, configurado, testes, ativo, inativo")


class ConectorResponse(BaseModel):
    """Resposta de um conector oficial."""

    id: str
    codigo: str
    nome: str
    descricao: str = ""
    provedor: str = ""
    url_base: str = ""
    autenticacao_tipo: str
    estado: str
    config: dict = {}
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
    is_deleted: bool = False
