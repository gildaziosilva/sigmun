"""Entidades do DOM-ASS — Assistência Social.

RN-ASS-001: o NIS da família é único no cadastro municipal.
RN-ASS-002: o CPF da pessoa é único no cadastro municipal.
RN-ASS-003: o benefício eventual obedece à máquina de estados
    SOLICITADO -> APROVADO | NEGADO -> ENTREGUE, com CANCELADO disponível
    enquanto não houver entrega.
RN-ASS-004: atendimentos são registrados por unidade CRAS/CREAS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class Sexo(Enum):
    """Sexo biológico registrado."""

    MASCULINO = "masculino"
    FEMININO = "feminino"
    IGNORADO = "ignorado"


class StatusFamilia(Enum):
    """Situação cadastral da família no CadÚnico."""

    ATIVA = "ativa"
    INATIVA = "inativa"
    EXCLUIDA = "excluida"


class TipoBeneficio(Enum):
    """Tipos de benefícios eventuais."""

    ALIMENTACAO = "alimentacao"
    ALUGUEL = "aluguel"
    MEDICAMENTO = "medicamento"
    FUNERAL = "funeral"
    NATALIDADE = "natalidade"
    CALAMIDADE = "calamidade"
    OUTRO = "outro"


class StatusBeneficio(Enum):
    """Situação do benefício eventual."""

    SOLICITADO = "solicitado"
    APROVADO = "aprovado"
    NEGADO = "negado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"


class TipoUnidade(Enum):
    """Tipo de unidade de assistência social."""

    CRAS = "cras"
    CREAS = "creas"
    CENTRO_POP = "centro_pop"
    ABRIGO = "abrigo"
    OUTRO = "outro"


class StatusUnidade(Enum):
    """Situação da unidade."""

    ATIVA = "ativa"
    INATIVA = "inativa"
    MANUTENCAO = "manutencao"


class TipoAtendimento(Enum):
    """Tipos de atendimento social."""

    ACOLHIMENTO = "acolhimento"
    ORIENTACAO = "orientacao"
    ENCAMINHAMENTO = "encaminhamento"
    VISITA_DOMICILIAR = "visita_domiciliar"
    GRUPO_CONVIVENCIA = "grupo_convivencia"
    BENEFICIO_EVENTUAL = "beneficio_eventual"
    OUTRO = "outro"


def _valida_nis(nis: str) -> None:
    """Valida a forma do NIS (11 dígitos numéricos)."""
    from ..exceptions import RegraNegocioError

    if not nis or not nis.isdigit() or len(nis) != 11:
        raise RegraNegocioError("NIS inválido: informe 11 dígitos numéricos (RN-ASS-001)")


def _valida_cpf(cpf: str) -> None:
    """Valida a forma do CPF (11 dígitos numéricos)."""
    from ..exceptions import RegraNegocioError

    if not cpf or not cpf.isdigit() or len(cpf) != 11:
        raise RegraNegocioError("CPF inválido: informe 11 dígitos numéricos (RN-ASS-002)")


@dataclass
class FamiliaCadUnico:
    """Família cadastrada no CadÚnico local."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nis: str = ""
    responsavel_nome: str = ""
    responsavel_cpf: str = ""
    endereco: str = ""
    telefone: str = ""
    renda_per_capita: float = 0.0
    quantidade_pessoas: int = 0
    status: StatusFamilia = field(default=StatusFamilia.ATIVA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativa(self) -> bool:
        """Indica se a família está ativa e não excluída."""
        return self.status == StatusFamilia.ATIVA and not self.is_deleted

    def inativar(self) -> None:
        """Inativa o cadastro da família."""
        self.status = StatusFamilia.INATIVA
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a família como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def atualizar_renda(self, renda: float) -> None:
        """Atualiza renda per capita da família."""
        self.renda_per_capita = renda
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.nis:
            raise RegraNegocioError("NIS da família é obrigatório")
        if not self.responsavel_nome:
            raise RegraNegocioError("Nome do responsável é obrigatório")
        _valida_nis(self.nis)


@dataclass
class PessoaCadUnico:
    """Pessoa cadastrada no CadÚnico local."""

    id: str = field(default_factory=lambda: str(uuid4()))
    familia_id: str = ""
    nome: str = ""
    cpf: str = ""
    data_nascimento: str = ""
    sexo: Sexo = field(default=Sexo.IGNORADO)
    nome_mae: str = ""
    parentesco: str = ""
    escolaridade: str = ""
    ocupacao: str = ""
    renda: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def excluir(self) -> None:
        """Marca a pessoa como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.nome:
            raise RegraNegocioError("Nome da pessoa é obrigatório")
        if not self.familia_id:
            raise RegraNegocioError("Família é obrigatória")
        _valida_cpf(self.cpf)


@dataclass
class UnidadeAssistencia:
    """Unidade CRAS/CREAS/Centro Pop."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    tipo: TipoUnidade = field(default=TipoUnidade.CRAS)
    endereco: str = ""
    telefone: str = ""
    email: str = ""
    responsavel: str = ""
    status: StatusUnidade = field(default=StatusUnidade.ATIVA)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativa(self) -> bool:
        """Indica se a unidade está ativa e não excluída."""
        return self.status == StatusUnidade.ATIVA and not self.is_deleted

    def inativar(self) -> None:
        """Inativa a unidade."""
        self.status = StatusUnidade.INATIVA
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a unidade como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Código da unidade é obrigatório")
        if not self.nome:
            raise RegraNegocioError("Nome da unidade é obrigatório")


@dataclass
class BeneficioEventual:
    """Benefício eventual concedido a família."""

    id: str = field(default_factory=lambda: str(uuid4()))
    familia_id: str = ""
    tipo: TipoBeneficio = field(default=TipoBeneficio.ALIMENTACAO)
    descricao: str = ""
    valor: float = 0.0
    quantidade: int = 1
    data_solicitacao: datetime = field(default_factory=datetime.utcnow)
    data_aprovacao: datetime | None = None
    data_entrega: datetime | None = None
    status: StatusBeneficio = field(default=StatusBeneficio.SOLICITADO)
    unidade_id: str = ""
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""

    def aprovar(self, autor_id: str) -> None:
        """Aprova o benefício."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusBeneficio.SOLICITADO:
            raise RegraNegocioError("Benefício deve estar solicitado para ser aprovado")
        self.status = StatusBeneficio.APROVADO
        self.data_aprovacao = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def negar(self, autor_id: str, justificativa: str) -> None:
        """Nega o benefício."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusBeneficio.SOLICITADO:
            raise RegraNegocioError("Benefício deve estar solicitado para ser negado")
        self.status = StatusBeneficio.NEGADO
        self.observacao = justificativa
        self.updated_at = datetime.utcnow()

    def entregar(self, autor_id: str) -> None:
        """Registra entrega do benefício."""
        from ..exceptions import RegraNegocioError

        if self.status != StatusBeneficio.APROVADO:
            raise RegraNegocioError("Benefício deve estar aprovado para ser entregue")
        self.status = StatusBeneficio.ENTREGUE
        self.data_entrega = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def cancelar(self, autor_id: str) -> None:
        """Cancela o benefício."""
        from ..exceptions import RegraNegocioError

        if self.status in (StatusBeneficio.ENTREGUE, StatusBeneficio.CANCELADO):
            raise RegraNegocioError(
                "Benefício já entregue ou cancelado não pode ser cancelado novamente"
            )
        self.status = StatusBeneficio.CANCELADO
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.familia_id:
            raise RegraNegocioError("Família é obrigatória")
        if self.valor < 0:
            raise RegraNegocioError("Valor não pode ser negativo")
        if self.quantidade <= 0:
            raise RegraNegocioError("Quantidade deve ser maior que zero")


@dataclass
class AtendimentoSocial:
    """Atendimento social realizado em unidade CRAS/CREAS."""

    id: str = field(default_factory=lambda: str(uuid4()))
    pessoa_id: str = ""
    unidade_id: str = ""
    tipo: TipoAtendimento = field(default=TipoAtendimento.ACOLHIMENTO)
    data: date = field(default_factory=date.today)
    descricao: str = ""
    encaminhamento: str = ""
    profissional: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""

    def validar(self) -> None:
        """Valida regras estruturais da entidade."""
        from ..exceptions import RegraNegocioError

        if not self.pessoa_id:
            raise RegraNegocioError("Pessoa é obrigatória")
        if not self.unidade_id:
            raise RegraNegocioError("Unidade é obrigatória")
        if not self.profissional:
            raise RegraNegocioError("Profissional responsável é obrigatório")


__all__ = [
    "Sexo",
    "StatusFamilia",
    "TipoBeneficio",
    "StatusBeneficio",
    "TipoUnidade",
    "StatusUnidade",
    "TipoAtendimento",
    "FamiliaCadUnico",
    "PessoaCadUnico",
    "UnidadeAssistencia",
    "BeneficioEventual",
    "AtendimentoSocial",
]
