"""Casos de uso para Credenciais (DOM-SEG)."""

import logging
from datetime import datetime

from src.modules.sigmun_seg.application.interfaces import CredencialRepositoryInterface
from src.modules.sigmun_seg.domain.entities import Credencial, StatusCredencial
from src.modules.sigmun_seg.domain.exceptions import (
    CredencialJaRevogadaError,
    CredencialNaoEncontradaError,
)

logger = logging.getLogger(__name__)


class CriarCredencialUseCase:
    """Cria uma nova credencial de acesso."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        usuario_id: str,
        identificador: str,
        tipo: str = "senha",
    ) -> Credencial:
        """Cria uma credencial. O identificador deve ser referência/hash, nunca o valor real."""
        if not usuario_id:
            raise ValueError("Usuário é obrigatório")
        if not identificador or not identificador.strip():
            raise ValueError("Identificador é obrigatório")

        credencial = Credencial(
            usuario_id=usuario_id,
            tipo=tipo,
            identificador=identificador.strip(),
            status=StatusCredencial.ATIVA,
        )
        logger.info("Credencial criada para usuário: %s", usuario_id)
        return self._repo.save(credencial)


class BuscarCredencialUseCase:
    """Busca credenciais."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def get_by_id(self, credencial_id: str) -> Credencial:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        return credencial

    def get_by_usuario(self, usuario_id: str):
        return self._repo.get_by_usuario(usuario_id)

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo: str | None = None,
    ):
        return self._repo.list_all(page, page_size, status, tipo)


class SuspenderCredencialUseCase:
    """Suspende uma credencial."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(self, credencial_id: str) -> Credencial:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        credencial.suspender()
        return self._repo.save(credencial)


class RevogarCredencialUseCase:
    """Revoga uma credencial."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(self, credencial_id: str) -> Credencial:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        if credencial.status == StatusCredencial.REVOGADA:
            raise CredencialJaRevogadaError(f"Credencial '{credencial_id}' já foi revogada")
        credencial.revogar()
        return self._repo.save(credencial)


class RegistrarFalhaCredencialUseCase:
    """Registra uma tentativa de uso falha."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(self, credencial_id: str) -> Credencial:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        credencial.registrar_falha()
        return self._repo.save(credencial)


class RegistrarUsoCredencialUseCase:
    """Registra uso bem-sucedido de uma credencial."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(self, credencial_id: str) -> Credencial:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        credencial.registrar_uso()
        return self._repo.save(credencial)


class DeletarCredencialUseCase:
    """Remove uma credencial (soft-delete)."""

    def __init__(self, repository: CredencialRepositoryInterface):
        self._repo = repository

    def execute(self, credencial_id: str) -> bool:
        credencial = self._repo.get_by_id(credencial_id)
        if credencial is None:
            raise CredencialNaoEncontradaError(f"Credencial '{credencial_id}' não encontrada")
        return self._repo.delete(credencial_id)


__all__ = [
    "CriarCredencialUseCase",
    "BuscarCredencialUseCase",
    "SuspenderCredencialUseCase",
    "RevogarCredencialUseCase",
    "RegistrarFalhaCredencialUseCase",
    "RegistrarUsoCredencialUseCase",
    "DeletarCredencialUseCase",
]