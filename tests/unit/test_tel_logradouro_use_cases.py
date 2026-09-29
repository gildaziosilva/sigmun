"""Testes de casos de uso do DOM-TEL (Gestão Territorial) — logradouros."""

from __future__ import annotations

import pytest

from src.modules.sigmun_territorial.application.use_cases import (
    AtualizarLogradouroInput,
    AtualizarLogradouroUseCase,
    CadastrarLogradouroInput,
    CadastrarLogradouroUseCase,
    ExcluirLogradouroUseCase,
)
from src.modules.sigmun_territorial.domain.entities import SituacaoLogradouro
from src.modules.sigmun_territorial.domain.exceptions import (
    BairroNaoEncontradoError,
    LogradouroJaExistenteError,
    LogradouroNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.tel_fixtures import _bairro as bairro
from tests.unit.tel_fixtures import _logradouro as logradouro
from tests.unit.tel_fixtures import repo_bairro, repo_logradouro


def _bairro_cadastrado() -> object:
    alvo = bairro()
    alvo.id = "bairro-1"
    return alvo


class TestLogradouro:
    def test_cadastra_logradouro(self) -> None:
        result = CadastrarLogradouroUseCase(
            repo_logradouro(), repo_bairro(_bairro_cadastrado())
        ).execute(
            CadastrarLogradouroInput(
                codigo="LG-01", nome="Rua da Matriz", bairro_id="bairro-1"
            )
        )
        assert result.codigo == "LG-01"
        assert result.esta_ativo
        assert result.bairro_id == "bairro-1"

    def test_nao_duplica_codigo(self) -> None:
        """RN-TEL-002: o código do logradouro é único."""
        with pytest.raises(LogradouroJaExistenteError):
            CadastrarLogradouroUseCase(
                repo_logradouro(logradouro()), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarLogradouroInput(codigo="LG-01", nome="Outra", bairro_id="bairro-1")
            )

    def test_exige_bairro_existente(self) -> None:
        """RN-TEL-002: todo logradouro pertence a um bairro cadastrado."""
        with pytest.raises(BairroNaoEncontradoError):
            CadastrarLogradouroUseCase(repo_logradouro(), repo_bairro()).execute(
                CadastrarLogradouroInput(codigo="LG-01", nome="Rua", bairro_id="bairro-9")
            )

    def test_codigo_e_nome_obrigatorios(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarLogradouroUseCase(
                repo_logradouro(), repo_bairro(_bairro_cadastrado())
            ).execute(CadastrarLogradouroInput(codigo="", nome="Rua", bairro_id="bairro-1"))

    def test_tipo_invalido_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarLogradouroUseCase(
                repo_logradouro(), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarLogradouroInput(
                    codigo="LG-01", nome="Rua", bairro_id="bairro-1", tipo="x"
                )
            )

    def test_numero_final_menor_que_inicial_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarLogradouroUseCase(
                repo_logradouro(), repo_bairro(_bairro_cadastrado())
            ).execute(
                CadastrarLogradouroInput(
                    codigo="LG-01",
                    nome="Rua",
                    bairro_id="bairro-1",
                    numero_inicial=100,
                    numero_final=10,
                )
            )

    def test_atualiza_campos(self) -> None:
        lg = logradouro()
        lg.id = "lg-1"
        result = AtualizarLogradouroUseCase(repo_logradouro(lg), repo_bairro()).execute(
            AtualizarLogradouroInput(logradouro_id="lg-1", nome="Rua Nova")
        )
        assert result.nome == "Rua Nova"

    def test_atualiza_situacao_em_obra(self) -> None:
        lg = logradouro()
        lg.id = "lg-1"
        result = AtualizarLogradouroUseCase(repo_logradouro(lg), repo_bairro()).execute(
            AtualizarLogradouroInput(logradouro_id="lg-1", situacao="em_obra")
        )
        assert result.situacao == SituacaoLogradouro.EM_OBRA

    def test_atualiza_tipo_invalido(self) -> None:
        lg = logradouro()
        lg.id = "lg-1"
        with pytest.raises(RegraNegocioError):
            AtualizarLogradouroUseCase(repo_logradouro(lg), repo_bairro()).execute(
                AtualizarLogradouroInput(logradouro_id="lg-1", tipo="x")
            )

    def test_atualiza_logradouro_inexistente(self) -> None:
        with pytest.raises(LogradouroNaoEncontradoError):
            AtualizarLogradouroUseCase(repo_logradouro(), repo_bairro()).execute(
                AtualizarLogradouroInput(logradouro_id="lg-9", nome="X")
            )

    def test_exclui_logicamente(self) -> None:
        lg = logradouro()
        lg.id = "lg-1"
        assert ExcluirLogradouroUseCase(repo_logradouro(lg)).execute("lg-1").is_deleted is True

    def test_exclui_logradouro_inexistente(self) -> None:
        with pytest.raises(LogradouroNaoEncontradoError):
            ExcluirLogradouroUseCase(repo_logradouro()).execute("lg-9")
