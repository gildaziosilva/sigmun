"""Infraestrutura de mensageria do DOM-GDO.

Implementa o padrão Transactional Outbox (014-Modelo-de-Integracao,
seção 6): eventos de domínio são gravados na tabela `gdo.eventos_outbox`
na MESMA transação do negócio e, em seguida, despachados para o
barramento (Redis Streams) pelo dispatcher.
"""

from .outbox import TopicosGDO, PublicadorOutboxGDO
from .dispatcher import DespachadorRedisStreams, despachar_eventos_pendentes

__all__ = [
    "TopicosGDO",
    "PublicadorOutboxGDO",
    "DespachadorRedisStreams",
    "despachar_eventos_pendentes",
]