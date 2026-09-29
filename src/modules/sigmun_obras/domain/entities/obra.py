"""Obra pública municipal do DOM-OBR — Obras e Infraestrutura.

RN-OBR-001: o número da obra é único no cadastro municipal.
RN-OBR-002: a obra obedece ao ciclo
    PLANEJADA -> EM_LICITACAO -> CONTRATADA -> EM_EXECUCAO -> CONCLUIDA,
    com SUSPENSA e CANCELADA disponíveis; obra CONCLUIDA é terminal.
RN-OBR-003: a contratação exige empresa, tipo de contratação e data de início
    prevista antes do início da execução.
RN-OBR-004: valores e percentuais de avanço são não negativos e o avanço
    financeiro não pode ultrapassar o avanço físico.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from uuid import uuid4

from .tipos import (
    FonteRecurso,
    SituacaoObra,
    TipoContratacao,
    TipoObra,
    validar_percentual,
    validar_valor,
)


@dataclass
class Obra:
    """Obra pública acompanhada quanto ao avanço físico e financeiro."""

    id: str = field(default_factory=lambda: str(uuid4()))
    numero: str = ""
    nome: str = ""
    descricao: str = ""
    tipo: TipoObra = field(default=TipoObra.OUTRO)
    situacao: SituacaoObra = field(default=SituacaoObra.PLANEJADA)
    tipo_contratacao: TipoContratacao = field(default=TipoContratacao.LICITACAO)
    fonte_recurso: FonteRecurso = field(default=FonteRecurso.ORCAMENTO_PROPRIO)
    valor_orcado: float = 0.0
    valor_contratado: float = 0.0
    valor_mediado: float = 0.0
    valor_pago: float = 0.0
    percentual_fisico: float = 0.0
    percentual_financeiro: float = 0.0
    empresa_contratada: str = ""
    numero_contrato: str = ""
    responsavel_tecnico: str = ""
    endereco: str = ""
    bairro: str = ""
    data_inicio_prevista: date | None = None
    data_fim_prevista: date | None = None
    data_inicio_real: date | None = None
    data_fim_real: date | None = None
    observacao: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None
    created_by: str = ""
    is_deleted: bool = False

    @property
    def saldo_a_executar(self) -> float:
        """Saldo físico-financeiro ainda não medido (RN-OBR-005)."""
        base = self.valor_contratado or self.valor_orcado
        return max(0.0, round(base - self.valor_mediado, 2))

    @property
    def saldo_a_pagar(self) -> float:
        """Saldo financeiro medido e ainda não pago (RN-OBR-006)."""
        return max(0.0, round(self.valor_mediado - self.valor_pago, 2))

    def iniciar_execucao(self, data: date | None = None) -> None:
        """Inicia a execução física da obra (RN-OBR-002, RN-OBR-003)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoObra.CONCLUIDA:
            raise RegraNegocioError("Obra concluída não pode voltar a execução (RN-OBR-002)")
        if self.situacao not in (SituacaoObra.CONTRATADA, SituacaoObra.SUSPENSA):
            raise RegraNegocioError(
                "Somente obra contratada (ou suspensa) pode iniciar execução (RN-OBR-002)"
            )
        if not self.empresa_contratada:
            raise RegraNegocioError(
                "Empresa contratada é obrigatória para iniciar execução (RN-OBR-003)"
            )
        if self.data_inicio_prevista is None:
            raise RegraNegocioError(
                "Data de início prevista é obrigatória para iniciar execução (RN-OBR-003)"
            )
        self.situacao = SituacaoObra.EM_EXECUCAO
        self.data_inicio_real = data or date.today()
        self.updated_at = datetime.utcnow()

    def suspender(self, motivo: str) -> None:
        """Suspende a execução da obra (RN-OBR-002)."""
        from ..exceptions import RegraNegocioError

        if self.situacao not in (SituacaoObra.EM_EXECUCAO, SituacaoObra.CONTRATADA):
            raise RegraNegocioError(
                "Somente obra em execução ou contratada pode ser suspensa (RN-OBR-002)"
            )
        self.situacao = SituacaoObra.SUSPENSA
        if motivo:
            self.observacao = motivo
        self.updated_at = datetime.utcnow()

    def concluir(self, data: date | None = None) -> None:
        """Conclui a obra, exigindo 100% do avanço físico (RN-OBR-005)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoObra.CONCLUIDA:
            raise RegraNegocioError("Obra já está concluída (RN-OBR-002)")
        if self.situacao not in (SituacaoObra.EM_EXECUCAO, SituacaoObra.SUSPENSA):
            raise RegraNegocioError(
                "Somente obra em execução ou suspensa pode ser concluída (RN-OBR-002)"
            )
        if self.percentual_fisico < 100.0:
            raise RegraNegocioError(
                "Obra só pode ser concluída com 100% do avanço físico registrado "
                "(RN-OBR-005)"
            )
        self.situacao = SituacaoObra.CONCLUIDA
        self.data_fim_real = data or date.today()
        self.updated_at = datetime.utcnow()

    def cancelar(self, motivo: str) -> None:
        """Cancela a obra (RN-OBR-002)."""
        from ..exceptions import RegraNegocioError

        if self.situacao == SituacaoObra.CONCLUIDA:
            raise RegraNegocioError("Obra concluída não pode ser cancelada (RN-OBR-002)")
        if self.situacao == SituacaoObra.CANCELADA:
            raise RegraNegocioError("Obra já está cancelada (RN-OBR-002)")
        self.situacao = SituacaoObra.CANCELADA
        if motivo:
            self.observacao = motivo
        self.updated_at = datetime.utcnow()

    def excluir(self) -> None:
        """Marca a obra como excluída (soft-delete)."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()

    def validar(self) -> None:
        """Valida as regras estruturais da obra (RN-OBR-001, RN-OBR-004)."""
        from ..exceptions import RegraNegocioError

        if not self.numero:
            raise RegraNegocioError("Número da obra é obrigatório (RN-OBR-001)")
        if not self.nome:
            raise RegraNegocioError("Nome da obra é obrigatório (RN-OBR-001)")

        validar_valor(self.valor_orcado, "Valor orçado")
        validar_valor(self.valor_contratado, "Valor contratado")
        validar_valor(self.valor_mediado, "Valor medido")
        validar_valor(self.valor_pago, "Valor pago")
        validar_percentual(self.percentual_fisico, "Avanço físico")
        validar_percentual(self.percentual_financeiro, "Avanço financeiro")

        if self.valor_contratado > self.valor_orcado > 0:
            raise RegraNegocioError(
                "Valor contratado não pode superar o valor orçado (RN-OBR-004)"
            )
        if self.valor_pago > self.valor_mediado:
            raise RegraNegocioError(
                "Valor pago não pode superar o valor medido (RN-OBR-006)"
            )
        if self.percentual_financeiro > self.percentual_fisico + 1e-9:
            raise RegraNegocioError(
                "Avanço financeiro não pode ultrapassar o avanço físico (RN-OBR-004)"
            )
        if (
            self.data_inicio_prevista
            and self.data_fim_prevista
            and self.data_inicio_prevista > self.data_fim_prevista
        ):
            raise RegraNegocioError(
                "Data de início prevista não pode ser posterior à de fim (RN-OBR-003)"
            )


__all__ = ["Obra"]
