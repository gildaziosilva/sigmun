"""Endpoints REST de Metadados Corporativos (DOM-MET)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_met.application.interfaces import (
    ClassificacaoRepositoryInterface,
    MetadadoRepositoryInterface,
    TaxonomiaRepositoryInterface,
    TermoTaxonomiaRepositoryInterface,
    ValorMetadadoRepositoryInterface,
)
from src.modules.sigmun_met.application.use_cases import (
    AtivarMetadadoUseCase,
    AtribuirValorMetadadoUseCase,
    AtualizarClassificacaoUseCase,
    AtualizarMetadadoUseCase,
    AtualizarTaxonomiaUseCase,
    AtualizarTermoUseCase,
    BuscarClassificacaoUseCase,
    BuscarMetadadoUseCase,
    BuscarTaxonomiaUseCase,
    BuscarTermoUseCase,
    BuscarValorMetadadoUseCase,
    CriarClassificacaoUseCase,
    CriarMetadadoUseCase,
    CriarTaxonomiaUseCase,
    CriarTermoUseCase,
    DeletarClassificacaoUseCase,
    DeletarMetadadoUseCase,
    DeletarTaxonomiaUseCase,
    DeletarTermoUseCase,
    DesativarMetadadoUseCase,
    RemoverValorMetadadoUseCase,
)
from src.modules.sigmun_met.domain.exceptions import (
    ClassificacaoJaExisteError,
    ClassificacaoNaoEncontradaError,
    CodigoInvalidoError,
    HierarquiaCiclicaError,
    MetadadoJaExisteError,
    MetadadoNaoEncontradoError,
    TaxonomiaJaExisteError,
    TaxonomiaNaoEncontradaError,
    TermoNaoEncontradoError,
    ValorMetadadoInvalidoError,
    ValorMetadadoNaoEncontradoError,
)
from src.modules.sigmun_met.infrastructure.repositories import (
    SqlAlchemyClassificacaoRepository,
    SqlAlchemyMetadadoRepository,
    SqlAlchemyTaxonomiaRepository,
    SqlAlchemyTermoTaxonomiaRepository,
    SqlAlchemyValorMetadadoRepository,
)
from src.modules.sigmun_met.presentation.schemas import (
    ClassificacaoCreateRequest,
    ClassificacaoListResponse,
    ClassificacaoResponse,
    ClassificacaoUpdateRequest,
    ErrorResponse,
    MetadadoCreateRequest,
    MetadadoListResponse,
    MetadadoResponse,
    MetadadoUpdateRequest,
    TaxonomiaCreateRequest,
    TaxonomiaListResponse,
    TaxonomiaResponse,
    TaxonomiaUpdateRequest,
    TermoCreateRequest,
    TermoListResponse,
    TermoResponse,
    TermoUpdateRequest,
    ValorMetadadoCreateRequest,
    ValorMetadadoListResponse,
    ValorMetadadoResponse,
    ValorMetadadoUpdateRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/met", tags=["Metadados Corporativos"])


# =============================================================================
# Dependency Injection
# =============================================================================


def get_metadado_repository(
    session: Annotated[Session, Depends(get_db)],
) -> MetadadoRepositoryInterface:
    return SqlAlchemyMetadadoRepository(session)


def get_valor_metadado_repository(
    session: Annotated[Session, Depends(get_db)],
) -> ValorMetadadoRepositoryInterface:
    return SqlAlchemyValorMetadadoRepository(session)


def get_classificacao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> ClassificacaoRepositoryInterface:
    return SqlAlchemyClassificacaoRepository(session)


def get_taxonomia_repository(
    session: Annotated[Session, Depends(get_db)],
) -> TaxonomiaRepositoryInterface:
    return SqlAlchemyTaxonomiaRepository(session)


def get_termo_repository(
    session: Annotated[Session, Depends(get_db)],
) -> TermoTaxonomiaRepositoryInterface:
    return SqlAlchemyTermoTaxonomiaRepository(session)

# =============================================================================
# Endpoints de Metadados
# =============================================================================


def _metadado_to_response(m) -> MetadadoResponse:
    return MetadadoResponse(
        id=m.id,
        codigo=m.codigo,
        nome=m.nome,
        descricao=m.descricao,
        tipo_dado=m.tipo_dado.value,
        obrigatorio=m.obrigatorio,
        multi_valor=m.multi_valor,
        aplicavel_a=m.aplicavel_a,
        valor_padrao=m.valor_padrao,
        status=m.status.value,
        created_at=m.created_at,
        updated_at=m.updated_at,
    )


@router.post(
    "/metadados",
    response_model=MetadadoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo metadado",
    responses={409: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def criar_metadado(
    payload: MetadadoCreateRequest,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> MetadadoResponse:
    use_case = CriarMetadadoUseCase(repo)
    try:
        metadado = use_case.execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao or "",
            tipo_dado=payload.tipo_dado.value,
            obrigatorio=payload.obrigatorio,
            multi_valor=payload.multi_valor,
            aplicavel_a=payload.aplicavel_a,
            valor_padrao=payload.valor_padrao or "",
        )
        return _metadado_to_response(metadado)
    except MetadadoJaExisteError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except (CodigoInvalidoError, ValueError) as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/metadados", response_model=MetadadoListResponse, summary="Lista metadados")
def listar_metadados(
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
    page: int = 0,
    page_size: int = 50,
    tipo_dado: str | None = None,
) -> MetadadoListResponse:
    use_case = BuscarMetadadoUseCase(repo)
    items, total = use_case.list_all(page=page, page_size=page_size, tipo_dado=tipo_dado)
    return MetadadoListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_metadado_to_response(m) for m in items],
    )


@router.get(
    "/metadados/{metadado_id}",
    response_model=MetadadoResponse,
    summary="Busca um metadado por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_metadado(
    metadado_id: str,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> MetadadoResponse:
    use_case = BuscarMetadadoUseCase(repo)
    try:
        return _metadado_to_response(use_case.get_by_id(metadado_id))
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/metadados/{metadado_id}",
    response_model=MetadadoResponse,
    summary="Atualiza um metadado",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atualizar_metadado(
    metadado_id: str,
    payload: MetadadoUpdateRequest,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> MetadadoResponse:
    use_case = AtualizarMetadadoUseCase(repo)
    try:
        metadado = use_case.execute(
            metadado_id=metadado_id,
            nome=payload.nome,
            descricao=payload.descricao,
            tipo_dado=payload.tipo_dado.value if payload.tipo_dado else None,
            obrigatorio=payload.obrigatorio,
            multi_valor=payload.multi_valor,
            aplicavel_a=payload.aplicavel_a,
            valor_padrao=payload.valor_padrao,
        )
        return _metadado_to_response(metadado)
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/metadados/{metadado_id}/ativar",
    response_model=MetadadoResponse,
    summary="Ativa um metadado",
    responses={404: {"model": ErrorResponse}},
)
def ativar_metadado(
    metadado_id: str,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> MetadadoResponse:
    use_case = AtivarMetadadoUseCase(repo)
    try:
        return _metadado_to_response(use_case.execute(metadado_id))
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/metadados/{metadado_id}/desativar",
    response_model=MetadadoResponse,
    summary="Desativa um metadado",
    responses={404: {"model": ErrorResponse}},
)
def desativar_metadado(
    metadado_id: str,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> MetadadoResponse:
    use_case = DesativarMetadadoUseCase(repo)
    try:
        return _metadado_to_response(use_case.execute(metadado_id))
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/metadados/{metadado_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta um metadado",
    responses={404: {"model": ErrorResponse}},
)
def deletar_metadado(
    metadado_id: str,
    repo: Annotated[MetadadoRepositoryInterface, Depends(get_metadado_repository)],
) -> None:
    use_case = DeletarMetadadoUseCase(repo)
    try:
        use_case.execute(metadado_id)
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Valores de Metadados
# =============================================================================


def _valor_to_response(v) -> ValorMetadadoResponse:
    return ValorMetadadoResponse(
        id=v.id,
        metadado_id=v.metadado_id,
        entidade_tipo=v.entidade_tipo,
        entidade_id=v.entidade_id,
        valor=v.valor,
        created_at=v.created_at,
        updated_at=v.updated_at,
    )


@router.post(
    "/valores",
    response_model=ValorMetadadoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Atribui um valor de metadado a uma entidade",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atribuir_valor(
    payload: ValorMetadadoCreateRequest,
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
    metadado_repo: Annotated[
        MetadadoRepositoryInterface, Depends(get_metadado_repository)
    ],
) -> ValorMetadadoResponse:
    use_case = AtribuirValorMetadadoUseCase(repo, metadado_repo)
    try:
        valor = use_case.execute(
            metadado_id=payload.metadado_id,
            entidade_tipo=payload.entidade_tipo,
            entidade_id=payload.entidade_id,
            valor=payload.valor,
        )
        return _valor_to_response(valor)
    except MetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValorMetadadoInvalidoError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/valores", response_model=ValorMetadadoListResponse, summary="Lista valores")
def listar_valores(
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
    page: int = 0,
    page_size: int = 50,
    entidade_tipo: str | None = None,
) -> ValorMetadadoListResponse:
    use_case = BuscarValorMetadadoUseCase(repo)
    items, total = use_case.list_all(page=page, page_size=page_size, entidade_tipo=entidade_tipo)
    return ValorMetadadoListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_valor_to_response(v) for v in items],
    )


@router.get(
    "/valores/{valor_id}",
    response_model=ValorMetadadoResponse,
    summary="Busca um valor de metadado por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_valor(
    valor_id: str,
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
) -> ValorMetadadoResponse:
    use_case = BuscarValorMetadadoUseCase(repo)
    try:
        return _valor_to_response(use_case.get_by_id(valor_id))
    except ValorMetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/entidades/{entidade_tipo}/{entidade_id}/valores",
    response_model=list[ValorMetadadoResponse],
    summary="Busca todos os valores de metadados de uma entidade",
)
def valores_da_entidade(
    entidade_tipo: str,
    entidade_id: str,
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
) -> list[ValorMetadadoResponse]:
    use_case = BuscarValorMetadadoUseCase(repo)
    return [_valor_to_response(v) for v in use_case.get_by_entidade(entidade_tipo, entidade_id)]


@router.put(
    "/valores/{valor_id}",
    response_model=ValorMetadadoResponse,
    summary="Atualiza o valor de um valor de metadado",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atualizar_valor(
    valor_id: str,
    payload: ValorMetadadoUpdateRequest,
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
    metadado_repo: Annotated[
        MetadadoRepositoryInterface, Depends(get_metadado_repository)
    ],
) -> ValorMetadadoResponse:
    from datetime import datetime

    from src.modules.sigmun_met.domain.services import MetadadoService

    existente = repo.get_by_id(valor_id)
    if existente is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Valor '{valor_id}' não encontrado"
        )
    metadado = metadado_repo.get_by_id(existente.metadado_id)
    if metadado is not None and not MetadadoService.validar_valor(metadado, payload.valor):
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"Valor '{payload.valor}' inválido para o metadado "
            f"'{metadado.codigo}' do tipo '{metadado.tipo_dado.value}'",
        )
    existente.valor = payload.valor
    existente.updated_at = datetime.utcnow()
    salvo = repo.save(existente)
    return _valor_to_response(salvo)


@router.delete(
    "/valores/{valor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove um valor de metadado",
    responses={404: {"model": ErrorResponse}},
)
def deletar_valor(
    valor_id: str,
    repo: Annotated[ValorMetadadoRepositoryInterface, Depends(get_valor_metadado_repository)],
) -> None:
    use_case = RemoverValorMetadadoUseCase(repo)
    try:
        use_case.execute(valor_id)
    except ValorMetadadoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Classificações
# =============================================================================


def _classificacao_to_response(c) -> ClassificacaoResponse:
    return ClassificacaoResponse(
        id=c.id,
        codigo=c.codigo,
        nome=c.nome,
        descricao=c.descricao,
        tipo=c.tipo.value,
        nivel=c.nivel,
        cor=c.cor,
        created_at=c.created_at,
        updated_at=c.updated_at,
    )


@router.post(
    "/classificacoes",
    response_model=ClassificacaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova classificação",
    responses={409: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def criar_classificacao(
    payload: ClassificacaoCreateRequest,
    repo: Annotated[ClassificacaoRepositoryInterface, Depends(get_classificacao_repository)],
) -> ClassificacaoResponse:
    use_case = CriarClassificacaoUseCase(repo)
    try:
        classificacao = use_case.execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao or "",
            tipo=payload.tipo.value,
            nivel=payload.nivel,
            cor=payload.cor or "",
        )
        return _classificacao_to_response(classificacao)
    except ClassificacaoJaExisteError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except (CodigoInvalidoError, ValueError) as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/classificacoes", response_model=ClassificacaoListResponse, summary="Lista classificações"
)
def listar_classificacoes(
    repo: Annotated[ClassificacaoRepositoryInterface, Depends(get_classificacao_repository)],
    page: int = 0,
    page_size: int = 50,
    tipo: str | None = None,
) -> ClassificacaoListResponse:
    use_case = BuscarClassificacaoUseCase(repo)
    items, total = use_case.list_all(page=page, page_size=page_size, tipo=tipo)
    return ClassificacaoListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_classificacao_to_response(c) for c in items],
    )


@router.get(
    "/classificacoes/{classificacao_id}",
    response_model=ClassificacaoResponse,
    summary="Busca uma classificação por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_classificacao(
    classificacao_id: str,
    repo: Annotated[ClassificacaoRepositoryInterface, Depends(get_classificacao_repository)],
) -> ClassificacaoResponse:
    use_case = BuscarClassificacaoUseCase(repo)
    try:
        return _classificacao_to_response(use_case.get_by_id(classificacao_id))
    except ClassificacaoNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/classificacoes/{classificacao_id}",
    response_model=ClassificacaoResponse,
    summary="Atualiza uma classificação",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atualizar_classificacao(
    classificacao_id: str,
    payload: ClassificacaoUpdateRequest,
    repo: Annotated[ClassificacaoRepositoryInterface, Depends(get_classificacao_repository)],
) -> ClassificacaoResponse:
    use_case = AtualizarClassificacaoUseCase(repo)
    try:
        classificacao = use_case.execute(
            classificacao_id=classificacao_id,
            nome=payload.nome,
            descricao=payload.descricao,
            tipo=payload.tipo.value if payload.tipo else None,
            nivel=payload.nivel,
            cor=payload.cor,
        )
        return _classificacao_to_response(classificacao)
    except ClassificacaoNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/classificacoes/{classificacao_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta uma classificação",
    responses={404: {"model": ErrorResponse}},
)
def deletar_classificacao(
    classificacao_id: str,
    repo: Annotated[ClassificacaoRepositoryInterface, Depends(get_classificacao_repository)],
) -> None:
    use_case = DeletarClassificacaoUseCase(repo)
    try:
        use_case.execute(classificacao_id)
    except ClassificacaoNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Taxonomias
# =============================================================================


def _taxonomia_to_response(t) -> TaxonomiaResponse:
    return TaxonomiaResponse(
        id=t.id,
        codigo=t.codigo,
        nome=t.nome,
        descricao=t.descricao,
        termos_ids=t.termos_ids,
        created_at=t.created_at,
        updated_at=t.updated_at,
    )


@router.post(
    "/taxonomias",
    response_model=TaxonomiaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova taxonomia",
    responses={409: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def criar_taxonomia(
    payload: TaxonomiaCreateRequest,
    repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
) -> TaxonomiaResponse:
    use_case = CriarTaxonomiaUseCase(repo)
    try:
        taxonomia = use_case.execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao or "",
        )
        return _taxonomia_to_response(taxonomia)
    except TaxonomiaJaExisteError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except (CodigoInvalidoError, ValueError) as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/taxonomias", response_model=TaxonomiaListResponse, summary="Lista taxonomias")
def listar_taxonomias(
    repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
    page: int = 0,
    page_size: int = 50,
) -> TaxonomiaListResponse:
    use_case = BuscarTaxonomiaUseCase(repo)
    items, total = use_case.list_all(page=page, page_size=page_size)
    return TaxonomiaListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_taxonomia_to_response(t) for t in items],
    )


@router.get(
    "/taxonomias/{taxonomia_id}",
    response_model=TaxonomiaResponse,
    summary="Busca uma taxonomia por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_taxonomia(
    taxonomia_id: str,
    repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
) -> TaxonomiaResponse:
    use_case = BuscarTaxonomiaUseCase(repo)
    try:
        return _taxonomia_to_response(use_case.get_by_id(taxonomia_id))
    except TaxonomiaNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/taxonomias/{taxonomia_id}",
    response_model=TaxonomiaResponse,
    summary="Atualiza uma taxonomia",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atualizar_taxonomia(
    taxonomia_id: str,
    payload: TaxonomiaUpdateRequest,
    repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
) -> TaxonomiaResponse:
    use_case = AtualizarTaxonomiaUseCase(repo)
    try:
        taxonomia = use_case.execute(
            taxonomia_id=taxonomia_id,
            nome=payload.nome,
            descricao=payload.descricao,
        )
        return _taxonomia_to_response(taxonomia)
    except TaxonomiaNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/taxonomias/{taxonomia_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta uma taxonomia",
    responses={404: {"model": ErrorResponse}},
)
def deletar_taxonomia(
    taxonomia_id: str,
    repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
) -> None:
    use_case = DeletarTaxonomiaUseCase(repo)
    try:
        use_case.execute(taxonomia_id)
    except TaxonomiaNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Termos de Taxonomia
# =============================================================================


def _termo_to_response(t) -> TermoResponse:
    return TermoResponse(
        id=t.id,
        taxonomia_id=t.taxonomia_id,
        termo_pai_id=t.termo_pai_id or None,
        codigo=t.codigo,
        nome=t.nome,
        descricao=t.descricao,
        sinonimos=t.sinonimos,
        ordem=t.ordem,
        created_at=t.created_at,
        updated_at=t.updated_at,
    )


@router.post(
    "/termos",
    response_model=TermoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo termo de taxonomia",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def criar_termo(
    payload: TermoCreateRequest,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
    taxonomia_repo: Annotated[TaxonomiaRepositoryInterface, Depends(get_taxonomia_repository)],
) -> TermoResponse:
    use_case = CriarTermoUseCase(repo, taxonomia_repo)
    try:
        termo = use_case.execute(
            taxonomia_id=payload.taxonomia_id,
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao or "",
            termo_pai_id=payload.termo_pai_id or "",
            sinonimos=payload.sinonimos,
            ordem=payload.ordem,
        )
        return _termo_to_response(termo)
    except TaxonomiaNaoEncontradaError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except HierarquiaCiclicaError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except (CodigoInvalidoError, ValueError) as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/termos", response_model=TermoListResponse, summary="Lista termos de taxonomia")
def listar_termos(
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
    page: int = 0,
    page_size: int = 50,
    taxonomia_id: str | None = None,
) -> TermoListResponse:
    use_case = BuscarTermoUseCase(repo)
    items, total = use_case.list_all(page=page, page_size=page_size, taxonomia_id=taxonomia_id)
    return TermoListResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[_termo_to_response(t) for t in items],
    )


@router.get(
    "/termos/{termo_id}",
    response_model=TermoResponse,
    summary="Busca um termo por ID",
    responses={404: {"model": ErrorResponse}},
)
def buscar_termo(
    termo_id: str,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
) -> TermoResponse:
    use_case = BuscarTermoUseCase(repo)
    try:
        return _termo_to_response(use_case.get_by_id(termo_id))
    except TermoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/taxonomias/{taxonomia_id}/termos",
    response_model=list[TermoResponse],
    summary="Busca todos os termos de uma taxonomia",
)
def termos_da_taxonomia(
    taxonomia_id: str,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
) -> list[TermoResponse]:
    use_case = BuscarTermoUseCase(repo)
    return [_termo_to_response(t) for t in use_case.get_by_taxonomia(taxonomia_id)]


@router.get(
    "/termos/{termo_id}/filhos",
    response_model=list[TermoResponse],
    summary="Busca os termos filhos diretos de um termo",
)
def filhos_do_termo(
    termo_id: str,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
) -> list[TermoResponse]:
    use_case = BuscarTermoUseCase(repo)
    return [_termo_to_response(t) for t in use_case.get_by_pai(termo_id)]


@router.put(
    "/termos/{termo_id}",
    response_model=TermoResponse,
    summary="Atualiza um termo de taxonomia",
    responses={404: {"model": ErrorResponse}, 400: {"model": ErrorResponse}},
)
def atualizar_termo(
    termo_id: str,
    payload: TermoUpdateRequest,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
) -> TermoResponse:
    use_case = AtualizarTermoUseCase(repo)
    try:
        termo = use_case.execute(
            termo_id=termo_id,
            nome=payload.nome,
            descricao=payload.descricao,
            sinonimos=payload.sinonimos,
            ordem=payload.ordem,
        )
        return _termo_to_response(termo)
    except TermoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/termos/{termo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta um termo de taxonomia",
    responses={404: {"model": ErrorResponse}},
)
def deletar_termo(
    termo_id: str,
    repo: Annotated[TermoTaxonomiaRepositoryInterface, Depends(get_termo_repository)],
) -> None:
    use_case = DeletarTermoUseCase(repo)
    try:
        use_case.execute(termo_id)
    except TermoNaoEncontradoError as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
