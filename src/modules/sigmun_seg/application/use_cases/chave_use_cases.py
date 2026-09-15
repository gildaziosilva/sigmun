"""Casos de uso para Chaves Criptográficas (DOM-SEG)."""

import logging
from datetime import datetime

from src.modules.sigmun_seg.application.interfaces import (
    ChaveCriptograficaRepositoryInterface,
)
from src.modules.sigmun_seg.domain.entities import ChaveCriptografica
from src.modules.sigmun_seg.domain.exceptions import (
    ChaveJaRevogadaError,
    ChaveNaoEncontradaError,
)

logger = logging.getLogger(__name__)


class CriarChaveUseCase:
    """Cria uma nova chave criptográfica."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        nome: str,
        algoritmo: str = "AES256",
        tipo: str = "simetrica",
        tamanho_bits: int = 256,
        responsavel_id: str = "",
    ) -> ChaveCriptografica:
        """Cria uma nova chave criptográfica no sistema."""
        if not nome or not nome.strip():
            raise ValueError("Nome da chave é obrigatório")
        if tamanho_bits <= 0:
            raise ValueError("Tamanho em bits deve ser positivo")
        if self._repo.exists_by_nome(nome):
            raise ValueError(f"Já existe uma chave com o nome '{nome}'")

        chave = ChaveCriptografica(
            nome=nome.strip(),
            algoritmo=algoritmo,
            tipo=tipo,
            tamanho_bits=tamanho_bits,
            status="ativa",
            responsavel_id=responsavel_id,
        )
        logger.info("Chave criptográfica criada: %s", chave.nome)
        return self._repo.save(chave)


class BuscarChaveUseCase:
    """Busca chaves criptográficas."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, chave_id: str) -> ChaveCriptografica:
        chave = self._repo.get_by_id(chave_id)
        if chave is None:
            raise ChaveNaoEncontradaError(f"Chave '{chave_id}' não encontrada")
        return chave

    def get_by_nome(self, nome: str) -> ChaveCriptografica | None:
        return self._repo.get_by_nome(nome)

    def list_all(self, page: int = 0, page_size: int = 50, status: str | None = None):
        return self._repo.list_all(page, page_size, status)


class AtualizarChaveUseCase:
    """Atualiza uma chave criptográfica."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        chave_id: str,
        nome: str | None = None,
        algoritmo: str | None = None,
        tipo: str | None = None,
        responsavel_id: str | None = None,
    ) -> ChaveCriptografica:
        chave = self._repo.get_by_id(chave_id)
        if chave is None:
            raise ChaveNaoEncontradaError(f"Chave '{chave_id}' não encontrada")

        if nome is not None:
            chave.nome = nome
        if algoritmo is not None:
            chave.algoritmo = algoritmo
        if tipo is not None:
            chave.tipo = tipo
        if responsavel_id is not None:
            chave.responsavel_id = responsavel_id

        chave.updated_at = datetime.utcnow()
        return self._repo.save(chave)


class RevogarChaveUseCase:
    """Revoga uma chave criptográfica."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def execute(self, chave_id: str) -> ChaveCriptografica:
        chave = self._repo.get_by_id(chave_id)
        if chave is None:
            raise ChaveNaoEncontradaError(f"Chave '{chave_id}' não encontrada")
        if chave.status == "revogada":
            raise ChaveJaRevogadaError(f"Chave '{chave_id}' já foi revogada")
        chave.revogar()
        return self._repo.save(chave)


class ExpirarChaveUseCase:
    """Marca uma chave criptográfica como expirada."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def execute(self, chave_id: str) -> ChaveCriptografica:
        chave = self._repo.get_by_id(chave_id)
        if chave is None:
            raise ChaveNaoEncontradaError(f"Chave '{chave_id}' não encontrada")
        chave.expirar()
        return self._repo.save(chave)


class DeletarChaveUseCase:
    """Remove uma chave criptográfica (soft-delete)."""

    def __init__(self, repository: ChaveCriptograficaRepositoryInterface):
        self._repo = repository

    def execute(self, chave_id: str) -> bool:
        chave = self._repo.get_by_id(chave_id)
        if chave is None:
            raise ChaveNaoEncontradaError(f"Chave '{chave_id}' não encontrada")
        return self._repo.delete(chave_id)


__all__ = [
    "CriarChaveUseCase",
    "BuscarChaveUseCase",
    "AtualizarChaveUseCase",
    "RevogarChaveUseCase",
    "ExpirarChaveUseCase",
    "DeletarChaveUseCase",
]
