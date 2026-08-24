"""Testes unitários dos casos de uso de Compra (processo de compras).

Usam um repositório em memória que implementa o contrato do domínio,
validando as regras RN-COMPRAS-025 a 029 sem depender de banco.
"""

from decimal import Decimal
from uuid import UUID, uuid4

import pytest

from src.modules.sigmun_compras.application.commands.alterar_situacao_compra_command import (
    AlterarSituacaoCompraCommand,
)
from src.modules.sigmun_compras.application.commands.atualizar_compra_command import (
    AtualizarCompraCommand,
)
from src.modules.sigmun_compras.application.commands.criar_compra_command import (
    CriarCompraCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_compra_command import (
    ExcluirCompraCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_compra_query import (
    ConsultarCompraQuery,
)
from src.modules.sigmun_compras.application.queries.listar_compras_query import (
    ListarComprasQuery,
)
from src.modules.sigmun_compras.application.use_cases.alterar_situacao_compra import (
    AlterarSituacaoCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_compra import (
    AtualizarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_compra import (
    ConsultarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_compra import (
    ExcluirCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_compras import (
    ListarComprasUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_compra import (
    RegistrarCompraUseCase,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.compra_repository import (
    CompraRepository,
)


class InMemoryCompraRepository(CompraRepository):
    """Repositório em memória para testes."""

    def __init__(self) -> None:
        self._data: dict[UUID, Compra] = {}
        self.processos: set[UUID] = set()
        self.fornecedores_ativos: set[UUID] = set()
        self.unidades: set[UUID] = set()

    def add_processo(self, pid: UUID) -> None:
        self.processos.add(pid)

    def add_fornecedor_ativo(self, fid: UUID) -> None:
        self.fornecedores_ativos.add(fid)

    def add_unidade(self, uid: UUID) -> None:
        self.unidades.add(uid)

    def save(self, compra: Compra) -> Compra:
        self._data[compra.id] = compra
        return compra

    def get_by_id(self, compra_id: UUID):
        return self._data.get(compra_id)

    def list(self, situacao=None, include_deleted=False, limit=None, offset=0):
        itens = [
            c
            for c in self._data.values()
            if (include_deleted or not c.foi_excluido())
            and (situacao is None or c.situacao == situacao)
        ]
        itens.sort(key=lambda c: c.created_at)
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    def update(self, compra: Compra) -> Compra:
        return self.save(compra)

    def delete(self, compra_id: UUID, usuario_id: UUID) -> None:
        compra = self._data.get(compra_id)
        if compra:
            compra.excluir(usuario_id)

    def exists_processo_documental(self, pid: UUID) -> bool:
        return pid in self.processos

    def exists_fornecedor_ativo(self, fid: UUID) -> bool:
        return fid in self.fornecedores_ativos

    def exists_unidade(self, uid: UUID) -> bool:
        return uid in self.unidades


@pytest.fixture()
def repository() -> InMemoryCompraRepository:
    repo = InMemoryCompraRepository()
    repo.add_processo(uuid4())
    repo.add_fornecedor_ativo(uuid4())
    repo.add_unidade(uuid4())
    return repo


def _command(repository: InMemoryCompraRepository, **overrides) -> CriarCompraCommand:
    dados = {
        "processo_documental_id": next(iter(repository.processos)),
        "fornecedor_id": next(iter(repository.fornecedores_ativos)),
        "unidade_id": next(iter(repository.unidades)),
        "numero": "001/2026",
        "valor_total": Decimal("1000.00"),
    }
    dados.update(overrides)
    return CriarCompraCommand(**dados)


# -- Registrar -----------------------------------------------------------------


def test_registrar_compra_sucesso(repository):
    compra = RegistrarCompraUseCase(repository).execute(_command(repository))

    assert compra.id in repository._data  # noqa: SLF001
    assert compra.situacao == SituacaoCompra.RASCUNHO


def test_registrar_compra_processo_inexistente_lanca_erro(repository):
    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        RegistrarCompraUseCase(repository).execute(
            _command(repository, processo_documental_id=uuid4())
        )


def test_registrar_compra_fornecedor_inexistente_lanca_erro(repository):
    with pytest.raises(FornecedorNaoEncontradoError):
        RegistrarCompraUseCase(repository).execute(
            _command(repository, fornecedor_id=uuid4())
        )


def test_registrar_compra_unidade_inexistente_lanca_erro(repository):
    with pytest.raises(UnidadeNaoEncontradaError):
        RegistrarCompraUseCase(repository).execute(_command(repository, unidade_id=uuid4()))


# -- Consultar -----------------------------------------------------------------


def test_consultar_compra_sucesso_e_nao_encontrado(repository):
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))
    consulta = ConsultarCompraUseCase(repository)

    assert consulta.execute(ConsultarCompraQuery(compra_id=criada.id)).id == criada.id

    with pytest.raises(CompraNaoEncontradaError):
        consulta.execute(ConsultarCompraQuery(compra_id=uuid4()))


# -- Listar --------------------------------------------------------------------


def test_listar_compras_com_paginacao_e_filtro(repository):
    registrar = RegistrarCompraUseCase(repository)
    for n in range(3):
        registrar.execute(_command(repository, numero=f"00{n}/2026"))
    registrar.execute(_command(repository, numero="010/2026", valor_total=Decimal("1.00")))

    pagina = ListarComprasUseCase(repository).execute(
        ListarComprasQuery(page=0, page_size=2)
    )
    rascunhos = ListarComprasUseCase(repository).execute(
        ListarComprasQuery(situacao=SituacaoCompra.RASCUNHO)
    )

    assert len(pagina) == 2
    assert len(rascunhos) == 4


# -- Atualizar -----------------------------------------------------------------


def test_atualizar_compra_sucesso(repository):
    usuario = uuid4()
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))

    atualizada = AtualizarCompraUseCase(repository).execute(
        AtualizarCompraCommand(
            compra_id=criada.id,
            numero="999/2026",
            valor_total=Decimal("2500.00"),
            usuario_id=usuario,
        )
    )

    assert atualizada.numero == "999/2026"
    assert atualizada.valor_total == Decimal("2500.00")
    assert atualizada.updated_by == usuario


def test_atualizar_compra_sem_campos_lanca_erro(repository):
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError):
        AtualizarCompraUseCase(repository).execute(
            AtualizarCompraCommand(compra_id=criada.id)
        )


def test_atualizar_compra_inexistente_lanca_erro(repository):
    with pytest.raises(CompraNaoEncontradaError):
        AtualizarCompraUseCase(repository).execute(
            AtualizarCompraCommand(compra_id=uuid4(), numero="X/2026")
        )


# -- Alterar situação ------------------------------------------------------------


def test_alterar_situacao_valida(repository):
    usuario = uuid4()
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))

    alterada = AlterarSituacaoCompraUseCase(repository).execute(
        AlterarSituacaoCompraCommand(
            compra_id=criada.id,
            nova_situacao=SituacaoCompra.EM_INSTRUCAO,
            usuario_id=usuario,
        )
    )

    assert alterada.situacao == SituacaoCompra.EM_INSTRUCAO
    assert alterada.updated_by == usuario


def test_alterar_situacao_invalida_propaga_erro(repository):
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError, match="RN-COMPRAS-026"):
        AlterarSituacaoCompraUseCase(repository).execute(
            AlterarSituacaoCompraCommand(
                compra_id=criada.id, nova_situacao=SituacaoCompra.CONTRATADO
            )
        )


def test_alterar_situacao_compra_inexistente_lanca_erro(repository):
    with pytest.raises(CompraNaoEncontradaError):
        AlterarSituacaoCompraUseCase(repository).execute(
            AlterarSituacaoCompraCommand(
                compra_id=uuid4(), nova_situacao=SituacaoCompra.EM_INSTRUCAO
            )
        )


# -- Excluir ---------------------------------------------------------------------


def test_excluir_compra_marca_soft_delete(repository):
    usuario = uuid4()
    criada = RegistrarCompraUseCase(repository).execute(_command(repository))

    excluida = ExcluirCompraUseCase(repository).execute(
        ExcluirCompraCommand(compra_id=criada.id, usuario_id=usuario)
    )

    assert excluida.foi_excluido() is True
    assert repository._data[criada.id].foi_excluido() is True  # noqa: SLF001

    with pytest.raises(CompraNaoEncontradaError):
        ConsultarCompraUseCase(repository).execute(
            ConsultarCompraQuery(compra_id=criada.id)
        )


def test_excluir_compra_inexistente_lanca_erro(repository):
    with pytest.raises(CompraNaoEncontradaError):
        ExcluirCompraUseCase(repository).execute(
            ExcluirCompraCommand(compra_id=uuid4(), usuario_id=uuid4())
        )
