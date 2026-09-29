"""Use cases do DOM-TEL — Gestão Territorial (parte 4: georreferenciamento)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..domain.entities import DatumGeorreferencia, Georreferencia, TipoGeometria
from . import interfaces as ports


def _geometria(valor: str) -> TipoGeometria:
    """Converte o tipo de geometria textual, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoGeometria(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de geometria inválido: {valor}") from exc


def _datum(valor: str) -> DatumGeorreferencia:
    """Converte o datum textual, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return DatumGeorreferencia(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Datum geodésico inválido: {valor}") from exc


@dataclass
class RegistrarGeorreferenciaInput:
    """DTO de registro de georreferência territorial (RN-TEL-005)."""

    bairro_id: str = ""
    logradouro_id: str = ""
    geometria: str = "ponto"
    latitude: float = 0.0
    longitude: float = 0.0
    altitude_m: float | None = None
    vertices: list[dict[str, float]] | None = None
    datum: str = "sirgas2000"
    precisao_m: float = 0.0
    data_levantamento: date | None = None
    autor_id: str = ""


class RegistrarGeorreferenciaUseCase:
    """Registra a georreferência de um bairro ou logradouro (RN-TEL-005)."""

    def __init__(
        self,
        repo: ports.RepositorioGeorreferencia,
        bairros: ports.RepositorioBairro,
        logradouros: ports.RepositorioLogradouro,
    ) -> None:
        self._repo = repo
        self._bairros = bairros
        self._logradouros = logradouros

    def execute(self, dto: RegistrarGeorreferenciaInput) -> Georreferencia:
        """Executa o registro da georreferência."""
        from ..domain.exceptions import BairroNaoEncontradoError, LogradouroNaoEncontradoError

        if dto.bairro_id and dto.logradouro_id:
            from ..domain.exceptions import RegraNegocioError

            raise RegraNegocioError(
                "Georreferência deve estar vinculada a um bairro OU a um logradouro, "
                "não a ambos (RN-TEL-005)"
            )
        if dto.bairro_id and self._bairros.get_by_id(dto.bairro_id) is None:
            raise BairroNaoEncontradoError("Bairro não encontrado para a georreferência")
        if dto.logradouro_id and self._logradouros.get_by_id(dto.logradouro_id) is None:
            raise LogradouroNaoEncontradoError(
                "Logradouro não encontrado para a georreferência"
            )

        geometria = _geometria(dto.geometria)
        vertices = list(dto.vertices) if dto.vertices else []
        # Ponto com vértices informados adota o primeiro vértice como coordenada
        # principal, evitando divergência entre a coordenada e a geometria.
        primeiro = vertices[0] if geometria is TipoGeometria.PONTO and vertices else None
        latitude = float(primeiro["latitude"]) if primeiro else dto.latitude
        longitude = float(primeiro["longitude"]) if primeiro else dto.longitude

        georreferencia = Georreferencia(
            bairro_id=dto.bairro_id,
            logradouro_id=dto.logradouro_id,
            geometria=geometria,
            latitude=latitude,
            longitude=longitude,
            altitude_m=dto.altitude_m,
            vertices=vertices,
            datum=_datum(dto.datum),
            precisao_m=dto.precisao_m,
            data_levantamento=dto.data_levantamento or date.today(),
            created_by=dto.autor_id,
        )
        georreferencia.validar()
        return self._repo.save(georreferencia)


class ExcluirGeorreferenciaUseCase:
    """Exclui (soft-delete) uma georreferência territorial."""

    def __init__(self, repo: ports.RepositorioGeorreferencia) -> None:
        self._repo = repo

    def execute(self, georreferencia_id: str) -> Georreferencia:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import GeorreferenciaNaoEncontradaError

        georreferencia = self._repo.get_by_id(georreferencia_id)
        if georreferencia is None:
            raise GeorreferenciaNaoEncontradaError("Georreferência não encontrada para exclusão")
        georreferencia.excluir()
        return self._repo.save(georreferencia)
