"""Testes de integração das implementações SQLAlchemy (infrastructure).

Exercitam as seis implementações concretas de repositório do domínio Compras
contra o PostgreSQL local (docker compose), validando CRUD/soft-delete,
filtros, paginação e verificação de vínculos.

Isolamento: cada teste executa dentro de uma transação revertida (rollback)
ao final, sem deixar dados persistentes no banco.

Dependência: PostgreSQL acessível em ``settings.DATABASE_URL`` com as
migrações ``20260820_01`` a ``20260823_01`` aplicadas (ver Makefile docker-up).
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID, uuid4

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import engine
from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import (
    Fornecedor,
    SituacaoFornecedor,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
    ResultadoEventoAuditoria,
)
from src.modules.sigmun_compras.infrastructure.repositories import (
    SqlAlchemyCompraRepository,
    SqlAlchemyContratoRepository,
    SqlAlchemyFornecedorRepository,
    SqlAlchemyItemCompraRepository,
    SqlAlchemyProcessoDocumentalRepository,
    SqlAlchemyTrilhaAuditoriaRepository,
)

# -- Fixtures ------------------------------------------------------------------


@pytest.fixture
def session() -> Session:
    """Sessão com transação revertida (rollback) ao final de cada teste."""
    connection = engine.connect()
    connection.begin()
    try:
        yield Session(bind=connection, expire_on_commit=False)
    finally:
        connection.rollback()
        connection.close()


# -- Helpers de dados de apoio (tabelas do núcleo corporativo) -----------------


def _criar_unidade(session: Session) -> UUID:
    """Insere uma unidade administrativa em ``core.unidades_administrativas``.

    A sigla é gerada com sufixo aleatório porque a coluna ``sigla`` possui
    constraint UNIQUE no banco.
    """
    unidade_id = uuid4()
    session.execute(
        text(
            "INSERT INTO core.unidades_administrativas (id, nome, sigla) "
            "VALUES (:id, :nome, :sigla)"
        ),
        {
            "id": unidade_id,
            "nome": f"Secretaria Municipal {uuid4().hex[:6].upper()}",
            "sigla": f"SMT{uuid4().hex[:4].upper()}",
        },
    )
    return unidade_id


def _criar_pessoa_juridica(session: Session) -> UUID:
    """Insere pessoa jurídica válida (cadeia: pessoas -> pessoas_juridicas)."""
    pessoa_id = uuid4()
    session.execute(
        text(
            "INSERT INTO core.pessoas (id, tipo, categoria) "
            "VALUES (:id, 'JURIDICA', 'FORNECEDOR')"
        ),
        {"id": pessoa_id},
    )
    pj_id = uuid4()
    session.execute(
        text(
            "INSERT INTO core.pessoas_juridicas (id, pessoa_id, razao_social, nome_fantasia) "
            "VALUES (:id, :pessoa_id, :razao_social, :nome_fantasia)"
        ),
        {
            "id": pj_id,
            "pessoa_id": pessoa_id,
            "razao_social": "Fornecedora Teste Ltda",
            "nome_fantasia": "Fornecedora Teste",
        },
    )
    return pj_id


def _criar_cadeia_base(session: Session) -> dict:
    """Cria a cadeia mínima: unidade, fornecedor ativo e processo documental."""
    unidade_id = _criar_unidade(session)
    pj_id = _criar_pessoa_juridica(session)

    fornecedor = SqlAlchemyFornecedorRepository(session).save(
        Fornecedor(pessoa_juridica_id=pj_id)
    )

    processo = SqlAlchemyProcessoDocumentalRepository(session).save(
        ProcessoDocumental(
            unidade_id=unidade_id,
            numero=f"P-{uuid4().hex[:8].upper()}",
            ano=2026,
            assunto="Aquisição de materiais de escritório",
            descricao="Processo criado em teste de integração",
        )
    )

    return {
        "unidade_id": unidade_id,
        "pj_id": pj_id,
        "fornecedor": fornecedor,
        "processo": processo,
    }


def _criar_compra(session: Session, cadeia: dict | None = None) -> Compra:
    cadeia = cadeia or _criar_cadeia_base(session)
    return SqlAlchemyCompraRepository(session).save(
        Compra(
            processo_documental_id=cadeia["processo"].id,
            fornecedor_id=cadeia["fornecedor"].id,
            unidade_id=cadeia["unidade_id"],
            numero="001/2026",
            data=date(2026, 1, 5),
            valor_total=Decimal("1234.56"),
            situacao=SituacaoCompra.RASCUNHO,
        )
    )


# -- Fornecedor ----------------------------------------------------------------


class TestSqlAlchemyFornecedorRepository:
    def test_save_e_get_by_id_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        pj_id = _criar_pessoa_juridica(session)

        salvo = repo.save(Fornecedor(pessoa_juridica_id=pj_id))

        assert salvo.id is not None
        assert salvo.situacao_cadastro == SituacaoFornecedor.ATIVO
        assert salvo.created_at is not None

        obtido = repo.get_by_id(salvo.id)
        assert obtido is not None
        assert obtido.pessoa_juridica_id == pj_id
        assert obtido.macro_categoria is None

    def test_get_by_id_inexistente_retorna_none(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)

        assert repo.get_by_id(uuid4()) is None

    def test_get_by_pessoa_juridica_id(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        pj_id = _criar_pessoa_juridica(session)
        salvo = repo.save(Fornecedor(pessoa_juridica_id=pj_id))

        obtido = repo.get_by_pessoa_juridica_id(pj_id)

        assert obtido is not None
        assert obtido.id == salvo.id

    def test_list_filtra_por_situacao_e_pagina(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        pj_ativo = _criar_pessoa_juridica(session)
        pj_suspenso = _criar_pessoa_juridica(session)

        ativo = repo.save(Fornecedor(pessoa_juridica_id=pj_ativo))
        suspenso = repo.save(
            Fornecedor(
                pessoa_juridica_id=pj_suspenso,
                situacao_cadastro=SituacaoFornecedor.SUSPENSO,
            )
        )

        todos = repo.list()
        ativos = repo.list(situacao=SituacaoFornecedor.ATIVO)
        primeira_pagina = repo.list(limit=1, offset=0)

        ids_todos = {f.id for f in todos}
        assert {ativo.id, suspenso.id} <= ids_todos
        assert ativo.id in {f.id for f in ativos}
        assert suspenso.id not in {f.id for f in ativos}
        assert len(primeira_pagina) == 1

    def test_update_reflete_dados_alterados(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        salvo = repo.save(
            Fornecedor(pessoa_juridica_id=_criar_pessoa_juridica(session))
        )

        salvo.macro_categoria = "MATERIAL_ESCRITORIO"
        atualizado = repo.update(salvo)

        assert atualizado.macro_categoria == "MATERIAL_ESCRITORIO"
        assert repo.get_by_id(salvo.id).macro_categoria == "MATERIAL_ESCRITORIO"

    def test_delete_marca_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        usuario = uuid4()
        salvo = repo.save(
            Fornecedor(pessoa_juridica_id=_criar_pessoa_juridica(session))
        )
        assert salvo.foi_excluido() is False

        repo.delete(salvo.id, usuario)

        obtido = repo.get_by_id(salvo.id)
        assert obtido is not None
        assert obtido.foi_excluido() is True
        assert obtido.deleted_by == usuario
        # Listagem padrão oculta excluídos; include_deleted expõe.
        assert obtido.id not in {f.id for f in repo.list()}
        assert obtido.id in {f.id for f in repo.list(include_deleted=True)}

    def test_exists_pessoa_juridica(self, session: Session) -> None:
        repo = SqlAlchemyFornecedorRepository(session)
        pj_id = _criar_pessoa_juridica(session)

        assert repo.exists_pessoa_juridica(pj_id) is False

        repo.save(Fornecedor(pessoa_juridica_id=pj_id))

        assert repo.exists_pessoa_juridica(pj_id) is True


# -- Processo Documental --------------------------------------------------------


class TestSqlAlchemyProcessoDocumentalRepository:
    def test_save_e_get_by_id_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        unidade_id = _criar_unidade(session)

        salvo = repo.save(
            ProcessoDocumental(
                unidade_id=unidade_id,
                numero="2026-001",
                ano=2026,
                assunto="Pregão eletrônico",
                descricao="Processo teste",
            )
        )

        assert salvo.id is not None
        assert salvo.created_at is not None

        obtido = repo.get_by_id(salvo.id)
        assert obtido is not None
        assert obtido.numero == "2026-001"
        assert obtido.ano == 2026
        assert obtido.unidade_id == unidade_id

    def test_get_by_id_inexistente_retorna_none(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)

        assert repo.get_by_id(uuid4()) is None

    def test_list_filtra_unidade_ano_e_pagina(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        unidade_a = _criar_unidade(session)
        unidade_b = _criar_unidade(session)

        ano_2026 = repo.save(
            ProcessoDocumental(
                unidade_id=unidade_a, numero="2026-001", ano=2026, assunto="A"
            )
        )
        repo.save(
            ProcessoDocumental(
                unidade_id=unidade_a, numero="2027-001", ano=2027, assunto="B"
            )
        )
        outra_unidade = repo.save(
            ProcessoDocumental(
                unidade_id=unidade_b, numero="2026-002", ano=2026, assunto="C"
            )
        )

        por_unidade_e_ano = repo.list(unidade_id=unidade_a, ano=2026)
        primeira_pagina = repo.list(limit=1)

        assert [p.id for p in por_unidade_e_ano] == [ano_2026.id]
        assert len(primeira_pagina) == 1
        assert outra_unidade.id in {p.id for p in repo.list()}

    def test_update_reflete_dados_alterados(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        unidade_id = _criar_unidade(session)
        salvo = repo.save(
            ProcessoDocumental(
                unidade_id=unidade_id, numero="2026-001", ano=2026, assunto="Inicial"
            )
        )

        salvo.assunto = "Alterado"
        atualizado = repo.update(salvo)

        assert atualizado.assunto == "Alterado"
        assert repo.get_by_id(salvo.id).assunto == "Alterado"

    def test_delete_marca_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        usuario = uuid4()
        salvo = repo.save(
            ProcessoDocumental(
                unidade_id=_criar_unidade(session),
                numero="2026-001",
                ano=2026,
                assunto="A",
            )
        )

        repo.delete(salvo.id, usuario)

        obtido = repo.get_by_id(salvo.id)
        assert obtido is not None
        assert obtido.foi_excluido() is True
        assert obtido.deleted_by == usuario
        assert obtido.id not in {p.id for p in repo.list()}
        assert obtido.id in {p.id for p in repo.list(include_deleted=True)}

    def test_exists_unidade(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        unidade_id = _criar_unidade(session)

        assert repo.exists_unidade(unidade_id) is True
        assert repo.exists_unidade(uuid4()) is False

    def test_exists_numero_ano(self, session: Session) -> None:
        repo = SqlAlchemyProcessoDocumentalRepository(session)
        salvo = repo.save(
            ProcessoDocumental(
                unidade_id=_criar_unidade(session),
                numero="2026-001",
                ano=2026,
                assunto="A",
            )
        )

        assert repo.exists_numero_ano("2026-001", 2026) is True
        assert repo.exists_numero_ano("2026-001", 2027) is False
        # Excluir o próprio registro permite atualizações sem falso positivo.
        assert repo.exists_numero_ano("2026-001", 2026, excluir_id=salvo.id) is False


# -- Item de Compra -------------------------------------------------------------


class TestSqlAlchemyItemCompraRepository:
    def test_save_e_get_by_id_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)
        compra = _criar_compra(session)

        salvo = repo.save(
            ItemCompra(
                compra_id=compra.id,
                descricao="Resma de papel A4",
                quantidade=Decimal("10"),
                valor_unitario=Decimal("22.50"),
            )
        )

        # valor_total recalculado pela entidade: 10 * 22.50 = 225.00
        assert salvo.valor_total == Decimal("225.00")
        assert salvo.created_at is not None

        obtido = repo.get_by_id(salvo.id)
        assert obtido is not None
        assert obtido.compra_id == compra.id
        assert obtido.descricao == "Resma de papel A4"

    def test_get_by_id_inexistente_retorna_none(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)

        assert repo.get_by_id(uuid4()) is None

    def test_list_by_compra_com_paginacao(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)
        compra = _criar_compra(session)

        item1 = repo.save(
            ItemCompra(
                compra_id=compra.id,
                descricao="Item 1",
                quantidade=Decimal("1"),
                valor_unitario=Decimal("10"),
            )
        )
        item2 = repo.save(
            ItemCompra(
                compra_id=compra.id,
                descricao="Item 2",
                quantidade=Decimal("2"),
                valor_unitario=Decimal("20"),
            )
        )

        itens = repo.list_by_compra(compra.id)
        pagina = repo.list_by_compra(compra.id, limit=1)

        assert {i.id for i in itens} == {item1.id, item2.id}
        assert len(pagina) == 1

    def test_update_recalcula_valor_total(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)
        compra = _criar_compra(session)
        salvo = repo.save(
            ItemCompra(
                compra_id=compra.id,
                descricao="Item",
                quantidade=Decimal("2"),
                valor_unitario=Decimal("10"),
            )
        )

        # O recalculo do valor total é responsabilidade da entidade; o
        # repositório persiste o estado corrente.
        salvo.atualizar_dados(quantidade=Decimal("5"))
        atualizado = repo.update(salvo)

        assert atualizado.valor_total == Decimal("50.00")

    def test_delete_marca_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)
        compra = _criar_compra(session)
        salvo = repo.save(
            ItemCompra(
                compra_id=compra.id,
                descricao="Item",
                quantidade=Decimal("1"),
                valor_unitario=Decimal("10"),
            )
        )

        repo.delete(salvo.id, uuid4())

        assert repo.get_by_id(salvo.id).foi_excluido() is True
        assert salvo.id not in {i.id for i in repo.list_by_compra(compra.id)}
        assert salvo.id in {
            i.id for i in repo.list_by_compra(compra.id, include_deleted=True)
        }

    def test_exists_compra(self, session: Session) -> None:
        repo = SqlAlchemyItemCompraRepository(session)
        compra = _criar_compra(session)

        assert repo.exists_compra(compra.id) is True
        assert repo.exists_compra(uuid4()) is False


# -- Compra ---------------------------------------------------------------------


class TestSqlAlchemyCompraRepository:
    def test_save_e_get_by_id_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        compra = _criar_compra(session)

        assert compra.id is not None
        assert compra.situacao == SituacaoCompra.RASCUNHO
        assert compra.created_at is not None

        obtido = repo.get_by_id(compra.id)
        assert obtido is not None
        assert obtido.numero == "001/2026"
        assert obtido.fornecedor_id == compra.fornecedor_id
        assert obtido.pendencias_impeditivas is False

    def test_get_by_id_inexistente_retorna_none(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)

        assert repo.get_by_id(uuid4()) is None

    def test_list_filtra_por_situacao(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        cadeia = _criar_cadeia_base(session)

        rascunho = _criar_compra(session, cadeia)
        homologada = repo.save(
            Compra(
                processo_documental_id=cadeia["processo"].id,
                fornecedor_id=cadeia["fornecedor"].id,
                unidade_id=cadeia["unidade_id"],
                numero="002/2026",
                data=date(2026, 2, 1),
                valor_total=Decimal("500.00"),
                situacao=SituacaoCompra.HOMOLOGADO,
            )
        )

        homologadas = repo.list(situacao=SituacaoCompra.HOMOLOGADO)

        assert homologada.id in {c.id for c in homologadas}
        assert rascunho.id not in {c.id for c in homologadas}
        assert rascunho.id in {c.id for c in repo.list()}

    def test_update_reflete_dados_alterados(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        compra = _criar_compra(session)

        compra.numero = "999/2026"
        atualizada = repo.update(compra)

        assert atualizada.numero == "999/2026"
        assert repo.get_by_id(compra.id).numero == "999/2026"

    def test_delete_marca_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        compra = _criar_compra(session)

        repo.delete(compra.id, uuid4())

        assert repo.get_by_id(compra.id).foi_excluido() is True
        assert compra.id not in {c.id for c in repo.list()}
        assert compra.id in {c.id for c in repo.list(include_deleted=True)}

    def test_exists_processo_documental(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        cadeia = _criar_cadeia_base(session)

        assert repo.exists_processo_documental(cadeia["processo"].id) is True
        assert repo.exists_processo_documental(uuid4()) is False

    def test_exists_fornecedor_ativo(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        cadeia = _criar_cadeia_base(session)

        assert repo.exists_fornecedor_ativo(cadeia["fornecedor"].id) is True
        assert repo.exists_fornecedor_ativo(uuid4()) is False

    def test_exists_unidade(self, session: Session) -> None:
        repo = SqlAlchemyCompraRepository(session)
        cadeia = _criar_cadeia_base(session)

        assert repo.exists_unidade(cadeia["unidade_id"]) is True
        assert repo.exists_unidade(uuid4()) is False


# -- Contrato -------------------------------------------------------------------


def _criar_contrato(
    session: Session, cadeia: dict | None = None, numero: str | None = None
) -> Contrato:
    cadeia = cadeia or _criar_cadeia_base(session)
    return SqlAlchemyContratoRepository(session).save(
        Contrato(
            processo_documental_id=cadeia["processo"].id,
            fornecedor_id=cadeia["fornecedor"].id,
            unidade_id=cadeia["unidade_id"],
            numero=numero or f"CT-{uuid4().hex[:6].upper()}",
            data_inicio=date(2026, 2, 1),
            data_fim=date(2026, 12, 31),
            valor=Decimal("1234.56"),
            objeto="Contrato de teste",
        )
    )


class TestSqlAlchemyContratoRepository:
    def test_save_e_get_by_id_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        contrato = _criar_contrato(session)

        assert contrato.id is not None
        assert contrato.situacao == SituacaoContrato.EM_ELABORACAO
        assert contrato.created_at is not None

        obtido = repo.get_by_id(contrato.id)
        assert obtido is not None
        assert obtido.numero == contrato.numero
        assert obtido.valor == Decimal("1234.56")

    def test_get_by_id_inexistente_retorna_none(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)

        assert repo.get_by_id(uuid4()) is None

    def test_list_filtra_por_situacao_e_fornecedor(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        cadeia_a = _criar_cadeia_base(session)
        _criar_contrato(session, cadeia_a)  # EM_ELABORACAO

        # Contrato assinado, mesmo fornecedor da cadeia_a.
        assinado = repo.save(
            Contrato(
                processo_documental_id=cadeia_a["processo"].id,
                fornecedor_id=cadeia_a["fornecedor"].id,
                unidade_id=cadeia_a["unidade_id"],
                numero=f"CT-{uuid4().hex[:6].upper()}",
                data_inicio=date(2026, 2, 1),
                situacao=SituacaoContrato.ASSINADO,
            )
        )

        assinados = repo.list(situacao=SituacaoContrato.ASSINADO)
        do_fornecedor = repo.list(fornecedor_id=cadeia_a["fornecedor"].id)

        assert assinado.id in {c.id for c in assinados}
        assert assinado.id in {c.id for c in do_fornecedor}

    def test_update_reflete_dados_alterados(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        contrato = _criar_contrato(session)

        contrato.objeto = "Objeto atualizado"
        atualizado = repo.update(contrato)

        assert atualizado.objeto == "Objeto atualizado"
        assert repo.get_by_id(contrato.id).objeto == "Objeto atualizado"

    def test_delete_marca_soft_delete(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        contrato = _criar_contrato(session)

        repo.delete(contrato.id, uuid4())

        assert repo.get_by_id(contrato.id).foi_excluido() is True
        assert contrato.id not in {c.id for c in repo.list()}
        assert contrato.id in {c.id for c in repo.list(include_deleted=True)}

    def test_exists_compra(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        compra = _criar_compra(session)

        assert repo.exists_compra(compra.id) is True
        assert repo.exists_compra(uuid4()) is False

    def test_exists_numero(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        contrato = _criar_contrato(session)
        numero_inexistente = f"ZZ-{uuid4().hex[:10].upper()}"

        assert repo.exists_numero(contrato.numero) is True
        assert repo.exists_numero(numero_inexistente) is False
        # Atualização do próprio registro não é falso positivo.
        assert repo.exists_numero(contrato.numero, excluir_id=contrato.id) is False

    def test_verificacoes_de_vinculo(self, session: Session) -> None:
        repo = SqlAlchemyContratoRepository(session)
        cadeia = _criar_cadeia_base(session)

        assert repo.exists_processo_documental(cadeia["processo"].id) is True
        assert repo.exists_fornecedor_ativo(cadeia["fornecedor"].id) is True
        assert repo.exists_unidade(cadeia["unidade_id"]) is True
        assert repo.exists_processo_documental(uuid4()) is False


# -- Trilha de Auditoria --------------------------------------------------------


class TestSqlAlchemyTrilhaAuditoriaRepository:
    def _registrar(
        self,
        repo: SqlAlchemyTrilhaAuditoriaRepository,
        tipo_evento: str,
        *,
        categoria: CategoriaEventoAuditoria = CategoriaEventoAuditoria.ALTERACAO,
        recurso_id: UUID | None = None,
        ator_id: UUID | None = None,
    ) -> RegistroAuditoria:
        return repo.registrar(
            RegistroAuditoria(
                categoria=categoria,
                tipo_evento=tipo_evento,
                operacao="op",
                recurso_tipo="Contrato",
                recurso_id=recurso_id,
                ator_id=ator_id,
                origem="teste-integracao",
            )
        )

    def test_registrar_e_list_roundtrip(self, session: Session) -> None:
        repo = SqlAlchemyTrilhaAuditoriaRepository(session)
        recurso_id = uuid4()

        salvo = self._registrar(repo, "ContratoCriado", recurso_id=recurso_id)

        assert salvo.id is not None
        assert salvo.created_at is not None

        eventos = repo.list(recurso_id=recurso_id)
        assert len(eventos) == 1
        assert eventos[0].id == salvo.id
        assert eventos[0].categoria == CategoriaEventoAuditoria.ALTERACAO
        assert eventos[0].resultado == ResultadoEventoAuditoria.SUCESSO

    def test_list_filtra_e_pagina(self, session: Session) -> None:
        repo = SqlAlchemyTrilhaAuditoriaRepository(session)
        ator = uuid4()
        recurso = uuid4()

        for i in range(3):
            self._registrar(
                repo,
                f"Evento{i}",
                categoria=(
                    CategoriaEventoAuditoria.CRIACAO
                    if i < 2
                    else CategoriaEventoAuditoria.EXCLUSAO
                ),
                recurso_id=recurso,
                ator_id=ator if i < 2 else None,
            )

        todos = repo.list(recurso_id=recurso)
        por_categoria = repo.list(recurso_id=recurso, categoria=CategoriaEventoAuditoria.CRIACAO)
        por_usuario = repo.list(recurso_id=recurso, usuario_id=ator)
        pagina = repo.list(recurso_id=recurso, limit=2)

        assert len(todos) == 3
        assert len(por_categoria) == 2
        assert len(por_usuario) == 2
        assert len(pagina) == 2

    def test_count(self, session: Session) -> None:
        repo = SqlAlchemyTrilhaAuditoriaRepository(session)
        ator = uuid4()
        recurso = uuid4()

        self._registrar(repo, "E1", recurso_id=recurso, ator_id=ator)
        self._registrar(repo, "E2", recurso_id=recurso, ator_id=ator)
        self._registrar(repo, "E3", recurso_id=recurso)

        assert repo.count(recurso_id=recurso) == 3
        assert repo.count(recurso_id=recurso, usuario_id=ator) == 2
        assert repo.count(recurso_id=recurso, categoria=CategoriaEventoAuditoria.ALTERACAO) == 3
        assert repo.count(recurso_id=uuid4()) == 0

    def test_ordena_por_ocorrido_em_desc(self, session: Session) -> None:
        repo = SqlAlchemyTrilhaAuditoriaRepository(session)
        recurso = uuid4()

        self._registrar(repo, "Primeiro", recurso_id=recurso)
        self._registrar(repo, "Segundo", recurso_id=recurso)

        eventos = repo.list(recurso_id=recurso)

        assert [e.tipo_evento for e in eventos] == ["Segundo", "Primeiro"]
