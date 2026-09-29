"""Serviço geoespacial do DOM-GEO — Geoinformação Municipal.

RN-GEO-007: o serviço geoespacial exige URL válida, código único e parâmetros
    de publicação coerentes com o protocolo declarado.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from .tipos import (
    DatumGeografico,
    SituacaoServicoGeo,
    TipoServicoGeo,
    validar_zoom,
)


@dataclass
class ServicoGeo:
    """Serviço de publicação/consumo de dados geoespaciais (WMS, WFS, XYZ)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoServicoGeo = field(default=TipoServicoGeo.WMS)
    situacao: SituacaoServicoGeo = field(default=SituacaoServicoGeo.ATIVO)
    url: str = ""
    camada: str = ""
    datum: DatumGeografico = field(default=DatumGeografico.SIRGAS2000)
    srid: int = 4326
    zoom_minimo: int = 0
    zoom_maximo: int = 24
    publico: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    def ativar(self, autor_id: str = "") -> None:
        """Ativa o serviço geoespacial."""
        self.situacao = SituacaoServicoGeo.ATIVO
        self.updated_at = datetime.utcnow()

    def inativar(self, autor_id: str = "") -> None:
        """Inativa o serviço geoespacial."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoServicoGeo.INATIVO:
            raise RegraNegocioError("Serviço geoespacial já está inativo (RN-GEO-007)")
        self.situacao = SituacaoServicoGeo.INATIVO
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca o serviço como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais do serviço (RN-GEO-007)."""
        from ..exceptions import RegraNegocioError

        if not self.codigo:
            raise RegraNegocioError("Código do serviço geoespacial é obrigatório (RN-GEO-007)")
        if not self.nome:
            raise RegraNegocioError("Nome do serviço geoespacial é obrigatório (RN-GEO-007)")

        if self.situacao == SituacaoServicoGeo.ATIVO:
            url = self.url.strip()
            if not url:
                raise RegraNegocioError(
                    "Serviço geoespacial ativo exige URL de acesso (RN-GEO-007)"
                )
            if not url.startswith(("http://", "https://")):
                raise RegraNegocioError(
                    "URL do serviço geoespacial deve iniciar com http:// ou https:// "
                    "(RN-GEO-007)"
                )
            if self.tipo in (TipoServicoGeo.WMS, TipoServicoGeo.WFS) and not self.camada.strip():
                raise RegraNegocioError(
                    f"Serviço {self.tipo.value.upper()} exige o nome da camada publicada "
                    "(RN-GEO-007)"
                )

        validar_zoom(self.zoom_minimo, "Zoom mínimo do serviço")
        validar_zoom(self.zoom_maximo, "Zoom máximo do serviço")
        if self.zoom_minimo > self.zoom_maximo:
            raise RegraNegocioError(
                "Zoom mínimo não pode ser maior que o zoom máximo do serviço (RN-GEO-005)"
            )
        if not 2000 <= self.srid <= 99999:
            raise RegraNegocioError("SRID inválido para o serviço geoespacial (RN-GEO-007)")


__all__ = ["ServicoGeo"]
