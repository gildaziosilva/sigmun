"""Casos de uso para gerenciamento de ativos de dados."""

import logging

from src.modules.sigmun_dad.application.interfaces import AtivoRepositoryInterface
from src.modules.sigmun_dad.application.use_cases.catalogo_use_cases import (
    AdicionarAtivoCatalogoUseCase,
    AtualizarCatalogoUseCase,
    BuscarCatalogoUseCase,
    CriarCatalogoUseCase,
    DeletarCatalogoUseCase,
    RemoverAtivoCatalogoUseCase,
)
from src.modules.sigmun_dad.application.use_cases.linhagem_use_cases import (
    AtualizarLinhagemUseCase,
    BuscarLinhagemUseCase,
    CriarLinhagemUseCase,
    DeletarLinhagemUseCase,
)
from src.modules.sigmun_dad.application.use_cases.politica_use_cases import (
    AdicionarRegraPoliticaUseCase,
    AtualizarPoliticaUseCase,
    BuscarPoliticaUseCase,
    CriarPoliticaUseCase,
    DeletarPoliticaUseCase,
    RemoverRegraPoliticaUseCase,
)
from src.modules.sigmun_dad.application.use_cases.qualidade_use_cases import (
    AtualizarQualidadeDadosUseCase,
    AvaliarQualidadeUseCase,
    BuscarQualidadeUseCase,
    DeletarQualidadeUseCase,
)
from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    TipoAtivoDado,
)
from src.modules.sigmun_dad.domain.exceptions import (
    AtivoJaExisteError,
    AtivoNaoEncontradoError,
    NomeAtivoInvalidoError,
)
from src.modules.sigmun_dad.domain.value_objects import NomeAtivo

logger = logging.getLogger(__name__)


class CriarAtivoUseCase:
    """Caso de uso para criar um novo ativo de dado."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def execute(
        self,
        nome: str,
        descricao: str,
        tipo: str,
        dono_id: str = "",
        steward_id: str = "",
        schema_origem: str = "",
        tabela_origem: str = "",
        classificacao: str = "",
        tags: list[str] = None,
    ) -> AtivoDado:
        """Cria um novo ativo de dado."""
        valido, msg = NomeAtivo.validar(nome)
        if not valido:
            raise NomeAtivoInvalidoError(f"Nome inválido: {msg}")

        if self._repo.exists_by_nome(nome):
            raise AtivoJaExisteError(f"Ativo com nome '{nome}' já existe")

        ativo = AtivoDado(
            nome=nome,
            descricao=descricao,
            tipo=TipoAtivoDado(tipo),
            dono_id=dono_id,
            steward_id=steward_id,
            schema_origem=schema_origem,
            tabela_origem=tabela_origem,
            classificacao=classificacao,
            tags=tags or [],
        )

        return self._repo.save(ativo)


class AtivarAtivoUseCase:
    """Caso de uso para ativar um ativo."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def execute(self, ativo_id: str) -> AtivoDado:
        """Ativa um ativo de dado."""
        ativo = self._repo.get_by_id(ativo_id)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")
        ativo.activate()
        return self._repo.save(ativo)


class DesativarAtivoUseCase:
    """Caso de uso para desativar um ativo."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def execute(self, ativo_id: str) -> AtivoDado:
        """Desativa um ativo de dado."""
        ativo = self._repo.get_by_id(ativo_id)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")
        ativo.deactivate()
        return self._repo.save(ativo)


class ArquivarAtivoUseCase:
    """Caso de uso para arquivar um ativo."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def execute(self, ativo_id: str) -> AtivoDado:
        """Arquiva um ativo de dado."""
        ativo = self._repo.get_by_id(ativo_id)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")
        ativo.archive()
        return self._repo.save(ativo)


class BuscarAtivoUseCase:
    """Caso de uso para buscar ativos."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def get_by_id(self, ativo_id: str) -> AtivoDado:
        """Busca ativo por ID."""
        ativo = self._repo.get_by_id(ativo_id)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")
        return ativo

    def get_by_nome(self, nome: str) -> AtivoDado:
        """Busca ativo por nome."""
        ativo = self._repo.get_by_nome(nome)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo com nome '{nome}' não encontrado")
        return ativo

    def list_all(
        self, page: int = 0, page_size: int = 50, tipo: str | None = None, status: str | None = None
    ) -> tuple:
        """Lista ativos com paginação."""
        return self._repo.list_all(page, page_size, tipo, status)


class AtualizarQualidadeUseCase:
    """Caso de uso para atualizar qualidade do ativo."""

    def __init__(self, repository: AtivoRepositoryInterface):
        self._repo = repository

    def execute(self, ativo_id: str, nivel: str) -> AtivoDado:
        """Atualiza nível de qualidade do ativo."""
        from src.modules.sigmun_dad.domain.entities import QualidadeNivel
        ativo = self._repo.get_by_id(ativo_id)
        if ativo is None:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado")
        ativo.update_quality(QualidadeNivel(nivel))
        return self._repo.save(ativo)


__all__ = [
    # Ativos
    "CriarAtivoUseCase",
    "AtivarAtivoUseCase",
    "DesativarAtivoUseCase",
    "ArquivarAtivoUseCase",
    "BuscarAtivoUseCase",
    "AtualizarQualidadeUseCase",
    # Catálogos
    "CriarCatalogoUseCase",
    "AtualizarCatalogoUseCase",
    "BuscarCatalogoUseCase",
    "DeletarCatalogoUseCase",
    "AdicionarAtivoCatalogoUseCase",
    "RemoverAtivoCatalogoUseCase",
    # Linhagens
    "CriarLinhagemUseCase",
    "AtualizarLinhagemUseCase",
    "BuscarLinhagemUseCase",
    "DeletarLinhagemUseCase",
    # Políticas
    "CriarPoliticaUseCase",
    "AtualizarPoliticaUseCase",
    "BuscarPoliticaUseCase",
    "DeletarPoliticaUseCase",
    "AdicionarRegraPoliticaUseCase",
    "RemoverRegraPoliticaUseCase",
    # Qualidade
    "AvaliarQualidadeUseCase",
    "AtualizarQualidadeDadosUseCase",
    "BuscarQualidadeUseCase",
    "DeletarQualidadeUseCase",
]
