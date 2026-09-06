"""Transactional Outbox do DOM-GDO (014-Modelo-de-Integracao, seção 6).

Os eventos de integração são gravados na tabela `gdo.eventos_outbox` na
MESMA transação da operação de negócio, garantindo atomicidade entre o
estado persistido e o evento a ser publicado. O despacho para o barramento
(Redis Streams) é feito depois pelo `DespachadorRedisStreams`.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from ...application.interfaces import PublicadorEventos
from ..database.models import EventoOutboxModel


class TopicosGDO:
    """Tópicos dos eventos publicados pelo DOM-GDO.

    Espelha a lista de eventos publicados definida no
    `014-Modelo-de-Integracao-Gestao-Documental.md` (seção Eventos de Domínio).
    """

    DOCUMENTO_CRIADO = "gdo.documento.criado"
    DOCUMENTO_CLASSIFICADO = "gdo.documento.classificado"
    DOCUMENTO_TRAMITADO = "gdo.documento.tramitado"
    DOCUMENTO_RECEBIDO = "gdo.documento.recebido"
    DOCUMENTO_ARQUIVADO = "gdo.documento.arquivado"
    DOCUMENTO_ASSINADO = "gdo.documento.assinado"
    DOCUMENTO_ELIMINADO = "gdo.documento.eliminado"
    DOCUMENTO_PUBLICADO = "gdo.documento.publicado"
    DOCUMENTO_VINCULADO_PROCESSO = "gdo.documento.vinculado_processo"


class PublicadorOutboxGDO(PublicadorEventos):
    """Publica eventos via Transactional Outbox.

    O evento é adicionado à sessão recebida — portanto é gravado no banco
    com commit/rollback da própria operação de negócio (mesma transação).
    """

    def __init__(self, session: Session):
        self._session = session

    def publicar(
        self,
        topico: str,
        evento_nome: str,
        agregado_tipo: str,
        agregado_id: str,
        payload: dict,
    ) -> None:
        """Registra o evento na outbox (status inicial: pendente)."""
        self._session.add(
            EventoOutboxModel(
                topico=topico,
                evento_nome=evento_nome,
                agregado_tipo=agregado_tipo,
                agregado_id=agregado_id,
                payload=payload,
                status="pendente",
            )
        )
        self._session.flush()


__all__ = ["TopicosGDO", "PublicadorOutboxGDO"]
