"""Use cases de PCASP, lançamentos e conciliação (DOM-CON)."""

from __future__ import annotations

from dataclasses import dataclass

from . import interfaces as ports
from ..domain.entities.conta import ContaContabil
from ..domain.entities.lancamento import (
    ConciliacaoContabil,
    LancamentoContabil,
    Partida,
    TipoPartida,
)


@dataclass
class CriarContaInput:
    """DTO de criação de conta PCASP."""

    codigo: str
    nome: str
    classe: str = ""
    tipo: str = "analitica"
    natureza: str = "devedora"
    autor_id: str = ""


class CriarContaUseCase:
    """Cria conta contábil (RN-CON-010)."""

    def __init__(self, repo: ports.RepositorioContaContabil) -> None:
        self._repo = repo

    def execute(self, dto: CriarContaInput) -> ContaContabil:
        """Executa a criação."""
        from ..domain.exceptions import RegraNegocioError

        if not dto.codigo or not dto.nome:
            raise RegraNegocioError("Código e nome são obrigatórios (RN-CON-010)")
        if self._repo.get_by_codigo(dto.codigo) is not None:
            raise RegraNegocioError(f"Conta '{dto.codigo}' já existe (RN-CON-010)")
        conta = ContaContabil(codigo=dto.codigo, nome=dto.nome, classe=dto.classe,
                              tipo=dto.tipo, natureza_saldo=dto.natureza,
                              aceita_lancamento=(dto.tipo == "analitica"),
                              created_by=dto.autor_id)
        return self._repo.save(conta)


@dataclass
class PartidaInput:
    """DTO de partida dobrada."""

    conta_id: str
    codigo_conta: str
    tipo: str
    valor: float


@dataclass
class LancarInput:
    """DTO de lançamento contábil."""

    exercicio: int
    historico: str
    partidas: list
    origem: str = ""
    origem_id: str = ""
    autor_id: str = ""


class LancarContabilUseCase:
    """Registra lançamento por partidas dobradas (RN-CON-040)."""

    def __init__(self, lancamentos: ports.RepositorioLancamento,
                 contas: ports.RepositorioContaContabil) -> None:
        self._lancamentos = lancamentos
        self._contas = contas

    def execute(self, dto: LancarInput) -> LancamentoContabil:
        """Executa o lançamento."""
        from ..domain.exceptions import RegraNegocioError

        if len(dto.partidas) < 2:
            raise RegraNegocioError("Lançamento exige ao menos 2 partidas")
        partidas: list[Partida] = []
        for p in dto.partidas:
            conta = self._contas.get_by_id(p.conta_id)
            if conta is None:
                raise RegraNegocioError(f"Conta {p.codigo_conta} inválida")
            if not conta.pode_receber_lancamento():
                raise RegraNegocioError(f"Conta {p.codigo_conta} não aceita lançamento")
            partidas.append(Partida(conta_id=p.conta_id, codigo_conta=p.codigo_conta,
                                    tipo=TipoPartida(p.tipo), valor=p.valor))
        lanc = LancamentoContabil(exercicio=dto.exercicio, historico=dto.historico,
                                  origem=dto.origem, origem_id=dto.origem_id,
                                  partidas=partidas, created_by=dto.autor_id)
        lanc.lancar()
        return self._lancamentos.save(lanc)


@dataclass
class ConciliarInput:
    """DTO de conciliação contábil."""

    conta_id: str
    codigo_conta: str
    ano: int
    mes: int
    saldo_contabil: float
    saldo_extrato: float
    autor_id: str = ""


class ConciliarContaUseCase:
    """Concilia conta (saldo contábil × extrato)."""

    def __init__(self, repo: ports.RepositorioConciliacao) -> None:
        self._repo = repo

    def execute(self, dto: ConciliarInput, justificativa: str = "") -> ConciliacaoContabil:
        """Executa a conciliação."""
        conc = ConciliacaoContabil(conta_id=dto.conta_id, codigo_conta=dto.codigo_conta,
                                   competencia_ano=dto.ano, competencia_mes=dto.mes,
                                   saldo_contabil=dto.saldo_contabil,
                                   saldo_extrato=dto.saldo_extrato,
                                   created_by=dto.autor_id)
        try:
            conc.conciliar()
        except Exception:
            if not justificativa:
                raise
            conc.marcar_divergente(justificativa)
        return self._repo.save(conc)


__all__ = [
    "CriarContaInput", "CriarContaUseCase",
    "PartidaInput", "LancarInput", "LancarContabilUseCase",
    "ConciliarInput", "ConciliarContaUseCase",
]
