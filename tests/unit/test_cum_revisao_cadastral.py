"""Testes da revisão periódica do cadastro (DOM-CUM / ADR-0007)."""

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

from src.modules.sigmun_cadastro.application.use_cases.revisar_cadastral import (
    RevisarCadastralUseCase,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)


class _RepoFalso(PessoaRepository):
    def __init__(self, desatualizadas):
        self.desatualizadas = desatualizadas
        self.cortes = []

    def listar_desatualizadas(self, anterior_a, *, limite=1000):
        self.cortes.append(anterior_a)
        return [p[0] for p in self.desatualizadas if p[1] < anterior_a][:limite]

    def save(self, pessoa):  # pragma: no cover - não usado
        return pessoa

    def get_by_id(self, pessoa_id, *, include_deleted=False):  # pragma: no cover
        return None

    def list(self, **kwargs):  # pragma: no cover - não usado
        return []

    def delete(self, pessoa_id, usuario_id):  # pragma: no cover - não usado
        return None

    def exists_documento(self, tipo, numero):  # pragma: no cover - não usado
        return False


class TestRevisarCadastral:
    def test_seleciona_pessoas_com_12_meses(self):
        agora = datetime(2026, 9, 30, tzinfo=timezone.utc)
        antiga = uuid4()
        recente = uuid4()
        repo = _RepoFalso([(antiga, agora - timedelta(days=400)), (recente, agora)])
        caso = RevisarCadastralUseCase(repo, relogio=lambda: agora)
        relatorio = caso.execute(limite_meses=12)
        assert relatorio["total"] == 1
        assert relatorio["pessoas_desatualizadas"] == [str(antiga)]
        assert repo.cortes[0] == agora - timedelta(days=360)

    def test_divulga_evento_com_event_id(self):
        agora = datetime(2026, 9, 30, tzinfo=timezone.utc)
        repo = _RepoFalso([(uuid4(), agora - timedelta(days=500))])
        relatorio = RevisarCadastralUseCase(repo, relogio=lambda: agora).execute()
        assert UUID(relatorio["event_id"])
        assert relatorio["limite_meses"] == 12
