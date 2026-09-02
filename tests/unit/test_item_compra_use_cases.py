"""Testes unitários dos casos de uso de Item de Compra.

Usam um repositório em memória que implementa o contrato do domínio,
validando as regras RN-COMPRAS-011 a 013 sem depender de banco.
"""

from decimal import Decimal
from uuid import UUID, uuid4

import pytest

from src.modules.sigmun_compras.application.commands.atualizar_item_compra_command import (
    AtualizarItemCompraCommand,
)
from src.modules.sigmun_compras.application.commands.criar_item_compra_command import (
    CriarItemCompraCommand,
)
from src.modules.sigmun_compras.application.commands.remover_item_compra_command import (
    RemoverItemCompraCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_item_compra_query import (
    ConsultarItemCompraQuery,
)
from src.modules.sigmun_compras.application.queries.listar_itens_compra_query import (
    ListarItensCompraQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_item_compra import (
    AtualizarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_item_compra import (
    ConsultarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_itens_compra import (
    ListarItensCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_item_compra import (
    RegistrarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.remover_item_compra import (
    RemoverItemCompraUseCase,
)
from src.modules.sigmun_compras.domain.entities.item_compra import ItemCompra
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    ItemNaoEncontradoError,
)
from src.modules.sigmun_compras.domain.repositories.item_compra_repository import (
    ItemCompraRepository,
)


class InMemoryItemCompraRepository(ItemCompraRepository):
    """Repositório em memória para testes."""

    def __init__(self, compras_existentes: set[UUID] | None = None) -> None:
        self._data: dict[UUID, ItemCompra] = {}
        self._compras: set[UUID] = compras_existentes or set()

    def add_compra(self, compra_id: UUID) -> None:
        self._compras.add(compra_id)

    def save(self, item: ItemCompra) -> ItemCompra:
        self._data[item.id] = item
        return item

    def get_by_id(self, item_id: UUID):
        return self._data.get(item_id)

    def list_by_compra(self, compra_id, include_deleted=False, limit=None, offset=0):
        itens = [
            i
            for i in self._data.values()
            if i.compra_id == compra_id
            and (include_deleted or not i.foi_excluido())
        ]
        itens.sort(key=lambda i: i.created_at)
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    def update(self, item: ItemCompra) -> ItemCompra:
        return self.save(item)

    def delete(self, item_id: UUID, usuario_id: UUID) -> None:
        item = self._data.get(item_id)
        if item:
            item.excluir(usuario_id)

    def exists_compra(self, compra_id: UUID) -> bool:
        return compra_id in self._compras


@pytest.fixture()
def repository() -> InMemoryItemCompraRepository:
    repo = InMemoryItemCompraRepository()
    repo.add_compra(uuid4())
    return repo


# -- Registrar -----------------------------------------------------------------


def test_registrar_item_sucesso(repository):
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    command = CriarItemCompraCommand(
        compra_id=compra_id,
        descricao="Serviço de manutenção de impressoras",
        quantidade=Decimal("2"),
        valor_unitario=Decimal("350.00"),
    )

    item = RegistrarItemCompraUseCase(repository).execute(command)

    assert item.valor_total == Decimal("700.00")
    assert item.pertence_a(compra_id)


def test_registrar_item_compra_inexistente_lanca_erro():
    repo = InMemoryItemCompraRepository()  # nenhuma compra registrada
    command = CriarItemCompraCommand(
        compra_id=uuid4(),
        descricao="Material de escritório",
        quantidade=Decimal("10"),
        valor_unitario=Decimal("5.00"),
    )

    with pytest.raises(CompraNaoEncontradaError):
        RegistrarItemCompraUseCase(repo).execute(command)


def test_registrar_item_quantidade_invalida_propaga_erro(repository):
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    command = CriarItemCompraCommand(
        compra_id=compra_id,
        descricao="Produto X",
        quantidade=Decimal("0"),
        valor_unitario=Decimal("5.00"),
    )

    with pytest.raises(ValueError, match="RN-COMPRAS-012"):
        RegistrarItemCompraUseCase(repository).execute(command)


# -- Consultar -----------------------------------------------------------------


def test_consultar_item_sucesso_e_nao_encontrado(repository):
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    criado = RegistrarItemCompraUseCase(repository).execute(
        CriarItemCompraCommand(
            compra_id=compra_id,
            descricao="Licença de software",
            quantidade=Decimal("5"),
            valor_unitario=Decimal("120.00"),
        )
    )
    consulta = ConsultarItemCompraUseCase(repository)

    assert consulta.execute(ConsultarItemCompraQuery(item_id=criado.id)).id == criado.id

    with pytest.raises(ItemNaoEncontradoError):
        consulta.execute(ConsultarItemCompraQuery(item_id=uuid4()))


# -- Listar --------------------------------------------------------------------


def test_listar_itens_por_compra_e_paginacao(repository):
    registrar = RegistrarItemCompraUseCase(repository)
    compra_a = uuid4()
    compra_b = uuid4()
    repository.add_compra(compra_a)
    repository.add_compra(compra_b)

    for n in range(3):
        registrar.execute(
            CriarItemCompraCommand(
                compra_id=compra_a,
                descricao=f"Item A{n} - material de consumo",
                quantidade=Decimal("1"),
                valor_unitario=Decimal("10.00"),
            )
        )
    registrar.execute(
        CriarItemCompraCommand(
            compra_id=compra_b,
            descricao="Serviço de pintura predial",
            quantidade=Decimal("1"),
            valor_unitario=Decimal("500.00"),
        )
    )

    pagina = ListarItensCompraUseCase(repository).execute(
        ListarItensCompraQuery(compra_id=compra_a, page=0, page_size=2)
    )
    todos_b = ListarItensCompraUseCase(repository).execute(
        ListarItensCompraQuery(compra_id=compra_b)
    )

    assert len(pagina) == 2
    assert all(i.compra_id == compra_a for i in pagina)
    assert len(todos_b) == 1
    assert todos_b[0].compra_id == compra_b


def test_listar_itens_compra_inexistente_lanca_erro(repository):
    with pytest.raises(CompraNaoEncontradaError):
        ListarItensCompraUseCase(repository).execute(ListarItensCompraQuery(compra_id=uuid4()))


# -- Atualizar -----------------------------------------------------------------


def test_atualizar_item_recalcula_total(repository):
    usuario = uuid4()
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    criado = RegistrarItemCompraUseCase(repository).execute(
        CriarItemCompraCommand(
            compra_id=compra_id,
            descricao="Cadeira giratória",
            quantidade=Decimal("4"),
            valor_unitario=Decimal("300.00"),
        )
    )

    atualizado = AtualizarItemCompraUseCase(repository).execute(
        AtualizarItemCompraCommand(
            item_id=criado.id, quantidade=Decimal("7"), usuario_id=usuario
        )
    )

    assert atualizado.valor_unitario == Decimal("300.00")
    assert atualizado.valor_total == Decimal("2100.00")
    assert atualizado.updated_by == usuario


def test_atualizar_item_sem_campos_lanca_erro(repository):
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    criado = RegistrarItemCompraUseCase(repository).execute(
        CriarItemCompraCommand(
            compra_id=compra_id,
            descricao="Mesa de escritório",
            quantidade=Decimal("1"),
            valor_unitario=Decimal("800.00"),
        )
    )

    with pytest.raises(ValueError):
        AtualizarItemCompraUseCase(repository).execute(
            AtualizarItemCompraCommand(item_id=criado.id)
        )


def test_atualizar_item_inexistente_lanca_erro(repository):
    with pytest.raises(ItemNaoEncontradoError):
        AtualizarItemCompraUseCase(repository).execute(
            AtualizarItemCompraCommand(item_id=uuid4(), quantidade=Decimal("1"))
        )


# -- Remover -------------------------------------------------------------------


def test_remover_item_marca_soft_delete(repository):
    usuario = uuid4()
    compra_id = next(iter(repository._compras))  # noqa: SLF001
    criado = RegistrarItemCompraUseCase(repository).execute(
        CriarItemCompraCommand(
            compra_id=compra_id,
            descricao="Monitor 24 polegadas",
            quantidade=Decimal("2"),
            valor_unitario=Decimal("900.00"),
        )
    )

    removido = RemoverItemCompraUseCase(repository).execute(
        RemoverItemCompraCommand(item_id=criado.id, usuario_id=usuario)
    )

    assert removido.foi_excluido() is True

    with pytest.raises(ItemNaoEncontradoError):
        ConsultarItemCompraUseCase(repository).execute(
            ConsultarItemCompraQuery(item_id=criado.id)
        )


def test_remover_item_inexistente_lanca_erro(repository):
    with pytest.raises(ItemNaoEncontradoError):
        RemoverItemCompraUseCase(repository).execute(
            RemoverItemCompraCommand(item_id=uuid4(), usuario_id=uuid4())
        )
