"""Casos de uso do barramento de eventos interno (DOM-INT).

Implementam o Event Bus corporativo (014-Modelo-de-Integracao):

1. ``ConsumirOutboxUseCase`` consome o Transactional Outbox dos domínios
   produtores (GDO e Compras), garante idempotência (inbox
   ``integracao.eventos_processados``) e enfileira entregas para os webhooks
   inscritos no tópico de cada evento.

2. ``DespacharWebhooksUseCase`` entrega as mensagens pendentes aos
   webhooks destino via HTTP com retries com backoff exponencial; ao
   esgotar as tentativas a mensagem vai para a fila de mensagens mortas (DLQ).
"""

from datetime import datetime

from ...domain.entities import EntregaWebhook, EstadoEntrega, EventoProcessado
from ...domain.exceptions import FonteOutboxInvalidaError
from ..interfaces import (
    FonteOutbox,
    RepositorioEntregaWebhook,
    RepositorioEventoProcessado,
    RepositorioWebhook,
    TransporteWebhook,
)

__all__ = [
    "FONTES_OUTBOX_VALIDAS",
    "ConsumirOutboxUseCase",
    "DespacharWebhooksUseCase",
]

#: Domínios produtores cujos outbox o barramento consome (DOM-INT).
FONTES_OUTBOX_VALIDAS: tuple[str, ...] = ("gdo", "compras")

TIMEOUT_ENVIO_PADRAO_SEG = 30


class ConsumirOutboxUseCase:
    """Consome eventos pendentes do outbox de um domínio produtor.

    Para cada evento novo: enfileira uma entrega por cada webhook inscrito no
    tópico, registra o evento no inbox (idempotência) e marca o evento
    como publicado no outbox de origem.
    """

    def __init__(
        self,
        outbox: FonteOutbox,
        repo_webhooks: RepositorioWebhook,
        repo_entregas: RepositorioEntregaWebhook,
        repo_eventos: RepositorioEventoProcessado,
    ) -> None:
        self._outbox = outbox
        self._repo_webhooks = repo_webhooks
        self._repo_entregas = repo_entregas
        self._repo_eventos = repo_eventos

    def execute(self, fonte: str = "gdo", lote: int = 100) -> dict:
        """Processa até ``lote`` eventos pendentes da fonte indicada."""
        if fonte not in FONTES_OUTBOX_VALIDAS:
            raise FonteOutboxInvalidaError(
                f"Fonte de outbox inválida: '{fonte}' (válidas: {FONTES_OUTBOX_VALIDAS})"
            )

        pendentes = self._outbox.ler_pendentes(fonte, lote)
        webhooks_ativos = self._repo_webhooks.find_ativos()

        resumo = {
            "fonte": fonte,
            "lidos": 0,
            "novos": 0,
            "duplicados": 0,
            "entregas_criadas": 0,
        }
        for evento in pendentes:
            resumo["lidos"] += 1
            if self._repo_eventos.exists(fonte, evento.id):
                resumo["duplicados"] += 1
                continue

            for webhook in webhooks_ativos:
                if not webhook.inscrito_em(evento.topico):
                    continue
                entrega = EntregaWebhook(
                    webhook_id=webhook.id,
                    url_destino=webhook.url_destino,
                    cabecalhos=webhook.cabecalhos,
                    topico=evento.topico,
                    evento_nome=evento.evento_nome,
                    agregado_tipo=evento.agregado_tipo,
                    agregado_id=evento.agregado_id,
                    payload=evento.payload,
                    estado=EstadoEntrega.PENDENTE,
                    max_tentativas=webhook.max_tentativas,
                    backoff_base_seg=webhook.backoff_base_seg,
                )
                self._repo_entregas.save(entrega)
                resumo["entregas_criadas"] += 1

            processado = EventoProcessado(
                fonte=fonte,
                evento_outbox_id=evento.id,
                topico=evento.topico,
                evento_nome=evento.evento_nome,
                agregado_tipo=evento.agregado_tipo,
                agregado_id=evento.agregado_id,
                payload=evento.payload,
            )
            self._repo_eventos.save(processado)
            self._outbox.marcar_publicado(fonte, evento.id)
            resumo["novos"] += 1

        return resumo


class DespacharWebhooksUseCase:
    """Entrega as mensagens pendentes aos webhooks inscritos.

    Utiliza ``TransporteWebhook`` para o envio HTTP. Em caso de falha, registra a
    tentativa e agenda a próxima via backoff exponencial; ao esgotar
    ``max_tentativas`` a mensagem vai para a fila de mensagens mortas.
    """

    def __init__(
        self,
        repo_entregas: RepositorioEntregaWebhook,
        transporte: TransporteWebhook,
    ) -> None:
        self._repo_entregas = repo_entregas
        self._transporte = transporte

    def execute(self, lote: int = 100, agora: datetime | None = None) -> dict:
        """Processa até ``lote`` entregas pendentes e retorna o resumo."""
        momento = agora or datetime.utcnow()
        pendentes = self._repo_entregas.list_pendentes_para_retry(lote, momento)

        resumo = {"processadas": 0, "sucessos": 0, "falhas": 0, "fila_morta": 0}
        for entrega in pendentes:
            resumo["processadas"] += 1
            resultado = self._transporte.enviar(
                url=entrega.url_destino,
                payload=self._payload_de(entrega),
                cabecalhos=entrega.cabecalhos,
                timeout_seg=TIMEOUT_ENVIO_PADRAO_SEG,
            )
            if resultado.ok:
                entrega.registrar_sucesso(resultado.http_status, momento)
                resumo["sucessos"] += 1
            else:
                entrega.registrar_falha(
                    resultado.http_status, resultado.erro or "erro de transporte", momento
                )
                resumo["falhas" if not entrega.na_fila_morta else "fila_morta"] += 1
            self._repo_entregas.save(entrega)

        return resumo

    @staticmethod
    def _payload_de(entrega: EntregaWebhook) -> dict:
        """Envelope da mensagem entregue ao webhook (014-Modelo-de-Integracao)."""
        return {
            "evento_nome": entrega.evento_nome,
            "agregado_tipo": entrega.agregado_tipo,
            "agregado_id": entrega.agregado_id,
            "topico": entrega.topico,
            "tentativa": entrega.tentativas,
            "payload": entrega.payload,
        }
