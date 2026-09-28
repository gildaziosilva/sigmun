"""Repositórios SQLAlchemy do DOM-ASS."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from ...application.interfaces import (
    RepositorioAtendimento,
    RepositorioBeneficio,
    RepositorioFamilia,
    RepositorioPessoa,
    RepositorioUnidade,
)
from ...domain.entities import (
    AtendimentoSocial,
    BeneficioEventual,
    FamiliaCadUnico,
    PessoaCadUnico,
    Sexo,
    StatusBeneficio,
    StatusFamilia,
    StatusUnidade,
    TipoAtendimento,
    TipoBeneficio,
    TipoUnidade,
    UnidadeAssistencia,
)
from ..database.models import (
    AtendimentoSocialModel,
    BeneficioEventualModel,
    FamiliaCadUnicoModel,
    PessoaCadUnicoModel,
    UnidadeAssistenciaModel,
)


class SQLAlchemyFamiliaRepository(RepositorioFamilia):
    """Persistência de famílias do CadÚnico."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, familia: FamiliaCadUnico) -> FamiliaCadUnico:
        """Insere ou atualiza uma família."""
        existente = self._session.get(FamiliaCadUnicoModel, uuid.UUID(familia.id))
        if existente is not None:
            existente.nis = familia.nis
            existente.responsavel_nome = familia.responsavel_nome
            existente.responsavel_cpf = familia.responsavel_cpf
            existente.endereco = familia.endereco
            existente.telefone = familia.telefone
            existente.renda_per_capita = familia.renda_per_capita
            existente.quantidade_pessoas = familia.quantidade_pessoas
            existente.status = familia.status.value
            existente.updated_at = familia.updated_at
            existente.is_deleted = familia.is_deleted
        else:
            self._session.add(
                FamiliaCadUnicoModel(
                    id=uuid.UUID(familia.id),
                    nis=familia.nis,
                    responsavel_nome=familia.responsavel_nome,
                    responsavel_cpf=familia.responsavel_cpf,
                    endereco=familia.endereco,
                    telefone=familia.telefone,
                    renda_per_capita=familia.renda_per_capita,
                    quantidade_pessoas=familia.quantidade_pessoas,
                    status=familia.status.value,
                    created_at=familia.created_at,
                    updated_at=familia.updated_at,
                    created_by=familia.created_by,
                    is_deleted=familia.is_deleted,
                )
            )
        self._session.flush()
        return familia

    def get_by_id(self, familia_id: str) -> FamiliaCadUnico | None:
        """Busca família por id."""
        model = self._session.get(FamiliaCadUnicoModel, uuid.UUID(familia_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_nis(self, nis: str) -> FamiliaCadUnico | None:
        """Busca família pelo NIS."""
        model = (
            self._session.query(FamiliaCadUnicoModel)
            .filter(FamiliaCadUnicoModel.nis == nis, FamiliaCadUnicoModel.is_deleted == False)
            .first()
        )  # noqa: E712
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista famílias paginadas."""
        models = (
            self._session.query(FamiliaCadUnicoModel)
            .filter(FamiliaCadUnicoModel.is_deleted == False)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )  # noqa: E712
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: FamiliaCadUnicoModel) -> FamiliaCadUnico:
        return FamiliaCadUnico(
            id=str(model.id),
            nis=model.nis or "",
            responsavel_nome=model.responsavel_nome or "",
            responsavel_cpf=model.responsavel_cpf or "",
            endereco=model.endereco or "",
            telefone=model.telefone or "",
            renda_per_capita=float(model.renda_per_capita or 0),
            quantidade_pessoas=int(model.quantidade_pessoas or 0),
            status=StatusFamilia(model.status or "ativa"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyPessoaRepository(RepositorioPessoa):
    """Persistência de pessoas do CadÚnico."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, pessoa: PessoaCadUnico) -> PessoaCadUnico:
        """Insere ou atualiza uma pessoa."""
        existente = self._session.get(PessoaCadUnicoModel, uuid.UUID(pessoa.id))
        if existente is not None:
            existente.familia_id = pessoa.familia_id
            existente.nome = pessoa.nome
            existente.cpf = pessoa.cpf
            existente.data_nascimento = pessoa.data_nascimento
            existente.sexo = pessoa.sexo.value
            existente.nome_mae = pessoa.nome_mae
            existente.parentesco = pessoa.parentesco
            existente.escolaridade = pessoa.escolaridade
            existente.ocupacao = pessoa.ocupacao
            existente.renda = pessoa.renda
            existente.updated_at = pessoa.updated_at
            existente.is_deleted = pessoa.is_deleted
        else:
            self._session.add(
                PessoaCadUnicoModel(
                    id=uuid.UUID(pessoa.id),
                    familia_id=pessoa.familia_id,
                    nome=pessoa.nome,
                    cpf=pessoa.cpf,
                    data_nascimento=pessoa.data_nascimento,
                    sexo=pessoa.sexo.value,
                    nome_mae=pessoa.nome_mae,
                    parentesco=pessoa.parentesco,
                    escolaridade=pessoa.escolaridade,
                    ocupacao=pessoa.ocupacao,
                    renda=pessoa.renda,
                    created_at=pessoa.created_at,
                    updated_at=pessoa.updated_at,
                    created_by=pessoa.created_by,
                    is_deleted=pessoa.is_deleted,
                )
            )
        self._session.flush()
        return pessoa

    def get_by_id(self, pessoa_id: str) -> PessoaCadUnico | None:
        """Busca pessoa por id."""
        model = self._session.get(PessoaCadUnicoModel, uuid.UUID(pessoa_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_cpf(self, cpf: str) -> PessoaCadUnico | None:
        """Busca pessoa pelo CPF."""
        model = (
            self._session.query(PessoaCadUnicoModel)
            .filter(PessoaCadUnicoModel.cpf == cpf, PessoaCadUnicoModel.is_deleted == False)
            .first()
        )  # noqa: E712
        return self._to_entity(model) if model else None

    def list_by_familia(self, familia_id: str) -> list:
        """Lista pessoas da família."""
        models = (
            self._session.query(PessoaCadUnicoModel)
            .filter(PessoaCadUnicoModel.familia_id == familia_id, PessoaCadUnicoModel.is_deleted == False)
            .all()
        )  # noqa: E712
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista pessoas paginadas."""
        models = (
            self._session.query(PessoaCadUnicoModel)
            .filter(PessoaCadUnicoModel.is_deleted == False)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )  # noqa: E712
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: PessoaCadUnicoModel) -> PessoaCadUnico:
        return PessoaCadUnico(
            id=str(model.id),
            familia_id=model.familia_id or "",
            nome=model.nome or "",
            cpf=model.cpf or "",
            data_nascimento=model.data_nascimento or "",
            sexo=Sexo(model.sexo or "ignorado"),
            nome_mae=model.nome_mae or "",
            parentesco=model.parentesco or "",
            escolaridade=model.escolaridade or "",
            ocupacao=model.ocupacao or "",
            renda=float(model.renda or 0),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyUnidadeRepository(RepositorioUnidade):
    """Persistência de unidades CRAS/CREAS."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, unidade: UnidadeAssistencia) -> UnidadeAssistencia:
        """Insere ou atualiza uma unidade."""
        existente = self._session.get(UnidadeAssistenciaModel, uuid.UUID(unidade.id))
        if existente is not None:
            existente.codigo = unidade.codigo
            existente.nome = unidade.nome
            existente.tipo = unidade.tipo.value
            existente.endereco = unidade.endereco
            existente.telefone = unidade.telefone
            existente.email = unidade.email
            existente.responsavel = unidade.responsavel
            existente.status = unidade.status.value
            existente.updated_at = unidade.updated_at
            existente.is_deleted = unidade.is_deleted
        else:
            self._session.add(
                UnidadeAssistenciaModel(
                    id=uuid.UUID(unidade.id),
                    codigo=unidade.codigo,
                    nome=unidade.nome,
                    tipo=unidade.tipo.value,
                    endereco=unidade.endereco,
                    telefone=unidade.telefone,
                    email=unidade.email,
                    responsavel=unidade.responsavel,
                    status=unidade.status.value,
                    created_at=unidade.created_at,
                    updated_at=unidade.updated_at,
                    created_by=unidade.created_by,
                    is_deleted=unidade.is_deleted,
                )
            )
        self._session.flush()
        return unidade

    def get_by_id(self, unidade_id: str) -> UnidadeAssistencia | None:
        """Busca unidade por id."""
        model = self._session.get(UnidadeAssistenciaModel, uuid.UUID(unidade_id))
        if model is None or model.is_deleted:
            return None
        return self._to_entity(model)

    def get_by_codigo(self, codigo: str) -> UnidadeAssistencia | None:
        """Busca unidade pelo código."""
        model = (
            self._session.query(UnidadeAssistenciaModel)
            .filter(UnidadeAssistenciaModel.codigo == codigo, UnidadeAssistenciaModel.is_deleted == False)
            .first()
        )  # noqa: E712
        return self._to_entity(model) if model else None

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista unidades paginadas."""
        models = (
            self._session.query(UnidadeAssistenciaModel)
            .filter(UnidadeAssistenciaModel.is_deleted == False)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )  # noqa: E712
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: UnidadeAssistenciaModel) -> UnidadeAssistencia:
        return UnidadeAssistencia(
            id=str(model.id),
            codigo=model.codigo or "",
            nome=model.nome or "",
            tipo=TipoUnidade(model.tipo or "cras"),
            endereco=model.endereco or "",
            telefone=model.telefone or "",
            email=model.email or "",
            responsavel=model.responsavel or "",
            status=StatusUnidade(model.status or "ativa"),
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
            is_deleted=bool(model.is_deleted),
        )


class SQLAlchemyBeneficioRepository(RepositorioBeneficio):
    """Persistência de benefícios eventuais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, beneficio: BeneficioEventual) -> BeneficioEventual:
        """Insere ou atualiza um benefício."""
        existente = self._session.get(BeneficioEventualModel, uuid.UUID(beneficio.id))
        if existente is not None:
            existente.familia_id = beneficio.familia_id
            existente.tipo = beneficio.tipo.value
            existente.descricao = beneficio.descricao
            existente.valor = beneficio.valor
            existente.quantidade = str(beneficio.quantidade)
            existente.data_solicitacao = beneficio.data_solicitacao
            existente.data_aprovacao = beneficio.data_aprovacao
            existente.data_entrega = beneficio.data_entrega
            existente.status = beneficio.status.value
            existente.unidade_id = beneficio.unidade_id
            existente.observacao = beneficio.observacao
            existente.updated_at = beneficio.updated_at
        else:
            self._session.add(
                BeneficioEventualModel(
                    id=uuid.UUID(beneficio.id),
                    familia_id=beneficio.familia_id,
                    tipo=beneficio.tipo.value,
                    descricao=beneficio.descricao,
                    valor=beneficio.valor,
                    quantidade=str(beneficio.quantidade),
                    data_solicitacao=beneficio.data_solicitacao,
                    data_aprovacao=beneficio.data_aprovacao,
                    data_entrega=beneficio.data_entrega,
                    status=beneficio.status.value,
                    unidade_id=beneficio.unidade_id,
                    observacao=beneficio.observacao,
                    created_at=beneficio.created_at,
                    updated_at=beneficio.updated_at,
                    created_by=beneficio.created_by,
                )
            )
        self._session.flush()
        return beneficio

    def get_by_id(self, beneficio_id: str) -> BeneficioEventual | None:
        """Busca benefício por id."""
        model = self._session.get(BeneficioEventualModel, uuid.UUID(beneficio_id))
        if model is None:
            return None
        return self._to_entity(model)

    def list_by_familia(self, familia_id: str) -> list:
        """Lista benefícios da família."""
        models = (
            self._session.query(BeneficioEventualModel)
            .filter(BeneficioEventualModel.familia_id == familia_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista benefícios paginados."""
        models = (
            self._session.query(BeneficioEventualModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: BeneficioEventualModel) -> BeneficioEventual:
        return BeneficioEventual(
            id=str(model.id),
            familia_id=model.familia_id or "",
            tipo=TipoBeneficio(model.tipo or "alimentacao"),
            descricao=model.descricao or "",
            valor=float(model.valor or 0),
            quantidade=int(model.quantidade or 1),
            data_solicitacao=model.data_solicitacao,
            data_aprovacao=model.data_aprovacao,
            data_entrega=model.data_entrega,
            status=StatusBeneficio(model.status or "solicitado"),
            unidade_id=model.unidade_id or "",
            observacao=model.observacao or "",
            created_at=model.created_at,
            updated_at=model.updated_at,
            created_by=model.created_by or "",
        )


class SQLAlchemyAtendimentoRepository(RepositorioAtendimento):
    """Persistência de atendimentos sociais."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, atendimento: AtendimentoSocial) -> AtendimentoSocial:
        """Insere ou atualiza um atendimento."""
        self._session.add(
            AtendimentoSocialModel(
                id=uuid.UUID(atendimento.id),
                pessoa_id=atendimento.pessoa_id,
                unidade_id=atendimento.unidade_id,
                tipo=atendimento.tipo.value,
                data=atendimento.data,
                descricao=atendimento.descricao,
                encaminhamento=atendimento.encaminhamento,
                profissional=atendimento.profissional,
                created_at=atendimento.created_at,
                created_by=atendimento.created_by,
            )
        )
        self._session.flush()
        return atendimento

    def get_by_id(self, atendimento_id: str) -> AtendimentoSocial | None:
        """Busca atendimento por id."""
        model = self._session.get(AtendimentoSocialModel, uuid.UUID(atendimento_id))
        if model is None:
            return None
        return self._to_entity(model)

    def list_by_pessoa(self, pessoa_id: str) -> list:
        """Lista atendimentos da pessoa."""
        models = (
            self._session.query(AtendimentoSocialModel)
            .filter(AtendimentoSocialModel.pessoa_id == pessoa_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_by_unidade(self, unidade_id: str) -> list:
        """Lista atendimentos da unidade."""
        models = (
            self._session.query(AtendimentoSocialModel)
            .filter(AtendimentoSocialModel.unidade_id == unidade_id)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def list_all(self, page: int = 1, page_size: int = 20) -> list:
        """Lista atendimentos paginados."""
        models = (
            self._session.query(AtendimentoSocialModel)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )
        return [self._to_entity(m) for m in models]

    def _to_entity(self, model: AtendimentoSocialModel) -> AtendimentoSocial:
        return AtendimentoSocial(
            id=str(model.id),
            pessoa_id=model.pessoa_id or "",
            unidade_id=model.unidade_id or "",
            tipo=TipoAtendimento(model.tipo or "acolhimento"),
            data=model.data,
            descricao=model.descricao or "",
            encaminhamento=model.encaminhamento or "",
            profissional=model.profissional or "",
            created_at=model.created_at,
            created_by=model.created_by or "",
        )


__all__ = [
    "SQLAlchemyFamiliaRepository",
    "SQLAlchemyPessoaRepository",
    "SQLAlchemyUnidadeRepository",
    "SQLAlchemyBeneficioRepository",
    "SQLAlchemyAtendimentoRepository",
]
