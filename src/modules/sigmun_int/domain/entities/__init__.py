"""Entidades do domínio de Integração e Interoperabilidade (DOM-INT).

Representam o núcleo do domínio: o catálogo de APIs externas e contratos
de integração, os conectores oficiais (GOV.BR, e-Social, SIAFIC, PNCP),
os webhooks de inscrição em eventos, o registro de entregas de mensagens
(com retry e fila de mensagens mortas) e o registro de eventos consumidos
do Transactional Outbox dos domínios produtores (GDO, Compras).

O modelo segue o padrão DDD do SIGMUN: entidades ``dataclass`` de domínio
puro (sem dependências de infraestrutura), com identificadores ``str`` por
padrão (UUID) e indicador de exclusão lógica ``is_deleted``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from uuid import uuid4

__all__ = [
    "EstadoApi",
    "TipoApi",
    "AutenticacaoApi",
    "EstadoContrato",
    "EstadoConector",
    "EstadoInscricao",
    "EstadoEntrega",
    "ApiExterna",
    "ContratoIntegracao",
    "Conector",
    "Webhook",
    "EntregaWebhook",
    "EventoProcessado",
]


class EstadoApi(Enum):
    """Estado do ciclo de vida de uma API externa."""

    RASCUNHO = "rascunho"
    TESTES = "testes"
    ATIVA = "ativa"
    INATIVA = "inativa"
    RETIRADA = "retirada"


class TipoApi(Enum):
    """Tipo de interface da API externa."""

    REST = "rest"
    SOAP = "soap"
    GRAPHQL = "graphql"


class AutenticacaoApi(Enum):
    """Esquema de autenticação usado pela API externa."""

    NENHUMA = "nenhuma"
    API_KEY = "api_key"
    BASIC = "basic"
    OAUTH2 = "oauth2"
    MTLS = "mtls"


class EstadoContrato(Enum):
    """Estado do contrato de integração."""

    RASCUNHO = "rascunho"
    VIGENTE = "vigente"
    OBSOLETO = "obsoleto"
    RETIRADO = "retirado"


class EstadoConector(Enum):
    """Estado de configuração de um conector oficial de interoperabilidade."""

    SEM_CONFIGURACAO = "sem_configuracao"
    CONFIGURADO = "configurado"
    TESTES = "testes"
    ATIVO = "ativo"
    INATIVO = "inativo"


class EstadoInscricao(Enum):
    """Estado de uma inscrição de webhook em eventos."""

    ATIVA = "ativa"
    DESATIVADA = "desativada"


class EstadoEntrega(Enum):
    """Estado de uma entrega de mensagem a um webhook (com retry e DLQ)."""

    PENDENTE = "pendente"
    SUCESSO = "sucesso"
    FALHOU = "falhou"
    FILA_MORTA = "fila_morta"
    CANCELADO = "cancelado"


# ---------------------------------------------------------------------------
# Catálogo de APIs externas
# ---------------------------------------------------------------------------


@dataclass
class ApiExterna:
    """API externa do catálogo de integrações do município."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    provedor: str = ""
    url_base: str = ""
    tipo: TipoApi = TipoApi.REST
    autenticacao: AutenticacaoApi = AutenticacaoApi.OAUTH2
    estado: EstadoApi = EstadoApi.RASCUNHO
    versao: str = "1.0"
    limite_por_minuto: int = 300
    timeout_seg: int = 30
    criado_em: datetime = field(default_factory=datetime.utcnow)
    atualizado_em: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    @property
    def eh_consumivel(self) -> bool:
        """API é consumível se está ativa ou em testes."""
        return self.estado in (EstadoApi.ATIVA, EstadoApi.TESTES)


# ---------------------------------------------------------------------------
# Contratos de integração
# ---------------------------------------------------------------------------


@dataclass
class ContratoIntegracao:
    """Contrato de integração com uma API externa do catálogo."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    versao_formato: str = "1.0"
    esquema_ref: str = ""
    api_externa_id: str = ""
    estado: EstadoContrato = EstadoContrato.RASCUNHO
    criado_em: datetime = field(default_factory=datetime.utcnow)
    atualizado_em: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    @property
    def eh_vigente(self) -> bool:
        return self.estado is EstadoContrato.VIGENTE


# ---------------------------------------------------------------------------
# Conectores oficiais
# ---------------------------------------------------------------------------


@dataclass
class Conector:
    """Conector oficial de interoperabilidade (GOV.BR, e-Social, SIAFIC, PNCP)."""

    id: str = field(default_factory=lambda: str(uuid4()))
    codigo: str = ""
    nome: str = ""
    descricao: str = ""
    provedor: str = ""
    url_base: str = ""
    autenticacao_tipo: str = "oauth2"
    estado: EstadoConector = EstadoConector.SEM_CONFIGURACAO
    config: dict = field(default_factory=dict)
    criado_em: datetime = field(default_factory=datetime.utcnow)
    atualizado_em: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    @property
    def esta_ativo(self) -> bool:
        return self.estado is EstadoConector.ATIVO


# ---------------------------------------------------------------------------
# Webhooks de inscrição em eventos
# ---------------------------------------------------------------------------


@dataclass
class Webhook:
    """Webhook inscrito para receber eventos do barramento."""

    id: str = field(default_factory=lambda: str(uuid4()))
    nome: str = ""
    url_destino: str = ""
    segredo_ref: str = ""
    topicos: list[str] = field(default_factory=list)
    cabecalhos: dict = field(default_factory=dict)
    estado: EstadoInscricao = EstadoInscricao.ATIVA
    max_tentativas: int = 5
    backoff_base_seg: int = 60
    criado_em: datetime = field(default_factory=datetime.utcnow)
    atualizado_em: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    def inscrito_em(self, topico: str) -> bool:
        """Indica se este webhook está inscrito no tópico informado."""
        if "*" in self.topicos:
            return True
        return topico in self.topicos


# ---------------------------------------------------------------------------
# Entregas de mensagens a webhooks (retry/DLQ)
# ---------------------------------------------------------------------------


@dataclass
class EntregaWebhook:
    """Entrega de uma mensagem a um webhook inscrito."""

    id: str = field(default_factory=lambda: str(uuid4()))
    webhook_id: str = ""
    url_destino: str = ""
    cabecalhos: dict = field(default_factory=dict)
    topico: str = ""
    evento_nome: str = ""
    agregado_tipo: str = ""
    agregado_id: str = ""
    payload: dict = field(default_factory=dict)
    estado: EstadoEntrega = EstadoEntrega.PENDENTE
    tentativas: int = 0
    max_tentativas: int = 5
    backoff_base_seg: int = 60
    ultimo_http_status: int | None = None
    ultimo_erro: str = ""
    proximo_retry: datetime | None = None
    criado_em: datetime = field(default_factory=datetime.utcnow)
    entregue_em: datetime | None = None
    atualizado_em: datetime | None = None
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted

    @property
    def eh_sucesso(self) -> bool:
        return self.estado is EstadoEntrega.SUCESSO

    @property
    def na_fila_morta(self) -> bool:
        return self.estado is EstadoEntrega.FILA_MORTA

    def pendente_para_retry(self, agora: datetime) -> bool:
        """Pendente e habilitada para tentar novamente no instante informado?"""
        if self.estado is not EstadoEntrega.PENDENTE:
            return False
        return self.proximo_retry is None or self.proximo_retry <= agora

    def registrar_sucesso(self, http_status: int | None, agora: datetime) -> None:
        """Registra uma entrega bem-sucedida."""
        self.estado = EstadoEntrega.SUCESSO
        self.tentativas += 1
        self.ultimo_http_status = http_status
        self.ultimo_erro = ""
        self.proximo_retry = None
        self.entregue_em = agora

    def registrar_falha(self, http_status: int | None, erro: str, agora: datetime) -> None:
        """Registra uma falha, programando o retry ou indo para a fila de mortas."""
        self.tentativas += 1
        self.ultimo_http_status = http_status
        self.ultimo_erro = erro[:500]
        if self.tentativas >= max(self.max_tentativas, 1):
            self.estado = EstadoEntrega.FILA_MORTA
            self.proximo_retry = None
        else:
            self.estado = EstadoEntrega.FALHOU
            self.proximo_retry = self._calcular_proximo_retry(agora)

    def _calcular_proximo_retry(self, desde: datetime) -> datetime:
        """Atraso backoff exponencial: base * 2^(tentativas-1) segundos."""
        atraso_seg = self.backoff_base_seg * (2 ** max(self.tentativas - 1, 0))
        return desde + timedelta(seconds=atraso_seg)


# ---------------------------------------------------------------------------
# Registro de eventos consumidos do outbox de domínios produtores
# ---------------------------------------------------------------------------


@dataclass
class EventoProcessado:
    """Evento consumido do Transactional Outbox de um domínio produtor.

    Cumpre o papel de inbox do barramento e garante a idempotência: um
    evento da fonte (``evento_outbox_id``) é processado uma única vez.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    fonte: str = ""
    evento_outbox_id: str = ""
    topico: str = ""
    evento_nome: str = ""
    agregado_tipo: str = ""
    agregado_id: str = ""
    payload: dict = field(default_factory=dict)
    recebido_em: datetime = field(default_factory=datetime.utcnow)
    is_deleted: bool = False

    @property
    def is_active(self) -> bool:
        return not self.is_deleted
