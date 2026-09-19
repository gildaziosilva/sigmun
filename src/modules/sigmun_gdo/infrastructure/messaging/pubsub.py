"""Despacho de eventos pendentes da outbox para o barramento Redis Pub/Sub.

Complementa o `DespachadorRedisStreams` (persistente/auditável): aqui cada
evento com status `pendente` da tabela `gdo.eventos_outbox` é serializado
como envelope JSON e publicado via `PUBLISH <topico> <envelope>` — o canal
Pub/Sub é o próprio tópico do evento (ex.: `gdo.documento.criado`).

Semântica de entrega: at-least-once (o status só é marcado como `publicado`
após o PUBLISH; assinantes devem ser idempotentes — o DOM-INT já garante
idempotência via `integracao.eventos_processados`).
"""

from __future__ import annotations

import json
from typing import Any

from sqlalchemy.orm import Session

from ..database.models import EventoOutboxModel

MAX_TENTATIVAS = 5
LOTE_PADRAO = 100


def montar_envelope(evento: EventoOutboxModel) -> str:
    """Serializa o evento da outbox como envelope JSON do Pub/Sub."""
    criado_em = evento.created_at.isoformat() if evento.created_at is not None else None
    return json.dumps(
        {
            "evento_id": str(evento.id),
            "topico": evento.topico,
            "evento_nome": evento.evento_nome,
            "agregado_tipo": evento.agregado_tipo,
            "agregado_id": evento.agregado_id,
            "payload": evento.payload or {},
            "created_at": criado_em,
        },
        ensure_ascii=False,
        default=str,
    )


class DespachadorPubSub:
    """Publica eventos da outbox em canais Redis Pub/Sub.

    Recebe um cliente Redis já conectado (injetável para testes); o canal
    de cada mensagem é o próprio `topico` do evento.
    """

    def __init__(self, redis_client: Any, max_tentativas: int = MAX_TENTATIVAS) -> None:
        self._redis = redis_client
        self._max_tentativas = max_tentativas

    def despachar(self, session: Session, lote: int = LOTE_PADRAO) -> dict[str, int]:
        """Despacha até `lote` eventos pendentes via PUBLISH e commita.

        Eventos em falha têm a tentativa incrementada; ao atingir
        `max_tentativas` são marcados com status `erro` para análise.
        """
        from datetime import datetime, timezone

        pendentes = (
            session.query(EventoOutboxModel)
            .filter(EventoOutboxModel.status == "pendente")
            .order_by(EventoOutboxModel.created_at)
            .limit(lote)
            .all()
        )

        resultado = {"processados": 0, "publicados": 0, "erros": 0}
        for evento in pendentes:
            resultado["processados"] += 1
            try:
                self._redis.publish(evento.topico, montar_envelope(evento))
                evento.status = "publicado"
                evento.published_at = datetime.now(timezone.utc)
                resultado["publicados"] += 1
            except Exception as exc:  # noqa: BLE001 — falha de broker é recuperável
                evento.tentativas += 1
                evento.ultimo_erro = str(exc)[:500]
                if evento.tentativas >= self._max_tentativas:
                    evento.status = "erro"
                resultado["erros"] += 1

        session.commit()
        return resultado


__all__ = ["DespachadorPubSub", "montar_envelope", "MAX_TENTATIVAS", "LOTE_PADRAO"]
