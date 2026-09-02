"""Testes unitários do agregado Pessoa (DOM-CUM RN-CUM-001 a 007)."""

from __future__ import annotations

from uuid import uuid4

import pytest

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


def _pessoa_fisica(**kwargs) -> Pessoa:
    return Pessoa(
        tipo=TipoPessoa.FISICA,
        categoria=CategoriaPessoa.CIDADAO,
        dados_fisicos=DadosFisicos(nome="Maria da Silva", **kwargs.pop("fisicos", {})),
        **kwargs,
    )


def _pessoa_juridica(**kwargs) -> Pessoa:
    return Pessoa(
        tipo=TipoPessoa.JURIDICA,
        categoria=CategoriaPessoa.FORNECEDOR,
        dados_juridicos=DadosJuridicos(razao_social="Alfa Comércio LTDA"),
        **kwargs,
    )


class TestRN001ExtensaoCondicionada:
    """RN-CUM-001: extensão física/jurídica condicionada ao tipo."""

    def test_pessoa_fisica_exige_dados_fisicos(self):
        with pytest.raises(ValueError, match="RN-CUM-001"):
            Pessoa(tipo=TipoPessoa.FISICA, categoria=CategoriaPessoa.CIDADAO)

    def test_pessoa_juridica_exige_dados_juridicos(self):
        with pytest.raises(ValueError, match="RN-CUM-001"):
            Pessoa(tipo=TipoPessoa.JURIDICA, categoria=CategoriaPessoa.FORNECEDOR)

    def test_pessoa_fisica_nao_aceita_dados_juridicos(self):
        with pytest.raises(ValueError, match="RN-CUM-001"):
            Pessoa(
                tipo=TipoPessoa.FISICA,
                categoria=CategoriaPessoa.CIDADAO,
                dados_fisicos=DadosFisicos(nome="Maria"),
                dados_juridicos=DadosJuridicos(razao_social="X"),
            )

    def test_nome_vazio_rejeitado(self):
        with pytest.raises(ValueError, match="obrigatório"):
            DadosFisicos(nome="   ")

    def test_nome_identificacao(self):
        assert _pessoa_fisica().nome_identificacao == "Maria da Silva"
        assert _pessoa_juridica().nome_identificacao == "Alfa Comércio LTDA"


class TestRN002003Documentos:
    """RN-CUM-002/003: CPF/CNPJ validados; RN-CUM-006: principal único."""

    def test_cpf_invalido_rejeitado(self):
        pessoa = _pessoa_fisica()
        with pytest.raises(ValueError, match="RN-CUM-002"):
            pessoa.adicionar_documento(TipoDocumento.CPF, "52998224724")

    def test_cnpj_invalido_rejeitado(self):
        pessoa = _pessoa_juridica()
        with pytest.raises(ValueError, match="RN-CUM-003"):
            pessoa.adicionar_documento(TipoDocumento.CNPJ, "11222333000182")

    def test_cpf_normalizado_para_digitos(self):
        pessoa = _pessoa_fisica()
        doc = pessoa.adicionar_documento(TipoDocumento.CPF, "529.982.247-25")
        assert doc.numero == "52998224725"

    def test_documento_principal_unico_por_tipo(self):
        pessoa = _pessoa_fisica()
        primeiro = pessoa.adicionar_documento(TipoDocumento.CPF, "52998224725", principal=True)
        segundo = pessoa.adicionar_documento(TipoDocumento.CPF, "11144477735", principal=True)
        assert not primeiro.principal
        assert segundo.principal
        assert pessoa.documento_principal(TipoDocumento.CPF) is segundo


class TestRN005Enderecos:
    """RN-CUM-005: endereço principal vigente único."""

    def test_endereco_principal_desativa_anterior(self):
        pessoa = _pessoa_fisica()
        primeiro = pessoa.adicionar_endereco(
            TipoEndereco.RESIDENCIAL, "Rua A", "1", principal=True
        )
        segundo = pessoa.adicionar_endereco(
            TipoEndereco.RESIDENCIAL, "Rua B", "2", principal=True
        )
        assert not primeiro.principal
        assert segundo.principal

    def test_remover_endereco_inexistente(self):
        pessoa = _pessoa_fisica()
        with pytest.raises(ValueError, match="não encontrado"):
            pessoa.remover_endereco(uuid4())

    def test_remover_endereco(self):
        pessoa = _pessoa_fisica()
        endereco = pessoa.adicionar_endereco(TipoEndereco.RESIDENCIAL, "Rua A", "1")
        pessoa.remover_endereco(endereco.id)
        assert endereco.foi_excluido()


class TestRN006Contatos:
    """RN-CUM-006: contato principal único por tipo."""

    def test_contato_principal_desativa_anterior(self):
        pessoa = _pessoa_fisica()
        primeiro = pessoa.adicionar_contato(TipoContato.EMAIL, "a@x.com", principal=True)
        segundo = pessoa.adicionar_contato(TipoContato.EMAIL, "b@x.com", principal=True)
        assert not primeiro.principal
        assert segundo.principal

    def test_contato_valor_obrigatorio(self):
        pessoa = _pessoa_fisica()
        with pytest.raises(ValueError, match="obrigatório"):
            pessoa.adicionar_contato(TipoContato.EMAIL, "  ")


class TestRN007CicloDeVida:
    """RN-CUM-007: exclusão lógica preservando histórico."""

    def test_excluir_cascata_para_filhos(self):
        pessoa = _pessoa_fisica()
        endereco = pessoa.adicionar_endereco(TipoEndereco.RESIDENCIAL, "Rua A", "1")
        documento = pessoa.adicionar_documento(TipoDocumento.RG, "1234567")
        contato = pessoa.adicionar_contato(TipoContato.EMAIL, "a@x.com")
        usuario = uuid4()
        pessoa.excluir(usuario)
        assert pessoa.foi_excluido()
        assert endereco.foi_excluido()
        assert documento.foi_excluido()
        assert contato.foi_excluido()
        assert pessoa.deleted_by == usuario

    def test_operacoes_apos_exclusao_rejeitadas(self):
        pessoa = _pessoa_fisica()
        pessoa.excluir(uuid4())
        with pytest.raises(ValueError, match="RN-CUM-007"):
            pessoa.adicionar_endereco(TipoEndereco.RESIDENCIAL, "Rua B", "2")

    def test_atualizar_dados_fisicos(self):
        pessoa = _pessoa_fisica()
        pessoa.atualizar_dados_fisicos(nome="Maria S. Almeida")
        assert pessoa.dados_fisicos.nome == "Maria S. Almeida"

    def test_atualizar_dados_juridicos_somente_pj(self):
        with pytest.raises(ValueError, match="RN-CUM-001"):
            _pessoa_fisica().atualizar_dados_juridicos(razao_social="X")

    def test_alterar_categoria(self):
        pessoa = _pessoa_fisica()
        pessoa.alterar_categoria(CategoriaPessoa.SERVIDOR)
        assert pessoa.categoria is CategoriaPessoa.SERVIDOR
