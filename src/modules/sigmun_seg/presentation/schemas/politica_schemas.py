"""Schemas Pydantic para Políticas de Segurança (DOM-SEG)."""

from pydantic import BaseModel, Field


class PoliticaPayload(BaseModel):
    """Payload de criação/atualização de uma política de segurança."""

    codigo: str = Field(min_length=1, max_length=20, description="Código da política")
    titulo: str = Field(min_length=1, description="Título da política")
    conteudo: str = Field(min_length=1, description="Conteúdo da política")
    versao: str = Field(default="1.0", description="Versão da política")
    ativa: bool = Field(default=False, description="Indica se a política está ativa")


class PoliticaResponse(BaseModel):
    """Resposta de uma política de segurança."""

    id: str
    codigo: str
    titulo: str
    conteudo: str
    versao: str
    ativa: bool
    is_deleted: bool = False