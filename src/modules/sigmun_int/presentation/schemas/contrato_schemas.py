"""Schemas Pydantic de contratos de integração (DOM-INT)."""

from datetime import datetime

from pydantic import BaseModel, Field


class ContratoPayload(BaseModel):
    """Payload de criação de um contrato de integração."""

    codigo: str = Field(..., min_length=2, max_length=50, description="Código único")
    nome: str = Field(..., min_length=1, description="Nome do contrato")
    descricao: str = Field(default="", description="Descrição")
    versao_formato: str = Field(default="1.0", description="Versão do formato da mensagem")
    esquema_ref: str = Field(default="", description="Referência ao schema (URI/JSON Schema)")
    api_externa_id: str | None = Field(default=None, description="ID da API do catálogo")
    estado: str = Field(default="rascunho", description="rascunho, vigente, obsoleto, retirado")


class ContratoResponse(BaseModel):
    """Resposta de um contrato de integração."""

    id: str
    codigo: str
    nome: str
    descricao: str = ""
    versao_formato: str
    esquema_ref: str = ""
    api_externa_id: str | None = None
    estado: str
    criado_em: datetime | None = None
    atualizado_em: datetime | None = None
    is_deleted: bool = False
