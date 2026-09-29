"""Vínculo de composição entre mapa SIG e camada de mapa (DOM-GEO).

RN-GEO-004: um mapa publicado não aceita nova camada na composição; a
    publicação do mapa exige ao menos uma camada ativa vinculada.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class MapaCamada:
    """Camada composta por um mapa SIG, com ordem e opacidade de exibição."""

    id: str = field(default_factory=lambda: str(uuid4()))
    mapa_id: str = ""
    camada_id: str = ""
    ordem: int = 0
    opacidade: float = 100.0
    visivel: bool = True
    rotulo: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    created_by: str = ""
    is_deleted: bool = False

    def validar(self) -> None:
        """Valida a composição do mapa (RN-GEO-004)."""
        from ..exceptions import RegraNegocioError

        if not self.mapa_id:
            raise RegraNegocioError("Mapa é obrigatório na composição (RN-GEO-004)")
        if not self.camada_id:
            raise RegraNegocioError("Camada é obrigatória na composição (RN-GEO-004)")
        if self.ordem < 0:
            raise RegraNegocioError("Ordem da camada no mapa não pode ser negativa")
        if not 0.0 <= self.opacidade <= 100.0:
            raise RegraNegocioError(
                "Opacidade da camada deve estar entre 0 e 100 (RN-GEO-004)"
            )


__all__ = ["MapaCamada"]
