"""Schemas Pydantic para Chaves Criptográficas (DOM-SEG)."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ChavePayload(BaseModel):
    """Payload de criação/atualização de uma chave criptográfica."""

    nome: str = Field(min_length=1, description="Nome da chave")
    algoritmo: str = Field(default="AES256", description="algoritmo: AES256, RSA4096, ECDSA")
    tipo: str = Field(default="simetrica", description="tipo: simetrica, assimetrica")
    tamanho_bits: int = Field(default=256, ge=1, description="Tamanho em bits")
    responsavel_id: str = Field(default="", description="Responsável pela chave")


class ChaveResponse(BaseModel):
    """Resposta de uma chave criptográfica."""

    id: str
    nome: str
    algoritmo: str
    tipo: str
    tamanho_bits: int
    status: str
    responsavel_id: str = ""
    data_expiracao: Optional[datetime] = None
    is_deleted: bool = False