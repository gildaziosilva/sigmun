"""Testes de casos de uso do DOM-PAT (Gestão Patrimonial)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_patrimonio.application.interfaces import (
    RepositorioBem,
    RepositorioDepreciacao,
    RepositorioTransferencia,
)
from src.modules.sigmun_patrimonio.application.use_cases import (
    BaixarBemUseCase,
    CadastrarBemInput,
    CadastrarBemUseCase,
    ConcluirTransferenciaUseCase,
    DepreciarBemUseCase,
    TransferirBemInput,
    TransferirBemUseCase,
)
from src.modules.sigmun_patrimonio.domain.entities.bem import Bem, StatusBem
from src.modules.sigmun_patrimonio.domain.entities.transferencia import (
    StatusTransferencia,
)
from src.modules.sigmun_patrimonio.domain.exceptions import (
    BemNaoEncontradoError,
    BemJaExistenteError,
)


def _bem(codigo: str = "TMB-001") -> Bem:
    return Bem(
        codigo=codigo, descricao="Notebook", valor_aquisicao=10000.0,
        valor_residual=1000.0, vida_util_anos=3, valor_contabil=10000.0,
    )


class TestBem:
    """Cadastro de bens."""

    def test_cadastra_bem(self) -> None:
        repo = MagicMock(spec=RepositorioBem)
        repo.get_by_codigo = MagicMock(return_value=None)
        novo = _bem()
        novo.id = "b-1"
        repo.save = MagicMock(return_value=novo)
        result = CadastrarBemUseCase(repo).execute(
            CadastrarBemInput(
                codigo="TMB-001", tipo="movel", descricao="Notebook",
                valor_aquisicao=10000.0, valor_residual=1000.0, vida_util_anos=3,
            )
        )
        assert result.codigo == "TMB-001"
        assert result.valor_contabil == 10000.0

    def test_tombo_duplicado(self) -> None:
        repo = MagicMock(spec=RepositorioBem)
        repo.get_by_codigo = MagicMock(return_value=_bem())
        with pytest.raises(BemJaExistenteError):
            CadastrarBemUseCase(repo).execute(
                CadastrarBemInput(
                    codigo="TMB-001", tipo="movel", descricao="X",
                    valor_aquisicao=1000.0,
                )
            )


class TestDepreciacao:
    """Depreciação linear de bens."""

    def test_deprecia_anual(self) -> None:
        bens = MagicMock(spec=RepositorioBem)
        dep_repo = MagicMock(spec=RepositorioDepreciacao)
        bem = _bem()
        bem.id = "b-1"
        bens.get_by_id = MagicMock(return_value=bem)
        bens.save = MagicMock(return_value=bem)
        dep_repo.list_by_bem = MagicMock(return_value=[])
        dep = MagicMock()
        dep.valor_depreciado = 3000.0
        dep.valor_acumulado = 3000.0
        dep.valor_liquido = 7000.0
        dep_repo.save = MagicMock(return_value=dep)
        result = DepreciarBemUseCase(bens, dep_repo).execute("b-1")
        # valor depreciavel = (10000 - 1000)/3 = 3000
        assert result.valor_depreciado == 3000.0
        assert bem.valor_contabil == 7000.0

    def test_baixado_nao_deprecia(self) -> None:
        bens = MagicMock(spec=RepositorioBem)
        dep_repo = MagicMock(spec=RepositorioDepreciacao)
        bem = _bem()
        bem.status = StatusBem.BAIXADO
        bens.get_by_id = MagicMock(return_value=bem)
        with pytest.raises(Exception):
            DepreciarBemUseCase(bens, dep_repo).execute("b-1")


class TestTransferencia:
    """Transferência de bens."""

    def test_transfere_e_conclui(self) -> None:
        bens = MagicMock(spec=RepositorioBem)
        trans = MagicMock(spec=RepositorioTransferencia)
        bem = _bem()
        bem.localizacao = "Sede"
        bens.get_by_id = MagicMock(return_value=bem)
        bens.save = MagicMock(return_value=bem)
        t = MagicMock()
        t.id = "t-1"
        t.status = StatusTransferencia.PENDENTE
        t.bem_id = "b-1"
        t.para_localizacao = "Depósito"
        trans.save = MagicMock(return_value=t)
        realizada = TransferirBemUseCase(bens, trans).execute(
            TransferirBemInput(bem_id="b-1", para_localizacao="Depósito")
        )
        assert bem.status == StatusBem.EM_TRANSFERENCIA

        trans.get_by_id = MagicMock(return_value=t)
        concluida = ConcluirTransferenciaUseCase(trans, bens).execute("t-1")
        assert concluida.id == "t-1"
        assert bem.localizacao == "Depósito"
        assert bem.status == StatusBem.EM_USO

    def test_baixar_bem(self) -> None:
        repo = MagicMock(spec=RepositorioBem)
        bem = _bem()
        repo.get_by_id = MagicMock(return_value=bem)
        repo.save = MagicMock(return_value=bem)
        resultado = BaixarBemUseCase(repo).execute("b-1")
        assert resultado.status == StatusBem.BAIXADO

    def test_baixar_inexistente(self) -> None:
        repo = MagicMock(spec=RepositorioBem)
        repo.get_by_id = MagicMock(return_value=None)
        with pytest.raises(BemNaoEncontradoError):
            BaixarBemUseCase(repo).execute("b-x")