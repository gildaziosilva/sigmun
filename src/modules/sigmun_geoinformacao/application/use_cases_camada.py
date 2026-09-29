"""Casos de uso do DOM-GEO — camadas de mapa (RN-GEO-001, RN-GEO-006)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from ..domain.entities import CamadaMapa
from . import interfaces as ports
from .conversores import (
    datum,
    formato_camada,
    tipo_camada,
)


@dataclass
class CadastrarCamadaInput:
    """DTO de cadastro de camada de mapa (RN-GEO-001)."""

    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: str = "outro"
    formato: str = "geojson"
    fonte: str = ""
    data_atualizacao: date | None = None
    datum: str = "sirgas2000"
    srid: int = 4326
    url_servico: str = ""
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    ativar: bool = False
    autor_id: str = ""


class CadastrarCamadaUseCase:
    """Cadastra uma camada de mapa no geoportal (RN-GEO-001)."""

    def __init__(self, repo: ports.RepositorioCamadaMapa) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarCamadaInput) -> CamadaMapa:
        """Executa o cadastro."""
        from ..domain.exceptions import CamadaMapaJaExistenteError

        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise CamadaMapaJaExistenteError("Código de camada já cadastrado (RN-GEO-001)")

        camada = CamadaMapa(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            tipo=tipo_camada(dto.tipo),
            formato=formato_camada(dto.formato),
            fonte=dto.fonte,
            data_atualizacao=dto.data_atualizacao or date.today(),
            datum=datum(dto.datum),
            srid=dto.srid,
            url_servico=dto.url_servico,
            zoom_minimo=dto.zoom_minimo,
            zoom_maximo=dto.zoom_maximo,
            created_by=dto.autor_id,
        )
        if dto.ativar:
            camada.ativar(dto.autor_id)
        camada.validar()
        return self._repo.save(camada)


@dataclass
class AtualizarCamadaInput:
    """DTO de atualização de camada de mapa (todos os campos opcionais)."""

    camada_id: str = ""
    codigo: str | None = None
    nome: str | None = None
    descricao: str | None = None
    tipo: str | None = None
    formato: str | None = None
    fonte: str | None = None
    data_atualizacao: date | None = None
    datum: str | None = None
    srid: int | None = None
    url_servico: str | None = None
    zoom_minimo: int | None = None
    zoom_maximo: int | None = None
    visivel: bool | None = None
    autor_id: str = ""


class AtualizarCamadaUseCase:
    """Atualiza o cadastro de uma camada de mapa."""

    def __init__(self, repo: ports.RepositorioCamadaMapa) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarCamadaInput) -> CamadaMapa:
        """Executa a atualização."""
        from ..domain.exceptions import CamadaMapaNaoEncontradaError, RegraNegocioError

        camada = self._repo.get_by_id(dto.camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError("Camada de mapa não encontrada para atualização")

        if dto.codigo is not None and dto.codigo != camada.codigo:
            outra = self._repo.get_by_codigo(dto.codigo)
            if outra is not None and outra.id != camada.id:
                raise RegraNegocioError("Código de camada já cadastrado (RN-GEO-001)")
            camada.codigo = dto.codigo
        if dto.nome is not None:
            camada.nome = dto.nome
        if dto.descricao is not None:
            camada.descricao = dto.descricao
        if dto.tipo is not None:
            camada.tipo = tipo_camada(dto.tipo)
        if dto.formato is not None:
            camada.formato = formato_camada(dto.formato)
        if dto.fonte is not None:
            camada.fonte = dto.fonte
        if dto.data_atualizacao is not None:
            camada.data_atualizacao = dto.data_atualizacao
        if dto.datum is not None:
            camada.datum = datum(dto.datum)
        if dto.srid is not None:
            camada.srid = dto.srid
        if dto.url_servico is not None:
            camada.url_servico = dto.url_servico
        if dto.zoom_minimo is not None:
            camada.zoom_minimo = dto.zoom_minimo
        if dto.zoom_maximo is not None:
            camada.zoom_maximo = dto.zoom_maximo
        if dto.visivel is not None:
            camada.visivel = dto.visivel

        camada.updated_at = datetime.utcnow()
        camada.validar()
        return self._repo.save(camada)


class AtivarCamadaUseCase:
    """Ativa uma camada de mapa para publicação (RN-GEO-006)."""

    def __init__(self, repo: ports.RepositorioCamadaMapa) -> None:
        self._repo = repo

    def execute(self, camada_id: str, autor_id: str = "") -> CamadaMapa:
        """Executa a ativação."""
        from ..domain.exceptions import CamadaMapaNaoEncontradaError

        camada = self._repo.get_by_id(camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError("Camada de mapa não encontrada para ativação")
        camada.ativar(autor_id)
        camada.validar()
        return self._repo.save(camada)


class DesativarCamadaUseCase:
    """Desativa uma camada de mapa (RN-GEO-006)."""

    def __init__(self, repo: ports.RepositorioCamadaMapa) -> None:
        self._repo = repo

    def execute(self, camada_id: str, autor_id: str = "") -> CamadaMapa:
        """Executa a desativação."""
        from ..domain.exceptions import CamadaMapaNaoEncontradaError

        camada = self._repo.get_by_id(camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError("Camada de mapa não encontrada para desativação")
        camada.desativar(autor_id)
        return self._repo.save(camada)


class ExcluirCamadaUseCase:
    """Exclui (soft-delete) uma camada de mapa (RN-GEO-006).

    Uma camada que compõe um mapa publicado não pode ser excluída: a composição
    publicada é parte do produto cartográfico entregue ao cidadão (RN-GEO-004).
    """

    def __init__(
        self,
        repo: ports.RepositorioCamadaMapa,
        vinculos: ports.RepositorioMapaCamada,
        mapas: ports.RepositorioMapaSig,
    ) -> None:
        self._repo = repo
        self._vinculos = vinculos
        self._mapas = mapas

    def execute(self, camada_id: str) -> CamadaMapa:
        """Executa a exclusão lógica."""
        from ..domain.entities import SituacaoMapaSig
        from ..domain.exceptions import (
            CamadaMapaNaoEncontradaError,
            MapaComCamadasError,
        )

        camada = self._repo.get_by_id(camada_id)
        if camada is None:
            raise CamadaMapaNaoEncontradaError("Camada de mapa não encontrada para exclusão")

        for vinculo in self._vinculos.list_by_camada(camada_id):
            mapa = self._mapas.get_by_id(vinculo.mapa_id)
            if mapa is not None and mapa.situacao == SituacaoMapaSig.PUBLICADO:
                raise MapaComCamadasError(
                    f"Camada compõe o mapa publicado '{mapa.nome}' e não pode ser "
                    "excluída (RN-GEO-004)"
                )

        camada.excluir()
        return self._repo.save(camada)


__all__ = [
    "CadastrarCamadaInput",
    "CadastrarCamadaUseCase",
    "AtualizarCamadaInput",
    "AtualizarCamadaUseCase",
    "AtivarCamadaUseCase",
    "DesativarCamadaUseCase",
    "ExcluirCamadaUseCase",
]
