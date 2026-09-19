"""Use Case: Restituir Valor Glosado.

Use case para restituir o valor glosado de uma prestação de contas.
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
class RestituicaPrestacaoInputDTO:
    """DTO de entrada para restituição de prestação de contas."""

    diaria_id: str = ""
    autor_id: str = ""


@dataclass
class RestituicaPrestacaoOutputDTO:
    """DTO de saída para restituição de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_glosado: float
    valor_liquido: float
    data_restituicao: datetime


class RestituirPrestacaoUseCase:
    """Caso de uso para restituir valor glosado.
    
    RN-DIA-017: Restituição requer:
    - Diária em estado PAGA
    - Prestação de contas em estado GLOSADA
    """

    def __init__(self, repositorio_diaria: RepositorioDiaria, repositorio_prestacao: RepositorioPrestacaoContas):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: RestituicaPrestacaoInputDTO) -> RestituicaPrestacaoOutputDTO:
        """Executa a restituição do valor glosado."""
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
            raise RegraNegocioError(f"Diária deve estar em estado PAGA para restituir (status atual: {diaria.status.value})")
        
        # Validar status da prestação
        if prestacao.status != "glosa":
            raise RegraNegocioError(f"Prestação de contas deve estar em estado GLOSADA para restituição (status atual: {prestacao.status})")
        
        # Validar valor glosado
        if prestacao.valor_glosado <= 0:
            raise RegraNegocioError("Não há valor glosado para restituir")
        
        # Restituir
        prestacao.restituir()
        prestacao_salva = self._repo_prestacao.save(prestacao)
        
        return RestituicaPrestacaoOutputDTO(
            id=prestacao_salva.id,
            diaria_id=prestacao_salva.diaria_id,
            status=prestacao_salva.status,
            valor_glosado=prestacao_salva.valor_glosado,
            valor_liquido=prestacao_salva.valor_liquido,
            data_restituicao=prestacao_salva.data_restituicao,
        )
