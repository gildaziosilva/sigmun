"""Testes unitários dos Value Objects CPF e CNPJ (DOM-CUM RN-CUM-002/003)."""

from __future__ import annotations

import pytest

from src.modules.sigmun_cadastro.domain.value_objects.cnpj import CNPJ
from src.modules.sigmun_cadastro.domain.value_objects.cpf import CPF


class TestCPF:
    """Validação de CPF com dígitos verificadores (RN-CUM-002)."""

    def test_aceita_cpf_valido_com_mascara(self):
        cpf = CPF("529.982.247-25")
        assert cpf.valor == "52998224725"

    def test_aceita_cpf_valido_sem_mascara(self):
        assert CPF("11144477735").valor == "11144477735"

    def test_formatado(self):
        assert CPF("52998224725").formatado() == "529.982.247-25"

    def test_rejeita_quantidade_errada_de_digitos(self):
        with pytest.raises(ValueError, match="11 dígitos"):
            CPF("1234567890")

    def test_rejeita_digitos_repetidos(self):
        with pytest.raises(ValueError, match="repetidos"):
            CPF("11111111111")

    def test_rejeita_digito_verificador_invalido(self):
        with pytest.raises(ValueError, match="verificadores"):
            CPF("52998224724")

    def test_igualdade_e_hash(self):
        assert CPF("52998224725") == CPF("529.982.247-25")
        assert hash(CPF("52998224725")) == hash(CPF("52998224725"))

    def test_str_retorna_digitos(self):
        assert str(CPF("52998224725")) == "52998224725"


class TestCNPJ:
    """Validação de CNPJ com dígitos verificadores (RN-CUM-003)."""

    def test_aceita_cnpj_valido_com_mascara(self):
        cnpj = CNPJ("11.222.333/0001-81")
        assert cnpj.valor == "11222333000181"

    def test_aceita_cnpj_valido_sem_mascara(self):
        assert CNPJ("45723174000110").valor == "45723174000110"

    def test_formatado(self):
        assert CNPJ("11222333000181").formatado() == "11.222.333/0001-81"

    def test_rejeita_quantidade_errada_de_digitos(self):
        with pytest.raises(ValueError, match="14 dígitos"):
            CNPJ("1122233300018")

    def test_rejeita_digitos_repetidos(self):
        with pytest.raises(ValueError, match="repetidos"):
            CNPJ("11111111111111")

    def test_rejeita_digito_verificador_invalido(self):
        with pytest.raises(ValueError, match="verificadores"):
            CNPJ("11222333000182")

    def test_igualdade_e_hash(self):
        assert CNPJ("11222333000181") == CNPJ("11.222.333/0001-81")
        assert hash(CNPJ("11222333000181")) == hash(CNPJ("11222333000181"))
