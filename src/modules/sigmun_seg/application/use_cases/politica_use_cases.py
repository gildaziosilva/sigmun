"""Casos de uso para Políticas de Segurança."""

import logging
from datetime import datetime

from src.modules.sigmun_seg.application.interfaces import (
    PoliticaSegurancaRepositoryInterface,
)
from src.modules.sigmun_seg.domain.entities import PoliticaSeguranca
from src.modules.sigmun_seg.domain.exceptions import (
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
)
from src.modules.sigmun_seg.domain.value_objects import CodigoControle

logger = logging.getLogger(__name__)


class CriarPoliticaSegurancaUseCase:
    """Cria uma nova política de segurança."""

    def __init__(self, repository: PoliticaSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        titulo: str,
        conteudo: str,
        versao: str = "1.0",
    ) -> PoliticaSeguranca:
        """Cria uma nova política de segurança."""
        valido, msg = CodigoControle.validar(codigo)
        if not valido:
            raise ValueError(msg)

        if not titulo:
            raise ValueError("Título obrigatório")

        if self._repo.exists_by_codigo(codigo):
            raise PoliticaJaExisteError(f"Política '{codigo}' já existe")

        politica = PoliticaSeguranca(
            codigo=codigo,
            titulo=titulo,
            conteudo=conteudo,
            versao=versao,
            ativa=False,
        )
        logger.info("Política de segurança criada: %s", politica.codigo)
        return self._repo.save(politica)


class BuscarPoliticaSegurancaUseCase:
    """Busca políticas de segurança."""

    def __init__(self, repository: PoliticaSegurancaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, politica_id: str) -> PoliticaSeguranca:
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")
        return politica

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        ativa: bool | None = None,
    ) -> tuple:
        return self._repo.list_all(page, page_size, ativa)


class AtualizarPoliticaSegurancaUseCase:
    """Atualiza uma política de segurança."""

    def __init__(self, repository: PoliticaSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        politica_id: str,
        titulo: str | None = None,
        conteudo: str | None = None,
        versao: str | None = None,
        data_revisao: str | None = None,
    ) -> PoliticaSeguranca:
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")

        if titulo is not None:
            politica.titulo = titulo
        if conteudo is not None:
            politica.conteudo = conteudo
        if versao is not None:
            politica.versao = versao
        if data_revisao is not None:
            politica.data_revisao = datetime.fromisoformat(data_revisao)

        politica.updated_at = datetime.utcnow()
        return self._repo.save(politica)


class AprovarPoliticaSegurancaUseCase:
    """Aprova uma política de segurança."""

    def __init__(self, repository: PoliticaSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        politica_id: str,
        aprovador_id: str,
    ) -> PoliticaSeguranca:
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")

        politica.aprovar(aprovador_id)
        return self._repo.save(politica)


class DeletarPoliticaSegurancaUseCase:
    """Remove uma política de segurança (soft-delete)."""

    def __init__(self, repository: PoliticaSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, politica_id: str) -> bool:
        politica = self._repo.get_by_id(politica_id)
        if politica is None:
            raise PoliticaNaoEncontradaError(f"Política '{politica_id}' não encontrada")
        return self._repo.delete(politica_id)


__all__ = [
    "CriarPoliticaSegurancaUseCase",
    "BuscarPoliticaSegurancaUseCase",
    "AtualizarPoliticaSegurancaUseCase",
    "AprovarPoliticaSegurancaUseCase",
    "DeletarPoliticaSegurancaUseCase",
]
