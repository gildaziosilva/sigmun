"""Testes unitários dos casos de uso de Contrato.

Usam um repositório em memória que implementa o contrato do domínio,
validando as regras RN-COMPRAS-036 a 039 sem depender de banco.
"""

from datetime import date
from decimal import Decimal
from typing import List, Optional
from uuid import UUID, uuid4

import pytest

from src.modules.sigmun_compras.application.commands.alterar_situacao_contrato_command import (
    AlterarSituacaoContratoCommand,
)
from src.modules.sigmun_compras.application.commands.atualizar_contrato_command import (
    AtualizarContratoCommand,
)
from src.modules.sigmun_compras.application.commands.criar_contrato_command import (
    CriarContratoCommand,
)
from src.modules.sigmun_compras.application.commands.excluir_contrato_command import (
    ExcluirContratoCommand,
)
from src.modules.sigmun_compras.application.queries.consultar_contrato_query import (
    ConsultarContratoQuery,
)
from src.modules.sigmun_compras.application.queries.listar_contratos_query import (
    ListarContratosQuery,
)
from src.modules.sigmun_compras.application.use_cases.alterar_situacao_contrato import (
    AlterarSituacaoContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_contrato import (
    AtualizarContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_contrato import (
    ConsultarContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_contrato import (
    ExcluirContratoUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_contratos import (
    ListarContratosUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_contrato import (
    RegistrarContratoUseCase,
)
from src.modules.sigmun_compras.domain.entities.contrato import (
    Contrato,
    SituacaoContrato,
)
from src.modules.sigmun_compras.domain.exceptions import (
    ContratoDuplicadoError,
    ContratoNaoEncontradoError,
    FornecedorNaoEncontradoError,
    ProcessoDocumentalNaoEncontradoError,
    UnidadeNaoEncontradaError,
)
from src.modules.sigmun_compras.domain.repositories.contrato_repository import (
    ContratoRepository,
)


class InMemoryContratoRepository(ContratoRepository):
    """Repositório em memória para testes."""

    def __init__(self) -> None:
        self._data: dict[UUID, Contrato] = {}
        self.processos_documentais: set[UUID] = set()
        self.fornecedores_ativos: set[UUID] = set()
        self.unidades: set[UUID] = set()
        self.compras: set[UUID] = set()

    def add_processo_documental(self, pid: UUID) -> None:
        self.processos_documentais.add(pid)

    def add_fornecedor_ativo(self, fid: UUID) -> None:
        self.fornecedores_ativos.add(fid)

    def add_unidade(self, uid: UUID) -> None:
        self.unidades.add(uid)

    def add_compra(self, cid: UUID) -> None:
        self.compras.add(cid)

    def save(self, contrato: Contrato) -> Contrato:
        self._data[contrato.id] = contrato
        return contrato

    def get_by_id(self, contrato_id: UUID) -> Optional[Contrato]:
        return self._data.get(contrato_id)

    def list(
        self,
        situacao: Optional[SituacaoContrato] = None,
        fornecedor_id: Optional[UUID] = None,
        unidade_id: Optional[UUID] = None,
        include_deleted: bool = False,
        limit: Optional[int] = None,
        offset: int = 0,
    ) -> List[Contrato]:
        itens = [
            c
            for c in self._data.values()
            if (include_deleted or not c.foi_excluido())
            and (situacao is None or c.situacao == situacao)
            and (fornecedor_id is None or c.fornecedor_id == fornecedor_id)
            and (unidade_id is None or c.unidade_id == unidade_id)
        ]
        itens.sort(key=lambda c: c.created_at)
        if limit is None:
            return itens[offset:]
        return itens[offset : offset + limit]

    def update(self, contrato: Contrato) -> Contrato:
        return self.save(contrato)

    def delete(self, contrato_id: UUID, usuario_id: UUID) -> None:
        contrato = self._data.get(contrato_id)
        if contrato:
            contrato.excluir(usuario_id)

    def exists_processo_documental(self, processo_documental_id: UUID) -> bool:
        return processo_documental_id in self.processos_documentais

    def exists_fornecedor_ativo(self, fornecedor_id: UUID) -> bool:
        return fornecedor_id in self.fornecedores_ativos

    def exists_unidade(self, unidade_id: UUID) -> bool:
        return unidade_id in self.unidades

    def exists_numero(self, numero: str, excluir_id: Optional[UUID] = None) -> bool:
        return any(
            c.numero == numero
            and not c.foi_excluido()
            and c.id != excluir_id
            for c in self._data.values()
        )

    def exists_compra(self, compra_id: UUID) -> bool:
        return compra_id in self.compras


@pytest.fixture()
def repository() -> InMemoryContratoRepository:
    repo = InMemoryContratoRepository()
    repo.add_processo_documental(uuid4())
    repo.add_fornecedor_ativo(uuid4())
    repo.add_unidade(uuid4())
    return repo


def _command(repo: InMemoryContratoRepository, **overrides) -> CriarContratoCommand:
    dados = {
        "processo_documental_id": next(iter(repo.processos_documentais)),
        "fornecedor_id": next(iter(repo.fornecedores_ativos)),
        "unidade_id": next(iter(repo.unidades)),
        "numero": "001/2026",
        "data_inicio": date(2026, 1, 1),
        "data_fim": date(2026, 12, 31),
        "valor": Decimal("10000.00"),
        "objeto": "Aquisição de serviços",
    }
    dados.update(overrides)
    return CriarContratoCommand(**dados)


# -- Registrar -------------------------------------------------------------------


def test_registrar_contrato_sucesso(repository):
    contrato = RegistrarContratoUseCase(repository).execute(_command(repository))

    assert contrato.id in repository._data  # noqa: SLF001
    assert contrato.numero == "001/2026"
    assert contrato.situacao == SituacaoContrato.EM_ELABORACAO


def test_registrar_contrato_processo_inexistente_lanca_erro():
    repo = InMemoryContratoRepository()
    repo.add_fornecedor_ativo(uuid4())
    repo.add_unidade(uuid4())

    with pytest.raises(ProcessoDocumentalNaoEncontradoError):
        RegistrarContratoUseCase(repo).execute(
            CriarContratoCommand(
                processo_documental_id=uuid4(),
                fornecedor_id=next(iter(repo.fornecedores_ativos)),
                unidade_id=next(iter(repo.unidades)),
                numero="001/2026",
            )
        )


def test_registrar_contrato_fornecedor_inexistente_lanca_erro():
    repo = InMemoryContratoRepository()
    repo.add_processo_documental(uuid4())
    repo.add_unidade(uuid4())

    with pytest.raises(FornecedorNaoEncontradoError):
        RegistrarContratoUseCase(repo).execute(
            CriarContratoCommand(
                processo_documental_id=next(iter(repo.processos_documentais)),
                fornecedor_id=uuid4(),
                unidade_id=next(iter(repo.unidades)),
                numero="001/2026",
            )
        )


def test_registrar_contrato_unidade_inexistente_lanca_erro():
    repo = InMemoryContratoRepository()
    repo.add_processo_documental(uuid4())
    repo.add_fornecedor_ativo(uuid4())

    with pytest.raises(UnidadeNaoEncontradaError):
        RegistrarContratoUseCase(repo).execute(
            CriarContratoCommand(
                processo_documental_id=next(iter(repo.processos_documentais)),
                fornecedor_id=next(iter(repo.fornecedores_ativos)),
                unidade_id=uuid4(),
                numero="001/2026",
            )
        )


def test_registrar_contrato_duplicado_lanca_erro(repository):
    use_case = RegistrarContratoUseCase(repository)
    use_case.execute(_command(repository))

    with pytest.raises(ContratoDuplicadoError):
        use_case.execute(_command(repository, objeto="Outro objeto"))


def test_registrar_contrato_numero_diferente_ok(repository):
    use_case = RegistrarContratoUseCase(repository)
    use_case.execute(_command(repository, numero="001/2026"))
    outro = use_case.execute(_command(repository, numero="002/2026"))

    assert outro.numero == "002/2026"


# -- Consultar / Listar ----------------------------------------------------------


def test_consultar_sucesso_e_nao_encontrado(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))
    use_case = ConsultarContratoUseCase(repository)

    ok = use_case.execute(ConsultarContratoQuery(contrato_id=criado.id))
    assert ok.id == criado.id

    with pytest.raises(ContratoNaoEncontradoError):
        use_case.execute(ConsultarContratoQuery(contrato_id=uuid4()))


def test_consultar_excluido_retorna_404(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))
    repository.delete(criado.id, uuid4())

    with pytest.raises(ContratoNaoEncontradoError):
        ConsultarContratoUseCase(repository).execute(
            ConsultarContratoQuery(contrato_id=criado.id)
        )


def test_listar_com_paginacao_e_filtros(repository):
    unidade_a = next(iter(repository.unidades))
    unidade_b = uuid4()
    repository.add_unidade(unidade_b)
    uc = RegistrarContratoUseCase(repository)
    uc.execute(_command(repository, numero="001/2026", unidade_id=unidade_a))
    uc.execute(_command(repository, numero="002/2026", unidade_id=unidade_a))
    uc.execute(_command(repository, numero="003/2026", unidade_id=unidade_b))

    todos = ListarContratosUseCase(repository).execute(ListarContratosQuery())
    paginado = ListarContratosUseCase(repository).execute(
        ListarContratosQuery(page=0, page_size=2)
    )
    da_unidade_b = ListarContratosUseCase(repository).execute(
        ListarContratosQuery(unidade_id=unidade_b)
    )

    assert len(todos) == 3
    assert len(paginado) == 2
    assert len(da_unidade_b) == 1
    assert da_unidade_b[0].unidade_id == unidade_b


def test_listar_nao_inclui_excluidos_por_padrao(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))
    repository.delete(criado.id, uuid4())

    ativos = repository.list()
    com_excluidos = repository.list(include_deleted=True)

    assert len(ativos) == 0
    assert len(com_excluidos) == 1


# -- Atualizar --------------------------------------------------------------------


def test_atualizar_contrato_sucesso(repository):
    usuario = uuid4()
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    atualizado = AtualizarContratoUseCase(repository).execute(
        AtualizarContratoCommand(
            contrato_id=criado.id,
            numero="002/2026",
            objeto="Objeto alterado",
            valor=Decimal("20000.00"),
            usuario_id=usuario,
        )
    )

    assert atualizado.numero == "002/2026"
    assert atualizado.objeto == "Objeto alterado"
    assert atualizado.valor == Decimal("20000.00")
    assert atualizado.updated_by == usuario


def test_atualizar_contrato_sem_campos_lanca_erro(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError, match="Informe ao menos um campo"):
        AtualizarContratoUseCase(repository).execute(
            AtualizarContratoCommand(contrato_id=criado.id)
        )


def test_atualizar_contrato_para_numero_duplicado_lanca_erro(repository):
    use_case_reg = RegistrarContratoUseCase(repository)
    use_case_reg.execute(_command(repository, numero="001/2026"))
    segundo = use_case_reg.execute(_command(repository, numero="002/2026"))

    with pytest.raises(ContratoDuplicadoError):
        AtualizarContratoUseCase(repository).execute(
            AtualizarContratoCommand(contrato_id=segundo.id, numero="001/2026")
        )


def test_atualizar_contrato_mesmo_numero_ok(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    atualizado = AtualizarContratoUseCase(repository).execute(
        AtualizarContratoCommand(contrato_id=criado.id, numero="001/2026")
    )

    assert atualizado.numero == "001/2026"


def test_atualizar_contrato_inexistente_lanca_erro():
    with pytest.raises(ContratoNaoEncontradoError):
        AtualizarContratoUseCase(InMemoryContratoRepository()).execute(
            AtualizarContratoCommand(contrato_id=uuid4(), numero="001")
        )


def test_atualizar_contrato_valor_negativo_lanca_erro(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError, match="negativo"):
        AtualizarContratoUseCase(repository).execute(
            AtualizarContratoCommand(contrato_id=criado.id, valor=Decimal("-1"))
        )


# -- Excluir ----------------------------------------------------------------------


def test_excluir_contrato_marca_soft_delete(repository):
    usuario = uuid4()
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    excluido = ExcluirContratoUseCase(repository).execute(
        ExcluirContratoCommand(contrato_id=criado.id, usuario_id=usuario)
    )

    assert excluido.foi_excluido() is True
    assert excluido.deleted_by == usuario


def test_excluir_contrato_inexistente_lanca_erro():
    with pytest.raises(ContratoNaoEncontradoError):
        ExcluirContratoUseCase(InMemoryContratoRepository()).execute(
            ExcluirContratoCommand(contrato_id=uuid4(), usuario_id=uuid4())
        )


# -- Alterar situação -------------------------------------------------------------


def test_alterar_situacao_valida(repository):
    usuario = uuid4()
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    result = AlterarSituacaoContratoUseCase(repository).execute(
        AlterarSituacaoContratoCommand(
            contrato_id=criado.id,
            nova_situacao=SituacaoContrato.ASSINADO,
            usuario_id=usuario,
        )
    )

    assert result.situacao == SituacaoContrato.ASSINADO
    assert result.updated_by == usuario


def test_alterar_situacao_invalida_lanca_erro(repository):
    criado = RegistrarContratoUseCase(repository).execute(_command(repository))

    with pytest.raises(ValueError, match="não permitida"):
        AlterarSituacaoContratoUseCase(repository).execute(
            AlterarSituacaoContratoCommand(
                contrato_id=criado.id,
                nova_situacao=SituacaoContrato.VIGENTE,
            )
        )


def test_alterar_situacao_inexistente_lanca_erro():
    with pytest.raises(ContratoNaoEncontradoError):
        AlterarSituacaoContratoUseCase(InMemoryContratoRepository()).execute(
            AlterarSituacaoContratoCommand(
                contrato_id=uuid4(),
                nova_situacao=SituacaoContrato.ASSINADO,
            )
        )
