"""Infraestrutura de mensageria do DOM-GDO.

Implementa o padrão Transactional Outbox (014-Modelo-de-Integracao,
seção 6): eventos de domínio são gravados na tabela `gdo.eventos_outbox`
na MESMA transação do negócio e, em seguida, despachados para o
barramento Redis pelo dispatcher:

* `DespachadorRedisStreams` — barramento persistente/auditável (XADD);
* `DespachadorPubSub` — barramento efêmero tempo-real (PUBLISH, Fase VII),
  consumido pelos assinantes do DOM-INT / portais.
"""

from .dispatcher import DespachadorRedisStreams, despachar_eventos_pendentes
from .outbox import PublicadorOutboxGDO, TopicosGDO
from .pubsub import DespachadorPubSub, montar_envelope

__all__ = [
    "TopicosGDO",
    "PublicadorOutboxGDO",
    "DespachadorRedisStreams",
    "despachar_eventos_pendentes",
    "DespachadorPubSub",
    "montar_envelope",
]
