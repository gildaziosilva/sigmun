"""Repositórios SQLAlchemy do DOM-OUV."""

from __future__ import annotations

from datetime import date
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Session

from ...application.interfaces import (
    RepositorioAnexo,
    RepositorioDenuncia,
    RepositorioManifestacao,
    RepositorioPedidoLai,
    RepositorioProtocolo,
    RepositorioTramitacao,
)
from ...domain.entities import Denuncia, Manifestacao, PedidoLai, Prioridade
from ...domain.exceptions import (
    DenunciaNaoEncontradaError,
    ManifestacaoNaoEncontradaError,
    PedidoLaiNaoEncontradoError,
)
from ...domain.value_objects import (
    Anexo,
    CanalRecebimento,
    DadosCidadao,
    FormaResposta,
    NivelSigilo,
    PrazoResposta,
    Protocolo,
    StatusManifestacao,
    TipoDenuncia,
    TipoManifestacao,
)
from ..database import (
    AnexoModel,
    DenunciaModel,
    ManifestacaoModel,
    PedidoLaiModel,
    ProtocoloModel,
    TramitacaoModel,
)


# `session.get(Model, None)` retorna `None` de forma segura no SQLAlchemy, o
# que produz exatamente o mesmo resultado de "registro inexistente" sem que a
# consulta seja sequer executada.
def _como_uuid(valor: str) -> UUID | None:
    """Converte a string em UUID, tolerando identificador malformado.

    Uma rota pode receber um identificador inválido (``/manifestacoes/abc``).
    Sem esta guarda, ``UUID("abc")`` levanta ``ValueError`` e a requisição
    termina em HTTP 500. Retornando ``None``, o repositório responde "não
    encontrado" logo de cara e a rota devolve 404 — a semântica correta.
    """
    try:
        return UUID(str(valor))
    except (ValueError, AttributeError, TypeError):
        return None


class SQLAlchemyProtocoloRepository(RepositorioProtocolo):
    """Repositório de protocolos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def obter_proximo_sequencial(self, ano: int) -> int:
        protocolo = self._session.query(ProtocoloModel).filter(ProtocoloModel.ano == ano).first()
        if protocolo:
            protocolo.sequencial += 1
            self._session.flush()
            return protocolo.sequencial
        novo = ProtocoloModel(ano=ano, sequencial=1)
        self._session.add(novo)
        self._session.flush()
        return 1

    def existe_protocolo(self, codigo: str) -> bool:
        return (
            self._session.query(ManifestacaoModel)
            .filter(ManifestacaoModel.protocolo == codigo)
            .first()
            is not None
        )

    def registrar_protocolo(self, protocolo: Protocolo) -> None:
        # Já tratado em obter_proximo_sequencial
        pass


class SQLAlchemyAnexoRepository(RepositorioAnexo):
    """Repositório de anexos."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, anexo: Anexo, manifestacao_id: UUID) -> Anexo:
        model = AnexoModel(
            id=UUID(anexo.id),
            manifestacao_id=manifestacao_id,
            nome_arquivo=anexo.nome_arquivo,
            tipo_mime=anexo.tipo_mime,
            tamanho_bytes=anexo.tamanho_bytes,
            url=anexo.url,
            descricao=anexo.descricao,
            criado_em=anexo.criado_em,
        )
        self._session.add(model)
        self._session.flush()
        return anexo

    def get_by_id(self, anexo_id: UUID) -> Anexo | None:
        model = self._session.get(AnexoModel, anexo_id)
        return self._to_entity(model) if model else None

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list[Anexo]:
        models = (
            self._session.query(AnexoModel)
            .filter(AnexoModel.manifestacao_id == manifestacao_id)
            .order_by(AnexoModel.criado_em)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AnexoModel) -> Anexo:
        return Anexo(
            id=str(model.id),
            nome_arquivo=model.nome_arquivo,
            tipo_mime=model.tipo_mime,
            tamanho_bytes=model.tamanho_bytes,
            url=model.url,
            descricao=model.descricao or "",
            criado_em=model.criado_em,
        )


class SQLAlchemyTramitacaoRepository(RepositorioTramitacao):
    """Repositório de tramitações."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(
        self,
        manifestacao_id: UUID,
        status_anterior: StatusManifestacao | None,
        status_novo: StatusManifestacao,
        observacao: str,
        usuario_id: str,
    ) -> None:
        model = TramitacaoModel(
            manifestacao_id=manifestacao_id,
            status_anterior=status_anterior.value if status_anterior else None,
            status_novo=status_novo.value,
            observacao=observacao,
            usuario_id=usuario_id,
        )
        self._session.add(model)
        self._session.flush()

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list[dict]:
        models = (
            self._session.query(TramitacaoModel)
            .filter(TramitacaoModel.manifestacao_id == manifestacao_id)
            .order_by(TramitacaoModel.created_at)
            .all()
        )
        return [
            {
                "id": str(m.id),
                "status_anterior": m.status_anterior,
                "status_novo": m.status_novo,
                "observacao": m.observacao,
                "usuario_id": m.usuario_id,
                "created_at": m.created_at,
            }
            for m in models
        ]


class SQLAlchemyManifestacaoRepository(RepositorioManifestacao):
    """Repositório de manifestações genéricas."""

    def __init__(
        self,
        session: Session,
        anexo_repo: SQLAlchemyAnexoRepository,
        tramitacao_repo: SQLAlchemyTramitacaoRepository,
    ) -> None:
        self._session = session
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo

    def save(self, manifestacao: Manifestacao) -> Manifestacao:
        is_new = (
            manifestacao.id is None
            or self._session.get(ManifestacaoModel, UUID(manifestacao.id)) is None
        )

        if is_new:
            model = ManifestacaoModel(
                id=UUID(manifestacao.id),
                protocolo=manifestacao.protocolo.codigo if manifestacao.protocolo else "",
                ano_protocolo=manifestacao.protocolo.ano if manifestacao.protocolo else 0,
                numero_protocolo=int(manifestacao.protocolo.numero)
                if manifestacao.protocolo
                else 0,
                tipo=manifestacao.tipo.value,
                status=manifestacao.status.value,
                prioridade=manifestacao.prioridade.value,
                assunto=manifestacao.assunto,
                descricao=manifestacao.descricao,
                cidadao_nome=manifestacao.cidadao.nome if manifestacao.cidadao else None,
                cidadao_cpf=manifestacao.cidadao.cpf if manifestacao.cidadao else None,
                cidadao_email=manifestacao.cidadao.email if manifestacao.cidadao else None,
                cidadao_telefone=manifestacao.cidadao.telefone if manifestacao.cidadao else None,
                cidadao_endereco=manifestacao.cidadao.endereco if manifestacao.cidadao else None,
                cidadao_anonimo=manifestacao.cidadao.anonimo if manifestacao.cidadao else False,
                canal=manifestacao.canal.value,
                orgao_destino=manifestacao.orgao_destino,
                setor_responsavel=manifestacao.setor_responsavel,
                prazo_data_limite=manifestacao.prazo.data_limite if manifestacao.prazo else None,
                prazo_dias_uteis=manifestacao.prazo.dias_uteis if manifestacao.prazo else None,
                prazo_prorrogado=manifestacao.prazo.prorrogado if manifestacao.prazo else False,
                prazo_data_prorrogacao=manifestacao.prazo.data_prorrogacao
                if manifestacao.prazo
                else None,
                prazo_justificativa_prorrogacao=manifestacao.prazo.justificativa_prorrogacao
                if manifestacao.prazo
                else "",
                resposta=manifestacao.resposta,
                forma_resposta=manifestacao.forma_resposta.value
                if manifestacao.forma_resposta
                else None,
                data_resposta=manifestacao.data_resposta,
                respondido_por=manifestacao.respondido_por,
                avaliacao_cidadao=manifestacao.avaliacao_cidadao,
                comentario_avaliacao=manifestacao.comentario_avaliacao,
                created_at=manifestacao.created_at,
                updated_at=manifestacao.updated_at,
                created_by=manifestacao.created_by,
                updated_by=manifestacao.updated_by,
                is_deleted=manifestacao.is_deleted,
            )
            self._session.add(model)
            self._session.flush()

            # Salvar anexos
            for anexo in manifestacao.anexos:
                self._anexo_repo.save(anexo, UUID(manifestacao.id))

            # Registrar tramitação inicial
            self._tramitacao_repo.save(
                UUID(manifestacao.id),
                None,
                manifestacao.status,
                "Registro inicial",
                manifestacao.created_by,
            )
        else:
            model = self._session.get(ManifestacaoModel, UUID(manifestacao.id))
            if not model:
                raise ManifestacaoNaoEncontradaError(
                    f"Manifestação {manifestacao.id} não encontrada"
                )

            status_anterior = StatusManifestacao(model.status)

            model.protocolo = (
                manifestacao.protocolo.codigo if manifestacao.protocolo else model.protocolo
            )
            model.tipo = manifestacao.tipo.value
            model.status = manifestacao.status.value
            model.prioridade = manifestacao.prioridade.value
            model.assunto = manifestacao.assunto
            model.descricao = manifestacao.descricao
            if manifestacao.cidadao:
                model.cidadao_nome = manifestacao.cidadao.nome
                model.cidadao_cpf = manifestacao.cidadao.cpf
                model.cidadao_email = manifestacao.cidadao.email
                model.cidadao_telefone = manifestacao.cidadao.telefone
                model.cidadao_endereco = manifestacao.cidadao.endereco
                model.cidadao_anonimo = manifestacao.cidadao.anonimo
            model.canal = manifestacao.canal.value
            model.orgao_destino = manifestacao.orgao_destino
            model.setor_responsavel = manifestacao.setor_responsavel
            if manifestacao.prazo:
                model.prazo_data_limite = manifestacao.prazo.data_limite
                model.prazo_dias_uteis = manifestacao.prazo.dias_uteis
                model.prazo_prorrogado = manifestacao.prazo.prorrogado
                model.prazo_data_prorrogacao = manifestacao.prazo.data_prorrogacao
                model.prazo_justificativa_prorrogacao = manifestacao.prazo.justificativa_prorrogacao
            model.resposta = manifestacao.resposta
            model.forma_resposta = (
                manifestacao.forma_resposta.value if manifestacao.forma_resposta else None
            )
            model.data_resposta = manifestacao.data_resposta
            model.respondido_por = manifestacao.respondido_por
            model.avaliacao_cidadao = manifestacao.avaliacao_cidadao
            model.comentario_avaliacao = manifestacao.comentario_avaliacao
            model.updated_at = manifestacao.updated_at
            model.updated_by = manifestacao.updated_by
            model.is_deleted = manifestacao.is_deleted

            # Registrar tramitação se status mudou
            if status_anterior != manifestacao.status:
                self._tramitacao_repo.save(
                    UUID(manifestacao.id),
                    status_anterior,
                    manifestacao.status,
                    "Alteração de status",
                    manifestacao.updated_by or "",
                )

        self._session.flush()
        return manifestacao

    def get_by_id(self, manifestacao_id: str) -> Manifestacao | None:
        pk = _como_uuid(manifestacao_id)
        if pk is None:
            return None
        model = self._session.get(ManifestacaoModel, pk)
        if not model or model.is_deleted:
            return None
        # Filtrar apenas manifestações genéricas (não denúncias nem LAI)
        if model.tipo in ("denuncia", "pedido_acesso_informacao"):
            return None
        return self._to_entity(model)

    def get_by_protocolo(self, protocolo: str) -> Manifestacao | None:
        model = (
            self._session.query(ManifestacaoModel)
            .filter(
                ManifestacaoModel.protocolo == protocolo, ManifestacaoModel.is_deleted.is_(False)
            )
            .first()
        )
        if not model or model.tipo in ("denuncia", "pedido_acesso_informacao"):
            return None
        return self._to_entity(model)

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[Manifestacao]:
        query = self._session.query(ManifestacaoModel).filter(
            ManifestacaoModel.is_deleted.is_(False),
            ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
        )

        if filtros:
            if "status" in filtros:
                query = query.filter(ManifestacaoModel.status == filtros["status"])
            if "tipo" in filtros:
                query = query.filter(ManifestacaoModel.tipo == filtros["tipo"])
            if "orgao_destino" in filtros:
                query = query.filter(
                    ManifestacaoModel.orgao_destino.ilike(f"%{filtros['orgao_destino']}%")
                )
            if "cidadao_nome" in filtros:
                query = query.filter(
                    ManifestacaoModel.cidadao_nome.ilike(f"%{filtros['cidadao_nome']}%")
                )
            if "data_inicio" in filtros:
                query = query.filter(ManifestacaoModel.created_at >= filtros["data_inicio"])
            if "data_fim" in filtros:
                query = query.filter(ManifestacaoModel.created_at <= filtros["data_fim"])

        query = query.order_by(ManifestacaoModel.created_at.desc())
        offset = (page - 1) * page_size
        models = query.offset(offset).limit(page_size).all()
        return [self._to_entity(m) for m in models]

    def count_all(self, filtros: dict | None = None) -> int:
        query = self._session.query(func.count(ManifestacaoModel.id)).filter(
            ManifestacaoModel.is_deleted.is_(False),
            ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
        )
        if filtros:
            if "status" in filtros:
                query = query.filter(ManifestacaoModel.status == filtros["status"])
            if "tipo" in filtros:
                query = query.filter(ManifestacaoModel.tipo == filtros["tipo"])
        return query.scalar() or 0

    def contar_por_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(ManifestacaoModel.id))
            .filter(
                ManifestacaoModel.is_deleted.is_(False),
                ManifestacaoModel.ano_protocolo == ano,
                ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
            )
            .scalar()
            or 0
        )

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        return (
            self._session.query(func.count(ManifestacaoModel.id))
            .filter(
                ManifestacaoModel.is_deleted.is_(False),
                ManifestacaoModel.status == status.value,
                ManifestacaoModel.ano_protocolo == ano,
                ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
            )
            .scalar()
            or 0
        )

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(ManifestacaoModel.id))
            .filter(
                ManifestacaoModel.is_deleted.is_(False),
                ManifestacaoModel.prazo_data_limite < date.today(),
                ManifestacaoModel.ano_protocolo == ano,
                ~ManifestacaoModel.status.in_(
                    ["respondida", "concluida", "arquivada", "cancelada"]
                ),
                ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
            )
            .scalar()
            or 0
        )

    def estatisticas_por_tipo(self, ano: int) -> dict:
        resultados = (
            self._session.query(ManifestacaoModel.tipo, func.count(ManifestacaoModel.id))
            .filter(
                ManifestacaoModel.is_deleted.is_(False),
                ManifestacaoModel.ano_protocolo == ano,
                ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
            )
            .group_by(ManifestacaoModel.tipo)
            .all()
        )
        return dict(resultados)

    def buscar_vencendo_prazo(self, dias: int) -> list[Manifestacao]:
        from datetime import timedelta

        data_limite = date.today() + timedelta(days=dias)
        models = (
            self._session.query(ManifestacaoModel)
            .filter(
                ManifestacaoModel.is_deleted.is_(False),
                ManifestacaoModel.prazo_data_limite <= data_limite,
                ManifestacaoModel.prazo_data_limite >= date.today(),
                ~ManifestacaoModel.status.in_(
                    ["respondida", "concluida", "arquivada", "cancelada"]
                ),
                ~ManifestacaoModel.tipo.in_(["denuncia", "pedido_acesso_informacao"]),
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: ManifestacaoModel) -> Manifestacao:
        cidadao = None
        if model.cidadao_nome or model.cidadao_cpf or model.cidadao_email:
            cidadao = DadosCidadao(
                nome=model.cidadao_nome or "",
                cpf=model.cidadao_cpf,
                email=model.cidadao_email,
                telefone=model.cidadao_telefone,
                endereco=model.cidadao_endereco,
                anonimo=model.cidadao_anonimo,
            )

        prazo = None
        if model.prazo_data_limite:
            prazo = PrazoResposta(
                data_limite=model.prazo_data_limite,
                dias_uteis=model.prazo_dias_uteis or 0,
                prorrogado=model.prazo_prorrogado,
                data_prorrogacao=model.prazo_data_prorrogacao,
                justificativa_prorrogacao=model.prazo_justificativa_prorrogacao or "",
            )

        anexos = self._anexo_repo.list_by_manifestacao(model.id)

        return Manifestacao(
            id=str(model.id),
            protocolo=Protocolo(numero=f"{model.numero_protocolo:06d}", ano=model.ano_protocolo)
            if model.protocolo
            else None,
            tipo=TipoManifestacao(model.tipo),
            status=StatusManifestacao(model.status),
            prioridade=Prioridade(model.prioridade),
            assunto=model.assunto,
            descricao=model.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(model.canal),
            orgao_destino=model.orgao_destino,
            setor_responsavel=model.setor_responsavel or "",
            prazo=prazo,
            anexos=anexos,
            resposta=model.resposta or "",
            forma_resposta=FormaResposta(model.forma_resposta) if model.forma_resposta else None,
            data_resposta=model.data_resposta,
            respondido_por=model.respondido_por or "",
            avaliacao_cidadao=model.avaliacao_cidadao,
            comentario_avaliacao=model.comentario_avaliacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=model.is_deleted,
        )


class SQLAlchemyDenunciaRepository(RepositorioDenuncia):
    """Repositório de denúncias."""

    def __init__(
        self,
        session: Session,
        anexo_repo: SQLAlchemyAnexoRepository,
        tramitacao_repo: SQLAlchemyTramitacaoRepository,
    ) -> None:
        self._session = session
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo

    def save(self, denuncia: Denuncia) -> Denuncia:
        is_new = denuncia.id is None or self._session.get(DenunciaModel, UUID(denuncia.id)) is None

        if is_new:
            model = DenunciaModel(
                id=UUID(denuncia.id),
                protocolo=denuncia.protocolo.codigo if denuncia.protocolo else "",
                ano_protocolo=denuncia.protocolo.ano if denuncia.protocolo else 0,
                numero_protocolo=int(denuncia.protocolo.numero) if denuncia.protocolo else 0,
                tipo=TipoManifestacao.DENUNCIA.value,
                status=denuncia.status.value,
                prioridade=denuncia.prioridade.value,
                assunto=denuncia.assunto,
                descricao=denuncia.descricao,
                cidadao_nome=denuncia.cidadao.nome if denuncia.cidadao else None,
                cidadao_cpf=denuncia.cidadao.cpf if denuncia.cidadao else None,
                cidadao_email=denuncia.cidadao.email if denuncia.cidadao else None,
                cidadao_telefone=denuncia.cidadao.telefone if denuncia.cidadao else None,
                cidadao_endereco=denuncia.cidadao.endereco if denuncia.cidadao else None,
                cidadao_anonimo=denuncia.cidadao.anonimo if denuncia.cidadao else True,
                canal=denuncia.canal.value,
                orgao_destino=denuncia.orgao_destino,
                setor_responsavel=denuncia.setor_responsavel,
                prazo_data_limite=denuncia.prazo.data_limite if denuncia.prazo else None,
                prazo_dias_uteis=denuncia.prazo.dias_uteis if denuncia.prazo else None,
                prazo_prorrogado=denuncia.prazo.prorrogado if denuncia.prazo else False,
                prazo_data_prorrogacao=denuncia.prazo.data_prorrogacao if denuncia.prazo else None,
                prazo_justificativa_prorrogacao=denuncia.prazo.justificativa_prorrogacao
                if denuncia.prazo
                else "",
                resposta=denuncia.resposta,
                forma_resposta=denuncia.forma_resposta.value if denuncia.forma_resposta else None,
                data_resposta=denuncia.data_resposta,
                respondido_por=denuncia.respondido_por,
                tipo_denuncia=denuncia.tipo_denuncia.value,
                envolve_servidor_publico=denuncia.envolve_servidor_publico,
                servidor_envolvido=denuncia.servidor_envolvido or "",
                valor_envolvido=denuncia.valor_envolvido,
                local_fato=denuncia.local_fato,
                data_fato=denuncia.data_fato,
                sigilo_denunciante=denuncia.sigilo_denunciante,
                encaminhada_mp=denuncia.encaminhada_mp,
                encaminhada_pf=denuncia.encaminhada_pf,
                encaminhada_tce=denuncia.encaminhada_tce,
                numero_inquerito=denuncia.numero_inquerito or "",
                resultado_investigacao=denuncia.resultado_investigacao or "",
                created_at=denuncia.created_at,
                updated_at=denuncia.updated_at,
                created_by=denuncia.created_by,
                updated_by=denuncia.updated_by,
                is_deleted=denuncia.is_deleted,
            )
            self._session.add(model)
            self._session.flush()

            for anexo in denuncia.anexos:
                self._anexo_repo.save(anexo, UUID(denuncia.id))

            self._tramitacao_repo.save(
                UUID(denuncia.id), None, denuncia.status, "Registro inicial", denuncia.created_by
            )
        else:
            model = self._session.get(DenunciaModel, UUID(denuncia.id))
            if not model:
                raise DenunciaNaoEncontradaError(f"Denúncia {denuncia.id} não encontrada")

            status_anterior = StatusManifestacao(model.status)

            model.protocolo = denuncia.protocolo.codigo if denuncia.protocolo else model.protocolo
            model.status = denuncia.status.value
            model.prioridade = denuncia.prioridade.value
            model.assunto = denuncia.assunto
            model.descricao = denuncia.descricao
            if denuncia.cidadao:
                model.cidadao_nome = denuncia.cidadao.nome
                model.cidadao_cpf = denuncia.cidadao.cpf
                model.cidadao_email = denuncia.cidadao.email
                model.cidadao_telefone = denuncia.cidadao.telefone
                model.cidadao_endereco = denuncia.cidadao.endereco
                model.cidadao_anonimo = denuncia.cidadao.anonimo
            model.canal = denuncia.canal.value
            model.orgao_destino = denuncia.orgao_destino
            model.setor_responsavel = denuncia.setor_responsavel
            if denuncia.prazo:
                model.prazo_data_limite = denuncia.prazo.data_limite
                model.prazo_dias_uteis = denuncia.prazo.dias_uteis
                model.prazo_prorrogado = denuncia.prazo.prorrogado
                model.prazo_data_prorrogacao = denuncia.prazo.data_prorrogacao
                model.prazo_justificativa_prorrogacao = denuncia.prazo.justificativa_prorrogacao
            model.resposta = denuncia.resposta
            model.forma_resposta = (
                denuncia.forma_resposta.value if denuncia.forma_resposta else None
            )
            model.data_resposta = denuncia.data_resposta
            model.respondido_por = denuncia.respondido_por
            model.tipo_denuncia = denuncia.tipo_denuncia.value
            model.envolve_servidor_publico = denuncia.envolve_servidor_publico
            model.servidor_envolvido = denuncia.servidor_envolvido or ""
            model.valor_envolvido = denuncia.valor_envolvido
            model.local_fato = denuncia.local_fato
            model.data_fato = denuncia.data_fato
            model.sigilo_denunciante = denuncia.sigilo_denunciante
            model.encaminhada_mp = denuncia.encaminhada_mp
            model.encaminhada_pf = denuncia.encaminhada_pf
            model.encaminhada_tce = denuncia.encaminhada_tce
            model.numero_inquerito = denuncia.numero_inquerito or ""
            model.resultado_investigacao = denuncia.resultado_investigacao or ""
            model.updated_at = denuncia.updated_at
            model.updated_by = denuncia.updated_by
            model.is_deleted = denuncia.is_deleted

            if status_anterior != denuncia.status:
                self._tramitacao_repo.save(
                    UUID(denuncia.id),
                    status_anterior,
                    denuncia.status,
                    "Alteração de status",
                    denuncia.updated_by or "",
                )

        self._session.flush()
        return denuncia

    def get_by_id(self, denuncia_id: str) -> Denuncia | None:
        pk = _como_uuid(denuncia_id)
        if pk is None:
            return None
        model = self._session.get(DenunciaModel, pk)
        if not model or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_protocolo(self, protocolo: str) -> Denuncia | None:
        model = (
            self._session.query(DenunciaModel)
            .filter(DenunciaModel.protocolo == protocolo, DenunciaModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[Denuncia]:
        query = self._session.query(DenunciaModel).filter(DenunciaModel.is_deleted.is_(False))

        if filtros:
            if "status" in filtros:
                query = query.filter(DenunciaModel.status == filtros["status"])
            if "tipo_denuncia" in filtros:
                query = query.filter(DenunciaModel.tipo_denuncia == filtros["tipo_denuncia"])
            if "orgao_destino" in filtros:
                query = query.filter(
                    DenunciaModel.orgao_destino.ilike(f"%{filtros['orgao_destino']}%")
                )
            if "anonima" in filtros:
                query = query.filter(DenunciaModel.cidadao_anonimo == filtros["anonima"])
            if "data_inicio" in filtros:
                query = query.filter(DenunciaModel.created_at >= filtros["data_inicio"])
            if "data_fim" in filtros:
                query = query.filter(DenunciaModel.created_at <= filtros["data_fim"])

        query = query.order_by(DenunciaModel.created_at.desc())
        offset = (page - 1) * page_size
        models = query.offset(offset).limit(page_size).all()
        return [self._to_entity(m) for m in models]

    def count_all(self, filtros: dict | None = None) -> int:
        query = self._session.query(func.count(DenunciaModel.id)).filter(
            DenunciaModel.is_deleted.is_(False)
        )
        if filtros and "status" in filtros:
            query = query.filter(DenunciaModel.status == filtros["status"])
        return query.scalar() or 0

    def contar_por_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(DenunciaModel.id))
            .filter(DenunciaModel.is_deleted.is_(False), DenunciaModel.ano_protocolo == ano)
            .scalar()
            or 0
        )

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        return (
            self._session.query(func.count(DenunciaModel.id))
            .filter(
                DenunciaModel.is_deleted.is_(False),
                DenunciaModel.status == status.value,
                DenunciaModel.ano_protocolo == ano,
            )
            .scalar()
            or 0
        )

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(DenunciaModel.id))
            .filter(
                DenunciaModel.is_deleted.is_(False),
                DenunciaModel.prazo_data_limite < date.today(),
                DenunciaModel.ano_protocolo == ano,
                ~DenunciaModel.status.in_(["respondida", "concluida", "arquivada", "cancelada"]),
            )
            .scalar()
            or 0
        )

    def estatisticas_por_tipo(self, ano: int) -> dict:
        resultados = (
            self._session.query(DenunciaModel.tipo_denuncia, func.count(DenunciaModel.id))
            .filter(DenunciaModel.is_deleted.is_(False), DenunciaModel.ano_protocolo == ano)
            .group_by(DenunciaModel.tipo_denuncia)
            .all()
        )
        return dict(resultados)

    def buscar_vencendo_prazo(self, dias: int) -> list[Denuncia]:
        from datetime import timedelta

        data_limite = date.today() + timedelta(days=dias)
        models = (
            self._session.query(DenunciaModel)
            .filter(
                DenunciaModel.is_deleted.is_(False),
                DenunciaModel.prazo_data_limite <= data_limite,
                DenunciaModel.prazo_data_limite >= date.today(),
                ~DenunciaModel.status.in_(["respondida", "concluida", "arquivada", "cancelada"]),
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: DenunciaModel) -> Denuncia:
        cidadao = None
        if model.cidadao_nome or model.cidadao_cpf or model.cidadao_email:
            cidadao = DadosCidadao(
                nome=model.cidadao_nome or "",
                cpf=model.cidadao_cpf,
                email=model.cidadao_email,
                telefone=model.cidadao_telefone,
                endereco=model.cidadao_endereco,
                anonimo=model.cidadao_anonimo,
            )

        prazo = None
        if model.prazo_data_limite:
            prazo = PrazoResposta(
                data_limite=model.prazo_data_limite,
                dias_uteis=model.prazo_dias_uteis or 0,
                prorrogado=model.prazo_prorrogado,
                data_prorrogacao=model.prazo_data_prorrogacao,
                justificativa_prorrogacao=model.prazo_justificativa_prorrogacao or "",
            )

        anexos = self._anexo_repo.list_by_manifestacao(model.id)

        return Denuncia(
            id=str(model.id),
            protocolo=Protocolo(numero=f"{model.numero_protocolo:06d}", ano=model.ano_protocolo)
            if model.protocolo
            else None,
            tipo=TipoManifestacao.DENUNCIA,
            status=StatusManifestacao(model.status),
            prioridade=Prioridade(model.prioridade),
            assunto=model.assunto,
            descricao=model.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(model.canal),
            orgao_destino=model.orgao_destino,
            setor_responsavel=model.setor_responsavel or "",
            prazo=prazo,
            anexos=anexos,
            resposta=model.resposta or "",
            forma_resposta=FormaResposta(model.forma_resposta) if model.forma_resposta else None,
            data_resposta=model.data_resposta,
            respondido_por=model.respondido_por or "",
            tipo_denuncia=TipoDenuncia(model.tipo_denuncia),
            envolve_servidor_publico=model.envolve_servidor_publico,
            servidor_envolvido=model.servidor_envolvido or "",
            valor_envolvido=model.valor_envolvido,
            local_fato=model.local_fato,
            data_fato=model.data_fato,
            sigilo_denunciante=model.sigilo_denunciante,
            encaminhada_mp=model.encaminhada_mp,
            encaminhada_pf=model.encaminhada_pf,
            encaminhada_tce=model.encaminhada_tce,
            numero_inquerito=model.numero_inquerito or "",
            resultado_investigacao=model.resultado_investigacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=model.is_deleted,
        )


class SQLAlchemyPedidoLaiRepository(RepositorioPedidoLai):
    """Repositório de pedidos LAI."""

    def __init__(
        self,
        session: Session,
        anexo_repo: SQLAlchemyAnexoRepository,
        tramitacao_repo: SQLAlchemyTramitacaoRepository,
    ) -> None:
        self._session = session
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo

    def _protocolo_do_pedido(self, pedido: PedidoLai) -> tuple[str, int, int]:
        """Resolve (protocolo, ano, número) a persistir para um pedido LAI.

        Pedido normal usa o próprio protocolo. Recurso deriva o código do
        pedido original com o sufixo ``-R``, preservando a unicidade da coluna
        `protocolo` sem inventar uma numeração FalaBR para o recurso.
        """
        if pedido.protocolo:
            return (
                pedido.protocolo.codigo,
                pedido.protocolo.ano,
                int(pedido.protocolo.numero),
            )
        if pedido.is_recurso and pedido.pedido_original_id:
            original = self._session.get(PedidoLaiModel, _como_uuid(pedido.pedido_original_id))
            if original:
                return (
                    f"{original.protocolo}-R",
                    original.ano_protocolo,
                    original.numero_protocolo,
                )
        # Fallback defensivo: sem protocolo nem original, usa o id do próprio
        # registro, que é único por natureza.
        return (f"sem-protocolo-{pedido.id}", 0, 0)

    def save(self, pedido: PedidoLai) -> PedidoLai:
        is_new = pedido.id is None or self._session.get(PedidoLaiModel, UUID(pedido.id)) is None

        if is_new:
            # Um recurso não recebe numeração própria do FalaBR: o protocolo
            # identifica o pedido original. Como `protocolo` é NOT NULL e
            # único, deriva-se o código do pedido original com o sufixo "-R".
            # Sem isso, todo recurso gravaria "" e o segundo interposto
            # violaria a constraint `manifestacoes_protocolo_key`.
            protocolo_texto, ano_protocolo, numero_protocolo = self._protocolo_do_pedido(pedido)
            model = PedidoLaiModel(
                id=UUID(pedido.id),
                protocolo=protocolo_texto,
                ano_protocolo=ano_protocolo,
                numero_protocolo=numero_protocolo,
                tipo=TipoManifestacao.PEDIDO_ACESSO_INFORMACAO.value,
                status=pedido.status.value,
                prioridade=pedido.prioridade.value,
                assunto=pedido.assunto,
                descricao=pedido.descricao,
                cidadao_nome=pedido.cidadao.nome if pedido.cidadao else None,
                cidadao_cpf=pedido.cidadao.cpf if pedido.cidadao else None,
                cidadao_email=pedido.cidadao.email if pedido.cidadao else None,
                cidadao_telefone=pedido.cidadao.telefone if pedido.cidadao else None,
                cidadao_endereco=pedido.cidadao.endereco if pedido.cidadao else None,
                cidadao_anonimo=pedido.cidadao.anonimo if pedido.cidadao else False,
                canal=pedido.canal.value,
                orgao_destino=pedido.orgao_destino,
                setor_responsavel=pedido.setor_responsavel,
                prazo_data_limite=pedido.prazo.data_limite if pedido.prazo else None,
                prazo_dias_uteis=pedido.prazo.dias_uteis if pedido.prazo else None,
                prazo_prorrogado=pedido.prazo.prorrogado if pedido.prazo else False,
                prazo_data_prorrogacao=pedido.prazo.data_prorrogacao if pedido.prazo else None,
                prazo_justificativa_prorrogacao=pedido.prazo.justificativa_prorrogacao
                if pedido.prazo
                else "",
                resposta=pedido.resposta,
                forma_resposta=pedido.forma_resposta.value if pedido.forma_resposta else None,
                data_resposta=pedido.data_resposta,
                respondido_por=pedido.respondido_por,
                informacao_solicitada=pedido.informacao_solicitada,
                fundamentacao=pedido.fundamentacao,
                nivel_sigilo=pedido.nivel_sigilo.value,
                fundamentacao_sigilo=pedido.fundamentacao_sigilo or "",
                dados_pessoais_terceiros=pedido.dados_pessoais_terceiros,
                formato_resposta=pedido.formato_resposta,
                is_recurso=pedido.is_recurso,
                pedido_original_id=UUID(pedido.pedido_original_id)
                if pedido.pedido_original_id
                else None,
                decisao_recurso=pedido.decisao_recurso or "",
                data_decisao_recurso=pedido.data_decisao_recurso,
                created_at=pedido.created_at,
                updated_at=pedido.updated_at,
                created_by=pedido.created_by,
                updated_by=pedido.updated_by,
                is_deleted=pedido.is_deleted,
            )
            self._session.add(model)
            self._session.flush()

            for anexo in pedido.anexos:
                self._anexo_repo.save(anexo, UUID(pedido.id))

            self._tramitacao_repo.save(
                UUID(pedido.id), None, pedido.status, "Registro inicial", pedido.created_by
            )
        else:
            model = self._session.get(PedidoLaiModel, UUID(pedido.id))
            if not model:
                raise PedidoLaiNaoEncontradoError(f"Pedido LAI {pedido.id} não encontrado")

            status_anterior = StatusManifestacao(model.status)

            # O protocolo é imutável após a emissão (RN-OUV-001) e não é
            # reatribuído aqui. Para um recurso lido do banco, `_to_entity`
            # reconstrói o protocolo a partir de ano/numero — que no recurso
            # espelham o pedido original — e reescrever isso apagaria o
            # sufixo "-R", colidindo com o registro original na constraint
            # única.
            model.status = pedido.status.value
            model.prioridade = pedido.prioridade.value
            model.assunto = pedido.assunto
            model.descricao = pedido.descricao
            if pedido.cidadao:
                model.cidadao_nome = pedido.cidadao.nome
                model.cidadao_cpf = pedido.cidadao.cpf
                model.cidadao_email = pedido.cidadao.email
                model.cidadao_telefone = pedido.cidadao.telefone
                model.cidadao_endereco = pedido.cidadao.endereco
                model.cidadao_anonimo = pedido.cidadao.anonimo
            model.canal = pedido.canal.value
            model.orgao_destino = pedido.orgao_destino
            model.setor_responsavel = pedido.setor_responsavel
            if pedido.prazo:
                model.prazo_data_limite = pedido.prazo.data_limite
                model.prazo_dias_uteis = pedido.prazo.dias_uteis
                model.prazo_prorrogado = pedido.prazo.prorrogado
                model.prazo_data_prorrogacao = pedido.prazo.data_prorrogacao
                model.prazo_justificativa_prorrogacao = pedido.prazo.justificativa_prorrogacao
            model.resposta = pedido.resposta
            model.forma_resposta = pedido.forma_resposta.value if pedido.forma_resposta else None
            model.data_resposta = pedido.data_resposta
            model.respondido_por = pedido.respondido_por
            model.informacao_solicitada = pedido.informacao_solicitada
            model.fundamentacao = pedido.fundamentacao
            model.nivel_sigilo = pedido.nivel_sigilo.value
            model.fundamentacao_sigilo = pedido.fundamentacao_sigilo or ""
            model.dados_pessoais_terceiros = pedido.dados_pessoais_terceiros
            model.formato_resposta = pedido.formato_resposta
            model.is_recurso = pedido.is_recurso
            model.pedido_original_id = (
                UUID(pedido.pedido_original_id) if pedido.pedido_original_id else None
            )
            model.decisao_recurso = pedido.decisao_recurso or ""
            model.data_decisao_recurso = pedido.data_decisao_recurso
            model.updated_at = pedido.updated_at
            model.updated_by = pedido.updated_by
            model.is_deleted = pedido.is_deleted

            if status_anterior != pedido.status:
                self._tramitacao_repo.save(
                    UUID(pedido.id),
                    status_anterior,
                    pedido.status,
                    "Alteração de status",
                    pedido.updated_by or "",
                )

        self._session.flush()
        return pedido

    def get_by_id(self, pedido_id: str) -> PedidoLai | None:
        pk = _como_uuid(pedido_id)
        if pk is None:
            return None
        model = self._session.get(PedidoLaiModel, pk)
        if not model or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_protocolo(self, protocolo: str) -> PedidoLai | None:
        model = (
            self._session.query(PedidoLaiModel)
            .filter(PedidoLaiModel.protocolo == protocolo, PedidoLaiModel.is_deleted.is_(False))
            .first()
        )
        return self._to_entity(model) if model else None

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[PedidoLai]:
        query = self._session.query(PedidoLaiModel).filter(PedidoLaiModel.is_deleted.is_(False))

        if filtros:
            if "status" in filtros:
                query = query.filter(PedidoLaiModel.status == filtros["status"])
            if "nivel_sigilo" in filtros:
                query = query.filter(PedidoLaiModel.nivel_sigilo == filtros["nivel_sigilo"])
            if "is_recurso" in filtros:
                query = query.filter(PedidoLaiModel.is_recurso == filtros["is_recurso"])
            if "data_inicio" in filtros:
                query = query.filter(PedidoLaiModel.created_at >= filtros["data_inicio"])
            if "data_fim" in filtros:
                query = query.filter(PedidoLaiModel.created_at <= filtros["data_fim"])

        query = query.order_by(PedidoLaiModel.created_at.desc())
        offset = (page - 1) * page_size
        models = query.offset(offset).limit(page_size).all()
        return [self._to_entity(m) for m in models]

    def count_all(self, filtros: dict | None = None) -> int:
        query = self._session.query(func.count(PedidoLaiModel.id)).filter(
            PedidoLaiModel.is_deleted.is_(False)
        )
        if filtros and "status" in filtros:
            query = query.filter(PedidoLaiModel.status == filtros["status"])
        return query.scalar() or 0

    def contar_por_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(PedidoLaiModel.id))
            .filter(PedidoLaiModel.is_deleted.is_(False), PedidoLaiModel.ano_protocolo == ano)
            .scalar()
            or 0
        )

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        return (
            self._session.query(func.count(PedidoLaiModel.id))
            .filter(
                PedidoLaiModel.is_deleted.is_(False),
                PedidoLaiModel.status == status.value,
                PedidoLaiModel.ano_protocolo == ano,
            )
            .scalar()
            or 0
        )

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        return (
            self._session.query(func.count(PedidoLaiModel.id))
            .filter(
                PedidoLaiModel.is_deleted.is_(False),
                PedidoLaiModel.prazo_data_limite < date.today(),
                PedidoLaiModel.ano_protocolo == ano,
                ~PedidoLaiModel.status.in_(["respondida", "concluida", "arquivada", "cancelada"]),
            )
            .scalar()
            or 0
        )

    def estatisticas_por_tipo(self, ano: int) -> dict:
        resultados = (
            self._session.query(PedidoLaiModel.nivel_sigilo, func.count(PedidoLaiModel.id))
            .filter(PedidoLaiModel.is_deleted.is_(False), PedidoLaiModel.ano_protocolo == ano)
            .group_by(PedidoLaiModel.nivel_sigilo)
            .all()
        )
        return {f"nivel_{nivel}": count for nivel, count in resultados}

    def buscar_vencendo_prazo(self, dias: int) -> list[PedidoLai]:
        from datetime import timedelta

        data_limite = date.today() + timedelta(days=dias)
        models = (
            self._session.query(PedidoLaiModel)
            .filter(
                PedidoLaiModel.is_deleted.is_(False),
                PedidoLaiModel.prazo_data_limite <= data_limite,
                PedidoLaiModel.prazo_data_limite >= date.today(),
                ~PedidoLaiModel.status.in_(["respondida", "concluida", "arquivada", "cancelada"]),
            )
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: PedidoLaiModel) -> PedidoLai:
        cidadao = None
        if model.cidadao_nome or model.cidadao_cpf or model.cidadao_email:
            cidadao = DadosCidadao(
                nome=model.cidadao_nome or "",
                cpf=model.cidadao_cpf,
                email=model.cidadao_email,
                telefone=model.cidadao_telefone,
                endereco=model.cidadao_endereco,
                anonimo=model.cidadao_anonimo,
            )

        prazo = None
        if model.prazo_data_limite:
            prazo = PrazoResposta(
                data_limite=model.prazo_data_limite,
                dias_uteis=model.prazo_dias_uteis or 0,
                prorrogado=model.prazo_prorrogado,
                data_prorrogacao=model.prazo_data_prorrogacao,
                justificativa_prorrogacao=model.prazo_justificativa_prorrogacao or "",
            )

        anexos = self._anexo_repo.list_by_manifestacao(model.id)

        return PedidoLai(
            id=str(model.id),
            protocolo=Protocolo(numero=f"{model.numero_protocolo:06d}", ano=model.ano_protocolo)
            if model.protocolo
            else None,
            tipo=TipoManifestacao.PEDIDO_ACESSO_INFORMACAO,
            status=StatusManifestacao(model.status),
            prioridade=Prioridade(model.prioridade),
            assunto=model.assunto,
            descricao=model.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(model.canal),
            orgao_destino=model.orgao_destino,
            setor_responsavel=model.setor_responsavel or "",
            prazo=prazo,
            anexos=anexos,
            resposta=model.resposta or "",
            forma_resposta=FormaResposta(model.forma_resposta) if model.forma_resposta else None,
            data_resposta=model.data_resposta,
            respondido_por=model.respondido_por or "",
            informacao_solicitada=model.informacao_solicitada,
            fundamentacao=model.fundamentacao,
            nivel_sigilo=NivelSigilo(model.nivel_sigilo),
            fundamentacao_sigilo=model.fundamentacao_sigilo or "",
            dados_pessoais_terceiros=model.dados_pessoais_terceiros,
            formato_resposta=model.formato_resposta,
            is_recurso=model.is_recurso,
            pedido_original_id=str(model.pedido_original_id) if model.pedido_original_id else None,
            decisao_recurso=model.decisao_recurso or "",
            data_decisao_recurso=model.data_decisao_recurso,
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            updated_by=model.updated_by or "",
            is_deleted=model.is_deleted,
        )


__all__ = [
    "SQLAlchemyProtocoloRepository",
    "SQLAlchemyAnexoRepository",
    "SQLAlchemyTramitacaoRepository",
    "SQLAlchemyManifestacaoRepository",
    "SQLAlchemyDenunciaRepository",
    "SQLAlchemyPedidoLaiRepository",
]
