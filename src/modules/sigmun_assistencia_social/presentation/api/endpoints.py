"""Endpoints do DOM-ASS (prefixo /api/v1/ass)."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db

from ...application.interfaces import (
    RepositorioAtendimento,
    RepositorioBeneficio,
    RepositorioFamilia,
    RepositorioPessoa,
    RepositorioUnidade,
)
from ...application.use_cases import (
    AprovarBeneficioUseCase,
    AtualizarFamiliaInput,
    AtualizarFamiliaUseCase,
    AtualizarPessoaInput,
    AtualizarPessoaUseCase,
    AtualizarUnidadeInput,
    AtualizarUnidadeUseCase,
    CadastrarFamiliaInput,
    CadastrarFamiliaUseCase,
    CadastrarPessoaInput,
    CadastrarPessoaUseCase,
    CadastrarUnidadeInput,
    CadastrarUnidadeUseCase,
    CancelarBeneficioUseCase,
    EntregarBeneficioUseCase,
    ExcluirFamiliaUseCase,
    ExcluirPessoaUseCase,
    ExcluirUnidadeUseCase,
    NegarBeneficioUseCase,
    RegistrarAtendimentoInput,
    RegistrarAtendimentoUseCase,
    SolicitarBeneficioInput,
    SolicitarBeneficioUseCase,
)
from ...domain.entities import (
    AtendimentoSocial,
    BeneficioEventual,
    FamiliaCadUnico,
    PessoaCadUnico,
    UnidadeAssistencia,
)
from ...domain.exceptions import (
    BeneficioNaoEncontradoError,
    DomAssDomainError,
    FamiliaNaoEncontradaError,
    PessoaNaoEncontradaError,
    UnidadeNaoEncontradaError,
)
from ...infrastructure.repositories import (
    SQLAlchemyAtendimentoRepository,
    SQLAlchemyBeneficioRepository,
    SQLAlchemyFamiliaRepository,
    SQLAlchemyPessoaRepository,
    SQLAlchemyUnidadeRepository,
)
from ..schemas import (
    AtendimentoCreateRequest,
    AtendimentoResponse,
    BeneficioCreateRequest,
    BeneficioResponse,
    FamiliaCreateRequest,
    FamiliaResponse,
    FamiliaUpdateRequest,
    PessoaCreateRequest,
    PessoaResponse,
    PessoaUpdateRequest,
    UnidadeCreateRequest,
    UnidadeResponse,
    UnidadeUpdateRequest,
)

router = APIRouter(prefix="/api/v1/ass", tags=["Assistência Social"])

# Todos os ports de repositorio expoem get_by_id(str).
_Repo = (
    RepositorioFamilia
    | RepositorioPessoa
    | RepositorioUnidade
    | RepositorioBeneficio
    | RepositorioAtendimento
)


def get_familia_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioFamilia:
    return SQLAlchemyFamiliaRepository(session)


def get_pessoa_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioPessoa:
    return SQLAlchemyPessoaRepository(session)


def get_unidade_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioUnidade:
    return SQLAlchemyUnidadeRepository(session)


def get_beneficio_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioBeneficio:
    return SQLAlchemyBeneficioRepository(session)


def get_atendimento_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioAtendimento:
    return SQLAlchemyAtendimentoRepository(session)


def _to_familia(f: FamiliaCadUnico) -> FamiliaResponse:
    return FamiliaResponse(
        id=f.id,
        nis=f.nis,
        responsavel_nome=f.responsavel_nome,
        responsavel_cpf=f.responsavel_cpf,
        endereco=f.endereco,
        telefone=f.telefone,
        renda_per_capita=f.renda_per_capita,
        quantidade_pessoas=f.quantidade_pessoas,
        status=f.status.value,
        created_at=f.created_at,
        updated_at=f.updated_at,
    )


def _to_pessoa(p: PessoaCadUnico) -> PessoaResponse:
    return PessoaResponse(
        id=p.id,
        familia_id=p.familia_id,
        nome=p.nome,
        cpf=p.cpf,
        data_nascimento=p.data_nascimento,
        sexo=p.sexo.value,
        nome_mae=p.nome_mae,
        parentesco=p.parentesco,
        escolaridade=p.escolaridade,
        ocupacao=p.ocupacao,
        renda=p.renda,
        created_at=p.created_at,
        updated_at=p.updated_at,
    )


def _to_unidade(u: UnidadeAssistencia) -> UnidadeResponse:
    return UnidadeResponse(
        id=u.id,
        codigo=u.codigo,
        nome=u.nome,
        tipo=u.tipo.value,
        endereco=u.endereco,
        telefone=u.telefone,
        email=u.email,
        responsavel=u.responsavel,
        status=u.status.value,
        created_at=u.created_at,
        updated_at=u.updated_at,
    )


def _to_beneficio(b: BeneficioEventual) -> BeneficioResponse:
    return BeneficioResponse(
        id=b.id,
        familia_id=b.familia_id,
        tipo=b.tipo.value,
        descricao=b.descricao,
        valor=b.valor,
        quantidade=b.quantidade,
        data_solicitacao=b.data_solicitacao,
        data_aprovacao=b.data_aprovacao,
        data_entrega=b.data_entrega,
        status=b.status.value,
        unidade_id=b.unidade_id or None,
        observacao=b.observacao,
        created_at=b.created_at,
        updated_at=b.updated_at,
    )


def _to_atendimento(a: AtendimentoSocial) -> AtendimentoResponse:
    data = a.data.date() if isinstance(a.data, datetime) else a.data
    return AtendimentoResponse(
        id=a.id,
        pessoa_id=a.pessoa_id,
        unidade_id=a.unidade_id,
        tipo=a.tipo.value,
        data=data,
        descricao=a.descricao,
        encaminhamento=a.encaminhamento,
        profissional=a.profissional,
        created_at=a.created_at,
    )


def _obter(repo: _Repo, entidade_id: str) -> Any:
    """Busca por id tolerando UUID malformado (evita 500 em input inválido)."""
    try:
        return repo.get_by_id(entidade_id)
    except (ValueError, AttributeError):
        return None


@router.post("/familias", status_code=201)
def cadastrar_familia(
    payload: FamiliaCreateRequest, repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)]
) -> FamiliaResponse:
    try:
        f = CadastrarFamiliaUseCase(repo).execute(
            CadastrarFamiliaInput(
                nis=payload.nis,
                responsavel_nome=payload.responsavel_nome,
                responsavel_cpf=payload.responsavel_cpf,
                endereco=payload.endereco,
                telefone=payload.telefone,
                renda_per_capita=payload.renda_per_capita,
                quantidade_pessoas=payload.quantidade_pessoas,
                autor_id=payload.created_by,
            )
        )
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="NIS ja cadastrado para outra familia (RN-ASS-001)",
        ) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_familia(f)


@router.get("/familias")
def listar_familias(
    repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[FamiliaResponse]:
    return [_to_familia(f) for f in repo.list_all(page=page, page_size=page_size)]


@router.get("/familias/nis/{nis}")
def obter_familia_por_nis(
    nis: str, repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)]
) -> FamiliaResponse:
    f = repo.get_by_nis(nis)
    if f is None:
        raise HTTPException(status_code=404, detail="Familia nao encontrada no CadUnico")
    return _to_familia(f)


@router.get("/familias/{familia_id}")
def obter_familia(
    familia_id: str, repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)]
) -> FamiliaResponse:
    f = _obter(repo, familia_id)
    if f is None:
        raise HTTPException(status_code=404, detail="Familia nao encontrada no CadUnico")
    return _to_familia(f)


@router.get("/familias/{familia_id}/pessoas")
def listar_pessoas_da_familia(
    familia_id: str,
    familias: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
    pessoas: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
) -> list[PessoaResponse]:
    if _obter(familias, familia_id) is None:
        raise HTTPException(status_code=404, detail="Familia nao encontrada no CadUnico")
    return [_to_pessoa(p) for p in pessoas.list_by_familia(familia_id)]


@router.get("/familias/{familia_id}/beneficios")
def listar_beneficios_da_familia(
    familia_id: str,
    familias: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
    beneficios: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)],
) -> list[BeneficioResponse]:
    if _obter(familias, familia_id) is None:
        raise HTTPException(status_code=404, detail="Familia nao encontrada no CadUnico")
    return [_to_beneficio(b) for b in beneficios.list_by_familia(familia_id)]


@router.post("/pessoas", status_code=201)
def cadastrar_pessoa(
    payload: PessoaCreateRequest,
    repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
    familias: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
) -> PessoaResponse:
    try:
        p = CadastrarPessoaUseCase(repo, familias).execute(
            CadastrarPessoaInput(
                familia_id=payload.familia_id,
                nome=payload.nome,
                cpf=payload.cpf,
                data_nascimento=payload.data_nascimento,
                sexo=payload.sexo,
                nome_mae=payload.nome_mae,
                parentesco=payload.parentesco,
                escolaridade=payload.escolaridade,
                ocupacao=payload.ocupacao,
                renda=payload.renda,
                autor_id=payload.created_by,
            )
        )
    except FamiliaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="CPF ja cadastrado para outra pessoa (RN-ASS-002)",
        ) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_pessoa(p)


@router.get("/pessoas")
def listar_pessoas(
    repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[PessoaResponse]:
    return [_to_pessoa(p) for p in repo.list_all(page=page, page_size=page_size)]


@router.get("/pessoas/cpf/{cpf}")
def obter_pessoa_por_cpf(
    cpf: str, repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)]
) -> PessoaResponse:
    p = repo.get_by_cpf(cpf)
    if p is None:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada no CadUnico")
    return _to_pessoa(p)


@router.get("/pessoas/{pessoa_id}")
def obter_pessoa(
    pessoa_id: str, repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)]
) -> PessoaResponse:
    p = _obter(repo, pessoa_id)
    if p is None:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada no CadUnico")
    return _to_pessoa(p)


@router.get("/pessoas/{pessoa_id}/atendimentos")
def listar_atendimentos_da_pessoa(
    pessoa_id: str,
    pessoas: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
    atendimentos: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)],
) -> list[AtendimentoResponse]:
    if _obter(pessoas, pessoa_id) is None:
        raise HTTPException(status_code=404, detail="Pessoa nao encontrada no CadUnico")
    return [_to_atendimento(a) for a in atendimentos.list_by_pessoa(pessoa_id)]


@router.post("/unidades", status_code=201)
def cadastrar_unidade(
    payload: UnidadeCreateRequest, repo: Annotated[RepositorioUnidade, Depends(get_unidade_repo)]
) -> UnidadeResponse:
    try:
        u = CadastrarUnidadeUseCase(repo).execute(
            CadastrarUnidadeInput(
                codigo=payload.codigo,
                nome=payload.nome,
                tipo=payload.tipo,
                endereco=payload.endereco,
                telefone=payload.telefone,
                email=payload.email,
                responsavel=payload.responsavel,
                autor_id=payload.created_by,
            )
        )
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Codigo de unidade ja cadastrado"
        ) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_unidade(u)


@router.get("/unidades")
def listar_unidades(
    repo: Annotated[RepositorioUnidade, Depends(get_unidade_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[UnidadeResponse]:
    return [_to_unidade(u) for u in repo.list_all(page=page, page_size=page_size)]


@router.get("/unidades/{unidade_id}")
def obter_unidade(
    unidade_id: str, repo: Annotated[RepositorioUnidade, Depends(get_unidade_repo)]
) -> UnidadeResponse:
    u = _obter(repo, unidade_id)
    if u is None:
        raise HTTPException(status_code=404, detail="Unidade de assistencia nao encontrada")
    return _to_unidade(u)


@router.get("/unidades/{unidade_id}/atendimentos")
def listar_atendimentos_da_unidade(
    unidade_id: str,
    unidades: Annotated[RepositorioUnidade, Depends(get_unidade_repo)],
    atendimentos: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)],
) -> list[AtendimentoResponse]:
    if _obter(unidades, unidade_id) is None:
        raise HTTPException(status_code=404, detail="Unidade de assistencia nao encontrada")
    return [_to_atendimento(a) for a in atendimentos.list_by_unidade(unidade_id)]


@router.post("/beneficios", status_code=201)
def solicitar_beneficio(
    payload: BeneficioCreateRequest,
    repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)],
    familias: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
    unidades: Annotated[RepositorioUnidade, Depends(get_unidade_repo)],
) -> BeneficioResponse:
    try:
        b = SolicitarBeneficioUseCase(repo, familias, unidades).execute(
            SolicitarBeneficioInput(
                familia_id=payload.familia_id,
                tipo=payload.tipo,
                descricao=payload.descricao,
                valor=payload.valor,
                quantidade=payload.quantidade,
                unidade_id=payload.unidade_id,
                observacao=payload.observacao,
                autor_id=payload.created_by,
            )
        )
    except (FamiliaNaoEncontradaError, UnidadeNaoEncontradaError) as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_beneficio(b)


@router.get("/beneficios")
def listar_beneficios(
    repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[BeneficioResponse]:
    return [_to_beneficio(b) for b in repo.list_all(page=page, page_size=page_size)]


@router.get("/beneficios/{beneficio_id}")
def obter_beneficio(
    beneficio_id: str, repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)]
) -> BeneficioResponse:
    b = _obter(repo, beneficio_id)
    if b is None:
        raise HTTPException(status_code=404, detail="Beneficio nao encontrado")
    return _to_beneficio(b)


@router.post("/beneficios/{beneficio_id}/aprovar")
def aprovar_beneficio(
    beneficio_id: str, repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)]
) -> BeneficioResponse:
    try:
        return _to_beneficio(AprovarBeneficioUseCase(repo).execute(beneficio_id))
    except BeneficioNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post("/beneficios/{beneficio_id}/negar")
def negar_beneficio(
    beneficio_id: str,
    repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)],
    justificativa: str = Query(""),
) -> BeneficioResponse:
    try:
        return _to_beneficio(NegarBeneficioUseCase(repo).execute(beneficio_id, justificativa))
    except BeneficioNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post("/beneficios/{beneficio_id}/entregar")
def entregar_beneficio(
    beneficio_id: str, repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)]
) -> BeneficioResponse:
    try:
        return _to_beneficio(EntregarBeneficioUseCase(repo).execute(beneficio_id))
    except BeneficioNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post("/beneficios/{beneficio_id}/cancelar")
def cancelar_beneficio(
    beneficio_id: str, repo: Annotated[RepositorioBeneficio, Depends(get_beneficio_repo)]
) -> BeneficioResponse:
    try:
        return _to_beneficio(CancelarBeneficioUseCase(repo).execute(beneficio_id))
    except BeneficioNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post("/atendimentos", status_code=201)
def registrar_atendimento(
    payload: AtendimentoCreateRequest,
    repo: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)],
    pessoas: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
    unidades: Annotated[RepositorioUnidade, Depends(get_unidade_repo)],
) -> AtendimentoResponse:
    try:
        a = RegistrarAtendimentoUseCase(repo, pessoas, unidades).execute(
            RegistrarAtendimentoInput(
                pessoa_id=payload.pessoa_id,
                unidade_id=payload.unidade_id,
                tipo=payload.tipo,
                data=payload.data,
                descricao=payload.descricao,
                encaminhamento=payload.encaminhamento,
                profissional=payload.profissional,
                autor_id=payload.created_by,
            )
        )
    except (PessoaNaoEncontradaError, UnidadeNaoEncontradaError) as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_atendimento(a)


@router.get("/atendimentos")
def listar_atendimentos(
    repo: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> list[AtendimentoResponse]:
    return [_to_atendimento(a) for a in repo.list_all(page=page, page_size=page_size)]


@router.get("/atendimentos/{atendimento_id}")
def obter_atendimento(
    atendimento_id: str, repo: Annotated[RepositorioAtendimento, Depends(get_atendimento_repo)]
) -> AtendimentoResponse:
    a = _obter(repo, atendimento_id)
    if a is None:
        raise HTTPException(status_code=404, detail="Atendimento nao encontrado")
    return _to_atendimento(a)


@router.patch("/familias/{familia_id}")
def atualizar_familia(
    familia_id: str,
    payload: FamiliaUpdateRequest,
    repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
) -> FamiliaResponse:
    try:
        f = AtualizarFamiliaUseCase(repo).execute(
            AtualizarFamiliaInput(
                familia_id=familia_id,
                nis=payload.nis,
                responsavel_nome=payload.responsavel_nome,
                responsavel_cpf=payload.responsavel_cpf,
                endereco=payload.endereco,
                telefone=payload.telefone,
                renda_per_capita=payload.renda_per_capita,
                quantidade_pessoas=payload.quantidade_pessoas,
                status=payload.status,
                autor_id=payload.created_by,
            )
        )
    except FamiliaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_familia(f)


@router.delete("/familias/{familia_id}")
def excluir_familia(
    familia_id: str, repo: Annotated[RepositorioFamilia, Depends(get_familia_repo)]
) -> FamiliaResponse:
    try:
        return _to_familia(ExcluirFamiliaUseCase(repo).execute(familia_id))
    except FamiliaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.patch("/pessoas/{pessoa_id}")
def atualizar_pessoa(
    pessoa_id: str,
    payload: PessoaUpdateRequest,
    repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)],
    familias: Annotated[RepositorioFamilia, Depends(get_familia_repo)],
) -> PessoaResponse:
    try:
        p = AtualizarPessoaUseCase(repo, familias).execute(
            AtualizarPessoaInput(
                pessoa_id=pessoa_id,
                familia_id=payload.familia_id,
                nome=payload.nome,
                cpf=payload.cpf,
                data_nascimento=payload.data_nascimento,
                sexo=payload.sexo,
                nome_mae=payload.nome_mae,
                parentesco=payload.parentesco,
                escolaridade=payload.escolaridade,
                ocupacao=payload.ocupacao,
                renda=payload.renda,
                autor_id=payload.created_by,
            )
        )
    except (PessoaNaoEncontradaError, FamiliaNaoEncontradaError) as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_pessoa(p)


@router.delete("/pessoas/{pessoa_id}")
def excluir_pessoa(
    pessoa_id: str, repo: Annotated[RepositorioPessoa, Depends(get_pessoa_repo)]
) -> PessoaResponse:
    try:
        return _to_pessoa(ExcluirPessoaUseCase(repo).execute(pessoa_id))
    except PessoaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.patch("/unidades/{unidade_id}")
def atualizar_unidade(
    unidade_id: str,
    payload: UnidadeUpdateRequest,
    repo: Annotated[RepositorioUnidade, Depends(get_unidade_repo)],
) -> UnidadeResponse:
    try:
        u = AtualizarUnidadeUseCase(repo).execute(
            AtualizarUnidadeInput(
                unidade_id=unidade_id,
                codigo=payload.codigo,
                nome=payload.nome,
                tipo=payload.tipo,
                endereco=payload.endereco,
                telefone=payload.telefone,
                email=payload.email,
                responsavel=payload.responsavel,
                status=payload.status,
                autor_id=payload.created_by,
            )
        )
    except UnidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_unidade(u)


@router.delete("/unidades/{unidade_id}")
def excluir_unidade(
    unidade_id: str, repo: Annotated[RepositorioUnidade, Depends(get_unidade_repo)]
) -> UnidadeResponse:
    try:
        return _to_unidade(ExcluirUnidadeUseCase(repo).execute(unidade_id))
    except UnidadeNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except DomAssDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
