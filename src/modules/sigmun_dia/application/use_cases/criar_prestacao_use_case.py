"""Use Case: Criar Prestação de Contas.

RN-DIA-009: Prestação de contas requer documento GDO anexado.
"""

from dataclasses import dataclass
from datetime import datetime

from ..interfaces import RepositorioDiaria, RepositorioPrestacaoContas
from ...domain.entities import PrestacaoContas
from ...domain.exceptions import RegraNegocioError


@dataclass
class CriarPrestacaoContasInputDTO:
    """DTO de entrada para criação de prestação de contas."""
    
    diaria_id: str = ""
    servidor_id: str = ""
    dota_id: str = ""
    documento_id: str = ""
    valor_previsto: float = 0.0
    valor_apresentado: float = 0.0
    data_vencimento: datetime | None = None
    autor_id: str = ""


@dataclass
class CriarPrestacaoContasOutputDTO:
    """DTO de saída para criação de prestação de contas."""
    
    id: str
    diaria_id: str
    servidor_id: str
    dota_id: str
    documento_id: str
    valor_previsto: float
    valor_apresentado: float
    valor_liquido: float
    status: str
    created_at: datetime


class CriarPrestacaoContasUseCase:
    """Caso de uso para criar uma prestação de contas.
    
    RN-DIA-009: Prestação de contas requer documento GDO anexado.
    """
    
    def __init__(self, repositorio_prestacao: RepositorioPrestacaoContas, repositorio_diaria: RepositorioDiaria):
        self._repo_prestacao = repositorio_prestacao
        self._repo_diaria = repositorio_diaria
    
    def execute(self, dto: CriarPrestacaoContasInputDTO) -> CriarPrestacaoContasOutputDTO:
        """Executa o caso de uso."""
        diaria = self._repo_diaria.get_by_id(dto.diaria_id)
        if not diaria:
            raise RegraNegocioError(f"Diária {dto.diaria_id} não encontrada")
        
        if not dto.documento_id:
            raise RegraNegocioError("Prestação de contas requer documento GDO anexado (RN-DIA-009)")
        
        if dto.status:
            raise RegraNegocioError("Não é possível especificar status na criação")
        
        prestacao = PrestacaoContas(
            diaria_id=dto.diaria_id,
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            data_vencimento=dto.data_vencimento,
            documento_id=dto.documento_id,
            valor_previsto=dto.valor_previsto,
            valor_apresentado=dto.valor_apresentado,
            valor_glosado=0.0,
            valor_liquido=dto.valor_apresentado,
            status="aberta",
            created_by=dto.autor_id,
        )
        
        prestacao_salva = self._repo_prestacao.save(prestacao)
        
        return CriarPrestacaoContasOutputDTO(
            id=prestacao_salva.id,
            diaria_id=prestacao_salva.diaria_id,
            servidor_id=prestacao_salva.servidor_id,
            dota_id=prestacao_salva.dota_id,
            documento_id=prestacao_salva.documento_id,
            valor_previsto=prestacao_salva.valor_previsto,
            valor_apresentado=prestacao_salva.valor_apresentado,
            valor_liquido=prestacao_salva.valor_liquido,
            status=prestacao_salva.status,
            created_at=prestacao_salva.created_at,
        )
