"""Implementação SQLAlchemy do repositório de Pessoas (DOM-CUM).

Implementa o contrato ``PessoaRepository`` do domínio sobre as tabelas
``core.pessoas``, ``core.pessoas_fisicas``, ``core.pessoas_juridicas``,
``core.enderecos``, ``core.documentos`` e ``core.contatos``
(migrations 20260820_01 e 20260831_02).

Observações de projeto:
  - O repositório executa ``flush`` (não ``commit``); a transação é
    controlada pela sessão da requisição (ver core get_db).
  - RN-CUM-004: a unicidade de documento considera apenas registros
    vivos; exclusões lógicas liberam o número para reuso.
  - RN-CUM-007: exclusão lógica em cascata (pessoa, extensão e filhos).
"""

from __future__ import annotations

import builtins
import logging
import re
from uuid import UUID

from sqlalchemy import func, select, update
import sqlalchemy as ja
from sqlalchemy.orm import Session

from src.modules.sigmun_cadastro.domain.entities.contato import Contato, TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import Documento, TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import Endereco, TipoEndereco
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    DadosFisicos,
    DadosJuridicos,
    Pessoa,
    Sexo,
    TipoPessoa,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import PessoaRepository
from src.modules.sigmun_cadastro.infrastructure.database.models import (
    ContatoModel,
    DocumentoModel,
    EnderecoModel,
    PessoaFisicaModel,
    PessoaJuridicaModel,
    PessoaModel,
)

logger = logging.getLogger(__name__)


def _to_endereco_entity(model: EnderecoModel) -> Endereco:
    """Converte um registro ORM de endereço em entidade de domínio."""
    return Endereco(
        id=model.id,
        pessoa_id=model.pessoa_id,
        tipo=TipoEndereco(model.tipo),
        logradouro=model.logradouro,
        numero=model.numero,
        complemento=model.complemento,
        bairro=model.bairro,
        cep=model.cep,
        cidade=model.cidade,
        estado=model.estado,
        pais=model.pais,
        principal=model.principal,
        vigencia_inicio=model.vigencia_inicio,
        vigencia_fim=model.vigencia_fim,
        motivo_alteracao=model.motivo_alteracao,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


def _to_documento_entity(model: DocumentoModel) -> Documento:
    """Converte um registro ORM de documento em entidade de domínio."""
    return Documento(
        id=model.id,
        pessoa_id=model.pessoa_id,
        tipo=TipoDocumento(model.tipo),
        numero=model.numero,
        orgao_emissor=model.orgao_emissor,
        data_emissao=model.data_emissao,
        data_validade=model.data_validade,
        principal=model.principal,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


def _to_contato_entity(model: ContatoModel) -> Contato:
    """Converte um registro ORM de contato em entidade de domínio."""
    return Contato(
        id=model.id,
        pessoa_id=model.pessoa_id,
        tipo=TipoContato(model.tipo),
        valor=model.valor,
        principal=model.principal,
        created_at=model.created_at,
        created_by=model.created_by,
        updated_at=model.updated_at,
        updated_by=model.updated_by,
        deleted_at=model.deleted_at,
        deleted_by=model.deleted_by,
    )


class SqlAlchemyPessoaRepository(PessoaRepository):
    """Repositório de pessoas (agregado completo) persistido via SQLAlchemy."""

    def __init__(self, session: Session) -> None:
        self._session = session

    # -- Helpers -------------------------------------------------------------------

    def _get_model(self, pessoa_id: UUID, *, include_deleted: bool = False) -> PessoaModel | None:
        model = self._session.get(PessoaModel, pessoa_id)
        if model is None:
            return None
        if model.deleted_at is not None and not include_deleted:
            return None
        return model

    def _hydrate(self, model: PessoaModel, *, include_deleted: bool = False) -> Pessoa:
        """Hidrata o agregado completo (raiz + extensão + filhos)."""
        dados_fisicos: DadosFisicos | None = None
        dados_juridicos: DadosJuridicos | None = None

        pf = self._session.scalars(
            select(PessoaFisicaModel).where(
                PessoaFisicaModel.pessoa_id == model.id,
                PessoaFisicaModel.deleted_at.is_(None) if not include_deleted else ja.true(),
            )
        ).first()
        if pf is not None:
            dados_fisicos = DadosFisicos(
                nome=pf.nome,
                data_nascimento=pf.data_nascimento,
                sexo=Sexo(pf.sexo) if pf.sexo else None,
                estado_civil=pf.estado_civil,
                mae=pf.mae,
                pai=pf.pai,
            )
        else:
            pj = self._session.scalars(
                select(PessoaJuridicaModel).where(
                    PessoaJuridicaModel.pessoa_id == model.id,
                    PessoaJuridicaModel.deleted_at.is_(None) if not include_deleted else ja.true(),
                )
            ).first()
            if pj is not None:
                dados_juridicos = DadosJuridicos(
                    razao_social=pj.razao_social,
                    nome_fantasia=pj.nome_fantasia,
                    cnae_principal=pj.cnae_principal,
                    capital=pj.capital,
                )

        enderecos = [
            _to_endereco_entity(m)
            for m in self._session.scalars(
                select(EnderecoModel).where(EnderecoModel.pessoa_id == model.id)
            ).all()
        ]
        documentos = [
            _to_documento_entity(m)
            for m in self._session.scalars(
                select(DocumentoModel).where(DocumentoModel.pessoa_id == model.id)
            ).all()
        ]
        contatos = [
            _to_contato_entity(m)
            for m in self._session.scalars(
                select(ContatoModel).where(ContatoModel.pessoa_id == model.id)
            ).all()
        ]

        return Pessoa(
            id=model.id,
            tipo=TipoPessoa(model.tipo),
            categoria=CategoriaPessoa(model.categoria),
            unidade_id=model.unidade_id,
            dados_fisicos=dados_fisicos,
            dados_juridicos=dados_juridicos,
            enderecos=enderecos,
            documentos=documentos,
            contatos=contatos,
            created_at=model.created_at,
            created_by=model.created_by,
            updated_at=model.updated_at,
            updated_by=model.updated_by,
            deleted_at=model.deleted_at,
            deleted_by=model.deleted_by,
        )

    # -- Contrato do domínio ------------------------------------------------------

    def save(self, pessoa: Pessoa) -> Pessoa:
        model = self._session.get(PessoaModel, pessoa.id)
        if model is None:
            model = PessoaModel(
                id=pessoa.id,
                tipo=pessoa.tipo.value,
                categoria=pessoa.categoria.value,
                unidade_id=pessoa.unidade_id,
                created_at=pessoa.created_at,
                created_by=pessoa.created_by,
                updated_at=pessoa.updated_at,
                updated_by=pessoa.updated_by,
                deleted_at=pessoa.deleted_at,
                deleted_by=pessoa.deleted_by,
            )
            self._session.add(model)
            logger.info("Pessoa inserida: %s", pessoa.id)
        else:
            model.tipo = pessoa.tipo.value
            model.categoria = pessoa.categoria.value
            model.unidade_id = pessoa.unidade_id
            model.updated_at = pessoa.updated_at
            model.updated_by = pessoa.updated_by
            model.deleted_at = pessoa.deleted_at
            model.deleted_by = pessoa.deleted_by
            logger.info("Pessoa atualizada: %s", pessoa.id)

        self._salvar_extensao(pessoa)
        self._sync_enderecos(pessoa)
        self._sync_documentos(pessoa)
        self._sync_contatos(pessoa)
        self._session.flush()
        return self._hydrate(model)

    def get_by_id(
        self, pessoa_id: UUID, *, include_deleted: bool = False
    ) -> Pessoa | None:
        model = self._get_model(pessoa_id, include_deleted=include_deleted)
        return self._hydrate(model, include_deleted=include_deleted) if model else None

    def list(
        self,
        *,
        tipo: TipoPessoa | None = None,
        categoria: CategoriaPessoa | None = None,
        include_deleted: bool = False,
        limit: int | None = None,
        offset: int = 0,
    ) -> builtins.list[Pessoa]:
        stmt = select(PessoaModel).order_by(PessoaModel.created_at)
        if not include_deleted:
            stmt = stmt.where(PessoaModel.deleted_at.is_(None))
        if tipo is not None:
            stmt = stmt.where(PessoaModel.tipo == tipo.value)
        if categoria is not None:
            stmt = stmt.where(PessoaModel.categoria == categoria.value)
        if limit is not None:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        return [self._hydrate(m, include_deleted=include_deleted) for m in self._session.scalars(stmt).all()]

    def delete(self, pessoa_id: UUID, usuario_id: UUID) -> None:
        """Soft-delete da pessoa e de extensão/filhos (RN-CUM-007)."""
        model = self._get_model(pessoa_id, include_deleted=True)
        if model is None or model.deleted_at is not None:
            return
        model.deleted_at = func.now()
        model.deleted_by = usuario_id
        for modelo_filho in (
            PessoaFisicaModel,
            PessoaJuridicaModel,
            EnderecoModel,
            DocumentoModel,
            ContatoModel,
        ):
            self._session.execute(
                update(modelo_filho)
                .where(modelo_filho.pessoa_id == pessoa_id, modelo_filho.deleted_at.is_(None))
                .values(deleted_at=func.now(), deleted_by=usuario_id)
            )
        self._session.flush()
        logger.info("Pessoa marcada como excluída: %s", pessoa_id)

    def exists_documento(self, tipo: TipoDocumento, numero: str) -> bool:
        """Verifica unicidade de documento entre pessoas vivas (RN-CUM-004).

        O número é normalizado (remove não-dígitos) para permitir busca
        tanto formatada (``529.982.247-25``) quanto pura (``52998224725``).
        """
        numero_normalizado = re.sub(r"\D", "", numero)
        stmt = (
            select(DocumentoModel.id)
            .where(
                DocumentoModel.tipo == tipo.value,
                DocumentoModel.numero == numero_normalizado,
                DocumentoModel.deleted_at.is_(None),
            )
            .limit(1)
        )
        return self._session.scalars(stmt).first() is not None

    # -- Internals -----------------------------------------------------------------

    def _salvar_extensao(self, pessoa: Pessoa) -> None:
        """Sobresscreve a extensão 1:1 (física ou jurídica) da pessoa."""
        if pessoa.dados_fisicos is not None:
            d = pessoa.dados_fisicos
            pf = self._session.scalars(
                select(PessoaFisicaModel).where(PessoaFisicaModel.pessoa_id == pessoa.id)
            ).first()
            if pf is None:
                self._session.add(
                    PessoaFisicaModel(
                        pessoa_id=pessoa.id,
                        nome=d.nome,
                        data_nascimento=d.data_nascimento,
                        sexo=d.sexo.value if d.sexo else None,
                        estado_civil=d.estado_civil,
                        mae=d.mae,
                        pai=d.pai,
                        created_at=pessoa.created_at,
                        created_by=pessoa.created_by,
                        updated_at=pessoa.updated_at,
                        updated_by=pessoa.updated_by,
                        deleted_at=pessoa.deleted_at,
                        deleted_by=pessoa.deleted_by,
                    )
                )
            else:
                pf.nome = d.nome
                pf.data_nascimento = d.data_nascimento
                pf.sexo = d.sexo.value if d.sexo else None
                pf.estado_civil = d.estado_civil
                pf.mae = d.mae
                pf.pai = d.pai
                pf.updated_at = pessoa.updated_at
                pf.updated_by = pessoa.updated_by
                pf.deleted_at = pessoa.deleted_at
                pf.deleted_by = pessoa.deleted_by
        elif pessoa.dados_juridicos is not None:
            d = pessoa.dados_juridicos
            pj = self._session.scalars(
                select(PessoaJuridicaModel).where(PessoaJuridicaModel.pessoa_id == pessoa.id)
            ).first()
            if pj is None:
                self._session.add(
                    PessoaJuridicaModel(
                        pessoa_id=pessoa.id,
                        razao_social=d.razao_social,
                        nome_fantasia=d.nome_fantasia,
                        cnae_principal=d.cnae_principal,
                        capital=d.capital,
                        created_at=pessoa.created_at,
                        created_by=pessoa.created_by,
                        updated_at=pessoa.updated_at,
                        updated_by=pessoa.updated_by,
                        deleted_at=pessoa.deleted_at,
                        deleted_by=pessoa.deleted_by,
                    )
                )
            else:
                pj.razao_social = d.razao_social
                pj.nome_fantasia = d.nome_fantasia
                pj.cnae_principal = d.cnae_principal
                pj.capital = d.capital
                pj.updated_at = pessoa.updated_at
                pj.updated_by = pessoa.updated_by
                pj.deleted_at = pessoa.deleted_at
                pj.deleted_by = pessoa.deleted_by

    def _sync_enderecos(self, pessoa: Pessoa) -> None:
        """Sincroniza os endereços do agregado com a persistência."""
        existentes = {
            m.id: m
            for m in self._session.scalars(
                select(EnderecoModel).where(EnderecoModel.pessoa_id == pessoa.id)
            ).all()
        }
        atuais = {e.id for e in pessoa.enderecos}
        for e in pessoa.enderecos:
            m = existentes.get(e.id)
            if m is None:
                self._session.add(
                    EnderecoModel(
                        id=e.id,
                        pessoa_id=e.pessoa_id,
                        tipo=e.tipo.value,
                        logradouro=e.logradouro,
                        numero=e.numero,
                        complemento=e.complemento,
                        bairro=e.bairro,
                        cep=e.cep,
                        cidade=e.cidade,
                        estado=e.estado,
                        pais=e.pais,
                        principal=e.principal,
                        vigencia_inicio=e.vigencia_inicio,
                        vigencia_fim=e.vigencia_fim,
                        motivo_alteracao=e.motivo_alteracao,
                        created_at=e.created_at,
                        created_by=e.created_by,
                        updated_at=e.updated_at,
                        updated_by=e.updated_by,
                        deleted_at=e.deleted_at,
                        deleted_by=e.deleted_by,
                    )
                )
            else:
                m.tipo = e.tipo.value
                m.logradouro = e.logradouro
                m.numero = e.numero
                m.complemento = e.complemento
                m.bairro = e.bairro
                m.cep = e.cep
                m.cidade = e.cidade
                m.estado = e.estado
                m.pais = e.pais
                m.principal = e.principal
                m.vigencia_inicio = e.vigencia_inicio
                m.vigencia_fim = e.vigencia_fim
                m.motivo_alteracao = e.motivo_alteracao
                m.updated_at = e.updated_at
                m.updated_by = e.updated_by
                m.deleted_at = e.deleted_at
                m.deleted_by = e.deleted_by
        for id_existente, m in existentes.items():
            if id_existente not in atuais and m.deleted_at is None:
                m.deleted_at = func.now()
                m.motivo_alteracao = m.motivo_alteracao or "Removido do agregado"

    def _sync_documentos(self, pessoa: Pessoa) -> None:
        """Sincroniza os documentos do agregado com a persistência."""
        existentes = {
            m.id: m
            for m in self._session.scalars(
                select(DocumentoModel).where(DocumentoModel.pessoa_id == pessoa.id)
            ).all()
        }
        atuais = {d.id for d in pessoa.documentos}
        for d in pessoa.documentos:
            m = existentes.get(d.id)
            if m is None:
                self._session.add(
                    DocumentoModel(
                        id=d.id,
                        pessoa_id=d.pessoa_id,
                        tipo=d.tipo.value,
                        numero=d.numero,
                        orgao_emissor=d.orgao_emissor,
                        data_emissao=d.data_emissao,
                        data_validade=d.data_validade,
                        principal=d.principal,
                        created_at=d.created_at,
                        created_by=d.created_by,
                        updated_at=d.updated_at,
                        updated_by=d.updated_by,
                        deleted_at=d.deleted_at,
                        deleted_by=d.deleted_by,
                    )
                )
            else:
                m.tipo = d.tipo.value
                m.numero = d.numero
                m.orgao_emissor = d.orgao_emissor
                m.data_emissao = d.data_emissao
                m.data_validade = d.data_validade
                m.principal = d.principal
                m.updated_at = d.updated_at
                m.updated_by = d.updated_by
                m.deleted_at = d.deleted_at
                m.deleted_by = d.deleted_by
        for id_existente, m in existentes.items():
            if id_existente not in atuais and m.deleted_at is None:
                m.deleted_at = func.now()

    def _sync_contatos(self, pessoa: Pessoa) -> None:
        """Sincroniza os contatos do agregado com a persistência."""
        existentes = {
            m.id: m
            for m in self._session.scalars(
                select(ContatoModel).where(ContatoModel.pessoa_id == pessoa.id)
            ).all()
        }
        atuais = {c.id for c in pessoa.contatos}
        for c in pessoa.contatos:
            m = existentes.get(c.id)
            if m is None:
                self._session.add(
                    ContatoModel(
                        id=c.id,
                        pessoa_id=c.pessoa_id,
                        tipo=c.tipo.value,
                        valor=c.valor,
                        principal=c.principal,
                        created_at=c.created_at,
                        created_by=c.created_by,
                        updated_at=c.updated_at,
                        updated_by=c.updated_by,
                        deleted_at=c.deleted_at,
                        deleted_by=c.deleted_by,
                    )
                )
            else:
                m.tipo = c.tipo.value
                m.valor = c.valor
                m.principal = c.principal
                m.updated_at = c.updated_at
                m.updated_by = c.updated_by
                m.deleted_at = c.deleted_at
                m.deleted_by = c.deleted_by
        for id_existente, m in existentes.items():
            if id_existente not in atuais and m.deleted_at is None:
                m.deleted_at = func.now()


__all__ = ["SqlAlchemyPessoaRepository"]
