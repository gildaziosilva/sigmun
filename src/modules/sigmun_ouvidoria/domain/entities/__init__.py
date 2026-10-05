"""Entidades do domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal).

RN-OUV-001: toda manifestação recebe protocolo único (AAAA-NNNNNN).
RN-OUV-002: denúncias podem ser anônimas; demais tipos exigem identificação.
RN-OUV-003: LAI (Lei 12.527/2011) - prazo de 20 dias, prorrogáveis por mais 10.
RN-OUV-010: transições de status controladas (fluxo FalaBR).
RN-OUV-020: prazos de resposta por tipo de manifestação.
RN-OUV-030: proteção de dados do denunciante (sigilo).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from uuid import uuid4

from ..exceptions import (
    AcessoNegadoError,
    EstadoInvalidoError,
    RegraNegocioError,
)
from ..value_objects import (
    Anexo,
    CanalRecebimento,
    DadosCidadao,
    FormaResposta,
    NivelSigilo,
    PrazoResposta,
    Protocolo,
    StatusManifestacao,
    TipoDenuncia,
    TipoManifestacao,
)


class Prioridade(Enum):
    """Prioridade de tratamento."""

    BAIXA = "baixa"
    NORMAL = "normal"
    ALTA = "alta"
    URGENTE = "urgente"

    @property
    def rotulo(self) -> str:
        return {
            Prioridade.BAIXA: "Baixa",
            Prioridade.NORMAL: "Normal",
            Prioridade.ALTA: "Alta",
            Prioridade.URGENTE: "Urgente",
        }[self]


@dataclass
class ManifestacaoBase:
    """Base comum para manifestações."""

    id: str = field(default_factory=lambda: str(uuid4()))
    protocolo: Protocolo | None = None
    tipo: TipoManifestacao = TipoManifestacao.SOLICITACAO
    status: StatusManifestacao = StatusManifestacao.REGISTRADA
    prioridade: Prioridade = Prioridade.NORMAL
    assunto: str = ""
    descricao: str = ""
    cidadao: DadosCidadao | None = None
    canal: CanalRecebimento = CanalRecebimento.PORTAL_CIDADAO
    orgao_destino: str = ""
    setor_responsavel: str = ""
    prazo: PrazoResposta | None = None
    anexos: list[Anexo] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    updated_by: str = ""
    is_deleted: bool = False
    # Avaliação do cidadão — presente na base porque `avaliar()` é herdado por
    # manifestação, denúncia e pedido LAI.
    avaliacao_cidadao: int | None = None
    comentario_avaliacao: str = ""

    def validar(self) -> None:
        """Valida regras estruturais (RN-OUV-001, RN-OUV-002)."""
        if not self.assunto:
            raise RegraNegocioError("Assunto é obrigatório")
        if not self.descricao:
            raise RegraNegocioError("Descrição é obrigatória")
        if not self.orgao_destino:
            raise RegraNegocioError("Órgão de destino é obrigatório")
        if self.tipo != TipoManifestacao.DENUNCIA and (not self.cidadao or self.cidadao.anonimo):
            raise RegraNegocioError(
                "Manifestações não-anônimas exigem identificação do cidadão (RN-OUV-002)"
            )
        if self.tipo == TipoManifestacao.DENUNCIA and self.cidadao and not self.cidadao.anonimo:
            pass

    def alterar_status(self, novo_status: StatusManifestacao, usuario: str = "") -> None:
        """Altera status validando transições (RN-OUV-010)."""
        if not self.status.pode_transicionar_para(novo_status):
            raise EstadoInvalidoError(
                f"Transição inválida: {self.status.rotulo} -> {novo_status.rotulo}"
            )
        self.status = novo_status
        self.updated_at = datetime.utcnow()
        self.updated_by = usuario

    def adicionar_anexo(self, anexo: Anexo) -> None:
        """Adiciona anexo à manifestação."""
        self.anexos.append(anexo)
        self.updated_at = datetime.utcnow()

    def prorrogar_prazo(self, justificativa: str, usuario: str = "") -> None:
        """Prorroga prazo de resposta (RN-OUV-020, LAI Art. 11 §1º)."""
        if not self.prazo:
            raise RegraNegocioError("Não há prazo definido para prorrogar")
        if self.prazo.prorrogado:
            raise RegraNegocioError("Prazo já foi prorrogado anteriormente")
        from datetime import timedelta

        nova_data = self.prazo.data_limite + timedelta(days=10)
        self.prazo = PrazoResposta(
            data_limite=nova_data,
            dias_uteis=self.prazo.dias_uteis + 10,
            prorrogado=True,
            data_prorrogacao=date.today(),
            justificativa_prorrogacao=justificativa,
        )
        self.updated_at = datetime.utcnow()
        self.updated_by = usuario

    def verificar_prazo(self) -> bool:
        """Verifica se o prazo está vencido."""
        return self.prazo.vencido if self.prazo else False

    def excluir(self) -> None:
        """Marca como excluído (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def avaliar(self, nota: int, comentario: str = "") -> None:
        """Registra avaliação do cidadão (1-5) e conclui a manifestação.

        Definido na base porque denúncia e pedido LAI também podem ser
        avaliados; os campos ficam aqui para que todas as herdeiras os possuam.
        """
        if self.status != StatusManifestacao.RESPONDIDA:
            raise EstadoInvalidoError("Só é possível avaliar manifestações respondidas")
        if not 1 <= nota <= 5:
            raise RegraNegocioError("Avaliação deve ser entre 1 e 5")
        self.avaliacao_cidadao = nota
        self.comentario_avaliacao = comentario
        self.alterar_status(StatusManifestacao.CONCLUIDA, "cidadao")


@dataclass
class Manifestacao(ManifestacaoBase):
    """Manifestação genérica (sugestão, elogio, reclamação, solicitação).

    RN-OUV-001: protocolo único.
    RN-OUV-002: exige identificação (não anônima).
    """

    resposta: str = ""
    forma_resposta: FormaResposta | None = None
    data_resposta: date | None = None
    respondido_por: str = ""

    def registrar_resposta(self, resposta: str, forma: FormaResposta, respondido_por: str) -> None:
        """Registra resposta ao cidadão."""
        if self.status not in (
            StatusManifestacao.EM_TRATAMENTO,
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
        ):
            raise EstadoInvalidoError("Só é possível responder manifestações em tratamento")
        self.resposta = resposta
        self.forma_resposta = forma
        self.data_resposta = date.today()
        self.respondido_por = respondido_por
        self.alterar_status(StatusManifestacao.RESPONDIDA, respondido_por)


@dataclass
class Denuncia(ManifestacaoBase):
    """Denúncia com proteção ao denunciante.

    RN-OUV-002: pode ser anônima.
    RN-OUV-030: dados do denunciante são sigilosos.
    """

    tipo_denuncia: TipoDenuncia = TipoDenuncia.OUTRO
    envolve_servidor_publico: bool = False
    servidor_envolvido: str = ""
    valor_envolvido: float | None = None
    local_fato: str = ""
    data_fato: date | None = None
    sigilo_denunciante: bool = True
    encaminhada_mp: bool = False
    encaminhada_pf: bool = False
    encaminhada_tce: bool = False
    numero_inquerito: str = ""
    resultado_investigacao: str = ""
    resposta: str = ""
    forma_resposta: FormaResposta | None = None
    data_resposta: date | None = None
    respondido_por: str = ""

    def validar(self) -> None:
        super().validar()
        if self.tipo != TipoManifestacao.DENUNCIA:
            self.tipo = TipoManifestacao.DENUNCIA
        if not self.local_fato:
            raise RegraNegocioError("Local do fato é obrigatório na denúncia")
        if not self.data_fato:
            raise RegraNegocioError("Data do fato é obrigatória na denúncia")

    def encaminhar_orgao_externo(self, orgao: str, numero_processo: str, usuario: str) -> None:
        """Registra encaminhamento a órgão externo (MP, PF, TCE)."""
        if orgao.upper() == "MP":
            self.encaminhada_mp = True
        elif orgao.upper() == "PF":
            self.encaminhada_pf = True
        elif orgao.upper() == "TCE":
            self.encaminhada_tce = True
        self.numero_inquerito = numero_processo
        self.alterar_status(StatusManifestacao.ENCAMINHADA, usuario)

    def concluir_investigacao(self, resultado: str, usuario: str) -> None:
        """Registra o resultado da investigação e conclui a tramitação.

        O encerramento de uma apuração não depende de o cidadão já ter sido
        respondido. O fluxo do domínio (PUML 003) admite tanto
        ``Respondida --> Concluida`` quanto ``EmApuracao --> Concluida``.
        Por isso a conclusão é aplicada em um passo, a partir do estado atual,
        sem exigir a passagem obrigatória por ``RESPONDIDA``.
        """
        self.resultado_investigacao = resultado
        self.updated_at = datetime.utcnow()
        self.updated_by = usuario
        self.status = StatusManifestacao.CONCLUIDA

    def registrar_resposta(self, resposta: str, forma: FormaResposta, respondido_por: str) -> None:
        """Registra resposta ao denunciante."""
        if self.status not in (
            StatusManifestacao.EM_TRATAMENTO,
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
        ):
            raise EstadoInvalidoError("Só é possível responder denúncias em tratamento")
        self.resposta = resposta
        self.forma_resposta = forma
        self.data_resposta = date.today()
        self.respondido_por = respondido_por
        self.alterar_status(StatusManifestacao.RESPONDIDA, respondido_por)

    def get_dados_sigilosos(self, usuario_autorizado: bool = False) -> dict:
        """Retorna dados do denunciante (apenas para autorizados - RN-OUV-030)."""
        if not usuario_autorizado:
            raise AcessoNegadoError("Acesso aos dados do denunciante restrito")
        if not self.cidadao:
            return {}
        return self.cidadao.para_exibicao()


@dataclass
class PedidoLai(ManifestacaoBase):
    """Pedido de Acesso à Informação (LAI - Lei 12.527/2011).

    RN-OUV-003: prazo 20 dias, prorrogável por 10.
    """

    informacao_solicitada: str = ""
    fundamentacao: str = ""
    nivel_sigilo: NivelSigilo = NivelSigilo.PUBLICO
    fundamentacao_sigilo: str = ""
    dados_pessoais_terceiros: bool = False
    formato_resposta: str = "digital"
    is_recurso: bool = False
    pedido_original_id: str | None = None
    decisao_recurso: str = ""
    data_decisao_recurso: date | None = None
    resposta: str = ""
    forma_resposta: FormaResposta | None = None
    data_resposta: date | None = None
    respondido_por: str = ""

    def validar(self) -> None:
        super().validar()
        if self.tipo != TipoManifestacao.PEDIDO_ACESSO_INFORMACAO:
            self.tipo = TipoManifestacao.PEDIDO_ACESSO_INFORMACAO
        if not self.informacao_solicitada:
            raise RegraNegocioError("Informação solicitada é obrigatória no pedido LAI")
        if not self.fundamentacao:
            raise RegraNegocioError("Fundamentação é obrigatória no pedido LAI")
        if self.nivel_sigilo != NivelSigilo.PUBLICO and not self.fundamentacao_sigilo:
            raise RegraNegocioError(
                "Fundamentação do sigilo é obrigatória para informações não públicas"
            )

    def classificar_sigilo(self, nivel: NivelSigilo, fundamentacao: str, usuario: str) -> None:
        """Classifica nível de sigilo da informação solicitada."""
        self.nivel_sigilo = nivel
        self.fundamentacao_sigilo = fundamentacao
        self.updated_at = datetime.utcnow()
        self.updated_by = usuario

    def interpor_recurso(self, pedido_original_id: str) -> PedidoLai:
        """Cria recurso de pedido negado (LAI Art. 15)."""
        recurso = PedidoLai(
            tipo=TipoManifestacao.PEDIDO_ACESSO_INFORMACAO,
            assunto=f"Recurso - {self.assunto}",
            descricao=self.descricao,
            cidadao=self.cidadao,
            orgao_destino=self.orgao_destino,
            setor_responsavel=self.setor_responsavel,
            informacao_solicitada=self.informacao_solicitada,
            fundamentacao=f"RECURSO: {self.fundamentacao}",
            is_recurso=True,
            pedido_original_id=pedido_original_id,
            created_by=self.created_by,
        )
        recurso.validar()
        return recurso

    def decidir_recurso(self, deferido: bool, fundamentacao: str, usuario: str) -> None:
        """Decide sobre recurso interposto (LAI Art. 15).

        A decisão é um ato administrativo terminal. O recurso nasce em
        ``REGISTRADA`` e nem sempre passa por ``RESPONDIDA`` — o fluxo de
        análise de um pedido de acesso não obriga o registro de uma resposta
        formal antes da decisão. Como apenas ``RESPONDIDA`` alcança
        ``CONCLUIDA``/``ARQUIVADA`` na máquina de estados, exigir essa
        passagem produziria um ``EstadoInvalidoError`` indevido.

        Por isso a conclusão é aplicada em um passo, a partir do estado atual.
        """
        if not self.is_recurso:
            raise RegraNegocioError("Este pedido não é um recurso")
        self.decisao_recurso = "deferido" if deferido else "indeferido"
        self.fundamentacao_sigilo = fundamentacao
        self.data_decisao_recurso = date.today()
        self.updated_at = datetime.utcnow()
        self.updated_by = usuario
        self.status = (
            StatusManifestacao.CONCLUIDA if deferido else StatusManifestacao.ARQUIVADA
        )

    def registrar_resposta(self, resposta: str, forma: FormaResposta, respondido_por: str) -> None:
        """Registra resposta ao solicitante."""
        if self.status not in (
            StatusManifestacao.EM_TRATAMENTO,
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
        ):
            raise EstadoInvalidoError("Só é possível responder pedidos em tratamento")
        self.resposta = resposta
        self.forma_resposta = forma
        self.data_resposta = date.today()
        self.respondido_por = respondido_por
        self.alterar_status(StatusManifestacao.RESPONDIDA, respondido_por)


__all__ = [
    "Prioridade",
    "ManifestacaoBase",
    "Manifestacao",
    "Denuncia",
    "PedidoLai",
]
