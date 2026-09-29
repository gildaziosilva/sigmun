"""Casos de uso do DOM-OBR — medições físico-financeiras.

RN-OBR-005: a medição compõe o avanço da obra apenas quando APROVADA, e o
    valor medido não pode ultrapassar o valor contratado da obra.
RN-OBR-006: o total pago (despesas) nunca supera o total medido aprovado.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date

from ..domain.entities import (
    DespesaObra,
    MedicaoObra,
    Obra,
    SituacaoMedicao,
    SituacaoObra,
)
from . import interfaces as ports
from .conversores import situacao_obra, tipo_medicao  # noqa: F401


def recalcular_avanco(
    obra: Obra, medicoes: Sequence[MedicaoObra], despesas: Sequence[DespesaObra]
) -> None:
    """Recalcula o avanço físico-financeiro da obra a partir das medições.

    Regras aplicadas (RN-OBR-005, RN-OBR-006):
    - `valor_mediado` e `percentual_fisico` somam apenas as medições aprovadas;
    - `valor_pago` e `percentual_financeiro` somam apenas as despesas da obra;
    - o avanço financeiro é limitado ao avanço físico, pois não se paga o que
      não foi medido.
    """
    aprovadas = [m for m in medicoes if m.situacao == SituacaoMedicao.APROVADA]
    obra.valor_mediado = round(sum(m.valor_medido for m in aprovadas), 2)
    obra.percentual_fisico = round(sum(m.percentual_fisico for m in aprovadas), 2)

    obra.valor_pago = round(sum(float(getattr(d, "valor", 0.0)) for d in despesas), 2)
    base = obra.valor_contratado or obra.valor_orcado
    percentual_pago = round((obra.valor_pago / base) * 100, 2) if base > 0 else 0.0
    obra.percentual_financeiro = min(percentual_pago, obra.percentual_fisico)


@dataclass
class RegistrarMedicaoInput:
    """DTO de registro de medição físico-financeira (RN-OBR-005)."""

    obra_id: str = ""
    numero: str = ""
    tipo: str = "avanco"
    data: date | None = None
    percentual_fisico: float = 0.0
    valor_medido: float = 0.0
    responsavel_tecnico: str = ""
    observacao: str = ""
    autor_id: str = ""


class RegistrarMedicaoUseCase:
    """Registra uma medição de avanço em obra em execução (RN-OBR-005)."""

    def __init__(
        self,
        repo: ports.RepositorioMedicao,
        obras: ports.RepositorioObra,
        despesas: ports.RepositorioDespesa,
    ) -> None:
        self._repo = repo
        self._obras = obras
        self._despesas = despesas

    def execute(self, dto: RegistrarMedicaoInput) -> MedicaoObra:
        """Executa o registro da medição."""
        from ..domain.exceptions import (
            MedicaoJaRegistradaError,
            ObraNaoEncontradaError,
            RegraNegocioError,
        )

        obra = self._obras.get_by_id(dto.obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para a medição")
        if obra.situacao not in (SituacaoObra.EM_EXECUCAO, SituacaoObra.SUSPENSA):
            raise RegraNegocioError(
                "Somente obra em execução ou suspensa aceita medições (RN-OBR-005)"
            )
        if self._repo.get_by_numero_obra(dto.numero, dto.obra_id) is not None:
            raise MedicaoJaRegistradaError(
                "Já existe medição com este número nesta obra (RN-OBR-005)"
            )

        limite = obra.valor_contratado or obra.valor_orcado
        if dto.valor_medido > limite:
            raise RegraNegocioError(
                "Valor medido não pode superar o valor contratado da obra (RN-OBR-005)"
            )

        medicao = MedicaoObra(
            obra_id=dto.obra_id,
            numero=dto.numero,
            tipo=tipo_medicao(dto.tipo),
            data=dto.data or date.today(),
            percentual_fisico=dto.percentual_fisico,
            valor_medido=dto.valor_medido,
            responsavel_tecnico=dto.responsavel_tecnico,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        medicao.validar()
        return self._repo.save(medicao)


class AprovarMedicaoUseCase:
    """Aprova a medição e recompõe o avanço da obra (RN-OBR-005)."""

    def __init__(
        self,
        repo: ports.RepositorioMedicao,
        obras: ports.RepositorioObra,
        despesas: ports.RepositorioDespesa,
    ) -> None:
        self._repo = repo
        self._obras = obras
        self._despesas = despesas

    def execute(self, medicao_id: str, autor_id: str = "") -> MedicaoObra:
        """Executa a conferência e a aprovação da medição."""
        from ..domain.exceptions import MedicaoNaoEncontradaError, ObraNaoEncontradaError

        medicao = self._repo.get_by_id(medicao_id)
        if medicao is None:
            raise MedicaoNaoEncontradaError("Medição não encontrada para aprovação")

        medicao.conferir(autor_id)
        medicao.aprovar(autor_id)
        medicao = self._repo.save(medicao)

        obra = self._obras.get_by_id(medicao.obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra da medição não encontrada")
        recalcular_avanco(
            obra,
            self._repo.list_by_obra(obra.id),
            self._despesas.list_by_obra(obra.id),
        )
        self._obras.save(obra)
        return medicao


class GlosarMedicaoUseCase:
    """Glosa uma medição conferida (RN-OBR-005)."""

    def __init__(self, repo: ports.RepositorioMedicao) -> None:
        self._repo = repo

    def execute(self, medicao_id: str, motivo: str, autor_id: str = "") -> MedicaoObra:
        """Executa a glosa da medição."""
        from ..domain.exceptions import MedicaoNaoEncontradaError, RegraNegocioError

        medicao = self._repo.get_by_id(medicao_id)
        if medicao is None:
            raise MedicaoNaoEncontradaError("Medição não encontrada para glosa")
        if not motivo.strip():
            raise RegraNegocioError("Justificativa da glosa é obrigatória (RN-OBR-005)")
        medicao.glosar(motivo)
        return self._repo.save(medicao)


class CancelarMedicaoUseCase:
    """Cancela uma medição não aprovada (RN-OBR-005)."""

    def __init__(self, repo: ports.RepositorioMedicao) -> None:
        self._repo = repo

    def execute(self, medicao_id: str, motivo: str = "", autor_id: str = "") -> MedicaoObra:
        """Executa o cancelamento da medição."""
        from ..domain.exceptions import MedicaoNaoEncontradaError

        medicao = self._repo.get_by_id(medicao_id)
        if medicao is None:
            raise MedicaoNaoEncontradaError("Medição não encontrada para cancelamento")
        medicao.cancelar(motivo)
        return self._repo.save(medicao)


__all__ = [
    "RegistrarMedicaoInput",
    "RegistrarMedicaoUseCase",
    "AprovarMedicaoUseCase",
    "GlosarMedicaoUseCase",
    "CancelarMedicaoUseCase",
    "recalcular_avanco",
]
