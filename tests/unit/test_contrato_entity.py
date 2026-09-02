"""Testes unitários da entidade Contrato.

Valida as regras de negócio RN-COMPRAS-036 a 039 e as transições de
situação definidas em 013-Modelo-de-Dados (seção 30).
"""

from datetime import date, datetime

from src.shared.compat import UTC
from decimal import Decimal
from uuid import uuid4

import pytest

from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)


def _criar_contrato(**overrides) -> Contrato:
    dados = {
        "processo_documental_id": uuid4(),
        "fornecedor_id": uuid4(),
        "unidade_id": uuid4(),
        "numero": "001/2026",
        "data_inicio": date(2026, 1, 1),
        "data_fim": date(2026, 12, 31),
        "valor": Decimal("10000.00"),
        "objeto": "Aquisição de serviços de limpeza",
    }
    dados.update(overrides)
    return Contrato(**dados)


def test_criar_contrato_com_valores_padrao():
    processo = uuid4()
    fornecedor = uuid4()
    unidade = uuid4()

    contrato = Contrato(
        processo_documental_id=processo,
        fornecedor_id=fornecedor,
        unidade_id=unidade,
        numero="001",
    )

    assert contrato.id is not None
    assert contrato.processo_documental_id == processo
    assert contrato.fornecedor_id == fornecedor
    assert contrato.unidade_id == unidade
    assert contrato.numero == "001"
    assert contrato.situacao == SituacaoContrato.EM_ELABORACAO
    assert contrato.licitacao_master_id is None
    assert contrato.objeto is None
    assert contrato.valor is None
    assert contrato.data_inicio is not None
    assert contrato.created_at is not None
    assert contrato.updated_at is not None
    assert not contrato.foi_excluido()


def test_processo_documental_id_obrigatorio():
    with pytest.raises(ValueError, match="processo_documental_id"):
        Contrato(
            processo_documental_id=None,  # type: ignore[arg-type]
            fornecedor_id=uuid4(),
            unidade_id=uuid4(),
            numero="001",
        )


def test_fornecedor_id_obrigatorio():
    with pytest.raises(ValueError, match="fornecedor_id"):
        Contrato(
            processo_documental_id=uuid4(),
            fornecedor_id=None,  # type: ignore[arg-type]
            unidade_id=uuid4(),
            numero="001",
        )


def test_unidade_id_obrigatorio():
    with pytest.raises(ValueError, match="unidade_id"):
        Contrato(
            processo_documental_id=uuid4(),
            fornecedor_id=uuid4(),
            unidade_id=None,  # type: ignore[arg-type]
            numero="001",
        )


@pytest.mark.parametrize("numero", ["", "   ", None])
def test_numero_invalido_lanca_erro(numero):
    with pytest.raises(ValueError, match="numero"):
        _criar_contrato(numero=numero)  # type: ignore[arg-type]


def test_numero_eh_normalizado():
    contrato = _criar_contrato(numero="  002/2026  ")
    assert contrato.numero == "002/2026"


@pytest.mark.parametrize("valor", [Decimal("-0.01"), Decimal("-100.00")])
def test_valor_negativo_lanca_erro(valor):
    with pytest.raises(ValueError, match="negativo"):
        _criar_contrato(valor=valor)


def test_valor_zero_ok():
    contrato = _criar_contrato(valor=Decimal("0.00"))
    assert contrato.valor == Decimal("0.00")


def test_valor_positivo_ok():
    contrato = _criar_contrato(valor=Decimal("50000.50"))
    assert contrato.valor == Decimal("50000.50")


def test_vigencia_data_fim_anterior_lanca_erro():
    with pytest.raises(ValueError, match="RN-COMPRAS-037"):
        _criar_contrato(data_inicio=date(2026, 6, 1), data_fim=date(2026, 1, 1))


def test_vigencia_data_fim_igual_data_inicio_ok():
    contrato = _criar_contrato(data_inicio=date(2026, 1, 1), data_fim=date(2026, 1, 1))
    assert contrato.data_fim == contrato.data_inicio


def test_situacao_invalida_lanca_erro():
    with pytest.raises(ValueError, match="Situação inválida"):
        Contrato(
            processo_documental_id=uuid4(),
            fornecedor_id=uuid4(),
            unidade_id=uuid4(),
            numero="001",
            situacao="INVALIDA",  # type: ignore[arg-type]
        )


# -- Transições de situação --------------------------------------------------------


def test_transicao_valida_em_elaboracao_para_assinado():
    contrato = _criar_contrato()
    assert contrato.pode_transicionar_para(SituacaoContrato.ASSINADO)
    contrato.alterar_situacao(SituacaoContrato.ASSINADO, uuid4())
    assert contrato.situacao == SituacaoContrato.ASSINADO


def test_transicao_invalida_em_elaboracao_para_vigente_lanca_erro():
    contrato = _criar_contrato()
    with pytest.raises(ValueError, match="não permitida"):
        contrato.alterar_situacao(SituacaoContrato.VIGENTE, uuid4())


def test_transicao_para_mesma_situacao_eh_noop():
    contrato = _criar_contrato()
    contrato.alterar_situacao(SituacaoContrato.EM_ELABORACAO, uuid4())
    assert contrato.situacao == SituacaoContrato.EM_ELABORACAO


def test_transicao_completa_da_vida_util():
    usuario = uuid4()
    contrato = _criar_contrato()

    contrato.alterar_situacao(SituacaoContrato.ASSINADO, usuario)
    assert contrato.situacao == SituacaoContrato.ASSINADO

    contrato.alterar_situacao(SituacaoContrato.VIGENTE, usuario)
    assert contrato.situacao == SituacaoContrato.VIGENTE

    contrato.alterar_situacao(SituacaoContrato.ENCERRADO, usuario)
    assert contrato.situacao == SituacaoContrato.ENCERRADO


def test_transicao_de_encerrado_nao_permitida():
    usuario = uuid4()
    contrato = _criar_contrato(situacao=SituacaoContrato.ENCERRADO)

    with pytest.raises(ValueError, match="não permitida"):
        contrato.alterar_situacao(SituacaoContrato.VIGENTE, usuario)


def test_alterar_situacao_registra_usuario_e_data():
    usuario = uuid4()
    contrato = _criar_contrato()
    contrato.alterar_situacao(SituacaoContrato.ASSINADO, usuario)

    assert contrato.updated_by == usuario
    assert contrato.updated_at is not None


def test_esta_vigente_true_apenas_em_vigente():
    contrato = _criar_contrato(situacao=SituacaoContrato.VIGENTE)
    assert contrato.esta_vigente() is True

    contrato.alterar_situacao(SituacaoContrato.ENCERRADO, uuid4())
    assert contrato.esta_vigente() is False


# -- Atualização de dados ----------------------------------------------------------


def test_atualizar_dados_modifica_campos():
    usuario = uuid4()
    contrato = _criar_contrato()

    contrato.atualizar_dados(
        numero="002/2026",
        data_inicio=date(2026, 2, 1),
        data_fim=date(2026, 11, 30),
        valor=Decimal("20000.00"),
        objeto="Nova descrição do objeto",
        usuario_id=usuario,
    )

    assert contrato.numero == "002/2026"
    assert contrato.data_inicio == date(2026, 2, 1)
    assert contrato.data_fim == date(2026, 11, 30)
    assert contrato.valor == Decimal("20000.00")
    assert contrato.objeto == "Nova descrição do objeto"
    assert contrato.updated_by == usuario


def test_atualizar_dados_registra_usuario_e_data():
    usuario = uuid4()
    contrato = _criar_contrato()
    contrato.atualizar_dados(numero="002", usuario_id=usuario)

    assert contrato.updated_by == usuario
    assert contrato.updated_at > datetime(2000, 1, 1, tzinfo=UTC)


def test_atualizar_objeto_vazio_vira_none():
    contrato = _criar_contrato(objeto="Texto inicial")
    contrato.atualizar_dados(objeto="   ")
    assert contrato.objeto is None


# -- Exclusão (soft-delete) --------------------------------------------------------


def test_excluir_marca_soft_delete():
    usuario = uuid4()
    contrato = _criar_contrato()
    contrato.excluir(usuario)

    assert contrato.foi_excluido() is True
    assert contrato.deleted_by == usuario
    assert contrato.deleted_at is not None


def test_foi_excluido_false_antes_da_exclusao():
    contrato = _criar_contrato()
    assert contrato.foi_excluido() is False