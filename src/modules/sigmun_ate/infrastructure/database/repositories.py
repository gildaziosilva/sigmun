"""Repositórios de persistência do domínio Atendimento ao Cidadão (DOM-ATE)."""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.modules.sigmun_ate.application.interfaces import (
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
from src.modules.sigmun_ate.infrastructure.database.models import (
    AtendimentoModel,
    AvaliacaoAtendimentoModel,
    ChamadaModel,
    EncaminhamentoModel,
    FilaAtendimentoModel,
    GuicheModel,
    SenhaModel,
    ServicoAtendimentoModel,
    TriagemModel,
    UnidadeAtendimentoModel,
)


class SQLAlchemyTriagemRepository(RepositorioTriagem):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, triagem) -> None:
        model = TriagemModel(
            id=triagem.id,
            servico_id=triagem.servico_id,
            data_hora=triagem.data_hora,
            classificacao=triagem.classificacao,
            prioridade=triagem.prioridade,
            observacao=triagem.observacao,
            created_at=triagem.created_at,
            created_by=triagem.created_by,
            updated_at=triagem.updated_at,
            updated_by=triagem.updated_by,
            is_deleted=triagem.is_deleted,
        )
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(TriagemModel, id)
        if not model:
            return None
        return Triagem(
            id=model.id, servico_id=model.servico_id,
            data_hora=model.data_hora, classificacao=model.classificacao,
            prioridade=model.prioridade, observacao=model.observacao or "",
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None,
        )

    def listar_por_servico(self, servico_id: str):
        stmt = select(TriagemModel).where(
            TriagemModel.servico_id == servico_id,
            TriagemModel.deleted_at.is_(None),
        )
        models = self._session.execute(stmt).scalars().all()
        return [
            Triagem(
                id=m.id, servico_id=m.servico_id, data_hora=m.data_hora,
                classificacao=m.classificacao, prioridade=m.prioridade,
                observacao=m.observacao or "",
                created_at=m.created_at, created_by=m.created_by,
                updated_at=m.updated_at, updated_by=m.updated_by,
                is_deleted=m.deleted_at is not None,
            ) for m in models
        ]


class SQLAlchemyFilaRepository(RepositorioFila):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, fila: FilaAtendimento) -> None:
        model = FilaAtendimentoModel(
            id=fila.id, unidade_id=fila.unidade_id, servico_id=fila.servico_id,
            data=fila.data, status=fila.status,
            created_at=fila.created_at, created_by=fila.created_by,
            updated_at=fila.updated_at, updated_by=fila.updated_by,
            is_deleted=fila.is_deleted,
        )
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(FilaAtendimentoModel, id)
        if not model: return None
        return FilaAtendimento(id=model.id, unidade_id=model.unidade_id,
            servico_id=model.servico_id, data=model.data, status=model.status,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_aberta(self, unidade_id: str, servico_id: str):
        stmt = select(FilaAtendimentoModel).where(
            FilaAtendimentoModel.unidade_id == unidade_id,
            FilaAtendimentoModel.servico_id == servico_id,
            FilaAtendimentoModel.status == "aberta",
            FilaAtendimentoModel.deleted_at.is_(None),
        )
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        return FilaAtendimento(
            id=model.id, unidade_id=model.unidade_id, servico_id=model.servico_id,
            data=model.data, status=model.status,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def listar_por_unidade(self, unidade_id: str):
        stmt = select(FilaAtendimentoModel).where(
            FilaAtendimentoModel.unidade_id == unidade_id,
            FilaAtendimentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [FilaAtendimento(id=m.id, unidade_id=m.unidade_id,
            servico_id=m.servico_id, data=m.data, status=m.status,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemySenhaRepository(RepositorioSenha):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, senha) -> None:
        model = SenhaModel(
            id=senha.id, fila_id=senha.fila_id, servico_id=senha.servico_id,
            triagem_id=senha.triagem_id, numero=senha.numero,
            data_hora_emissao=senha.data_hora_emissao, prioridade=senha.prioridade,
            status=senha.status.value, created_at=senha.created_at,
            created_by=senha.created_by, updated_at=senha.updated_at,
            updated_by=senha.updated_by, is_deleted=senha.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(SenhaModel, id)
        if not model: return None
        from src.modules.sigmun_ate.domain.entities import StatusSenha
        return Senha(id=model.id, fila_id=model.fila_id, servico_id=model.servico_id,
            triagem_id=model.triagem_id, numero=model.numero,
            data_hora_emissao=model.data_hora_emissao, prioridade=model.prioridade,
            status=model.status, created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_por_numero(self, numero: str):
        stmt = select(SenhaModel).where(SenhaModel.numero == numero, SenhaModel.deleted_at.is_(None))
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        from src.modules.sigmun_ate.domain.entities import StatusSenha
        return Senha(id=model.id, fila_id=model.fila_id, servico_id=model.servico_id,
            triagem_id=model.triagem_id, numero=model.numero,
            data_hora_emissao=model.data_hora_emissao, prioridade=model.prioridade,
            status=model.status, created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def listar_por_fila(self, fila_id: str):
        stmt = select(SenhaModel).where(SenhaModel.fila_id == fila_id, SenhaModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        from src.modules.sigmun_ate.domain.entities import StatusSenha
        return [Senha(id=m.id, fila_id=m.fila_id, servico_id=m.servico_id,
            triagem_id=m.triagem_id, numero=m.numero,
            data_hora_emissao=m.data_hora_emissao, prioridade=m.prioridade,
            status=m.status, created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]

    def listar_emitidas_hoje(self, fila_id: str):
        from datetime import date
        hoje = date.today()
        stmt = select(SenhaModel).where(
            SenhaModel.fila_id == fila_id, func.date(SenhaModel.data_hora_emissao) == hoje,
            SenhaModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        from src.modules.sigmun_ate.domain.entities import StatusSenha
        return [Senha(id=m.id, fila_id=m.fila_id, servico_id=m.servico_id,
            triagem_id=m.triagem_id, numero=m.numero,
            data_hora_emissao=m.data_hora_emissao, prioridade=m.prioridade,
            status=m.status, created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyChamadaRepository:
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, chamada) -> None:
        model = ChamadaModel(
            id=chamada.id, senha_id=chamada.senha_id, guiche_id=chamada.guiche_id,
            unidade_id=chamada.unidade_id, operador=chamada.operador,
            data_hora=chamada.data_hora, ordem=chamada.ordem,
            tentativa=chamada.tentativa, resultado=chamada.resultado,
            created_at=chamada.created_at, created_by=chamada.created_by,
            updated_at=chamada.updated_at, updated_by=chamada.updated_by,
            is_deleted=chamada.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(ChamadaModel, id)
        if not model: return None
        return Chamada(id=model.id, senha_id=model.senha_id, guiche_id=model.guiche_id,
            unidade_id=model.unidade_id, operador=model.operador,
            data_hora=model.data_hora, ordem=model.ordem, tentativa=model.tentativa,
            resultado=model.resultado, created_at=model.created_at,
            created_by=model.created_by, updated_at=model.updated_at,
            updated_by=model.updated_by, is_deleted=model.deleted_at is not None)

    def buscar_por_senha(self, senha_id: str):
        stmt = select(ChamadaModel).where(ChamadaModel.senha_id == senha_id, ChamadaModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Chamada(id=m.id, senha_id=m.senha_id, guiche_id=m.guiche_id,
            unidade_id=m.unidade_id, operador=m.operador, data_hora=m.data_hora,
            ordem=m.ordem, tentativa=m.tentativa, resultado=m.resultado,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]

    def listar_por_guiche(self, guiche_id: str):
        from datetime import date
        hoje = date.today()
        stmt = select(ChamadaModel).where(ChamadaModel.guiche_id == guiche_id,
            func.date(ChamadaModel.data_hora) == hoje, ChamadaModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Chamada(id=m.id, senha_id=m.senha_id, guiche_id=m.guiche_id,
            unidade_id=m.unidade_id, operador=m.operador, data_hora=m.data_hora,
            ordem=m.ordem, tentativa=m.tentativa, resultado=m.resultado,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyAtendimentoRepository(RepositorioAtendimento):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, atendimento) -> None:
        model = AtendimentoModel(
            id=atendimento.id, chamada_id=atendimento.chamada_id,
            canal_id=atendimento.canal_id, inicio=atendimento.inicio,
            fim=atendimento.fim, status=atendimento.status.value,
            descricao=atendimento.descricao, created_at=atendimento.created_at,
            created_by=atendimento.created_by, updated_at=atendimento.updated_at,
            updated_by=atendimento.updated_by, is_deleted=atendimento.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(AtendimentoModel, id)
        if not model: return None
        from src.modules.sigmun_ate.domain.entities import StatusAtendimento
        return Atendimento(id=model.id, chamada_id=model.chamada_id,
            canal_id=model.canal_id, inicio=model.inicio, fim=model.fim,
            status=model.status, descricao=model.descricao or "",
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_por_chamada(self, chamada_id: str):
        stmt = select(AtendimentoModel).where(AtendimentoModel.chamada_id == chamada_id, AtendimentoModel.deleted_at.is_(None))
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        from src.modules.sigmun_ate.domain.entities import StatusAtendimento
        return Atendimento(id=model.id, chamada_id=model.chamada_id,
            canal_id=model.canal_id, inicio=model.inicio, fim=model.fim,
            status=model.status, descricao=model.descricao or "",
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def listar_em_andamento(self):
        stmt = select(AtendimentoModel).where(AtendimentoModel.status == "em_andamento", AtendimentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        from src.modules.sigmun_ate.domain.entities import StatusAtendimento
        return [Atendimento(id=m.id, chamada_id=m.chamada_id, canal_id=m.canal_id,
            inicio=m.inicio, fim=m.fim, status=m.status, descricao=m.descricao or "",
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyAvaliacaoRepository(RepositorioAvaliacao):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, avaliacao) -> None:
        model = AvaliacaoAtendimentoModel(
            id=avaliacao.id, atendimento_id=avaliacao.atendimento_id,
            nota=avaliacao.nota, comentario=avaliacao.comentario,
            data_hora=avaliacao.data_hora, created_at=avaliacao.created_at,
            created_by=avaliacao.created_by, updated_at=avaliacao.updated_at,
            updated_by=avaliacao.updated_by, is_deleted=avaliacao.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(AvaliacaoAtendimentoModel, id)
        if not model: return None
        return AvaliacaoAtendimento(id=model.id, atendimento_id=model.atendimento_id,
            nota=model.nota, comentario=model.comentario or "",
            data_hora=model.data_hora, created_at=model.created_at,
            created_by=model.created_by, updated_at=model.updated_at,
            updated_by=model.updated_by, is_deleted=model.deleted_at is not None)

    def buscar_por_atendimento(self, atendimento_id: str):
        stmt = select(AvaliacaoAtendimentoModel).where(
            AvaliacaoAtendimentoModel.atendimento_id == atendimento_id,
            AvaliacaoAtendimentoModel.deleted_at.is_(None))
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        return AvaliacaoAtendimento(id=model.id, atendimento_id=model.atendimento_id,
            nota=model.nota, comentario=model.comentario or "",
            data_hora=model.data_hora, created_at=model.created_at,
            created_by=model.created_by, updated_at=model.updated_at,
            updated_by=model.updated_by, is_deleted=model.deleted_at is not None)


class SQLAlchemyEncaminhamentoRepository(RepositorioEncaminhamento):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, encaminhamento) -> None:
        model = EncaminhamentoModel(
            id=encaminhamento.id, atendimento_id=encaminhamento.atendimento_id,
            data_hora=encaminhamento.data_hora, destino=encaminhamento.destino,
            motivo=encaminhamento.motivo, status=encaminhamento.status,
            created_at=encaminhamento.created_at, created_by=encaminhamento.created_by,
            updated_at=encaminhamento.updated_at, updated_by=encaminhamento.updated_by,
            is_deleted=encaminhamento.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(EncaminhamentoModel, id)
        if not model: return None
        return Encaminhamento(id=model.id, atendimento_id=model.atendimento_id,
            data_hora=model.data_hora, destino=model.destino,
            motivo=model.motivo, status=model.status,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_por_atendimento(self, atendimento_id: str):
        stmt = select(EncaminhamentoModel).where(EncaminhamentoModel.atendimento_id == atendimento_id, EncaminhamentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Encaminhamento(id=m.id, atendimento_id=m.atendimento_id,
            data_hora=m.data_hora, destino=m.destino, motivo=m.motivo,
            status=m.status, created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]

    def listar_pendentes(self):
        stmt = select(EncaminhamentoModel).where(EncaminhamentoModel.status == "pendente", EncaminhamentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Encaminhamento(id=m.id, atendimento_id=m.atendimento_id,
            data_hora=m.data_hora, destino=m.destino, motivo=m.motivo,
            status=m.status, created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyGuicheRepository:
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, guiche) -> None:
        model = GuicheModel(
            id=guiche.id, unidade_id=guiche.unidade_id, numero=guiche.numero,
            descricao=guiche.descricao, ativo=guiche.ativo,
            created_at=guiche.created_at, created_by=guiche.created_by,
            updated_at=guiche.updated_at, updated_by=guiche.updated_by,
            is_deleted=guiche.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(GuicheModel, id)
        if not model: return None
        return Guiche(id=model.id, unidade_id=model.unidade_id,
            numero=model.numero, descricao=model.descricao or "",
            ativo=model.ativo, created_at=model.created_at,
            created_by=model.created_by, updated_at=model.updated_at,
            updated_by=model.updated_by, is_deleted=model.deleted_at is not None)

    def listar_por_unidade(self, unidade_id: str):
        stmt = select(GuicheModel).where(GuicheModel.unidade_id == unidade_id, GuicheModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Guiche(id=m.id, unidade_id=m.unidade_id, numero=m.numero,
            descricao=m.descricao or "", ativo=m.ativo,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]

    def listar_ativos(self, unidade_id: str):
        stmt = select(GuicheModel).where(GuicheModel.unidade_id == unidade_id, GuicheModel.ativo == True, GuicheModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [Guiche(id=m.id, unidade_id=m.unidade_id, numero=m.numero,
            descricao=m.descricao or "", ativo=m.ativo,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyUnidadeAtendimentoRepository(RepositorioUnidadeAtendimento):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, unidade) -> None:
        model = UnidadeAtendimentoModel(
            id=unidade.id, codigo=unidade.codigo, nome=unidade.nome,
            ativo=unidade.ativo, max_rechamadas=unidade.max_rechamadas,
            created_at=unidade.created_at, created_by=unidade.created_by,
            updated_at=unidade.updated_at, updated_by=unidade.updated_by,
            is_deleted=unidade.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(UnidadeAtendimentoModel, id)
        if not model: return None
        return UnidadeAtendimento(id=model.id, codigo=model.codigo,
            nome=model.nome, ativo=model.ativo, max_rechamadas=model.max_rechamadas,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_por_codigo(self, codigo: str):
        stmt = select(UnidadeAtendimentoModel).where(UnidadeAtendimentoModel.codigo == codigo, UnidadeAtendimentoModel.deleted_at.is_(None))
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        return UnidadeAtendimento(id=model.id, codigo=model.codigo,
            nome=model.nome, ativo=model.ativo, max_rechamadas=model.max_rechamadas,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def listar_ativas(self):
        stmt = select(UnidadeAtendimentoModel).where(UnidadeAtendimentoModel.ativo == True, UnidadeAtendimentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [UnidadeAtendimento(id=m.id, codigo=m.codigo, nome=m.nome,
            ativo=m.ativo, max_rechamadas=m.max_rechamadas,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


class SQLAlchemyServicoAtendimentoRepository(RepositorioServicoAtendimento):
    def __init__(self, session: Session):
        self._session = session

    def salvar(self, servico) -> None:
        model = ServicoAtendimentoModel(
            id=servico.id, codigo=servico.codigo, nome=servico.nome,
            prioridade=servico.prioridade, ativo=servico.ativo,
            created_at=servico.created_at, created_by=servico.created_by,
            updated_at=servico.updated_at, updated_by=servico.updated_by,
            is_deleted=servico.is_deleted)
        self._session.merge(model)

    def buscar_por_id(self, id: str):
        model = self._session.get(ServicoAtendimentoModel, id)
        if not model: return None
        return ServicoAtendimento(id=model.id, codigo=model.codigo,
            nome=model.nome, prioridade=model.prioridade, ativo=model.ativo,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def buscar_por_codigo(self, codigo: str):
        stmt = select(ServicoAtendimentoModel).where(ServicoAtendimentoModel.codigo == codigo, ServicoAtendimentoModel.deleted_at.is_(None))
        model = self._session.execute(stmt).scalar_one_or_none()
        if not model: return None
        return ServicoAtendimento(id=model.id, codigo=model.codigo,
            nome=model.nome, prioridade=model.prioridade, ativo=model.ativo,
            created_at=model.created_at, created_by=model.created_by,
            updated_at=model.updated_at, updated_by=model.updated_by,
            is_deleted=model.deleted_at is not None)

    def listar_ativos(self):
        stmt = select(ServicoAtendimentoModel).where(ServicoAtendimentoModel.ativo == True, ServicoAtendimentoModel.deleted_at.is_(None))
        models = self._session.execute(stmt).scalars().all()
        return [ServicoAtendimento(id=m.id, codigo=m.codigo, nome=m.nome,
            prioridade=m.prioridade, ativo=m.ativo,
            created_at=m.created_at, created_by=m.created_by,
            updated_at=m.updated_at, updated_by=m.updated_by,
            is_deleted=m.deleted_at is not None) for m in models]


__all__ = [
    "SQLAlchemyTriagemRepository",
    "SQLAlchemyFilaRepository",
    "SQLAlchemySenhaRepository",
    "SQLAlchemyChamadaRepository",
    "SQLAlchemyAtendimentoRepository",
    "SQLAlchemyAvaliacaoRepository",
    "SQLAlchemyEncaminhamentoRepository",
    "SQLAlchemyGuicheRepository",
    "SQLAlchemyUnidadeAtendimentoRepository",
    "SQLAlchemyServicoAtendimentoRepository",
]
