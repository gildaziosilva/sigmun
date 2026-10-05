"""Eventos de domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal).

Eventos disparados para integração com outros domínios e auditoria.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class TipoEventoOuv(Enum):
    """Tipos de eventos do domínio ouvidoria."""

    MANIFESTACAO_REGISTRADA = "manifestacao_registrada"
    MANIFESTACAO_ENCAMINHADA = "manifestacao_encaminhada"
    MANIFESTACAO_RESPONDIDA = "manifestacao_respondida"
    MANIFESTACAO_CONCLUIDA = "manifestacao_concluida"
    MANIFESTACAO_ARQUIVADA = "manifestacao_arquivada"
    MANIFESTACAO_CANCELADA = "manifestacao_cancelada"
    DENUNCIA_REGISTRADA = "denuncia_registrada"
    DENUNCIA_ENCAMINHADA_MP = "denuncia_encaminhada_mp"
    DENUNCIA_ENCAMINHADA_PF = "denuncia_encaminhada_pf"
    DENUNCIA_ENCAMINHADA_TCE = "denuncia_encaminhada_tce"
    DENUNCIA_CONCLUIDA = "denuncia_concluida"
    PEDIDO_LAI_REGISTRADO = "pedido_lai_registrado"
    PEDIDO_LAI_CLASSIFICADO_SIGILO = "pedido_lai_classificado_sigilo"
    PEDIDO_LAI_RESPONDIDO = "pedido_lai_respondido"
    PEDIDO_LAI_RECURSO_INTERPOSTO = "pedido_lai_recurso_interposto"
    PEDIDO_LAI_RECURSO_DECIDIDO = "pedido_lai_recurso_decidido"
    PRAZO_VENCENDO = "prazo_vencendo"
    PRAZO_VENCIDO = "prazo_vencido"
    PRAZO_PRORROGADO = "prazo_prorrogado"


@dataclass
class EventoOuvidoria:
    """Evento base do domínio ouvidoria."""

    id: str = field(default_factory=lambda: str(uuid4()))
    tipo: TipoEventoOuv = TipoEventoOuv.MANIFESTACAO_REGISTRADA
    aggregate_id: str = ""  # ID da manifestação/denúncia/pedido LAI
    aggregate_type: str = ""  # manifestacao, denuncia, pedido_lai
    protocolo: str = ""
    dados: dict[str, Any] = field(default_factory=dict)
    usuario_id: str = ""
    occurred_at: datetime = field(default_factory=datetime.utcnow)
    correlation_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "tipo": self.tipo.value,
            "aggregate_id": self.aggregate_id,
            "aggregate_type": self.aggregate_type,
            "protocolo": self.protocolo,
            "dados": self.dados,
            "usuario_id": self.usuario_id,
            "occurred_at": self.occurred_at.isoformat(),
            "correlation_id": self.correlation_id,
        }


@dataclass
class ManifestacaoRegistradaEvento(EventoOuvidoria):
    """Evento: Manifestação registrada."""

    tipo: TipoEventoOuv = TipoEventoOuv.MANIFESTACAO_REGISTRADA
    aggregate_type: str = "manifestacao"


@dataclass
class ManifestacaoRespondidaEvento(EventoOuvidoria):
    """Evento: Manifestação respondida."""

    tipo: TipoEventoOuv = TipoEventoOuv.MANIFESTACAO_RESPONDIDA
    aggregate_type: str = "manifestacao"
    forma_resposta: str = ""


@dataclass
class DenunciaRegistradaEvento(EventoOuvidoria):
    """Evento: Denúncia registrada."""

    tipo: TipoEventoOuv = TipoEventoOuv.DENUNCIA_REGISTRADA
    aggregate_type: str = "denuncia"
    anonima: bool = False
    tipo_denuncia: str = ""


@dataclass
class DenunciaEncaminhadaEvento(EventoOuvidoria):
    """Evento: Denúncia encaminhada a órgão externo."""

    aggregate_type: str = "denuncia"
    orgao_destino: str = ""  # MP, PF, TCE
    numero_processo: str = ""


@dataclass
class PedidoLaiRegistradoEvento(EventoOuvidoria):
    """Evento: Pedido LAI registrado."""

    tipo: TipoEventoOuv = TipoEventoOuv.PEDIDO_LAI_REGISTRADO
    aggregate_type: str = "pedido_lai"
    nivel_sigilo: str = "publico"


@dataclass
class PedidoLaiRespondidoEvento(EventoOuvidoria):
    """Evento: Pedido LAI respondido."""

    tipo: TipoEventoOuv = TipoEventoOuv.PEDIDO_LAI_RESPONDIDO
    aggregate_type: str = "pedido_lai"
    deferido: bool = True


@dataclass
class PrazoVencendoEvento(EventoOuvidoria):
    """Evento: Prazo de resposta vencendo (alerta)."""

    tipo: TipoEventoOuv = TipoEventoOuv.PRAZO_VENCENDO
    dias_restantes: int = 0


@dataclass
class PrazoVencidoEvento(EventoOuvidoria):
    """Evento: Prazo de resposta vencido."""

    tipo: TipoEventoOuv = TipoEventoOuv.PRAZO_VENCIDO


__all__ = [
    "TipoEventoOuv",
    "EventoOuvidoria",
    "ManifestacaoRegistradaEvento",
    "ManifestacaoRespondidaEvento",
    "DenunciaRegistradaEvento",
    "DenunciaEncaminhadaEvento",
    "PedidoLaiRegistradoEvento",
    "PedidoLaiRespondidoEvento",
    "PrazoVencendoEvento",
    "PrazoVencidoEvento",
]
