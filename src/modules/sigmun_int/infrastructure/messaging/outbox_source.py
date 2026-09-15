"""Fonte SQL de leitura do Transactional Outbox dos domínios produtores.

``OutboxSQLAlchemySource`` lê os eventos ``pendente`` da tabela
``<schema>.eventos_outbox`` do domínio produtor (``gdo``, ``compras``) e
os marca como ``publicado`` após seu processamento pelo barramento DOM-INT.

O nome do schema é validado contra as fontes permitidas (RN-INT-003)
para impedir injeção SQL pelo parâmetro ``fonte``.
"""

from __future__ import annotations

from sqlalchemy import text
from sqlalchemy.orm import Session

from ...application.interfaces import EventoOutbox, FonteOutbox
from ...application.use_cases.bus_use_cases import FONTES_OUTBOX_VALIDAS
from ...domain.exceptions import FonteOutboxInvalidaError

__all__ = ["OutboxSQLAlchemySource"]


class OutboxSQLAlchemySource(FonteOutbox):
    """Implementação SQLAlchemy de ``FonteOutbox`` para outbox transacionais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def ler_pendentes(self, fonte: str, lote: int = 100) -> list[EventoOutbox]:
        """Lê até ``lote`` eventos con status ``pendente`` da fonte."""
        schema = self._validar_fonte(fonte)
        filas = self._session.execute(
            text(
                f"SELECT id, topico, evento_nome, agregado_tipo, agregado_id, payload "
                f"FROM {schema}.eventos_outbox "
                f"WHERE status = 'pendente' "
                f"ORDER BY criado_em "
                f"LIMIT :lote"
            ),
            {"lote": lote},
        ).all()
        return [
            EventoOutbox(
                id=str(fila.id),
                topico=fila.topico,
                evento_nome=fila.evento_nome,
                agregado_tipo=fila.agregado_tipo,
                agregado_id=fila.agregado_id,
                payload=fila.payload or {},
            )
            for fila in filas
        ]

    def marcar_publicado(self, fonte: str, evento_outbox_id: str) -> None:
        """Marca o evento do outbox como ``publicado`` após seu processamento."""
        schema = self._validar_fonte(fonte)
        self._session.execute(
            text(
                f"UPDATE {schema}.eventos_outbox "
                f"SET status = 'publicado', published_at = now() "
                f"WHERE id = :evento_id AND status = 'pendente'"
            ),
            {"evento_id": evento_outbox_id},
        )
        self._session.flush()

    @staticmethod
    def _validar_fonte(fonte: str) -> str:
        """Valida o nome do schema/fonte contra as permitidas."""
        if fonte not in FONTES_OUTBOX_VALIDAS:
            raise FonteOutboxInvalidaError(
                f"Fonte de outbox inválida: '{fonte}' (válidas: {FONTES_OUTBOX_VALIDAS})"
            )
        return fonte
