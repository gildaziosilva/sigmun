"""Testes unitários dos casos de uso de Dados Corporativos (DOM-DAD).

Usam repositórios em memória que implementam os contratos do domínio,
validando as regras de negócio sem depender de banco.
"""

from uuid import uuid4

import pytest

from src.modules.sigmun_dad.application.interfaces import (
    AtivoRepositoryInterface,
    CatalogoRepositoryInterface,
    LinhagemRepositoryInterface,
    PoliticaRepositoryInterface,
    QualidadeRepositoryInterface,
)
from src.modules.sigmun_dad.application.use_cases import (
    ArquivarAtivoUseCase,
    AtivarAtivoUseCase,
    AvaliarQualidadeUseCase,
    BuscarAtivoUseCase,
    BuscarCatalogoUseCase,
    BuscarLinhagemUseCase,
    BuscarPoliticaUseCase,
    BuscarQualidadeUseCase,
    CriarAtivoUseCase,
    CriarCatalogoUseCase,
    CriarLinhagemUseCase,
    CriarPoliticaUseCase,
    DeletarCatalogoUseCase,
    DeletarLinhagemUseCase,
    DeletarPoliticaUseCase,
    DeletarQualidadeUseCase,
    DesativarAtivoUseCase,
)
from src.modules.sigmun_dad.domain.entities import (
    AtivoDado,
    Catalogo,
    LinhagemDado,
    PoliticaDado,
    QualidadeDado,
    QualidadeNivel,
    StatusAtivo,
    TipoAtivoDado,
)
from src.modules.sigmun_dad.domain.exceptions import (
    AtivoJaExisteError,
    AtivoNaoEncontradoError,
    CatalogoJaExisteError,
    CatalogoNaoEncontradoError,
    LinhagemJaExisteError,
    LinhagemNaoEncontradaError,
    NomeAtivoInvalidoError,
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
    QualidadeNaoEncontradaError,
)

# =============================================================================
# Repositórios em Memória para Testes
# =============================================================================


class InMemoryAtivoRepository(AtivoRepositoryInterface):
    """Repositório em memória para Ativos de Dados."""

    def __init__(self) -> None:
        self._data: dict[str, AtivoDado] = {}

    def get_by_id(self, ativo_id: str) -> AtivoDado | None:
        return self._data.get(ativo_id)

    def get_by_nome(self, nome: str) -> AtivoDado | None:
        for ativo in self._data.values():
            if ativo.nome == nome:
                return ativo
        return None

    def list_all(self, page=0, page_size=50, tipo=None, status=None):
        itens = [a for a in self._data.values() if not a.is_deleted]
        if tipo:
            itens = [a for a in itens if a.tipo.value == tipo]
        if status:
            itens = [a for a in itens if a.status.value == status]
        return itens[page * page_size : (page + 1) * page_size], len(itens)

    def save(self, ativo: AtivoDado) -> AtivoDado:
        self._data[ativo.id] = ativo
        return ativo

    def delete(self, ativo_id: str) -> bool:
        if ativo_id in self._data:
            self._data[ativo_id].is_deleted = True
            return True
        return False

    def exists_by_nome(self, nome: str) -> bool:
        return any(a.nome == nome for a in self._data.values() if not a.is_deleted)


class InMemoryCatalogoRepository(CatalogoRepositoryInterface):
    """Repositório em memória para Catálogos."""

    def __init__(self) -> None:
        self._data: dict[str, Catalogo] = {}

    def get_by_id(self, catalogo_id: str) -> Catalogo | None:
        return self._data.get(catalogo_id)

    def get_by_nome(self, nome: str) -> Catalogo | None:
        for cat in self._data.values():
            if cat.nome == nome:
                return cat
        return None

    def list_all(self, page=0, page_size=50):
        itens = [c for c in self._data.values() if not c.is_deleted]
        return itens[page * page_size : (page + 1) * page_size], len(itens)

    def save(self, catalogo: Catalogo) -> Catalogo:
        self._data[catalogo.id] = catalogo
        return catalogo

    def delete(self, catalogo_id: str) -> bool:
        if catalogo_id in self._data:
            self._data[catalogo_id].is_deleted = True
            return True
        return False

    def exists_by_nome(self, nome: str) -> bool:
        return any(c.nome == nome for c in self._data.values() if not c.is_deleted)


class InMemoryLinhagemRepository(LinhagemRepositoryInterface):
    """Repositório em memória para Linhagens."""

    def __init__(self) -> None:
        self._data: dict[str, LinhagemDado] = {}

    def get_by_id(self, linhagem_id: str) -> LinhagemDado | None:
        return self._data.get(linhagem_id)

    def get_by_origem(self, ativo_origem_id: str) -> list[LinhagemDado]:
        return [
            linhagem for linhagem in self._data.values()
            if linhagem.ativo_origem_id == ativo_origem_id
        ]

    def get_by_destino(self, ativo_destino_id: str) -> list[LinhagemDado]:
        return [
            linhagem for linhagem in self._data.values()
            if linhagem.ativo_destino_id == ativo_destino_id
        ]

    def list_all(self, page=0, page_size=50):
        itens = [linhagem for linhagem in self._data.values() if not linhagem.is_deleted]
        return itens[page * page_size : (page + 1) * page_size], len(itens)

    def save(self, linhagem: LinhagemDado) -> LinhagemDado:
        self._data[linhagem.id] = linhagem
        return linhagem

    def delete(self, linhagem_id: str) -> bool:
        if linhagem_id in self._data:
            self._data[linhagem_id].is_deleted = True
            return True
        return False

    def exists_linhagem(self, origem_id: str, destino_id: str) -> bool:
        return any(
            linhagem.ativo_origem_id == origem_id and linhagem.ativo_destino_id == destino_id
            for linhagem in self._data.values()
            if not linhagem.is_deleted
        )


class InMemoryPoliticaRepository(PoliticaRepositoryInterface):
    """Repositório em memória para Políticas."""

    def __init__(self) -> None:
        self._data: dict[str, PoliticaDado] = {}

    def get_by_id(self, politica_id: str) -> PoliticaDado | None:
        return self._data.get(politica_id)

    def get_by_codigo(self, codigo: str) -> PoliticaDado | None:
        for p in self._data.values():
            if p.codigo == codigo:
                return p
        return None

    def list_all(self, page=0, page_size=50):
        itens = [p for p in self._data.values() if not p.is_deleted]
        return itens[page * page_size : (page + 1) * page_size], len(itens)

    def save(self, politica: PoliticaDado) -> PoliticaDado:
        self._data[politica.id] = politica
        return politica

    def delete(self, politica_id: str) -> bool:
        if politica_id in self._data:
            self._data[politica_id].is_deleted = True
            return True
        return False

    def exists_by_codigo(self, codigo: str) -> bool:
        return any(p.codigo == codigo for p in self._data.values() if not p.is_deleted)


class InMemoryQualidadeRepository(QualidadeRepositoryInterface):
    """Repositório em memória para Qualidade de Dados."""

    def __init__(self) -> None:
        self._data: dict[str, QualidadeDado] = {}

    def get_by_id(self, qualidade_id: str) -> QualidadeDado | None:
        return self._data.get(qualidade_id)

    def get_by_ativo(self, ativo_id: str) -> QualidadeDado | None:
        for q in self._data.values():
            if q.ativo_id == ativo_id:
                return q
        return None

    def list_all(self, page=0, page_size=50):
        itens = [q for q in self._data.values() if not q.is_deleted]
        return itens[page * page_size : (page + 1) * page_size], len(itens)

    def save(self, qualidade: QualidadeDado) -> QualidadeDado:
        self._data[qualidade.id] = qualidade
        return qualidade

    def delete(self, qualidade_id: str) -> bool:
        if qualidade_id in self._data:
            self._data[qualidade_id].is_deleted = True
            return True
        return False

    def exists_by_ativo(self, ativo_id: str) -> bool:
        return any(q.ativo_id == ativo_id for q in self._data.values() if not q.is_deleted)


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def ativo_repo():
    return InMemoryAtivoRepository()


@pytest.fixture
def catalogo_repo():
    return InMemoryCatalogoRepository()


@pytest.fixture
def linhagem_repo():
    return InMemoryLinhagemRepository()


@pytest.fixture
def politica_repo():
    return InMemoryPoliticaRepository()


@pytest.fixture
def qualidade_repo():
    return InMemoryQualidadeRepository()


# =============================================================================
# Testes de Ativos de Dados
# =============================================================================


class TestCriarAtivoUseCase:
    def test_criar_ativo_sucesso(self, ativo_repo):
        use_case = CriarAtivoUseCase(ativo_repo)
        ativo = use_case.execute(
            nome="Clientes",
            descricao="Dados de clientes",
            tipo="tabela",
        )
        assert ativo.nome == "Clientes"
        assert ativo.tipo == TipoAtivoDado.TABELA
        assert ativo.status == StatusAtivo.PENDENTE

    def test_criar_ativo_nome_duplicado_lanca_erro(self, ativo_repo):
        use_case = CriarAtivoUseCase(ativo_repo)
        use_case.execute(nome="Clientes", descricao="", tipo="tabela")
        with pytest.raises(AtivoJaExisteError):
            use_case.execute(nome="Clientes", descricao="", tipo="tabela")

    def test_criar_ativo_nome_invalido_lanca_erro(self, ativo_repo):
        use_case = CriarAtivoUseCase(ativo_repo)
        with pytest.raises(NomeAtivoInvalidoError):
            use_case.execute(nome="AB", descricao="", tipo="tabela")


class TestAtivarAtivoUseCase:
    def test_ativar_ativo_sucesso(self, ativo_repo):
        criado = CriarAtivoUseCase(ativo_repo).execute(nome="Teste", descricao="", tipo="tabela")
        ativado = AtivarAtivoUseCase(ativo_repo).execute(criado.id)
        assert ativado.status == StatusAtivo.ATIVO

    def test_ativar_ativo_inexistente_lanca_erro(self, ativo_repo):
        with pytest.raises(AtivoNaoEncontradoError):
            AtivarAtivoUseCase(ativo_repo).execute(str(uuid4()))


class TestDesativarAtivoUseCase:
    def test_desativar_ativo_sucesso(self, ativo_repo):
        criado = CriarAtivoUseCase(ativo_repo).execute(nome="Teste", descricao="", tipo="tabela")
        DesativarAtivoUseCase(ativo_repo).execute(criado.id)
        buscado = BuscarAtivoUseCase(ativo_repo).get_by_id(criado.id)
        assert buscado.status == StatusAtivo.INATIVO


class TestArquivarAtivoUseCase:
    def test_arquivar_ativo_sucesso(self, ativo_repo):
        criado = CriarAtivoUseCase(ativo_repo).execute(nome="Teste", descricao="", tipo="tabela")
        arquivado = ArquivarAtivoUseCase(ativo_repo).execute(criado.id)
        assert arquivado.status == StatusAtivo.ARQUIVADO


class TestBuscarAtivoUseCase:
    def test_buscar_ativo_por_id(self, ativo_repo):
        criado = CriarAtivoUseCase(ativo_repo).execute(nome="Teste", descricao="", tipo="tabela")
        buscado = BuscarAtivoUseCase(ativo_repo).get_by_id(criado.id)
        assert buscado.id == criado.id

    def test_buscar_ativo_inexistente_lanca_erro(self, ativo_repo):
        with pytest.raises(AtivoNaoEncontradoError):
            BuscarAtivoUseCase(ativo_repo).get_by_id(str(uuid4()))

    def test_listar_ativos(self, ativo_repo):
        CriarAtivoUseCase(ativo_repo).execute(nome="Ativo1", descricao="", tipo="tabela")
        CriarAtivoUseCase(ativo_repo).execute(nome="Ativo2", descricao="", tipo="tabela")
        itens, total = BuscarAtivoUseCase(ativo_repo).list_all()
        assert total == 2


# =============================================================================
# Testes de Catálogos
# =============================================================================


class TestCriarCatalogoUseCase:
    def test_criar_catalogo_sucesso(self, catalogo_repo):
        use_case = CriarCatalogoUseCase(catalogo_repo)
        catalogo = use_case.execute(nome="Catálogo RH", descricao="Dados de RH")
        assert catalogo.nome == "Catálogo RH"

    def test_criar_catalogo_nome_duplicado_lanca_erro(self, catalogo_repo):
        use_case = CriarCatalogoUseCase(catalogo_repo)
        use_case.execute(nome="Catálogo RH", descricao="")
        with pytest.raises(CatalogoJaExisteError):
            use_case.execute(nome="Catálogo RH", descricao="")


class TestBuscarCatalogoUseCase:
    def test_buscar_catalogo_por_id(self, catalogo_repo):
        criado = CriarCatalogoUseCase(catalogo_repo).execute(nome="Teste", descricao="")
        buscado = BuscarCatalogoUseCase(catalogo_repo).get_by_id(criado.id)
        assert buscado.id == criado.id

    def test_buscar_catalogo_inexistente_lanca_erro(self, catalogo_repo):
        with pytest.raises(CatalogoNaoEncontradoError):
            BuscarCatalogoUseCase(catalogo_repo).get_by_id(str(uuid4()))


class TestDeletarCatalogoUseCase:
    def test_deletar_catalogo_sucesso(self, catalogo_repo):
        criado = CriarCatalogoUseCase(catalogo_repo).execute(nome="Teste", descricao="")
        assert DeletarCatalogoUseCase(catalogo_repo).execute(criado.id) is True

    def test_deletar_catalogo_inexistente_lanca_erro(self, catalogo_repo):
        with pytest.raises(CatalogoNaoEncontradoError):
            DeletarCatalogoUseCase(catalogo_repo).execute(str(uuid4()))


# =============================================================================
# Testes de Linhagens
# =============================================================================


class TestCriarLinhagemUseCase:
    def test_criar_linhagem_sucesso(self, linhagem_repo):
        use_case = CriarLinhagemUseCase(linhagem_repo)
        origem = str(uuid4())
        destino = str(uuid4())
        linhagem = use_case.execute(ativo_origem_id=origem, ativo_destino_id=destino)
        assert linhagem.ativo_origem_id == origem
        assert linhagem.ativo_destino_id == destino

    def test_criar_linhagem_duplicada_lanca_erro(self, linhagem_repo):
        use_case = CriarLinhagemUseCase(linhagem_repo)
        origem = str(uuid4())
        destino = str(uuid4())
        use_case.execute(ativo_origem_id=origem, ativo_destino_id=destino)
        with pytest.raises(LinhagemJaExisteError):
            use_case.execute(ativo_origem_id=origem, ativo_destino_id=destino)

    def test_criar_linhagem_mesmo_ativo_lanca_erro(self, linhagem_repo):
        use_case = CriarLinhagemUseCase(linhagem_repo)
        mesmo_id = str(uuid4())
        with pytest.raises(ValueError):
            use_case.execute(ativo_origem_id=mesmo_id, ativo_destino_id=mesmo_id)


class TestBuscarLinhagemUseCase:
    def test_buscar_linhagem_por_id(self, linhagem_repo):
        criado = CriarLinhagemUseCase(linhagem_repo).execute(
            ativo_origem_id=str(uuid4()), ativo_destino_id=str(uuid4()))
        buscado = BuscarLinhagemUseCase(linhagem_repo).get_by_id(criado.id)
        assert buscado.id == criado.id

    def test_buscar_linhagem_inexistente_lanca_erro(self, linhagem_repo):
        with pytest.raises(LinhagemNaoEncontradaError):
            BuscarLinhagemUseCase(linhagem_repo).get_by_id(str(uuid4()))


class TestDeletarLinhagemUseCase:
    def test_deletar_linhagem_sucesso(self, linhagem_repo):
        criado = CriarLinhagemUseCase(linhagem_repo).execute(
            ativo_origem_id=str(uuid4()), ativo_destino_id=str(uuid4()))
        assert DeletarLinhagemUseCase(linhagem_repo).execute(criado.id) is True

    def test_deletar_linhagem_inexistente_lanca_erro(self, linhagem_repo):
        with pytest.raises(LinhagemNaoEncontradaError):
            DeletarLinhagemUseCase(linhagem_repo).execute(str(uuid4()))


# =============================================================================
# Testes de Políticas
# =============================================================================


class TestCriarPoliticaUseCase:
    def test_criar_politica_sucesso(self, politica_repo):
        use_case = CriarPoliticaUseCase(politica_repo)
        politica = use_case.execute(
            codigo="POL-001",
            nome="Política de Privacidade",
            descricao="Regras de privacidade",
        )
        assert politica.codigo == "POL-001"
        assert politica.nome == "Política de Privacidade"

    def test_criar_politica_codigo_duplicado_lanca_erro(self, politica_repo):
        use_case = CriarPoliticaUseCase(politica_repo)
        use_case.execute(codigo="POL-001", nome="Política 1")
        with pytest.raises(PoliticaJaExisteError):
            use_case.execute(codigo="POL-001", nome="Política 2")


class TestBuscarPoliticaUseCase:
    def test_buscar_politica_por_id(self, politica_repo):
        criado = CriarPoliticaUseCase(politica_repo).execute(codigo="POL-001", nome="Teste")
        buscado = BuscarPoliticaUseCase(politica_repo).get_by_id(criado.id)
        assert buscado.id == criado.id

    def test_buscar_politica_por_codigo(self, politica_repo):
        criado = CriarPoliticaUseCase(politica_repo).execute(codigo="POL-001", nome="Teste")
        buscado = BuscarPoliticaUseCase(politica_repo).get_by_codigo("POL-001")
        assert buscado.id == criado.id

    def test_buscar_politica_inexistente_lanca_erro(self, politica_repo):
        with pytest.raises(PoliticaNaoEncontradaError):
            BuscarPoliticaUseCase(politica_repo).get_by_id(str(uuid4()))


class TestDeletarPoliticaUseCase:
    def test_deletar_politica_sucesso(self, politica_repo):
        criado = CriarPoliticaUseCase(politica_repo).execute(codigo="POL-001", nome="Teste")
        assert DeletarPoliticaUseCase(politica_repo).execute(criado.id) is True

    def test_deletar_politica_inexistente_lanca_erro(self, politica_repo):
        with pytest.raises(PoliticaNaoEncontradaError):
            DeletarPoliticaUseCase(politica_repo).execute(str(uuid4()))


# =============================================================================
# Testes de Qualidade de Dados
# =============================================================================


class TestAvaliarQualidadeUseCase:
    def test_avaliar_qualidade_sucesso(self, qualidade_repo):
        use_case = AvaliarQualidadeUseCase(qualidade_repo)
        ativo_id = str(uuid4())
        qualidade = use_case.execute(ativo_id=ativo_id, score=85.0)
        assert qualidade.ativo_id == ativo_id
        assert qualidade.score == 85.0
        assert qualidade.nivel == QualidadeNivel.ALTO

    def test_avaliar_qualidade_score_invalido_lanca_erro(self, qualidade_repo):
        use_case = AvaliarQualidadeUseCase(qualidade_repo)
        with pytest.raises(ValueError):
            use_case.execute(ativo_id=str(uuid4()), score=150.0)


class TestBuscarQualidadeUseCase:
    def test_buscar_qualidade_por_id(self, qualidade_repo):
        criado = AvaliarQualidadeUseCase(qualidade_repo).execute(
            ativo_id=str(uuid4()), score=80.0)
        buscado = BuscarQualidadeUseCase(qualidade_repo).get_by_id(criado.id)
        assert buscado.id == criado.id

    def test_buscar_qualidade_por_ativo(self, qualidade_repo):
        ativo_id = str(uuid4())
        AvaliarQualidadeUseCase(qualidade_repo).execute(ativo_id=ativo_id, score=80.0)
        buscado = BuscarQualidadeUseCase(qualidade_repo).get_by_ativo(ativo_id)
        assert buscado.ativo_id == ativo_id

    def test_buscar_qualidade_inexistente_lanca_erro(self, qualidade_repo):
        with pytest.raises(QualidadeNaoEncontradaError):
            BuscarQualidadeUseCase(qualidade_repo).get_by_id(str(uuid4()))


class TestDeletarQualidadeUseCase:
    def test_deletar_qualidade_sucesso(self, qualidade_repo):
        criado = AvaliarQualidadeUseCase(qualidade_repo).execute(
            ativo_id=str(uuid4()), score=80.0)
        assert DeletarQualidadeUseCase(qualidade_repo).execute(criado.id) is True

    def test_deletar_qualidade_inexistente_lanca_erro(self, qualidade_repo):
        with pytest.raises(QualidadeNaoEncontradaError):
            DeletarQualidadeUseCase(qualidade_repo).execute(str(uuid4()))
