"""Testes unitários dos casos de uso do módulo de Metadados Corporativos (DOM-MET)."""

import pytest

from src.modules.sigmun_met.application.interfaces import (
    ClassificacaoRepositoryInterface,
    MetadadoRepositoryInterface,
    TaxonomiaRepositoryInterface,
    TermoTaxonomiaRepositoryInterface,
    ValorMetadadoRepositoryInterface,
)
from src.modules.sigmun_met.application.use_cases import (
    AtivarMetadadoUseCase,
    AtribuirValorMetadadoUseCase,
    AtualizarClassificacaoUseCase,
    AtualizarMetadadoUseCase,
    AtualizarTaxonomiaUseCase,
    AtualizarTermoUseCase,
    BuscarClassificacaoUseCase,
    BuscarMetadadoUseCase,
    BuscarTaxonomiaUseCase,
    BuscarTermoUseCase,
    BuscarValorMetadadoUseCase,
    CriarClassificacaoUseCase,
    CriarMetadadoUseCase,
    CriarTaxonomiaUseCase,
    CriarTermoUseCase,
    DeletarClassificacaoUseCase,
    DeletarMetadadoUseCase,
    DeletarTaxonomiaUseCase,
    DeletarTermoUseCase,
    DesativarMetadadoUseCase,
    RemoverValorMetadadoUseCase,
    ValidarValorMetadadoUseCase,
)
from src.modules.sigmun_met.domain.exceptions import (
    ClassificacaoJaExisteError,
    ClassificacaoNaoEncontradaError,
    CodigoInvalidoError,
    MetadadoJaExisteError,
    MetadadoNaoEncontradoError,
    TaxonomiaJaExisteError,
    TaxonomiaNaoEncontradaError,
    TermoJaExisteError,
    TermoNaoEncontradoError,
    ValorMetadadoInvalidoError,
    ValorMetadadoNaoEncontradoError,
)

# =============================================================================
# Repositórios em memória
# =============================================================================


class _FakeBaseRepository:
    """Armazenamento em memória compartilhado pelos repositórios falsos."""

    def __init__(self):
        self._data: dict[str, object] = {}

    def get_by_id(self, entity_id: str):
        return self._data.get(entity_id)

    def save(self, entity):
        self._data[entity.id] = entity
        return entity

    def delete(self, entity_id: str) -> bool:
        return self._data.pop(entity_id, None) is not None

    def list_all(self, page: int = 0, page_size: int = 50):
        items = list(self._data.values())
        return items[page * page_size:(page + 1) * page_size], len(items)


class FakeMetadadoRepository(_FakeBaseRepository, MetadadoRepositoryInterface):
    def get_by_codigo(self, codigo: str):
        return next((m for m in self._data.values() if m.codigo == codigo), None)

    def list_all(self, page=0, page_size=50, status=None, tipo_dado=None):
        items = list(self._data.values())
        if status:
            items = [m for m in items if m.status.value == status]
        if tipo_dado:
            items = [m for m in items if m.tipo_dado.value == tipo_dado]
        return items[page * page_size:(page + 1) * page_size], len(items)

    def exists_by_codigo(self, codigo: str) -> bool:
        return any(m.codigo == codigo for m in self._data.values())


class FakeValorMetadadoRepository(_FakeBaseRepository, ValorMetadadoRepositoryInterface):
    def get_by_entidade(self, entidade_tipo: str, entidade_id: str):
        return [
            v for v in self._data.values()
            if v.entidade_tipo == entidade_tipo and v.entidade_id == entidade_id
        ]

    def get_by_metadado_e_entidade(self, metadado_id: str, entidade_tipo: str, entidade_id: str):
        return next(
            (
                v for v in self._data.values()
                if v.metadado_id == metadado_id
                and v.entidade_tipo == entidade_tipo
                and v.entidade_id == entidade_id
            ),
            None,
        )

    def list_all(self, page=0, page_size=50, metadado_id=None, entidade_tipo=None):
        items = list(self._data.values())
        if metadado_id:
            items = [v for v in items if v.metadado_id == metadado_id]
        if entidade_tipo:
            items = [v for v in items if v.entidade_tipo == entidade_tipo]
        return items[page * page_size:(page + 1) * page_size], len(items)


class FakeClassificacaoRepository(_FakeBaseRepository, ClassificacaoRepositoryInterface):
    def get_by_codigo(self, codigo: str):
        return next((c for c in self._data.values() if c.codigo == codigo), None)

    def list_all(self, page=0, page_size=50, tipo=None):
        items = list(self._data.values())
        if tipo:
            items = [c for c in items if c.tipo.value == tipo]
        return items[page * page_size:(page + 1) * page_size], len(items)

    def exists_by_codigo(self, codigo: str) -> bool:
        return any(c.codigo == codigo for c in self._data.values())


class FakeTaxonomiaRepository(_FakeBaseRepository, TaxonomiaRepositoryInterface):
    def get_by_codigo(self, codigo: str):
        return next((t for t in self._data.values() if t.codigo == codigo), None)

    def exists_by_codigo(self, codigo: str) -> bool:
        return any(t.codigo == codigo for t in self._data.values())


class FakeTermoRepository(_FakeBaseRepository, TermoTaxonomiaRepositoryInterface):
    def get_by_taxonomia(self, taxonomia_id: str):
        return [t for t in self._data.values() if t.taxonomia_id == taxonomia_id]

    def get_by_pai(self, termo_pai_id: str):
        return [t for t in self._data.values() if t.termo_pai_id == termo_pai_id]

    def list_all(self, page=0, page_size=50, taxonomia_id=None):
        items = list(self._data.values())
        if taxonomia_id:
            items = [t for t in items if t.taxonomia_id == taxonomia_id]
        return items[page * page_size:(page + 1) * page_size], len(items)



# =============================================================================
# Testes de Metadados
# =============================================================================


class TestCriarMetadadoUseCase:
    def test_cria_metadado_com_sucesso(self):
        repo = FakeMetadadoRepository()
        metadado = CriarMetadadoUseCase(repo).execute(
            codigo="orgaoresponsavel",
            nome="Orgao Responsavel",
            descricao="Orgao responsavel pelo dado",
            tipo_dado="texto",
        )
        assert metadado.id
        assert metadado.codigo == "orgaoresponsavel"
        assert metadado.tipo_dado.value == "texto"
        assert metadado.status.value == "ativo"

    def test_codigo_invalido_levanta_erro(self):
        use_case = CriarMetadadoUseCase(FakeMetadadoRepository())
        with pytest.raises(CodigoInvalidoError):
            use_case.execute(codigo="1-invalido", nome="Nome Valido")

    def test_codigo_duplicado_levanta_erro(self):
        repo = FakeMetadadoRepository()
        CriarMetadadoUseCase(repo).execute(codigo="orgao", nome="Orgao")
        with pytest.raises(MetadadoJaExisteError):
            CriarMetadadoUseCase(repo).execute(codigo="orgao", nome="Outro")


class TestAtualizarBuscarMetadadoUseCase:
    def test_atualiza_campos(self):
        repo = FakeMetadadoRepository()
        criado = CriarMetadadoUseCase(repo).execute(codigo="campo", nome="Campo X")
        atualizado = AtualizarMetadadoUseCase(repo).execute(
            criado.id, nome="Campo Y", descricao="Nova descricao"
        )
        assert atualizado.nome == "Campo Y"
        assert atualizado.descricao == "Nova descricao"

    def test_atualizar_inexistente_levanta_erro(self):
        use_case = AtualizarMetadadoUseCase(FakeMetadadoRepository())
        with pytest.raises(MetadadoNaoEncontradoError):
            use_case.execute("id-inexistente", nome="Novo")

    def test_busca_por_id_e_codigo(self):
        repo = FakeMetadadoRepository()
        criado = CriarMetadadoUseCase(repo).execute(codigo="busca", nome="Busca Teste")
        buscar = BuscarMetadadoUseCase(repo)
        assert buscar.get_by_id(criado.id).codigo == "busca"
        assert buscar.get_by_codigo("busca").id == criado.id

    def test_buscar_inexistente_levanta_erro(self):
        buscar = BuscarMetadadoUseCase(FakeMetadadoRepository())
        with pytest.raises(MetadadoNaoEncontradoError):
            buscar.get_by_id("nada")

    def test_listar_com_filtro_tipo(self):
        repo = FakeMetadadoRepository()
        criar = CriarMetadadoUseCase(repo)
        criar.execute(codigo="mtexto", nome="Metadado Texto", tipo_dado="texto")
        criar.execute(codigo="mnum", nome="Metadado Numero", tipo_dado="numero")
        items, total = BuscarMetadadoUseCase(repo).list_all(tipo_dado="numero")
        assert total == 1
        assert items[0].codigo == "mnum"


class TestAtivarDesativarDeletarMetadadoUseCase:
    def test_desativar_e_ativar(self):
        repo = FakeMetadadoRepository()
        criado = CriarMetadadoUseCase(repo).execute(codigo="ciclo", nome="Ciclo")
        DesativarMetadadoUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).status.value == "inativo"
        AtivarMetadadoUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).status.value == "ativo"

    def test_desativar_inexistente_levanta_erro(self):
        with pytest.raises(MetadadoNaoEncontradoError):
            DesativarMetadadoUseCase(FakeMetadadoRepository()).execute("nada")

    def test_deletar(self):
        repo = FakeMetadadoRepository()
        criado = CriarMetadadoUseCase(repo).execute(codigo="remover", nome="Remover")
        assert DeletarMetadadoUseCase(repo).execute(criado.id) is True
        assert repo.get_by_id(criado.id) is None
        with pytest.raises(MetadadoNaoEncontradoError):
            DeletarMetadadoUseCase(repo).execute(criado.id)


# =============================================================================
# Testes de Valores de Metadado
# =============================================================================


def _repo_com_metadado(tipo="texto"):
    """Cria (metadado_repo, metadado) com um metadado salvo."""
    metadado_repo = FakeMetadadoRepository()
    metadado = CriarMetadadoUseCase(metadado_repo).execute(
        codigo="campo", nome="Campo", tipo_dado=tipo
    )
    return metadado_repo, metadado


class TestAtribuirValorMetadadoUseCase:
    def test_atribui_novo_valor(self):
        metadado_repo, metadado = _repo_com_metadado()
        valor_repo = FakeValorMetadadoRepository()
        resultado = AtribuirValorMetadadoUseCase(valor_repo, metadado_repo).execute(
            metadado.id,
            "ativo",
            "11111111-1111-1111-1111-111111111111",
            "Prefeitura",
        )
        assert resultado.valor == "Prefeitura"
        assert resultado.metadado_id == metadado.id

    def test_atualiza_valor_existente(self):
        metadado_repo, metadado = _repo_com_metadado()
        valor_repo = FakeValorMetadadoRepository()
        use_case = AtribuirValorMetadadoUseCase(valor_repo, metadado_repo)
        entidade_id = "22222222-2222-2222-2222-222222222222"
        use_case.execute(metadado.id, "ativo", entidade_id, "v1")
        resultado = use_case.execute(metadado.id, "ativo", entidade_id, "v2")
        assert resultado.valor == "v2"
        _, total = valor_repo.list_all()
        assert total == 1

    def test_valor_invalido_para_tipo_numero(self):
        metadado_repo, metadado = _repo_com_metadado(tipo="numero")
        use_case = AtribuirValorMetadadoUseCase(
            FakeValorMetadadoRepository(), metadado_repo
        )
        with pytest.raises(ValorMetadadoInvalidoError):
            use_case.execute(
                metadado.id, "ativo", "33333333-3333-3333-3333-333333333333", "abc"
            )

    def test_metadado_inexistente_levanta_erro(self):
        use_case = AtribuirValorMetadadoUseCase(
            FakeValorMetadadoRepository(), FakeMetadadoRepository()
        )
        with pytest.raises(MetadadoNaoEncontradoError):
            use_case.execute(
                "nada", "ativo", "44444444-4444-4444-4444-444444444444", "x"
            )

    def test_entidade_tipo_invalida_levanta_erro(self):
        metadado_repo, metadado = _repo_com_metadado()
        use_case = AtribuirValorMetadadoUseCase(
            FakeValorMetadadoRepository(), metadado_repo
        )
        with pytest.raises(ValueError, match="Entidade alvo inválida"):
            use_case.execute(
                metadado.id,
                "Tipo-Invalido",
                "55555555-5555-5555-5555-555555555555",
                "x",
            )


class TestBuscarRemoverValidarValorUseCase:
    def test_busca_por_entidade(self):
        metadado_repo, metadado = _repo_com_metadado()
        valor_repo = FakeValorMetadadoRepository()
        use_case = AtribuirValorMetadadoUseCase(valor_repo, metadado_repo)
        entidade_id = "66666666-6666-6666-6666-666666666666"
        use_case.execute(metadado.id, "ativo", entidade_id, "valor-a")
        valores = BuscarValorMetadadoUseCase(valor_repo).get_by_entidade(
            "ativo", entidade_id
        )
        assert len(valores) == 1
        assert valores[0].valor == "valor-a"

    def test_remover_valor(self):
        metadado_repo, metadado = _repo_com_metadado()
        valor_repo = FakeValorMetadadoRepository()
        atribuido = AtribuirValorMetadadoUseCase(valor_repo, metadado_repo).execute(
            metadado.id, "ativo", "77777777-7777-7777-7777-777777777777", "v"
        )
        assert RemoverValorMetadadoUseCase(valor_repo).execute(atribuido.id) is True
        with pytest.raises(ValorMetadadoNaoEncontradoError):
            BuscarValorMetadadoUseCase(valor_repo).get_by_id(atribuido.id)

    def test_validar_valor_valido_e_invalido(self):
        metadado_repo, metadado = _repo_com_metadado(tipo="numero")
        validar = ValidarValorMetadadoUseCase(metadado_repo)
        assert validar.execute(metadado.id, "1234.56") is True
        with pytest.raises(ValorMetadadoInvalidoError):
            validar.execute(metadado.id, "não-numero")
        repo = FakeMetadadoRepository()
        CriarMetadadoUseCase(repo).execute(codigo="del", nome="Deletavel")


# =============================================================================
# Testes de Classificações
# =============================================================================


class TestClassificacaoUseCases:
    def test_cria_classificacao(self):
        repo = FakeClassificacaoRepository()
        criada = CriarClassificacaoUseCase(repo).execute(
            codigo="publico", nome="Público", tipo="confidencialidade", nivel=1
        )
        assert criada.codigo == "publico"
        assert criada.nivel == 1

    def test_codigo_duplicado_levanta_erro(self):
        repo = FakeClassificacaoRepository()
        CriarClassificacaoUseCase(repo).execute(codigo="sigiloso", nome="Sigiloso")
        with pytest.raises(ClassificacaoJaExisteError):
            CriarClassificacaoUseCase(repo).execute(codigo="sigiloso", nome="Outro")

    def test_atualizar_e_buscar(self):
        repo = FakeClassificacaoRepository()
        criada = CriarClassificacaoUseCase(repo).execute(
            codigo="interno", nome="Interno"
        )
        atualizada = AtualizarClassificacaoUseCase(repo).execute(
            criada.id, nome="Interno Uso", nivel=2
        )
        assert atualizada.nome == "Interno Uso"
        assert atualizada.nivel == 2
        busca = BuscarClassificacaoUseCase(repo)
        assert busca.get_by_id(criada.id).codigo == "interno"
        assert busca.get_by_codigo("interno").id == criada.id

    def test_buscar_inexistente_levanta_erro(self):
        with pytest.raises(ClassificacaoNaoEncontradaError):
            BuscarClassificacaoUseCase(FakeClassificacaoRepository()).get_by_id("nada")

    def test_deletar(self):
        repo = FakeClassificacaoRepository()
        criada = CriarClassificacaoUseCase(repo).execute(
            codigo="temporario", nome="Temporário"
        )
        assert DeletarClassificacaoUseCase(repo).execute(criada.id) is True
        assert repo.get_by_id(criada.id) is None

    def test_listar_com_filtro_tipo(self):
        repo = FakeClassificacaoRepository()
        criar = CriarClassificacaoUseCase(repo)
        criar.execute(codigo="conf", nome="Confidencial", tipo="confidencialidade")
        criar.execute(codigo="assunto", nome="Assunto", tipo="assunto")
        _, total = BuscarClassificacaoUseCase(repo).list_all(tipo="assunto")
        assert total == 1


# =============================================================================
# Testes de Taxonomias
# =============================================================================


class TestTaxonomiaUseCases:
    def test_cria_taxonomia(self):
        repo = FakeTaxonomiaRepository()
        criada = CriarTaxonomiaUseCase(repo).execute(
            codigo="assuntos", nome="Assuntos Municipais"
        )
        assert criada.codigo == "assuntos"
        assert criada.termos_ids == []

    def test_codigo_duplicado_levanta_erro(self):
        repo = FakeTaxonomiaRepository()
        CriarTaxonomiaUseCase(repo).execute(codigo="temas", nome="Temas")
        with pytest.raises(TaxonomiaJaExisteError):
            CriarTaxonomiaUseCase(repo).execute(codigo="temas", nome="Outro")

    def test_atualizar_e_buscar(self):
        repo = FakeTaxonomiaRepository()
        criada = CriarTaxonomiaUseCase(repo).execute(
            codigo="estrutura", nome="Estrutura"
        )
        atualizada = AtualizarTaxonomiaUseCase(repo).execute(
            criada.id, nome="Estrutura Organizacional", descricao="Desc"
        )
        assert atualizada.nome == "Estrutura Organizacional"
        busca = BuscarTaxonomiaUseCase(repo)
        assert busca.get_by_id(criada.id).codigo == "estrutura"
        assert busca.get_by_codigo("estrutura").id == criada.id

    def test_buscar_inexistente_levanta_erro(self):
        with pytest.raises(TaxonomiaNaoEncontradaError):
            BuscarTaxonomiaUseCase(FakeTaxonomiaRepository()).get_by_id("nada")

    def test_deletar(self):
        repo = FakeTaxonomiaRepository()
        criada = CriarTaxonomiaUseCase(repo).execute(
            codigo="apagar", nome="Para Apagar"
        )
        assert DeletarTaxonomiaUseCase(repo).execute(criada.id) is True
        assert repo.get_by_id(criada.id) is None


# =============================================================================
# Testes de Termos de Taxonomia
# =============================================================================


def _taxonomia_com_repo():
    repo = FakeTaxonomiaRepository()
    taxonomia = CriarTaxonomiaUseCase(repo).execute(
        codigo="orgchart", nome="Organograma"
    )
    return repo, taxonomia


class TestTermoUseCases:
    def test_cria_termo_raiz_e_filho(self):
        tax_repo, taxonomia = _taxonomia_com_repo()
        termo_repo = FakeTermoRepository()
        criar = CriarTermoUseCase(termo_repo, tax_repo)
        raiz = criar.execute(
            taxonomia_id=taxonomia.id, codigo="gabinete", nome="Gabinete"
        )
        assert raiz.termo_pai_id == ""
        filho = criar.execute(
            taxonomia_id=taxonomia.id,
            codigo="assessoria",
            nome="Assessoria",
            termo_pai_id=raiz.id,
        )
        assert filho.termo_pai_id == raiz.id

    def test_taxonomia_inexistente_levanta_erro(self):
        use_case = CriarTermoUseCase(FakeTermoRepository(), FakeTaxonomiaRepository())
        with pytest.raises(TaxonomiaNaoEncontradaError):
            use_case.execute(taxonomia_id="nada", codigo="termo", nome="Termo")

    def test_codigo_duplicado_na_taxonomia_levanta_erro(self):
        tax_repo, taxonomia = _taxonomia_com_repo()
        termo_repo = FakeTermoRepository()
        criar = CriarTermoUseCase(termo_repo, tax_repo)
        criar.execute(taxonomia_id=taxonomia.id, codigo="repetido", nome="Primeiro")
        with pytest.raises(TermoJaExisteError):
            criar.execute(
                taxonomia_id=taxonomia.id, codigo="repetido", nome="Segundo"
            )

    def test_atualizar_termo(self):
        tax_repo, taxonomia = _taxonomia_com_repo()
        termo_repo = FakeTermoRepository()
        criado = CriarTermoUseCase(termo_repo, tax_repo).execute(
            taxonomia_id=taxonomia.id, codigo="setor", nome="Setor"
        )
        atualizado = AtualizarTermoUseCase(termo_repo).execute(
            criado.id, nome="Novo Setor", sinonimos=["departamento"]
        )
        assert atualizado.nome == "Novo Setor"
        assert atualizado.sinonimos == ["departamento"]

    def test_buscar_filhos_e_por_taxonomia(self):
        tax_repo, taxonomia = _taxonomia_com_repo()
        termo_repo = FakeTermoRepository()
        criar = CriarTermoUseCase(termo_repo, tax_repo)
        raiz = criar.execute(
            taxonomia_id=taxonomia.id, codigo="raiz", nome="Raiz"
        )
        criar.execute(
            taxonomia_id=taxonomia.id,
            codigo="filho1",
            nome="Filho Um",
            termo_pai_id=raiz.id,
        )
        criar.execute(
            taxonomia_id=taxonomia.id,
            codigo="filho2",
            nome="Filho Dois",
            termo_pai_id=raiz.id,
        )
        buscar = BuscarTermoUseCase(termo_repo)
        assert len(buscar.get_by_pai(raiz.id)) == 2
        assert len(buscar.get_by_taxonomia(taxonomia.id)) == 3

    def test_deletar_termo(self):
        tax_repo, taxonomia = _taxonomia_com_repo()
        termo_repo = FakeTermoRepository()
        criado = CriarTermoUseCase(termo_repo, tax_repo).execute(
            taxonomia_id=taxonomia.id, codigo="sair", nome="Sair"
        )
        assert DeletarTermoUseCase(termo_repo).execute(criado.id) is True
        with pytest.raises(TermoNaoEncontradoError):
            BuscarTermoUseCase(termo_repo).get_by_id(criado.id)
