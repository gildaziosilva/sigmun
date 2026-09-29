"""Camada de mapa do DOM-GEO — Geoinformação Municipal.

RN-GEO-001: o código da camada é único no geoportal municipal.
RN-GEO-006: a camada de mapa obedece ao ciclo RASCUNHO -> ATIVA ->
    DESATIVADA, sem retorno a partir de DESATIVADA; camadas ATIVA exigem
    datum, formato e, quando o formato é de serviço, a URL correspondente.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import (
    FORMATOS_REQUEREM_URL,
    DatumGeografico,
    FormatoCamada,
    SituacaoCamadaMapa,
    TipoCamadaMapa,
    validar_zoom,
)


@dataclass
class CamadaMapa:
    """Camada cartográfica disponibilizada no geoportal municipal."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoCamadaMapa = field(default=TipoCamadaMapa.OUTRO)
    formato: FormatoCamada = field(default=FormatoCamada.GEOJSON)
    fonte: str = ""
    data_atualizacao: date = field(default_factory=date.today)
    datum: DatumGeografico = field(default=DatumGeografico.SIRGAS2000)
    srid: int = 4326
    url_servico: str = ""
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    visivel: bool = True
    situacao: SituacaoCamadaMapa = field(default=SituacaoCamadaMapa.RASCUNHO)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def exige_url(self) -> bool:
        """Indica se o formato da camada exige URL de serviço (RN-GEO-006)."""
        return self.formato in FORMATOS_REQUEREM_URL

    def ativar(self, autor_id: str = "") -> None:
        """Ativa a camada para publicação no geoportal (RN-GEO-006)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoCamadaMapa.DESATIVADA:
            raise RegraNegocioError(
                "Camada desativada não pode ser reativada; crie nova camada (RN-GEO-006)"
            )
        self.situacao = SituacaoCamadaMapa.ATIVA
        self.updated_at = datetime.utcnow()

    def desativar(self, autor_id: str = "") -> None:
        """Desativa a camada, retire-a do geoportal (RN-GEO-006)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoCamadaMapa.DESATIVADA:
            raise RegraNegocioError("Camada já está desativada (RN-GEO-006)")
        self.situacao = SituacaoCamadaMapa.DESATIVADA
        self.visivel = False
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a camada como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da camada (RN-GEO-001, RN-GEO-006)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Código da camada é obrigatório (RN-GEO-001)")
        if not self.nome:
            raise RegraNegocioError("Nome da camada é obrigatório (RN-GEO-001)")

        validar_zoom(self.zoom_minimo, "Zoom mínimo da camada")
        validar_zoom(self.zoom_maximo, "Zoom máximo da camada")
        if self.zoom_minimo > self.zoom_maximo:
            raise RegraNegocioError(
                "Zoom mínimo não pode ser maior que o zoom máximo da camada (RN-GEO-005)"
            )

        if self.situacao != SituacaoCamadaMapa.ATIVA:
            return

        # Validações aplicáveis apenas às camadas publicadas (RN-GEO-006).
        if self.exige_url and not self.url_servico.strip():
            raise RegraNegocioError(
                f"Camada no formato {self.formato.value} exige URL de serviço (RN-GEO-006)"
            )
        if not 2000 <= self.srid <= 99999:
            raise RegraNegocioError("SRID inválido para a camada (RN-GEO-006)")


__all__ = ["CamadaMapa"]
