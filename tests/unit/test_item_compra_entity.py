"""Testes unitários da entidade ItemCompra (ENT-COMPRAS-004)."""

from decimal import Decimal
from uuid import uuid4

import pytest

from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra


def _criar_item(**overrides) -> ItemCompra:
    dados = {
        "compra_id": uuid4(),
        "descricao": "Notebook Dell i5 16GB RAM",
        "quantidade": Decimal("3"),
        "valor_unitario": Decimal("4500.00"),
    }
    dados.update(overrides)
    return ItemCompra(**dados)


def test_criar_item_calcula_valor_total():
    item = _criar_item()

    assert item.valor_total == Decimal("13500.00")
    assert item.id is not None
    assert not item.foi_excluido()


def test_criar_item_sem_compra_lanca_erro():
    with pytest.raises(ValueError):
        ItemCompra(compra_id=None, descricao="X", quantidade=Decimal("1"))  # type: ignore[arg-type]


def test_descricao_vazia_lanca_erro_rn011():
    with pytest.raises(ValueError, match="RN-COMPRAS-011"):
        _criar_item(descricao="   ")


def test_quantidade_zero_ou_negativa_lanca_erro_rn012():
    with pytest.raises(ValueError, match="RN-COMPRAS-012"):
        _criar_item(quantidade=Decimal("0"))
    with pytest.raises(ValueError, match="RN-COMPRAS-012"):
        _criar_item(quantidade=Decimal("-2"))


def test_valor_unitario_negativo_lanca_erro():
    with pytest.raises(ValueError):
        _criar_item(valor_unitario=Decimal("-1.00"))


def test_atualizar_dados_recalcula_total_e_registra_usuario():
    usuario = uuid4()
    item = _criar_item()

    item.atualizar_dados(
        quantidade=Decimal("10"),
        valor_unitario=Decimal("199.90"),
        usuario_id=usuario,
    )

    assert item.quantidade == Decimal("10")
    assert item.valor_unitario == Decimal("199.90")
    assert item.valor_total == Decimal("1999.00")
    assert item.updated_by == usuario


def test_atualizar_apenas_descricao_mantem_total():
    item = _criar_item()
    total_original = item.valor_total

    item.atualizar_dados(descricao="  Notebook Dell i7 32GB  ")

    assert item.descricao == "Notebook Dell i7 32GB"
    assert item.valor_total == total_original


def test_excluir_marca_soft_delete():
    usuario = uuid4()
    item = _criar_item()

    item.excluir(usuario)

    assert item.foi_excluido() is True
    assert item.deleted_by == usuario


def test_pertence_a_verifica_vinculo():
    compra_id = uuid4()
    item = _criar_item(compra_id=compra_id)

    assert item.pertence_a(compra_id) is True
    assert item.pertence_a(uuid4()) is False
