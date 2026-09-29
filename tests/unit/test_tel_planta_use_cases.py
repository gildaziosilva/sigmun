"""Testes de casos de uso do DOM-TEL (Gestão Territorial) — planta de valores."""

from __future__ import annotations

import pytest

from src.modules.sigmun_territorial.application.use_cases import (
    AtivarPlantaValoresUseCase,
    AtualizarPlantaValoresInput,
    AtualizarPlantaValoresUseCase,
    CadastrarPlantaValoresInput,
    CadastrarPlantaValoresUseCase,
    RevogarPlantaValoresUseCase,
)
from src.modules.sigmun_territorial.domain.entities import (
    SituacaoPlantaValores,
    TipoOcupacaoImovel,
)
from src.modules.sigmun_territorial.domain.exceptions import (
    BairroNaoEncontradoError,
    PlantaValoresJaExistenteError,
    PlantaValoresNaoEncontradaError,
    RegraNegocioError,
)
from tests.unit.tel_fixtures import _bairro as bairro
from tests.unit.tel_fixtures import _planta as planta
from tests.unit.tel_fixtures import repo_bairro, repo_planta


def _bairro_cadastrado():
    alvo = bairro()
    alvo.id = "bairro-1"
    return alvo


class TestPlantaValores:
    def test_cadastra_planta_rascunho(self) -> None:
        result = CadastrarPlantaValoresUseCase(
            repo_planta(), repo_bairro(_bairro_cadastrado())
        ).execute(
            CadastrarPlantaValoresInput(
                ano=2026, bairro_id="bairro-1", valor_terreno_m2=180.0, valor_construcao_m2=950.0
            )
        )
        assert result.situacao == SituacaoPlantaValores.RASCUNHO
        assert result.ocupacao == TipoOcupacaoImovel.RESIDENCIAL

    def test_cadastra_ja_vigente(self) -> None:
        result = CadastrarPlantaValoresUseCase(
            repo_planta(), repo_bairro(_bairro_cadastrado())
        ).execute(
            CadastrarPlantaValoresInput(ano=2026, bairro_id="bairro-1", ativar=True)
        )
        assert result.esta_vigente

    def test_nao_duplica_planta_vigente(self) -> None:
        """RN-TEL-003: no máximo uma planta vigente por ano/bairro/ocupação."""
        repo = repo_planta()
        repo.get_vigente.return_value = planta(SituacaoPlantaValores.VIGENTE)
        with pytest.raises(PlantaValoresJaExistenteError):
            CadastrarPlantaValoresUseCase(repo, repo_bairro(_bairro_cadastrado())).execute(
                CadastrarPlantaValoresInput(
                    ano=2026, bairro_id="bairro-1", ativar=True
                )
            )

    def test_exige_bairro(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarPlantaValoresUseCase(repo_planta(), repo_bairro()).execute(
                CadastrarPlantaValoresInput(ano=2026, bairro_id="")
            )

    def test_exige_bairro_existente(self) -> None:
        with pytest.raises(BairroNaoEncontradoError):
            CadastrarPlantaValoresUseCase(repo_planta(), repo_bairro()).execute(
                CadastrarPlantaValoresInput(ano=2026, bairro_id="bairro-9")
            )

    def test_ocupacao_invalida_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarPlantaValoresUseCase(
                repo_planta(), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarPlantaValoresInput(ano=2026, bairro_id="bairro-1", ocupacao="x")
            )

    def test_ano_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarPlantaValoresUseCase(
                repo_planta(), repo_bairro(_bairro_cadastrado())
            ).execute(CadastrarPlantaValoresInput(ano=1800, bairro_id="bairro-1"))

    def test_valor_negativo_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarPlantaValoresUseCase(
                repo_planta(), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarPlantaValoresInput(
                    ano=2026, bairro_id="bairro-1", valor_terreno_m2=-1.0
                )
            )

    def test_aliquota_fora_de_faixa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarPlantaValoresUseCase(
                repo_planta(), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarPlantaValoresInput(
                    ano=2026, bairro_id="bairro-1", aliquota_percent=150.0
                )
            )


    def test_ativa_planta(self) -> None:
        alvo = planta()
        alvo.id = "planta-1"
        result = AtivarPlantaValoresUseCase(repo_planta(alvo)).execute("planta-1")
        assert result.situacao == SituacaoPlantaValores.VIGENTE

    def test_planta_inexistente_nao_ativa(self) -> None:
        with pytest.raises(PlantaValoresNaoEncontradaError):
            AtivarPlantaValoresUseCase(repo_planta()).execute("planta-9")

    def test_nao_ativa_planta_ja_vigente(self) -> None:
        """RN-TEL-004: somente rascunho pode ser ativado."""
        alvo = planta(SituacaoPlantaValores.VIGENTE)
        alvo.id = "planta-1"
        with pytest.raises(RegraNegocioError):
            AtivarPlantaValoresUseCase(repo_planta(alvo)).execute("planta-1")

    def test_revoga_planta_com_justificativa(self) -> None:
        alvo = planta(SituacaoPlantaValores.VIGENTE)
        alvo.id = "planta-1"
        result = RevogarPlantaValoresUseCase(repo_planta(alvo)).execute(
            "planta-1", "Lei 1.234/2026"
        )
        assert result.situacao == SituacaoPlantaValores.REVOGADA
        assert "Lei 1.234/2026" in result.legislacao

    def test_revogacao_exige_motivo(self) -> None:
        alvo = planta(SituacaoPlantaValores.VIGENTE)
        alvo.id = "planta-1"
        with pytest.raises(RegraNegocioError):
            RevogarPlantaValoresUseCase(repo_planta(alvo)).execute("planta-1", "")

    def test_nao_revoga_planta_rascunho(self) -> None:
        alvo = planta()
        alvo.id = "planta-1"
        with pytest.raises(RegraNegocioError):
            RevogarPlantaValoresUseCase(repo_planta(alvo)).execute("planta-1", "motivo")

    def test_atualiza_planta_rascunho(self) -> None:
        alvo = planta()
        alvo.id = "planta-1"
        result = AtualizarPlantaValoresUseCase(repo_planta(alvo)).execute(
            AtualizarPlantaValoresInput(planta_id="planta-1", valor_terreno_m2=250.0)
        )
        assert result.valor_terreno_m2 == 250.0

    def test_nao_atualiza_planta_vigente(self) -> None:
        """RN-TEL-004: planta vigente é preservada como evidência histórica."""
        alvo = planta(SituacaoPlantaValores.VIGENTE)
        alvo.id = "planta-1"
        with pytest.raises(RegraNegocioError):
            AtualizarPlantaValoresUseCase(repo_planta(alvo)).execute(
                AtualizarPlantaValoresInput(planta_id="planta-1", valor_terreno_m2=250.0)
            )

    def test_atualiza_valor_negativo_rejeitado(self) -> None:
        alvo = planta()
        alvo.id = "planta-1"
        with pytest.raises(RegraNegocioError):
            AtualizarPlantaValoresUseCase(repo_planta(alvo)).execute(
                AtualizarPlantaValoresInput(planta_id="planta-1", valor_terreno_m2=-1.0)
            )

    def test_atualiza_planta_inexistente(self) -> None:
        with pytest.raises(PlantaValoresNaoEncontradaError):
            AtualizarPlantaValoresUseCase(repo_planta()).execute(
                AtualizarPlantaValoresInput(planta_id="planta-9")
            )

