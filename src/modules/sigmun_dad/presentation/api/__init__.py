"""Endpoints REST de Dados Corporativos (DOM-DAD)."""

from __future__ import annotations

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_dad.application.interfaces import (
    AtivoRepositoryInterface,
    CatalogoRepositoryInterface,
    LinhagemRepositoryInterface,
    PoliticaRepositoryInterface,
    QualidadeRepositoryInterface,
)
from src.modules.sigmun_dad.application.use_cases import (
    AdicionarAtivoCatalogoUseCase,
    AdicionarRegraPoliticaUseCase,
    ArquivarAtivoUseCase,
    AtivarAtivoUseCase,
    AtualizarCatalogoUseCase,
    AtualizarLinhagemUseCase,
    AtualizarPoliticaUseCase,
    AtualizarQualidadeDadosUseCase,
    AvaliarQualidadeUseCase,
    BuscarAtivoUseCase,
    BuscarCatalogoUseCase,
    BuscarLinhagemUseCase,
    BuscarPoliticaUseCase,
    BuscarQualidadeUseCase,
    CriarAtivoUseCase,
    CriarCatalogoUseCase,
    CriarLinhagemUseCase,
    CriarPoliticaUseCase,
    DeletarCatalogoUseCase,
    DeletarLinhagemUseCase,
    DeletarPoliticaUseCase,
    DeletarQualidadeUseCase,
    DesativarAtivoUseCase,
    RemoverAtivoCatalogoUseCase,
)
from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    Catalogo,
    LinhagemDado,
    PoliticaDado,
    QualidadeDado,
)
from src.modules.sigmun_dad.domain.exceptions import (
    AtivoJaCadastradoError,
    AtivoNaoEncontradoError,
    CatalogoDuplicadoError,
    CatalogoNaoEncontradoError,
    LinhagemDuplicadaError,
    LinhagemNaoEncontradaError,
    NomeAtivoInvalidoError,
    PoliticaDuplicadaError,
    PoliticaNaoEncontradaError,
    QualidadeNaoEncontradaError,
)
from src.modules.sigmun_dad.infrastructure.repositories import (
    SqlAlchemyAtivoRepository,
    SqlAlchemyCatalogoRepository,
    SqlAlchemyLinhagemRepository,
    SqlAlchemyPoliticaRepository,
    SqlAlchemyQualidadeRepository,
)
from src.modules.sigmun_dad.presentation.schemas import (
    AtivoCreateRequest,
    AtivoListResponse,
    AtivoResponse,
    # Catálogo
    CatalogoCreateRequest,
    CatalogoListResponse,
    CatalogoResponse,
    CatalogoUpdateRequest,
    # Linhagem
    LinhagemCreateRequest,
    LinhagemListResponse,
    LinhagemResponse,
    LinhagemUpdateRequest,
    # Política
    PoliticaCreateRequest,
    PoliticaListResponse,
    PoliticaResponse,
    PoliticaUpdateRequest,
    # Qualidade
    QualidadeCreateRequest,
    QualidadeListResponse,
    QualidadeResponse,
    QualidadeUpdateRequest,
)
from src.shared.presentation.dependencies import (
    JWTUsuarioContexto,
    UsuarioOpcional,
    exigir_papeis,
)
from src.shared.presentation.paginacao import (
    Pagina,
    ParametrosPaginacao,
    criar_pagina,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/dad", tags=["Dados Corporativos"])


# =============================================================================
# Dependency Injection
# =============================================================================


def get_ativo_repository(
    session: Annotated[Session, Depends(get_db)],
) -> AtivoRepositoryInterface:
    return SqlAlchemyAtivoRepository(session)


def get_catalogo_repository(
    session: Annotated[Session, Depends(get_db)],
) -> CatalogoRepositoryInterface:
    return SqlAlchemyCatalogoRepository(session)


def get_linhagem_repository(
    session: Annotated[Session, Depends(get_db)],
) -> LinhagemRepositoryInterface:
    return SqlAlchemyLinhagemRepository(session)


def get_politica_repository(
    session: Annotated[Session, Depends(get_db)],
) -> PoliticaRepositoryInterface:
    return SqlAlchemyPoliticaRepository(session)


def get_qualidade_repository(
    session: Annotated[Session, Depends(get_db)],
) -> QualidadeRepositoryInterface:
    return SqlAlchemyQualidadeRepository(session)


def _to_response(ativo: AtivoDado) -> AtivoResponse:
    return AtivoResponse(
        id=ativo.id,
        nome=ativo.nome,
        descricao=ativo.descricao,
        tipo=ativo.tipo.value,
        status=ativo.status.value,
        qualidade=ativo.qualidade.value,
        dono_id=ativo.dono_id,
        steward_id=ativo.steward_id,
        schema_origem=ativo.schema_origem,
        tabela_origem=ativo.tabela_origem,
        classificacao=ativo.classificacao,
        tags=ativo.tags,
        created_at=ativo.created_at,
        updated_at=ativo.updated_at,
    )


@router.post(
    "/ativos",
    response_model=AtivoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo ativo de dado",
)
def criar_ativo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    payload: AtivoCreateRequest,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> AtivoResponse:
    use_case = CriarAtivoUseCase(repo)
    try:
        ativo = use_case.execute(
            nome=payload.nome,
            descricao=payload.descricao or "",
            tipo=payload.tipo.value,
            dono_id=payload.dono_id or "",
            steward_id=payload.steward_id or "",
            schema_origem=payload.schema_origem or "",
            tabela_origem=payload.tabela_origem or "",
            classificacao=payload.classificacao or "",
            tags=payload.tags,
        )
        return _to_response(ativo)
    except AtivoJaCadastradoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except NomeAtivoInvalidoError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/ativos/{ativo_id}",
    response_model=AtivoResponse,
    summary="Busca ativo por ID",
)
def buscar_ativo(
    usuario: UsuarioOpcional,
    ativo_id: str,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> AtivoResponse:
    use_case = BuscarAtivoUseCase(repo)
    try:
        ativo = use_case.get_by_id(ativo_id)
        return _to_response(ativo)
    except AtivoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/ativos",
    response_model=Pagina[AtivoResponse],
    summary="Lista ativos de dados",
)
def listar_ativos(
    usuario: UsuarioOpcional,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
    params: Annotated[ParametrosPaginacao, Depends()],
    tipo: str | None = None,
    status_filter: str | None = None,
) -> Pagina[AtivoResponse]:
    use_case = BuscarAtivoUseCase(repo)
    ativos, total = use_case.list_all(params.page, params.page_size, tipo, status_filter)
    return criar_pagina(
        [_to_response(a) for a in ativos],
        params,
        total,
    )


@router.post(
    "/ativos/{ativo_id}/ativar",
    response_model=AtivoResponse,
    summary="Ativa um ativo",
)
def ativar_ativo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    ativo_id: str,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> AtivoResponse:
    use_case = AtivarAtivoUseCase(repo)
    try:
        ativo = use_case.execute(ativo_id)
        return _to_response(ativo)
    except AtivoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/ativos/{ativo_id}/desativar",
    response_model=AtivoResponse,
    summary="Desativa um ativo",
)
def desativar_ativo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    ativo_id: str,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> AtivoResponse:
    use_case = DesativarAtivoUseCase(repo)
    try:
        ativo = use_case.execute(ativo_id)
        return _to_response(ativo)
    except AtivoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/ativos/{ativo_id}/arquivar",
    response_model=AtivoResponse,
    summary="Arquiva um ativo",
)
def arquivar_ativo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    ativo_id: str,
    repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> AtivoResponse:
    use_case = ArquivarAtivoUseCase(repo)
    try:
        ativo = use_case.execute(ativo_id)
        return _to_response(ativo)
    except AtivoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Catálogo
# =============================================================================


def _to_catalogo_response(catalogo: Catalogo) -> CatalogoResponse:
    return CatalogoResponse(
        id=catalogo.id,
        nome=catalogo.nome,
        descricao=catalogo.descricao,
        dominio=catalogo.dominio,
        ativos_ids=catalogo.ativos_ids,
        created_at=catalogo.created_at,
        updated_at=catalogo.updated_at,
    )


@router.post(
    "/catalogos",
    response_model=CatalogoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo catálogo",
)
def criar_catalogo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    payload: CatalogoCreateRequest,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
) -> CatalogoResponse:
    use_case = CriarCatalogoUseCase(repo)
    try:
        catalogo = use_case.execute(
            nome=payload.nome,
            descricao=payload.descricao or "",
            dominio=payload.dominio or "",
        )
        return _to_catalogo_response(catalogo)
    except CatalogoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/catalogos/{catalogo_id}",
    response_model=CatalogoResponse,
    summary="Busca catálogo por ID",
)
def buscar_catalogo(
    usuario: UsuarioOpcional,
    catalogo_id: str,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
) -> CatalogoResponse:
    use_case = BuscarCatalogoUseCase(repo)
    try:
        catalogo = use_case.get_by_id(catalogo_id)
        return _to_catalogo_response(catalogo)
    except CatalogoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/catalogos",
    response_model=Pagina[CatalogoResponse],
    summary="Lista catálogos",
)
def listar_catalogos(
    usuario: UsuarioOpcional,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
    params: Annotated[ParametrosPaginacao, Depends()],
) -> Pagina[CatalogoResponse]:
    use_case = BuscarCatalogoUseCase(repo)
    catalogos, total = use_case.list_all(params.page, params.page_size)
    return criar_pagina(
        [_to_catalogo_response(c) for c in catalogos],
        params,
        total,
    )


@router.patch(
    "/catalogos/{catalogo_id}",
    response_model=CatalogoResponse,
    summary="Atualiza um catálogo",
)
def atualizar_catalogo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    catalogo_id: str,
    payload: CatalogoUpdateRequest,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
) -> CatalogoResponse:
    use_case = AtualizarCatalogoUseCase(repo)
    try:
        catalogo = use_case.execute(
            catalogo_id=catalogo_id,
            nome=payload.nome,
            descricao=payload.descricao,
            dominio=payload.dominio,
        )
        return _to_catalogo_response(catalogo)
    except CatalogoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/catalogos/{catalogo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta um catálogo",
)
def deletar_catalogo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "dados"))],
    catalogo_id: str,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
) -> None:
    use_case = DeletarCatalogoUseCase(repo)
    try:
        use_case.execute(catalogo_id)
    except CatalogoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/catalogos/{catalogo_id}/ativos/{ativo_id}",
    response_model=CatalogoResponse,
    summary="Adiciona ativo ao catálogo",
)
def adicionar_ativo_catalogo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    catalogo_id: str,
    ativo_id: str,
    catalogo_repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
    ativo_repo: Annotated[AtivoRepositoryInterface, Depends(get_ativo_repository)],
) -> CatalogoResponse:
    use_case = AdicionarAtivoCatalogoUseCase(catalogo_repo, ativo_repo)
    try:
        catalogo = use_case.execute(catalogo_id, ativo_id)
        return _to_catalogo_response(catalogo)
    except (CatalogoNaoEncontradoError, AtivoNaoEncontradoError) as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/catalogos/{catalogo_id}/ativos/{ativo_id}",
    response_model=CatalogoResponse,
    summary="Remove ativo do catálogo",
)
def remover_ativo_catalogo(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "dados"))],
    catalogo_id: str,
    ativo_id: str,
    repo: Annotated[CatalogoRepositoryInterface, Depends(get_catalogo_repository)],
) -> CatalogoResponse:
    use_case = RemoverAtivoCatalogoUseCase(repo)
    try:
        catalogo = use_case.execute(catalogo_id, ativo_id)
        return _to_catalogo_response(catalogo)
    except CatalogoNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Linhagem
# =============================================================================


def _to_linhagem_response(linhagem: LinhagemDado) -> LinhagemResponse:
    return LinhagemResponse(
        id=linhagem.id,
        ativo_origem_id=linhagem.ativo_origem_id,
        ativo_destino_id=linhagem.ativo_destino_id,
        tipo_transformacao=linhagem.tipo_transformacao,
        descricao=linhagem.descricao,
        regras=linhagem.regras,
        created_at=linhagem.created_at,
    )


@router.post(
    "/linhagens",
    response_model=LinhagemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova linhagem",
)
def criar_linhagem(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    payload: LinhagemCreateRequest,
    repo: Annotated[LinhagemRepositoryInterface, Depends(get_linhagem_repository)],
) -> LinhagemResponse:
    use_case = CriarLinhagemUseCase(repo)
    try:
        linhagem = use_case.execute(
            ativo_origem_id=payload.ativo_origem_id,
            ativo_destino_id=payload.ativo_destino_id,
            tipo_transformacao=payload.tipo_transformacao or "",
            descricao=payload.descricao or "",
            regras=payload.regras or "",
        )
        return _to_linhagem_response(linhagem)
    except LinhagemDuplicadaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/linhagens/{linhagem_id}",
    response_model=LinhagemResponse,
    summary="Busca linhagem por ID",
)
def buscar_linhagem(
    usuario: UsuarioOpcional,
    linhagem_id: str,
    repo: Annotated[LinhagemRepositoryInterface, Depends(get_linhagem_repository)],
) -> LinhagemResponse:
    use_case = BuscarLinhagemUseCase(repo)
    try:
        linhagem = use_case.get_by_id(linhagem_id)
        return _to_linhagem_response(linhagem)
    except LinhagemNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/linhagens",
    response_model=Pagina[LinhagemResponse],
    summary="Lista linhagens",
)
def listar_linhagens(
    usuario: UsuarioOpcional,
    repo: Annotated[LinhagemRepositoryInterface, Depends(get_linhagem_repository)],
    params: Annotated[ParametrosPaginacao, Depends()],
) -> Pagina[LinhagemResponse]:
    use_case = BuscarLinhagemUseCase(repo)
    linhagens, total = use_case.list_all(params.page, params.page_size)
    return criar_pagina(
        [_to_linhagem_response(item) for item in linhagens],
        params,
        total,
    )


@router.patch(
    "/linhagens/{linhagem_id}",
    response_model=LinhagemResponse,
    summary="Atualiza uma linhagem",
)
def atualizar_linhagem(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    linhagem_id: str,
    payload: LinhagemUpdateRequest,
    repo: Annotated[LinhagemRepositoryInterface, Depends(get_linhagem_repository)],
) -> LinhagemResponse:
    use_case = AtualizarLinhagemUseCase(repo)
    try:
        linhagem = use_case.execute(
            linhagem_id=linhagem_id,
            tipo_transformacao=payload.tipo_transformacao,
            descricao=payload.descricao,
            regras=payload.regras,
        )
        return _to_linhagem_response(linhagem)
    except LinhagemNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/linhagens/{linhagem_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta uma linhagem",
)
def deletar_linhagem(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "dados"))],
    linhagem_id: str,
    repo: Annotated[LinhagemRepositoryInterface, Depends(get_linhagem_repository)],
) -> None:
    use_case = DeletarLinhagemUseCase(repo)
    try:
        use_case.execute(linhagem_id)
    except LinhagemNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Política
# =============================================================================


def _to_politica_response(politica: PoliticaDado) -> PoliticaResponse:
    return PoliticaResponse(
        id=politica.id,
        codigo=politica.codigo,
        nome=politica.nome,
        descricao=politica.descricao,
        tipo=politica.tipo,
        regras=politica.regras,
        created_at=politica.created_at,
        updated_at=politica.updated_at,
    )


@router.post(
    "/politicas",
    response_model=PoliticaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova política",
)
def criar_politica(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    payload: PoliticaCreateRequest,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
) -> PoliticaResponse:
    use_case = CriarPoliticaUseCase(repo)
    try:
        politica = use_case.execute(
            codigo=payload.codigo,
            nome=payload.nome,
            descricao=payload.descricao or "",
            tipo=payload.tipo or "",
            regras=payload.regras,
        )
        return _to_politica_response(politica)
    except PoliticaDuplicadaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.get(
    "/politicas/{politica_id}",
    response_model=PoliticaResponse,
    summary="Busca política por ID",
)
def buscar_politica(
    usuario: UsuarioOpcional,
    politica_id: str,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
) -> PoliticaResponse:
    use_case = BuscarPoliticaUseCase(repo)
    try:
        politica = use_case.get_by_id(politica_id)
        return _to_politica_response(politica)
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/politicas",
    response_model=Pagina[PoliticaResponse],
    summary="Lista políticas",
)
def listar_politicas(
    usuario: UsuarioOpcional,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
    params: Annotated[ParametrosPaginacao, Depends()],
) -> Pagina[PoliticaResponse]:
    use_case = BuscarPoliticaUseCase(repo)
    politicas, total = use_case.list_all(params.page, params.page_size)
    return criar_pagina(
        [_to_politica_response(p) for p in politicas],
        params,
        total,
    )


@router.patch(
    "/politicas/{politica_id}",
    response_model=PoliticaResponse,
    summary="Atualiza uma política",
)
def atualizar_politica(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    politica_id: str,
    payload: PoliticaUpdateRequest,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
) -> PoliticaResponse:
    use_case = AtualizarPoliticaUseCase(repo)
    try:
        politica = use_case.execute(
            politica_id=politica_id,
            nome=payload.nome,
            descricao=payload.descricao,
            tipo=payload.tipo,
        )
        return _to_politica_response(politica)
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/politicas/{politica_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta uma política",
)
def deletar_politica(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "dados"))],
    politica_id: str,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
) -> None:
    use_case = DeletarPoliticaUseCase(repo)
    try:
        use_case.execute(politica_id)
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/politicas/{politica_id}/regras",
    response_model=PoliticaResponse,
    summary="Adiciona regra à política",
)
def adicionar_regra_politica(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    politica_id: str,
    regra: str,
    repo: Annotated[PoliticaRepositoryInterface, Depends(get_politica_repository)],
) -> PoliticaResponse:
    use_case = AdicionarRegraPoliticaUseCase(repo)
    try:
        politica = use_case.execute(politica_id, regra)
        return _to_politica_response(politica)
    except PoliticaNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =============================================================================
# Endpoints de Qualidade de Dados
# =============================================================================


def _to_qualidade_response(qualidade: QualidadeDado) -> QualidadeResponse:
    return QualidadeResponse(
        id=qualidade.id,
        ativo_id=qualidade.ativo_id,
        nivel=qualidade.nivel.value,
        score=qualidade.score,
        criterios=qualidade.criterios,
        observacao=qualidade.observacao,
        created_at=qualidade.created_at,
        updated_at=qualidade.updated_at,
    )


@router.post(
    "/qualidade",
    response_model=QualidadeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Avalia qualidade de um ativo",
)
def avaliar_qualidade(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    payload: QualidadeCreateRequest,
    repo: Annotated[QualidadeRepositoryInterface, Depends(get_qualidade_repository)],
) -> QualidadeResponse:
    use_case = AvaliarQualidadeUseCase(repo)
    try:
        qualidade = use_case.execute(
            ativo_id=payload.ativo_id,
            score=payload.score,
            criterios=payload.criterios,
            observacao=payload.observacao or "",
        )
        return _to_qualidade_response(qualidade)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "/qualidade/{qualidade_id}",
    response_model=QualidadeResponse,
    summary="Busca registro de qualidade por ID",
)
def buscar_qualidade(
    usuario: UsuarioOpcional,
    qualidade_id: str,
    repo: Annotated[QualidadeRepositoryInterface, Depends(get_qualidade_repository)],
) -> QualidadeResponse:
    use_case = BuscarQualidadeUseCase(repo)
    try:
        qualidade = use_case.get_by_id(qualidade_id)
        return _to_qualidade_response(qualidade)
    except QualidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/qualidade",
    response_model=Pagina[QualidadeResponse],
    summary="Lista registros de qualidade",
)
def listar_qualidade(
    usuario: UsuarioOpcional,
    repo: Annotated[QualidadeRepositoryInterface, Depends(get_qualidade_repository)],
    params: Annotated[ParametrosPaginacao, Depends()],
) -> Pagina[QualidadeResponse]:
    use_case = BuscarQualidadeUseCase(repo)
    registros, total = use_case.list_all(params.page, params.page_size)
    return criar_pagina(
        [_to_qualidade_response(r) for r in registros],
        params,
        total,
    )


@router.patch(
    "/qualidade/{qualidade_id}",
    response_model=QualidadeResponse,
    summary="Atualiza registro de qualidade",
)
def atualizar_qualidade(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "dados"))],
    qualidade_id: str,
    payload: QualidadeUpdateRequest,
    repo: Annotated[QualidadeRepositoryInterface, Depends(get_qualidade_repository)],
) -> QualidadeResponse:
    use_case = AtualizarQualidadeDadosUseCase(repo)
    try:
        qualidade = use_case.execute(
            qualidade_id=qualidade_id,
            score=payload.score,
            nivel=payload.nivel,
            criterios=payload.criterios,
            observacao=payload.observacao,
        )
        return _to_qualidade_response(qualidade)
    except QualidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/qualidade/{qualidade_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta registro de qualidade",
)
def deletar_qualidade(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("admin", "dados"))],
    qualidade_id: str,
    repo: Annotated[QualidadeRepositoryInterface, Depends(get_qualidade_repository)],
) -> None:
    use_case = DeletarQualidadeUseCase(repo)
    try:
        use_case.execute(qualidade_id)
    except QualidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


__all__ = [
    "router",
    "get_ativo_repository",
    "get_catalogo_repository",
    "get_linhagem_repository",
    "get_politica_repository",
    "get_qualidade_repository",
]
