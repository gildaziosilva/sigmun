"""Schemas Pydantic para Credenciais (DOM-SEG)."""

from datetime import datetime

from pydantic import BaseModel, Field


class CredencialPayload(BaseModel):
    """Payload de criação de uma credencial de acesso."""

    usuario_id: str = Field(min_length=1, description="Identificador do usuário")
    identificador: str = Field(min_length=1, description="Hash ou referência (nunca o valor real)")
    tipo: str = Field(default="senha", description="tipo: senha, certificado, chave_api, token")


class CredencialResponse(BaseModel):
    """Resposta de uma credencial de acesso."""

    id: str
    usuario_id: str
    tipo: str
    identificador: str
    status: str
    tentativas_falhas: int = 0
    validade: datetime | None = None
    ultimo_uso: datetime | None = None
    is_deleted: bool = False
