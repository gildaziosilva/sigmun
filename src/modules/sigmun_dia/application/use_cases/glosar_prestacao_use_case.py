"""Use Case: Glosar Prestação de Contas.

Use case para glosar uma prestação de contas de diária.
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
class GlosagemPrestacaoInputDTO:
    """DTO de entrada para glosagem de prestação de contas."""

    diaria_id: str = ""
    motivo: str = ""
    valor_glosado: float = 0.0
    autor_id: str = ""


@dataclass
class GlosagemPrestacaoOutputDTO:
    """DTO de saída para glosagem de prestação de contas."""

    id: str
    diaria_id: str
    status: str
    valor_glosado: float
    valor_liquido: float
    motivo_glosa: str
    data_glosa: datetime


class GlosarPrestacaoUseCase:
    """Caso de uso para glosar uma prestação de contas.
    
    RN-DIA-016: Glosa de prestação requer:
    - Diária em estado PAGA
    - Prestação de contas aberta
    - Motivo da glosa (obrigatório)
    - Valor glosado (0 = glosa total)
    """

    def __init__(self, repositorio_diaria: RepositorioDiaria, repositorio_prestacao: RepositorioPrestacaoContas):
        self._repo_diaria = repositorio_diaria
        self._repo_prestacao = repositorio_prestacao

    def execute(self, dto: GlosagemPrestacaoInputDTO) -> GlosagemPrestacaoOutputDTO:
        """Executa a glosagem da prestação de contas."""
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
            raise RegraNegocioError(f"Diária deve estar em estado PAGA para glosar prestação (status atual: {diaria.status.value})")
        
        # Validar status da prestação
        if prestacao.status != "aberta":
            raise RegraNegocioError(f"Prestação de contas deve estar aberta para glosa (status atual: {prestacao.status})")
        
        # Validar motivo
        if not dto.motivo:
            raise RegraNegocioError("Motivo da glosa é obrigatório (RN-DIA-016)")
        
        # Validar valor
        if dto.valor_glosado < 0:
            raise RegraNegocioError("Valor glosado não pode ser negativo")
        if dto.valor_glosado > prestacao.valor_apresentado:
            raise RegraNegocioError(f"Valor glosado ({dto.valor_glosado}) não pode exceder valor apresentado ({prestacao.valor_apresentado})")
        
        # Glosar prestação
        prestacao.glosar(motivo=dto.motivo, valor_glosado=dto.valor_glosado)
        prestacao_salva = self._repo_prestacao.save(prestacao)
        
        return GlosagemPrestacaoOutputDTO(
            id=prestacao_salva.id,
            diaria_id=prestacao_salva.diaria_id,
            status=prestacao_salva.status,
            valor_glosado=prestacao_salva.valor_glosado,
            valor_liquido=prestacao_salva.valor_liquido,
            motivo_glosa=prestacao_salva.motivo_glosa,
            data_glosa=prestacao_salva.data_glosa,
        )
