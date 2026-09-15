"""Testes unitários dos casos de uso de Chaves Criptográficas e Credenciais (DOM-SEG)."""
import pytest

from src.modules.sigmun_seg.domain.entities import (
    ChaveCriptografica,
    Credencial,
    StatusCredencial,
)
from src.modules.sigmun_seg.domain.exceptions import (
    ChaveJaRevogadaError,
    ChaveNaoEncontradaError,
    CredencialJaRevogadaError,
    CredencialNaoEncontradaError,
)
from src.modules.sigmun_seg.application.use_cases.chave_use_cases import (
    AtualizarChaveUseCase,
    BuscarChaveUseCase,
    CriarChaveUseCase,
    DeletarChaveUseCase,
    ExpirarChaveUseCase,
    RevogarChaveUseCase,
)
from src.modules.sigmun_seg.application.use_cases.credencial_use_cases import (
    BuscarCredencialUseCase,
    CriarCredencialUseCase,
    DeletarCredencialUseCase,
    RegistrarFalhaCredencialUseCase,
    RegistrarUsoCredencialUseCase,
    RevogarCredencialUseCase,
    SuspenderCredencialUseCase,
)


class FakeChaveRepo:
    """Repositório em memória de chaves criptográficas."""

    def __init__(self) -> None:
        self._db: dict[str, ChaveCriptografica] = {}

    def get_by_id(self, chave_id):
        return self._db.get(chave_id)

    def get_by_nome(self, nome):
        for c in self._db.values():
            if c.nome == nome:
                return c
        return None

    def list_all(self, page=0, page_size=50, status=None):
        items = [c for c in self._db.values() if not c.is_deleted]
        return items, len(items)

    def save(self, chave):
        self._db[chave.id] = chave
        return chave

    def delete(self, chave_id):
        c = self._db.get(chave_id)
        if c is None:
            return False
        c.is_deleted = True
        return True

    def exists_by_nome(self, nome):
        return any(c.nome == nome for c in self._db.values())


class FakeCredencialRepo:
    """Repositório em memória de credenciais."""

    def __init__(self) -> None:
        self._db: dict[str, Credencial] = {}

    def get_by_id(self, credencial_id):
        return self._db.get(credencial_id)

    def get_by_usuario(self, usuario_id):
        return [c for c in self._db.values() if c.usuario_id == usuario_id]

    def list_all(self, page=0, page_size=50, status=None, tipo=None):
        items = [c for c in self._db.values() if not c.is_deleted]
        return items, len(items)

    def save(self, credencial):
        self._db[credencial.id] = credencial
        return credencial

    def delete(self, credencial_id):
        c = self._db.get(credencial_id)
        if c is None:
            return False
        c.is_deleted = True
        return True

    def exists_by_identificador(self, identificador):
        return any(c.identificador == identificador for c in self._db.values())


# ============================ CHAVES CRIPTOGRÁFICAS ============================


class TestCriarChaveUseCase:
    def test_criar_chave_valida(self) -> None:
        repo = FakeChaveRepo()
        chave = CriarChaveUseCase(repo).execute(
            nome="chave-master", algoritmo="AES256", tipo="simetrica", tamanho_bits=256
        )
        assert chave.nome == "chave-master"
        assert chave.algoritmo == "AES256"
        assert chave.status == "ativa"
        assert chave.is_active is True

    def test_criar_chave_sem_nome_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CriarChaveUseCase(FakeChaveRepo()).execute(nome="   ")

    def test_criar_chave_nome_duplicado_lanca_erro(self) -> None:
        repo = FakeChaveRepo()
        CriarChaveUseCase(repo).execute(nome="chave-x")
        with pytest.raises(ValueError):
            CriarChaveUseCase(repo).execute(nome="chave-x")

    def test_criar_chave_tamanho_bits_invalido(self) -> None:
        with pytest.raises(ValueError):
            CriarChaveUseCase(FakeChaveRepo()).execute(nome="c", tamanho_bits=0)


class TestBuscarChaveUseCase:
    def test_buscar_por_id(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-1")
        encontrada = BuscarChaveUseCase(repo).get_by_id(criada.id)
        assert encontrada is not None
        assert encontrada.nome == "chave-1"

    def test_buscar_por_nome(self) -> None:
        repo = FakeChaveRepo()
        CriarChaveUseCase(repo).execute(nome="chave-2")
        assert BuscarChaveUseCase(repo).get_by_nome("chave-2") is not None

    def test_buscar_inexistente_lanca_erro(self) -> None:
        with pytest.raises(ChaveNaoEncontradaError):
            BuscarChaveUseCase(FakeChaveRepo()).get_by_id("nao-existe")

    def test_listar_vazio(self) -> None:
        items, total = BuscarChaveUseCase(FakeChaveRepo()).list_all()
        assert items == []
        assert total == 0


class TestFluxoChave:
    def test_revogar_chave(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-3")
        RevogarChaveUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).status == "revogada"
        assert repo.get_by_id(criada.id).is_active is False

    def test_revogar_ja_revogada_lanca_erro(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-4")
        RevogarChaveUseCase(repo).execute(criada.id)
        with pytest.raises(ChaveJaRevogadaError):
            RevogarChaveUseCase(repo).execute(criada.id)

    def test_expirar_chave(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-5")
        ExpirarChaveUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).status == "expirada"

    def test_atualizar_chave(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-6")
        AtualizarChaveUseCase(repo).execute(criada.id, nome="chave-6-renomeada")
        assert repo.get_by_id(criada.id).nome == "chave-6-renomeada"

    def test_deletar_chave_soft_delete(self) -> None:
        repo = FakeChaveRepo()
        criada = CriarChaveUseCase(repo).execute(nome="chave-7")
        assert DeletarChaveUseCase(repo).execute(criada.id) is True
        assert repo.get_by_id(criada.id).is_deleted is True
# ============================ CREDENCIAIS ============================


class TestCriarCredencialUseCase:
    def test_criar_credencial_valida(self) -> None:
        repo = FakeCredencialRepo()
        credencial = CriarCredencialUseCase(repo).execute(
            usuario_id="user-1", identificador="hash-abc", tipo="chave_api"
        )
        assert credencial.usuario_id == "user-1"
        assert credencial.identificador == "hash-abc"
        assert credencial.status == StatusCredencial.ATIVA

    def test_criar_credencial_sem_usuario_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CriarCredencialUseCase(FakeCredencialRepo()).execute(
                usuario_id="", identificador="x"
            )

    def test_criar_credencial_sem_identificador_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            CriarCredencialUseCase(FakeCredencialRepo()).execute(
                usuario_id="u", identificador="  "
            )


class TestBuscarCredencialUseCase:
    def test_buscar_por_id(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="id-1"
        )
        assert BuscarCredencialUseCase(repo).get_by_id(criada.id) is not None

    def test_buscar_por_usuario(self) -> None:
        repo = FakeCredencialRepo()
        criar = CriarCredencialUseCase(repo)
        criar.execute(usuario_id="u1", identificador="a")
        criar.execute(usuario_id="u1", identificador="b")
        criar.execute(usuario_id="u2", identificador="c")
        assert len(BuscarCredencialUseCase(repo).get_by_usuario("u1")) == 2

    def test_buscar_inexistente_lanca_erro(self) -> None:
        with pytest.raises(CredencialNaoEncontradaError):
            BuscarCredencialUseCase(FakeCredencialRepo()).get_by_id("nao-existe")

    def test_listar(self) -> None:
        repo = FakeCredencialRepo()
        criar = CriarCredencialUseCase(repo)
        criar.execute(usuario_id="u1", identificador="a")
        criar.execute(usuario_id="u2", identificador="b")
        items, total = BuscarCredencialUseCase(repo).list_all()
        assert total == 2


class TestFluxoCredencial:
    def test_suspender_credencial(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x1"
        )
        SuspenderCredencialUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).status == StatusCredencial.SUSPENSA

    def test_revogar_credencial(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x2"
        )
        RevogarCredencialUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).status == StatusCredencial.REVOGADA

    def test_revogar_ja_revogada_lanca_erro(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x3"
        )
        RevogarCredencialUseCase(repo).execute(criada.id)
        with pytest.raises(CredencialJaRevogadaError):
            RevogarCredencialUseCase(repo).execute(criada.id)

    def test_registrar_falha_incrementa_tentativas(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x4"
        )
        RegistrarFalhaCredencialUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).tentativas_falhas == 1

    def test_registrar_uso_zera_tentativas(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x5"
        )
        RegistrarFalhaCredencialUseCase(repo).execute(criada.id)
        RegistrarUsoCredencialUseCase(repo).execute(criada.id)
        assert repo.get_by_id(criada.id).tentativas_falhas == 0

    def test_deletar_credencial_soft_delete(self) -> None:
        repo = FakeCredencialRepo()
        criada = CriarCredencialUseCase(repo).execute(
            usuario_id="u", identificador="x6"
        )
        assert DeletarCredencialUseCase(repo).execute(criada.id) is True
        assert repo.get_by_id(criada.id).is_deleted is True