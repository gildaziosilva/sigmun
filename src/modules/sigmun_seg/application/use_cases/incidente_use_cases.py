"""Casos de uso para Incidentes de Segurança."""

import logging

from src.modules.sigmun_seg.application.interfaces import (
    IncidenteSegurancaRepositoryInterface,
)
from src.modules.sigmun_seg.domain.entities import (
    IncidenteSeguranca,
    SeveridadeIncidente,
    StatusIncidente,
)
from src.modules.sigmun_seg.domain.exceptions import (
    IncidenteJaResolvidoError,
    IncidenteNaoEncontradoError,
)

logger = logging.getLogger(__name__)


class RegistrarIncidenteSegurancaUseCase:
    """Registra um novo incidente de segurança."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        titulo: str,
        descricao: str,
        severidade: str = "baixa",
        impacto: str = "",
        categoria: str = "",
        relator_id: str = "",
    ) -> IncidenteSeguranca:
        """Registra um novo incidente de segurança."""
        if not titulo:
            raise ValueError("Título obrigatório")
        if not descricao:
            raise ValueError("Descrição obrigatória")

        incidente = IncidenteSeguranca(
            titulo=titulo,
            descricao=descricao,
            severidade=SeveridadeIncidente(severidade),
            impacto=impacto,
            categoria=categoria,
            relator_id=relator_id,
        )
        logger.info("Incidente registrado: %s", incidente.titulo)
        return self._repo.save(incidente)


class BuscarIncidenteSegurancaUseCase:
    """Busca incidentes de segurança."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, incidente_id: str) -> IncidenteSeguranca:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")
        return incidente

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        severidade: str | None = None,
        status: str | None = None,
    ) -> tuple:
        return self._repo.list_all(page, page_size, severidade, status)


class EscalarIncidenteSegurancaUseCase:
    """Escala um incidente para um responsável."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        incidente_id: str,
        atribuido_a: str,
    ) -> IncidenteSeguranca:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")

        incidente.escalar(atribuido_a)
        return self._repo.save(incidente)


class MitigarIncidenteSegurancaUseCase:
    """Inicia mitigação de um incidente."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, incidente_id: str) -> IncidenteSeguranca:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")

        incidente.mitigar()
        return self._repo.save(incidente)


class ResolverIncidenteSegurancaUseCase:
    """Resolve um incidente."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, incidente_id: str) -> IncidenteSeguranca:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")

        if incidente.status == StatusIncidente.RESOLVIDO:
            raise IncidenteJaResolvidoError(f"Incidente '{incidente_id}' já resolvido")
        if incidente.status == StatusIncidente.ENCERRADO:
            raise IncidenteJaResolvidoError(f"Incidente '{incidente_id}' já encerrado")

        incidente.resolver()
        return self._repo.save(incidente)


class EncerrarIncidenteSegurancaUseCase:
    """Encerra um incidente resolvido."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, incidente_id: str) -> IncidenteSeguranca:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")

        incidente.encerrar()
        return self._repo.save(incidente)


class DeletarIncidenteSegurancaUseCase:
    """Remove um incidente (soft-delete)."""

    def __init__(self, repository: IncidenteSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, incidente_id: str) -> bool:
        incidente = self._repo.get_by_id(incidente_id)
        if incidente is None:
            raise IncidenteNaoEncontradoError(f"Incidente '{incidente_id}' não encontrado")
        return self._repo.delete(incidente_id)


__all__ = [
    "RegistrarIncidenteSegurancaUseCase",
    "BuscarIncidenteSegurancaUseCase",
    "EscalarIncidenteSegurancaUseCase",
    "MitigarIncidenteSegurancaUseCase",
    "ResolverIncidenteSegurancaUseCase",
    "EncerrarIncidenteSegurancaUseCase",
    "DeletarIncidenteSegurancaUseCase",
]
