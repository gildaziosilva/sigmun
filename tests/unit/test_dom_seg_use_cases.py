"""Testes unitários dos casos de uso do módulo de Segurança da Informação (DOM-SEG).

Os casos de uso reais são `*UseCase` (Criar/Buscar/Atualizar/etc.) e recebem um
repositório injetado no construtor. Estes testes usam repositórios em memória
(fake) para validar o comportamento de domínio com e sem persistência.
"""

import pytest

from src.modules.sigmun_seg.application.use_cases.controle_use_cases import (
    AtualizarControleSegurancaUseCase,
    BuscarControleSegurancaUseCase,
    CriarControleSegurancaUseCase,
    DeletarControleSegurancaUseCase,
    ImplementarControleSegurancaUseCase,
    ParcialmenteImplementadoUseCase,
)
from src.modules.sigmun_seg.application.use_cases.incidente_use_cases import (
    BuscarIncidenteSegurancaUseCase,
    DeletarIncidenteSegurancaUseCase,
    EncerrarIncidenteSegurancaUseCase,
    EscalarIncidenteSegurancaUseCase,
    MitigarIncidenteSegurancaUseCase,
    RegistrarIncidenteSegurancaUseCase,
    ResolverIncidenteSegurancaUseCase,
)
from src.modules.sigmun_seg.application.use_cases.politica_use_cases import (
    AprovarPoliticaSegurancaUseCase,
    AtualizarPoliticaSegurancaUseCase,
    BuscarPoliticaSegurancaUseCase,
    CriarPoliticaSegurancaUseCase,
    DeletarPoliticaSegurancaUseCase,
)
from src.modules.sigmun_seg.domain.entities import (
    ControleSeguranca,
    IncidenteSeguranca,
    PoliticaSeguranca,
    SeveridadeIncidente,
    StatusIncidente,
)
from src.modules.sigmun_seg.domain.exceptions import (
    ControleJaExisteError,
    ControleNaoEncontradoError,
    IncidenteJaResolvidoError,
    IncidenteNaoEncontradoError,
    NivelRiscoInvalidoError,
    PoliticaJaExisteError,
    PoliticaNaoEncontradaError,
)


class FakeControleRepo:
    """Repositório em memória de controles de segurança."""

    def __init__(self) -> None:
        self._db: dict[str, ControleSeguranca] = {}

    def get_by_id(self, controle_id: str):
        return self._db.get(controle_id)

    def get_by_codigo(self, codigo: str):
        for c in self._db.values():
            if c.codigo == codigo:
                return c
        return None

    def list_all(self, page=0, page_size=50, status=None, tipo=None, categoria=None):
        items = [c for c in self._db.values() if not c.is_deleted]
        return items, len(items)

    def save(self, controle):
        self._db[controle.id] = controle
        return controle

    def delete(self, controle_id):
        c = self._db.get(controle_id)
        if c is None:
            return False
        c.is_deleted = True
        return True

    def exists_by_codigo(self, codigo):
        return any(c.codigo == codigo for c in self._db.values())


class FakePoliticaRepo:
    """Repositório em memória de políticas de segurança."""

    def __init__(self) -> None:
        self._db: dict[str, PoliticaSeguranca] = {}

    def get_by_id(self, politica_id):
        return self._db.get(politica_id)

    def get_by_codigo(self, codigo):
        for p in self._db.values():
            if p.codigo == codigo:
                return p
        return None

    def list_all(self, page=0, page_size=50, ativa=None):
        items = [p for p in self._db.values() if not p.is_deleted]
        return items, len(items)

    def save(self, politica):
        self._db[politica.id] = politica
        return politica

    def delete(self, politica_id):
        p = self._db.get(politica_id)
        if p is None:
            return False
        p.is_deleted = True
        return True

    def exists_by_codigo(self, codigo):
        return any(p.codigo == codigo for p in self._db.values())


class FakeIncidenteRepo:
    """Repositório em memória de incidentes de segurança."""

    def __init__(self) -> None:
        self._db: dict[str, IncidenteSeguranca] = {}

    def get_by_id(self, incidente_id):
        return self._db.get(incidente_id)

    def list_all(self, page=0, page_size=50, severidade=None, status=None):
        items = [i for i in self._db.values() if not i.is_deleted]
        return items, len(items)

    def save(self, incidente):
        self._db[incidente.id] = incidente
        return incidente

    def delete(self, incidente_id):
        i = self._db.get(incidente_id)
        if i is None:
            return False
        i.is_deleted = True
        return True


# ============================ CONTROLES DE SEGURANÇA ============================


class TestCriarControleSegurancaUseCase:
    def test_criar_controle_valido(self) -> None:
        repo = FakeControleRepo()
        use_case = CriarControleSegurancaUseCase(repo)
        controle = use_case.execute(
            codigo="CTRL-001",
            nome="Autenticação multifator",
            descricao="Exige MFA para acesso administrativo",
            tipo="tecnico",
            categoria="acesso",
        )
        assert controle.codigo == "CTRL-001"
        assert controle.nome == "Autenticação multifator"
        assert controle.status.value == "planejado"

    def test_criar_controle_duplicado_lanca_erro(self) -> None:
        repo = FakeControleRepo()
        use_case = CriarControleSegurancaUseCase(repo)
        use_case.execute(codigo="CTRL-001", nome="Controle A")
        with pytest.raises(ControleJaExisteError):
            use_case.execute(codigo="CTRL-001", nome="Controle A")

    def test_codigo_invalido_lanca_value_error(self) -> None:
        repo = FakeControleRepo()
        use_case = CriarControleSegurancaUseCase(repo)
        with pytest.raises(ValueError):
            use_case.execute(codigo="", nome="Controle B")

    def test_nivel_risco_invalido_lanca_erro(self) -> None:
        repo = FakeControleRepo()
        use_case = CriarControleSegurancaUseCase(repo)
        with pytest.raises(NivelRiscoInvalidoError):
            use_case.execute(codigo="CTRL-002", nome="Controle B", nivel_risco="inexistente")


class TestBuscarControleSegurancaUseCase:
    def test_buscar_por_id(self) -> None:
        repo = FakeControleRepo()
        criado = CriarControleSegurancaUseCase(repo).execute(
            codigo="CTRL-003", nome="Criptografia em repouso"
        )
        encontrado = BuscarControleSegurancaUseCase(repo).get_by_id(criado.id)
        assert encontrado is not None
        assert encontrado.codigo == "CTRL-003"

    def test_buscar_inexistente_lanca_erro(self) -> None:
        repo = FakeControleRepo()
        with pytest.raises(ControleNaoEncontradoError):
            BuscarControleSegurancaUseCase(repo).get_by_id("nao-existe")

    def test_listar_vazio(self) -> None:
        items, total = BuscarControleSegurancaUseCase(FakeControleRepo()).list_all()
        assert items == []
        assert total == 0

    def test_listar_com_registros(self) -> None:
        repo = FakeControleRepo()
        criar = CriarControleSegurancaUseCase(repo)
        criar.execute(codigo="CTRL-004", nome="Controle 1")
        criar.execute(codigo="CTRL-005", nome="Controle 2")
        items, total = BuscarControleSegurancaUseCase(repo).list_all()
        assert total == 2
        assert len(items) == 2


class TestAtualizarControleSegurancaUseCase:
    def test_atualizar_nome_e_descricao(self) -> None:
        repo = FakeControleRepo()
        criado = CriarControleSegurancaUseCase(repo).execute(codigo="CTRL-006", nome="Antigo")
        atualizado = AtualizarControleSegurancaUseCase(repo).execute(
            criado.id, nome="Novo nome", descricao="Nova descrição"
        )
        assert atualizado.nome == "Novo nome"
        assert atualizado.descricao == "Nova descrição"

    def test_atualizar_inexistente_lanca_erro(self) -> None:
        repo = FakeControleRepo()
        with pytest.raises(ControleNaoEncontradoError):
            AtualizarControleSegurancaUseCase(repo).execute("nao-existe", nome="X")


class TestFluxoControleImplementacao:
    def test_implementar_controle(self) -> None:
        repo = FakeControleRepo()
        criado = CriarControleSegurancaUseCase(repo).execute(codigo="CTRL-007", nome="Controle")
        assert criado.is_active is False
        ImplementarControleSegurancaUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).is_active is True

    def test_marcar_parcialmente_implementado(self) -> None:
        repo = FakeControleRepo()
        criado = CriarControleSegurancaUseCase(repo).execute(codigo="CTRL-008", nome="Controle")
        ParcialmenteImplementadoUseCase(repo).execute(criado.id)
        controle = repo.get_by_id(criado.id)
        assert controle.status.value == "parcial"

    def test_deletar_controle_soft_delete(self) -> None:
        repo = FakeControleRepo()
        criado = CriarControleSegurancaUseCase(repo).execute(codigo="CTRL-009", nome="Controle")
        assert DeletarControleSegurancaUseCase(repo).execute(criado.id) is True
        assert repo.get_by_id(criado.id).is_deleted is True

    def test_deletar_inexistente_retorna_falso(self) -> None:
        with pytest.raises(ControleNaoEncontradoError):
            DeletarControleSegurancaUseCase(FakeControleRepo()).execute("nao-existe")


# ============================ POLÍTICAS DE SEGURANÇA ============================


class TestCriarPoliticaSegurancaUseCase:
    def test_criar_politica_valida(self) -> None:
        repo = FakePoliticaRepo()
        politica = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo="POL-001", titulo="Política de Senhas", conteudo="Mínimo 12 caracteres"
        )
        assert politica.codigo == "POL-001"
        assert politica.titulo == "Política de Senhas"
        assert politica.ativa is False
        assert politica.versao == "1.0"

    def test_criar_politica_duplicada_lanca_erro(self) -> None:
        repo = FakePoliticaRepo()
        use_case = CriarPoliticaSegurancaUseCase(repo)
        use_case.execute(codigo="POL-001", titulo="P", conteudo="c")
        with pytest.raises(PoliticaJaExisteError):
            use_case.execute(codigo="POL-001", titulo="P2", conteudo="c2")

    def test_criar_politica_sem_titulo_lanca_value_error(self) -> None:
        repo = FakePoliticaRepo()
        with pytest.raises(ValueError):
            CriarPoliticaSegurancaUseCase(repo).execute(codigo="POL-002", titulo="", conteudo="c")


class TestBuscarPoliticaSegurancaUseCase:
    def test_buscar_por_id(self) -> None:
        repo = FakePoliticaRepo()
        criada = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo="POL-003", titulo="LGPD", conteudo="Conteúdo"
        )
        encontrada = BuscarPoliticaSegurancaUseCase(repo).get_by_id(criada.id)
        assert encontrada is not None
        assert encontrada.codigo == "POL-003"

    def test_buscar_inexistente_lanca_erro(self) -> None:
        repo = FakePoliticaRepo()
        with pytest.raises(PoliticaNaoEncontradaError):
            BuscarPoliticaSegurancaUseCase(repo).get_by_id("nao-existe")

    def test_listar_politicas(self) -> None:
        repo = FakePoliticaRepo()
        criar = CriarPoliticaSegurancaUseCase(repo)
        criar.execute(codigo="POL-004", titulo="P1", conteudo="c")
        criar.execute(codigo="POL-005", titulo="P2", conteudo="c")
        items, total = BuscarPoliticaSegurancaUseCase(repo).list_all()
        assert total == 2


class TestAtualizarPoliticaSegurancaUseCase:
    def test_atualizar_titulo_e_versao(self) -> None:
        repo = FakePoliticaRepo()
        criada = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo="POL-006", titulo="Antiga", conteudo="c"
        )
        atualizada = AtualizarPoliticaSegurancaUseCase(repo).execute(
            criada.id, titulo="Nova", versao="2.0"
        )
        assert atualizada.titulo == "Nova"
        assert atualizada.versao == "2.0"

    def test_atualizar_inexistente_lanca_erro(self) -> None:
        repo = FakePoliticaRepo()
        with pytest.raises(PoliticaNaoEncontradaError):
            AtualizarPoliticaSegurancaUseCase(repo).execute("nao-existe", titulo="X")


class TestFluxoPoliticaAprovacao:
    def test_aprovar_politica(self) -> None:
        repo = FakePoliticaRepo()
        criada = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo="POL-007", titulo="Política", conteudo="c"
        )
        aprovada = AprovarPoliticaSegurancaUseCase(repo).execute(criada.id, "user-1")
        assert aprovada.ativa is True
        assert aprovada.aprovador_id == "user-1"

    def test_deletar_politica(self) -> None:
        repo = FakePoliticaRepo()
        criada = CriarPoliticaSegurancaUseCase(repo).execute(
            codigo="POL-008", titulo="Política", conteudo="c"
        )
        assert DeletarPoliticaSegurancaUseCase(repo).execute(criada.id) is True
        assert repo.get_by_id(criada.id).is_deleted is True


# ============================ INCIDENTES DE SEGURANÇA ============================


class TestRegistrarIncidenteSegurancaUseCase:
    def test_registrar_incidente_valido(self) -> None:
        repo = FakeIncidenteRepo()
        incidente = RegistrarIncidenteSegurancaUseCase(repo).execute(
            titulo="Acesso indevido",
            descricao="Tentativa de acesso não autorizado",
            severidade="alta",
            impacto="crítico",
            categoria="acesso",
        )
        assert incidente.titulo == "Acesso indevido"
        assert incidente.status == StatusIncidente.ABERTO

    def test_registrar_sem_titulo_lanca_value_error(self) -> None:
        repo = FakeIncidenteRepo()
        with pytest.raises(ValueError):
            RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="", descricao="desc")

    def test_registrar_severidade_invalida_lanca_erro(self) -> None:
        repo = FakeIncidenteRepo()
        with pytest.raises(ValueError):
            RegistrarIncidenteSegurancaUseCase(repo).execute(
                titulo="T", descricao="d", severidade="inexistente"
            )


class TestBuscarIncidenteSegurancaUseCase:
    def test_buscar_por_id(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(
            titulo="Incidente", descricao="desc"
        )
        encontrado = BuscarIncidenteSegurancaUseCase(repo).get_by_id(criado.id)
        assert encontrado is not None
        assert encontrado.titulo == "Incidente"

    def test_buscar_inexistente_lanca_erro(self) -> None:
        with pytest.raises(IncidenteNaoEncontradoError):
            BuscarIncidenteSegurancaUseCase(FakeIncidenteRepo()).get_by_id("nao-existe")

    def test_listar_incidentes(self) -> None:
        repo = FakeIncidenteRepo()
        usar = RegistrarIncidenteSegurancaUseCase(repo)
        usar.execute(titulo="I1", descricao="d")
        usar.execute(titulo="I2", descricao="d")
        items, total = BuscarIncidenteSegurancaUseCase(repo).list_all()
        assert total == 2


class TestFluxoIncidente:
    def test_escalar_incidente(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        EscalarIncidenteSegurancaUseCase(repo).execute(criado.id, "resp-1")
        assert repo.get_by_id(criado.id).atribuido_a == "resp-1"
        assert repo.get_by_id(criado.id).status == StatusIncidente.EM_ANALISE

    def test_mitigar_incidente(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        MitigarIncidenteSegurancaUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).status == StatusIncidente.EM_MITIGACAO

    def test_resolver_incidente(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        ResolverIncidenteSegurancaUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).status == StatusIncidente.RESOLVIDO

    def test_resolver_ja_resolvido_lanca_erro(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        ResolverIncidenteSegurancaUseCase(repo).execute(criado.id)
        with pytest.raises(IncidenteJaResolvidoError):
            ResolverIncidenteSegurancaUseCase(repo).execute(criado.id)

    def test_encerrar_incidente(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        EncerrarIncidenteSegurancaUseCase(repo).execute(criado.id)
        assert repo.get_by_id(criado.id).status == StatusIncidente.ENCERRADO

    def test_deletar_incidente(self) -> None:
        repo = FakeIncidenteRepo()
        criado = RegistrarIncidenteSegurancaUseCase(repo).execute(titulo="Incidente", descricao="d")
        assert DeletarIncidenteSegurancaUseCase(repo).execute(criado.id) is True
        assert repo.get_by_id(criado.id).is_deleted is True


# ============================ VALIDAÇÕES DE ENTIDADES ============================


class TestEntidades:
    def test_controle_is_active_reflete_status(self) -> None:
        c = ControleSeguranca(codigo="X", nome="n")
        assert c.is_active is False
        c.implementar()
        assert c.is_active is True

    def test_chave_criptografica_revogada(self) -> None:
        from src.modules.sigmun_seg.domain.entities import ChaveCriptografica

        chave = ChaveCriptografica(nome="chave-1")
        assert chave.is_active is True
        chave.revogar()
        assert chave.is_active is False
        assert chave.status == "revogada"

    def test_severidade_incidente_enum(self) -> None:
        assert SeveridadeIncidente.ALTA.value == "alta"
        assert SeveridadeIncidente.CRITICA.value == "critica"
