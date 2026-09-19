"""Use Case: Criar Diária.

Baseado nas regras de negócio RN-DIA-001 a RN-DIA-004.
"""

from dataclasses import dataclass
from datetime import datetime

from ...domain.entities import CategoriaDiaria, Diaria, StatusDiaria, Viagem
from ...domain.exceptions import (
    DiariaNaoEncontradaError,
    DiariaJaTerminadaError,
    RegraNegocioError,
    ValidacaoDiariaError,
    ViagemNaoEncontradaError,
)
from ..interfaces import RepositorioDiaria, RepositorioViagem


@dataclass
class CriarDiariaInputDTO:
    """DTO de entrada para criação de diária."""

    viagem_id: str
    servidor_id: str
    dota_id: str
    categoria: str
    descricao: str
    data_inicio: str | None = None
    data_fim: str | None = None
    valor_diaria: float = 0.0
    valor_total: float = 0.0
    created_by: str = ""


@dataclass
class CriarDiariaOutputDTO:
    """DTO de saída para criação de diária."""

    id: str
    viagem_id: str
    servidor_id: str
    dota_id: str
    categoria: str
    descricao: str
    status: str
    valor_diaria: float
    valor_total: float
    created_at: datetime


class CriarDiariaUseCase:
    """Caso de uso para criar uma diária.

    RN-DIA-001: A diária é criada com status SOLICITADA.
    RN-DIA-002: A diária deve estar associada a uma viagem válida.
    """

    def __init__(
        self,
        repositorio_diaria: RepositorioDiaria,
        repositorio_viagem: RepositorioViagem,
    ):
        self._repo_diaria = repositorio_diaria
        self._repo_viagem = repositorio_viagem

    def execute(self, dto: CriarDiariaInputDTO) -> CriarDiariaOutputDTO:
        """Executa o caso de uso."""
        # Validar viagem existente
        viagem = self._repo_viagem.get_by_id(dto.viagem_id)
        if not viagem:
            raise ViagemNaoEncontradaError(f"Viagem {dto.viagem_id} não encontrada")

        # Validar categoria
        try:
            categoria = CategoriaDiaria(dto.categoria)
        except ValueError:
            raise ValidacaoDiariaError(
                f"Categoria inválida: {dto.categoria}"
            )

        # Criar entidade
        diaria = Diaria(
            viagem_id=dto.viagem_id,
            servidor_id=dto.servidor_id,
            dota_id=dto.dota_id,
            categoria=categoria,
            descricao=dto.descricao,
            data_inicio=datetime.strptime(dto.data_inicio, "%Y-%m-%d") if dto.data_inicio else None,
            data_fim=datetime.strptime(dto.data_fim, "%Y-%m-%d") if dto.data_fim else None,
            valor_diaria=dto.valor_diaria,
            valor_total=dto.valor_total,
            status=StatusDiaria.SOLICITADA,
            created_by=dto.created_by,
            created_at=datetime.utcnow(),
        )

        # Persistir
        diaria_salva = self._repo_diaria.save(diaria)

        return CriarDiariaOutputDTO(
            id=diaria_salva.id,
            viagem_id=diaria_salva.viagem_id,
            servidor_id=diaria_salva.servidor_id,
            dota_id=diaria_salva.dota_id,
            categoria=diaria_salva.categoria.value,
            descricao=diaria_salva.descricao,
            status=diaria_salva.status.value,
            valor_diaria=diaria_salva.valor_diaria,
            valor_total=diaria_salva.valor_total,
            created_at=diaria_salva.created_at,
        )
