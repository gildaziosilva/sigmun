"""Use cases da Folha de Pagamento (DOM-PES)."""

from __future__ import annotations

from dataclasses import dataclass

from . import interfaces as ports
from ..domain.entities.folha import FolhaPagamento, StatusFolha


@dataclass
class AbrirFolhaInput:
    """DTO de abertura de folha."""

    competencia_ano: int
    competencia_mes: int
    descricao: str = ""
    autor_id: str = ""


class AbrirFolhaUseCase:
    """Abre folha da competência (RN-PES-030)."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, dto: AbrirFolhaInput) -> FolhaPagamento:
        """Executa a abertura."""
        from ..domain.exceptions import RegraNegocioError

        if not 1 <= dto.competencia_mes <= 12:
            raise RegraNegocioError("Mês de competência inválido")
        if dto.competencia_ano < 2000:
            raise RegraNegocioError("Ano de competência inválido")
        existente = self._repo.get_by_competencia(dto.competencia_ano, dto.competencia_mes)
        if existente is not None:
            raise RegraNegocioError(
                f"Folha {dto.competencia_ano:04d}-{dto.competencia_mes:02d} "
                "já existe (RN-PES-030)"
            )
        folha = FolhaPagamento(
            competencia_ano=dto.competencia_ano,
            competencia_mes=dto.competencia_mes,
            descricao=dto.descricao,
            status=StatusFolha.ABERTA,
            created_by=dto.autor_id,
        )
        return self._repo.save(folha)


@dataclass
class ConsolidarFolhaInput:
    """DTO de consolidação de totais da folha."""

    folha_id: str
    proventos: float
    descontos: float
    quantidade_servidores: int


class ConsolidarFolhaUseCase:
    """Consolida totais da folha aberta (RN-PES-031)."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, dto: ConsolidarFolhaInput) -> FolhaPagamento:
        """Executa a consolidação."""
        from ..domain.exceptions import FolhaNaoEncontradaError

        folha = self._repo.get_by_id(dto.folha_id)
        if folha is None:
            raise FolhaNaoEncontradaError("Folha não encontrada")
        folha.consolidar(dto.proventos, dto.descontos, dto.quantidade_servidores)
        return self._repo.save(folha)


class FecharFolhaUseCase:
    """Fecha folha (ABERTA → FECHADA)."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, folha_id: str) -> FolhaPagamento:
        """Executa o fechamento."""
        from ..domain.exceptions import FolhaNaoEncontradaError

        folha = self._repo.get_by_id(folha_id)
        if folha is None:
            raise FolhaNaoEncontradaError("Folha não encontrada")
        folha.fechar()
        return self._repo.save(folha)


class ReabrirFolhaUseCase:
    """Reabre folha fechada."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, folha_id: str) -> FolhaPagamento:
        """Executa a reabertura."""
        from ..domain.exceptions import FolhaNaoEncontradaError

        folha = self._repo.get_by_id(folha_id)
        if folha is None:
            raise FolhaNaoEncontradaError("Folha não encontrada")
        folha.reabrir()
        return self._repo.save(folha)


class HomologarFolhaUseCase:
    """Homologa folha fechada."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, folha_id: str) -> FolhaPagamento:
        """Executa a homologação."""
        from ..domain.exceptions import FolhaNaoEncontradaError

        folha = self._repo.get_by_id(folha_id)
        if folha is None:
            raise FolhaNaoEncontradaError("Folha não encontrada")
        folha.homologar()
        return self._repo.save(folha)


class PagarFolhaUseCase:
    """Registra pagamento da folha homologada."""

    def __init__(self, repo: ports.RepositorioFolha) -> None:
        self._repo = repo

    def execute(self, folha_id: str) -> FolhaPagamento:
        """Executa o pagamento."""
        from ..domain.exceptions import FolhaNaoEncontradaError

        folha = self._repo.get_by_id(folha_id)
        if folha is None:
            raise FolhaNaoEncontradaError("Folha não encontrada")
        folha.pagar()
        return self._repo.save(folha)


__all__ = [
    "AbrirFolhaInput",
    "AbrirFolhaUseCase",
    "ConsolidarFolhaInput",
    "ConsolidarFolhaUseCase",
    "FecharFolhaUseCase",
    "ReabrirFolhaUseCase",
    "HomologarFolhaUseCase",
    "PagarFolhaUseCase",
]
