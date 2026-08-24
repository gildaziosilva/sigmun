"""Testes unitários da entidade Fornecedor (ENT-COMPRAS-007)."""

from uuid import uuid4

import pytest

from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor, SituacaoFornecedor


def test_criar_fornecedor_com_valores_padrao():
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())

    assert fornecedor.id is not None
    assert fornecedor.pessoa_juridica_id is not None
    assert fornecedor.situacao_cadastro == SituacaoFornecedor.ATIVO
    assert fornecedor.macro_categoria is None
    assert fornecedor.created_at is not None
    assert not fornecedor.foi_excluido()


def test_inativar_altera_situacao_e_registra_usuario():
    usuario = uuid4()
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())

    fornecedor.inativar(usuario)

    assert fornecedor.situacao_cadastro == SituacaoFornecedor.INATIVO
    assert fornecedor.updated_by == usuario


def test_ativar_reativa_fornecedor():
    usuario = uuid4()
    fornecedor = Fornecedor(
        pessoa_juridica_id=uuid4(), situacao_cadastro=SituacaoFornecedor.INATIVO
    )

    fornecedor.ativar(usuario)

    assert fornecedor.situacao_cadastro == SituacaoFornecedor.ATIVO
    assert fornecedor.esta_ativo() is True


def test_suspender_altera_situacao():
    usuario = uuid4()
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())

    fornecedor.suspender(usuario)

    assert fornecedor.situacao_cadastro == SituacaoFornecedor.SUSPENSO
    assert fornecedor.esta_ativo() is False


def test_atualizar_situacao_invalida_lanca_erro():
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())

    with pytest.raises(ValueError):
        fornecedor.atualizar_situacao("BANANA", uuid4())  # type: ignore[arg-type]


def test_atualizar_categoria_registra_alteracao():
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())
    antes = fornecedor.updated_at

    fornecedor.atualizar_categoria("SAUDE")

    assert fornecedor.macro_categoria == "SAUDE"
    assert fornecedor.updated_at >= antes


def test_excluir_marca_soft_delete():
    usuario = uuid4()
    fornecedor = Fornecedor(pessoa_juridica_id=uuid4())

    fornecedor.excluir(usuario)

    assert fornecedor.foi_excluido() is True
    assert fornecedor.deleted_by == usuario
