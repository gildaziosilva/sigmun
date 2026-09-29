"""Testes de casos de uso do DOM-TEL (Gestão Territorial) — bairros."""

from __future__ import annotations

import pytest

from src.modules.sigmun_territorial.application.use_cases import (
    AtualizarBairroInput,
    AtualizarBairroUseCase,
    CadastrarBairroInput,
    CadastrarBairroUseCase,
    ExcluirBairroUseCase,
)
from src.modules.sigmun_territorial.domain.entities import SituacaoBairro
from src.modules.sigmun_territorial.domain.exceptions import (
    BairroComDependenciasError,
    BairroJaExistenteError,
    BairroNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.tel_fixtures import _bairro as bairro
from tests.unit.tel_fixtures import _logradouro as logradouro
from tests.unit.tel_fixtures import repo_bairro, repo_logradouro


class TestBairro:
    def test_cadastra_bairro(self) -> None:
        result = CadastrarBairroUseCase(repo_bairro()).execute(
            CadastrarBairroInput(codigo="BR-01", nome="Centro", populacao_estimada=1000)
        )
        assert result.codigo == "BR-01"
        assert result.esta_ativo
        assert result.populacao_estimada == 1000

    def test_nao_duplica_codigo(self) -> None:
        """RN-TEL-001: o código do bairro é único."""
        with pytest.raises(BairroJaExistenteError):
            CadastrarBairroUseCase(repo_bairro(bairro())).execute(
                CadastrarBairroInput(codigo="BR-01", nome="Centro")
            )

    def test_codigo_e_nome_obrigatorios(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarBairroUseCase(repo_bairro()).execute(
                CadastrarBairroInput(codigo="", nome="Centro")
            )

    def test_tipo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarBairroUseCase(repo_bairro()).execute(
                CadastrarBairroInput(codigo="BR-01", nome="Centro", tipo="x")
            )

    def test_area_negativa_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarBairroUseCase(repo_bairro()).execute(
                CadastrarBairroInput(codigo="BR-01", nome="Centro", area_km2=-1.0)
            )

    def test_atualiza_campos(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        result = AtualizarBairroUseCase(repo_bairro(alvo)).execute(
            AtualizarBairroInput(bairro_id="bairro-1", nome="Centro Historico")
        )
        assert result.nome == "Centro Historico"

    def test_atualiza_situacao_inativa_e_ativa(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        use_case = AtualizarBairroUseCase(repo_bairro(alvo))
        assert use_case.execute(
            AtualizarBairroInput(bairro_id="bairro-1", situacao="inativo")
        ).situacao == SituacaoBairro.INATIVO
        assert use_case.execute(
            AtualizarBairroInput(bairro_id="bairro-1", situacao="ativo")
        ).esta_ativo

    def test_atualiza_tipo_invalido(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        with pytest.raises(RegraNegocioError):
            AtualizarBairroUseCase(repo_bairro(alvo)).execute(
                AtualizarBairroInput(bairro_id="bairro-1", tipo="x")
            )

    def test_atualiza_codigo_duplicado(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        repo = repo_bairro(alvo)
        repo.get_by_codigo.return_value = bairro("BR-99")
        with pytest.raises(BairroJaExistenteError):
            AtualizarBairroUseCase(repo).execute(
                AtualizarBairroInput(bairro_id="bairro-1", codigo="BR-99")
            )

    def test_atualiza_bairro_inexistente(self) -> None:
        with pytest.raises(BairroNaoEncontradoError):
            AtualizarBairroUseCase(repo_bairro()).execute(
                AtualizarBairroInput(bairro_id="bairro-9", nome="X")
            )

    def test_exclui_logicamente(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        result = ExcluirBairroUseCase(repo_bairro(alvo), repo_logradouro()).execute(
            "bairro-1"
        )
        assert result.is_deleted is True

    def test_bairro_com_logradouro_ativo_bloqueia_exclusao(self) -> None:
        """RN-TEL-006: bairro com logradouro ativo não pode ser excluído."""
        alvo = bairro()
        alvo.id = "bairro-1"
        with pytest.raises(BairroComDependenciasError):
            ExcluirBairroUseCase(
                repo_bairro(alvo), repo_logradouro(logradouro())
            ).execute("bairro-1")

    def test_bairro_com_logradouro_inativo_pode_ser_excluido(self) -> None:
        alvo = bairro()
        alvo.id = "bairro-1"
        lg = logradouro()
        lg.inativar()
        result = ExcluirBairroUseCase(repo_bairro(alvo), repo_logradouro(lg)).execute(
            "bairro-1"
        )
        assert result.is_deleted is True

    def test_exclui_bairro_inexistente(self) -> None:
        with pytest.raises(BairroNaoEncontradoError):
            ExcluirBairroUseCase(repo_bairro(), repo_logradouro()).execute("bairro-9")
