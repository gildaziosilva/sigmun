"""Endpoints REST de Pessoas (DOM-CUM — Cadastro Único Municipal).

Baseado em:
  - 004-Mapa-de-Servicos-Cadastro-Unico-Municipal.md (serviços de pessoa)
  - RN-CUM-001 (extensão por tipo), 002/003 (CPF/CNPJ), 004 (unicidade
    de documento), 005 (endereço principal), 006 (documento/contato
    principal), 007 (exclusão lógica)

Nota: autorização e auditoria estruturadas seguem o padrão do
DOM-COMPRAS-001 (header X-Usuario-Id provisório até o DOM-IDN).
"""

from __future__ import annotations

import logging
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AdicionarContatoCommand,
    AdicionarDocumentoCommand,
    AdicionarEnderecoCommand,
    AlterarCategoriaPessoaCommand,
    AtualizarPessoaFisicaCommand,
    AtualizarPessoaJuridicaCommand,
    CriarPessoaCommand,
    ExcluirPessoaCommand,
)
from src.modules.sigmun_cadastro.application.queries.pessoa_queries import (
    ConsultarPessoaQuery,
    ListarPessoasQuery,
)
from src.modules.sigmun_cadastro.application.use_cases.adicionar_contato import (
    AdicionarContatoUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.adicionar_documento import (
    AdicionarDocumentoUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.adicionar_endereco import (
    AdicionarEnderecoUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.atualizar_pessoa import (
    AlterarCategoriaPessoaUseCase,
    AtualizarPessoaFisicaUseCase,
    AtualizarPessoaJuridicaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.consultar_pessoa import (
    ConsultarPessoaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.excluir_pessoa import (
    ExcluirPessoaUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.listar_pessoas import (
    ListarPessoasUseCase,
)
from src.modules.sigmun_cadastro.application.use_cases.registrar_pessoa import (
    RegistrarPessoaUseCase,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    Pessoa,
    TipoPessoa,
)
from src.modules.sigmun_cadastro.domain.exceptions import (
    DocumentoDuplicadoError,
    DocumentoInvalidoError,
    PessoaExcluidaError,
    PessoaNaoEncontradoError,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)
from src.modules.sigmun_cadastro.infrastructure.repositories import (
    SqlAlchemyPessoaRepository,
)
from src.modules.sigmun_cadastro.presentation.schemas.pessoa_schemas import (
    CategoriaUpdateRequest,
    ContatoPayload,
    DocumentoPayload,
    EnderecoPayload,
    PessoaCreateRequest,
    PessoaFisicaUpdateRequest,
    PessoaJuridicaUpdateRequest,
    PessoaListResponse,
    PessoaResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/cadastro/pessoas", tags=["Cadastro - Pessoas"])


# -- Providers (composition root do módulo) ------------------------------------


def get_pessoa_repository(
    session: Annotated[Session, Depends(get_db)],
) -> PessoaRepository:
    """Fornece o repositório concreto por requisição."""
    return SqlAlchemyPessoaRepository(session)


def _usuario_id_header(
    x_usuario_id: Annotated[
        UUID | None,
        Header(
            alias="X-Usuario-Id",
            description="Identificador do usuário autenticado (provisório até DOM-IDN).",
        ),
    ] = None,
) -> UUID | None:
    return x_usuario_id


# -- Endpoints ------------------------------------------------------------------


@router.post(
    "",
    response_model=PessoaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registra uma nova pessoa (PF ou PJ) com filhos do agregado",
    responses={
        400: {"description": "Requisição inválida"},
        409: {"description": "Documento duplicado"},
    },
)
def registrar_pessoa(
    payload: PessoaCreateRequest,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Registra uma pessoa com endereços/documentos/contatos (RN-CUM-001 a 006)."""
    command = CriarPessoaCommand(
        tipo=payload.tipo,
        categoria=payload.categoria,
        usuario_id=usuario_id,
        unidade_id=payload.unidade_id,
        nome=payload.nome,
        data_nascimento=payload.data_nascimento,
        sexo=payload.sexo,
        estado_civil=payload.estado_civil,
        mae=payload.mae,
        pai=payload.pai,
        razao_social=payload.razao_social,
        nome_fantasia=payload.nome_fantasia,
        cnae_principal=payload.cnae_principal,
        capital=payload.capital,
        enderecos=[e.model_dump() for e in payload.enderecos],
        documentos=[d.model_dump() for d in payload.documentos],
        contatos=[c.model_dump() for c in payload.contatos],
    )
    use_case = RegistrarPessoaUseCase(repository)
    try:
        return use_case.execute(command)
    except DocumentoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except (DocumentoInvalidoError, ValueError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get(
    "",
    response_model=PessoaListResponse,
    summary="Lista pessoas com filtros e paginação",
)
def listar_pessoas(
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    tipo: TipoPessoa | None = Query(default=None, description="Filtro por tipo (FISICA/JURIDICA)"),
    categoria: CategoriaPessoa | None = Query(default=None, description="Filtro por categoria"),
    include_deleted: bool = Query(default=False, description="Incluir logicamente excluídas"),
    page: int = Query(default=1, ge=1, description="Página (base 1)"),
    page_size: int = Query(default=50, ge=1, le=200, description="Itens por página"),
) -> PessoaListResponse:
    """Lista paginada de pessoas (padrão do DOM-COMPRAS-001)."""
    use_case = ListarPessoasUseCase(repository)
    todas = use_case.execute(
        ListarPessoasQuery(tipo=tipo, categoria=categoria, include_deleted=include_deleted)
    )
    total = len(todas)
    inicio = (page - 1) * page_size
    items = todas[inicio : inicio + page_size]
    return PessoaListResponse(total=total, page=page, page_size=page_size, items=items)


@router.get(
    "/{pessoa_id}",
    response_model=PessoaResponse,
    summary="Consulta uma pessoa pelo ID",
    responses={404: {"description": "Pessoa não encontrada"}},
)
def consultar_pessoa(
    pessoa_id: UUID,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    include_deleted: bool = Query(default=False, description="Incluir logicamente excluídas"),
) -> Pessoa:
    """Consulta dados cadastrais completos de uma pessoa."""
    use_case = ConsultarPessoaUseCase(repository)
    try:
        return use_case.execute(
            ConsultarPessoaQuery(pessoa_id=pessoa_id, include_deleted=include_deleted)
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# -- Atualizações -----------------------------------------------------------------


@router.patch(
    "/{pessoa_id}/dados-fisicos",
    response_model=PessoaResponse,
    summary="Atualiza dados da pessoa física",
    responses={
        404: {"description": "Pessoa não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def atualizar_dados_fisicos(
    pessoa_id: UUID,
    payload: PessoaFisicaUpdateRequest,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Atualização parcial dos dados físicos (somente tipo FISICA)."""
    if not payload.model_fields_set:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Informe ao menos um campo para atualização.",
        )
    use_case = AtualizarPessoaFisicaUseCase(repository)
    try:
        return use_case.execute(
            AtualizarPessoaFisicaCommand(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id,
                **payload.model_dump(),
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PessoaExcluidaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.patch(
    "/{pessoa_id}/dados-juridicos",
    response_model=PessoaResponse,
    summary="Atualiza dados da pessoa jurídica",
    responses={
        404: {"description": "Pessoa não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def atualizar_dados_juridicos(
    pessoa_id: UUID,
    payload: PessoaJuridicaUpdateRequest,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Atualização parcial dos dados jurídicos (somente tipo JURIDICA)."""
    if not payload.model_fields_set:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Informe ao menos um campo para atualização.",
        )
    use_case = AtualizarPessoaJuridicaUseCase(repository)
    try:
        return use_case.execute(
            AtualizarPessoaJuridicaCommand(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id,
                **payload.model_dump(),
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PessoaExcluidaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.patch(
    "/{pessoa_id}/categoria",
    response_model=PessoaResponse,
    summary="Altera a categoria cadastral da pessoa",
    responses={404: {"description": "Pessoa não encontrada"}},
)
def alterar_categoria(
    pessoa_id: UUID,
    payload: CategoriaUpdateRequest,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Altera a categoria (CIDADAO/SERVIDOR/FORNECEDOR/AGENTE_EXTERNO)."""
    use_case = AlterarCategoriaPessoaUseCase(repository)
    try:
        return use_case.execute(
            AlterarCategoriaPessoaCommand(
                pessoa_id=pessoa_id,
                categoria=payload.categoria,
                usuario_id=usuario_id,
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PessoaExcluidaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.delete(
    "/{pessoa_id}",
    response_model=PessoaResponse,
    summary="Exclui logicamente uma pessoa (soft-delete)",
    responses={404: {"description": "Pessoa não encontrada"}},
)
def excluir_pessoa(
    pessoa_id: UUID,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Exclusão lógica da pessoa e de seus filhos (RN-CUM-007)."""
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Header X-Usuario-Id é obrigatório para exclusão.",
        )
    use_case = ExcluirPessoaUseCase(repository)
    try:
        return use_case.execute(ExcluirPessoaCommand(pessoa_id=pessoa_id, usuario_id=usuario_id))
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# -- Sub-recursos do agregado ------------------------------------------------------


@router.post(
    "/{pessoa_id}/enderecos",
    response_model=PessoaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adiciona um endereço à pessoa",
    responses={
        404: {"description": "Pessoa não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def adicionar_endereco(
    pessoa_id: UUID,
    payload: EnderecoPayload,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Adiciona endereço ao agregado; principal substitui a anterior (RN-CUM-005)."""
    use_case = AdicionarEnderecoUseCase(repository)
    try:
        return use_case.execute(
            AdicionarEnderecoCommand(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id,
                **payload.model_dump(),
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PessoaExcluidaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/{pessoa_id}/documentos",
    response_model=PessoaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adiciona um documento à pessoa",
    responses={
        404: {"description": "Pessoa não encontrada"},
        400: {"description": "Documento inválido"},
        409: {"description": "Documento duplicado"},
    },
)
def adicionar_documento(
    pessoa_id: UUID,
    payload: DocumentoPayload,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Adiciona documento com validação de CPF/CNPJ (RN-CUM-002/003/004/006)."""
    use_case = AdicionarDocumentoUseCase(repository)
    try:
        return use_case.execute(
            AdicionarDocumentoCommand(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id,
                **payload.model_dump(),
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except DocumentoDuplicadoError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except (DocumentoInvalidoError, ValueError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.post(
    "/{pessoa_id}/contatos",
    response_model=PessoaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adiciona um contato à pessoa",
    responses={
        404: {"description": "Pessoa não encontrada"},
        400: {"description": "Requisição inválida"},
    },
)
def adicionar_contato(
    pessoa_id: UUID,
    payload: ContatoPayload,
    repository: Annotated[PessoaRepository, Depends(get_pessoa_repository)],
    usuario_id: Annotated[UUID | None, Depends(_usuario_id_header)] = None,
) -> Pessoa:
    """Adiciona contato (TEL/EMAIL/REDES/WHATSAPP) ao agregado (RN-CUM-006)."""
    use_case = AdicionarContatoUseCase(repository)
    try:
        return use_case.execute(
            AdicionarContatoCommand(
                pessoa_id=pessoa_id,
                usuario_id=usuario_id,
                **payload.model_dump(),
            )
        )
    except PessoaNaoEncontradoError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except PessoaExcluidaError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


__all__ = ["router", "get_pessoa_repository"]

