"""Use cases de empenho/liquidação/pagamento (DOM-CON)."""

from __future__ import annotations

from dataclasses import dataclass

from . import interfaces as ports
from ..domain.entities.empenho import Empenho, TipoEmpenho
from ..domain.entities.liquidacao import Liquidacao
from ..domain.entities.pagamento import Pagamento


@dataclass
class EmitirEmpenhoInput:
    """DTO de emissão de empenho."""

    exercicio: int
    numero: str
    valor: float
    favorecido_nome: str = ""
    descricao: str = ""
    tipo: str = "ordinario"
    autor_id: str = ""


class EmitirEmpenhoUseCase:
    """Emite empenho com baixa direta no saldo (RN-CON-001/002).

    Integração DOM-ORC → DOM-CON: recebe dotação já validada pelo
    chamador (endpoint) e debita via ``dotacao.empenhar_direto``.
    """

    def __init__(self, empenhos: ports.RepositorioEmpenho) -> None:
        self._empenhos = empenhos

    def execute(self, dto: EmitirEmpenhoInput, dotacao) -> Empenho:  # type: ignore[no-untyped-def]
        """Executa a emissão."""
        from ..domain.exceptions import RegraNegocioError

        if not dto.numero:
            raise RegraNegocioError("Número do empenho é obrigatório (RN-CON-001)")
        if dto.valor <= 0:
            raise RegraNegocioError("Valor do empenho deve ser maior que zero")
        if self._empenhos.get_by_numero_exercicio(dto.numero, dto.exercicio) is not None:
            raise RegraNegocioError("Empenho já existe (RN-CON-001)")
        dotacao.empenhar_direto(dto.valor)
        emp = Empenho(exercicio=dto.exercicio, numero=dto.numero,
                      dotacao_id=dotacao.id, favorecido_nome=dto.favorecido_nome,
                      tipo=TipoEmpenho(dto.tipo), descricao=dto.descricao,
                      valor_empenhado=dto.valor, created_by=dto.autor_id)
        return self._empenhos.save(emp)


class AnularEmpenhoUseCase:
    """Anula parcial/total do empenho (devolve saldo à dotação)."""

    def __init__(self, empenhos: ports.RepositorioEmpenho) -> None:
        self._empenhos = empenhos

    def execute(self, empenho_id: str, valor: float, dotacao, motivo: str = "") -> Empenho:  # type: ignore[no-untyped-def]
        """Executa a anulação."""
        from ..domain.exceptions import EmpenhoNaoEncontradoError

        emp = self._empenhos.get_by_id(empenho_id)
        if emp is None:
            raise EmpenhoNaoEncontradoError("Empenho não encontrado")
        emp.anular(valor, motivo)
        dotacao.anular_empenho(valor)
        return self._empenhos.save(emp)


class LiquidarEmpenhoUseCase:
    """Registra liquidação do empenho."""

    def __init__(self, empenhos: ports.RepositorioEmpenho,
                 liquidacoes: ports.RepositorioLiquidacao) -> None:
        self._empenhos = empenhos
        self._liquidacoes = liquidacoes

    def execute(self, empenho_id: str, valor: float, doc: str = "",
                autor_id: str = "") -> Liquidacao:
        """Executa a liquidação."""
        from ..domain.exceptions import EmpenhoNaoEncontradoError

        emp = self._empenhos.get_by_id(empenho_id)
        if emp is None:
            raise EmpenhoNaoEncontradoError("Empenho não encontrado")
        emp.liquidar(valor)
        self._empenhos.save(emp)
        liq = Liquidacao(empenho_id=empenho_id, valor=valor, documento_fiscal=doc,
                         created_by=autor_id)
        liq.confirmar()
        return self._liquidacoes.save(liq)


class PagarLiquidacaoUseCase:
    """Registra pagamento de liquidação confirmada."""

    def __init__(self, empenhos: ports.RepositorioEmpenho,
                 liquidacoes: ports.RepositorioLiquidacao,
                 pagamentos: ports.RepositorioPagamento) -> None:
        self._empenhos = empenhos
        self._liquidacoes = liquidacoes
        self._pagamentos = pagamentos

    def execute(self, liquidacao_id: str, valor: float,
                conta: str = "", autor_id: str = "") -> Pagamento:
        """Executa o pagamento."""
        from ..domain.exceptions import LiquidacaoNaoEncontradaError

        liq = self._liquidacoes.get_by_id(liquidacao_id)
        if liq is None:
            raise LiquidacaoNaoEncontradaError("Liquidação não encontrada")
        from ..domain.entities.liquidacao import StatusLiquidacao

        if liq.status != StatusLiquidacao.CONFIRMADA:
            from ..domain.exceptions import RegraNegocioError

            raise RegraNegocioError("Pagamento exige liquidação confirmada (RN-CON-030)")
        emp = self._empenhos.get_by_id(liq.empenho_id)
        if emp is None:
            from ..domain.exceptions import EmpenhoNaoEncontradoError

            raise EmpenhoNaoEncontradoError("Empenho não encontrado")
        emp.pagar(valor)
        self._empenhos.save(emp)
        pag = Pagamento(liquidacao_id=liquidacao_id, empenho_id=emp.id,
                        valor=valor, conta_bancaria=conta, created_by=autor_id)
        pag.efetivar()
        return self._pagamentos.save(pag)


__all__ = [
    "EmitirEmpenhoInput", "EmitirEmpenhoUseCase", "AnularEmpenhoUseCase",
    "LiquidarEmpenhoUseCase", "PagarLiquidacaoUseCase",
]
