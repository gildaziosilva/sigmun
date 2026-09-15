"""Testes unitários dos casos de uso do módulo de Gestão Documental (DOM-GDO)."""

from datetime import datetime, timedelta

import pytest

from src.modules.sigmun_gdo.application.interfaces import (
    RepositorioClassificacaoDocumental,
    RepositorioDocumento,
    RepositorioTipoDocumental,
    RepositorioTramitacao,
)
from src.modules.sigmun_gdo.application.use_cases import (
    ClassificarDocumentoUseCase,
    CriarDocumentoUseCase,
    TramitarDocumentoUseCase,
)
from src.modules.sigmun_gdo.application.use_cases.classificar_documento_use_case import (
    ClassificarDocumentoInputDTO,
)
from src.modules.sigmun_gdo.application.use_cases.criar_documento_use_case import (
    CriarDocumentoInputDTO,
)
from src.modules.sigmun_gdo.application.use_cases.tramitar_documento_use_case import (
    TramitarDocumentoInputDTO,
)
from src.modules.sigmun_gdo.domain.entities import (
    ClassificacaoDocumental,
    Documento,
    ProcessoDocumento,
    StatusDocumento,
    TabelaTemporalidade,
    TipoDestinacao,
    TipoTramitacao,
    TramitacaoDocumento,
)
from src.modules.sigmun_gdo.domain.events import EventoDocumentoCriado, EventoDocumentoTramitado
from src.modules.sigmun_gdo.domain.exceptions import (
    CodigoDocumentalDuplicadoError,
    DocumentoNaoEncontradoError,
    IntegridadeInvalidaError,
)
from src.modules.sigmun_gdo.domain.services import ServicoHashIntegridade, ServicoTemporalidade
from src.modules.sigmun_gdo.domain.value_objects import (
    CodigoDocumental,
    HashIntegridade,
    NumeroDocumento,
)


# Repositórios em memória
class _FakeBase:
    def __init__(self):
        self._data = {}

    def get_by_id(self, entity_id):
        return self._data.get(entity_id)

    def save(self, entity):
        self._data[entity.id] = entity
        return entity

    def delete(self, entity_id):
        return self._data.pop(entity_id, None) is not None


class FakeDocumentoRepository(_FakeBase, RepositorioDocumento):
    def get_by_codigo(self, codigo, ano):
        return next(
            (
                d
                for d in self._data.values()
                if d.codigo == codigo and d.ano == ano and not d.is_deleted
            ),
            None,
        )

    def find_by_processo(self, processo_id):
        return [d for d in self._data.values() if d.processo_id == processo_id and not d.is_deleted]

    def find_ativos(self):
        return [d for d in self._data.values() if not d.is_deleted]


class FakeClassificacaoRepository(_FakeBase, RepositorioClassificacaoDocumental):
    def get_by_codigo(self, codigo):
        return next((c for c in self._data.values() if c.codigo == codigo), None)

    def find_all(self):
        return list(self._data.values())


class FakeTramitacaoRepository(_FakeBase, RepositorioTramitacao):
    def find_by_documento(self, documento_id):
        return [t for t in self._data.values() if t.documento_id == documento_id]


class FakeTipoDocumentalRepository(_FakeBase, RepositorioTipoDocumental):
    """Fake de repositório de tipos documentais para testes unitários."""

    def get_by_codigo(self, codigo):
        return (
            next((t for t in self._data.values() if t.is_ativo), None)
            if self._data
            else type(
                "Tipo", (), {"id": "default", "codigo": codigo, "nome": "Default", "is_ativo": True}
            )()
        )

    def find_ativos(self):
        return [t for t in self._data.values() if t.is_ativo]

    def find_all(self):
        return list(self._data.values())

    def save(self, entity):
        self._data[entity.id] = entity
        return entity


# Testes de CriarDocumentoUseCase
class TestCriarDocumentoUseCase:
    def test_cria_documento_com_sucesso(self):
        repo = FakeDocumentoRepository()
        repo_tipo = FakeTipoDocumentalRepository()
        uc = CriarDocumentoUseCase(repo, repo_tipo)
        dto = CriarDocumentoInputDTO(
            codigo="DOC-001",
            numero="001",
            ano=2026,
            tipo_documental_id="tipo-001",
            titulo="Teste",
            descricao="Doc teste",
            unidade_autor_id="und-01",
            created_by="user-1",
        )
        result = uc.execute(dto)
        assert result.codigo == "DOC-001"
        assert result.status == "ativo"

    def test_codigo_duplicado_levanta_erro(self):
        repo = FakeDocumentoRepository()
        doc1 = Documento(
            codigo="DOC-001",
            numero="001",
            ano=2026,
            titulo="T1",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            created_by="user-1",
        )
        repo.save(doc1)
        repo_tipo = FakeTipoDocumentalRepository()
        uc = CriarDocumentoUseCase(repo, repo_tipo)
        dto = CriarDocumentoInputDTO(
            codigo="DOC-001",
            numero="002",
            ano=2026,
            tipo_documental_id="tipo-002",
            titulo="Duplicado",
            descricao="Doc duplicado",
            unidade_autor_id="und-02",
            created_by="user-2",
        )
        with pytest.raises(CodigoDocumentalDuplicadoError):
            uc.execute(dto)

    def test_hash_invalido_levanta_erro(self):
        repo = FakeDocumentoRepository()
        repo_tipo = FakeTipoDocumentalRepository()
        uc = CriarDocumentoUseCase(repo, repo_tipo)
        dto = CriarDocumentoInputDTO(
            codigo="DOC-002",
            numero="002",
            ano=2026,
            tipo_documental_id="t1",
            titulo="Hash inv",
            descricao="Doc hash invalido",
            unidade_autor_id="u1",
            hash_integridade="123",
            created_by="user-1",
        )
        with pytest.raises(IntegridadeInvalidaError):
            uc.execute(dto)

    def test_documento_com_conteudo_ref(self):
        repo = FakeDocumentoRepository()
        repo_tipo = FakeTipoDocumentalRepository()
        uc = CriarDocumentoUseCase(repo, repo_tipo)
        dto = CriarDocumentoInputDTO(
            codigo="DOC-003",
            numero="003",
            ano=2026,
            tipo_documental_id="t1",
            titulo="Com ref",
            descricao="Doc com referencia",
            unidade_autor_id="u1",
            conteudo_ref="/files/doc003.pdf",
            hash_integridade="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
            created_by="user-1",
        )
        result = uc.execute(dto)
        assert result.hash_integridade is not None

    def test_documento_sem_processo(self):
        repo = FakeDocumentoRepository()
        repo_tipo = FakeTipoDocumentalRepository()
        uc = CriarDocumentoUseCase(repo, repo_tipo)
        dto = CriarDocumentoInputDTO(
            codigo="DOC-004",
            numero="004",
            ano=2026,
            tipo_documental_id="t1",
            titulo="Sem proc",
            descricao="Doc sem processo",
            unidade_autor_id="u1",
            created_by="user-1",
        )
        result = uc.execute(dto)
        assert result is not None


class TestClassificarDocumentoUseCase:
    def _setup(self):
        repo_doc = FakeDocumentoRepository()
        repo_class = FakeClassificacaoRepository()
        doc = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            created_by="u1",
        )
        repo_doc.save(doc)
        cls = ClassificacaoDocumental(codigo="C1", nome="Teste", nivel=1, prazo_retencao=12)
        repo_class.save(cls)
        return repo_doc, repo_class, doc, cls

    def test_classifica_documento_com_sucesso(self):
        repo_doc, repo_class, doc, cls = self._setup()
        uc = ClassificarDocumentoUseCase(repo_doc, repo_class)
        dto = ClassificarDocumentoInputDTO(id=doc.id, classificacao_id=cls.id, autor_id="u1")
        result = uc.execute(dto)
        assert result is True

    def test_documento_nao_encontrado(self):
        repo_doc = FakeDocumentoRepository()
        repo_class = FakeClassificacaoRepository()
        uc = ClassificarDocumentoUseCase(repo_doc, repo_class)
        dto = ClassificarDocumentoInputDTO(id="nope", classificacao_id="c1", autor_id="u1")
        with pytest.raises(DocumentoNaoEncontradoError):
            uc.execute(dto)


class TestTramitarDocumentoUseCase:
    def test_tramita_com_sucesso(self):
        repo_doc = FakeDocumentoRepository()
        repo_tram = FakeTramitacaoRepository()
        doc = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            created_by="u1",
        )
        repo_doc.save(doc)
        uc = TramitarDocumentoUseCase(repo_doc, repo_tram)
        dto = TramitarDocumentoInputDTO(
            documento_id=doc.id,
            unidade_origem_id="u1",
            unidade_destino_id="u2",
            tipo=TipoTramitacao.ENVIO,
            motivo="Envio para analise",
            autor_id="u1",
        )
        result = uc.execute(dto)
        assert result.documento_id == doc.id
        assert result.tipo == TipoTramitacao.ENVIO

    def test_tramita_documento_nao_encontrado(self):
        repo_doc = FakeDocumentoRepository()
        repo_tram = FakeTramitacaoRepository()
        uc = TramitarDocumentoUseCase(repo_doc, repo_tram)
        dto = TramitarDocumentoInputDTO(
            documento_id="nope",
            unidade_origem_id="u1",
            unidade_destino_id="u2",
            tipo=TipoTramitacao.ENVIO,
            motivo="Teste",
            autor_id="u1",
        )
        with pytest.raises(DocumentoNaoEncontradoError):
            uc.execute(dto)


# Testes de Entidades
class TestDocumentoEntity:
    def test_status_rascunho_inicial(self):
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
        )
        assert d.status == StatusDocumento.RASCUNHO

    def test_assinado_com_hash(self):
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            hash_integridade="abc",
        )
        assert d.is_assinado is True

    def test_nao_assinado_sem_hash(self):
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
        )
        assert d.is_assinado is False

    def test_ativo_apos_criacao(self):
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
        )
        assert d.is_active is True
        d.is_deleted = True
        assert d.is_active is False


class TestClassificacaoDocumental:
    def test_raiz_sem_pai(self):
        c = ClassificacaoDocumental(codigo="C1", nome="R", prazo_retencao=12)
        assert c.is_root is True

    def test_filha_com_pai(self):
        c = ClassificacaoDocumental(
            codigo="C2", nome="F", prazo_retencao=6, classificacao_pai_id="p1"
        )
        assert c.is_root is False


class TestTramitacaoDocumento:
    def test_nova_nao_concluida(self):
        t = TramitacaoDocumento(
            documento_id="d1",
            unidade_origem_id="u1",
            unidade_destino_id="u2",
            tipo=TipoTramitacao.ENVIO,
        )
        assert t.is_concluida is False

    def test_concluida_com_recebimento(self):
        t = TramitacaoDocumento(
            documento_id="d1",
            unidade_origem_id="u1",
            unidade_destino_id="u2",
            tipo=TipoTramitacao.ENVIO,
            data_recebimento=datetime.utcnow(),
        )
        assert t.is_concluida is True


class TestProcessoDocumento:
    def test_novo_ativo(self):
        p = ProcessoDocumento(
            numero="P1", ano=2026, tipo_processo_id="t1", titulo="P", unidade_autor_id="u1"
        )
        assert p.is_active is True
        assert p.status == "aberto"


class TestTabelaTemporalidade:
    def test_ativa_padrao(self):
        t = TabelaTemporalidade(codigo="T1", nome="Temp", prazo_tempo=12)
        assert t.is_ativo is True
        assert t.tipo_destinacao == TipoDestinacao.ELIMINACAO


# Testes de Repositórios
class TestRepositorios:
    def test_documento_save_get(self):
        repo = FakeDocumentoRepository()
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            created_by="u1",
        )
        saved = repo.save(d)
        assert repo.get_by_id(saved.id) is not None

    def test_find_by_processo(self):
        repo = FakeDocumentoRepository()
        d = Documento(
            codigo="D1",
            numero="1",
            ano=2026,
            titulo="T",
            tipo_documental_id="t1",
            unidade_autor_id="u1",
            processo_id="p1",
            created_by="u1",
        )
        repo.save(d)
        assert len(repo.find_by_processo("p1")) == 1

    def test_classificacao_find_all(self):
        repo = FakeClassificacaoRepository()
        c = ClassificacaoDocumental(codigo="C1", nome="T", prazo_retencao=12)
        repo.save(c)
        assert len(repo.find_all()) == 1

    def test_tramitacao_find_by_documento(self):
        repo = FakeTramitacaoRepository()
        t = TramitacaoDocumento(
            documento_id="d1",
            unidade_origem_id="u1",
            unidade_destino_id="u2",
            tipo=TipoTramitacao.ENVIO,
        )
        repo.save(t)
        assert len(repo.find_by_documento("d1")) == 1


# Testes de Value Objects
class TestHashIntegridade:
    def test_hash_valido(self):
        h = HashIntegridade("a" * 64)
        assert h.valor == "a" * 64
        assert len(h.valor) == 64

    def test_hash_invalido_curto(self):
        with pytest.raises(ValueError):
            HashIntegridade("abc")

    def test_hash_invalido_vazio(self):
        with pytest.raises(ValueError):
            HashIntegridade("")

    def test_igualdade_case_insensitive(self):
        h1 = HashIntegridade("A" * 64)
        h2 = HashIntegridade("a" * 64)
        assert h1 == h2
        assert str(h1) == "a" * 64


class TestCodigoDocumental:
    def test_codigo_valido(self):
        c = CodigoDocumental("DOC-001")
        assert c.valor == "DOC-001"

    def test_codigo_muito_curto(self):
        with pytest.raises(ValueError):
            CodigoDocumental("AB")

    def test_codigo_vazio(self):
        with pytest.raises(ValueError):
            CodigoDocumental("")


class TestNumeroDocumento:
    def test_numero_com_ano(self):
        n = NumeroDocumento(numero="001", ano=2026)
        assert n.numero == "001"
        assert n.ano == 2026


# Testes de Serviços de Domínio
class TestServicoHashIntegridade:
    def test_calcular_hash_sha256(self):
        conteudo = b"conteudo do documento"
        hash_gerado = ServicoHashIntegridade.calcular_hash(conteudo)
        assert len(hash_gerado) == 64
        assert hash_gerado == ServicoHashIntegridade.calcular_hash(conteudo)

    def test_validar_hash_correto(self):
        conteudo = b"conteudo do documento"
        hash_gerado = ServicoHashIntegridade.calcular_hash(conteudo)
        assert ServicoHashIntegridade.validar_hash(conteudo, hash_gerado) is True

    def test_validar_hash_incorreto(self):
        conteudo = b"conteudo do documento"
        assert ServicoHashIntegridade.validar_hash(conteudo, "f" * 64) is False


class TestServicoTemporalidade:
    def test_calcular_data_destinacao(self):
        base = datetime(2026, 1, 1)
        resultado = ServicoTemporalidade.calcular_data_destinacao(base, 12, "encerramento")
        assert resultado == base + timedelta(days=360)

    def test_prazo_invalido_levanta_erro(self):
        with pytest.raises(ValueError):
            ServicoTemporalidade.calcular_data_destinacao(datetime(2026, 1, 1), 0, "encerramento")

    def test_documento_vencido(self):
        base = datetime(2020, 1, 1)
        vencimento = ServicoTemporalidade.calcular_data_destinacao(base, 12, "encerramento")
        assert ServicoTemporalidade.is_documento_vencido(vencimento) is True

    def test_documento_nao_vencido(self):
        futuro = datetime.utcnow() + timedelta(days=365)
        assert ServicoTemporalidade.is_documento_vencido(futuro) is False


# Testes de Eventos de Domínio
class TestEventosDominio:
    def test_evento_criado_nome(self):
        evento = EventoDocumentoCriado(documento_id="d1", usuario_id="u1")
        assert evento.evento_nome == "DocumentoCriado"

    def test_evento_tramitado_nome(self):
        evento = EventoDocumentoTramitado(documento_id="d1", usuario_id="u1")
        assert evento.evento_nome == "DocumentoTramitado"

    def test_evento_ids_unicos(self):
        e1 = EventoDocumentoCriado(documento_id="d1")
        e2 = EventoDocumentoCriado(documento_id="d1")
        assert e1.evento_id != e2.evento_id

    def test_evento_payload_padrao(self):
        evento = EventoDocumentoCriado(documento_id="d1")
        assert evento.payload == {}
        assert evento.timestamp is not None
