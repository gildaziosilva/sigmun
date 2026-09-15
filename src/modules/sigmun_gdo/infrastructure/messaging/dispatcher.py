"""Despacho de eventos pendentes da outbox para o barramento Redis Streams.

O `DespachadorRedisStreams` lê os eventos com status `pendente` da tabela
`gdo.eventos_outbox`, publica cada um no stream do seu tópico
(`XADD gdo.documento.<evento> ...`) e atualiza o status na outbox
(`publicado` em caso de sucesso; `erro` após esgotar as tentativas).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import redis as redis_lib
from sqlalchemy.orm import Session

from ..database.models import EventoOutboxModel

MAX_TENTATIVAS = 5
LOTE_PADRAO = 100


class DespachadorRedisStreams:
    """Publica eventos da outbox em streams do Redis.

    Cada tópico (ex.: `gdo.documento.criado`) corresponde a um stream Redis;
    cada evento é uma entrada com os campos de envelope + payload JSON.
    """

    def __init__(self, redis_url: str, max_tentativas: int = MAX_TENTATIVAS):
        self._redis = redis_lib.Redis.from_url(redis_url, decode_responses=True)
        self._max_tentativas = max_tentativas

    def despachar(self, session: Session, lote: int = LOTE_PADRAO) -> dict:
        """Despacha até `lote` eventos pendentes e confirma a transação.

        Eventos em falha têm a tentativa incrementada; ao atingir
        `max_tentativas` são marcados com status `erro` para análise.
        """
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
                self._publicar_no_stream(evento)
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

    def _publicar_no_stream(self, evento: EventoOutboxModel) -> None:
        """Publica o evento no stream do seu tópico (XADD)."""
        self._redis.xadd(
            evento.topico,
            {
                "evento_id": str(evento.id),
                "evento_nome": evento.evento_nome,
                "agregado_tipo": evento.agregado_tipo,
                "agregado_id": evento.agregado_id,
                "payload": json.dumps(evento.payload, ensure_ascii=False, default=str),
            },
        )


def despachar_eventos_pendentes(
    session: Session, redis_url: str | None = None, lote: int = LOTE_PADRAO
) -> dict:
    """Função de conveniência: despacha pendentes usando `settings.REDIS_URL`."""
    from src.shared.config.settings import settings

    url = redis_url or settings.REDIS_URL
    return DespachadorRedisStreams(url).despachar(session, lote=lote)


__all__ = ["DespachadorRedisStreams", "despachar_eventos_pendentes", "MAX_TENTATIVAS"]
