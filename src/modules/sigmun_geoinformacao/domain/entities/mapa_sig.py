"""Mapa SIG do DOM-GEO — Geoinformação Municipal.

RN-GEO-002: o código do mapa é único no geoportal municipal.
RN-GEO-004: o mapa obedece ao ciclo RASCUNHO -> PUBLICADO -> ARQUIVADO, sem
    retorno a partir de ARQUIVADO; a publicação exige ao menos uma camada
    ativa vinculada e mapas publicados não aceitam nova composição.
RN-GEO-005: a extensão (bbox) e os níveis de zoom do mapa são validados.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import (
    DatumGeografico,
    SituacaoMapaSig,
    TipoMapaSig,
    validar_coordenada,
    validar_zoom,
)


@dataclass
class MapaSig:
    """Mapa temático publicado no geoportal municipal."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoMapaSig = field(default=TipoMapaSig.TEMATICO)
    situacao: SituacaoMapaSig = field(default=SituacaoMapaSig.RASCUNHO)
    datum: DatumGeografico = field(default=DatumGeografico.SIRGAS2000)
    srid: int = 4326
    escala_denominador: int = 0
    zoom_inicial: int = 13
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    lat_min: float | None = None
    lon_min: float | None = None
    lat_max: float | None = None
    lon_max: float | None = None
    publicado_em: datetime | None = None
    criado_por: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def esta_publicado(self) -> bool:
        """Indica se o mapa está publicado no geoportal."""
        return self.situacao == SituacaoMapaSig.PUBLICADO

    def publicar(self, autor_id: str = "") -> None:
        """Publica o mapa no geoportal (RN-GEO-004)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoMapaSig.ARQUIVADO:
            raise RegraNegocioError("Mapa arquivado não pode ser publicado (RN-GEO-004)")
        if self.situacao == SituacaoMapaSig.PUBLICADO:
            raise RegraNegocioError("Mapa já está publicado (RN-GEO-004)")
        self.situacao = SituacaoMapaSig.PUBLICADO
        self.publicado_em = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def arquivar(self, autor_id: str = "") -> None:
        """Arquiva o mapa, retirando-o do geoportal (RN-GEO-004)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoMapaSig.ARQUIVADO:
            raise RegraNegocioError("Mapa já está arquivado (RN-GEO-004)")
        if self.situacao != SituacaoMapaSig.PUBLICADO:
            raise RegraNegocioError("Somente mapa publicado pode ser arquivado (RN-GEO-004)")
        self.situacao = SituacaoMapaSig.ARQUIVADO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o mapa como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do mapa (RN-GEO-002, RN-GEO-005)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Código do mapa é obrigatório (RN-GEO-002)")
        if not self.nome:
            raise RegraNegocioError("Nome do mapa é obrigatório (RN-GEO-002)")

        validar_zoom(self.zoom_minimo, "Zoom mínimo do mapa")
        validar_zoom(self.zoom_maximo, "Zoom máximo do mapa")
        if self.zoom_minimo > self.zoom_maximo:
            raise RegraNegocioError(
                "Zoom mínimo não pode ser maior que o zoom máximo do mapa (RN-GEO-005)"
            )
        if not self.zoom_minimo <= self.zoom_inicial <= self.zoom_maximo:
            raise RegraNegocioError(
                "Zoom inicial deve estar entre o zoom mínimo e o máximo (RN-GEO-005)"
            )
        if self.escala_denominador < 0:
            raise RegraNegocioError("Escala do mapa não pode ser negativa")
        if not 2000 <= self.srid <= 99999:
            raise RegraNegocioError("SRID inválido para o mapa (RN-GEO-005)")

        # A extensão só é validada quando informada por completo.
        if None not in (self.lat_min, self.lon_min, self.lat_max, self.lon_max):
            validar_coordenada(self.lat_min or 0.0, self.lon_min or 0.0, "Canto sudoeste")
            validar_coordenada(self.lat_max or 0.0, self.lon_max or 0.0, "Canto nordeste")
            if (self.lat_min or 0.0) > (self.lat_max or 0.0):
                raise RegraNegocioError(
                    "Latitude mínima não pode ser maior que a máxima (RN-GEO-005)"
                )
            if (self.lon_min or 0.0) > (self.lon_max or 0.0):
                raise RegraNegocioError(
                    "Longitude mínima não pode ser maior que a máxima (RN-GEO-005)"
                )


__all__ = ["MapaSig"]
