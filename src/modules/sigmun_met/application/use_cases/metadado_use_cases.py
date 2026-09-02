"""Casos de uso para gerenciamento de Metadados."""

import logging

from src.modules.sigmun_met.application.interfaces import MetadadoRepositoryInterface
from src.modules.sigmun_met.domain.entities import (
    Metadado,
    StatusMetadado,
    TipoDadoMetadado,
)
from src.modules.sigmun_met.domain.exceptions import (
    CodigoInvalidoError,
    MetadadoJaExisteError,
    MetadadoNaoEncontradoError,
)
from src.modules.sigmun_met.domain.value_objects import CodigoMetadado, NomeEntidade

logger = logging.getLogger(__name__)


class CriarMetadadoUseCase:
    """Caso de uso para criar um novo metadado."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        tipo_dado: str = "texto",
        obrigatorio: bool = False,
        multi_valor: bool = False,
        aplicavel_a: list[str] = None,
        valor_padrao: str = "",
    ) -> Metadado:
        """Cria um novo metadado."""
        valido, msg = CodigoMetadado.validar(codigo)
        if not valido:
            raise CodigoInvalidoError(f"Código inválido: {msg}")

        valido, msg = NomeEntidade.validar(nome)
        if not valido:
            raise ValueError(f"Nome inválido: {msg}")

        if self._repo.exists_by_codigo(codigo):
            raise MetadadoJaExisteError(f"Metadado com código '{codigo}' já existe")

        metadado = Metadado(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            tipo_dado=TipoDadoMetadado(tipo_dado),
            obrigatorio=obrigatorio,
            multi_valor=multi_valor,
            aplicavel_a=aplicavel_a or [],
            valor_padrao=valor_padrao,
        )
        logger.info("Metadado criado: %s", metadado.codigo)
        return self._repo.save(metadado)


class AtualizarMetadadoUseCase:
    """Caso de uso para atualizar um metadado."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        metadado_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        tipo_dado: str | None = None,
        obrigatorio: bool | None = None,
        multi_valor: bool | None = None,
        aplicavel_a: list[str] | None = None,
        valor_padrao: str | None = None,
    ) -> Metadado:
        """Atualiza um metadado existente."""
        metadado = self._repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")

        if nome is not None:
            valido, msg = NomeEntidade.validar(nome)
            if not valido:
                raise ValueError(f"Nome inválido: {msg}")
            metadado.nome = nome
        if descricao is not None:
            metadado.descricao = descricao
        if tipo_dado is not None:
            metadado.tipo_dado = TipoDadoMetadado(tipo_dado)
        if obrigatorio is not None:
            metadado.obrigatorio = obrigatorio
        if multi_valor is not None:
            metadado.multi_valor = multi_valor
        if aplicavel_a is not None:
            metadado.aplicavel_a = aplicavel_a
        if valor_padrao is not None:
            metadado.valor_padrao = valor_padrao

        from datetime import datetime
        metadado.updated_at = datetime.utcnow()
        return self._repo.save(metadado)


class BuscarMetadadoUseCase:
    """Caso de uso para buscar metadados."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def get_by_id(self, metadado_id: str) -> Metadado:
        """Busca metadado por ID."""
        metadado = self._repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")
        return metadado

    def get_by_codigo(self, codigo: str) -> Metadado:
        """Busca metadado por código."""
        metadado = self._repo.get_by_codigo(codigo)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado com código '{codigo}' não encontrado")
        return metadado

    def list_all(
        self, page: int = 0, page_size: int = 50,
        status: str | None = None, tipo_dado: str | None = None,
    ) -> tuple:
        """Lista metadados com paginação."""
        return self._repo.list_all(page, page_size, status, tipo_dado)


class AtivarMetadadoUseCase:
    """Caso de uso para ativar um metadado."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def execute(self, metadado_id: str) -> Metadado:
        """Ativa um metadado."""
        metadado = self._repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")
        metadado.status = StatusMetadado.ATIVO
        metadado.activate()
        return self._repo.save(metadado)


class DesativarMetadadoUseCase:
    """Caso de uso para desativar um metadado."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def execute(self, metadado_id: str) -> Metadado:
        """Desativa um metadado."""
        metadado = self._repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")
        metadado.deactivate()
        return self._repo.save(metadado)


class DeletarMetadadoUseCase:
    """Caso de uso para deletar um metadado."""

    def __init__(self, repository: MetadadoRepositoryInterface):
        self._repo = repository

    def execute(self, metadado_id: str) -> bool:
        """Deleta um metadado."""
        metadado = self._repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")
        return self._repo.delete(metadado_id)


__all__ = [
    "CriarMetadadoUseCase",
    "AtualizarMetadadoUseCase",
    "BuscarMetadadoUseCase",
    "AtivarMetadadoUseCase",
    "DesativarMetadadoUseCase",
    "DeletarMetadadoUseCase",
]
