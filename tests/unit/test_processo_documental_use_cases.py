"""Testes unitários dos casos de uso de Processo Documental.

Usam um repositório em memória que implementa o contrato do domínio,
validando a unicidade (numero, ano) e os vínculos sem depender de banco.
"""

from uuid import UUID, uuid4

import pytest

from src.modules.sigmun_compras.application.commands.atualizar_processo_documental_command import (
    AtualizarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.commands.criar_processo_documental_command import (
    CriarProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_processo_documental_command import (
    ExcluirProcessoDocumentalCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_processo_documental_query import (
    ConsultarProcessoDocumentalQuery,
)
from src.modules.sigmun_compras.application.queries.listar_processos_documentais_query import (
    ListarProcessosDocumentaisQuery,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_processo_documental import (
    AtualizarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_processo_documental import (
    ConsultarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_processo_documental import (
    ExcluirProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_processos_documentais import (
    ListarProcessosDocumentaisUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_processo_documental import (
    RegistrarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.domain.entities.processo_documental import (
    ProcessoDocumental,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ProcessoDocumentalDuplicadoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.processo_documental_repository import (
    ProcessoDocumentalRepository,
)


class InMemoryProcessoRepository(ProcessoDocumentalRepository):
    """Repositório em memória para testes."""

    def __init__(self) -> None:
        self._data: dict[UUID, ProcessoDocumental] = {}
        self.unidades: set[UUID] = set()

    def add_unidade(self, uid: UUID) -> None:
        self.unidades.add(uid)

    def save(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        self._data[processo.id] = processo
        return processo

    def get_by_id(self, processo_id: UUID):
        return self._data.get(processo_id)

    def list(self, unidade_id=None, ano=None, include_deleted=False, limit=None, offset=0):
        itens = [
            p
            for p in self._data.values()
            if (include_deleted or not p.foi_excluido())
            and (unidade_id is None or p.unidade_id == unidade_id)
            and (ano is None or p.ano == ano)
        ]
        itens.sort(key=lambda p: (p.ano, p.numero))
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    def update(self, processo: ProcessoDocumental) -> ProcessoDocumental:
        return self.save(processo)

    def delete(self, processo_id: UUID, usuario_id: UUID) -> None:
        processo = self._data.get(processo_id)
        if processo:
            processo.excluir(usuario_id)

    def exists_unidade(self, uid: UUID) -> bool:
        return uid in self.unidades

    def exists_numero_ano(self, numero: str, ano: int, excluir_id=None) -> bool:
        return any(
            p.numero == numero and p.ano == ano and p.id != excluir_id
            for p in self._data.values()
        )


@pytest.fixture()
def repository() -> InMemoryProcessoRepository:
    repo = InMemoryProcessoRepository()
    repo.add_unidade(uuid4())
    return repo


def _command(repository: InMemoryProcessoRepository, **overrides):
    dados = {
        "unidade_id": next(iter(repository.unidades)),
        "numero": "001",
        "ano": 2026,
        "assunto": "Aquisição de material de escritório",
    }
    dados.update(overrides)
    return CriarProcessoDocumentalCommand(**dados)


def test_registrar_processo_sucesso(repository):
    processo = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))

    assert processo.id in repository._data  # noqa: SLF001
    assert processo.numero == "001"


def test_registrar_processo_unidade_inexistente_lanca_erro():
    repo = InMemoryProcessoRepository()  # nenhuma unidade
    with pytest.raises(UnidadeNaoEncontradaError):
        RegistrarProcessoDocumentalUseCase(repo).execute(
            CriarProcessoDocumentalCommand(
                unidade_id=uuid4(), numero="001", ano=2026, assunto="Assunto qualquer"
            )
        )


def test_registrar_processo_duplicado_lanca_erro(repository):
    use_case = RegistrarProcessoDocumentalUseCase(repository)
    use_case.execute(_command(repository))

    with pytest.raises(ProcessoDocumentalDuplicadoError):
        use_case.execute(_command(repository, assunto="Outro assunto"))


def test_registrar_mesmo_numero_ano_diferente_ok(repository):
    use_case = RegistrarProcessoDocumentalUseCase(repository)
    use_case.execute(_command(repository))

    outro = use_case.execute(_command(repository, ano=2027))

    assert outro.ano == 2027


# -- Consultar / Listar ----------------------------------------------------------


def test_consultar_sucesso_e_nao_encontrado(repository):
    criado = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))
    consulta = ConsultarProcessoDocumentalUseCase(repository)

    ok = consulta.execute(ConsultarProcessoDocumentalQuery(processo_id=criado.id))
    assert ok.id == criado.id

    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        consulta.execute(ConsultarProcessoDocumentalQuery(processo_id=uuid4()))


def test_listar_com_paginacao_e_filtros(repository):
    registrar = RegistrarProcessoDocumentalUseCase(repository)
    unidade_a = next(iter(repository.unidades))
    unidade_b = uuid4()
    repository.add_unidade(unidade_b)

    for n in range(3):
        registrar.execute(
            _command(
                repository,
                unidade_id=unidade_a,
                numero=f"00{n}",
                ano=2026,
                assunto="Assunto padrão",
            )
        )
    registrar.execute(
        _command(repository, unidade_id=unidade_b, ano=2025, assunto="Outra unidade")
    )

    pagina = ListarProcessosDocumentaisUseCase(repository).execute(
        ListarProcessosDocumentaisQuery(page=0, page_size=2)
    )
    da_unidade_b = ListarProcessosDocumentaisUseCase(repository).execute(
        ListarProcessosDocumentaisQuery(unidade_id=unidade_b)
    )
    de_2025 = ListarProcessosDocumentaisUseCase(repository).execute(
        ListarProcessosDocumentaisQuery(ano=2025)
    )

    assert len(pagina) == 2
    assert len(da_unidade_b) == 1
    assert all(p.unidade_id == unidade_b for p in da_unidade_b)
    assert len(de_2025) == 1 and de_2025[0].ano == 2025


# -- Atualizar -----------------------------------------------------------------


def test_atualizar_processo_sucesso(repository):
    usuario = uuid4()
    criado = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))

    atualizado = AtualizarProcessoDocumentalUseCase(repository).execute(
        AtualizarProcessoDocumentalCommand(
            processo_id=criado.id, assunto="Objeto alterado", usuario_id=usuario
        )
    )

    assert atualizado.assunto == "Objeto alterado"
    assert atualizado.updated_by == usuario


def test_atualizar_para_par_duplicado_lanca_erro(repository):
    use_case = RegistrarProcessoDocumentalUseCase(repository)
    primeiro = use_case.execute(_command(repository))
    use_case.execute(_command(repository, numero="002"))

    with pytest.raises(ProcessoDocumentalDuplicadoError):
        AtualizarProcessoDocumentalUseCase(repository).execute(
            AtualizarProcessoDocumentalCommand(
                processo_id=primeiro.id, numero="002"
            )
        )


def test_atualizar_mesmo_registro_mantendo_par_ok(repository):
    criado = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))

    atualizado = AtualizarProcessoDocumentalUseCase(repository).execute(
        AtualizarProcessoDocumentalCommand(processo_id=criado.id, numero="001", ano=2026)
    )

    assert atualizado.numero == "001"


def test_atualizar_sem_campos_lanca_erro(repository):
    criado = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError):
        AtualizarProcessoDocumentalUseCase(repository).execute(
            AtualizarProcessoDocumentalCommand(processo_id=criado.id)
        )


def test_atualizar_inexistente_lanca_erro(repository):
    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        AtualizarProcessoDocumentalUseCase(repository).execute(
            AtualizarProcessoDocumentalCommand(processo_id=uuid4(), assunto="X")
        )


# -- Excluir ---------------------------------------------------------------------


def test_excluir_marca_soft_delete(repository):
    usuario = uuid4()
    criado = RegistrarProcessoDocumentalUseCase(repository).execute(_command(repository))

    excluido = ExcluirProcessoDocumentalUseCase(repository).execute(
        ExcluirProcessoDocumentalCommand(processo_id=criado.id, usuario_id=usuario)
    )

    assert excluido.foi_excluido() is True

    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        ConsultarProcessoDocumentalUseCase(repository).execute(
            ConsultarProcessoDocumentalQuery(processo_id=criado.id)
        )


def test_excluir_inexistente_lanca_erro(repository):
    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        ExcluirProcessoDocumentalUseCase(repository).execute(
            ExcluirProcessoDocumentalCommand(processo_id=uuid4(), usuario_id=uuid4())
        )
