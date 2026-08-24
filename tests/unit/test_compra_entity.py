"""Testes unitários da entidade Compra (processo de compras)."""

from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from src.modules.sigmun_compras.domain.entities.compra import (
    TRANSICOES_VALIDAS,
    Compra,
    SituacaoCompra,
)


def _criar_compra(**overrides) -> Compra:
    dados = {
        "processo_documental_id": uuid4(),
        "fornecedor_id": uuid4(),
        "unidade_id": uuid4(),
        "numero": "001/2026",
        "valor_total": Decimal("1500.00"),
    }
    dados.update(overrides)
    return Compra(**dados)


def test_criar_compra_com_valores_padrao():
    compra = _criar_compra()

    assert compra.id is not None
    assert compra.situacao == SituacaoCompra.RASCUNHO
    assert compra.data == date.today()
    assert not compra.foi_excluido()
    assert not compra.esta_cancelada()


def test_criar_sem_processo_documental_lanca_erro_rn025():
    with pytest.raises(ValueError, match="RN-COMPRAS-025"):
        _criar_compra(processo_documental_id=None)  # type: ignore[arg-type]


def test_criar_sem_fornecedor_ou_unidade_lanca_erro():
    with pytest.raises(ValueError):
        _criar_compra(fornecedor_id=None)  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        _criar_compra(unidade_id=None)  # type: ignore[arg-type]


def test_numero_vazio_lanca_erro():
    with pytest.raises(ValueError, match="numero"):
        _criar_compra(numero="   ")


def test_valor_total_negativo_lanca_erro():
    with pytest.raises(ValueError, match="negativo"):
        _criar_compra(valor_total=Decimal("-1.00"))


def test_transicoes_validas_do_rascunho():
    assert SituacaoCompra.EM_INSTRUCAO in TRANSICOES_VALIDAS[SituacaoCompra.RASCUNHO]
    assert SituacaoCompra.CANCELADO in TRANSICOES_VALIDAS[SituacaoCompra.RASCUNHO]
    assert SituacaoCompra.HOMOLOGADO not in TRANSICOES_VALIDAS[SituacaoCompra.RASCUNHO]


def test_transicao_valida_avanca_situacao_e_registra_usuario():
    usuario = uuid4()
    compra = _criar_compra()

    compra.alterar_situacao(SituacaoCompra.EM_INSTRUCAO, usuario)

    assert compra.situacao == SituacaoCompra.EM_INSTRUCAO
    assert compra.updated_by == usuario


def test_transicao_invalida_lanca_erro_rn026():
    compra = _criar_compra()  # RASCUNHO

    with pytest.raises(ValueError, match="RN-COMPRAS-026"):
        compra.alterar_situacao(SituacaoCompra.HOMOLOGADO, uuid4())


def test_mesma_situacao_nao_altera_nada():
    compra = _criar_compra()
    antes = compra.updated_at

    compra.alterar_situacao(SituacaoCompra.RASCUNHO, uuid4())

    assert compra.updated_at == antes


def test_estado_terminal_arquivado_nao_permite_transicao():
    compra = _criar_compra(situacao=SituacaoCompra.ARQUIVADO)

    assert TRANSICOES_VALIDAS[SituacaoCompra.ARQUIVADO] == set()
    with pytest.raises(ValueError):
        compra.alterar_situacao(SituacaoCompra.EM_INSTRUCAO, uuid4())


def test_fluxo_completo_ate_encerrado():
    compra = _criar_compra()
    usuario = uuid4()
    caminho = [
        SituacaoCompra.EM_INSTRUCAO,
        SituacaoCompra.EM_ANALISE,
        SituacaoCompra.EM_PROCEDIMENTO,
        SituacaoCompra.EM_JULGAMENTO,
        SituacaoCompra.HOMOLOGADO,
        SituacaoCompra.CONTRATADO,
        SituacaoCompra.ENCERRADO,
    ]

    for situacao in caminho:
        compra.alterar_situacao(situacao, usuario)

    assert compra.situacao == SituacaoCompra.ENCERRADO


def test_atualizar_dados_registra_usuario():
    usuario = uuid4()
    compra = _criar_compra()
    nova_data = date(2026, 1, 15)

    compra.atualizar_dados(
        numero="002/2026", data=nova_data, valor_total=Decimal("99.90"), usuario_id=usuario
    )

    assert compra.numero == "002/2026"
    assert compra.data == nova_data
    assert compra.valor_total == Decimal("99.90")
    assert compra.updated_by == usuario


def test_excluir_marca_soft_delete():
    usuario = uuid4()
    compra = _criar_compra()

    compra.excluir(usuario)

    assert compra.foi_excluido() is True
    assert compra.deleted_by == usuario


def test_cancelada_inclui_cancelado_e_arquivado():
    assert _criar_compra(situacao=SituacaoCompra.CANCELADO).esta_cancelada()
    assert _criar_compra(situacao=SituacaoCompra.ARQUIVADO).esta_cancelada()
    assert not _criar_compra().esta_cancelada()
