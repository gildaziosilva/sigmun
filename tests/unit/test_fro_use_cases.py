"""Testes de casos de uso do DOM-FRO (Gestão de Frota)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_frotas.application.interfaces import (
    RepositorioAbastecimento,
    RepositorioManutencao,
    RepositorioRota,
    RepositorioVeiculo,
)
from src.modules.sigmun_frotas.application.use_cases import (
    AbrirManutencaoUseCase,
    CadastrarVeiculoInput,
    CadastrarVeiculoUseCase,
    ConcluirManutencaoUseCase,
    ConcluirRotaUseCase,
    RegistrarAbastecimentoInput,
    RegistrarAbastecimentoUseCase,
    RegistrarRotaInput,
    RegistrarRotaUseCase,
)
from src.modules.sigmun_frotas.domain.entities.veiculo import (
    StatusVeiculo,
    Veiculo,
)
from src.modules.sigmun_frotas.domain.exceptions import (
    VeiculoJaExistenteError,
    VeiculoNaoEncontradoError,
)


def _veiculo(placa: str = "ABC-1234") -> Veiculo:
    return Veiculo(placa=placa, marca="Fiat", modelo="Uno", odometro_atual=1000.0)


class TestVeiculo:
    """Cadastro de veículos."""

    def test_cadastra_veiculo(self) -> None:
        repo = MagicMock(spec=RepositorioVeiculo)
        repo.get_by_placa = MagicMock(return_value=None)
        novo = _veiculo()
        novo.id = "v-1"
        repo.save = MagicMock(return_value=novo)
        result = CadastrarVeiculoUseCase(repo).execute(
            CadastrarVeiculoInput(
                placa="ABC-1234", marca="Fiat", modelo="Uno"
            )
        )
        assert result.placa == "ABC-1234"
        assert result.status == StatusVeiculo.ATIVO

    def test_placa_duplicada(self) -> None:
        repo = MagicMock(spec=RepositorioVeiculo)
        repo.get_by_placa = MagicMock(return_value=_veiculo())
        with pytest.raises(VeiculoJaExistenteError):
            CadastrarVeiculoUseCase(repo).execute(
                CadastrarVeiculoInput(placa="ABC-1234", marca="F", modelo="U")
            )


class TestAbastecimento:
    """Registro de abastecimentos."""

    def test_registra_e_atualiza_odometro(self) -> None:
        abast = MagicMock(spec=RepositorioAbastecimento)
        veiculos = MagicMock(spec=RepositorioVeiculo)
        veiculo = _veiculo()
        veiculos.get_by_id = MagicMock(return_value=veiculo)
        veiculos.save = MagicMock(return_value=veiculo)
        abastecimento = MagicMock()
        abastecimento.valor_total = 0.0
        abast.save = MagicMock(side_effect=lambda a: a)
        result = RegistrarAbastecimentoUseCase(abast, veiculos).execute(
            RegistrarAbastecimentoInput(
                veiculo_id="v-1", quantidade_litros=50.0,
                valor_unitario=6.0, odometro=1500.0,
            )
        )
        assert result.valor_total == 300.0
        assert veiculo.odometro_atual == 1500.0

    def test_veiculo_inexistente(self) -> None:
        abast = MagicMock(spec=RepositorioAbastecimento)
        veiculos = MagicMock(spec=RepositorioVeiculo)
        veiculos.get_by_id = MagicMock(return_value=None)
        with pytest.raises(VeiculoNaoEncontradoError):
            RegistrarAbastecimentoUseCase(abast, veiculos).execute(
                RegistrarAbastecimentoInput(veiculo_id="x", quantidade_litros=10.0)
            )


class TestManutencao:
    """Ciclo de manutenção."""

    def test_abre_e_conclui(self) -> None:
        manut = MagicMock(spec=RepositorioManutencao)
        veiculos = MagicMock(spec=RepositorioVeiculo)
        veiculo = _veiculo()
        veiculos.get_by_id = MagicMock(return_value=veiculo)
        veiculos.save = MagicMock(return_value=veiculo)
        m = MagicMock()
        m.id = "m-1"
        m.veiculo_id = "v-1"
        manut.save = MagicMock(side_effect=lambda x: x)
        aberta = AbrirManutencaoUseCase(manut, veiculos).execute(
            "v-1", descricao="Troca de óleo"
        )
        assert veiculo.status == StatusVeiculo.MANUTENCAO

        manut.get_by_id = MagicMock(return_value=aberta)
        concluida = ConcluirManutencaoUseCase(manut, veiculos).execute("m-1")
        assert veiculo.status == StatusVeiculo.ATIVO


class TestRota:
    """Registro de rotas/deslocamentos."""

    def test_registra_e_conclui(self) -> None:
        rotas = MagicMock(spec=RepositorioRota)
        veiculos = MagicMock(spec=RepositorioVeiculo)
        veiculo = _veiculo()
        veiculos.get_by_id = MagicMock(return_value=veiculo)
        veiculos.save = MagicMock(return_value=veiculo)
        rotas.save = MagicMock(side_effect=lambda r: r)
        rotas.get_by_id = MagicMock()
        rota_criada = RegistrarRotaUseCase(rotas, veiculos).execute(
            RegistrarRotaInput(
                veiculo_id="v-1", origem="Sede", destino="Distrito",
                km_inicio=1000.0, km_fim=1050.0,
            )
        )
        assert rota_criada.distancia_km == 50.0

        rotas.get_by_id = MagicMock(return_value=rota_criada)
        concluida = ConcluirRotaUseCase(rotas, veiculos).execute("r-1")
        assert concluida.distancia_km == 50.0
        assert veiculo.odometro_atual == 1050.0