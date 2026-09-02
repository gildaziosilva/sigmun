"""Casos de uso para gerenciamento de Valores de Metadados."""

import logging

from src.modules.sigmun_met.application.interfaces import (
    MetadadoRepositoryInterface,
    ValorMetadadoRepositoryInterface,
)
from src.modules.sigmun_met.domain.entities import ValorMetadado
from src.modules.sigmun_met.domain.exceptions import (
    MetadadoNaoEncontradoError,
    ValorMetadadoInvalidoError,
    ValorMetadadoNaoEncontradoError,
)
from src.modules.sigmun_met.domain.services import MetadadoService
from src.modules.sigmun_met.domain.value_objects import EntidadeAlvo

logger = logging.getLogger(__name__)


class AtribuirValorMetadadoUseCase:
    """Caso de uso para atribuir um valor de metadado a uma entidade."""

    def __init__(
        self,
        valor_repo: ValorMetadadoRepositoryInterface,
        metadado_repo: MetadadoRepositoryInterface,
    ):
        self._valor_repo = valor_repo
        self._metadado_repo = metadado_repo

    def execute(
        self,
        metadado_id: str,
        entidade_tipo: str,
        entidade_id: str,
        valor: str,
    ) -> ValorMetadado:
        """Atribui valor de metadado a uma entidade."""
        valido, msg = EntidadeAlvo.validar(entidade_tipo, entidade_id)
        if not valido:
            raise ValueError(f"Entidade alvo inválida: {msg}")

        metadado = self._metadado_repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")

        MetadadoService.validar_e_levantar(metadado, valor)

        # Atualiza valor existente para o mesmo metadado+entidade
        existente = self._valor_repo.get_by_metadado_e_entidade(
            metadado_id, entidade_tipo, entidade_id
        )
        if existente is not None:
            existente.valor = valor
            from datetime import datetime
            existente.updated_at = datetime.utcnow()
            logger.info(
                "Valor do metadado '%s' atualizado para entidade %s/%s",
                metadado.codigo, entidade_tipo, entidade_id,
            )
            return self._valor_repo.save(existente)

        valor_metadado = ValorMetadado(
            metadado_id=metadado_id,
            entidade_tipo=entidade_tipo,
            entidade_id=entidade_id,
            valor=valor,
        )
        logger.info(
            "Valor atribuído ao metadado '%s' para entidade %s/%s",
            metadado.codigo, entidade_tipo, entidade_id,
        )
        return self._valor_repo.save(valor_metadado)


class BuscarValorMetadadoUseCase:
    """Caso de uso para buscar valores de metadados."""

    def __init__(self, repository: ValorMetadadoRepositoryInterface):
        self._repo = repository

    def get_by_id(self, valor_id: str) -> ValorMetadado:
        """Busca valor por ID."""
        valor = self._repo.get_by_id(valor_id)
        if valor is None:
            raise ValorMetadadoNaoEncontradoError(f"Valor '{valor_id}' não encontrado")
        return valor

    def get_by_entidade(self, entidade_tipo: str, entidade_id: str) -> list[ValorMetadado]:
        """Busca valores atribuídos a uma entidade."""
        return self._repo.get_by_entidade(entidade_tipo, entidade_id)

    def list_all(
        self, page: int = 0, page_size: int = 50,
        metadado_id: str | None = None, entidade_tipo: str | None = None,
    ) -> tuple:
        """Lista valores com paginação."""
        return self._repo.list_all(page, page_size, metadado_id, entidade_tipo)


class RemoverValorMetadadoUseCase:
    """Caso de uso para remover um valor de metadado."""

    def __init__(self, repository: ValorMetadadoRepositoryInterface):
        self._repo = repository

    def execute(self, valor_id: str) -> bool:
        """Remove um valor de metadado."""
        valor = self._repo.get_by_id(valor_id)
        if valor is None:
            raise ValorMetadadoNaoEncontradoError(f"Valor '{valor_id}' não encontrado")
        logger.info("Valor de metadado removido: %s", valor_id)
        return self._repo.delete(valor_id)


class ValidarValorMetadadoUseCase:
    """Caso de uso para validar um valor contra um metadado."""

    def __init__(self, metadado_repo: MetadadoRepositoryInterface):
        self._metadado_repo = metadado_repo

    def execute(self, metadado_id: str, valor: str) -> bool:
        """Valida se o valor é compatível com o tipo do metadado."""
        metadado = self._metadado_repo.get_by_id(metadado_id)
        if metadado is None:
            raise MetadadoNaoEncontradoError(f"Metadado '{metadado_id}' não encontrado")
        if not MetadadoService.validar_valor(metadado, valor):
            raise ValorMetadadoInvalidoError(
                f"Valor '{valor}' inválido para o metadado '{metadado.codigo}' "
                f"do tipo '{metadado.tipo_dado.value}'"
            )
        return True


__all__ = [
    "AtribuirValorMetadadoUseCase",
    "BuscarValorMetadadoUseCase",
    "RemoverValorMetadadoUseCase",
    "ValidarValorMetadadoUseCase",
]
