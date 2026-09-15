"""Schemas Pydantic para Controles de Segurança (DOM-SEG)."""

from pydantic import BaseModel, Field


class ControlePayload(BaseModel):
    """Payload de criação/atualização de um controle de segurança."""

    codigo: str = Field(min_length=1, max_length=20, description="Código do controle (ex: A.5.1.1)")
    nome: str = Field(min_length=1, description="Nome do controle")
    descricao: str = Field(default="", description="Descrição do controle")
    tipo: str = Field(default="tecnico", description="tipo: fisico, tecnico, administrativo")
    categoria: str = Field(
        default="acesso",
        description="categoria: acesso, criptografia, incidente, conformidade, continuidade",
    )
    status: str = Field(default="planejado", description="status: implementado, parcial, planejado")
    nivel_risco: str = Field(
        default="medio", description="nível de risco: baixo, medio, alto, critico"
    )
    responsavel_id: str = Field(default="", description="Responsável pelo controle")


class ControleResponse(BaseModel):
    """Resposta de um controle de segurança."""

    id: str
    codigo: str
    nome: str
    descricao: str = ""
    tipo: str
    categoria: str
    status: str
    nivel_risco: str
    responsavel_id: str = ""
    is_deleted: bool = False
