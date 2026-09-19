"""Use cases de dotação e reserva de saldo (DOM-ORC)."""

from __future__ import annotations

from dataclasses import dataclass

from ..domain.entities.dotacao import Dotacao
from ..domain.entities.reserva import ReservaSaldo
from . import interfaces as ports


@dataclass
class CriarDotacaoInput:
    """DTO de criação de dotação."""

    loa_id: str
    exercicio: int
    codigo: str
    valor_inicial: float
    unidade_orcamentaria: str = ""
    natureza_despesa: str = ""
    fonte_recursos: str = ""
    autor_id: str = ""


class CriarDotacaoUseCase:
    """Cria dotação vinculada à LOA (RN-ORC-030)."""

    def __init__(self, dotacoes: ports.RepositorioDotacao,
                 loas: ports.RepositorioLOA) -> None:
        self._dotacoes = dotacoes
        self._loas = loas

    def execute(self, dto: CriarDotacaoInput) -> Dotacao:
        """Executa a criação."""
        from ..domain.entities.loa import StatusLOA
        from ..domain.exceptions import RegraNegocioError

        if not dto.codigo:
            raise RegraNegocioError("Código da dotação é obrigatório (RN-ORC-030)")
        if dto.valor_inicial <= 0:
            raise RegraNegocioError("Valor inicial deve ser maior que zero")
        loa = self._loas.get_by_id(dto.loa_id)
        if loa is None:
            raise RegraNegocioError("LOA inválida")
        if loa.status not in (StatusLOA.APROVADA, StatusLOA.PUBLICADA):
            raise RegraNegocioError("Dotação exige LOA aprovada/publicada")
        if self._dotacoes.get_by_codigo_exercicio(dto.codigo, dto.exercicio) is not None:
            raise RegraNegocioError("Dotação já existe (RN-ORC-030)")
        dot = Dotacao(loa_id=dto.loa_id, exercicio=dto.exercicio, codigo=dto.codigo,
                      unidade_orcamentaria=dto.unidade_orcamentaria,
                      natureza_despesa=dto.natureza_despesa,
                      fonte_recursos=dto.fonte_recursos,
                      valor_inicial=dto.valor_inicial, created_by=dto.autor_id)
        return self._dotacoes.save(dot)


class SuplementarDotacaoUseCase:
    """Suplementa dotação ativa."""

    def __init__(self, repo: ports.RepositorioDotacao) -> None:
        self._repo = repo

    def execute(self, dotacao_id: str, valor: float) -> Dotacao:
        """Executa a suplementação."""
        from ..domain.exceptions import DotacaoNaoEncontradaError

        dot = self._repo.get_by_id(dotacao_id)
        if dot is None:
            raise DotacaoNaoEncontradaError("Dotação não encontrada")
        dot.suplementar(valor)
        return self._repo.save(dot)


class AnularDotacaoUseCase:
    """Anula parcialmente dotação ativa."""

    def __init__(self, repo: ports.RepositorioDotacao) -> None:
        self._repo = repo

    def execute(self, dotacao_id: str, valor: float) -> Dotacao:
        """Executa a anulação."""
        from ..domain.exceptions import DotacaoNaoEncontradaError

        dot = self._repo.get_by_id(dotacao_id)
        if dot is None:
            raise DotacaoNaoEncontradaError("Dotação não encontrada")
        dot.anular(valor)
        return self._repo.save(dot)


@dataclass
class ReservarSaldoInput:
    """DTO de reserva de saldo."""

    dotacao_id: str
    valor: float
    finalidade: str = ""
    numero: str = ""
    autor_id: str = ""


class ReservarSaldoUseCase:
    """Reserva saldo da dotação (RN-ORC-040)."""

    def __init__(self, reservas: ports.RepositorioReserva,
                 dotacoes: ports.RepositorioDotacao) -> None:
        self._reservas = reservas
        self._dotacoes = dotacoes

    def execute(self, dto: ReservarSaldoInput) -> ReservaSaldo:
        """Executa a reserva (debita dotação + cria reserva)."""
        from ..domain.exceptions import DotacaoNaoEncontradaError

        dot = self._dotacoes.get_by_id(dto.dotacao_id)
        if dot is None:
            raise DotacaoNaoEncontradaError("Dotação não encontrada")
        dot.reservar(dto.valor)
        self._dotacoes.save(dot)
        reserva = ReservaSaldo(dotacao_id=dto.dotacao_id, numero=dto.numero,
                               valor=dto.valor, finalidade=dto.finalidade,
                               created_by=dto.autor_id)
        return self._reservas.save(reserva)


class CancelarReservaUseCase:
    """Cancela reserva ativa (devolve saldo)."""

    def __init__(self, reservas: ports.RepositorioReserva,
                 dotacoes: ports.RepositorioDotacao) -> None:
        self._reservas = reservas
        self._dotacoes = dotacoes

    def execute(self, reserva_id: str, motivo: str = "") -> ReservaSaldo:
        """Executa o cancelamento."""
        from ..domain.exceptions import DotacaoNaoEncontradaError, ReservaNaoEncontradaError

        res = self._reservas.get_by_id(reserva_id)
        if res is None:
            raise ReservaNaoEncontradaError("Reserva não encontrada")
        res.cancelar(motivo)
        dot = self._dotacoes.get_by_id(res.dotacao_id)
        if dot is None:
            raise DotacaoNaoEncontradaError("Dotação não encontrada")
        dot.liberar_reserva(res.valor)
        self._dotacoes.save(dot)
        return self._reservas.save(res)


__all__ = [
    "CriarDotacaoInput", "CriarDotacaoUseCase",
    "SuplementarDotacaoUseCase", "AnularDotacaoUseCase",
    "ReservarSaldoInput", "ReservarSaldoUseCase", "CancelarReservaUseCase",
]
