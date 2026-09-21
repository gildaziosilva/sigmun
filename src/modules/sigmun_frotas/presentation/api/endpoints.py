"""Endpoints do DOM-FRO — Gestão de Frota."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_frotas.application.interfaces import (
    RepositorioAbastecimento,
    RepositorioManutencao,
    RepositorioRota,
    RepositorioVeiculo,
)
from src.modules.sigmun_frotas.application.use_cases import (
    AbrirManutencaoUseCase,
    BaixarVeiculoUseCase,
    CadastrarVeiculoInput,
    CadastrarVeiculoUseCase,
    ConcluirManutencaoUseCase,
    ConcluirRotaUseCase,
    RegistrarAbastecimentoInput,
    RegistrarAbastecimentoUseCase,
    RegistrarRotaInput,
    RegistrarRotaUseCase,
)
from src.modules.sigmun_frotas.domain.exceptions import (
    DomFroDomainError,
    ManutencaoNaoEncontradaError,
    RotaNaoEncontradaError,
    VeiculoNaoEncontradoError,
)
from src.modules.sigmun_frotas.infrastructure.repositories.sqlalchemy_veiculo_repository import (
    SQLAlchemyVeiculoRepository,
)
from src.modules.sigmun_frotas.infrastructure.repositories.sqlalchemy_rota_repository import (
    SQLAlchemyRotaRepository,
)
from src.modules.sigmun_frotas.infrastructure.repositories.sqlalchemy_operacional_repository import (
    SQLAlchemyAbastecimentoRepository,
    SQLAlchemyManutencaoRepository,
)
from src.modules.sigmun_frotas.presentation.schemas.fro_schemas import (
    AbastecimentoCreateRequest,
    AbastecimentoResponse,
    ManutencaoCreateRequest,
    ManutencaoResponse,
    RotaCreateRequest,
    RotaResponse,
    VeiculoCreateRequest,
    VeiculoResponse,
)

router = APIRouter(prefix="/api/v1/fro", tags=["Gestao de Frota"])


def get_veiculo_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioVeiculo:
    """Fabrica de repositório de veículos."""
    return SQLAlchemyVeiculoRepository(session)


def get_abastecimento_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioAbastecimento:
    """Fabrica de repositório de abastecimentos."""
    return SQLAlchemyAbastecimentoRepository(session)


def get_manutencao_repo(
    session: Annotated[Session, Depends(get_db)],
) -> RepositorioManutencao:
    """Fabrica de repositório de manutenções."""
    return SQLAlchemyManutencaoRepository(session)


def get_rota_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioRota:
    """Fabrica de repositório de rotas."""
    return SQLAlchemyRotaRepository(session)


def _to_veiculo(v) -> VeiculoResponse:
    return VeiculoResponse(
        id=v.id, placa=v.placa, chassi=v.chassi, renavam=v.renavam,
        marca=v.marca, modelo=v.modelo, ano_fabricacao=v.ano_fabricacao,
        ano_modelo=v.ano_modelo, tipo=v.tipo.value,
        combustivel=v.combustivel.value, capacidade=v.capacidade,
        odometro_atual=v.odometro_atual, status=v.status.value,
        unidade_id=v.unidade_id, created_at=v.created_at,
    )


def _to_abastecimento(a) -> AbastecimentoResponse:
    return AbastecimentoResponse(
        id=a.id, veiculo_id=a.veiculo_id, data=a.data,
        quantidade_litros=a.quantidade_litros,
        valor_unitario=a.valor_unitario, valor_total=a.valor_total,
        odometro=a.odometro, posto=a.posto,
        tipo_combustivel=a.tipo_combustivel.value, created_at=a.created_at,
    )


def _to_manutencao(m) -> ManutencaoResponse:
    return ManutencaoResponse(
        id=m.id, veiculo_id=m.veiculo_id, data_entrada=m.data_entrada,
        data_saida=m.data_saida, tipo=m.tipo.value, descricao=m.descricao,
        oficina=m.oficina, valor=m.valor, status=m.status.value,
        created_at=m.created_at,
    )


def _to_rota(r) -> RotaResponse:
    return RotaResponse(
        id=r.id, veiculo_id=r.veiculo_id, data=r.data, origem=r.origem,
        destino=r.destino, km_inicio=r.km_inicio, km_fim=r.km_fim,
        distancia_km=r.distancia_km, descricao=r.descricao,
        status=r.status.value, created_at=r.created_at,
    )

@router.post("/veiculos", status_code=201)
def cadastrar_veiculo(
    payload: VeiculoCreateRequest,
    repo: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Cadastra um veículo da frota."""
    try:
        veiculo = CadastrarVeiculoUseCase(repo).execute(
            CadastrarVeiculoInput(
                placa=payload.placa, chassi=payload.chassi,
                renavam=payload.renavam, marca=payload.marca,
                modelo=payload.modelo, ano_fabricacao=payload.ano_fabricacao,
                ano_modelo=payload.ano_modelo, tipo=payload.tipo,
                combustivel=payload.combustivel, capacidade=payload.capacidade,
                odometro_atual=payload.odometro_atual,
                unidade_id=payload.unidade_id, autor_id=payload.created_by,
            )
        )
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_veiculo(veiculo)


@router.get("/veiculos")
def listar_veiculos(
    repo: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista veículos paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_veiculo(v) for v in itens]


@router.get("/veiculos/{veiculo_id}")
def obter_veiculo(
    veiculo_id: str,
    repo: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Obtém um veículo por id."""
    veiculo = repo.get_by_id(veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return _to_veiculo(veiculo)


@router.post("/veiculos/{veiculo_id}/baixar")
def baixar_veiculo(
    veiculo_id: str,
    repo: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Baixa definitivamente um veículo."""
    try:
        veiculo = BaixarVeiculoUseCase(repo).execute(veiculo_id)
    except VeiculoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_veiculo(veiculo)


@router.post("/veiculos/{veiculo_id}/abastecimentos", status_code=201)
def registrar_abastecimento(
    veiculo_id: str,
    payload: AbastecimentoCreateRequest,
    repo: Annotated[RepositorioAbastecimento, Depends(get_abastecimento_repo)],
    veiculos: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Registra abastecimento de um veículo."""
    try:
        ab = RegistrarAbastecimentoUseCase(repo, veiculos).execute(
            RegistrarAbastecimentoInput(
                veiculo_id=veiculo_id,
                quantidade_litros=payload.quantidade_litros,
                valor_unitario=payload.valor_unitario,
                data=payload.data, odometro=payload.odometro,
                posto=payload.posto,
                tipo_combustivel=payload.tipo_combustivel,
                autor_id=payload.created_by,
            )
        )
    except VeiculoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_abastecimento(ab)


@router.get("/abastecimentos")
def listar_abastecimentos(
    repo: Annotated[RepositorioAbastecimento, Depends(get_abastecimento_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista abastecimentos paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_abastecimento(a) for a in itens]


@router.get("/veiculos/{veiculo_id}/abastecimentos")
def listar_abastecimentos_veiculo(
    veiculo_id: str,
    repo: Annotated[RepositorioAbastecimento, Depends(get_abastecimento_repo)],
):
    """Lista abastecimentos de um veículo."""
    itens = repo.list_by_veiculo(veiculo_id)
    return [_to_abastecimento(a) for a in itens]


@router.post("/veiculos/{veiculo_id}/manutencoes", status_code=201)
def abrir_manutencao(
    veiculo_id: str,
    payload: ManutencaoCreateRequest,
    repo: Annotated[RepositorioManutencao, Depends(get_manutencao_repo)],
    veiculos: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Abre manutenção e marca o veículo em manutenção."""
    try:
        m = AbrirManutencaoUseCase(repo, veiculos).execute(
            veiculo_id, descricao=payload.descricao, tipo=payload.tipo,
            oficina=payload.oficina, valor=payload.valor,
            data_entrada=payload.data_entrada, autor_id=payload.created_by,
        )
    except VeiculoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_manutencao(m)


@router.get("/manutencoes")
def listar_manutencoes(
    repo: Annotated[RepositorioManutencao, Depends(get_manutencao_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista manutenções paginadas."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_manutencao(m) for m in itens]


@router.post("/manutencoes/{manutencao_id}/concluir")
def concluir_manutencao(
    manutencao_id: str,
    repo: Annotated[RepositorioManutencao, Depends(get_manutencao_repo)],
    veiculos: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Conclui manutenção e reativa o veículo."""
    try:
        m = ConcluirManutencaoUseCase(repo, veiculos).execute(manutencao_id)
    except ManutencaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_manutencao(m)


@router.post("/veiculos/{veiculo_id}/rotas", status_code=201)
def registrar_rota(
    veiculo_id: str,
    payload: RotaCreateRequest,
    repo: Annotated[RepositorioRota, Depends(get_rota_repo)],
    veiculos: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Registra rota de um veículo."""
    try:
        r = RegistrarRotaUseCase(repo, veiculos).execute(
            RegistrarRotaInput(
                veiculo_id=veiculo_id, origem=payload.origem,
                destino=payload.destino, data=payload.data,
                km_inicio=payload.km_inicio, km_fim=payload.km_fim,
                descricao=payload.descricao, autor_id=payload.created_by,
            )
        )
    except VeiculoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_rota(r)


@router.get("/rotas")
def listar_rotas(
    repo: Annotated[RepositorioRota, Depends(get_rota_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista rotas paginadas."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_rota(r) for r in itens]


@router.post("/rotas/{rota_id}/concluir")
def concluir_rota(
    rota_id: str,
    repo: Annotated[RepositorioRota, Depends(get_rota_repo)],
    veiculos: Annotated[RepositorioVeiculo, Depends(get_veiculo_repo)],
):
    """Conclui uma rota e atualiza o odômetro do veículo."""
    try:
        r = ConcluirRotaUseCase(repo, veiculos).execute(rota_id)
    except (RotaNaoEncontradaError, VeiculoNaoEncontradoError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomFroDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_rota(r)


__all__ = ["router"]
