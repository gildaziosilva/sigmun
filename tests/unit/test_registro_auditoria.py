"""Testes unitários da auditoria (entidade, serviço e consulta).

Usam um repositório em memória que implementa o contrato do domínio,
validando o modelo do 017-Modelo-de-Auditoria sem depender de banco.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from src.shared.compat import UTC

import pytest

from src.modules.sigmun_compras.application.queries.consultar_trilha_auditoria_query import (
    ConsultarTrilhaAuditoriaQuery,
)
from src.modules.sigmun_compras.application.services.servico_de_auditoria import (
    ServicoDeAuditoria,
)
from src.modules.sigmun_compras.application.use_cases.consultar_trilha_auditoria import (
    ConsultarTrilhaAuditoriaUseCase,
)
from src.modules.sigmun_compras.domain.entities.registro_auditoria import (
    CategoriaEventoAuditoria,
    RegistroAuditoria,
    ResultadoEventoAuditoria,
)
from src.modules.sigmun_compras.domain.repositories.trilha_auditoria_repository import (
    TrilhaAuditoriaRepository,
)


class InMemoryTrilhaAuditoriaRepository(TrilhaAuditoriaRepository):
    """Repositório em memória para testes."""

    def __init__(self) -> None:
        self._data: list[RegistroAuditoria] = []

    def registrar(self, registro: RegistroAuditoria) -> RegistroAuditoria:
        self._data.append(registro)
        return registro

    def list(self, **filtros) -> list[RegistroAuditoria]:
        data_inicio = filtros.get("data_inicio")
        data_fim = filtros.get("data_fim")
        usuario_id = filtros.get("usuario_id")
        categoria = filtros.get("categoria")
        recurso_tipo = filtros.get("recurso_tipo")
        recurso_id = filtros.get("recurso_id")
        correlation_id = filtros.get("correlation_id")

        itens = [
            r
            for r in self._data
            if (data_inicio is None or r.ocorrido_em >= data_inicio)
            and (data_fim is None or r.ocorrido_em <= data_fim)
            and (usuario_id is None or r.ator_id == usuario_id)
            and (categoria is None or r.categoria == categoria)
            and (recurso_tipo is None or r.recurso_tipo == recurso_tipo)
            and (recurso_id is None or r.recurso_id == recurso_id)
            and (correlation_id is None or r.correlation_id == correlation_id)
        ]
        itens.sort(key=lambda r: r.ocorrido_em, reverse=True)
        limit = filtros.get("limit")
        offset = filtros.get("offset", 0)
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    @property
    def eventos(self) -> list[RegistroAuditoria]:
        """Acesso bruto para asserções dos testes."""
        return list(self._data)

    def count(self, **filtros) -> int:
        filtros = {**filtros, "limit": None, "offset": 0}
        return len(self.list(**filtros))


# -- Entidade --------------------------------------------------------------------


def test_criar_registro_com_valores_padrao() -> None:
    registro = RegistroAuditoria(
        tipo_evento="ContratoCriado", operacao="criarContrato", recurso_tipo="Contrato"
    )

    assert registro.id is not None
    assert registro.ocorrido_em.tzinfo is not None  # padrão temporal UTC
    assert registro.categoria == CategoriaEventoAuditoria.ALTERACAO
    assert registro.resultado == ResultadoEventoAuditoria.SUCESSO
    assert registro.origem == RegistroAuditoria.ORIGEM_PADRAO


@pytest.mark.parametrize("categoria", ["CRIACAO", "EXCLUSAO"])
def test_categoria_valida_por_valor(categoria: str) -> None:
    registro = RegistroAuditoria(
        categoria=CategoriaEventoAuditoria(categoria),
        tipo_evento="X",
        operacao="op",
        recurso_tipo="Contrato",
    )
    assert registro.categoria.value == categoria


def test_categoria_invalida_lanca_erro() -> None:
    with pytest.raises(ValueError, match="Categoria"):
        RegistroAuditoria(
            categoria="INEXISTENTE",  # type: ignore[arg-type]
            tipo_evento="X",
            operacao="op",
            recurso_tipo="Contrato",
        )


@pytest.mark.parametrize(
    ("campo", "kwargs"),
    [
        ("tipo_evento", {"tipo_evento": "   ", "operacao": "op", "recurso_tipo": "Contrato"}),
        ("operacao", {"tipo_evento": "X", "operacao": "", "recurso_tipo": "Contrato"}),
        ("recurso_tipo", {"tipo_evento": "X", "operacao": "op", "recurso_tipo": None}),
        (
            "origem",
            {"tipo_evento": "X", "operacao": "op", "recurso_tipo": "Contrato", "origem": "  "},
        ),
    ],
)
def test_campos_obrigatorios_lancam_erro(campo: str, kwargs: dict) -> None:
    with pytest.raises(ValueError, match=campo):
        RegistroAuditoria(**kwargs)  # type: ignore[arg-type]


# -- ServicoDeAuditoria ----------------------------------------------------------


def test_registrar_evento_sucesso() -> None:
    repo = InMemoryTrilhaAuditoriaRepository()
    servico = ServicoDeAuditoria(repo)

    ator = uuid4()
    recurso = uuid4()
    salvo = servico.registrar(
        categoria=CategoriaEventoAuditoria.CRIACAO,
        tipo_evento="ContratoCriado",
        operacao="criarContrato",
        recurso_tipo="Contrato",
        recurso_id=recurso,
        chave_negocio="CT-001/2026",
        ator_id=ator,
        detalhes={"situacao_inicial": "EM_ELABORACAO"},
    )

    assert salvo is not None
    assert len(repo.eventos) == 1
    evento = repo.eventos[0]
    assert evento.categoria == CategoriaEventoAuditoria.CRIACAO
    assert evento.ator_id == ator
    assert evento.recurso_id == recurso
    assert evento.chave_negocio == "CT-001/2026"


def test_falha_de_auditoria_nao_interrompe_negocio() -> None:
    class RepositorioQuebrado(InMemoryTrilhaAuditoriaRepository):
        def registrar(self, registro):
            raise RuntimeError("falha simulada")

    servico = ServicoDeAuditoria(RepositorioQuebrado())
    resultado = servico.registrar(
        categoria=CategoriaEventoAuditoria.ALTERACAO,
        tipo_evento="ContratoAlterado",
        operacao="atualizarContrato",
        recurso_tipo="Contrato",
    )

    assert resultado is None  # operação de negócio segue sem exceção


# -- Consulta --------------------------------------------------------------------


def test_consultar_com_filtros_e_paginacao() -> None:
    repo = InMemoryTrilhaAuditoriaRepository()

    usuario_a = uuid4()
    recurso_1 = uuid4()
    for i in range(3):
        base = datetime(2026, 8, 1, 10, i, tzinfo=UTC)
        repo.registrar(
            RegistroAuditoria(
                ocorrido_em=base,
                categoria=CategoriaEventoAuditoria.CRIACAO,
                tipo_evento=f"Evento{i}",
                operacao="op",
                recurso_tipo="Contrato",
                recurso_id=recurso_1 if i < 2 else uuid4(),
                ator_id=usuario_a if i < 2 else None,
            )
        )

    todos = ConsultarTrilhaAuditoriaUseCase(repo).execute(ConsultarTrilhaAuditoriaQuery())
    por_recurso = ConsultarTrilhaAuditoriaUseCase(repo).execute(
        ConsultarTrilhaAuditoriaQuery(recurso_tipo="Contrato", recurso_id=recurso_1)
    )
    por_usuario = ConsultarTrilhaAuditoriaUseCase(repo).execute(
        ConsultarTrilhaAuditoriaQuery(usuario_id=usuario_a)
    )
    pagina = ConsultarTrilhaAuditoriaUseCase(repo).execute(
        ConsultarTrilhaAuditoriaQuery(page=0, page_size=2)
    )

    assert len(todos) == 3
    assert len(por_recurso) == 2
    assert len(por_usuario) == 2
    assert len(pagina) == 2
    # linha do tempo em ordem descendente (mais recente primeiro)
    assert todos[0].ocorrido_em >= todos[-1].ocorrido_em
