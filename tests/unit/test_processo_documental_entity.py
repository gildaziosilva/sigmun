"""Testes unitários da entidade ProcessoDocumental."""

from uuid import uuid4

import pytest

from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)


def _criar_processo(**overrides) -> ProcessoDocumental:
    dados = {
        "unidade_id": uuid4(),
        "numero": "001",
        "ano": 2026,
        "assunto": "Aquisição de materiais de escritório",
    }
    dados.update(overrides)
    return ProcessoDocumental(**dados)


def test_criar_processo_com_valores_padrao():
    processo = _criar_processo()

    assert processo.id is not None
    assert not processo.foi_excluido()
    assert processo.descricao is None


def test_unidade_obrigatoria():
    with pytest.raises(ValueError, match="unidade_id"):
        _criar_processo(unidade_id=None)  # type: ignore[arg-type]


@pytest.mark.parametrize("numero", ["", "   ", None])
def test_numero_invalido_lanca_erro(numero):
    with pytest.raises(ValueError, match="numero"):
        _criar_processo(numero=numero)


@pytest.mark.parametrize("ano", [1899, 2101, 0, -2026])
def test_ano_fora_do_intervalo_lanca_erro(ano):
    with pytest.raises(ValueError, match="ano"):
        _criar_processo(ano=ano)


@pytest.mark.parametrize("assunto", ["", "  ", None])
def test_assunto_invalido_lanca_erro(assunto):
    with pytest.raises(ValueError, match="assunto"):
        _criar_processo(assunto=assunto)


def test_atualizar_dados_registra_usuario_e_normaliza():
    usuario = uuid4()
    processo = _criar_processo()

    processo.atualizar_dados(
        numero=" 002 ", ano=2027, assunto="Nova licitação de TI", usuario_id=usuario
    )

    assert processo.numero == "002"
    assert processo.ano == 2027
    assert processo.assunto == "Nova licitação de TI"
    assert processo.updated_by == usuario


def test_atualizar_descricao_vira_none_quando_vazia():
    processo = _criar_processo(descricao="Texto inicial")

    processo.atualizar_dados(descricao="   ")

    assert processo.descricao is None


def test_excluir_marca_soft_delete():
    usuario = uuid4()
    processo = _criar_processo()

    processo.excluir(usuario)

    assert processo.foi_excluido() is True
    assert processo.deleted_by == usuario
