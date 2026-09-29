"""Casos de uso do DOM-OBR — despesas financeiras da obra (RN-OBR-006)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..domain.entities import DespesaObra, SituacaoObra
from . import interfaces as ports
from .conversores import tipo_despesa
from .use_cases_medicao import recalcular_avanco


@dataclass
class RegistrarDespesaInput:
    """DTO de registro de despesa financeira de obra (RN-OBR-006)."""

    obra_id: str = ""
    medicao_id: str = ""
    descricao: str = ""
    tipo: str = "medicao"
    valor: float = 0.0
    data: date | None = None
    documento: str = ""
    credor: str = ""
    observacao: str = ""
    autor_id: str = ""


class RegistrarDespesaUseCase:
    """Registra a despesa e recompõe o avanço financeiro da obra (RN-OBR-006).

    A despesa não pode ultrapassar o saldo medido e ainda não pago: o município
    não desembolsa valor superior ao fisicamente medido na obra.
    """

    def __init__(
        self,
        repo: ports.RepositorioDespesa,
        obras: ports.RepositorioObra,
        medicoes: ports.RepositorioMedicao,
    ) -> None:
        self._repo = repo
        self._obras = obras
        self._medicoes = medicoes

    def execute(self, dto: RegistrarDespesaInput) -> DespesaObra:
        """Executa o registro da despesa."""
        from ..domain.exceptions import (
            MedicaoNaoEncontradaError,
            ObraNaoEncontradaError,
            RegraNegocioError,
        )

        obra = self._obras.get_by_id(dto.obra_id)
        if obra is None:
            raise ObraNaoEncontradaError("Obra não encontrada para a despesa")
        if obra.situacao in (SituacaoObra.PLANEJADA, SituacaoObra.EM_LICITACAO):
            raise RegraNegocioError(
                "Somente obra contratada ou em execução registra despesa (RN-OBR-006)"
            )
        if dto.medicao_id and self._medicoes.get_by_id(dto.medicao_id) is None:
            raise MedicaoNaoEncontradaError("Medição vinculada não encontrada (RN-OBR-006)")

        if obra.saldo_a_pagar <= 0:
            raise RegraNegocioError(
                "Não há valor medido disponível para pagamento nesta obra (RN-OBR-006)"
            )
        if dto.valor > obra.saldo_a_pagar:
            raise RegraNegocioError(
                f"Despesa excede o saldo medido a pagar (R$ {obra.saldo_a_pagar:.2f}) "
                "(RN-OBR-006)"
            )

        despesa = DespesaObra(
            obra_id=dto.obra_id,
            medicao_id=dto.medicao_id,
            descricao=dto.descricao,
            tipo=tipo_despesa(dto.tipo),
            valor=dto.valor,
            data=dto.data or date.today(),
            documento=dto.documento,
            credor=dto.credor,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        despesa.validar()
        despesa = self._repo.save(despesa)

        recalcular_avanco(
            obra,
            self._medicoes.list_by_obra(obra.id),
            self._repo.list_by_obra(obra.id),
        )
        self._obras.save(obra)
        return despesa


class ExcluirDespesaUseCase:
    """Exclui (soft-delete) uma despesa e recompõe o avanço da obra."""

    def __init__(
        self,
        repo: ports.RepositorioDespesa,
        obras: ports.RepositorioObra,
        medicoes: ports.RepositorioMedicao,
    ) -> None:
        self._repo = repo
        self._obras = obras
        self._medicoes = medicoes

    def execute(self, despesa_id: str) -> DespesaObra:
        """Executa a exclusão lógica da despesa."""
        from ..domain.exceptions import DespesaNaoEncontradaError

        despesa = self._repo.get_by_id(despesa_id)
        if despesa is None:
            raise DespesaNaoEncontradaError("Despesa não encontrada para exclusão")
        despesa.excluir()
        despesa = self._repo.save(despesa)

        obra = self._obras.get_by_id(despesa.obra_id)
        if obra is not None:
            recalcular_avanco(
                obra,
                self._medicoes.list_by_obra(obra.id),
                self._repo.list_by_obra(obra.id),
            )
            self._obras.save(obra)
        return despesa


__all__ = ["RegistrarDespesaInput", "RegistrarDespesaUseCase", "ExcluirDespesaUseCase"]
