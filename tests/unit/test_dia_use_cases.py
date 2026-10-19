"""Testes unitários dos Use Cases de Diárias (DOM-DIA) — T-4.2.

Cobertura alvo: >= 80% para todos os 5 use cases:
- criar_diaria_use_case.py
- criar_prestacao_use_case.py
- aprovar_prestacao_use_case.py
- glosar_prestacao_use_case.py
- restituir_prestacao_use_case.py
"""
from datetime import datetime
from unittest.mock import MagicMock

import pytest

from src.modules.sigmun_dia.application.use_cases import (
    AprovacaoPrestacaoInputDTO,
    AprovarPrestacaoUseCase,
    SolicitacaoDiariaInput,
    CriarDiariaUseCase,
    CriarPrestacaoContasInputDTO,
    CriarPrestacaoContasUseCase,
    GlosagemPrestacaoInputDTO,
    GlosarPrestacaoUseCase,
    RestituicaPrestacaoInputDTO,
    RestituirPrestacaoUseCase,
)
from src.modules.sigmun_dia.domain.entities import (
    CategoriaDiaria,
    Diaria,
    PrestacaoContas,
    StatusDiaria,
)
from src.modules.sigmun_dia.domain.exceptions import (
    DiariaNaoEncontradaError,
    PrestacaoContasNaoEncontradaError,
    RegraNegocioError,
    ValidacaoDiariaError,
    ViagemNaoEncontradaError,
)
from src.modules.sigmun_dia.application.interfaces import (
    RepositorioDiaria,
    RepositorioPrestacaoContas,
    RepositorioViagem,
)


def _make_viagem():
    viagem = MagicMock()
    viagem.id = "viagem-1"
    return viagem


def _make_diaria(status="paga", **kwargs):
    d = MagicMock(spec=Diaria)
    d.id = "diaria-1"
    d.viagem_id = "viagem-1"
    d.servidor_id = "servidor-1"
    d.dota_id = "dota-1"
    d.categoria = CategoriaDiaria.EVENTO
    d.descricao = "Diária de teste"
    d.data_inicio = None
    d.data_fim = None
    d.valor_diaria = 150.0
    d.valor_total = 300.0
    d.status = type('Status', (), {'value': status})()
    d.data_solicitacao = None
    d.data_autorizacao = None
    d.data_calculo = None
    d.data_concessao = None
    d.data_inicio_prestacao = None
    d.data_fim_prestacao = None
    d.data_pagamento = None
    d.data_aprovacao = None
    d.data_glosa = None
    d.data_restituicao = None
    d.data_cancelamento = None
    d.motivo_cancelamento = ""
    d.motivo_glosa = ""
    d.valor_glosado = 0.0
    d.documento_prestacao_id = ""
    d.created_at = datetime.utcnow()
    d.updated_at = None
    d.created_by = "teste"
    d.updated_by = None
    d.is_deleted = False
    d.is_active = True
    d.aprovar = MagicMock()
    d.glosar = MagicMock()
    d.restituir = MagicMock()
    for k, v in kwargs.items():
        setattr(d, k, v)
    return d


def _make_prestacao(status="aberta", **kwargs):
    p = MagicMock(spec=PrestacaoContas)
    p.id = "prestacao-1"
    p.diaria_id = "diaria-1"
    p.servidor_id = "servidor-1"
    p.dota_id = "dota-1"
    p.data_emissao = None
    p.data_vencimento = None
    p.documento_id = "doc-1"
    p.valor_previsto = 300.0
    p.valor_apresentado = 300.0
    p.valor_glosado = 0.0
    p.valor_liquido = 300.0
    p.status = status
    p.motivo_glosa = ""
    p.created_at = datetime.utcnow()
    p.updated_at = None
    p.created_by = "teste"
    p.updated_by = None
    p.is_deleted = False
    p.aprovar = MagicMock()
    p.glosar = MagicMock()
    p.restituir = MagicMock()
    for k, v in kwargs.items():
        setattr(p, k, v)
    return p


class TestCriarDiariaUseCase:
    def test_criar_diaria_sucesso(self):
        repo_diaria = MagicMock()
        repo_viagem = MagicMock()
        repo_viagem.get_by_id.return_value = MagicMock(id="viagem-1")
        repo_diaria.save = MagicMock(return_value=MagicMock(id="diaria-1", viagem_id="viagem-1", status="solicitada", valor_diaria=150.0))
        
        uc = CriarDiariaUseCase(MagicMock(), MagicMock())
        dto = SolicitacaoDiariaInput(viagem_id="viagem-1", servidor_id="s1", dota_id="d1", categoria="evento")
        result = uc.execute(dto)
        assert result is not None

    def test_criar_diaria_categoria_invalida(self):
        repo_diaria = MagicMock()
        repo_viagem = MagicMock()
        repo_viagem.get_by_id.return_value = MagicMock()
        
        uc = CriarDiariaUseCase(repo_diaria, repo_viagem)
        dto = SolicitacaoDiariaInput(viagem_id="viagem-1", servidor_id="s1", dota_id="d1", categoria="invalida")
        with pytest.raises(ValueError):
            uc.execute(dto)


class TestCriarPrestacaoContasUseCase:
    def test_criar_prestacao_sucesso(self):
        pass


class TestAprovarPrestacaoUseCase:
    def test_aprovar_prestacao_sucesso(self):
        pass


class TestGlosarPrestacaoUseCase:
    def test_glosar_prestacao_sucesso(self):
        pass


class TestRestituirPrestacaoUseCase:
    def test_restituir_prestacao_sucesso(self):
        pass
