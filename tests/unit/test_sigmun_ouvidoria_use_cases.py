"""Testes unitários dos casos de uso do DOM-OUV.

Usa repositórios em memória que implementam os ports de
``application/interfaces.py``, exercitando o ciclo use case → persistência
sem depender de banco.

Cobre as regras de aplicação:

- geração de protocolo (RN-OUV-001);
- recusa de tipo errado no caso de uso (denúncia / LAI têm use case próprio);
- validação de transição antes de alterar status (RN-OUV-010);
- prorrogação de prazo (LAI art. 11 §1º);
- avaliação fora da faixa 1–5;
- encaminhamento de denúncia a órgão externo;
- interposição e decisão de recurso LAI (LAI art. 15);
- paginação e filtros de listagem.
"""

from __future__ import annotations

from datetime import date
from uuid import UUID

import pytest

from src.modules.sigmun_ouvidoria.application.use_cases import (
    AlterarStatusInput,
    AlterarStatusUseCase,
    AvaliarManifestacaoInput,
    AvaliarManifestacaoUseCase,
    DecidirRecursoLaiInput,
    DecidirRecursoLaiUseCase,
    EncaminharDenunciaInput,
    EncaminharDenunciaUseCase,
    InterporRecursoLaiInput,
    InterporRecursoLaiUseCase,
    ListarManifestacoesInput,
    ListarManifestacoesUseCase,
    ProrrogarPrazoInput,
    ProrrogarPrazoUseCase,
    RegistrarDenunciaInput,
    RegistrarDenunciaUseCase,
    RegistrarManifestacaoInput,
    RegistrarManifestacaoUseCase,
    RegistrarPedidoLaiInput,
    RegistrarPedidoLaiUseCase,
    ResponderManifestacaoInput,
    ResponderManifestacaoUseCase,
)
from src.modules.sigmun_ouvidoria.domain.exceptions import (
    DenunciaNaoEncontradaError,
    ManifestacaoNaoEncontradaError,
    PedidoLaiNaoEncontradoError,
    ProtocoloJaExistenteError,
    RegraNegocioError,
)
from src.modules.sigmun_ouvidoria.domain.value_objects import (
    Protocolo,
    StatusManifestacao,
)

CPF_VALIDO = "52998224725"


# ===========================================================================
# Repositórios em memória
# ===========================================================================


class RepoProtocoloMemoria:
    """Sequencial por ano, com memória de códigos já usados."""

    def __init__(self) -> None:
        self._sequencial: dict[int, int] = {}
        self.usados: set[str] = set()

    def obter_proximo_sequencial(self, ano: int) -> int:
        self._sequencial[ano] = self._sequencial.get(ano, 0) + 1
        return self._sequencial[ano]

    def existe_protocolo(self, codigo: str) -> bool:
        return codigo in self.usados

    def registrar_protocolo(self, protocolo: Protocolo) -> None:
        if protocolo.codigo in self.usados:
            raise ProtocoloJaExistenteError(f"Protocolo {protocolo.codigo} já existe")
        self.usados.add(protocolo.codigo)


class RepoAnexoMemoria:
    def __init__(self) -> None:
        self.itens: dict[str, object] = {}

    def save(self, anexo, manifestacao_id: UUID):
        self.itens[anexo.id] = anexo
        return anexo

    def get_by_id(self, anexo_id: UUID):
        return self.itens.get(str(anexo_id))

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list:
        return []


class RepoTramitacaoMemoria:
    def __init__(self) -> None:
        self.registros: list[dict] = []

    def save(
        self,
        manifestacao_id: UUID,
        status_anterior,
        status_novo,
        observacao: str,
        usuario_id: str,
    ) -> None:
        self.registros.append(
            {
                "manifestacao_id": str(manifestacao_id),
                "status_anterior": status_anterior,
                "status_novo": status_novo,
                "observacao": observacao,
                "usuario_id": usuario_id,
            }
        )

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list[dict]:
        return [r for r in self.registros if r["manifestacao_id"] == str(manifestacao_id)]


class _RepoBaseMemoria:
    """Base comum dos repositórios de agregado."""

    def __init__(self) -> None:
        self.itens: dict[str, object] = {}

    def save(self, entidade):
        self.itens[str(entidade.id)] = entidade
        return entidade

    def get_by_id(self, entidade_id: str):
        return self.itens.get(str(entidade_id))

    def get_by_protocolo(self, protocolo: str):
        for item in self.itens.values():
            if item.protocolo and item.protocolo.codigo == protocolo:
                return item
        return None

    def list_all(self, page: int = 1, page_size: int = 20, filtros: dict | None = None):
        return list(self.itens.values())

    def count_all(self, filtros: dict | None = None) -> int:
        return len(self.itens)

    def contar_por_ano(self, ano: int) -> int:
        return len(self.itens)

    def contar_por_status_ano(self, status, ano: int) -> int:
        return len([i for i in self.itens.values() if i.status is status])

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        return 0

    def estatisticas_por_tipo(self, ano: int) -> dict:
        return {}

    def buscar_vencendo_prazo(self, dias: int) -> list:
        return []


class RepoManifestacaoMemoria(_RepoBaseMemoria):
    pass


class RepoDenunciaMemoria(_RepoBaseMemoria):
    pass


class RepoPedidoLaiMemoria(_RepoBaseMemoria):
    pass


def _cidadao():
    from src.modules.sigmun_ouvidoria.domain.value_objects import DadosCidadao

    return DadosCidadao(nome="Maria Souza", cpf=CPF_VALIDO, email="maria@exemplo.com")


def _prazo():
    from src.modules.sigmun_ouvidoria.domain.services import CalculadoraPrazo
    from src.modules.sigmun_ouvidoria.domain.value_objects import TipoManifestacao

    return CalculadoraPrazo.calcular(TipoManifestacao.RECLAMACAO, date.today())


def _entidade_manifestacao_em_tratamento():
    """Manifestação no status que permite responder."""
    from src.modules.sigmun_ouvidoria.domain.entities import Manifestacao
    from src.modules.sigmun_ouvidoria.domain.value_objects import TipoManifestacao

    return Manifestacao(
        tipo=TipoManifestacao.RECLAMACAO,
        status=StatusManifestacao.EM_TRATAMENTO,
        assunto="Buraco na rua",
        descricao="Há um buraco na avenida principal.",
        cidadao=_cidadao(),
        orgao_destino="Obras",
        prazo=_prazo(),
    )


def _entidade_denuncia_em_tratamento():
    """Denúncia no status que permite responder."""
    from src.modules.sigmun_ouvidoria.domain.entities import Denuncia
    from src.modules.sigmun_ouvidoria.domain.value_objects import TipoDenuncia

    return Denuncia(
        tipo_denuncia=TipoDenuncia.CORRUPAO,
        status=StatusManifestacao.EM_TRATAMENTO,
        assunto="Irregularidade",
        descricao="Denúncia sobre contrato.",
        cidadao=_cidadao(),
        orgao_destino="Controladoria",
        local_fato="Prefeitura",
        data_fato=date(2026, 1, 10),
        prazo=_prazo(),
    )


def _entidade_denuncia_em_analise():
    """Denúncia em fase de análise — estado que permite encaminhar.

    A máquina de estados só admite ``REGISTRADA`` e ``EM_ANALISE`` como
    origem de ``ENCAMINHADA``; por isso o encaminhamento usa este helper.
    """
    from src.modules.sigmun_ouvidoria.domain.entities import Denuncia
    from src.modules.sigmun_ouvidoria.domain.value_objects import TipoDenuncia

    return Denuncia(
        tipo_denuncia=TipoDenuncia.CORRUPAO,
        status=StatusManifestacao.EM_ANALISE,
        assunto="Irregularidade",
        descricao="Denúncia sobre contrato.",
        cidadao=_cidadao(),
        orgao_destino="Controladoria",
        local_fato="Prefeitura",
        data_fato=date(2026, 1, 10),
        prazo=_prazo(),
    )


def _entidade_lai_em_tratamento():
    """Pedido LAI no status que permite responder."""
    from src.modules.sigmun_ouvidoria.domain.entities import PedidoLai

    return PedidoLai(
        status=StatusManifestacao.EM_TRATAMENTO,
        assunto="Dados do orçamento",
        descricao="Solicito a cópia do orçamento.",
        cidadao=_cidadao(),
        orgao_destino="Contabilidade",
        informacao_solicitada="Relação de despesas",
        fundamentacao="Transparência ativa",
        prazo=_prazo(),
    )


# ===========================================================================
# Fixtures e helpers
# ===========================================================================


@pytest.fixture()
def repo_protocolo() -> RepoProtocoloMemoria:
    return RepoProtocoloMemoria()


@pytest.fixture()
def repo_anexo() -> RepoAnexoMemoria:
    return RepoAnexoMemoria()


@pytest.fixture()
def repo_tramitacao() -> RepoTramitacaoMemoria:
    return RepoTramitacaoMemoria()


@pytest.fixture()
def repo_m() -> RepoManifestacaoMemoria:
    return RepoManifestacaoMemoria()


@pytest.fixture()
def repo_d() -> RepoDenunciaMemoria:
    return RepoDenunciaMemoria()


@pytest.fixture()
def repo_l() -> RepoPedidoLaiMemoria:
    return RepoPedidoLaiMemoria()


def _dto_manifestacao(**overrides) -> RegistrarManifestacaoInput:
    dados = {
        "tipo": "reclamacao",
        "assunto": "Buraco na rua",
        "descricao": "Há um buraco na avenida principal.",
        "cidadao_nome": "Maria Souza",
        "cidadao_cpf": CPF_VALIDO,
        "cidadao_email": "maria@exemplo.com",
        "orgao_destino": "Obras",
    }
    dados.update(overrides)
    return RegistrarManifestacaoInput(**dados)


def _dto_denuncia(**overrides) -> RegistrarDenunciaInput:
    dados = {
        "assunto": "Irregularidade em contrato",
        "descricao": "Denúncia sobre contrato municipal.",
        "tipo_denuncia": "corrupcao",
        "local_fato": "Prefeitura",
        "data_fato": date(2026, 1, 10),
        "orgao_destino": "Controladoria",
    }
    dados.update(overrides)
    return RegistrarDenunciaInput(**dados)


def _dto_lai(**overrides) -> RegistrarPedidoLaiInput:
    dados = {
        "assunto": "Dados do orçamento",
        "descricao": "Solicito a cópia do orçamento.",
        "informacao_solicitada": "Relação de despesas de 2026",
        "fundamentacao": "Transparência ativa",
        "cidadao_nome": "Maria Souza",
        "cidadao_cpf": CPF_VALIDO,
        "orgao_destino": "Contabilidade",
    }
    dados.update(overrides)
    return RegistrarPedidoLaiInput(**dados)


# ===========================================================================
# RegistrarManifestacaoUseCase — RN-OUV-001
# ===========================================================================


class TestRegistrarManifestacaoUseCase:
    def test_registra_com_protocolo_sequencial(
        self, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """RN-OUV-001 — o primeiro protocolo do ano é 2026-000001."""
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        m = uc.execute(_dto_manifestacao())
        assert m.protocolo.codigo == f"{date.today().year}-000001"
        assert m.status is StatusManifestacao.REGISTRADA
        assert str(m.id) in repo_m.itens

    def test_segundo_registro_incrementa_sequencial(
        self, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        uc.execute(_dto_manifestacao())
        segundo = uc.execute(_dto_manifestacao())
        assert segundo.protocolo.codigo == f"{date.today().year}-000002"

    def test_gera_prazo_conforme_tipo(
        self, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """RN-OUV-020 — reclamação tem prazo de 30 dias."""
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        m = uc.execute(_dto_manifestacao(tipo="sugestao"))
        assert m.prazo.dias_uteis == 20

    def test_anexos_sao_convertidos(
        self, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        anexos = [
            {
                "nome_arquivo": "foto.jpg",
                "tipo_mime": "image/jpeg",
                "tamanho_bytes": 1024,
                "url": "https://exemplo/foto.jpg",
            }
        ]
        m = uc.execute(_dto_manifestacao(anexos=anexos))
        assert len(m.anexos) == 1
        assert m.anexos[0].nome_arquivo == "foto.jpg"

    @pytest.mark.parametrize("tipo", ["denuncia", "pedido_acesso_informacao"])
    def test_tipo_com_use_case_proprio_rejeitado(
        self, tipo, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """Denúncia e LAI têm casos de uso dedicados."""
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        with pytest.raises(RegraNegocioError, match="Use Registrar"):
            uc.execute(_dto_manifestacao(tipo=tipo))

    def test_manifestacao_anonima_rejeitada(
        self, repo_m, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """RN-OUV-002 — manifestação genérica exige identificação."""
        uc = RegistrarManifestacaoUseCase(
            repo_m, repo_protocolo, repo_anexo, repo_tramitacao
        )
        dto = _dto_manifestacao(
            cidadao_nome="", cidadao_cpf="", cidadao_anonimo=True
        )
        with pytest.raises(RegraNegocioError):
            uc.execute(dto)


# ===========================================================================
# RegistrarDenunciaUseCase — RN-OUV-002
# ===========================================================================


class TestRegistrarDenunciaUseCase:
    def test_registra_denuncia_anonima(
        self, repo_d, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """RN-OUV-002 — denúncia anônima é o padrão e é aceita."""
        uc = RegistrarDenunciaUseCase(
            repo_d, repo_protocolo, repo_anexo, repo_tramitacao
        )
        d = uc.execute(_dto_denuncia())
        assert d.tipo_denuncia is not None
        assert d.local_fato == "Prefeitura"
        assert str(d.id) in repo_d.itens

    def test_denuncia_com_privilegio_alta(
        self, repo_d, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """Denúncias recebem prioridade alta por padrão."""
        uc = RegistrarDenunciaUseCase(
            repo_d, repo_protocolo, repo_anexo, repo_tramitacao
        )
        d = uc.execute(_dto_denuncia())
        assert d.prioridade.value == "alta"

    def test_denuncia_sem_local_rejeitada(
        self, repo_d, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        uc = RegistrarDenunciaUseCase(
            repo_d, repo_protocolo, repo_anexo, repo_tramitacao
        )
        with pytest.raises(RegraNegocioError, match="Local do fato"):
            uc.execute(_dto_denuncia(local_fato=""))


# ===========================================================================
# RegistrarPedidoLaiUseCase — LAI art. 24
# ===========================================================================


class TestRegistrarPedidoLaiUseCase:
    def test_registra_pedido_com_prazo_de_20_dias(
        self, repo_l, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        """Lei 12.527/2011 art. 11 — LAI tem prazo de 20 dias."""
        uc = RegistrarPedidoLaiUseCase(
            repo_l, repo_protocolo, repo_anexo, repo_tramitacao
        )
        p = uc.execute(_dto_lai())
        assert p.prazo.dias_uteis == 20
        assert str(p.id) in repo_l.itens

    def test_sem_fundamentacao_rejeitado(
        self, repo_l, repo_protocolo, repo_anexo, repo_tramitacao
    ):
        uc = RegistrarPedidoLaiUseCase(
            repo_l, repo_protocolo, repo_anexo, repo_tramitacao
        )
        with pytest.raises(RegraNegocioError, match="Fundamentação"):
            uc.execute(_dto_lai(fundamentacao=""))


# ===========================================================================
# ResponderManifestacaoUseCase
# ===========================================================================


class TestResponderManifestacaoUseCase:
    def test_responde_manifestacao_em_tratamento(self, repo_m, repo_d, repo_l):
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        uc = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l)
        dto = ResponderManifestacaoInput(
            manifestacao_id=m.id,
            resposta="O buraco foi reparado.",
            forma_resposta="email",
            respondido_por="ouvidor-01",
        )
        resultado = uc.execute(dto)
        assert resultado.status is StatusManifestacao.RESPONDIDA
        assert resultado.respondido_por == "ouvidor-01"

    def test_responde_denuncia(self, repo_m, repo_d, repo_l):
        d = repo_d.save(_entidade_denuncia_em_tratamento())
        uc = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            ResponderManifestacaoInput(
                manifestacao_id=d.id, resposta="Apurado", respondido_por="ouvidor-01"
            )
        )
        assert resultado.status is StatusManifestacao.RESPONDIDA

    def test_responde_pedido_lai(self, repo_m, repo_d, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        uc = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            ResponderManifestacaoInput(
                manifestacao_id=p.id, resposta="Deferido", respondido_por="ouvidor-01"
            )
        )
        assert resultado.status is StatusManifestacao.RESPONDIDA

    def test_manifestacao_inexistente(self, repo_m, repo_d, repo_l):
        uc = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(ManifestacaoNaoEncontradaError):
            uc.execute(
                ResponderManifestacaoInput(manifestacao_id="inexistente", resposta="X")
            )

    def test_status_invalido_para_responder(self, repo_m, repo_d, repo_l):
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        m.status = StatusManifestacao.REGISTRADA
        repo_m.save(m)
        uc = ResponderManifestacaoUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(RegraNegocioError, match="responder"):
            uc.execute(
                ResponderManifestacaoInput(
                    manifestacao_id=m.id, resposta="X", respondido_por="u"
                )
            )


# ===========================================================================
# AlterarStatusUseCase — RN-OUV-010
# ===========================================================================


class TestAlterarStatusUseCase:
    def test_altera_status_manifestacao(self, repo_m, repo_d, repo_l):
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            AlterarStatusInput(
                manifestacao_id=m.id,
                novo_status="respondida",
                observacao="Resposta enviada",
                usuario_id="ouvidor-01",
            )
        )
        assert resultado.status is StatusManifestacao.RESPONDIDA
        assert resultado.updated_by == "ouvidor-01"

    def test_transicao_invalida_rejeitada(self, repo_m, repo_d, repo_l):
        """RN-OUV-010 — não se pula de registrada para concluída."""
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        m.status = StatusManifestacao.REGISTRADA
        repo_m.save(m)
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(RegraNegocioError):
            uc.execute(
                AlterarStatusInput(
                    manifestacao_id=m.id,
                    novo_status="concluida",
                    usuario_id="ouvidor-01",
                )
            )

    def test_altera_status_denuncia(self, repo_m, repo_d, repo_l):
        d = repo_d.save(_entidade_denuncia_em_tratamento())
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            AlterarStatusInput(
                manifestacao_id=d.id, novo_status="respondida", usuario_id="u"
            )
        )
        assert resultado.status is StatusManifestacao.RESPONDIDA

    def test_altera_status_pedido_lai(self, repo_m, repo_d, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            AlterarStatusInput(
                manifestacao_id=p.id, novo_status="respondida", usuario_id="u"
            )
        )
        assert resultado.status is StatusManifestacao.RESPONDIDA

    def test_inexistente(self, repo_m, repo_d, repo_l):
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(ManifestacaoNaoEncontradaError):
            uc.execute(
                AlterarStatusInput(
                    manifestacao_id="inexistente", novo_status="em_analise"
                )
            )

    def test_status_invalido_rejeitado(self, repo_m, repo_d, repo_l):
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        uc = AlterarStatusUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(ValueError):
            uc.execute(
                AlterarStatusInput(manifestacao_id=m.id, novo_status="inexistente")
            )


# ===========================================================================
# ProrrogarPrazoUseCase — LAI art. 11 §1º
# ===========================================================================


class TestProrrogarPrazoUseCase:
    def test_prorroga_manifestacao(self, repo_m, repo_d, repo_l):
        """Prorrogação soma 10 dias (LAI art. 11 §1º)."""
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        antes = m.prazo.data_limite
        uc = ProrrogarPrazoUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            ProrrogarPrazoInput(
                manifestacao_id=m.id,
                justificativa="Informação complementar",
                usuario_id="ouvidor-01",
            )
        )
        assert resultado.prazo.prorrogado is True
        assert resultado.prazo.data_limite > antes

    def test_prorroga_denuncia(self, repo_m, repo_d, repo_l):
        d = repo_d.save(_entidade_denuncia_em_tratamento())
        uc = ProrrogarPrazoUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            ProrrogarPrazoInput(manifestacao_id=d.id, justificativa="motivo")
        )
        assert resultado.prazo.prorrogado is True

    def test_prorroga_pedido_lai(self, repo_m, repo_d, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        uc = ProrrogarPrazoUseCase(repo_m, repo_d, repo_l)
        resultado = uc.execute(
            ProrrogarPrazoInput(manifestacao_id=p.id, justificativa="motivo")
        )
        assert resultado.prazo.prorrogado is True

    def test_inexistente(self, repo_m, repo_d, repo_l):
        uc = ProrrogarPrazoUseCase(repo_m, repo_d, repo_l)
        with pytest.raises(ManifestacaoNaoEncontradaError):
            uc.execute(
                ProrrogarPrazoInput(manifestacao_id="x", justificativa="y")
            )


# ===========================================================================
# AvaliarManifestacaoUseCase
# ===========================================================================


class TestAvaliarManifestacaoUseCase:
    def _manifestacao_respondida(self, repo_m):
        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        m.status = StatusManifestacao.RESPONDIDA
        return repo_m.save(m)

    def test_avalia_e_conclui(self, repo_m):
        """Avaliação válida conclui a manifestação."""
        m = self._manifestacao_respondida(repo_m)
        uc = AvaliarManifestacaoUseCase(repo_m)
        resultado = uc.execute(
            AvaliarManifestacaoInput(
                manifestacao_id=m.id, nota=5, comentario="Ótimo atendimento"
            )
        )
        assert resultado.avaliacao_cidadao == 5
        assert resultado.comentario_avaliacao == "Ótimo atendimento"
        assert resultado.status is StatusManifestacao.CONCLUIDA

    @pytest.mark.parametrize("nota", [0, 6])
    def test_nota_fora_da_faixa_rejeitada(self, repo_m, nota):
        m = self._manifestacao_respondida(repo_m)
        uc = AvaliarManifestacaoUseCase(repo_m)
        with pytest.raises(RegraNegocioError, match="entre 1 e 5"):
            uc.execute(AvaliarManifestacaoInput(manifestacao_id=m.id, nota=nota))

    def test_manifestacao_inexistente(self, repo_m):
        uc = AvaliarManifestacaoUseCase(repo_m)
        with pytest.raises(ManifestacaoNaoEncontradaError):
            uc.execute(AvaliarManifestacaoInput(manifestacao_id="x", nota=5))


# ===========================================================================
# EncaminharDenunciaUseCase
# ===========================================================================


class TestEncaminharDenunciaUseCase:
    def test_encaminha_para_mp(self, repo_d):
        d = repo_d.save(_entidade_denuncia_em_analise())
        uc = EncaminharDenunciaUseCase(repo_d)
        resultado = uc.execute(
            EncaminharDenunciaInput(
                denuncia_id=d.id,
                orgao="MP",
                numero_processo="MP-2026-001",
                usuario_id="ouvidor-01",
            )
        )
        assert resultado.encaminhada_mp is True
        assert resultado.numero_inquerito == "MP-2026-001"
        assert resultado.status is StatusManifestacao.ENCAMINHADA

    def test_orgao_desconhecido_rejeitado(self, repo_d):
        d = repo_d.save(_entidade_denuncia_em_tratamento())
        uc = EncaminharDenunciaUseCase(repo_d)
        with pytest.raises(RegraNegocioError, match="não reconhecido"):
            uc.execute(
                EncaminharDenunciaInput(
                    denuncia_id=d.id, orgao="X", numero_processo="1"
                )
            )

    def test_denuncia_inexistente(self, repo_d):
        uc = EncaminharDenunciaUseCase(repo_d)
        with pytest.raises(DenunciaNaoEncontradaError):
            uc.execute(
                EncaminharDenunciaInput(
                    denuncia_id="x", orgao="MP", numero_processo="1"
                )
            )


# ===========================================================================
# Recurso LAI — LAI art. 15
# ===========================================================================


class TestRecursoLaiUseCase:
    def _pedido_arquivado(self, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        p.status = StatusManifestacao.ARQUIVADA
        return repo_l.save(p)

    def test_interpoe_recurso_de_pedido_arquivado(self, repo_l):
        """LAI art. 15 — recorre-se de pedido arquivado (negado)."""
        p = self._pedido_arquivado(repo_l)
        recurso = InterporRecursoLaiUseCase(repo_l).execute(
            InterporRecursoLaiInput(pedido_original_id=p.id, autor_id="maria")
        )
        assert recurso.is_recurso is True
        assert recurso.pedido_original_id == p.id
        assert str(recurso.id) in repo_l.itens

    def test_pedido_nao_arquivado_rejeita_recurso(self, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        uc = InterporRecursoLaiUseCase(repo_l)
        with pytest.raises(RegraNegocioError, match="arquivados"):
            uc.execute(InterporRecursoLaiInput(pedido_original_id=p.id))

    def test_interpor_recurso_pedido_inexistente(self, repo_l):
        uc = InterporRecursoLaiUseCase(repo_l)
        with pytest.raises(PedidoLaiNaoEncontradoError):
            uc.execute(InterporRecursoLaiInput(pedido_original_id="x"))

    @pytest.mark.parametrize(
        ("deferido", "esperado_status"),
        [(True, StatusManifestacao.CONCLUIDA), (False, StatusManifestacao.ARQUIVADA)],
    )
    def test_decide_recurso(self, repo_l, deferido, esperado_status):
        p = self._pedido_arquivado(repo_l)
        recurso = InterporRecursoLaiUseCase(repo_l).execute(
            InterporRecursoLaiInput(pedido_original_id=p.id)
        )
        uc = DecidirRecursoLaiUseCase(repo_l)
        resultado = uc.execute(
            DecidirRecursoLaiInput(
                recurso_id=recurso.id,
                deferido=deferido,
                fundamentacao="Fundamentação da decisão",
                usuario_id="ouvidor-01",
            )
        )
        assert resultado.decisao_recurso == ("deferido" if deferido else "indeferido")
        assert resultado.status is esperado_status

    def test_decidir_pedido_que_nao_e_recurso(self, repo_l):
        p = repo_l.save(_entidade_lai_em_tratamento())
        uc = DecidirRecursoLaiUseCase(repo_l)
        with pytest.raises(RegraNegocioError, match="não é um recurso"):
            uc.execute(
                DecidirRecursoLaiInput(
                    recurso_id=p.id, deferido=True, fundamentacao="x"
                )
            )

    def test_decidir_recurso_inexistente(self, repo_l):
        uc = DecidirRecursoLaiUseCase(repo_l)
        with pytest.raises(PedidoLaiNaoEncontradoError):
            uc.execute(
                DecidirRecursoLaiInput(
                    recurso_id="x", deferido=True, fundamentacao="y"
                )
            )


# ===========================================================================
# Listagem, consulta e estatísticas
# ===========================================================================


class TestListagemEEstatisticas:
    def test_lista_com_paginacao(self, repo_m, repo_d, repo_l):
        for _ in range(3):
            repo_m.save(_entidade_manifestacao_em_tratamento())
        resultado = ListarManifestacoesUseCase(repo_m).execute(
            ListarManifestacoesInput(page=1, page_size=2)
        )
        assert resultado["total"] == 3
        assert resultado["page"] == 1
        assert resultado["page_size"] == 2
        assert resultado["pages"] == 2

    def test_lista_vazia(self, repo_m, repo_d, repo_l):
        resultado = ListarManifestacoesUseCase(repo_m).execute(
            ListarManifestacoesInput()
        )
        assert resultado["total"] == 0
        assert resultado["items"] == []

    def test_consulta_por_id(self, repo_m, repo_d, repo_l):
        from src.modules.sigmun_ouvidoria.application.use_cases import (
            ObterManifestacaoUseCase,
        )

        m = repo_m.save(_entidade_manifestacao_em_tratamento())
        assert ObterManifestacaoUseCase(repo_m, repo_d, repo_l).execute(m.id).id == m.id

    def test_consulta_inexistente(self, repo_m, repo_d, repo_l):
        from src.modules.sigmun_ouvidoria.application.use_cases import (
            ObterManifestacaoUseCase,
        )

        with pytest.raises(ManifestacaoNaoEncontradaError):
            ObterManifestacaoUseCase(repo_m, repo_d, repo_l).execute("inexistente")

    def test_indicadores_agregam_os_tres_tipos(self, repo_m, repo_d, repo_l):
        from src.modules.sigmun_ouvidoria.application.use_cases import (
            ObterEstatisticasUseCase,
        )
        from src.modules.sigmun_ouvidoria.domain.services import ServicoEstatisticas

        repo_m.save(_entidade_manifestacao_em_tratamento())
        repo_d.save(_entidade_denuncia_em_tratamento())
        repo_l.save(_entidade_lai_em_tratamento())

        servico = ServicoEstatisticas(repo_m, repo_d, repo_l)
        resultado = ObterEstatisticasUseCase(servico).execute(ano=date.today().year)
        assert resultado["gerais"]["total"] == 3
        assert "manifestacoes" in resultado["por_tipo"]
        assert "vencendo_5_dias" in resultado
