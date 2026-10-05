"""Endpoints do DOM-OUV (prefixo /api/v1/ouv)."""

from __future__ import annotations

from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import get_db
from src.shared.security.jwt import (
    JWTUsuarioContexto,
    get_current_user_hybrid,
    get_current_user_hybrid_optional,
    require_roles_hybrid,
)

from ...application.interfaces import (
    RepositorioAnexo,
    RepositorioDenuncia,
    RepositorioManifestacao,
    RepositorioPedidoLai,
    RepositorioProtocolo,
    RepositorioTramitacao,
)
from ...application.use_cases import (
    AlterarStatusInput,
    AlterarStatusUseCase,
    AvaliarManifestacaoInput,
    AvaliarManifestacaoUseCase,
    DecidirRecursoLaiInput,
    DecidirRecursoLaiUseCase,
    EncaminharDenunciaInput,
    EncaminharDenunciaUseCase,
    InterporRecursoLaiInput,
    InterporRecursoLaiUseCase,
    ListarDenunciasUseCase,
    ListarManifestacoesInput,
    ListarManifestacoesUseCase,
    ListarPedidosLaiUseCase,
    ObterEstatisticasUseCase,
    ObterManifestacaoUseCase,
    ProrrogarPrazoInput,
    ProrrogarPrazoUseCase,
    RegistrarDenunciaInput,
    RegistrarDenunciaUseCase,
    RegistrarManifestacaoInput,
    RegistrarManifestacaoUseCase,
    RegistrarPedidoLaiInput,
    RegistrarPedidoLaiUseCase,
    ResponderManifestacaoInput,
    ResponderManifestacaoUseCase,
)
from ...domain.exceptions import (
    AcessoNegadoError,
    DenunciaNaoEncontradaError,
    EstadoInvalidoError,
    ManifestacaoNaoEncontradaError,
    PedidoLaiNaoEncontradoError,
    ProtocoloJaExistenteError,
    RegraNegocioError,
)
from ...domain.services import (
    ServicoEstatisticas,
    ServicoLGPD,
)
from ...infrastructure.repositories import (
    SQLAlchemyAnexoRepository,
    SQLAlchemyDenunciaRepository,
    SQLAlchemyManifestacaoRepository,
    SQLAlchemyPedidoLaiRepository,
    SQLAlchemyProtocoloRepository,
    SQLAlchemyTramitacaoRepository,
)
from ..schemas import (
    AlterarStatusRequest,
    AvaliarManifestacaoRequest,
    DecidirRecursoLaiRequest,
    DenunciaResponse,
    EncaminharDenunciaRequest,
    EstatisticasResponse,
    InterporRecursoLaiRequest,
    ManifestacaoResponse,
    PageResponse,
    PedidoLaiResponse,
    ProrrogarPrazoRequest,
    RegistrarDenunciaRequest,
    RegistrarManifestacaoRequest,
    RegistrarPedidoLaiRequest,
    ResponderManifestacaoRequest,
)

router = APIRouter(prefix="/api/v1/ouv", tags=["Ouvidoria FalaBR / e-OUV"])

# ==================== Dependencies ====================


def get_protocolo_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioProtocolo:
    return SQLAlchemyProtocoloRepository(session)


def get_anexo_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioAnexo:
    return SQLAlchemyAnexoRepository(session)


def get_tramitacao_repo(session: Annotated[Session, Depends(get_db)]) -> RepositorioTramitacao:
    return SQLAlchemyTramitacaoRepository(session)


def get_manifestacao_repo(
    session: Annotated[Session, Depends(get_db)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
) -> RepositorioManifestacao:
    return SQLAlchemyManifestacaoRepository(session, anexo_repo, tramitacao_repo)


def get_denuncia_repo(
    session: Annotated[Session, Depends(get_db)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
) -> RepositorioDenuncia:
    return SQLAlchemyDenunciaRepository(session, anexo_repo, tramitacao_repo)


def get_pedido_lai_repo(
    session: Annotated[Session, Depends(get_db)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
) -> RepositorioPedidoLai:
    return SQLAlchemyPedidoLaiRepository(session, anexo_repo, tramitacao_repo)


def get_servico_estatisticas(
    repo_m: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
):
    return ServicoEstatisticas(repo_m, repo_d, repo_l)


# ==================== Segurança — ADR-0008 ====================
#
# Matriz de papéis conforme ADR-0008 seções 2.3 e 2.6.
#
#   PAPEL_OUVIDOR / PAPEL_CORREGEDOR — tratamento integral + dados sensíveis
#   PAPEL_AUDITOR                   — leitura + dados sensíveis, sem escrita
#   PAPEL_ADMIN                     — metadados agregados, SEM dados sensíveis
#
# A separação entre "tratamento" e "consulta" reflete a decisão 2.6: prorrogação
# e avaliação alteram a relação de atendimento com o cidadão e não são ações
# administrativas de sistema.

PAPEIS_TRATAMENTO: tuple[str, ...] = ("ouvidor", "corregedor")
PAPEIS_CONSULTA: tuple[str, ...] = ("ouvidor", "corregedor", "auditor", "admin")
PAPEIS_DADOS_SENSITIVEIS: tuple[str, ...] = ("ouvidor", "corregedor", "auditor")

# Dependências prontas (equivalentes a require_roles_hybrid).
depende_tratamento = require_roles_hybrid(*PAPEIS_TRATAMENTO)
depende_consulta = require_roles_hybrid(*PAPEIS_CONSULTA)


def _autorizado_para_dados_sensiveis(usuario: JWTUsuarioContexto | None) -> bool:
    """Indica se o usuário pode ver a identificação do denunciante.

    ADR-0008 §2.3: `admin` NÃO tem acesso ao dado sensível. A administração
    técnica do sistema não é autoridade funcional sobre a identificação de um
    denunciante.
    """
    if usuario is None:
        return False
    return usuario.possui_algum_papel(*PAPEIS_DADOS_SENSITIVEIS)


def _pode_acessar_dados_sensiveis(usuario: JWTUsuarioContexto | None) -> bool:
    """Alias semântico usado pelos mappers de resposta."""
    return _autorizado_para_dados_sensiveis(usuario)


# ==================== Helpers ====================


def _dados_cidadao(cidadao, usuario_autorizado: bool):
    """Serializa os dados do cidadão conforme a autorização do solicitante.

    ADR-0008 §2.4 — sigilo por **negação total**, não mascaramento parcial.
    Mascarar (`***.123.***-45`) confirmaria ao solicitante a existência do CPF,
    o que já é informação protegida (Lei 12.527/2011 art. 24; LGPD art. 46).

    Quando o solicitante NÃO é autorizado, o bloco é **ausente** (None).
    Quando é autorizado, os dados seguem mascarados para exibição em tela,
    conforme RN-OUV-030.
    """
    if cidadao is None or not usuario_autorizado:
        return None
    return ServicoLGPD.mascarar_para_exibicao(cidadao)


def _to_manifestacao_response(m, usuario_autorizado: bool = False) -> ManifestacaoResponse:
    return ManifestacaoResponse(
        id=str(m.id),
        protocolo={"numero": m.protocolo.numero, "ano": m.protocolo.ano} if m.protocolo else None,
        tipo=m.tipo.value,
        status=m.status.value,
        prioridade=m.prioridade.value,
        assunto=m.assunto,
        descricao=m.descricao,
        cidadao=_dados_cidadao(m.cidadao, usuario_autorizado),
        canal=m.canal.value,
        orgao_destino=m.orgao_destino,
        setor_responsavel=m.setor_responsavel,
        prazo={
            "data_limite": m.prazo.data_limite,
            "dias_uteis": m.prazo.dias_uteis,
            "prorrogado": m.prazo.prorrogado,
            "data_prorrogacao": m.prazo.data_prorrogacao,
            "justificativa_prorrogacao": m.prazo.justificativa_prorrogacao,
        }
        if m.prazo
        else None,
        anexos=[
            {
                "id": str(a.id),
                "nome_arquivo": a.nome_arquivo,
                "tipo_mime": a.tipo_mime,
                "tamanho_bytes": a.tamanho_bytes,
                "url": a.url,
                "descricao": a.descricao,
                "criado_em": a.criado_em,
            }
            for a in m.anexos
        ],
        tramitacoes=[],  # Carregado separadamente se necessário
        resposta=m.resposta,
        forma_resposta=m.forma_resposta.value if m.forma_resposta else None,
        data_resposta=m.data_resposta,
        respondido_por=m.respondido_por,
        avaliacao_cidadao=m.avaliacao_cidadao,
        comentario_avaliacao=m.comentario_avaliacao,
        created_at=m.created_at,
        updated_at=m.updated_at,
        created_by=m.created_by,
        updated_by=m.updated_by,
        is_deleted=m.is_deleted,
    )


def _to_denuncia_response(d, usuario_autorizado: bool = False) -> DenunciaResponse:
    # ADR-0008 §2.4: sem autorização, `cidadao` é ausente e `servidor_envolvido`
    # também é omitido — identificar o servidor expõe dado protegido ligado à
    # pessoa que denunciou. Com autorização, delega ao domínio (RN-OUV-030),
    # que devolve o bloco mascarado via `get_dados_sigilosos`.
    dados_cidadao = None
    if usuario_autorizado:
        try:
            dados_cidadao = d.get_dados_sigilosos(usuario_autorizado=True) or None
        except AcessoNegadoError:
            dados_cidadao = None

    return DenunciaResponse(
        id=str(d.id),
        protocolo={"numero": d.protocolo.numero, "ano": d.protocolo.ano} if d.protocolo else None,
        tipo=d.tipo.value,
        status=d.status.value,
        prioridade=d.prioridade.value,
        assunto=d.assunto,
        descricao=d.descricao,
        cidadao=dados_cidadao,
        canal=d.canal.value,
        orgao_destino=d.orgao_destino,
        setor_responsavel=d.setor_responsavel,
        prazo={
            "data_limite": d.prazo.data_limite,
            "dias_uteis": d.prazo.dias_uteis,
            "prorrogado": d.prazo.prorrogado,
            "data_prorrogacao": d.prazo.data_prorrogacao,
            "justificativa_prorrogacao": d.prazo.justificativa_prorrogacao,
        }
        if d.prazo
        else None,
        anexos=[
            {
                "id": str(a.id),
                "nome_arquivo": a.nome_arquivo,
                "tipo_mime": a.tipo_mime,
                "tamanho_bytes": a.tamanho_bytes,
                "url": a.url,
                "descricao": a.descricao,
                "criado_em": a.criado_em,
            }
            for a in d.anexos
        ],
        tramitacoes=[],
        resposta=d.resposta,
        forma_resposta=d.forma_resposta.value if d.forma_resposta else None,
        data_resposta=d.data_resposta,
        respondido_por=d.respondido_por,
        tipo_denuncia=d.tipo_denuncia.value,
        envolve_servidor_publico=d.envolve_servidor_publico,
        servidor_envolvido=d.servidor_envolvido if usuario_autorizado else None,
        valor_envolvido=d.valor_envolvido,
        local_fato=d.local_fato,
        data_fato=d.data_fato,
        sigilo_denunciante=d.sigilo_denunciante,
        encaminhada_mp=d.encaminhada_mp,
        encaminhada_pf=d.encaminhada_pf,
        encaminhada_tce=d.encaminhada_tce,
        numero_inquerito=d.numero_inquerito,
        resultado_investigacao=d.resultado_investigacao,
        created_at=d.created_at,
        updated_at=d.updated_at,
        created_by=d.created_by,
        updated_by=d.updated_by,
        is_deleted=d.is_deleted,
    )


def _to_pedido_lai_response(p, usuario_autorizado: bool = False) -> PedidoLaiResponse:
    return PedidoLaiResponse(
        id=str(p.id),
        protocolo={"numero": p.protocolo.numero, "ano": p.protocolo.ano} if p.protocolo else None,
        tipo=p.tipo.value,
        status=p.status.value,
        prioridade=p.prioridade.value,
        assunto=p.assunto,
        descricao=p.descricao,
        cidadao=_dados_cidadao(p.cidadao, usuario_autorizado),
        canal=p.canal.value,
        orgao_destino=p.orgao_destino,
        setor_responsavel=p.setor_responsavel,
        prazo={
            "data_limite": p.prazo.data_limite,
            "dias_uteis": p.prazo.dias_uteis,
            "prorrogado": p.prazo.prorrogado,
            "data_prorrogacao": p.prazo.data_prorrogacao,
            "justificativa_prorrogacao": p.prazo.justificativa_prorrogacao,
        }
        if p.prazo
        else None,
        anexos=[
            {
                "id": str(a.id),
                "nome_arquivo": a.nome_arquivo,
                "tipo_mime": a.tipo_mime,
                "tamanho_bytes": a.tamanho_bytes,
                "url": a.url,
                "descricao": a.descricao,
                "criado_em": a.criado_em,
            }
            for a in p.anexos
        ],
        tramitacoes=[],
        resposta=p.resposta,
        forma_resposta=p.forma_resposta.value if p.forma_resposta else None,
        data_resposta=p.data_resposta,
        respondido_por=p.respondido_por,
        informacao_solicitada=p.informacao_solicitada,
        fundamentacao=p.fundamentacao,
        nivel_sigilo=p.nivel_sigilo.value,
        fundamentacao_sigilo=p.fundamentacao_sigilo,
        dados_pessoais_terceiros=p.dados_pessoais_terceiros,
        formato_resposta=p.formato_resposta,
        is_recurso=p.is_recurso,
        pedido_original_id=p.pedido_original_id,
        decisao_recurso=p.decisao_recurso,
        data_decisao_recurso=p.data_decisao_recurso,
        created_at=p.created_at,
        updated_at=p.updated_at,
        created_by=p.created_by,
        updated_by=p.updated_by,
        is_deleted=p.is_deleted,
    )


# ==================== Endpoints - Manifestações ====================


@router.post("/manifestacoes", response_model=ManifestacaoResponse, status_code=201)
def registrar_manifestacao(
    payload: RegistrarManifestacaoRequest,
    repo: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    protocolo_repo: Annotated[RepositorioProtocolo, Depends(get_protocolo_repo)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
    # ADR-0008 §2.2: criação permanece anônima (a LAI exige protocolar sem
    # conta). Quando há token, `autor_id` deriva dele; quando não há, fica vazio.
    usuario: Annotated[JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)],
):
    """Registra nova manifestação (sugestão, elogio, reclamação, solicitação)."""
    autor_id = str(usuario.usuario_id) if usuario else ""
    try:
        dto = RegistrarManifestacaoInput(
            tipo=payload.tipo,
            assunto=payload.assunto,
            descricao=payload.descricao,
            cidadao_nome=payload.cidadao_nome,
            cidadao_cpf=payload.cidadao_cpf,
            cidadao_email=payload.cidadao_email,
            cidadao_telefone=payload.cidadao_telefone,
            cidadao_endereco=payload.cidadao_endereco,
            cidadao_anonimo=payload.cidadao_anonimo,
            canal=payload.canal,
            orgao_destino=payload.orgao_destino,
            setor_responsavel=payload.setor_responsavel,
            prioridade=payload.prioridade,
            anexos=[a.model_dump() for a in payload.anexos],
            autor_id=autor_id,
        )
        m = RegistrarManifestacaoUseCase(repo, protocolo_repo, anexo_repo, tramitacao_repo).execute(
            dto
        )
    except (RegraNegocioError, ProtocoloJaExistenteError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    # O autor acabou de registrar: devolve os próprios dados mascarados.
    return _to_manifestacao_response(m, usuario_autorizado=True)


@router.get("/manifestacoes", response_model=PageResponse)
def listar_manifestacoes(
    repo: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_consulta)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: str | None = Query(None),
    tipo: str | None = Query(None),
    orgao_destino: str | None = Query(None),
    cidadao_nome: str | None = Query(None),
    data_inicio: date | None = Query(None),  # noqa: B008 — padrão FastAPI
    data_fim: date | None = Query(None),  # noqa: B008 — padrão FastAPI
):
    """Lista manifestações com paginação e filtros."""
    autorizado = _autorizado_para_dados_sensiveis(usuario)
    dto = ListarManifestacoesInput(
        page=page,
        page_size=page_size,
        filtros={
            k: v
            for k, v in {
                "status": status,
                "tipo": tipo,
                "orgao_destino": orgao_destino,
                "cidadao_nome": cidadao_nome,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
            }.items()
            if v is not None
        },
    )
    resultado = ListarManifestacoesUseCase(repo).execute(dto)
    return PageResponse(
        items=[_to_manifestacao_response(m, autorizado) for m in resultado["items"]],
        total=resultado["total"],
        page=resultado["page"],
        page_size=resultado["page_size"],
        pages=resultado["pages"],
    )


@router.get("/manifestacoes/{identificador}", response_model=ManifestacaoResponse)
def obter_manifestacao(
    identificador: str,
    repo: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(get_current_user_hybrid)],
):
    """Obtém manifestação por ID ou protocolo."""
    # ADR-0008 §2.7: `usuario_perfil`/`usuario_autorizado` deixam de ser query
    # parameters — quem os enviava, os controlava. A autorização vem do token.
    autorizado = _autorizado_para_dados_sensiveis(usuario)
    try:
        m = ObterManifestacaoUseCase(repo, repo_d, repo_l).execute(
            identificador, usuario.login, autorizado
        )
        if hasattr(m, "tipo_denuncia"):  # É denúncia
            return _to_denuncia_response(m, autorizado)
        if hasattr(m, "informacao_solicitada"):  # É pedido LAI
            return _to_pedido_lai_response(m, autorizado)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return _to_manifestacao_response(m, autorizado)


@router.post("/manifestacoes/{manifestacao_id}/responder", response_model=ManifestacaoResponse)
def responder_manifestacao(
    manifestacao_id: str,
    payload: ResponderManifestacaoRequest,
    repo_m: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Registra resposta à manifestação."""
    try:
        dto = ResponderManifestacaoInput(
            manifestacao_id=manifestacao_id,
            resposta=payload.resposta,
            forma_resposta=payload.forma_resposta,
            respondido_por=str(usuario.usuario_id),
        )
        m = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l).execute(dto)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_manifestacao_response(m)


@router.post("/manifestacoes/{manifestacao_id}/status", response_model=ManifestacaoResponse)
def alterar_status(
    manifestacao_id: str,
    payload: AlterarStatusRequest,
    repo_m: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Altera status da manifestação (RN-OUV-010)."""
    try:
        dto = AlterarStatusInput(
            manifestacao_id=manifestacao_id,
            novo_status=payload.novo_status,
            observacao=payload.observacao,
            usuario_id=str(usuario.usuario_id),
        )
        m = AlterarStatusUseCase(repo_m, repo_d, repo_l).execute(dto)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_manifestacao_response(m)


@router.post("/manifestacoes/{manifestacao_id}/prorrogar", response_model=ManifestacaoResponse)
def prorrogar_prazo(
    manifestacao_id: str,
    payload: ProrrogarPrazoRequest,
    repo_m: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Prorroga prazo de resposta (LAI Art. 11 §1º, RN-OUV-020)."""
    try:
        dto = ProrrogarPrazoInput(
            manifestacao_id=manifestacao_id,
            justificativa=payload.justificativa,
            usuario_id=str(usuario.usuario_id),
        )
        m = ProrrogarPrazoUseCase(repo_m, repo_d, repo_l).execute(dto)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_manifestacao_response(m)


@router.post("/manifestacoes/{manifestacao_id}/avaliar", response_model=ManifestacaoResponse)
def avaliar_manifestacao(
    manifestacao_id: str,
    payload: AvaliarManifestacaoRequest,
    repo: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Registra avaliação do cidadão (1-5)."""
    try:
        dto = AvaliarManifestacaoInput(
            manifestacao_id=manifestacao_id,
            nota=payload.nota,
            comentario=payload.comentario,
        )
        m = AvaliarManifestacaoUseCase(repo).execute(dto)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_manifestacao_response(m)


# ==================== Endpoints - Denúncias ====================


@router.post("/denuncias", response_model=DenunciaResponse, status_code=201)
def registrar_denuncia(
    payload: RegistrarDenunciaRequest,
    repo: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    protocolo_repo: Annotated[RepositorioProtocolo, Depends(get_protocolo_repo)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
    usuario: Annotated[JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)],
):
    """Registra nova denúncia (pode ser anônima - RN-OUV-002, RN-OUV-030)."""
    try:
        dto = RegistrarDenunciaInput(
            assunto=payload.assunto,
            descricao=payload.descricao,
            tipo_denuncia=payload.tipo_denuncia,
            envolve_servidor_publico=payload.envolve_servidor_publico,
            servidor_envolvido=payload.servidor_envolvido,
            valor_envolvido=payload.valor_envolvido,
            local_fato=payload.local_fato,
            data_fato=payload.data_fato,
            cidadao_nome=payload.cidadao_nome,
            cidadao_cpf=payload.cidadao_cpf,
            cidadao_email=payload.cidadao_email,
            cidadao_telefone=payload.cidadao_telefone,
            cidadao_endereco=payload.cidadao_endereco,
            cidadao_anonimo=payload.cidadao_anonimo,
            canal=payload.canal,
            orgao_destino=payload.orgao_destino,
            setor_responsavel=payload.setor_responsavel,
            prioridade=payload.prioridade,
            anexos=[a.model_dump() for a in payload.anexos],
            autor_id=str(usuario.usuario_id) if usuario else "",
        )
        d = RegistrarDenunciaUseCase(repo, protocolo_repo, anexo_repo, tramitacao_repo).execute(dto)
    except (RegraNegocioError, ProtocoloJaExistenteError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    # O autor acabou de registrar: devolve os proprios dados mascarados.
    return _to_denuncia_response(d, usuario_autorizado=True)


@router.get("/denuncias", response_model=PageResponse)
def listar_denuncias(
    repo: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_consulta)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: str | None = Query(None),
    tipo_denuncia: str | None = Query(None),
    orgao_destino: str | None = Query(None),
    anonima: bool | None = Query(None),
    data_inicio: date | None = Query(None),  # noqa: B008 — padrão FastAPI
    data_fim: date | None = Query(None),  # noqa: B008 — padrão FastAPI
):
    """Lista denúncias com paginação e filtros."""
    autorizado = _autorizado_para_dados_sensiveis(usuario)
    dto = ListarManifestacoesInput(
        page=page,
        page_size=page_size,
        filtros={
            k: v
            for k, v in {
                "status": status,
                "tipo_denuncia": tipo_denuncia,
                "orgao_destino": orgao_destino,
                "anonima": anonima,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
            }.items()
            if v is not None
        },
    )
    resultado = ListarDenunciasUseCase(repo).execute(dto)
    return PageResponse(
        items=[_to_denuncia_response(d, autorizado) for d in resultado["items"]],
        total=resultado["total"],
        page=resultado["page"],
        page_size=resultado["page_size"],
        pages=resultado["pages"],
    )


@router.post("/denuncias/{denuncia_id}/encaminhar", response_model=DenunciaResponse)
def encaminhar_denuncia(
    denuncia_id: str,
    payload: EncaminharDenunciaRequest,
    repo: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Encaminha denúncia a órgão externo (MP, PF, TCE)."""
    try:
        dto = EncaminharDenunciaInput(
            denuncia_id=denuncia_id,
            orgao=payload.orgao,
            numero_processo=payload.numero_processo,
            usuario_id=str(usuario.usuario_id),
        )
        d = EncaminharDenunciaUseCase(repo).execute(dto)
    except DenunciaNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_denuncia_response(d)


# ==================== Endpoints - Pedidos LAI ====================


@router.post("/pedidos-lai", response_model=PedidoLaiResponse, status_code=201)
def registrar_pedido_lai(
    payload: RegistrarPedidoLaiRequest,
    repo: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    protocolo_repo: Annotated[RepositorioProtocolo, Depends(get_protocolo_repo)],
    anexo_repo: Annotated[RepositorioAnexo, Depends(get_anexo_repo)],
    tramitacao_repo: Annotated[RepositorioTramitacao, Depends(get_tramitacao_repo)],
    usuario: Annotated[JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)],
):
    """Registra novo pedido de acesso à informação (LAI - Lei 12.527/2011)."""
    try:
        dto = RegistrarPedidoLaiInput(
            assunto=payload.assunto,
            descricao=payload.descricao,
            informacao_solicitada=payload.informacao_solicitada,
            fundamentacao=payload.fundamentacao,
            nivel_sigilo=payload.nivel_sigilo,
            fundamentacao_sigilo=payload.fundamentacao_sigilo,
            dados_pessoais_terceiros=payload.dados_pessoais_terceiros,
            formato_resposta=payload.formato_resposta,
            cidadao_nome=payload.cidadao_nome,
            cidadao_cpf=payload.cidadao_cpf,
            cidadao_email=payload.cidadao_email,
            cidadao_telefone=payload.cidadao_telefone,
            cidadao_endereco=payload.cidadao_endereco,
            canal=payload.canal,
            orgao_destino=payload.orgao_destino,
            setor_responsavel=payload.setor_responsavel,
            prioridade=payload.prioridade,
            anexos=[a.model_dump() for a in payload.anexos],
            autor_id=str(usuario.usuario_id) if usuario else "",
        )
        p = RegistrarPedidoLaiUseCase(repo, protocolo_repo, anexo_repo, tramitacao_repo).execute(
            dto
        )
    except (RegraNegocioError, ProtocoloJaExistenteError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_pedido_lai_response(p, usuario_autorizado=True)


@router.get("/pedidos-lai", response_model=PageResponse)
def listar_pedidos_lai(
    repo: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_consulta)],
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: str | None = Query(None),
    nivel_sigilo: str | None = Query(None),
    is_recurso: bool | None = Query(None),
    data_inicio: date | None = Query(None),  # noqa: B008 — padrão FastAPI
    data_fim: date | None = Query(None),  # noqa: B008 — padrão FastAPI
):
    """Lista pedidos LAI com paginação e filtros."""
    autorizado = _autorizado_para_dados_sensiveis(usuario)
    dto = ListarManifestacoesInput(
        page=page,
        page_size=page_size,
        filtros={
            k: v
            for k, v in {
                "status": status,
                "nivel_sigilo": nivel_sigilo,
                "is_recurso": is_recurso,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
            }.items()
            if v is not None
        },
    )
    resultado = ListarPedidosLaiUseCase(repo).execute(dto)
    return PageResponse(
        items=[_to_pedido_lai_response(p, autorizado) for p in resultado["items"]],
        total=resultado["total"],
        page=resultado["page"],
        page_size=resultado["page_size"],
        pages=resultado["pages"],
    )


@router.post("/pedidos-lai/{pedido_id}/recurso", response_model=PedidoLaiResponse)
def interpor_recurso_lai(
    pedido_id: str,
    payload: InterporRecursoLaiRequest,
    repo: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    # ADR-0008 §2.2: o cidadão pode recorrer sem conta, como no registro.
    usuario: Annotated[JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)],
):
    """Interpõe recurso de pedido LAI negado (LAI Art. 15)."""
    try:
        dto = InterporRecursoLaiInput(
            pedido_original_id=pedido_id,
            autor_id=str(usuario.usuario_id) if usuario else "",
        )
        recurso = InterporRecursoLaiUseCase(repo).execute(dto)
    except PedidoLaiNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_pedido_lai_response(recurso, usuario_autorizado=True)


@router.post("/pedidos-lai/{recurso_id}/decidir-recurso", response_model=PedidoLaiResponse)
def decidir_recurso_lai(
    recurso_id: str,
    payload: DecidirRecursoLaiRequest,
    repo: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_tratamento)],
):
    """Decide sobre recurso LAI interposto."""
    try:
        dto = DecidirRecursoLaiInput(
            recurso_id=recurso_id,
            deferido=payload.deferido,
            fundamentacao=payload.fundamentacao,
            usuario_id=str(usuario.usuario_id),
        )
        recurso = DecidirRecursoLaiUseCase(repo).execute(dto)
    except PedidoLaiNaoEncontradoError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (RegraNegocioError, EstadoInvalidoError) as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return _to_pedido_lai_response(recurso)


# ==================== Endpoints - Estatísticas ====================


@router.get("/estatisticas", response_model=EstatisticasResponse)
def obter_estatisticas(
    servico: Annotated[object, Depends(get_servico_estatisticas)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_consulta)],
    ano: int | None = Query(None),
):
    """Obtém estatísticas e indicadores da ouvidoria."""
    return ObterEstatisticasUseCase(servico).execute(ano)


@router.get("/manifestacoes-vencendo")
def manifestacoes_vencendo_prazo(
    repo_m: Annotated[RepositorioManifestacao, Depends(get_manifestacao_repo)],
    repo_d: Annotated[RepositorioDenuncia, Depends(get_denuncia_repo)],
    repo_l: Annotated[RepositorioPedidoLai, Depends(get_pedido_lai_repo)],
    usuario: Annotated[JWTUsuarioContexto, Depends(depende_consulta)],
    dias: int = Query(5, ge=1, le=30),
):
    """Lista manifestações com prazo vencendo em X dias."""
    servico = ServicoEstatisticas(repo_m, repo_d, repo_l)
    vencendo = servico.manifestacoes_vencendo_prazo(dias)
    return {
        "total": len(vencendo),
        "dias": dias,
        "items": [
            {
                "id": str(m.id),
                "protocolo": m.protocolo.codigo if m.protocolo else "",
                "assunto": m.assunto,
                "status": m.status.value,
                "prazo_limite": m.prazo.data_limite if m.prazo else None,
                "dias_restantes": m.prazo.dias_restantes if m.prazo else 0,
            }
            for m in vencendo
        ],
    }


__all__ = ["router"]
