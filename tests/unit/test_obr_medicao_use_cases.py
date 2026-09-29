"""Testes de casos de uso do DOM-OBR — medições e despesas (RN-OBR-005, RN-OBR-006)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_obras.application.use_cases import (
    AprovarMedicaoUseCase,
    CancelarMedicaoUseCase,
    ExcluirDespesaUseCase,
    GlosarMedicaoUseCase,
    RegistrarDespesaInput,
    RegistrarDespesaUseCase,
    RegistrarMedicaoInput,
    RegistrarMedicaoUseCase,
)
from src.modules.sigmun_obras.domain.entities import SituacaoMedicao
from src.modules.sigmun_obras.domain.exceptions import (
    MedicaoJaRegistradaError,
    MedicaoNaoEncontradaError,
    ObraNaoEncontradaError,
    RegraNegocioError,
)
from tests.unit.obr_fixtures import (
    _despesa,
    _medicao,
    _obra,
    _obra_em_execucao,
    repo_despesa,
    repo_medicao,
    repo_obra,
)


def _registrar(obra=None, medicoes=None, despesas=None, **kwargs):
    dto = {
        "obra_id": "obra-1",
        "numero": "MED-01",
        "percentual_fisico": 30.0,
        "valor_medido": 27_000.0,
        "responsavel_tecnico": "Eng. Responsavel",
    }
    dto.update(kwargs)
    return RegistrarMedicaoUseCase(
        repo_medicao(*(medicoes or ())),
        repo_obra(obra or _obra_em_execucao()),
        repo_despesa(*(despesas or ())),
    ).execute(RegistrarMedicaoInput(**dto))


class TestRegistroMedicao:
    def test_registra_medicao_em_obra_em_execucao(self) -> None:
        medicao = _registrar()
        assert medicao.situacao is SituacaoMedicao.REGISTRADA
        assert medicao.valor_medido == 27_000.0

    def test_registra_medicao_em_obra_planejada_rejeitado(self) -> None:
        """RN-OBR-005: só obra em execução aceita medição."""
        with pytest.raises(RegraNegocioError):
            _registrar(obra=_obra())

    def test_obra_inexistente_rejeitada(self) -> None:
        with pytest.raises(ObraNaoEncontradaError):
            RegistrarMedicaoUseCase(
                repo_medicao(), repo_obra(), repo_despesa()
            ).execute(
                RegistrarMedicaoInput(
                    obra_id="obra-9", numero="MED-1", responsavel_tecnico="Eng."
                )
            )

    def test_numero_de_medicao_duplicado_rejeitado(self) -> None:
        """RN-OBR-005: número de medição é único por obra."""
        with pytest.raises(MedicaoJaRegistradaError):
            _registrar(medicoes=(_medicao(),))

    def test_valor_acima_do_contratado_rejeitado(self) -> None:
        """RN-OBR-005: não se mede acima do valor contratado."""
        with pytest.raises(RegraNegocioError):
            _registrar(valor_medido=999_999.0)

    def test_percentual_acima_de_100_rejeitado(self) -> None:
        """RN-OBR-005: percentual físico entre 0 e 100."""
        with pytest.raises(RegraNegocioError):
            _registrar(percentual_fisico=150.0)

    def test_responsavel_tecnico_obrigatorio(self) -> None:
        with pytest.raises(RegraNegocioError):
            _registrar(responsavel_tecnico="")


class TestCicloMedicao:
    def test_aprova_medicao_e_recompoe_avanco_da_obra(self) -> None:
        """RN-OBR-005: a aprovação compõe o avanço físico-financeiro."""
        medicao = _medicao(percentual=30.0, valor=27_000.0)
        medicao.id = "med-1"
        obra = _obra_em_execucao()
        resultado = AprovarMedicaoUseCase(
            repo_medicao(medicao), repo_obra(obra), repo_despesa()
        ).execute("med-1")
        assert resultado.situacao is SituacaoMedicao.APROVADA
        assert obra.valor_mediado == 27_000.0
        assert obra.percentual_fisico == 30.0

    def test_avanco_financeiro_limitado_ao_fisico(self) -> None:
        """RN-OBR-004/006: não se paga mais do que se mediu."""
        medicao = _medicao(percentual=30.0, valor=27_000.0)
        medicao.id = "med-1"
        obra = _obra_em_execucao()
        despesa = _despesa(valor=999_999.0)
        AprovarMedicaoUseCase(
            repo_medicao(medicao), repo_obra(obra), repo_despesa(despesa)
        ).execute("med-1")
        # O total pago é limitado ao avanço físico da obra.
        assert obra.percentual_financeiro <= obra.percentual_fisico

    def test_glosa_medicao_exige_justificativa(self) -> None:
        """RN-OBR-005: glosa sempre motivada."""
        medicao = _medicao()
        medicao.id = "med-1"
        medicao.conferir()
        with pytest.raises(RegraNegocioError):
            GlosarMedicaoUseCase(repo_medicao(medicao)).execute("med-1", "  ")

    def test_glosa_medicao_conferida(self) -> None:
        medicao = _medicao()
        medicao.id = "med-1"
        medicao.conferir()
        resultado = GlosarMedicaoUseCase(repo_medicao(medicao)).execute("med-1", "servico faltante")
        assert resultado.situacao is SituacaoMedicao.GLOSADA

    def test_medicao_aprovada_nao_e_cancelada(self) -> None:
        """RN-OBR-005: medição aprovada exige glosa, não cancelamento."""
        medicao = _medicao(situacao=SituacaoMedicao.APROVADA)
        medicao.id = "med-1"
        with pytest.raises(RegraNegocioError):
            CancelarMedicaoUseCase(repo_medicao(medicao)).execute("med-1")

    def test_medicao_inexistente(self) -> None:
        with pytest.raises(MedicaoNaoEncontradaError):
            AprovarMedicaoUseCase(
                repo_medicao(), repo_obra(_obra_em_execucao()), repo_despesa()
            ).execute("med-9")


class TestDespesas:
    def test_registra_despesa_ate_o_saldo_mediado(self) -> None:
        """RN-OBR-006: a despesa não supera o medido ainda não pago."""
        medicao = _medicao(percentual=30.0, valor=27_000.0, situacao=SituacaoMedicao.APROVADA)
        obra = _obra_em_execucao()
        obra.valor_mediado = 27_000.0
        obra.percentual_fisico = 30.0
        despesa = RegistrarDespesaUseCase(
            repo_despesa(), repo_obra(obra), repo_medicao(medicao)
        ).execute(
            RegistrarDespesaInput(
                obra_id="obra-1", descricao="Repasse medicao 1", valor=10_000.0
            )
        )
        assert despesa.valor == 10_000.0
        assert obra.valor_pago == 10_000.0

    def test_despesa_acima_do_saldo_mediado_rejeitada(self) -> None:
        """RN-OBR-006: não se desembolsa além do medido."""
        obra = _obra_em_execucao()
        obra.valor_mediado = 1_000.0
        with pytest.raises(RegraNegocioError):
            RegistrarDespesaUseCase(
                repo_despesa(), repo_obra(obra), repo_medicao()
            ).execute(
                RegistrarDespesaInput(obra_id="obra-1", descricao="X", valor=50_000.0)
            )

    def test_despesa_sem_saldo_mediado_rejeitada(self) -> None:
        obra = _obra_em_execucao()
        with pytest.raises(RegraNegocioError):
            RegistrarDespesaUseCase(
                repo_despesa(), repo_obra(obra), repo_medicao()
            ).execute(
                RegistrarDespesaInput(obra_id="obra-1", descricao="X", valor=100.0)
            )

    def test_despesa_em_obra_planejada_rejeitada(self) -> None:
        with pytest.raises(RegraNegocioError):
            RegistrarDespesaUseCase(
                repo_despesa(), repo_obra(_obra()), repo_medicao()
            ).execute(
                RegistrarDespesaInput(obra_id="obra-1", descricao="X", valor=100.0)
            )

    def test_exclui_despesa_e_recompoe_avanco(self) -> None:
        despesa = _despesa(valor=5_000.0)
        despesa.id = "desp-1"
        obra = _obra_em_execucao()
        obra.valor_pago = 5_000.0
        resultado = ExcluirDespesaUseCase(
            repo_despesa(despesa), repo_obra(obra), repo_medicao()
        ).execute("desp-1")
        assert resultado.is_deleted is True
        assert obra.valor_pago == 0.0

    def test_exclui_despesa_inexistente(self) -> None:
        from src.modules.sigmun_obras.domain.exceptions import DespesaNaoEncontradaError

        with pytest.raises(DespesaNaoEncontradaError):
            ExcluirDespesaUseCase(
                repo_despesa(), repo_obra(_obra_em_execucao()), repo_medicao()
            ).execute("desp-9")
