"""Endpoints do DOM-EDU (prefixo /api/v1/edu)."""
from __future__ import annotations
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.core.infrastructure.database.session import get_db
from ...application.interfaces import (RepositorioAluno, RepositorioDistribuicaoMerenda, RepositorioItemMerenda, RepositorioLancamentoDiario, RepositorioMatricula, RepositorioPassagemTransporte, RepositorioRotaTransporte)
from ...application.use_cases import (AtivarRotaTransporteUseCase, CadastrarAlunoInput, CadastrarAlunoUseCase, CadastrarItemMerendaInput, CadastrarItemMerendaUseCase, CadastrarRotaTransporteInput, CadastrarRotaTransporteUseCase, CancelarMatriculaUseCase, ConcluirMatriculaUseCase, DistribuirMerendaInput, DistribuirMerendaUseCase, InativarRotaTransporteUseCase, RealizarMatriculaInput, RealizarMatriculaUseCase, RegistrarLancamentoDiarioInput, RegistrarLancamentoDiarioUseCase, RegistrarPassagemInput, RegistrarPassagemUseCase, ReporEstoqueMerendaUseCase, TransferirMatriculaUseCase)
from ...domain.exceptions import (AlunoNaoEncontradoError, DomEduDomainError, ItemMerendaNaoEncontradoError, MatriculaNaoEncontradaError, RotaNaoEncontradaError)
from ...infrastructure.repositories.sqlalchemy_aluno_repository import SQLAlchemyAlunoRepository
from ...infrastructure.repositories.sqlalchemy_edu_repository import (SQLAlchemyDistribuicaoMerendaRepository, SQLAlchemyItemMerendaRepository, SQLAlchemyLancamentoDiarioRepository, SQLAlchemyMatriculaRepository, SQLAlchemyPassagemTransporteRepository, SQLAlchemyRotaTransporteRepository)
from ..schemas.edu_schemas import (AlunoCreateRequest, AlunoResponse, DistribuicaoMerendaCreateRequest, DistribuicaoMerendaResponse, ItemMerendaCreateRequest, ItemMerendaResponse, LancamentoDiarioCreateRequest, LancamentoDiarioResponse, MatriculaCreateRequest, MatriculaResponse, PassagemTransporteCreateRequest, PassagemTransporteResponse, RotaTransporteCreateRequest, RotaTransporteResponse)
router = APIRouter(prefix="/api/v1/edu", tags=["Educacao Municipal"])

def get_aluno_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioAluno:
    return SQLAlchemyAlunoRepository(session)

def get_matricula_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioMatricula:
    return SQLAlchemyMatriculaRepository(session)

def get_diario_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioLancamentoDiario:
    return SQLAlchemyLancamentoDiarioRepository(session)

def get_rota_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioRotaTransporte:
    return SQLAlchemyRotaTransporteRepository(session)

def get_passagem_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioPassagemTransporte:
    return SQLAlchemyPassagemTransporteRepository(session)

def get_item_merenda_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioItemMerenda:
    return SQLAlchemyItemMerendaRepository(session)

def get_distribuicao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioDistribuicaoMerenda:
    return SQLAlchemyDistribuicaoMerendaRepository(session)

def _to_aluno(a) -> AlunoResponse:
    return AlunoResponse(id=a.id, nome=a.nome, cpf=a.cpf, data_nascimento=a.data_nascimento, sexo=a.sexo.value, nome_mae=a.nome_mae, telefone=a.telefone, endereco=a.endereco, status=a.status.value, created_at=a.created_at, updated_at=a.updated_at)

def _to_matricula(m) -> MatriculaResponse:
    return MatriculaResponse(id=m.id, aluno_id=m.aluno_id, escola=m.escola, serie=m.serie, turno=m.turno, ano_letivo=m.ano_letivo, data_matricula=m.data_matricula, status=m.status.value, escola_destino=m.escola_destino, motivo=m.motivo, created_at=m.created_at)

def _to_lancamento(l) -> LancamentoDiarioResponse:
    return LancamentoDiarioResponse(id=l.id, matricula_id=l.matricula_id, data=l.data, presente=l.presente, nota=l.nota, observacao=l.observacao, created_at=l.created_at)

def _to_rota(r) -> RotaTransporteResponse:
    return RotaTransporteResponse(id=r.id, identificacao=r.identificacao, veiculo=r.veiculo, motorista=r.motorista, vagas=r.vagas, turno=r.turno, status=r.status.value, created_at=r.created_at)

def _to_passagem(p) -> PassagemTransporteResponse:
    return PassagemTransporteResponse(id=p.id, rota_id=p.rota_id, matricula_id=p.matricula_id, data=p.data, created_at=p.created_at)

def _to_item(i) -> ItemMerendaResponse:
    return ItemMerendaResponse(id=i.id, nome=i.nome, tipo=i.tipo, estoque=i.estoque, estoque_minimo=i.estoque_minimo, created_at=i.created_at)

def _to_distribuicao(d) -> DistribuicaoMerendaResponse:
    return DistribuicaoMerendaResponse(id=d.id, matricula_id=d.matricula_id, item_id=d.item_id, quantidade=d.quantidade, data=d.data, refeicao=d.refeicao, created_at=d.created_at)

@router.post("/alunos", status_code=201)
def cadastrar_aluno(payload: AlunoCreateRequest, repo: Annotated[RepositorioAluno, Depends(get_aluno_repo)]):
    try:
        a = CadastrarAlunoUseCase(repo).execute(CadastrarAlunoInput(nome=payload.nome, cpf=payload.cpf, data_nascimento=payload.data_nascimento, sexo=payload.sexo, nome_mae=payload.nome_mae, telefone=payload.telefone, endereco=payload.endereco, autor_id=payload.created_by))
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CPF ja cadastrado por outro aluno (RN-EDU-001)")
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_aluno(a)

@router.get("/alunos")
def listar_alunos(repo: Annotated[RepositorioAluno, Depends(get_aluno_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_aluno(a) for a in repo.list_all(page=page, page_size=page_size)]

@router.get("/alunos/{aluno_id}")
def obter_aluno(aluno_id: str, repo: Annotated[RepositorioAluno, Depends(get_aluno_repo)]):
    a = repo.get_by_id(aluno_id)
    if a is None:
        raise HTTPException(status_code=404, detail="Aluno nao encontrado")
    return _to_aluno(a)

@router.post("/matriculas", status_code=201)
def realizar_matricula(payload: MatriculaCreateRequest, repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)], alunos: Annotated[RepositorioAluno, Depends(get_aluno_repo)]):
    try:
        m = RealizarMatriculaUseCase(repo, alunos).execute(RealizarMatriculaInput(aluno_id=payload.aluno_id, escola=payload.escola, serie=payload.serie, turno=payload.turno, ano_letivo=payload.ano_letivo, autor_id=payload.created_by))
    except AlunoNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_matricula(m)

@router.get("/matriculas")
def listar_matriculas(repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_matricula(m) for m in repo.list_all(page=page, page_size=page_size)]

@router.get("/matriculas/{matricula_id}")
def obter_matricula(matricula_id: str, repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)]):
    m = repo.get_by_id(matricula_id)
    if m is None:
        raise HTTPException(status_code=404, detail="Matricula nao encontrada")
    return _to_matricula(m)

@router.post("/matriculas/{matricula_id}/transferir")
def transferir_matricula(matricula_id: str, repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)], escola_destino: str = Query(...), motivo: str = Query("")):
    try:
        return _to_matricula(TransferirMatriculaUseCase(repo).execute(matricula_id, escola_destino, motivo))
    except MatriculaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/matriculas/{matricula_id}/cancelar")
def cancelar_matricula(matricula_id: str, repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)], motivo: str = Query("")):
    try:
        return _to_matricula(CancelarMatriculaUseCase(repo).execute(matricula_id, motivo))
    except MatriculaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/matriculas/{matricula_id}/concluir")
def concluir_matricula(matricula_id: str, repo: Annotated[RepositorioMatricula, Depends(get_matricula_repo)]):
    try:
        return _to_matricula(ConcluirMatriculaUseCase(repo).execute(matricula_id))
    except MatriculaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))


@router.post("/diario", status_code=201)
def registrar_lancamento(payload: LancamentoDiarioCreateRequest, repo: Annotated[RepositorioLancamentoDiario, Depends(get_diario_repo)], matriculas: Annotated[RepositorioMatricula, Depends(get_matricula_repo)]):
    try:
        l = RegistrarLancamentoDiarioUseCase(repo, matriculas).execute(RegistrarLancamentoDiarioInput(matricula_id=payload.matricula_id, data=payload.data, presente=payload.presente, nota=payload.nota, observacao=payload.observacao, autor_id=payload.created_by))
    except MatriculaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_lancamento(l)

@router.get("/diario")
def listar_diario(repo: Annotated[RepositorioLancamentoDiario, Depends(get_diario_repo)], matricula_id: str | None = Query(None), page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    if matricula_id:
        return [_to_lancamento(l) for l in repo.list_by_matricula(matricula_id)]
    return [_to_lancamento(l) for l in repo.list_all(page=page, page_size=page_size)]

@router.post("/transporte/rotas", status_code=201)
def cadastrar_rota(payload: RotaTransporteCreateRequest, repo: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)]):
    try:
        r = CadastrarRotaTransporteUseCase(repo).execute(CadastrarRotaTransporteInput(identificacao=payload.identificacao, motorista=payload.motorista, veiculo=payload.veiculo, vagas=payload.vagas, turno=payload.turno, autor_id=payload.created_by))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_rota(r)

@router.get("/transporte/rotas")
def listar_rotas(repo: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_rota(r) for r in repo.list_all(page=page, page_size=page_size)]

@router.post("/transporte/rotas/{rota_id}/inativar")
def inativar_rota(rota_id: str, repo: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)]):
    try:
        return _to_rota(InativarRotaTransporteUseCase(repo).execute(rota_id))
    except RotaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/transporte/rotas/{rota_id}/ativar")
def ativar_rota(rota_id: str, repo: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)]):
    try:
        return _to_rota(AtivarRotaTransporteUseCase(repo).execute(rota_id))
    except RotaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/transporte/passagens", status_code=201)
def registrar_passagem(payload: PassagemTransporteCreateRequest, repo: Annotated[RepositorioPassagemTransporte, Depends(get_passagem_repo)], rotas: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)], matriculas: Annotated[RepositorioMatricula, Depends(get_matricula_repo)]):
    try:
        p = RegistrarPassagemUseCase(repo, rotas, matriculas).execute(RegistrarPassagemInput(rota_id=payload.rota_id, matricula_id=payload.matricula_id, data=payload.data, autor_id=payload.created_by))
    except (RotaNaoEncontradaError, MatriculaNaoEncontradaError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_passagem(p)

@router.get("/transporte/passagens")
def listar_passagens(repo: Annotated[RepositorioPassagemTransporte, Depends(get_passagem_repo)], rota_id: str | None = Query(None), page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    if rota_id:
        return [_to_passagem(p) for p in repo.list_by_rota(rota_id)]
    return [_to_passagem(p) for p in repo.list_all(page=page, page_size=page_size)]


@router.post("/merenda/itens", status_code=201)
def cadastrar_item_merenda(payload: ItemMerendaCreateRequest, repo: Annotated[RepositorioItemMerenda, Depends(get_item_merenda_repo)]):
    try:
        i = CadastrarItemMerendaUseCase(repo).execute(CadastrarItemMerendaInput(nome=payload.nome, tipo=payload.tipo, estoque=payload.estoque, estoque_minimo=payload.estoque_minimo, autor_id=payload.created_by))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_item(i)

@router.get("/merenda/itens")
def listar_itens_merenda(repo: Annotated[RepositorioItemMerenda, Depends(get_item_merenda_repo)], page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    return [_to_item(i) for i in repo.list_all(page=page, page_size=page_size)]

@router.post("/merenda/itens/{item_id}/repor")
def repor_item_merenda(item_id: str, repo: Annotated[RepositorioItemMerenda, Depends(get_item_merenda_repo)], quantidade: float = Query(0)):
    try:
        return _to_item(ReporEstoqueMerendaUseCase(repo).execute(item_id, quantidade))
    except ItemMerendaNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))

@router.post("/merenda/distribuicoes", status_code=201)
def distribuir_merenda(payload: DistribuicaoMerendaCreateRequest, repo: Annotated[RepositorioDistribuicaoMerenda, Depends(get_distribuicao_repo)], itens: Annotated[RepositorioItemMerenda, Depends(get_item_merenda_repo)], matriculas: Annotated[RepositorioMatricula, Depends(get_matricula_repo)]):
    try:
        d = DistribuirMerendaUseCase(repo, itens, matriculas).execute(DistribuirMerendaInput(matricula_id=payload.matricula_id, item_id=payload.item_id, quantidade=payload.quantidade, refeicao=payload.refeicao, data=payload.data, autor_id=payload.created_by))
    except (MatriculaNaoEncontradaError, ItemMerendaNaoEncontradoError) as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except DomEduDomainError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    return _to_distribuicao(d)

@router.get("/merenda/distribuicoes")
def listar_distribuicoes(repo: Annotated[RepositorioDistribuicaoMerenda, Depends(get_distribuicao_repo)], matricula_id: str | None = Query(None), page: int = Query(1, ge=1), page_size: int = Query(20, ge=1, le=100)):
    if matricula_id:
        return [_to_distribuicao(d) for d in repo.list_by_matricula(matricula_id)]
    return [_to_distribuicao(d) for d in repo.list_all(page=page, page_size=page_size)]


@router.get("/transporte/rotas/{rota_id}")
def obter_rota(rota_id: str, repo: Annotated[RepositorioRotaTransporte, Depends(get_rota_repo)]):
    r = repo.get_by_id(rota_id)
    if r is None:
        raise HTTPException(status_code=404, detail="Rota não encontrada")
    return _to_rota(r)


@router.get("/merenda/itens/{item_id}")
def obter_item_merenda(item_id: str, repo: Annotated[RepositorioItemMerenda, Depends(get_item_merenda_repo)]):
    i = repo.get_by_id(item_id)
    if i is None:
        raise HTTPException(status_code=404, detail="Item de merenda não encontrado")
    return _to_item(i)


@router.patch("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: str, payload: dict, repo: Annotated[RepositorioAluno, Depends(get_aluno_repo)]):
    from ...domain.exceptions import AlunoNaoEncontradoError, RegraNegocioError
    a = repo.get_by_id(aluno_id)
    if a is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    # Atualiza apenas campos permitidos
    if "nome" in payload:
        a.nome = payload["nome"]
    if "cpf" in payload:
        a.cpf = payload["cpf"]
    if "data_nascimento" in payload:
        a.data_nascimento = payload["data_nascimento"]
    if "sexo" in payload:
        from ...domain.entities.aluno import Sexo
        a.sexo = Sexo(payload["sexo"])
    if "nome_mae" in payload:
        a.nome_mae = payload["nome_mae"]
    if "telefone" in payload:
        a.telefone = payload["telefone"]
    if "endereco" in payload:
        a.endereco = payload["endereco"]
    if "status" in payload:
        from ...domain.entities.aluno import StatusAluno
        a.status = StatusAluno(payload["status"])
    try:
        a.validar()
    except RegraNegocioError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    from datetime import datetime
    a.updated_at = datetime.utcnow()
    repo.save(a)
    return _to_aluno(a)

