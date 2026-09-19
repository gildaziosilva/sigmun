"""Use Case: Aprovar Prestação de Contas.

Use case para aprovar uma prestação de contas de diária.
"""

from dataclasses import dataclass
from datetime import datetime

from ...domain.entities import PrestacaoContas
from ...domain.exceptions import (
    DiariaNaoEncontradaError,
    PrestacaoContasNaoEncontradaError,
    RegraNegocioError,
)
from ..interfaces import RepositorioDiaria, RepositorioPrestacaoContas


@dataclass
class AprovacaoPrestacaoInputDTO:
    """DTO de entrada para aprovação de prestação de contas."""

    diaria_id: str = ""
    autor_id: str = ""


@dataclass
class AprovacaoPrestacaoOutputDTO:
    """DTO de saída para aprovação de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_liquido: float
    data_aprovacao: datetime


class AprovarPrestacaoUseCase:
    """Caso de uso para aprovar uma prestação de contas.
    
    RN-DIA-015: Aprovação de prestação de contas requer:
    - Diária em estado PAGA
    - Prestação de contas aberta
    """

    def __init__(self, repositorio_diaria: RepositorioDiaria, repositorio_prestacao: RepositorioPrestacaoContas):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: AprovacaoPrestacaoInputDTO) -> AprovacaoPrestacaoOutputDTO:
        """Executa a aprovação da prestação de contas."""
        # Buscar diária
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise DiariaNaoEncontradaError(f"Diária {dto.diaria_id} não encontrada")
        
        # Buscar prestação de contas
        prestacao = self._repo_prestacao.get_by_diaria(dto.diaria_id)
        if not prestacao:
            raise PrestacaoContasNaoEncontradaError(f"Prestação de contas para diária {dto.diaria_id} não encontrada")
        
        # Validar status da diária
        if diaria.status != "paga":
            raise RegraNegocioError(f"Diária deve estar em estado PAGA para aprovar prestação (status atual: {diaria.status.value})")
        
        # Validar status da prestação
        if prestacao.status != "aberta":
            raise RegraNegocioError(f"Prestação de contas deve estar aberta para aprovação (status atual: {prestacao.status})")
        
        # Aprovar prestação
        prestacao.aprovar()
        prestacao_salva = self._repo_prestacao.save(prestacao)
        
        return AprovacaoPrestacaoOutputDTO(
            id=prestacao_salva.id,
            diaria_id=prestacao_salva.diaria_id,
            status=prestacao_salva.status,
            valor_liquido=prestacao_salva.valor_liquido,
            data_aprovacao=prestacao_salva.data_aprovacao,
        )
