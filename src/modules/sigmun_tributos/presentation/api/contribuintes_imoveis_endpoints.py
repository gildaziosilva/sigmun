"""Endpoints de contribuintes e imóveis (DOM-TRI)."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_tributos.application.interfaces import (
    RepositorioContribuinte,
    RepositorioImovel,
)
from src.modules.sigmun_tributos.application.use_cases import (
    CadastrarContribuinteInput,
    CadastrarContribuinteUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
)
from src.modules.sigmun_tributos.domain.exceptions import (
    ContribuinteNaoEncontradoError,
    DomTriDomainError,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_contribuinte_repository import (
    SQLAlchemyContribuinteRepository,
)
from src.modules.sigmun_tributos.infrastructure.repositories.sqlalchemy_imovel_repository import (
    SQLAlchemyImovelRepository,
)
from src.modules.sigmun_tributos.presentation.schemas.tri_schemas import (
    ContribuinteCreateRequest,
    ContribuinteResponse,
    ImovelCreateRequest,
    ImovelResponse,
)

router = APIRouter(prefix="/api/v1/tri", tags=["Administracao Tributaria"])


def get_contribuinte_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioContribuinte:
    """Fabrica de repositório de contribuintes."""
    return SQLAlchemyContribuinteRepository(session)


def get_imovel_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioImovel:
    """Fabrica de repositório de imóveis."""
    return SQLAlchemyImovelRepository(session)


def _to_contribuinte(contribuinte) -> ContribuinteResponse:
    return ContribuinteResponse(
        id=contribuinte.id, tipo=contribuinte.tipo.value, nome=contribuinte.nome,
        cpf_cnpj=contribuinte.cpf_cnpj,
        inscricao_municipal=contribuinte.inscricao_municipal,
        email=contribuinte.email, telefone=contribuinte.telefone,
        endereco=contribuinte.endereco, status=contribuinte.status.value,
        created_at=contribuinte.created_at, updated_at=contribuinte.updated_at,
    )


def _to_imovel(imovel) -> ImovelResponse:
    return ImovelResponse(
        id=imovel.id, contribuinte_id=imovel.contribuinte_id,
        inscricao_imobiliaria=imovel.inscricao_imobiliaria,
        logradouro=imovel.logradouro, numero=imovel.numero, bairro=imovel.bairro,
        cidade=imovel.cidade, uf=imovel.uf, cep=imovel.cep,
        area_terreno=imovel.area_terreno, area_construida=imovel.area_construida,
        valor_venal=imovel.valor_venal, aliquota=imovel.aliquota,
        status=imovel.status.value, created_at=imovel.created_at,
    )


@router.post("/contribuintes", status_code=201)
def cadastrar_contribuinte(
    payload: ContribuinteCreateRequest,
    repo: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
):
    """Cadastra um contribuinte."""
    try:
        contribuinte = CadastrarContribuinteUseCase(repo).execute(
            CadastrarContribuinteInput(
                tipo=payload.tipo, nome=payload.nome, cpf_cnpj=payload.cpf_cnpj,
                inscricao_municipal=payload.inscricao_municipal,
                email=payload.email, telefone=payload.telefone,
                endereco=payload.endereco, autor_id=payload.created_by,
            )
        )
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_contribuinte(contribuinte)


@router.get("/contribuintes")
def listar_contribuintes(
    repo: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista contribuintes paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_contribuinte(c) for c in itens]


@router.get("/contribuintes/{contribuinte_id}")
def obter_contribuinte(
    contribuinte_id: str,
    repo: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
):
    """Obtém um contribuinte por id."""
    contribuinte = repo.get_by_id(contribuinte_id)
    if contribuinte is None:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return _to_contribuinte(contribuinte)


@router.post("/imoveis", status_code=201)
def cadastrar_imovel(
    payload: ImovelCreateRequest,
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    contribuintes: Annotated[RepositorioContribuinte, Depends(get_contribuinte_repo)],
):
    """Cadastra um imóvel para IPTU."""
    try:
        imovel = CadastrarImovelUseCase(repo, contribuintes).execute(
            CadastrarImovelInput(
                contribuinte_id=payload.contribuinte_id,
                inscricao_imobiliaria=payload.inscricao_imobiliaria,
                logradouro=payload.logradouro, numero=payload.numero,
                bairro=payload.bairro, cidade=payload.cidade, uf=payload.uf,
                cep=payload.cep, area_terreno=payload.area_terreno,
                area_construida=payload.area_construida,
                valor_venal=payload.valor_venal, aliquota=payload.aliquota,
                autor_id=payload.created_by,
            )
        )
    except ContribuinteNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomTriDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_imovel(imovel)


@router.get("/imoveis")
def listar_imoveis(
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Lista imóveis paginados."""
    itens = repo.list_all(page=page, page_size=page_size)
    return [_to_imovel(i) for i in itens]


@router.get("/imoveis/{imovel_id}")
def obter_imovel(
    imovel_id: str,
    repo: Annotated[RepositorioImovel, Depends(get_imovel_repo)],
):
    """Obtém um imóvel por id."""
    imovel = repo.get_by_id(imovel_id)
    if imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return _to_imovel(imovel)


__all__ = ["router"]