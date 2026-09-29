"""Testes de casos de uso do DOM-OBR — cadastro e ciclo de vida (RN-OBR-001/002/003/004)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_obras.application.use_cases import (
    AtualizarObraInput,
    AtualizarObraUseCase,
    CadastrarObraInput,
    CadastrarObraUseCase,
    CancelarObraUseCase,
    ConcluirObraUseCase,
    ExcluirObraUseCase,
    IniciarExecucaoObraUseCase,
    SuspenderObraUseCase,
)
from src.modules.sigmun_obras.domain.entities import SituacaoObra
from src.modules.sigmun_obras.domain.exceptions import (
    ObraComDependenciasError,
    ObraJaExistenteError,
    ObraNaoEncontradaError,
    RegraNegocioError,
)
from tests.unit.obr_fixtures import (
    _medicao,
    _obra,
    _obra_em_execucao,
    repo_despesa,
    repo_medicao,
    repo_obra,
)


def _cadastrar(repo=None):
    return CadastrarObraUseCase(repo or repo_obra()).execute(
        CadastrarObraInput(
            numero="OBR-2026-001",
            nome="Pavimentacao",
            valor_orcado=100_000.0,
            valor_contratado=90_000.0,
        )
    )


class TestCadastroObra:
    def test_cadastra_obra_planejada(self) -> None:
        obra = _cadastrar()
        assert obra.situacao is SituacaoObra.PLANEJADA
        assert obra.percentual_fisico == 0.0

    def test_numero_duplicado_rejeitado(self) -> None:
        """RN-OBR-001: o número da obra é único."""
        with pytest.raises(ObraJaExistenteError):
            _cadastrar(repo_obra(_obra()))

    def test_valor_contratado_acima_do_orcado_rejeitado(self) -> None:
        """RN-OBR-004: o contratado não pode superar o orçado."""
        with pytest.raises(RegraNegocioError):
            CadastrarObraUseCase(repo_obra()).execute(
                CadastrarObraInput(
                    numero="OBR-1", nome="X", valor_orcado=10.0, valor_contratado=20.0
                )
            )

    def test_valor_negativo_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            CadastrarObraUseCase(repo_obra()).execute(
                CadastrarObraInput(numero="OBR-1", nome="X", valor_orcado=-1.0)
            )

    def test_datas_previstas_invertidas_rejeitadas(self) -> None:
        """RN-OBR-003: o início previsto não pode ser posterior ao fim."""
        from datetime import date

        with pytest.raises(RegraNegocioError):
            CadastrarObraUseCase(repo_obra()).execute(
                CadastrarObraInput(
                    numero="OBR-1",
                    nome="X",
                    data_inicio_prevista=date(2026, 12, 1),
                    data_fim_prevista=date(2026, 10, 1),
                )
            )


class TestCicloVidaObra:
    def test_inicia_execucao(self) -> None:
        """RN-OBR-002: CONTRATADA -> EM_EXECUCAO."""
        obra = _obra(SituacaoObra.CONTRATADA)
        resultado = IniciarExecucaoObraUseCase(repo_obra(obra)).execute("obra-1")
        assert resultado.situacao is SituacaoObra.EM_EXECUCAO
        assert resultado.data_inicio_real is not None

    def test_inicia_execucao_sem_empresa_rejeitado(self) -> None:
        """RN-OBR-003: a contratação exige empresa."""
        obra = _obra(SituacaoObra.CONTRATADA)
        obra.empresa_contratada = ""
        with pytest.raises(RegraNegocioError):
            IniciarExecucaoObraUseCase(repo_obra(obra)).execute("obra-1")

    def test_inicia_execucao_de_obra_planejada_rejeitado(self) -> None:
        """RN-OBR-002: obra não contratada não entra em execução."""
        with pytest.raises(RegraNegocioError):
            IniciarExecucaoObraUseCase(repo_obra(_obra())).execute("obra-1")

    def test_suspende_obra_em_execucao(self) -> None:
        resultado = SuspenderObraUseCase(repo_obra(_obra_em_execucao())).execute(
            "obra-1", "licitacao de material"
        )
        assert resultado.situacao is SituacaoObra.SUSPENSA
        assert "licitacao" in resultado.observacao

    def test_conclui_obra_com_100_fisico(self) -> None:
        """RN-OBR-005: a conclusão exige 100% do avanço físico."""
        obra = _obra_em_execucao()
        obra.percentual_fisico = 100.0
        resultado = ConcluirObraUseCase(repo_obra(obra)).execute("obra-1")
        assert resultado.situacao is SituacaoObra.CONCLUIDA
        assert resultado.data_fim_real is not None

    def test_conclui_obra_incompleta_rejeitado(self) -> None:
        """RN-OBR-005: não se conclui obra com avanço parcial."""
        with pytest.raises(RegraNegocioError):
            ConcluirObraUseCase(repo_obra(_obra_em_execucao())).execute("obra-1")

    def test_obra_concluida_nao_retorna_a_execucao(self) -> None:
        """RN-OBR-002: a conclusão é terminal."""
        obra = _obra_em_execucao()
        obra.percentual_fisico = 100.0
        obra.concluir()
        with pytest.raises(RegraNegocioError):
            IniciarExecucaoObraUseCase(repo_obra(obra)).execute("obra-1")

    def test_cancela_obra_planejada(self) -> None:
        assert (
            CancelarObraUseCase(repo_obra(_obra())).execute("obra-1", "reprogramada").situacao
            is SituacaoObra.CANCELADA
        )

    def test_obra_inexistente_no_ciclo(self) -> None:
        with pytest.raises(ObraNaoEncontradaError):
            IniciarExecucaoObraUseCase(repo_obra()).execute("obra-9")


class TestAtualizacaoEExclusaoObra:
    def test_atualiza_obra(self) -> None:
        resultado = AtualizarObraUseCase(repo_obra(_obra())).execute(
            AtualizarObraInput(obra_id="obra-1", nome="Novo nome", bairro="Centro")
        )
        assert resultado.nome == "Novo nome"
        assert resultado.bairro == "Centro"

    def test_atualiza_obra_inexistente(self) -> None:
        with pytest.raises(ObraNaoEncontradaError):
            AtualizarObraUseCase(repo_obra()).execute(
                AtualizarObraInput(obra_id="obra-9", nome="X")
            )

    def test_obra_concluida_nao_aceita_alteracao(self) -> None:
        """RN-OBR-002: obra concluída é terminal."""
        obra = _obra_em_execucao()
        obra.percentual_fisico = 100.0
        obra.concluir()
        with pytest.raises(RegraNegocioError):
            AtualizarObraUseCase(repo_obra(obra)).execute(
                AtualizarObraInput(obra_id="obra-1", nome="X")
            )

    def test_exclui_obra_sem_dependencias(self) -> None:
        resultado = ExcluirObraUseCase(
            repo_obra(_obra()), repo_medicao(), repo_despesa()
        ).execute("obra-1")
        assert resultado.is_deleted is True

    def test_exclui_obra_com_mediacao_rejeitado(self) -> None:
        """RN-OBR-005: obra com medições não pode ser excluída."""
        with pytest.raises(ObraComDependenciasError):
            ExcluirObraUseCase(
                repo_obra(_obra()), repo_medicao(_medicao()), repo_despesa()
            ).execute("obra-1")

    def test_exclui_obra_com_despesa_rejeitado(self) -> None:
        """RN-OBR-006: obra com despesas não pode ser excluída."""
        from tests.unit.obr_fixtures import _despesa

        with pytest.raises(ObraComDependenciasError):
            ExcluirObraUseCase(
                repo_obra(_obra()), repo_medicao(), repo_despesa(_despesa())
            ).execute("obra-1")
