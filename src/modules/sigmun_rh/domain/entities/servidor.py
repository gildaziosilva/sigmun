"""Entidade Servidor — vínculo funcional do agente público (DOM-PES).

RN-PES-010: matrícula funcional é única no município.
RN-PES-011: CPF é único e validado (11 dígitos).
RN-PES-012: servidor precisa de cargo válido para admissão.
RN-PES-013: admissão exige data de admissão; demissão exige data
    posterior à admissão.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4


class StatusServidor(Enum):
    """Situação funcional do servidor."""

    ATIVO = "ativo"
    INATIVO = "inativo"
    AFASTADO = "afastado"
    APOSENTADO = "aposentado"
    EXONERADO = "exonerado"
    DEMITIDO = "demitido"


class TipoVinculo(Enum):
    """Tipo de vínculo do servidor com a administração."""

    EFETIVO = "efetivo"
    COMISSIONADO = "comissionado"
    TEMPORARIO = "temporario"
    ESTAGIARIO = "estagiario"
    TERCEIRIZADO = "terceirizado"


@dataclass
class Servidor:
    """Agente público municipal com matrícula e vínculo."""

    id: str = field(default_factory=lambda: str(uuid4()))
    matricula: str = ""
    cpf: str = ""
    nome: str = ""
    cargo_id: str = ""
    tipo_vinculo: TipoVinculo = field(default=TipoVinculo.EFETIVO)
    status: StatusServidor = field(default=StatusServidor.ATIVO)
    data_admissao: date | None = None
    data_desligamento: date | None = None
    salario: float = 0.0
    email: str = ""
    telefone: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False

    @property
    def esta_ativo(self) -> bool:
        """Indica se o servidor está em atividade."""
        return self.status == StatusServidor.ATIVO and not self.is_deleted

    @property
    def is_active(self) -> bool:
        """Alias de compatibilidade para ``esta_ativo``."""
        return self.esta_ativo

    def admitir(self) -> None:
        """Admite o servidor (status inicial ``ativo``)."""
        from ...domain.exceptions import RegraNegocioError

        if not self.matricula:
            raise RegraNegocioError("Admissão requer matrícula (RN-PES-010)")
        if not self.cargo_id:
            raise RegraNegocioError("Admissão requer cargo válido (RN-PES-012)")
        if not self.data_admissao:
            raise RegraNegocioError("Admissão requer data de admissão (RN-PES-013)")
        self.status = StatusServidor.ATIVO
        self.updated_at = datetime.utcnow()

    def afastar(self) -> None:
        """Registra afastamento temporário do servidor."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusServidor.ATIVO:
            raise RegraNegocioError(
                f"Apenas servidores ativos podem ser afastados (atual: {self.status.value})"
            )
        self.status = StatusServidor.AFASTADO
        self.updated_at = datetime.utcnow()

    def reativar(self) -> None:
        """Retorna servidor afastado à atividade."""
        from ...domain.exceptions import RegraNegocioError

        if self.status != StatusServidor.AFASTADO:
            raise RegraNegocioError(
                f"Apenas servidores afastados podem ser reativados (atual: {self.status.value})"
            )
        self.status = StatusServidor.ATIVO
        self.updated_at = datetime.utcnow()

    def desligar(self, data_desligamento: date | None = None) -> None:
        """Desliga o servidor (exoneração/demissão)."""
        from ...domain.exceptions import RegraNegocioError

        if self.status not in (StatusServidor.ATIVO, StatusServidor.AFASTADO):
            raise RegraNegocioError(
                f"Servidor não pode ser desligado no status '{self.status.value}'"
            )
        data = data_desligamento or date.today()
        if self.data_admissao and data < self.data_admissao:
            raise RegraNegocioError(
                "Data de desligamento anterior à admissão (RN-PES-013)"
            )
        self.data_desligamento = data
        if self.tipo_vinculo == TipoVinculo.EFETIVO:
            self.status = StatusServidor.EXONERADO
        else:
            self.status = StatusServidor.DEMITIDO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o servidor como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()


__all__ = ["StatusServidor", "TipoVinculo", "Servidor"]
