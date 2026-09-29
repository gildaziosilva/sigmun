"""Testes de casos de uso do DOM-GEO — mapas SIG e composição (RN-GEO-002/004/005)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_geoinformacao.application.use_cases import (
    ArquivarMapaUseCase,
    AtualizarMapaInput,
    AtualizarMapaUseCase,
    CadastrarMapaInput,
    CadastrarMapaUseCase,
    ComporCamadaInput,
    ComporCamadaUseCase,
    ExcluirMapaUseCase,
    PublicarMapaUseCase,
    RemoverComposicaoUseCase,
)
from src.modules.sigmun_geoinformacao.domain.entities import (
    MapaSig,
    SituacaoCamadaMapa,
    SituacaoMapaSig,
)
from src.modules.sigmun_geoinformacao.domain.exceptions import (
    CamadaMapaNaoEncontradaError,
    MapaNaoEditavelError,
    MapaSemCamadasError,
    MapaSigJaExistenteError,
    MapaSigNaoEncontradoError,
    RegraNegocioError,
)
from tests.unit.geo_fixtures import (
    _camada_ativa,
    _mapa,
    _vinculo,
    repo_camada,
    repo_mapa,
    repo_vinculo,
)


def _mapa_cadastrado(situacao=SituacaoMapaSig.RASCUNHO, mapa_id="mapa-1"):
    mapa = _mapa(situacao=situacao)
    mapa.id = mapa_id
    return mapa


def _camada_cadastrada(ativa=True, camada_id="camada-1"):
    camada = _camada_ativa() if ativa else _camada_ativa()
    if not ativa:
        camada.situacao = SituacaoCamadaMapa.RASCUNHO
    camada.id = camada_id
    return camada


class TestCadastroMapa:
    def test_cadastra_mapa_em_rascunho(self) -> None:
        mapa = CadastrarMapaUseCase(repo_mapa()).execute(
            CadastrarMapaInput(codigo="MAP-01", nome="Uso do solo")
        )
        assert mapa.situacao is SituacaoMapaSig.RASCUNHO

    def test_codigo_duplicado_rejeitado(self) -> None:
        """RN-GEO-002: o código do mapa é único."""
        with pytest.raises(MapaSigJaExistenteError):
            CadastrarMapaUseCase(repo_mapa(_mapa())).execute(
                CadastrarMapaInput(codigo="MAP-01", nome="X")
            )

    def test_zoom_inicial_fora_dos_limites_rejeitado(self) -> None:
        """RN-GEO-005: zoom inicial entre o mínimo e o máximo."""
        with pytest.raises(RegraNegocioError):
            CadastrarMapaUseCase(repo_mapa()).execute(
                CadastrarMapaInput(
                    codigo="MAP-9", nome="X", zoom_minimo=10, zoom_inicial=5, zoom_maximo=20
                )
            )

    def test_extensao_invertida_rejeitada(self) -> None:
        """RN-GEO-005: latitude mínima não supera a máxima."""
        with pytest.raises(RegraNegocioError):
            CadastrarMapaUseCase(repo_mapa()).execute(
                CadastrarMapaInput(
                    codigo="MAP-9",
                    nome="X",
                    lat_min=-10.0,
                    lat_max=-15.0,
                    lon_min=-39.0,
                    lon_max=-40.0,
                )
            )


class TestComposicao:
    def test_compõe_camada_ativa(self) -> None:
        vinculo = ComporCamadaUseCase(
            repo_vinculo(), repo_mapa(_mapa_cadastrado()), repo_camada(_camada_cadastrada())
        ).execute(ComporCamadaInput(mapa_id="mapa-1", camada_id="camada-1"))
        assert vinculo.camada_id == "camada-1"

    def test_compõe_camada_inexistente(self) -> None:
        with pytest.raises(CamadaMapaNaoEncontradaError):
            ComporCamadaUseCase(
                repo_vinculo(), repo_mapa(_mapa_cadastrado()), repo_camada()
            ).execute(ComporCamadaInput(mapa_id="mapa-1", camada_id="camada-9"))

    def test_camada_rascunho_nao_compoe_mapa(self) -> None:
        """RN-GEO-006: só camada ativa entra na composição."""
        with pytest.raises(RegraNegocioError):
            ComporCamadaUseCase(
                repo_vinculo(),
                repo_mapa(_mapa_cadastrado()),
                repo_camada(_camada_cadastrada(ativa=False)),
            ).execute(ComporCamadaInput(mapa_id="mapa-1", camada_id="camada-1"))

    def test_mapa_publicado_nao_aceita_nova_composicao(self) -> None:
        """RN-GEO-004: a composição publicada é congelada."""
        with pytest.raises(MapaNaoEditavelError):
            ComporCamadaUseCase(
                repo_vinculo(),
                repo_mapa(_mapa_cadastrado(SituacaoMapaSig.PUBLICADO)),
                repo_camada(_camada_cadastrada()),
            ).execute(ComporCamadaInput(mapa_id="mapa-1", camada_id="camada-1"))

    def test_opacidade_fora_de_faixa_rejeitada(self) -> None:
        """RN-GEO-004: opacidade entre 0 e 100."""
        with pytest.raises(RegraNegocioError):
            ComporCamadaUseCase(
                repo_vinculo(), repo_mapa(_mapa_cadastrado()), repo_camada(_camada_cadastrada())
            ).execute(
                ComporCamadaInput(mapa_id="mapa-1", camada_id="camada-1", opacidade=150.0)
            )

    def test_remove_composicao_de_mapa_rascunho(self) -> None:
        vinculo = _vinculo()
        vinculo.id = "vinc-1"
        resultado = RemoverComposicaoUseCase(
            repo_vinculo(vinculo), repo_mapa(_mapa_cadastrado())
        ).execute("vinc-1")
        assert resultado.id == "vinc-1"

    def test_remove_composicao_de_mapa_publicado_rejeitado(self) -> None:
        vinculo = _vinculo()
        vinculo.id = "vinc-1"
        with pytest.raises(MapaNaoEditavelError):
            RemoverComposicaoUseCase(
                repo_vinculo(vinculo),
                repo_mapa(_mapa_cadastrado(SituacaoMapaSig.PUBLICADO)),
            ).execute("vinc-1")


class TestPublicacaoMapa:
    def test_publica_mapa_com_camada_ativa(self) -> None:
        mapa = _mapa_cadastrado()
        resultado = PublicarMapaUseCase(
            repo_mapa(mapa), repo_vinculo(_vinculo()), repo_camada(_camada_cadastrada())
        ).execute("mapa-1")
        assert resultado.situacao is SituacaoMapaSig.PUBLICADO
        assert resultado.publicado_em is not None

    def test_publica_mapa_sem_camadas_rejeitado(self) -> None:
        """RN-GEO-004: a publicação exige ao menos uma camada ativa."""
        with pytest.raises(MapaSemCamadasError):
            PublicarMapaUseCase(
                repo_mapa(_mapa_cadastrado()), repo_vinculo(), repo_camada(_camada_cadastrada())
            ).execute("mapa-1")

    def test_publica_mapa_com_camada_rascunho_rejeitado(self) -> None:
        """RN-GEO-004/RN-GEO-006: toda camada da composição deve estar ativa."""
        with pytest.raises(MapaSemCamadasError):
            PublicarMapaUseCase(
                repo_mapa(_mapa_cadastrado()),
                repo_vinculo(_vinculo()),
                repo_camada(_camada_cadastrada(ativa=False)),
            ).execute("mapa-1")

    def test_publica_mapa_inexistente(self) -> None:
        with pytest.raises(MapaSigNaoEncontradoError):
            PublicarMapaUseCase(
                repo_mapa(), repo_vinculo(_vinculo()), repo_camada(_camada_cadastrada())
            ).execute("mapa-9")

    def test_arquiva_mapa_publicado(self) -> None:
        """RN-GEO-004: PUBLICADO -> ARQUIVADO."""
        mapa = _mapa_cadastrado(SituacaoMapaSig.PUBLICADO)
        resultado = ArquivarMapaUseCase(repo_mapa(mapa)).execute("mapa-1")
        assert resultado.situacao is SituacaoMapaSig.ARQUIVADO

    def test_arquiva_mapa_rascunho_rejeitado(self) -> None:
        """RN-GEO-004: só mapa publicado é arquivado."""
        with pytest.raises(RegraNegocioError):
            ArquivarMapaUseCase(repo_mapa(_mapa_cadastrado())).execute("mapa-1")

    def test_arquivado_nao_e_publicado_novamente(self) -> None:
        """RN-GEO-004: ARQUIVADO é terminal."""
        mapa = _mapa_cadastrado(SituacaoMapaSig.ARQUIVADO)
        mapa.publicar = MapaSig.publicar.__get__(mapa)  # noqa: SLF001
        with pytest.raises(RegraNegocioError):
            mapa.publicar()


class TestAtualizacaoEExclusaoMapa:
    def test_atualiza_mapa(self) -> None:
        resultado = AtualizarMapaUseCase(repo_mapa(_mapa_cadastrado())).execute(
            AtualizarMapaInput(mapa_id="mapa-1", nome="Novo nome")
        )
        assert resultado.nome == "Novo nome"

    def test_atualiza_mapa_inexistente(self) -> None:
        with pytest.raises(MapaSigNaoEncontradoError):
            AtualizarMapaUseCase(repo_mapa()).execute(
                AtualizarMapaInput(mapa_id="mapa-9", nome="X")
            )

    def test_codigo_de_mapa_publicado_e_imutavel(self) -> None:
        """RN-GEO-004: após a publicação o código identifica o mapa publicado."""
        with pytest.raises(MapaNaoEditavelError):
            AtualizarMapaUseCase(
                repo_mapa(_mapa_cadastrado(SituacaoMapaSig.PUBLICADO))
            ).execute(AtualizarMapaInput(mapa_id="mapa-1", codigo="MAP-NOVO"))

    def test_exclui_mapa_rascunho(self) -> None:
        resultado = ExcluirMapaUseCase(repo_mapa(_mapa_cadastrado()), repo_vinculo()).execute(
            "mapa-1"
        )
        assert resultado.is_deleted is True

    def test_exclui_mapa_publicado_rejeitado(self) -> None:
        """RN-GEO-004: mapa publicado deve ser arquivado antes da exclusão."""
        with pytest.raises(MapaNaoEditavelError):
            ExcluirMapaUseCase(
                repo_mapa(_mapa_cadastrado(SituacaoMapaSig.PUBLICADO)), repo_vinculo()
            ).execute("mapa-1")
