"""Testes unitários dos casos de uso de Fornecedor.

Usam um repositório em memória que implementa o contrato do domínio,
validando as regras RN-COMPRAS-030 a 033 sem depender de banco.
"""

from uuid import UUID, uuid4

import pytest

from src.modules.sigmun_compras.application.commands.atualizar_fornecedor_command import (
    AtualizarFornecedorCommand,
)
from src.modules.sigmun_compras.application.commands.criar_fornecedor_command import (
    CriarFornecedorCommand,
)
from src.modules.sigmun_compras.application.commands.inativar_fornecedor_command import (
    InativarFornecedorCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_fornecedor_query import (
    ConsultarFornecedorQuery,
)
from src.modules.sigmun_compras.application.queries.listar_fornecedores_query import (
    ListarFornecedoresQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_fornecedor import (
    AtualizarFornecedorUseCase,
    FornecedorNaoEncontradoError,
)
from src.modules.sigmun_compras.application.use_cases.consultar_fornecedor import (
    ConsultarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.inativar_fornecedor import (
    InativarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_fornecedores import (
    ListarFornecedoresUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_fornecedor import (
    FornecedorJaCadastradoError,
    RegistrarFornecedorUseCase,
)
from src.modules.sigmun_compras.domain.entities.fornecedor import Fornecedor, SituacaoFornecedor
from src.modules.sigmun_compras.domain.repositories.fornecedor_repository import (
    FornecedorRepository,
)


class InMemoryFornecedorRepository(FornecedorRepository):
    """Repositório em memória para testes."""

    def __init__(self) -> None:
        self._data: dict[UUID, Fornecedor] = {}

    def save(self, fornecedor: Fornecedor) -> Fornecedor:
        self._data[fornecedor.id] = fornecedor
        return fornecedor

    def get_by_id(self, fornecedor_id: UUID):
        return self._data.get(fornecedor_id)

    def get_by_pessoa_juridica_id(self, pessoa_juridica_id: UUID):
        return next(
            (f for f in self._data.values() if f.pessoa_juridica_id == pessoa_juridica_id),
            None,
        )

    def list(self, situacao=None, include_deleted=False, limit=None, offset=0):
        itens = [
            f
            for f in self._data.values()
            if (include_deleted or not f.foi_excluido())
            and (situacao is None or f.situacao_cadastro == situacao)
        ]
        itens.sort(key=lambda f: f.created_at)
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    def update(self, fornecedor: Fornecedor) -> Fornecedor:
        return self.save(fornecedor)

    def delete(self, fornecedor_id: UUID, usuario_id: UUID) -> None:
        fornecedor = self._data.get(fornecedor_id)
        if fornecedor:
            fornecedor.excluir(usuario_id)

    def exists_pessoa_juridica(self, pessoa_juridica_id: UUID) -> bool:
        return any(f.pessoa_juridica_id == pessoa_juridica_id for f in self._data.values())


@pytest.fixture()
def repository() -> InMemoryFornecedorRepository:
    return InMemoryFornecedorRepository()


# -- Registrar -----------------------------------------------------------------


def test_registrar_fornecedor_sucesso(repository):
    usuario = uuid4()
    command = CriarFornecedorCommand(pessoa_juridica_id=uuid4(), usuario_id=usuario)

    resultado = RegistrarFornecedorUseCase(repository).execute(command)

    assert resultado.id in repository._data  # noqa: SLF001
    assert resultado.situacao_cadastro == SituacaoFornecedor.ATIVO


def test_registrar_fornecedor_duplicado_lanca_erro(repository):
    pessoa_juridica_id = uuid4()
    use_case = RegistrarFornecedorUseCase(repository)

    use_case.execute(CriarFornecedorCommand(pessoa_juridica_id=pessoa_juridica_id))

    with pytest.raises(FornecedorJaCadastradoError):
        use_case.execute(
            CriarFornecedorCommand(
                pessoa_juridica_id=pessoa_juridica_id,
                situacao_cadastro=SituacaoFornecedor.SUSPENSO,
            )
        )


def test_registrar_sem_pessoa_juridica_lanca_erro(repository):
    command = CriarFornecedorCommand(pessoa_juridica_id=None)  # type: ignore[arg-type]

    with pytest.raises(ValueError):
        RegistrarFornecedorUseCase(repository).execute(command)


# -- Consultar / Listar ----------------------------------------------------------


def test_consultar_por_id_sucesso_e_nao_encontrado(repository):
    criado = RegistrarFornecedorUseCase(repository).execute(
        CriarFornecedorCommand(pessoa_juridica_id=uuid4())
    )
    consulta = ConsultarFornecedorUseCase(repository)

    assert consulta.execute(ConsultarFornecedorQuery(fornecedor_id=criado.id)).id == criado.id

    with pytest.raises(FornecedorNaoEncontradoError):
        consulta.execute(ConsultarFornecedorQuery(fornecedor_id=uuid4()))


def test_listar_respeita_paginacao(repository):
    for _ in range(5):
        RegistrarFornecedorUseCase(repository).execute(
            CriarFornecedorCommand(pessoa_juridica_id=uuid4())
        )

    pagina1 = ListarFornecedoresUseCase(repository).execute(
        ListarFornecedoresQuery(page=0, page_size=2)
    )
    pagina2 = ListarFornecedoresUseCase(repository).execute(
        ListarFornecedoresQuery(page=1, page_size=2)
    )

    assert len(pagina1) == 2
    assert len(pagina2) == 2
    assert {f.id for f in pagina1}.isdisjoint({f.id for f in pagina2})


def test_listar_filtra_por_situacao(repository):
    use_case = RegistrarFornecedorUseCase(repository)
    ativo = use_case.execute(CriarFornecedorCommand(pessoa_juridica_id=uuid4()))
    suspenso = use_case.execute(
        CriarFornecedorCommand(
            pessoa_juridica_id=uuid4(), situacao_cadastro=SituacaoFornecedor.SUSPENSO
        )
    )

    resultado = ListarFornecedoresUseCase(repository).execute(
        ListarFornecedoresQuery(situacao=SituacaoFornecedor.SUSPENSO)
    )

    assert [f.id for f in resultado] == [suspenso.id]
    assert ativo.id not in [f.id for f in resultado]


# -- Atualizar / Inativar ----------------------------------------------------------


def test_atualizar_situacao_sucesso(repository):
    usuario = uuid4()
    criado = RegistrarFornecedorUseCase(repository).execute(
        CriarFornecedorCommand(pessoa_juridica_id=uuid4())
    )

    atualizado = AtualizarFornecedorUseCase(repository).execute(
        AtualizarFornecedorCommand(
            fornecedor_id=criado.id,
            situacao_cadastro=SituacaoFornecedor.SUSPENSO,
            usuario_id=usuario,
        )
    )

    assert atualizado.situacao_cadastro == SituacaoFornecedor.SUSPENSO
    assert atualizado.updated_by == usuario


def test_atualizar_inexistente_lanca_erro(repository):
    with pytest.raises(FornecedorNaoEncontradoError):
        AtualizarFornecedorUseCase(repository).execute(
            AtualizarFornecedorCommand(
                fornecedor_id=uuid4(),
                situacao_cadastro=SituacaoFornecedor.INATIVO,
                usuario_id=uuid4(),
            )
        )


def test_inativar_marca_soft_delete(repository):
    usuario = uuid4()
    criado = RegistrarFornecedorUseCase(repository).execute(
        CriarFornecedorCommand(pessoa_juridica_id=uuid4())
    )

    inativado = InativarFornecedorUseCase(repository).execute(
        InativarFornecedorCommand(fornecedor_id=criado.id, usuario_id=usuario)
    )

    assert inativado.situacao_cadastro == SituacaoFornecedor.INATIVO
    assert inativado.foi_excluido() is True

    with pytest.raises(FornecedorNaoEncontradoError):
        ConsultarFornecedorUseCase(repository).execute(
            ConsultarFornecedorQuery(fornecedor_id=criado.id)
        )


def test_inativar_inexistente_lanca_erro(repository):
    with pytest.raises(FornecedorNaoEncontradoError):
        InativarFornecedorUseCase(repository).execute(
            InativarFornecedorCommand(fornecedor_id=uuid4(), usuario_id=uuid4())
        )
