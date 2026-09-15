"""Casos de uso para Controles de Segurança."""

import logging
from datetime import datetime

from src.modules.sigmun_seg.application.interfaces import (
    ControleSegurancaRepositoryInterface,
)
from src.modules.sigmun_seg.domain.entities import (
    CategoriaControle,
    ControleSeguranca,
    StatusControle,
    TipoControle,
)
from src.modules.sigmun_seg.domain.exceptions import (
    ControleJaExisteError,
    ControleNaoEncontradoError,
    NivelRiscoInvalidoError,
)
from src.modules.sigmun_seg.domain.value_objects import CodigoControle, NivelRisco

logger = logging.getLogger(__name__)


class CriarControleSegurancaUseCase:
    """Cria um novo controle de segurança."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        codigo: str,
        nome: str,
        descricao: str = "",
        tipo: str = "tecnico",
        categoria: str = "acesso",
        responsavel_id: str = "",
        nivel_risco: str = "medio",
    ) -> ControleSeguranca:
        """Cria um novo controle de segurança."""
        valido, msg = CodigoControle.validar(codigo)
        if not valido:
            raise ValueError(msg)

        valido, msg = NivelRisco.validar(nivel_risco)
        if not valido:
            raise NivelRiscoInvalidoError(msg)

        if self._repo.exists_by_codigo(codigo):
            raise ControleJaExisteError(f"Controle '{codigo}' já existe")

        controle = ControleSeguranca(
            codigo=codigo,
            nome=nome,
            descricao=descricao,
            tipo=TipoControle(tipo),
            categoria=CategoriaControle(categoria),
            status=StatusControle.PLANEJADO,
            responsavel_id=responsavel_id,
            nivel_risco=nivel_risco,
        )
        logger.info("Controle criado: %s", controle.codigo)
        return self._repo.save(controle)


class BuscarControleSegurancaUseCase:
    """Busca controles de segurança."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def get_by_id(self, controle_id: str) -> ControleSeguranca:
        controle = self._repo.get_by_id(controle_id)
        if controle is None:
            raise ControleNaoEncontradoError(f"Controle '{controle_id}' não encontrado")
        return controle

    def list_all(
        self,
        page: int = 0,
        page_size: int = 50,
        status: str | None = None,
        tipo: str | None = None,
        categoria: str | None = None,
    ) -> tuple:
        return self._repo.list_all(page, page_size, status, tipo, categoria)


class AtualizarControleSegurancaUseCase:
    """Atualiza um controle de segurança."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        controle_id: str,
        nome: str | None = None,
        descricao: str | None = None,
        tipo: str | None = None,
        categoria: str | None = None,
        responsavel_id: str | None = None,
        nivel_risco: str | None = None,
    ) -> ControleSeguranca:
        controle = self._repo.get_by_id(controle_id)
        if controle is None:
            raise ControleNaoEncontradoError(f"Controle '{controle_id}' não encontrado")

        if nome is not None:
            controle.nome = nome
        if descricao is not None:
            controle.descricao = descricao
        if tipo is not None:
            controle.tipo = TipoControle(tipo)
        if categoria is not None:
            controle.categoria = CategoriaControle(categoria)
        if responsavel_id is not None:
            controle.responsavel_id = responsavel_id
        if nivel_risco is not None:
            valido, msg = NivelRisco.validar(nivel_risco)
            if not valido:
                raise NivelRiscoInvalidoError(msg)
            controle.nivel_risco = nivel_risco

        controle.updated_at = datetime.utcnow()
        return self._repo.save(controle)


class ImplementarControleSegurancaUseCase:
    """Marca um controle como implementado."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, controle_id: str) -> ControleSeguranca:
        controle = self._repo.get_by_id(controle_id)
        if controle is None:
            raise ControleNaoEncontradoError(f"Controle '{controle_id}' não encontrado")
        controle.implementar()
        return self._repo.save(controle)


class ParcialmenteImplementadoUseCase:
    """Marca um controle como parcialmente implementado."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, controle_id: str) -> ControleSeguranca:
        controle = self._repo.get_by_id(controle_id)
        if controle is None:
            raise ControleNaoEncontradoError(f"Controle '{controle_id}' não encontrado")
        controle.parcial()
        return self._repo.save(controle)


class DeletarControleSegurancaUseCase:
    """Remove um controle de seguranção (soft-delete)."""

    def __init__(self, repository: ControleSegurancaRepositoryInterface):
        self._repo = repository

    def execute(self, controle_id: str) -> bool:
        controle = self._repo.get_by_id(controle_id)
        if controle is None:
            raise ControleNaoEncontradoError(f"Controle '{controle_id}' não encontrado")
        return self._repo.delete(controle_id)


__all__ = [
    "CriarControleSegurancaUseCase",
    "BuscarControleSegurancaUseCase",
    "AtualizarControleSegurancaUseCase",
    "ImplementarControleSegurancaUseCase",
    "ParcialmenteImplementadoUseCase",
    "DeletarControleSegurancaUseCase",
]
