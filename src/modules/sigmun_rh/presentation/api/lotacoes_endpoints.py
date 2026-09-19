"""Endpoints de lotacoes (DOM-PES)."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.modules.sigmun_rh.application.interfaces import (
    RepositorioLotacao,
    RepositorioServidor,
)
from src.modules.sigmun_rh.application.use_cases_lotacao import (
    LotarServidorInput,
    LotarServidorUseCase,
    RemoverServidorInput,
    RemoverServidorUseCase,
)
from src.modules.sigmun_rh.domain.exceptions import DomPesDomainError
from src.modules.sigmun_rh.presentation.schemas.pes_operacionais_schemas import (
    LotacaoCreateRequest,
)

from .lotacoes import (
    get_lotacao_repo,
    get_servidor_repo2,
    lotacao_to_response,
    router_lotacoes,
)

router = router_lotacoes


@router.post("/lotacoes", status_code=201)
def lotar_servidor(
    payload: LotacaoCreateRequest,
    lotacoes: Annotated[RepositorioLotacao, Depends(get_lotacao_repo)],
    servidores: Annotated[RepositorioServidor, Depends(get_servidor_repo2)],
):
    """Lota servidor em unidade."""
    try:
        lotacao = LotarServidorUseCase(lotacoes, servidores).execute(
            LotarServidorInput(
                servidor_id=payload.servidor_id,
                unidade_id=payload.unidade_id,
                cargo_id=payload.cargo_id,
                data_inicio=payload.data_inicio,
                motivo=payload.motivo,
                autor_id=payload.created_by,
            )
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return lotacao_to_response(lotacao)


@router.post("/lotacoes/{lotacao_id}/encerrar")
def encerrar_lotacao(
    lotacao_id: str,
    repo: Annotated[RepositorioLotacao, Depends(get_lotacao_repo)],
):
    """Encerra lotacao vigente."""
    try:
        lotacao = RemoverServidorUseCase(repo).execute(
            RemoverServidorInput(lotacao_id=lotacao_id)
        )
    except DomPesDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return lotacao_to_response(lotacao)


__all__ = ["router"]
