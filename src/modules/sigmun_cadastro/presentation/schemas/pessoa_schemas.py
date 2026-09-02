"""Schemas de apresentação (Pydantic) para Pessoas (DOM-CUM).

Baseado em:
  - 010-Especificacoes-Cadastro-Unico-Municipal.md (serviços de pessoa)
  - RN-CUM-001 a 006
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.modules.sigmun_cadastro.domain.entities.contato import TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import TipoEndereco
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    Sexo,
    TipoPessoa,
)


# -- Payloads de criação -------------------------------------------------------


class DadosFisicosPayload(BaseModel):
    """Dados da extensão física (pessoa física)."""

    nome: str = Field(..., min_length=1)
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None
    pai: str | None = None


class DadosJuridicosPayload(BaseModel):
    """Dados da extensão jurídica (pessoa jurídica)."""

    razao_social: str = Field(..., min_length=1)
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None


class EnderecoPayload(BaseModel):
    """Endereço embutido no registro da pessoa."""

    tipo: TipoEndereco
    logradouro: str = Field(..., min_length=1)
    numero: str = Field(..., min_length=1)
    complemento: str | None = None
    bairro: str | None = None
    cep: str | None = None
    cidade: str | None = None
    estado: str | None = None
    pais: str | None = None
    principal: bool = False


class DocumentoPayload(BaseModel):
    """Documento embutido no registro da pessoa."""

    tipo: TipoDocumento
    numero: str = Field(..., min_length=1)
    orgao_emissor: str | None = None
    data_emissao: date | None = None
    data_validade: date | None = None
    principal: bool = False


class ContatoPayload(BaseModel):
    """Contato embutido no registro da pessoa."""

    tipo: TipoContato
    valor: str = Field(..., min_length=1)
    principal: bool = False


class PessoaCreateRequest(BaseModel):
    """Payload de registro de pessoa (POST) — RN-CUM-001.

    Os campos de extensão seguem o ``tipo``: FISICA exige ``nome``;
    JURIDICA exige ``razao_social``.
    """

    tipo: TipoPessoa
    categoria: CategoriaPessoa
    unidade_id: UUID | None = None
    # Extensão física (PF)
    nome: str | None = None
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None
    pai: str | None = None
    # Extensão jurídica (PJ)
    razao_social: str | None = None
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None
    # Filhos do agregado
    enderecos: list[EnderecoPayload] = Field(default_factory=list)
    documentos: list[DocumentoPayload] = Field(default_factory=list)
    contatos: list[ContatoPayload] = Field(default_factory=list)

# -- Schemas de resposta --------------------------------------------------------


class DadosFisicosResponse(BaseModel):
    """Extensão física nas respostas."""

    model_config = ConfigDict(from_attributes=True)

    nome: str
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None  # LGPD: dado sensível
    pai: str | None = None  # LGPD: dado sensível


class DadosJuridicosResponse(BaseModel):
    """Extensão jurídica nas respostas."""

    model_config = ConfigDict(from_attributes=True)

    razao_social: str
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None


class EnderecoResponse(BaseModel):
    """Endereço nas respostas (vigência: NULL fim = vigente)."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    tipo: TipoEndereco
    logradouro: str
    numero: str
    complemento: str | None = None
    bairro: str | None = None
    cep: str | None = None
    cidade: str | None = None
    estado: str | None = None
    pais: str | None = None
    principal: bool
    vigencia_inicio: datetime
    vigencia_fim: datetime | None = None


class DocumentoResponse(BaseModel):
    """Documento nas respostas (LGPD: número é dado pessoal)."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    tipo: TipoDocumento
    numero: str
    orgao_emissor: str | None = None
    data_emissao: date | None = None
    data_validade: date | None = None
    principal: bool


class ContatoResponse(BaseModel):
    """Contato nas respostas."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    tipo: TipoContato
    valor: str
    principal: bool


class PessoaResponse(BaseModel):
    """Representação de uma pessoa (com os filhos do agregado)."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    tipo: TipoPessoa
    categoria: CategoriaPessoa
    unidade_id: UUID | None = None
    nome_identificacao: str
    dados_fisicos: DadosFisicosResponse | None = None
    dados_juridicos: DadosJuridicosResponse | None = None
    enderecos: list[EnderecoResponse] = Field(default_factory=list)
    documentos: list[DocumentoResponse] = Field(default_factory=list)
    contatos: list[ContatoResponse] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime


class PessoaListResponse(BaseModel):
    """Envelope paginado de listagem de pessoas."""

    total: int
    page: int
    page_size: int
    items: list[PessoaResponse]


# -- Payloads de atualização e sub-recursos -------------------------------------


class PessoaFisicaUpdateRequest(BaseModel):
    """Atualização parcial dos dados da pessoa física (PATCH)."""

    nome: str | None = None
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None
    pai: str | None = None


class PessoaJuridicaUpdateRequest(BaseModel):
    """Atualização parcial dos dados da pessoa jurídica (PATCH)."""

    razao_social: str | None = None
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None


class CategoriaUpdateRequest(BaseModel):
    """Alteração da categoria cadastral da pessoa."""

    categoria: CategoriaPessoa


class ErrorResponse(BaseModel):
    """Erro padronizado da API."""

    detail: str


__all__ = [
    "DadosFisicosPayload",
    "DadosJuridicosPayload",
    "EnderecoPayload",
    "DocumentoPayload",
    "ContatoPayload",
    "PessoaCreateRequest",
    "DadosFisicosResponse",
    "DadosJuridicosResponse",
    "EnderecoResponse",
    "DocumentoResponse",
    "ContatoResponse",
    "PessoaResponse",
    "PessoaListResponse",
    "PessoaFisicaUpdateRequest",
    "PessoaJuridicaUpdateRequest",
    "CategoriaUpdateRequest",
    "ErrorResponse",
]

