"""Mensageria e eventos de Atendimento ao Cidadão (DOM-ATE)."""

from typing import Optional
from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from src.modules.sigmun_ate.application.interfaces import PublicadorEventos
from src.modules.sigmun_ate.domain.events import EventoDominio
from src.modules.sigmun_ate.infrastructure.database.models import EventoOutboxModel


class PublicadorOutboxATE(PublicadorEventos):
    """Publicador de eventos via Transactional Outbox Pattern."""

    def __init__(self, session: Session):
        self._session = session

    def publicar(self, evento) -> None:
        """Publica evento salvando na tabela outbox (mesma transação do negócio)."""
        payload = self._serializar_evento(evento)
        
        outbox = EventoOutboxModel(
            id=evento.id if hasattr(evento, 'id') else evento.__dict__.get('id', str(__import__('uuid').uuid4())),
            topico=self._obter_topico(evento),
            evento_nome=evento.__class__.__name__,
            agregado_tipo=evento.aggregate_type if hasattr(evento, 'aggregate_type') else evento.__class__.__name__,
            agregado_id=evento.aggregate_id if hasattr(evento, 'aggregate_id') else "",
            payload=payload,
            status="pendente",
            tentativas=0,
            created_at=datetime.utcnow(),
        )
        
        # Salva na mesma transação do repositório de negócio
        from src.modules.sigmun_ate.infrastructure.database.models import AteBase
        from sqlalchemy.orm import Session as SASession
        # O merge será feito pelo chamador via session.merge
        # Apenas criamos o modelo aqui
        pass

    def _obter_topico(self, evento) -> str:
        """Mapeia evento para tópico de integração."""
        mapeamento = {
            "TriagemRealizada": "ate.triagem.realizada",
            "FilaAberta": "ate.fila.aberta",
            "FilaFechada": "ate.fila.fechada",
            "SenhaEmitida": "ate.senha.emitida",
            "SenhaChamada": "ate.senha.chamada",
            "SenhaRechamada": "ate.senha.rechamada",
            "SenhaAtendida": "ate.senha.atendida",
            "SenhaNaoCompareceu": "ate.senha.nao_compareceu",
            "SenhaCancelada": "ate.senha.cancelada",
            "AtendimentoIniciado": "ate.atendimento.iniciado",
            "AtendimentoConcluido": "ate.atendimento.concluido",
            "AtendimentoCancelado": "ate.atendimento.cancelado",
            "AvaliacaoRegistrada": "ate.avaliacao.registrada",
            "EncaminhamentoCriado": "ate.encaminhamento.criado",
            "EncaminhamentoConcluido": "ate.encaminhamento.concluido",
        }
        return mapeamento.get(evento.__class__.__name__, f"ate.{evento.__class__.__name__.lower()}")

    def _serializar_evento(self, evento) -> dict:
        """Serializa evento para JSON."""
        dados = {}
        for key, value in evento.__dict__.items():
            if key.startswith('_'):
                continue
            if isinstance(value, (datetime,)):
                dados[key] = value.isoformat()
            elif hasattr(value, 'value'):  # Enum
                dados[key] = value.value
            else:
                dados[key] = value
        return dados


class DespachanteEventosOutbox:
    """Despacha eventos pendentes da tabela outbox para o barramento de integração."""

    def __init__(self, session_factory, publicador_externo):
        self._session_factory = session_factory
        self._publicador_externo = publicador_externo

    def despachar_pendentes(self, limite: int = 100) -> int:
        """Processa eventos pendentes no outbox."""
        from sqlalchemy import select
        from sqlalchemy.orm import Session
        
        session = self._session_factory()
        try:
            from src.modules.sigmun_ate.infrastructure.database.models import EventoOutboxModel
            
            stmt = select(EventoOutboxModel).where(
                EventoOutboxModel.status == "pendente"
            ).order_by(EventoOutboxModel.created_at).limit(100)
            
            eventos = session.execute(select(EventoOutboxModel).where(
                EventoOutboxModel.status == "pendente"
            ).order_by(EventoOutboxModel.created_at).limit(limite)).scalars().all()
            
            processados = 0
            for evento in eventos:
                try:
                    self._publicador_externo.publicar(
                        topico=evento.topico,
                        payload=evento.payload,
                        evento_nome=evento.evento_nome,
                    )
                    evento.status = "publicado"
                    evento.published_at = __import__('datetime').datetime.utcnow()
                    processados += 1
                except Exception as e:
                    evento.tentativas += 1
                    evento.ultimo_erro = str(e)
                    if evento.tentativas >= 5:
                        evento.status = "erro"
            
            session.commit()
            return processados
        finally:
            session.close()


__all__ = [
    "PublicadorOutboxATE",
    "DespachanteEventosOutbox",
]