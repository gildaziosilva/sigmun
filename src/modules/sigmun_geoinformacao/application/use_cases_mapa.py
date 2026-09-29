"""Casos de uso do DOM-GEO — mapas SIG e composição de camadas.

RN-GEO-002: código do mapa único no geoportal.
RN-GEO-004: mapa em RASCUNHO aceita composição de camadas; PUBLICADO exige ao
    menos uma camada ativa e não aceita nova camada; ARQUIVADO é terminal.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..domain.entities import MapaCamada, MapaSig
from . import interfaces as ports
from .conversores import (
    datum,
    tipo_mapa,
)


@dataclass
class CadastrarMapaInput:
    """DTO de cadastro de mapa SIG (RN-GEO-002)."""

    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: str = "tematico"
    datum: str = "sirgas2000"
    srid: int = 4326
    escala_denominador: int = 0
    zoom_inicial: int = 13
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    lat_min: float | None = None
    lon_min: float | None = None
    lat_max: float | None = None
    lon_max: float | None = None
    autor_id: str = ""


class CadastrarMapaUseCase:
    """Cadastra um mapa SIG em rascunho (RN-GEO-002)."""

    def __init__(self, repo: ports.RepositorioMapaSig) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarMapaInput) -> MapaSig:
        """Executa o cadastro."""
        from ..domain.exceptions import MapaSigJaExistenteError

        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise MapaSigJaExistenteError("Código de mapa já cadastrado (RN-GEO-002)")

        mapa = MapaSig(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            tipo=tipo_mapa(dto.tipo),
            datum=datum(dto.datum),
            srid=dto.srid,
            escala_denominador=dto.escala_denominador,
            zoom_inicial=dto.zoom_inicial,
            zoom_minimo=dto.zoom_minimo,
            zoom_maximo=dto.zoom_maximo,
            lat_min=dto.lat_min,
            lon_min=dto.lon_min,
            lat_max=dto.lat_max,
            lon_max=dto.lon_max,
            criado_por=dto.autor_id,
            created_by=dto.autor_id,
        )
        mapa.validar()
        return self._repo.save(mapa)


@dataclass
class AtualizarMapaInput:
    """DTO de atualização de mapa SIG (todos os campos opcionais)."""

    mapa_id: str = ""
    codigo: str | None = None
    nome: str | None = None
    descricao: str | None = None
    tipo: str | None = None
    datum: str | None = None
    srid: int | None = None
    escala_denominador: int | None = None
    zoom_inicial: int | None = None
    zoom_minimo: int | None = None
    zoom_maximo: int | None = None
    lat_min: float | None = None
    lon_min: float | None = None
    lat_max: float | None = None
    lon_max: float | None = None
    autor_id: str = ""


class AtualizarMapaUseCase:
    """Atualiza os dados de um mapa SIG em rascunho (RN-GEO-004).

    Mapas publicados ou arquivados têm sua composição congelada; os atributos
    descritivos permanecem editáveis para correção administrativa.
    """

    def __init__(self, repo: ports.RepositorioMapaSig) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarMapaInput) -> MapaSig:
        """Executa a atualização."""
        from ..domain.entities import SituacaoMapaSig
        from ..domain.exceptions import (
            MapaNaoEditavelError,
            MapaSigNaoEncontradoError,
            RegraNegocioError,
        )

        mapa = self._repo.get_by_id(dto.mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa SIG não encontrado para atualização")

        if dto.codigo is not None and dto.codigo != mapa.codigo:
            if mapa.situacao != SituacaoMapaSig.RASCUNHO:
                raise MapaNaoEditavelError(
                    "Código do mapa não pode ser alterado após a publicação (RN-GEO-004)"
                )
            outro = self._repo.get_by_codigo(dto.codigo)
            if outro is not None and outro.id != mapa.id:
                raise RegraNegocioError("Código de mapa já cadastrado (RN-GEO-002)")
            mapa.codigo = dto.codigo

        for campo, valor in (
            ("nome", dto.nome),
            ("descricao", dto.descricao),
            ("escala_denominador", dto.escala_denominador),
            ("zoom_inicial", dto.zoom_inicial),
            ("zoom_minimo", dto.zoom_minimo),
            ("zoom_maximo", dto.zoom_maximo),
            ("lat_min", dto.lat_min),
            ("lon_min", dto.lon_min),
            ("lat_max", dto.lat_max),
            ("lon_max", dto.lon_max),
        ):
            if valor is not None:
                setattr(mapa, campo, valor)
        if dto.tipo is not None:
            mapa.tipo = tipo_mapa(dto.tipo)
        if dto.datum is not None:
            mapa.datum = datum(dto.datum)
        if dto.srid is not None:
            mapa.srid = dto.srid

        mapa.updated_at = datetime.utcnow()
        mapa.validar()
        return self._repo.save(mapa)


@dataclass
class ComporCamadaInput:
    """DTO de composição de camada em um mapa (RN-GEO-004)."""

    mapa_id: str = ""
    camada_id: str = ""
    ordem: int = 0
    opacidade: float = 100.0
    visivel: bool = True
    rotulo: str = ""
    autor_id: str = ""


class ComporCamadaUseCase:
    """Adiciona uma camada à composição de um mapa (RN-GEO-004, RN-GEO-008)."""

    def __init__(
        self,
        repo: ports.RepositorioMapaCamada,
        mapas: ports.RepositorioMapaSig,
        camadas: ports.RepositorioCamadaMapa,
    ) -> None:
        self._repo = repo
        self._mapas = mapas
        self._camadas = camadas

    def execute(self, dto: ComporCamadaInput) -> MapaCamada:
        """Executa a composição."""
        from ..domain.entities import SituacaoCamadaMapa, SituacaoMapaSig
        from ..domain.exceptions import (
            CamadaMapaNaoEncontradaError,
            MapaNaoEditavelError,
            MapaSigNaoEncontradoError,
            RegraNegocioError,
        )

        mapa = self._mapas.get_by_id(dto.mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa não encontrado para composição")
        if mapa.situacao != SituacaoMapaSig.RASCUNHO:
            raise MapaNaoEditavelError(
                "Somente mapa em rascunho aceita composição de camadas (RN-GEO-004)"
            )

        camada = self._camadas.get_by_id(dto.camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError("Camada não encontrada para composição")
        if camada.situacao != SituacaoCamadaMapa.ATIVA:
            raise RegraNegocioError("Somente camada ativa pode compor um mapa (RN-GEO-006)")
        if self._repo.get_by_mapa_camada(dto.mapa_id, dto.camada_id) is not None:
            raise RegraNegocioError("Camada já composta neste mapa (RN-GEO-004)")

        vinculo = MapaCamada(
            mapa_id=dto.mapa_id,
            camada_id=dto.camada_id,
            ordem=dto.ordem,
            opacidade=dto.opacidade,
            visivel=dto.visivel,
            rotulo=dto.rotulo,
            created_by=dto.autor_id,
        )
        vinculo.validar()
        return self._repo.save(vinculo)


class RemoverComposicaoUseCase:
    """Remove uma camada da composição de um mapa (RN-GEO-004)."""

    def __init__(
        self,
        repo: ports.RepositorioMapaCamada,
        mapas: ports.RepositorioMapaSig,
    ) -> None:
        self._repo = repo
        self._mapas = mapas

    def execute(self, vinculo_id: str) -> MapaCamada:
        """Executa a remoção do vínculo."""
        from ..domain.entities import SituacaoMapaSig
        from ..domain.exceptions import (
            MapaNaoEditavelError,
            MapaSigNaoEncontradoError,
            RegraNegocioError,
        )

        vinculo = self._repo.get_by_id(vinculo_id)
        if vinculo is None:
            raise RegraNegocioError("Vínculo de composição não encontrado")

        mapa = self._mapas.get_by_id(vinculo.mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa não encontrado para remoção da composição")
        if mapa.situacao != SituacaoMapaSig.RASCUNHO:
            raise MapaNaoEditavelError(
                "Somente mapa em rascunho aceita alteração de composição (RN-GEO-004)"
            )

        self._repo.delete(vinculo_id)
        return vinculo


class PublicarMapaUseCase:
    """Publica o mapa SIG no geoportal (RN-GEO-004).

    A publicação exige ao menos uma camada ativa na composição, garantindo que
    o mapa publicado tenha conteúdo cartográfico verificável.
    """

    def __init__(
        self,
        repo: ports.RepositorioMapaSig,
        vinculos: ports.RepositorioMapaCamada,
        camadas: ports.RepositorioCamadaMapa,
    ) -> None:
        self._repo = repo
        self._vinculos = vinculos
        self._camadas = camadas

    def execute(self, mapa_id: str, autor_id: str = "") -> MapaSig:
        """Executa a publicação."""
        from ..domain.entities import SituacaoCamadaMapa
        from ..domain.exceptions import MapaSemCamadasError, MapaSigNaoEncontradoError

        mapa = self._repo.get_by_id(mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa SIG não encontrado para publicação")

        vinculos = self._vinculos.list_by_mapa(mapa_id)
        if not vinculos:
            raise MapaSemCamadasError(
                "Mapa não possui camadas na composição; a publicação exige ao menos "
                "uma camada ativa (RN-GEO-004)"
            )
        for vinculo in vinculos:
            camada = self._camadas.get_by_id(vinculo.camada_id)
            if camada is None or camada.situacao != SituacaoCamadaMapa.ATIVA:
                raise MapaSemCamadasError(
                    "Toda camada da composição deve estar ativa para publicar o mapa "
                    "(RN-GEO-004, RN-GEO-006)"
                )

        mapa.publicar(autor_id)
        return self._repo.save(mapa)


class ArquivarMapaUseCase:
    """Arquiva um mapa publicado, retirando-o do geoportal (RN-GEO-004)."""

    def __init__(self, repo: ports.RepositorioMapaSig) -> None:
        self._repo = repo

    def execute(self, mapa_id: str, autor_id: str = "") -> MapaSig:
        """Executa o arquivamento."""
        from ..domain.exceptions import MapaSigNaoEncontradoError

        mapa = self._repo.get_by_id(mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa SIG não encontrado para arquivamento")
        mapa.arquivar(autor_id)
        return self._repo.save(mapa)


class ExcluirMapaUseCase:
    """Exclui (soft-delete) um mapa SIG em rascunho ou arquivado (RN-GEO-004)."""

    def __init__(
        self,
        repo: ports.RepositorioMapaSig,
        vinculos: ports.RepositorioMapaCamada,
    ) -> None:
        self._repo = repo
        self._vinculos = vinculos

    def execute(self, mapa_id: str) -> MapaSig:
        """Executa a exclusão lógica."""
        from ..domain.entities import SituacaoMapaSig
        from ..domain.exceptions import MapaNaoEditavelError, MapaSigNaoEncontradoError

        mapa = self._repo.get_by_id(mapa_id)
        if mapa is None:
            raise MapaSigNaoEncontradoError("Mapa SIG não encontrado para exclusão")
        if mapa.situacao == SituacaoMapaSig.PUBLICADO:
            raise MapaNaoEditavelError(
                "Mapa publicado deve ser arquivado antes da exclusão (RN-GEO-004)"
            )

        for vinculo in self._vinculos.list_by_mapa(mapa_id):
            self._vinculos.delete(vinculo.id)
        mapa.excluir()
        return self._repo.save(mapa)


__all__ = [
    "CadastrarMapaInput",
    "CadastrarMapaUseCase",
    "AtualizarMapaInput",
    "AtualizarMapaUseCase",
    "ComporCamadaInput",
    "ComporCamadaUseCase",
    "RemoverComposicaoUseCase",
    "PublicarMapaUseCase",
    "ArquivarMapaUseCase",
    "ExcluirMapaUseCase",
]
