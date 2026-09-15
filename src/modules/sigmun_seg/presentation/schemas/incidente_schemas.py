"""Schemas Pydantic para Incidentes de Segurança (DOM-SEG)."""

from pydantic import BaseModel, Field


class IncidentePayload(BaseModel):
    """Payload de criação de um incidente de segurança."""

    titulo: str = Field(min_length=1, description="Título do incidente")
    descricao: str = Field(min_length=1, description="Descrição detalhada do incidente")
    severidade: str = Field(default="baixa", description="severidade: baixa, media, alta, critica")
    impacto: str = Field(default="", description="Impacto do incidente")
    categoria: str = Field(default="", description="Categoria do incidente")
    relator_id: str = Field(default="", description="Relator do incidente")


class IncidenteResponse(BaseModel):
    """Resposta de um incidente de segurança."""

    id: str
    titulo: str
    descricao: str
    severidade: str
    impacto: str = ""
    categoria: str = ""
    relator_id: str = ""
    atribuido_a: str = ""
    status: str
    is_deleted: bool = False
