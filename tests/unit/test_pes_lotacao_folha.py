"""Testes de lotacao e folha (DOM-PES)."""

from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioFolha,
    RepositorioLotacao,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_folha import (
    AbrirFolhaInput,
    AbrirFolhaUseCase,
    ConsolidarFolhaInput,
    ConsolidarFolhaUseCase,
    FecharFolhaUseCase,
    HomologarFolhaUseCase,
    PagarFolhaUseCase,
)
from src.modules.sigmun_rh.application.use_cases_lotacao import (
    LotarServidorInput,
    LotarServidorUseCase,
)
from src.modules.sigmun_rh.domain.entities.folha import FolhaPagamento, StatusFolha
from src.modules.sigmun_rh.domain.entities.lotacao import Lotacao
from src.modules.sigmun_rh.domain.entities.servidor import Servidor


def _servidor() -> Servidor:
    return Servidor(id="s1", matricula="001", cpf="12345678901",
                    nome="Ana", cargo_id="c1",
                    data_admissao=date(2024, 1, 1))


class TestLotacao:
    """Lotacao de servidores."""

    def test_lotar(self) -> None:
        """Lota servidor ativo."""
        servidores = MagicMock(spec=RepositorioServidor)
        servidores.get_by_id = MagicMock(return_value=_servidor())
        lotacoes = MagicMock(spec=RepositorioLotacao)
        lotacoes.list_vigentes_por_servidor = MagicMock(return_value=[])
        lotacoes.save = MagicMock(
            return_value=Lotacao(id="l1", servidor_id="s1",
                                 unidade_id="u1",
                                 data_inicio=date(2024, 2, 1))
        )
        uc = LotarServidorUseCase(lotacoes, servidores)
        dto = LotarServidorInput(servidor_id="s1", unidade_id="u1",
                                 data_inicio=date(2024, 2, 1))
        result = uc.execute(dto)
        assert result.unidade_id == "u1"


class TestFolha:
    """Ciclo de vida da folha."""

    def test_ciclo(self) -> None:
        """Abre, consolida, fecha, homologa e paga."""
        repo = MagicMock(spec=RepositorioFolha)
        repo.get_by_competencia = MagicMock(return_value=None)
        folha = FolhaPagamento(id="f1", competencia_ano=2024,
                               competencia_mes=5)
        repo.save = MagicMock(return_value=folha)
        repo.get_by_id = MagicMock(return_value=folha)
        AbrirFolhaUseCase(repo).execute(AbrirFolhaInput(2024, 5))
        ConsolidarFolhaUseCase(repo).execute(
            ConsolidarFolhaInput(folha_id="f1", proventos=1000.0,
                                 descontos=100.0,
                                 quantidade_servidores=2)
        )
        assert folha.total_liquido == 900.0
        FecharFolhaUseCase(repo).execute("f1")
        assert folha.status == StatusFolha.FECHADA
        HomologarFolhaUseCase(repo).execute("f1")
        assert folha.status == StatusFolha.HOMOLOGADA
        PagarFolhaUseCase(repo).execute("f1")
        assert folha.status == StatusFolha.PAGA

    def test_fechar_sem_lancamento(self) -> None:
        """Fechamento sem lancamento gera erro."""
        folha = FolhaPagamento(id="f1", competencia_ano=2024,
                               competencia_mes=5)
        repo = MagicMock(spec=RepositorioFolha)
        repo.get_by_id = MagicMock(return_value=folha)
        with pytest.raises(Exception):
            FecharFolhaUseCase(repo).execute("f1")
