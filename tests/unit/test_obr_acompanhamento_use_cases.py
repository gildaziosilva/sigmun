"""Testes de casos de uso do DOM-OBR — etapas e vistorias (RN-OBR-007, RN-OBR-008)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_obras.application.use_cases import (
    AtualizarEtapaUseCase,
    CadastrarEtapaInput,
    CadastrarEtapaUseCase,
    ConcluirEtapaUseCase,
    RegistrarVistoriaInput,
    RegistrarVistoriaUseCase,
)
from src.modules.sigmun_obras.domain.entities import SituacaoEtapa
from src.modules.sigmun_obras.domain.exceptions import (
    EtapaNaoEncontradaError,
    ObraNaoEncontradaError,
    RegraNegocioError,
)
from tests.unit.obr_fixtures import _etapa, _obra_em_execucao, repo_etapa, repo_obra, repo_vistoria


def _etapa_cadastrada(etapa_id: str = "etapa-1"):
    etapa = _etapa()
    etapa.id = etapa_id
    return etapa


class TestEtapas:
    def test_cadastra_etapa(self) -> None:
        """RN-OBR-007: a etapa pertence a uma obra existente."""
        etapa = CadastrarEtapaUseCase(repo_etapa(), repo_obra(_obra_em_execucao())).execute(
            CadastrarEtapaInput(
                obra_id="obra-1",
                numero="ET-01",
                descricao="Estrutura",
                percentual_previsto=40.0,
                responsavel="Eng. Responsavel",
            )
        )
        assert etapa.situacao is SituacaoEtapa.PENDENTE

    def test_cadastra_etapa_em_obra_inexistente(self) -> None:
        with pytest.raises(ObraNaoEncontradaError):
            CadastrarEtapaUseCase(repo_etapa(), repo_obra()).execute(
                CadastrarEtapaInput(
                    obra_id="obra-9",
                    numero="ET-01",
                    descricao="X",
                    responsavel="Eng.",
                )
            )

    def test_responsavel_da_etapa_obrigatorio(self) -> None:
        """RN-OBR-007: toda etapa tem responsável definido."""
        with pytest.raises(RegraNegocioError):
            CadastrarEtapaUseCase(repo_etapa(), repo_obra(_obra_em_execucao())).execute(
                CadastrarEtapaInput(
                    obra_id="obra-1", numero="ET-01", descricao="X", responsavel=""
                )
            )

    def test_etapa_de_peso_parcial_aceita_100_de_conclusao(self) -> None:
        """RN-OBR-007: peso previsto e conclusão são escalas distintas.

        Uma etapa com 40% de peso na obra pode estar 100% concluída.
        """
        etapa = _etapa_cadastrada()  # percentual previsto = 40%
        resultado = AtualizarEtapaUseCase(repo_etapa(etapa)).execute(
            "etapa-1", percentual_realizado=100.0
        )
        assert resultado.percentual_realizado == 100.0
        assert resultado.percentual_previsto == 40.0

    def test_percentual_realizado_fora_de_faixa_rejeitado(self) -> None:
        """RN-OBR-007: a conclusão da etapa fica na faixa 0..100."""
        etapa = _etapa_cadastrada()
        with pytest.raises(RegraNegocioError):
            AtualizarEtapaUseCase(repo_etapa(etapa)).execute(
                "etapa-1", percentual_realizado=150.0
            )

    def test_atualiza_avanco_da_etapa(self) -> None:
        etapa = _etapa_cadastrada()
        resultado = AtualizarEtapaUseCase(repo_etapa(etapa)).execute(
            "etapa-1", percentual_realizado=20.0
        )
        assert resultado.percentual_realizado == 20.0

    def test_atualiza_etapa_inexistente(self) -> None:
        with pytest.raises(EtapaNaoEncontradaError):
            AtualizarEtapaUseCase(repo_etapa()).execute("etapa-9", percentual_realizado=10.0)

    def test_atualiza_etapa_com_situacao_invalida(self) -> None:
        with pytest.raises(RegraNegocioError):
            AtualizarEtapaUseCase(repo_etapa(_etapa_cadastrada())).execute(
                "etapa-1", situacao="inexistente"
            )

    def test_conclui_etapa_com_100_realizado(self) -> None:
        """RN-OBR-007: conclusão exige 100% do previsto."""
        etapa = _etapa_cadastrada()
        etapa.percentual_realizado = 100.0
        resultado = ConcluirEtapaUseCase(repo_etapa(etapa)).execute("etapa-1")
        assert resultado.situacao is SituacaoEtapa.CONCLUIDA

    def test_conclui_etapa_incompleta_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            ConcluirEtapaUseCase(repo_etapa(_etapa_cadastrada())).execute("etapa-1")

    def test_conclui_etapa_inexistente(self) -> None:
        with pytest.raises(EtapaNaoEncontradaError):
            ConcluirEtapaUseCase(repo_etapa()).execute("etapa-9")


class TestVistorias:
    def test_registra_vistoria_periodica(self) -> None:
        """RN-OBR-008: a vistoria registra o avanço verificado em campo."""
        vistoria = RegistrarVistoriaUseCase(
            repo_vistoria(), repo_obra(_obra_em_execucao())
        ).execute(
            RegistrarVistoriaInput(
                obra_id="obra-1",
                tipo="periodica",
                parecer="aprovado_com_ressalvas",
                percentual_fisico_verificado=28.0,
                fiscal="Fiscal Municipal",
            )
        )
        assert vistoria.percentual_fisico_verificado == 28.0
        assert vistoria.aprovada is True

    def test_registra_vistoria_reprovada(self) -> None:
        vistoria = RegistrarVistoriaUseCase(
            repo_vistoria(), repo_obra(_obra_em_execucao())
        ).execute(
            RegistrarVistoriaInput(
                obra_id="obra-1", parecer="reprovado", fiscal="Fiscal Municipal"
            )
        )
        assert vistoria.aprovada is False

    def test_registra_vistoria_em_obra_inexistente(self) -> None:
        with pytest.raises(ObraNaoEncontradaError):
            RegistrarVistoriaUseCase(repo_vistoria(), repo_obra()).execute(
                RegistrarVistoriaInput(obra_id="obra-9", fiscal="Fiscal")
            )

    def test_fiscal_obrigatorio(self) -> None:
        """RN-OBR-008: vistoria exige fiscal responsável."""
        with pytest.raises(RegraNegocioError):
            RegistrarVistoriaUseCase(
                repo_vistoria(), repo_obra(_obra_em_execucao())
            ).execute(RegistrarVistoriaInput(obra_id="obra-1", fiscal=""))

    def test_percentual_verificado_fora_de_faixa_rejeitado(self) -> None:
        with pytest.raises(RegraNegocioError):
            RegistrarVistoriaUseCase(
                repo_vistoria(), repo_obra(_obra_em_execucao())
            ).execute(
                RegistrarVistoriaInput(
                    obra_id="obra-1", fiscal="Fiscal", percentual_fisico_verificado=120.0
                )
            )
