"""Serviços de domínio do módulo de Dados Corporativos."""

import logging

from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    Catalogo,
    LinhagemDado,
)
from src.modules.sigmun_dad.domain.exceptions import (
    AtivoJaExisteError,
    AtivoNaoEncontradoError,
)

logger = logging.getLogger(__name__)


class CatalogoService:
    """Serviço de catálogo de dados."""

    @staticmethod
    def validar_ativo_unico(ativos: list[AtivoDado], nome: str, exclude_id: str = None) -> bool:
        """Valida se nome do ativo é único no catálogo."""
        for ativo in ativos:
            if ativo.nome.lower() == nome.lower() and ativo.id != exclude_id:
                return False
        return True

    @staticmethod
    def adicionar_ativo_ao_catalogo(catalogo: Catalogo, ativo: AtivoDado) -> Catalogo:
        """Adiciona ativo ao catálogo."""
        if ativo.id in catalogo.ativos_ids:
            raise AtivoJaExisteError(f"Ativo '{ativo.nome}' já está no catálogo")
        catalogo.add_ativo(ativo.id)
        logger.info("Ativo '%s' adicionado ao catálogo '%s'", ativo.nome, catalogo.nome)
        return catalogo

    @staticmethod
    def remover_ativo_do_catalogo(catalogo: Catalogo, ativo_id: str) -> Catalogo:
        """Remove ativo do catálogo."""
        if ativo_id not in catalogo.ativos_ids:
            raise AtivoNaoEncontradoError(f"Ativo '{ativo_id}' não encontrado no catálogo")
        catalogo.remove_ativo(ativo_id)
        logger.info("Ativo '%s' removido do catálogo '%s'", ativo_id, catalogo.nome)
        return catalogo


class LinhagemService:
    """Serviço de linhagem de dados."""

    @staticmethod
    def validar_linhagem_ciclica(
        linhagens: list[LinhagemDado], origem_id: str, destino_id: str
    ) -> bool:
        """Valida se a linhagem criaria um ciclo."""
        if origem_id == destino_id:
            return False
        # Verifica se destino já é origem de alguma linhagem que chega em origem
        for linhagem in linhagens:
            if linhagem.ativo_origem_id == destino_id and linhagem.ativo_destino_id == origem_id:
                return False
        return True

    @staticmethod
    def rastrear_origem(linhagens: list[LinhagemDado], ativo_id: str) -> list[str]:
        """Rastreia a origem de um ativo."""
        origens = []
        for linhagem in linhagens:
            if linhagem.ativo_destino_id == ativo_id:
                origens.append(linhagem.ativo_origem_id)
        return origens

    @staticmethod
    def rastrear_destinos(linhagens: list[LinhagemDado], ativo_id: str) -> list[str]:
        """Rastreia os destinos de um ativo."""
        destinos = []
        for linhagem in linhagens:
            if linhagem.ativo_origem_id == ativo_id:
                destinos.append(linhagem.ativo_destino_id)
        return destinos


class GovernançaService:
    """Serviço de governança de dados."""

    @staticmethod
    def validar_classificacao(classificacao: str) -> bool:
        """Valida classificação do dado."""
        from src.modules.sigmun_dad.domain.value_objects import ClassificacaoDado
        valido, _ = ClassificacaoDado.validar(classificacao)
        return valido

    @staticmethod
    def pode_ser_publico(ativo: AtivoDado) -> bool:
        """Verifica se ativo pode ser tornado público."""
        return ativo.classificacao.upper() == "PUBLICO"

    @staticmethod
    def requer_aprovacao(ativo: AtivoDado) -> bool:
        """Verifica se ativo requer aprovação para ativação."""
        return ativo.classificacao.upper() in ["CONFIDENCIAL", "RESTRITO", "SENSIVEL"]


__all__ = [
    "CatalogoService",
    "LinhagemService",
    "GovernançaService",
]
