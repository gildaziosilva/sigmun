"""Commands de aplicação do agregado Pessoa (DOM-CUM).

Agrupados por agregado (diferente do padrão 1-arquivo-por-command do
COMPRAS) para conter a proliferação de arquivos; a imutabilidade e o
padrão frozen-dataclass são preservados.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID, uuid4

from src.modules.sigmun_cadastro.domain.entities.contato import TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import TipoEndereco
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    DadosFisicos,
    DadosJuridicos,
    Sexo,
    TipoPessoa,
)


def _novo_id() -> UUID:
    return uuid4()


def _agora() -> datetime:
    return datetime.now()


@dataclass(frozen=True)
class CriarPessoaCommand:
    """Registro de uma nova pessoa (com endereços/documentos/contatos)."""

    tipo: TipoPessoa
    categoria: CategoriaPessoa
    usuario_id: UUID | None = None
    unidade_id: UUID | None = None
    nome: str | None = None  # PF
    data_nascimento: date | None = None  # PF
    sexo: Sexo | None = None  # PF
    estado_civil: str | None = None  # PF
    mae: str | None = None  # PF (LGPD: sensível)
    pai: str | None = None  # PF (LGPD: sensível)
    razao_social: str | None = None  # PJ
    nome_fantasia: str | None = None  # PJ
    cnae_principal: str | None = None  # PJ
    capital: Decimal | None = None  # PJ
    enderecos: list[dict] = field(default_factory=list)
    documentos: list[dict] = field(default_factory=list)
    contatos: list[dict] = field(default_factory=list)

    def dados_fisicos(self) -> DadosFisicos | None:
        """Monta a extensão física quando ``tipo`` é FISICA."""
        if self.tipo is not TipoPessoa.FISICA:
            return None
        return DadosFisicos(
            nome=self.nome or "",
            data_nascimento=self.data_nascimento,
            sexo=self.sexo,
            estado_civil=self.estado_civil,
            mae=self.mae,
            pai=self.pai,
        )

    def dados_juridicos(self) -> DadosJuridicos | None:
        """Monta a extensão jurídica quando ``tipo`` é JURIDICA."""
        if self.tipo is not TipoPessoa.JURIDICA:
            return None
        return DadosJuridicos(
            razao_social=self.razao_social or "",
            nome_fantasia=self.nome_fantasia,
            cnae_principal=self.cnae_principal,
            capital=self.capital,
        )


@dataclass(frozen=True)
class AtualizarPessoaFisicaCommand:
    """Atualização de dados de pessoa física (PATCH parcial)."""

    pessoa_id: UUID
    usuario_id: UUID | None = None
    nome: str | None = None
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None
    pai: str | None = None


@dataclass(frozen=True)
class AtualizarPessoaJuridicaCommand:
    """Atualização de dados de pessoa jurídica (PATCH parcial)."""

    pessoa_id: UUID
    usuario_id: UUID | None = None
    razao_social: str | None = None
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None


@dataclass(frozen=True)
class AlterarCategoriaPessoaCommand:
    """Alteração da categoria cadastral da pessoa."""

    pessoa_id: UUID
    categoria: CategoriaPessoa
    usuario_id: UUID | None = None


@dataclass(frozen=True)
class ExcluirPessoaCommand:
    """Exclusão lógica da pessoa (RN-CUM-007)."""

    pessoa_id: UUID
    usuario_id: UUID


@dataclass(frozen=True)
class AdicionarEnderecoCommand:
    """Adição de endereço ao agregado (RN-CUM-005)."""

    pessoa_id: UUID
    tipo: TipoEndereco
    logradouro: str
    numero: str
    usuario_id: UUID | None = None
    complemento: str | None = None
    bairro: str | None = None
    cep: str | None = None
    cidade: str | None = None
    estado: str | None = None
    pais: str | None = None
    principal: bool = False


@dataclass(frozen=True)
class AdicionarDocumentoCommand:
    """Adição de documento ao agregado (RN-CUM-002/003/004/006)."""

    pessoa_id: UUID
    tipo: TipoDocumento
    numero: str
    usuario_id: UUID | None = None
    orgao_emissor: str | None = None
    data_emissao: date | None = None
    data_validade: date | None = None
    principal: bool = False


@dataclass(frozen=True)
class AdicionarContatoCommand:
    """Adição de contato ao agregado."""

    pessoa_id: UUID
    tipo: TipoContato
    valor: str
    usuario_id: UUID | None = None
    principal: bool = False


__all__ = [
    "CriarPessoaCommand",
    "AtualizarPessoaFisicaCommand",
    "AtualizarPessoaJuridicaCommand",
    "AlterarCategoriaPessoaCommand",
    "ExcluirPessoaCommand",
    "AdicionarEnderecoCommand",
    "AdicionarDocumentoCommand",
    "AdicionarContatoCommand",
]
