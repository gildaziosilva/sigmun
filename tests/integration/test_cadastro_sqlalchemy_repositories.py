"""Testes de integração dos repositórios SQLAlchemy do DOM-CUM.

Exercitam as implementações concretas dos repositórios de Pessoas e
Unidades Administrativas (módulo ``sigmun_cadastro``) contra o PostgreSQL
local (docker compose), validando o ciclo completo do agregado
(extensão 1:1, endereços, documentos, contatos), soft-delete em cascata,
filtros, paginação, hierarquia e unicidades.

Isolamento: cada teste executa dentro de uma transação revertida
(rollback) ao final, sem deixar dados persistentes no banco.

Dependência: PostgreSQL acessível em ``settings.DATABASE_URL`` com a
migração ``20260831_02`` aplicada.
"""

from __future__ import annotations

from uuid import uuid4

import pytest
from sqlalchemy import event as sa_event, text
from sqlalchemy.orm import Session

from src.core.infrastructure.database.session import engine
from src.modules.sigmun_cadastro.domain.entities.contato import TipoContato
from src.modules.sigmun_cadastro.domain.entities.documento import TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.endereco import TipoEndereco
from src.modules.sigmun_cadastro.domain.entities.pessoa import (
    CategoriaPessoa,
    DadosFisicos,
    DadosJuridicos,
    Pessoa,
    TipoPessoa,
)
from src.modules.sigmun_cadastro.domain.entities.unidade_administrativa import (
    UnidadeAdministrativa,
)
from src.modules.sigmun_cadastro.domain.exceptions import CicloHierarquiaError
from src.modules.sigmun_cadastro.infrastructure.repositories import (
    SqlAlchemyPessoaRepository,
    SqlAlchemyUnidadeAdministrativaRepository,
)

CPF_VALIDO = "529.982.247-25"  # dígito verificador válido (RN-CUM-002)
CNPJ_VALIDO = "11.222.333/0001-81"  # dígito verificador válido (RN-CUM-003)


# -- Fixtures --------------------------------------------------------------------


@pytest.fixture
def session() -> Session:
    """Sessão com savepoint revertido ao final de cada teste.

    Usa nested transaction (SAVEPOINT) para garantir isolamento:
    cada teste executa em um savepoint que é revertido ao final,
    independentemente de commits feitos pelo repositório.
    """
    connection = engine.connect()
    transaction = connection.begin()

    # Limpa dados residuais de testes anteriores (garantir isolamento)
    # TRUNCATE CASCADE remove dados de todas as tabelas com FK para estas
    connection.execute(
        text(
            "TRUNCATE TABLE core.contatos, core.documentos, core.enderecos, "
            "core.pessoas_fisicas, core.pessoas_juridicas, core.pessoas, "
            "core.unidades_administrativas, core.fornecedores "
            "RESTART IDENTITY CASCADE"
        )
    )

    session = Session(bind=connection, expire_on_commit=False)
    nested = connection.begin_nested()

    @sa_event.listens_for(session, "after_transaction_end")
    def end_savepoint(session: Session, trans: object) -> None:
        """Reabre o savepoint após cada commit/rollback do teste."""
        nonlocal nested
        if trans.nested and not trans._parent.nested:  # type: ignore[attr-defined]
            nested = connection.begin_nested()

    try:
        yield session
    finally:
        sa_event.remove(session, "after_transaction_end", end_savepoint)
        transaction.rollback()
        session.close()
        connection.close()


@pytest.fixture
def pessoa_repo(session: Session) -> SqlAlchemyPessoaRepository:
    return SqlAlchemyPessoaRepository(session)


@pytest.fixture
def unidade_repo(session: Session) -> SqlAlchemyUnidadeAdministrativaRepository:
    return SqlAlchemyUnidadeAdministrativaRepository(session)


# -- Helpers -----------------------------------------------------------------------


def _pessoa_fisica(**kwargs) -> Pessoa:
    pessoa = Pessoa(
        tipo=TipoPessoa.FISICA,
        categoria=CategoriaPessoa.CIDADAO,
        dados_fisicos=DadosFisicos(nome="Maria de Souza"),
        **kwargs,
    )
    pessoa.adicionar_endereco(
        TipoEndereco.RESIDENCIAL,
        "Rua das Flores",
        "123",
        principal=True,
        bairro="Centro",
        cep="69900-000",
        cidade="Rio Branco",
        estado="AC",
    )
    pessoa.adicionar_documento(TipoDocumento.CPF, CPF_VALIDO, principal=True)
    pessoa.adicionar_contato(TipoContato.EMAIL, "maria@example.com", principal=True)
    return pessoa


def _pessoa_juridica(**kwargs) -> Pessoa:
    pessoa = Pessoa(
        tipo=TipoPessoa.JURIDICA,
        categoria=CategoriaPessoa.FORNECEDOR,
        dados_juridicos=DadosJuridicos(razao_social="Empresa Exemplo LTDA"),
        **kwargs,
    )
    pessoa.adicionar_documento(TipoDocumento.CNPJ, CNPJ_VALIDO, principal=True)
    return pessoa


# -- SqlAlchemyPessoaRepository ------------------------------------------------------


class TestSqlAlchemyPessoaRepository:
    def test_save_e_get_by_id_roundtrip_pf(self, pessoa_repo):
        pessoa = _pessoa_fisica()

        salvo = pessoa_repo.save(pessoa)
        carregado = pessoa_repo.get_by_id(salvo.id)

        assert carregado is not None
        assert carregado.id == salvo.id
        assert carregado.tipo is TipoPessoa.FISICA
        assert carregado.categoria is CategoriaPessoa.CIDADAO
        assert carregado.nome_identificacao == "Maria de Souza"
        # Agregado hidratado: endereço, documento e contato
        assert len(carregado.enderecos) == 1
        endereco = carregado.enderecos[0]
        assert endereco.tipo is TipoEndereco.RESIDENCIAL
        assert endereco.logradouro == "Rua das Flores"
        assert endereco.principal is True
        assert endereco.esta_vigente()
        assert len(carregado.documentos) == 1
        assert carregado.documentos[0].numero == "52998224725"
        assert carregado.documento_principal(TipoDocumento.CPF) is not None
        assert len(carregado.contatos) == 1
        assert carregado.contatos[0].valor == "maria@example.com"

    def test_save_e_get_by_id_roundtrip_pj(self, pessoa_repo):
        pessoa = _pessoa_juridica()

        salvo = pessoa_repo.save(pessoa)
        carregado = pessoa_repo.get_by_id(salvo.id)

        assert carregado is not None
        assert carregado.tipo is TipoPessoa.JURIDICA
        assert carregado.dados_fisicos is None
        assert carregado.nome_identificacao == "Empresa Exemplo LTDA"
        assert carregado.documentos[0].numero == "11222333000181"
        assert carregado.enderecos == []

    def test_update_extensao_e_subrecursos(self, pessoa_repo):
        pessoa = _pessoa_fisica()
        pessoa_repo.save(pessoa)

        # Altera extensão e endereço existente, adiciona novo contato
        pessoa.atualizar_dados_fisicos(nome="Maria S. de Souza")
        pessoa.enderecos[0].bairro = "Bosque"
        pessoa.adicionar_contato(TipoContato.TELEFONE, "(68) 99999-0000")
        pessoa_repo.save(pessoa)

        carregado = pessoa_repo.get_by_id(pessoa.id)
        assert carregado.nome_identificacao == "Maria S. de Souza"
        assert carregado.enderecos[0].bairro == "Bosque"
        assert len(carregado.contatos) == 2

    def test_lista_com_filtros_e_paginacao(self, pessoa_repo):
        pessoa_repo.save(_pessoa_fisica())
        pessoa_repo.save(_pessoa_juridica())
        pessoa_repo.save(_pessoa_juridica())

        assert len(pessoa_repo.list()) == 3

        fisicas = pessoa_repo.list(tipo=TipoPessoa.FISICA)
        assert len(fisicas) == 1
        assert fisicas[0].nome_identificacao == "Maria de Souza"

        cidadaos = pessoa_repo.list(categoria=CategoriaPessoa.CIDADAO)
        assert len(cidadaos) == 1

        assert len(pessoa_repo.list(limit=2)) == 2
        assert len(pessoa_repo.list(limit=2, offset=2)) == 1

    def test_delete_cascade_soft_delete(self, pessoa_repo, session):
        pessoa = _pessoa_fisica()
        pessoa_repo.save(pessoa)
        usuario = uuid4()

        pessoa_repo.delete(pessoa.id, usuario)

        # Raiz não aparece mais por padrão; com include_deleted, excluída
        assert pessoa_repo.get_by_id(pessoa.id) is None
        excluida = pessoa_repo.get_by_id(pessoa.id, include_deleted=True)
        assert excluida is not None
        assert excluida.foi_excluido()
        # Filhos marcados como excluídos no banco (RN-CUM-007)
        for tabela in ("enderecos", "documentos", "contatos", "pessoas_fisicas"):
            total = session.execute(
                text(
                    f"SELECT count(*) FROM core.{tabela} "
                    "WHERE pessoa_id = :pid AND deleted_at IS NOT NULL"
                ),
                {"pid": pessoa.id},
            ).scalar_one()
            assert total >= 1, f"{tabela} deveria estar marcado como excluído"

    def test_delete_idempotente_para_inexistente(self, pessoa_repo):
        pessoa_repo.delete(uuid4(), uuid4())  # não levanta

    def test_exists_documento(self, pessoa_repo):
        pessoa = _pessoa_fisica()
        pessoa_repo.save(pessoa)

        assert pessoa_repo.exists_documento(TipoDocumento.CPF, "52998224725")
        assert pessoa_repo.exists_documento(TipoDocumento.CPF, CPF_VALIDO)
        assert not pessoa_repo.exists_documento(TipoDocumento.CPF, "11144477735")
        assert not pessoa_repo.exists_documento(TipoDocumento.RG, "52998224725")

    def test_exists_documento_ignora_excluidos(self, pessoa_repo):
        pessoa = _pessoa_fisica()
        pessoa_repo.save(pessoa)
        pessoa_repo.delete(pessoa.id, uuid4())

        assert not pessoa_repo.exists_documento(TipoDocumento.CPF, "52998224725")


# -- SqlAlchemyUnidadeAdministrativaRepository -----------------------------------------


class TestSqlAlchemyUnidadeAdministrativaRepository:
    def test_save_e_get_by_id_roundtrip(self, unidade_repo):
        unidade = UnidadeAdministrativa(
            nome="Secretaria Municipal de Saúde",
            sigla=f"SMS{uuid4().hex[:4].upper()}",
            codigo_ibge=f"{uuid4().int % 9999999:07d}",
            codigo_siafi=f"SIAFI{uuid4().hex[:6].upper()}",
        )

        salvo = unidade_repo.save(unidade)
        carregado = unidade_repo.get_by_id(salvo.id)

        assert carregado is not None
        assert carregado.id == salvo.id
        assert carregado.nome == "Secretaria Municipal de Saúde"
        assert carregado.sigla == unidade.sigla
        assert carregado.codigo_ibge == unidade.codigo_ibge
        assert carregado.codigo_siafi == unidade.codigo_siafi
        assert carregado.unidade_pai_id is None
        assert not carregado.foi_excluido()

    def test_update_campos(self, unidade_repo):
        unidade = UnidadeAdministrativa(nome="Setor de Compras")
        unidade_repo.save(unidade)

        unidade.atualizar(nome="Departamento de Compras", sigla=f"DC{uuid4().hex[:3].upper()}")
        salvo = unidade_repo.save(unidade)

        carregado = unidade_repo.get_by_id(unidade.id)
        assert carregado.nome == "Departamento de Compras"
        assert carregado.sigla == salvo.sigla

    def test_lista_com_paginacao(self, unidade_repo):
        for i in range(3):
            unidade_repo.save(UnidadeAdministrativa(nome=f"Unidade Teste {i} {uuid4().hex[:6]}"))

        todas = unidade_repo.list()
        assert len(todas) >= 3
        assert len(unidade_repo.list(limit=2)) == 2

    def test_hierarquia_e_ancestrais(self, unidade_repo):
        avo = unidade_repo.save(UnidadeAdministrativa(nome="Gabinete do Prefeito"))
        pai = unidade_repo.save(
            UnidadeAdministrativa(nome="Secretaria de Administração", unidade_pai_id=avo.id)
        )
        filho = unidade_repo.save(
            UnidadeAdministrativa(nome="Setor de Compras", unidade_pai_id=pai.id)
        )

        ancestrais = unidade_repo.get_ancestral_ids(filho.id)
        assert set(ancestrais) == {pai.id, avo.id}
        assert len(ancestrais) == 2
        assert unidade_repo.get_ancestral_ids(avo.id) == []

    def test_save_rejeita_ciclo(self, unidade_repo):
        pai = unidade_repo.save(UnidadeAdministrativa(nome="Secretaria A"))
        filho = unidade_repo.save(
            UnidadeAdministrativa(nome="Departamento B", unidade_pai_id=pai.id)
        )

        # Tornar a "Secretaria A" filha do próprio "Departamento B" cria ciclo
        pai.unidade_pai_id = filho.id
        with pytest.raises(CicloHierarquiaError):
            unidade_repo.save(pai)

    def test_save_rejeita_auto_paternidade(self, unidade_repo):
        unidade = UnidadeAdministrativa(nome="Unidade Órfã")
        unidade.unidade_pai_id = unidade.id
        with pytest.raises(CicloHierarquiaError):
            unidade_repo.save(unidade)

    def test_delete_soft_delete(self, unidade_repo):
        unidade = unidade_repo.save(UnidadeAdministrativa(nome="Setor Extinto"))

        unidade_repo.delete(unidade.id, uuid4())

        assert unidade_repo.get_by_id(unidade.id) is None
        excluida = unidade_repo.get_by_id(unidade.id, include_deleted=True)
        assert excluida is not None
        assert excluida.foi_excluido()

    def test_tem_filhas_ativas(self, unidade_repo):
        pai = unidade_repo.save(UnidadeAdministrativa(nome="Secretaria Mãe"))
        filho = unidade_repo.save(
            UnidadeAdministrativa(nome="Departamento Filho", unidade_pai_id=pai.id)
        )

        assert unidade_repo.tem_filhas_ativas(pai.id)
        unidade_repo.delete(filho.id, uuid4())
        assert not unidade_repo.tem_filhas_ativas(pai.id)

    def test_exists_sigla_com_exclude(self, unidade_repo):
        sigla = f"UNI{uuid4().hex[:4].upper()}"
        unidade = unidade_repo.save(UnidadeAdministrativa(nome="Unidade Sigla", sigla=sigla))

        assert unidade_repo.exists_sigla(sigla)
        assert not unidade_repo.exists_sigla(sigla, exclude_id=unidade.id)
        assert not unidade_repo.exists_sigla(f"OUTRA{uuid4().hex[:4].upper()}")

    def test_exists_sigla_inclui_excluidos(self, unidade_repo):
        """RN-CUM-009: a unicidade considera também registros excluídos."""
        sigla = f"EXT{uuid4().hex[:4].upper()}"
        unidade = unidade_repo.save(UnidadeAdministrativa(nome="Unidade Extinta", sigla=sigla))
        unidade_repo.delete(unidade.id, uuid4())

        assert unidade_repo.exists_sigla(sigla)
        assert not unidade_repo.tem_filhas_ativas(unidade.id)

    def test_exists_codigos_ibge_e_siafi(self, unidade_repo):
        ibge = f"{uuid4().int % 9999999:07d}"
        siafi = f"SIAFI{uuid4().hex[:6].upper()}"
        unidade = unidade_repo.save(
            UnidadeAdministrativa(nome="Unidade Códigos", codigo_ibge=ibge, codigo_siafi=siafi)
        )

        assert unidade_repo.exists_codigo_ibge(ibge)
        assert not unidade_repo.exists_codigo_ibge(ibge, exclude_id=unidade.id)
        assert unidade_repo.exists_codigo_siafi(siafi)
        assert not unidade_repo.exists_codigo_siafi(siafi, exclude_id=unidade.id)
