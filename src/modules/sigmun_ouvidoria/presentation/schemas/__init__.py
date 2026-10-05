"""Schemas Pydantic do DOM-OUV - Ouvidoria FalaBR / e-OUV municipal."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field

# ==================== Value Objects Schemas ====================


class ProtocoloSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    numero: str
    ano: int

    @property
    def codigo(self) -> str:
        return f"{self.ano}-{self.numero}"


class DadosCidadaoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # `nome` é opcional porque a denúncia anônima — o caso padrão do FalaBR —
    # não possui identificação. `DadosCidadao.para_exibicao()` devolve apenas
    # `{"anonimo": True}` nesse cenário, e exigir `nome` faria toda denúncia
    # anônima falhar na serialização com HTTP 500.
    nome: str | None = None
    cpf: str | None = None
    email: str | None = None
    telefone: str | None = None
    endereco: str | None = None
    anonimo: bool = False


class PrazoRespostaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    data_limite: date
    dias_uteis: int
    prorrogado: bool = False
    data_prorrogacao: date | None = None
    justificativa_prorrogacao: str = ""

    @property
    def vencido(self) -> bool:
        return date.today() > self.data_limite

    @property
    def dias_restantes(self) -> int:
        delta = self.data_limite - date.today()
        return max(0, delta.days)


class AnexoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    nome_arquivo: str
    tipo_mime: str
    tamanho_bytes: int
    url: str
    descricao: str = ""
    criado_em: datetime


class TramitacaoSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    status_anterior: str | None = None
    status_novo: str
    observacao: str | None = None
    usuario_id: str
    created_at: datetime


# ==================== Request Schemas ====================


class RegistrarManifestacaoRequest(BaseModel):
    tipo: str = Field(default="solicitacao", pattern="^(sugestao|elogio|reclamacao|solicitacao)$")
    assunto: str = Field(..., min_length=1, max_length=200)
    descricao: str = Field(..., min_length=1)
    cidadao_nome: str = ""
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    cidadao_anonimo: bool = False
    canal: str = Field(
        default="portal_cidadao",
        pattern="^(portal_cidadao|presencial|telefone|email|correios|aplicativo|outro)$",
    )
    orgao_destino: str = Field(..., min_length=1)
    setor_responsavel: str = ""
    prioridade: str = Field(default="normal", pattern="^(baixa|normal|alta|urgente)$")
    anexos: list[AnexoSchema] = []
    autor_id: str = ""


class RegistrarDenunciaRequest(BaseModel):
    assunto: str = Field(..., min_length=1, max_length=200)
    descricao: str = Field(..., min_length=1)
    tipo_denuncia: str = Field(
        default="outro",
        pattern="^(corrupcao|improbidade|assedio|desvio_verba|nepotismo|fraude_licitacao|outro)$",
    )
    envolve_servidor_publico: bool = False
    servidor_envolvido: str = ""
    valor_envolvido: float | None = None
    local_fato: str = Field(..., min_length=1)
    data_fato: date
    cidadao_nome: str = ""
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    cidadao_anonimo: bool = True
    canal: str = Field(
        default="portal_cidadao",
        pattern="^(portal_cidadao|presencial|telefone|email|correios|aplicativo|outro)$",
    )
    orgao_destino: str = Field(..., min_length=1)
    setor_responsavel: str = ""
    prioridade: str = Field(default="alta", pattern="^(baixa|normal|alta|urgente)$")
    anexos: list[AnexoSchema] = []
    autor_id: str = ""


class RegistrarPedidoLaiRequest(BaseModel):
    assunto: str = Field(..., min_length=1, max_length=200)
    descricao: str = Field(..., min_length=1)
    informacao_solicitada: str = Field(..., min_length=1)
    fundamentacao: str = Field(..., min_length=1)
    nivel_sigilo: str = Field(
        default="publico", pattern="^(publico|restrito|sigiloso|ultra_sigiloso)$"
    )
    fundamentacao_sigilo: str = ""
    dados_pessoais_terceiros: bool = False
    formato_resposta: str = Field(default="digital", pattern="^(digital|fisico|presencial)$")
    cidadao_nome: str = Field(..., min_length=1)
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    canal: str = Field(
        default="portal_cidadao",
        pattern="^(portal_cidadao|presencial|telefone|email|correios|aplicativo|outro)$",
    )
    orgao_destino: str = Field(..., min_length=1)
    setor_responsavel: str = ""
    prioridade: str = Field(default="normal", pattern="^(baixa|normal|alta|urgente)$")
    anexos: list[AnexoSchema] = []
    # ADR-0008 §2.1: `autor_id` não é mais aceito do corpo. Mantido apenas
    # para leitura (clientes legados) e **ignorado** — a identidade vem do token.
    autor_id: str = Field(default="", deprecated=True, exclude=True)


class ResponderManifestacaoRequest(BaseModel):
    resposta: str = Field(..., min_length=1)
    forma_resposta: str = Field(
        default="portal", pattern="^(portal|email|correios|presencial|telefone)$"
    )
    # ADR-0008 §2.1: `respondido_por` vem do token, não do corpo.
    respondido_por: str = Field(default="", deprecated=True, exclude=True)


class AlterarStatusRequest(BaseModel):
    novo_status: str = Field(
        ...,
        pattern="^(registrada|em_analise|encaminhada|em_tratamento|aguardando_complementacao|respondida|concluida|arquivada|cancelada)$",
    )
    observacao: str = ""
    usuario_id: str = Field(default="", deprecated=True, exclude=True)


class ProrrogarPrazoRequest(BaseModel):
    justificativa: str = Field(..., min_length=1)
    usuario_id: str = Field(default="", deprecated=True, exclude=True)


class AvaliarManifestacaoRequest(BaseModel):
    nota: int = Field(..., ge=1, le=5)
    comentario: str = ""


class EncaminharDenunciaRequest(BaseModel):
    orgao: str = Field(..., pattern="^(MP|PF|TCE|TCU|CGU)$")
    numero_processo: str = Field(..., min_length=1)
    usuario_id: str = Field(default="", deprecated=True, exclude=True)


class InterporRecursoLaiRequest(BaseModel):
    autor_id: str = Field(default="", deprecated=True, exclude=True)


class DecidirRecursoLaiRequest(BaseModel):
    deferido: bool
    fundamentacao: str = Field(..., min_length=1)
    usuario_id: str = Field(default="", deprecated=True, exclude=True)


class ListarManifestacoesRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    status: str | None = None
    tipo: str | None = None
    orgao_destino: str | None = None
    cidadao_nome: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None


# ==================== Response Schemas ====================


class ManifestacaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    protocolo: ProtocoloSchema | None = None
    tipo: str
    status: str
    prioridade: str
    assunto: str
    descricao: str
    cidadao: DadosCidadaoSchema | None = None
    canal: str
    orgao_destino: str
    setor_responsavel: str | None = None
    prazo: PrazoRespostaSchema | None = None
    anexos: list[AnexoSchema] = []
    tramitacoes: list[TramitacaoSchema] = []
    resposta: str | None = None
    forma_resposta: str | None = None
    data_resposta: date | None = None
    respondido_por: str | None = None
    avaliacao_cidadao: int | None = None
    comentario_avaliacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str
    updated_by: str | None = None
    is_deleted: bool = False


class DenunciaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    protocolo: ProtocoloSchema | None = None
    tipo: str
    status: str
    prioridade: str
    assunto: str
    descricao: str
    cidadao: DadosCidadaoSchema | None = None
    canal: str
    orgao_destino: str
    setor_responsavel: str | None = None
    prazo: PrazoRespostaSchema | None = None
    anexos: list[AnexoSchema] = []
    tramitacoes: list[TramitacaoSchema] = []
    resposta: str | None = None
    forma_resposta: str | None = None
    data_resposta: date | None = None
    respondido_por: str | None = None
    tipo_denuncia: str
    envolve_servidor_publico: bool
    servidor_envolvido: str | None = None
    valor_envolvido: float | None = None
    local_fato: str
    data_fato: date
    sigilo_denunciante: bool
    encaminhada_mp: bool
    encaminhada_pf: bool
    encaminhada_tce: bool
    numero_inquerito: str | None = None
    resultado_investigacao: str | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str
    updated_by: str | None = None
    is_deleted: bool = False


class PedidoLaiResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    protocolo: ProtocoloSchema | None = None
    tipo: str
    status: str
    prioridade: str
    assunto: str
    descricao: str
    cidadao: DadosCidadaoSchema | None = None
    canal: str
    orgao_destino: str
    setor_responsavel: str | None = None
    prazo: PrazoRespostaSchema | None = None
    anexos: list[AnexoSchema] = []
    tramitacoes: list[TramitacaoSchema] = []
    resposta: str | None = None
    forma_resposta: str | None = None
    data_resposta: date | None = None
    respondido_por: str | None = None
    informacao_solicitada: str
    fundamentacao: str
    nivel_sigilo: str
    fundamentacao_sigilo: str | None = None
    dados_pessoais_terceiros: bool
    formato_resposta: str
    is_recurso: bool
    pedido_original_id: str | None = None
    decisao_recurso: str | None = None
    data_decisao_recurso: date | None = None
    created_at: datetime
    updated_at: datetime | None = None
    created_by: str
    updated_by: str | None = None
    is_deleted: bool = False


class PageResponse(BaseModel):
    items: list
    total: int
    page: int
    page_size: int
    pages: int


class EstatisticasResponse(BaseModel):
    gerais: dict
    por_tipo: dict
    vencendo_5_dias: int
    vencendo_10_dias: int


__all__ = [
    "ProtocoloSchema",
    "DadosCidadaoSchema",
    "PrazoRespostaSchema",
    "AnexoSchema",
    "TramitacaoSchema",
    "RegistrarManifestacaoRequest",
    "RegistrarDenunciaRequest",
    "RegistrarPedidoLaiRequest",
    "ResponderManifestacaoRequest",
    "AlterarStatusRequest",
    "ProrrogarPrazoRequest",
    "AvaliarManifestacaoRequest",
    "EncaminharDenunciaRequest",
    "InterporRecursoLaiRequest",
    "DecidirRecursoLaiRequest",
    "ListarManifestacoesRequest",
    "ManifestacaoResponse",
    "DenunciaResponse",
    "PedidoLaiResponse",
    "PageResponse",
    "EstatisticasResponse",
]
