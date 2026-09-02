"""Agregado Pessoa do Cadastro Único Municipal.

Baseado em:
  - Modelo-Fisico.md §4.1 (core.pessoas / core.pessoas_fisicas /
    core.pessoas_juridicas)
  - 000-Dominio-Cadastro-Unico-Municipal.md §5 (informação mestra)

Regras de negócio implementadas:
  - RN-CUM-001: tipo {FISICA, JURIDICA} exige extensão correspondente
    (pessoa física exige nome; jurídica exige razão social)
  - RN-CUM-002/003: CPF/CNPJ com dígitos verificadores válidos
  - RN-CUM-005: unicidade de endereço principal vigente
  - RN-CUM-006: unicidade de documento/contato principal por tipo
  - RN-CUM-007: exclusão lógica preservando histórico
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4

from src.modules.sigmun_cadastro.domain.entities.contato import Contato, TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import Documento, TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import Endereco, TipoEndereco
from src.modules.sigmun_cadastro.domain.value_objects.cnpj import CNPJ
from src.modules.sigmun_cadastro.domain.value_objects.cpf import CPF
from src.shared.compat import UTC


class TipoPessoa(str, Enum):
    """Natureza da pessoa (constraint ``ck_pessoas_tipo``)."""

    FISICA = "FISICA"
    JURIDICA = "JURIDICA"


class CategoriaPessoa(str, Enum):
    """Categoria da pessoa no cadastro (constraint ``ck_pessoas_categoria``)."""

    CIDADAO = "CIDADAO"
    SERVIDOR = "SERVIDOR"
    FORNECEDOR = "FORNECEDOR"
    AGENTE_EXTERNO = "AGENTE_EXTERNO"


class Sexo(str, Enum):
    """Sexo da pessoa física (constraint do modelo físico)."""

    MASCULINO = "M"
    FEMININO = "F"
    OUTRO = "OUTRO"


@dataclass(frozen=True)
class DadosFisicos:
    """Extensão 1:1 de pessoa física (``core.pessoas_fisicas``)."""

    nome: str
    data_nascimento: date | None = None
    sexo: Sexo | None = None
    estado_civil: str | None = None
    mae: str | None = None
    pai: str | None = None

    def __post_init__(self) -> None:
        if not self.nome or not self.nome.strip():
            raise ValueError("Nome da pessoa física é obrigatório (RN-CUM-001)")


@dataclass(frozen=True)
class DadosJuridicos:
    """Extensão 1:1 de pessoa jurídica (``core.pessoas_juridicas``)."""

    razao_social: str
    nome_fantasia: str | None = None
    cnae_principal: str | None = None
    capital: Decimal | None = None

    def __post_init__(self) -> None:
        if not self.razao_social or not self.razao_social.strip():
            raise ValueError("Razão social da pessoa jurídica é obrigatória (RN-CUM-001)")


class Pessoa:
    """Entidade-mestra: pessoa física ou jurídica do município.

    Raiz do agregado que engloba endereços, documentos e contatos.
    A extensão (``dados_fisicos``/``dados_juridicos``) é condicionada ao
    ``tipo`` (RN-CUM-001).
    """

    def __init__(
        self,
        tipo: TipoPessoa,
        categoria: CategoriaPessoa,
        id: UUID | None = None,
        unidade_id: UUID | None = None,
        dados_fisicos: DadosFisicos | None = None,
        dados_juridicos: DadosJuridicos | None = None,
        enderecos: list[Endereco] | None = None,
        documentos: list[Documento] | None = None,
        contatos: list[Contato] | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        self.id: UUID = id or uuid4()
        self.tipo: TipoPessoa = tipo
        self.categoria: CategoriaPessoa = categoria
        self.unidade_id: UUID | None = unidade_id
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

        # RN-CUM-001: extensão condicionada ao tipo
        if tipo is TipoPessoa.FISICA:
            if dados_fisicos is None:
                raise ValueError("Pessoa física exige dados físicos (RN-CUM-001)")
            if dados_juridicos is not None:
                raise ValueError("Pessoa física não possui dados jurídicos (RN-CUM-001)")
        elif tipo is TipoPessoa.JURIDICA:
            if dados_juridicos is None:
                raise ValueError("Pessoa jurídica exige dados jurídicos (RN-CUM-001)")
            if dados_fisicos is not None:
                raise ValueError("Pessoa jurídica não possui dados físicos (RN-CUM-001)")
        else:
            raise ValueError(f"Tipo de pessoa inválido: {tipo}")
        self.dados_fisicos: DadosFisicos | None = dados_fisicos
        self.dados_juridicos: DadosJuridicos | None = dados_juridicos

        # Filhos do agregado (carregados pelo repositório)
        self.enderecos: list[Endereco] = enderecos or []
        self.documentos: list[Documento] = documentos or []
        self.contatos: list[Contato] = contatos or []

    # -- Identificação ---------------------------------------------------------

    @property
    def nome_identificacao(self) -> str:
        """Nome (PF) ou razão social (PJ) da pessoa."""
        if self.dados_fisicos is not None:
            return self.dados_fisicos.nome
        if self.dados_juridicos is not None:
            return self.dados_juridicos.razao_social
        return ""

    def documento_principal(self, tipo: TipoDocumento) -> Documento | None:
        """Retorna o documento principal vigente do tipo informado."""
        for doc in self.documentos:
            if doc.tipo is tipo and doc.principal and not doc.foi_excluido():
                return doc
        return None

    # -- Comportamentos: endereços (RN-CUM-005) --------------------------------

    def adicionar_endereco(
        self,
        tipo: TipoEndereco,
        logradouro: str,
        numero: str,
        usuario_id: UUID | None = None,
        **campos: object,
    ) -> Endereco:
        """Adiciona um endereço ao agregado.

        Se ``principal``, os demais endereços vigentes deixam de ser
        principais (RN-CUM-005).
        """
        self._garantir_ativa()
        principal = bool(campos.pop("principal", False))
        if principal:
            self._desativar_principais(self.enderecos, usuario_id)
        endereco = Endereco(
            pessoa_id=self.id,
            tipo=tipo,
            logradouro=logradouro,
            numero=numero,
            principal=principal,
            created_by=usuario_id,
            **campos,
        )
        self.enderecos.append(endereco)
        self._registrar_alteracao(usuario_id)
        return endereco

    def remover_endereco(self, endereco_id: UUID, usuario_id: UUID | None = None) -> None:
        """Remove logicamente um endereço (RN-CUM-007)."""
        self._garantir_ativa()
        endereco = next((e for e in self.enderecos if e.id == endereco_id), None)
        if endereco is None or endereco.foi_excluido():
            raise ValueError("Endereço não encontrado para esta pessoa")
        endereco.excluir(usuario_id)
        self._registrar_alteracao(usuario_id)

    # -- Comportamentos: documentos (RN-CUM-002/003/006) -----------------------

    def adicionar_documento(
        self,
        tipo: TipoDocumento,
        numero: str,
        usuario_id: UUID | None = None,
        **campos: object,
    ) -> Documento:
        """Adiciona um documento validando CPF/CNPJ quando aplicável.

        CPF/CNPJ passam pela validação de dígitos verificadores
        (RN-CUM-002/003). Se ``principal``, os demais do mesmo tipo
        deixam de ser principais (RN-CUM-006).
        """
        self._garantir_ativa()
        numero_limpo = numero
        if tipo is TipoDocumento.CPF:
            numero_limpo = CPF(numero).valor
        elif tipo is TipoDocumento.CNPJ:
            numero_limpo = CNPJ(numero).valor
        principal = bool(campos.pop("principal", False))
        if principal:
            for doc in self.documentos:
                if doc.tipo is tipo and not doc.foi_excluido():
                    doc.principal = False
        documento = Documento(
            pessoa_id=self.id,
            tipo=tipo,
            numero=numero_limpo,
            principal=principal,
            created_by=usuario_id,
            **campos,
        )
        self.documentos.append(documento)
        self._registrar_alteracao(usuario_id)
        return documento

    # -- Comportamentos: contatos (RN-CUM-006) ---------------------------------

    def adicionar_contato(
        self,
        tipo: TipoContato,
        valor: str,
        usuario_id: UUID | None = None,
        principal: bool = False,
    ) -> Contato:
        """Adiciona um contato (tel/e-mail/redes/whatsapp) ao agregado."""
        self._garantir_ativa()
        if principal:
            for contato in self.contatos:
                if contato.tipo is tipo and not contato.foi_excluido():
                    contato.principal = False
        contato = Contato(
            pessoa_id=self.id,
            tipo=tipo,
            valor=valor,
            principal=principal,
            created_by=usuario_id,
        )
        self.contatos.append(contato)
        self._registrar_alteracao(usuario_id)
        return contato

    # -- Comportamentos: ciclo de vida ------------------------------------------

    def atualizar_dados_fisicos(
        self,
        usuario_id: UUID | None = None,
        nome: str | None = None,
        data_nascimento: date | None = None,
        sexo: Sexo | None = None,
        estado_civil: str | None = None,
        mae: str | None = None,
        pai: str | None = None,
    ) -> None:
        """Atualiza os dados da pessoa física (somente tipo FISICA)."""
        self._garantir_ativa()
        if self.dados_fisicos is None:
            raise ValueError("Somente pessoa física possui dados físicos (RN-CUM-001)")
        atual = self.dados_fisicos
        self.dados_fisicos = DadosFisicos(
            nome=nome if nome is not None else atual.nome,
            data_nascimento=(
                data_nascimento if data_nascimento is not None else atual.data_nascimento
            ),
            sexo=sexo if sexo is not None else atual.sexo,
            estado_civil=estado_civil if estado_civil is not None else atual.estado_civil,
            mae=mae if mae is not None else atual.mae,
            pai=pai if pai is not None else atual.pai,
        )
        self._registrar_alteracao(usuario_id)

    def atualizar_dados_juridicos(
        self,
        usuario_id: UUID | None = None,
        razao_social: str | None = None,
        nome_fantasia: str | None = None,
        cnae_principal: str | None = None,
        capital: Decimal | None = None,
    ) -> None:
        """Atualiza os dados da pessoa jurídica (somente tipo JURIDICA)."""
        self._garantir_ativa()
        if self.dados_juridicos is None:
            raise ValueError("Somente pessoa jurídica possui dados jurídicos (RN-CUM-001)")
        atual = self.dados_juridicos
        self.dados_juridicos = DadosJuridicos(
            razao_social=razao_social if razao_social is not None else atual.razao_social,
            nome_fantasia=(
                nome_fantasia if nome_fantasia is not None else atual.nome_fantasia
            ),
            cnae_principal=(
                cnae_principal if cnae_principal is not None else atual.cnae_principal
            ),
            capital=capital if capital is not None else atual.capital,
        )
        self._registrar_alteracao(usuario_id)

    def alterar_categoria(self, categoria: CategoriaPessoa, usuario_id: UUID | None = None) -> None:
        """Altera a categoria cadastral da pessoa."""
        self._garantir_ativa()
        self.categoria = categoria
        self._registrar_alteracao(usuario_id)

    def excluir(self, usuario_id: UUID) -> None:
        """Soft-delete da pessoa e de seus filhos (RN-CUM-007)."""
        if self.foi_excluido():
            return
        agora = datetime.now(UTC)
        self.deleted_at = agora
        self.deleted_by = usuario_id
        for endereco in self.enderecos:
            if not endereco.foi_excluido():
                endereco.excluir(usuario_id)
        for documento in self.documentos:
            if not documento.foi_excluido():
                documento.excluir(usuario_id)
        for contato in self.contatos:
            if not contato.foi_excluido():
                contato.excluir(usuario_id)

    def foi_excluido(self) -> bool:
        """Retorna True se a pessoa foi logicamente excluída."""
        return self.deleted_at is not None

    # -- Internals ---------------------------------------------------------------

    def _garantir_ativa(self) -> None:
        if self.foi_excluido():
            raise ValueError("Pessoa excluída não pode ser alterada (RN-CUM-007)")

    @staticmethod
    def _desativar_principais(enderecos: list[Endereco], usuario_id: UUID | None) -> None:
        for endereco in enderecos:
            if endereco.principal and not endereco.foi_excluido():
                endereco.principal = False
                endereco.updated_at = datetime.now(UTC)
                endereco.updated_by = usuario_id

    def _registrar_alteracao(self, usuario_id: UUID | None) -> None:
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id


__all__ = [
    "Pessoa",
    "TipoPessoa",
    "CategoriaPessoa",
    "Sexo",
    "DadosFisicos",
    "DadosJuridicos",
]
