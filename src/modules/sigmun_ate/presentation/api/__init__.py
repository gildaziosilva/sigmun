"""Endpoints REST de Atendimento ao Cidadão (DOM-ATE)."""

from __future__ import annotations

import logging
from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.modules.sigmun_ate.application.interfaces import (
    PublicadorEventos,
    RepositorioAtendimento,
    RepositorioAvaliacao,
    RepositorioChamada,
    RepositorioEncaminhamento,
    RepositorioFila,
    RepositorioGuiche,
    RepositorioSenha,
    RepositorioServicoAtendimento,
    RepositorioTriagem,
    RepositorioUnidadeAtendimento,
)
from src.modules.sigmun_ate.application.use_cases import (
    AbrirFilaUseCase,
    CancelarAtendimentoUseCase,
    ChamarSenhaUseCase,
    ConcluirEncaminhamentoUseCase,
    CriarEncaminhamentoUseCase,
    EmitirSenhaUseCase,
    FecharFilaUseCase,
    IniciarAtendimentoUseCase,
    MarcarSenhaAtendidaUseCase,
    RealizarTriagemUseCase,
    RechamarSenhaUseCase,
    RegistrarAvaliacaoUseCase,
)
from src.modules.sigmun_ate.domain.entities import (
    Atendimento,
    AvaliacaoAtendimento,
    Chamada,
    Encaminhamento,
    FilaAtendimento,
    Guiche,
    Senha,
    ServicoAtendimento,
    StatusAtendimento,
    StatusSenha,
    Triagem,
    UnidadeAtendimento,
)
from src.modules.sigmun_ate.domain.exceptions import (
    AtendimentoInvalidoError,
    AtendimentoJaConcluidoError,
    AtendimentoNaoIniciadoError,
    AvaliacaoInvalidaError,
    AvaliacaoJaRegistradaError,
    CanalInvalidoError,
    EncaminhamentoInvalidoError,
    EncaminhamentoJaConcluidoError,
    FilaFechadaError,
    FilaInvalidaError,
    GuicheInativoError,
    GuicheInvalidoError,
    MaximoRechamadasError,
    OperadorInvalidoError,
    SenhaAtendidaError,
    SenhaCanceladaError,
    SenhaInvalidaError,
    SenhaJaChamadaError,
    SenhaNaoChamadaError,
    UnidadeInvalidaError,
)
from src.modules.sigmun_ate.infrastructure.database.repositories import (
    SQLAlchemyAtendimentoRepository,
    SQLAlchemyAvaliacaoRepository,
    SQLAlchemyChamadaRepository,
    SQLAlchemyEncaminhamentoRepository,
    SQLAlchemyFilaRepository,
    SQLAlchemyGuicheRepository,
    SQLAlchemySenhaRepository,
    SQLAlchemyServicoAtendimentoRepository,
    SQLAlchemyTriagemRepository,
    SQLAlchemyUnidadeAtendimentoRepository,
)
from src.modules.sigmun_ate.infrastructure.messaging import PublicadorOutboxATE
from src.modules.sigmun_ate.presentation.schemas import (
    AtendimentoCancelarRequest,
    AtendimentoCancelarResponse,
    AtendimentoConcluirRequest,
    AtendimentoConcluirResponse,
    AtendimentoIniciarRequest,
    AtendimentoIniciarResponse,
    AtendimentoResponse,
    AvaliacaoCreateRequest,
    AvaliacaoResponse,
    EncaminhamentoConcluirResponse,
    EncaminhamentoCreateRequest,
    EncaminhamentoResponse,
    ErrorResponse,
    EstatisticasFilaResponse,
    EstatisticasUnidadeResponse,
    FilaCreateRequest,
    FilaResponse,
    GuicheResponse,
    MarcarSenhaAtendidaRequest,
    MarcarSenhaAtendidaResponse,
    RechamarSenhaRequest,
    RechamarSenhaResponse,
    SenhaChamadaRequest,
    SenhaChamadaResponse,
    SenhaCreateRequest,
    SenhaResponse,
    ServicoAtendimentoResponse,
    TriagemCreateRequest,
    TriagemResponse,
    UnidadeAtendimentoResponse,
)
from src.shared.presentation.dependencies import (
    JWTUsuarioContexto,
    UsuarioOpcional,
    exigir_papeis,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/ate", tags=["Atendimento ao Cidadão"])


# =============================================================================
# Dependency Injection
# =============================================================================


def get_triagem_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyTriagemRepository:
    return SQLAlchemyTriagemRepository(session)


def get_fila_repository(session: Annotated[Session, Depends(get_db)]) -> SQLAlchemyFilaRepository:
    return SQLAlchemyFilaRepository(session)


def get_senha_repository(session: Annotated[Session, Depends(get_db)]) -> SQLAlchemySenhaRepository:
    return SQLAlchemySenhaRepository(session)


def get_chamada_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyChamadaRepository:
    return SQLAlchemyChamadaRepository(session)


def get_atendimento_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyAtendimentoRepository:
    return SQLAlchemyAtendimentoRepository(session)


def get_avaliacao_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyAvaliacaoRepository:
    return SQLAlchemyAvaliacaoRepository(session)


def get_encaminhamento_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyEncaminhamentoRepository:
    return SQLAlchemyEncaminhamentoRepository(session)


def get_guiche_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyGuicheRepository:
    return SQLAlchemyGuicheRepository(session)


def get_unidade_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyUnidadeAtendimentoRepository:
    return SQLAlchemyUnidadeAtendimentoRepository(session)


def get_servico_repository(
    session: Annotated[Session, Depends(get_db)],
) -> SQLAlchemyServicoAtendimentoRepository:
    return SQLAlchemyServicoAtendimentoRepository(session)


def get_event_publisher(session: Annotated[Session, Depends(get_db)]) -> PublicadorOutboxATE:
    return PublicadorOutboxATE(session)


# =============================================================================
# Triagem
# =============================================================================


@router.post("/triagens", response_model=TriagemResponse, status_code=status.HTTP_201_CREATED)
def realizar_triagem(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: TriagemCreateRequest,
    repo_triagem: Annotated[SQLAlchemyTriagemRepository, Depends(get_triagem_repository)],
    repo_servico: Annotated[
        SQLAlchemyServicoAtendimentoRepository, Depends(get_servico_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import RealizarTriagemInputDTO
    from src.modules.sigmun_ate.infrastructure.database.repositories import (
        SQLAlchemyServicoAtendimentoRepository,
    )

    servico = repo_servico.buscar_por_id(str(request.servico_id))
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    use_case = RealizarTriagemUseCase(
        repo_triagem=repo_triagem,
        repo_servico=repo_servico,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            RealizarTriagemInputDTO(
                servico_id=str(request.servico_id),
                observacao=request.observacao,
                prioridade=request.prioridade,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    triagem = repo_triagem.buscar_por_id(result.triagem_id)
    return triagem


# =============================================================================
# Fila
# =============================================================================


@router.post("/filas", response_model=FilaResponse, status_code=status.HTTP_201_CREATED)
def abrir_fila(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: FilaCreateRequest,
    repo_fila: Annotated[SQLAlchemyFilaRepository, Depends(get_fila_repository)],
    repo_unidade: Annotated[
        SQLAlchemyUnidadeAtendimentoRepository, Depends(get_unidade_repository)
    ],
    repo_servico: Annotated[
        SQLAlchemyServicoAtendimentoRepository, Depends(get_servico_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import AbrirFilaInputDTO

    use_case = AbrirFilaUseCase(
        repo_fila=repo_fila,
        repo_unidade=repo_unidade,
        repo_servico=repo_servico,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            AbrirFilaInputDTO(
                unidade_id=str(request.unidade_id),
                servico_id=str(request.servico_id),
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    fila = repo_fila.buscar_por_id(result.fila_id)
    return fila


@router.post("/filas/{fila_id}/fechar", response_model=FilaResponse)
def fechar_fila(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    fila_id: UUID,
    repo_fila: Annotated[SQLAlchemyFilaRepository, Depends(get_fila_repository)],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import FecharFilaInputDTO

    use_case = FecharFilaUseCase(
        repo_fila=repo_fila,
        eventos=eventos,
    )

    try:
        result = use_case.execute(FecharFilaInputDTO(fila_id=str(fila_id)))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e

    fila = repo_fila.buscar_por_id(str(fila_id))
    return fila


# =============================================================================
# Senha
# =============================================================================


@router.post("/senhas", response_model=SenhaResponse, status_code=status.HTTP_201_CREATED)
def emitir_senha(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: SenhaCreateRequest,
    repo_senha: Annotated[SQLAlchemySenhaRepository, Depends(get_senha_repository)],
    repo_fila: Annotated[SQLAlchemyFilaRepository, Depends(get_fila_repository)],
    repo_servico: Annotated[
        SQLAlchemyServicoAtendimentoRepository, Depends(get_servico_repository)
    ],
    repo_triagem: Annotated[SQLAlchemyTriagemRepository, Depends(get_triagem_repository)],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import EmitirSenhaInputDTO

    use_case = EmitirSenhaUseCase(
        repo_senha=repo_senha,
        repo_fila=repo_fila,
        repo_servico=repo_servico,
        repo_triagem=repo_triagem,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            EmitirSenhaInputDTO(
                fila_id=str(request.fila_id),
                servico_id=str(request.servico_id),
                triagem_id=str(request.triagem_id),
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    senha = repo_senha.buscar_por_id(result.senha_id)
    return senha


@router.post("/senhas/{senha_id}/chamar", response_model=SenhaChamadaResponse)
def chamar_senha(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    senha_id: UUID,
    request: SenhaChamadaRequest,
    repo_senha: Annotated[SQLAlchemySenhaRepository, Depends(get_senha_repository)],
    repo_chamada: Annotated[SQLAlchemyChamadaRepository, Depends(get_chamada_repository)],
    repo_guiche: Annotated[SQLAlchemyGuicheRepository, Depends(get_guiche_repository)],
    repo_unidade: Annotated[
        SQLAlchemyUnidadeAtendimentoRepository, Depends(get_unidade_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import ChamarSenhaInputDTO

    use_case = ChamarSenhaUseCase(
        repo_senha=repo_senha,
        repo_chamada=repo_chamada,
        repo_guiche=repo_guiche,
        repo_unidade=repo_unidade,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            ChamarSenhaInputDTO(
                senha_id=str(senha_id),
                guiche_id=str(request.guiche_id),
                unidade_id=str(request.unidade_id),
                operador=request.operador,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return SenhaChamadaResponse(
        chamada_id=UUID(result.chamada_id),
        senha_id=UUID(result.senha_id),
        guiche_id=UUID(result.guiche_id),
        ordem=result.ordem,
    )


@router.post("/senhas/{senha_id}/rechamar", response_model=RechamarSenhaResponse)
def rechamar_senha(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    senha_id: UUID,
    repo_senha: Annotated[SQLAlchemySenhaRepository, Depends(get_senha_repository)],
    repo_chamada: Annotated[SQLAlchemyChamadaRepository, Depends(get_chamada_repository)],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import RechamarSenhaInputDTO

    use_case = RechamarSenhaUseCase(
        repo_senha=repo_senha,
        repo_chamada=repo_chamada,
        eventos=eventos,
    )

    try:
        result = use_case.execute(RechamarSenhaInputDTO(senha_id=str(senha_id)))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return RechamarSenhaResponse(
        chamada_id=UUID(result.chamada_id),
        tentativa=result.tentativa,
    )


@router.post("/senhas/{senha_id}/atender", response_model=MarcarSenhaAtendidaResponse)
def marcar_senha_atendida(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    senha_id: UUID,
    repo_senha: Annotated[SQLAlchemySenhaRepository, Depends(get_senha_repository)],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import MarcarSenhaAtendidaInputDTO

    use_case = MarcarSenhaAtendidaUseCase(
        repo_senha=repo_senha,
        eventos=eventos,
    )

    try:
        result = use_case.execute(MarcarSenhaAtendidaInputDTO(senha_id=str(senha_id)))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return MarcarSenhaAtendidaResponse(senha_id=UUID(result.senha_id))


# =============================================================================
# Atendimento
# =============================================================================


@router.post(
    "/atendimentos/iniciar",
    response_model=AtendimentoIniciarResponse,
    status_code=status.HTTP_201_CREATED,
)
def iniciar_atendimento(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: AtendimentoIniciarRequest,
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
    repo_chamada: Annotated[SQLAlchemyChamadaRepository, Depends(get_chamada_repository)],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import IniciarAtendimentoInputDTO

    use_case = IniciarAtendimentoUseCase(
        repo_atendimento=repo_atendimento,
        repo_chamada=repo_chamada,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            IniciarAtendimentoInputDTO(
                chamada_id=str(request.chamada_id),
                canal_id=str(request.canal_id),
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return AtendimentoIniciarResponse(atendimento_id=UUID(result.atendimento_id))


@router.post("/atendimentos/{atendimento_id}/concluir", response_model=AtendimentoConcluirResponse)
def concluir_atendimento(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    atendimento_id: UUID,
    request: AtendimentoConcluirRequest,
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import (
        ConcluirAtendimentoInputDTO,
        ConcluirAtendimentoUseCase,
    )

    use_case = ConcluirAtendimentoUseCase(
        repo_atendimento=repo_atendimento,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            ConcluirAtendimentoInputDTO(
                atendimento_id=str(atendimento_id),
                descricao=request.descricao,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return AtendimentoConcluirResponse(
        atendimento_id=UUID(result.atendimento_id),
        duracao_segundos=result.duracao_segundos,
    )


@router.post("/atendimentos/{atendimento_id}/cancelar", response_model=AtendimentoCancelarResponse)
def cancelar_atendimento(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    atendimento_id: UUID,
    request: AtendimentoCancelarRequest,
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import CancelarAtendimentoInputDTO

    use_case = CancelarAtendimentoUseCase(
        repo_atendimento=repo_atendimento,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            CancelarAtendimentoInputDTO(
                atendimento_id=str(atendimento_id),
                motivo=request.motivo,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return AtendimentoCancelarResponse(atendimento_id=UUID(result.atendimento_id))


@router.get("/atendimentos/{atendimento_id}", response_model=AtendimentoResponse)
def buscar_atendimento(
    usuario: UsuarioOpcional,
    atendimento_id: UUID,
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
):
    atendimento = repo_atendimento.buscar_por_id(str(atendimento_id))
    if not atendimento:
        raise HTTPException(status_code=404, detail="Atendimento não encontrado")
    return atendimento


@router.get("/atendimentos", response_model=list[AtendimentoResponse])
def listar_atendimentos_em_andamento(
    usuario: UsuarioOpcional,
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
):
    return repo_atendimento.listar_em_andamento()


# =============================================================================
# Avaliação
# =============================================================================


@router.post("/avaliacoes", response_model=AvaliacaoResponse, status_code=status.HTTP_201_CREATED)
def registrar_avaliacao(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: AvaliacaoCreateRequest,
    repo_avaliacao: Annotated[SQLAlchemyAvaliacaoRepository, Depends(get_avaliacao_repository)],
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import RegistrarAvaliacaoInputDTO

    use_case = RegistrarAvaliacaoUseCase(
        repo_avaliacao=repo_avaliacao,
        repo_atendimento=repo_atendimento,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            RegistrarAvaliacaoInputDTO(
                atendimento_id=str(request.atendimento_id),
                nota=request.nota,
                comentario=request.comentario,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    avaliacao = repo_avaliacao.buscar_por_id(result.avaliacao_id)
    return avaliacao


@router.get("/avaliacoes/{avaliacao_id}", response_model=AvaliacaoResponse)
def buscar_avaliacao(
    usuario: UsuarioOpcional,
    avaliacao_id: UUID,
    repo_avaliacao: Annotated[SQLAlchemyAvaliacaoRepository, Depends(get_avaliacao_repository)],
):
    avaliacao = repo_avaliacao.buscar_por_id(str(avaliacao_id))
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao


# =============================================================================
# Encaminhamento
# =============================================================================


@router.post(
    "/encaminhamentos", response_model=EncaminhamentoResponse, status_code=status.HTTP_201_CREATED
)
def criar_encaminhamento(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    request: EncaminhamentoCreateRequest,
    repo_encaminhamento: Annotated[
        SQLAlchemyEncaminhamentoRepository, Depends(get_encaminhamento_repository)
    ],
    repo_atendimento: Annotated[
        SQLAlchemyAtendimentoRepository, Depends(get_atendimento_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import CriarEncaminhamentoInputDTO

    use_case = CriarEncaminhamentoUseCase(
        repo_encaminhamento=repo_encaminhamento,
        repo_atendimento=repo_atendimento,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            CriarEncaminhamentoInputDTO(
                atendimento_id=str(request.atendimento_id),
                destino=request.destino,
                motivo=request.motivo,
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    encaminhamento = repo_encaminhamento.buscar_por_id(result.encaminhamento_id)
    return encaminhamento


@router.post(
    "/encaminhamentos/{encaminhamento_id}/concluir", response_model=EncaminhamentoConcluirResponse
)
def concluir_encaminhamento(
    usuario: Annotated[JWTUsuarioContexto, Depends(exigir_papeis("gestor", "admin", "atendimento"))],
    encaminhamento_id: UUID,
    repo_encaminhamento: Annotated[
        SQLAlchemyEncaminhamentoRepository, Depends(get_encaminhamento_repository)
    ],
    eventos: Annotated[PublicadorOutboxATE, Depends(get_event_publisher)],
):
    from src.modules.sigmun_ate.application.use_cases import ConcluirEncaminhamentoInputDTO

    use_case = ConcluirEncaminhamentoUseCase(
        repo_encaminhamento=repo_encaminhamento,
        eventos=eventos,
    )

    try:
        result = use_case.execute(
            ConcluirEncaminhamentoInputDTO(
                encaminhamento_id=str(encaminhamento_id),
            )
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return EncaminhamentoConcluirResponse(encaminhamento_id=UUID(result.encaminhamento_id))


@router.get("/encaminhamentos/{encaminhamento_id}", response_model=EncaminhamentoResponse)
def buscar_encaminhamento(
    usuario: UsuarioOpcional,
    encaminhamento_id: UUID,
    repo_encaminhamento: Annotated[
        SQLAlchemyEncaminhamentoRepository, Depends(get_encaminhamento_repository)
    ],
):
    encaminhamento = repo_encaminhamento.buscar_por_id(str(encaminhamento_id))
    if not encaminhamento:
        raise HTTPException(status_code=404, detail="Encaminhamento não encontrado")
    return encaminhamento


@router.get(
    "/atendimentos/{atendimento_id}/encaminhamentos", response_model=list[EncaminhamentoResponse]
)
def listar_encaminhamentos_por_atendimento(
    usuario: UsuarioOpcional,
    atendimento_id: UUID,
    repo_encaminhamento: Annotated[
        SQLAlchemyEncaminhamentoRepository, Depends(get_encaminhamento_repository)
    ],
):
    return repo_encaminhamento.buscar_por_atendimento(str(atendimento_id))


# =============================================================================
# Health Check
# =============================================================================


@router.get("/health")
def health_check(
    usuario: UsuarioOpcional,
):
    return {"status": "ok", "module": "ate"}


__all__ = ["router"]
