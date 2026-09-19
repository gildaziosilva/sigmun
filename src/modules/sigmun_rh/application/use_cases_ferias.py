"""Use cases de Ferias (DOM-PES)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.ferias import Ferias


@dataclass
class PlanejarFeriasInput:
    """DTO de planejamento de ferias."""

    servidor_id: str
    periodo_aquisitivo_inicio: date | None = None
    periodo_aquisitivo_fim: date | None = None
    data_inicio_gozo: date | None = None
    data_fim_gozo: date | None = None
    dias: int = 30
    parcela: int = 1
    autor_id: str = ""


class PlanejarFeriasUseCase:
    """Planeja ferias (RN-PES-040/041)."""

    def __init__(
        self, repo: ports.RepositorioFerias, servidores: ports.RepositorioServidor
    ) -> None:
        self._repo = repo
        self._servidores = servidores

    def execute(self, dto: PlanejarFeriasInput) -> Ferias:
        """Executa o planejamento."""
        from ..domain.exceptions import RegraNegocioError

        if self._servidores.get_by_id(dto.servidor_id) is None:
            raise RegraNegocioError("Servidor nao encontrado")
        if dto.dias < 10:
            raise RegraNegocioError("Parcela minima de 10 dias (RN-PES-041)")
        if dto.parcela < 1 or dto.parcela > 3:
            raise RegraNegocioError("Maximo de 3 parcelas (RN-PES-041)")
        ferias = Ferias(
            servidor_id=dto.servidor_id,
            periodo_aquisitivo_inicio=dto.periodo_aquisitivo_inicio,
            periodo_aquisitivo_fim=dto.periodo_aquisitivo_fim,
            data_inicio_gozo=dto.data_inicio_gozo,
            data_fim_gozo=dto.data_fim_gozo,
            dias=dto.dias,
            parcela=dto.parcela,
            created_by=dto.autor_id,
        )
        return self._repo.save(ferias)


class AprovarFeriasUseCase:
    """Aprova ferias planejadas."""

    def __init__(self, repo: ports.RepositorioFerias) -> None:
        self._repo = repo

    def execute(self, ferias_id: str) -> Ferias:
        """Executa a aprovacao."""
        from ..domain.exceptions import FeriasNaoEncontradasError

        ferias = self._repo.get_by_id(ferias_id)
        if ferias is None:
            raise FeriasNaoEncontradasError("Ferias nao encontradas")
        ferias.aprovar()
        return self._repo.save(ferias)


class IniciarGozoFeriasUseCase:
    """Inicia gozo de ferias aprovadas."""

    def __init__(self, repo: ports.RepositorioFerias) -> None:
        self._repo = repo

    def execute(self, ferias_id: str) -> Ferias:
        """Executa o inicio do gozo."""
        from ..domain.exceptions import FeriasNaoEncontradasError

        ferias = self._repo.get_by_id(ferias_id)
        if ferias is None:
            raise FeriasNaoEncontradasError("Ferias nao encontradas")
        ferias.iniciar_gozo()
        return self._repo.save(ferias)


class ConcluirFeriasUseCase:
    """Conclui gozo de ferias."""

    def __init__(self, repo: ports.RepositorioFerias) -> None:
        self._repo = repo

    def execute(self, ferias_id: str) -> Ferias:
        """Executa a conclusao."""
        from ..domain.exceptions import FeriasNaoEncontradasError

        ferias = self._repo.get_by_id(ferias_id)
        if ferias is None:
            raise FeriasNaoEncontradasError("Ferias nao encontradas")
        ferias.concluir()
        return self._repo.save(ferias)


__all__ = [
    "PlanejarFeriasInput",
    "PlanejarFeriasUseCase",
    "AprovarFeriasUseCase",
    "IniciarGozoFeriasUseCase",
    "ConcluirFeriasUseCase",
]
