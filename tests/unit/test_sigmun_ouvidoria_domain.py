"""Testes unitários do domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal).

Cobre as regras de negócio sem depender de banco:

- RN-OUV-001 — protocolo único no formato ``AAAA-NNNNNN``;
- RN-OUV-002 — denúncia pode ser anônima; demais tipos exigem identificação;
- RN-OUV-003 / LAI art. 11 — prazo de 20 dias, prorrogável por mais 10;
- RN-OUV-010 — transições de status controladas pelo fluxo FalaBR;
- RN-OUV-020 — prazos por tipo de manifestação;
- RN-OUV-030 — sigilo e mascaramento dos dados do denunciante (LGPD).
"""

from __future__ import annotations

from datetime import date, timedelta

import pytest

from src.modules.sigmun_ouvidoria.domain.entities import (
    Denuncia,
    Manifestacao,
    PedidoLai,
    Prioridade,
)
from src.modules.sigmun_ouvidoria.domain.exceptions import (
    AcessoNegadoError,
    EstadoInvalidoError,
    RegraNegocioError,
)
from src.modules.sigmun_ouvidoria.domain.services import (
    CalculadoraPrazo,
    ServicoLGPD,
    ValidadorManifestacao,
)
from src.modules.sigmun_ouvidoria.domain.value_objects import (
    Anexo,
    CanalRecebimento,
    DadosCidadao,
    FormaResposta,
    NivelSigilo,
    PrazoResposta,
    Protocolo,
    StatusManifestacao,
    TipoDenuncia,
    TipoManifestacao,
)

# CPF válido de teste (dígitos verificadores conferidos pelo domínio).
CPF_VALIDO = "52998224725"


def _cidadao(anonimo: bool = False) -> DadosCidadao:
    if anonimo:
        return DadosCidadao(nome="", anonimo=True)
    return DadosCidadao(
        nome="Maria Souza",
        cpf=CPF_VALIDO,
        email="maria@exemplo.com",
        telefone="71999998888",
    )


def _manifestacao(**overrides) -> Manifestacao:
    """Manifestação genérica válida (status registrada)."""
    dados = {
        "tipo": TipoManifestacao.RECLAMACAO,
        "status": StatusManifestacao.REGISTRADA,
        "assunto": "Buraco na rua",
        "descricao": "Há um buraco na avenida principal.",
        "cidadao": _cidadao(),
        "orgao_destino": "Obras",
        "prazo": CalculadoraPrazo.calcular(TipoManifestacao.RECLAMACAO, date.today()),
    }
    dados.update(overrides)
    return Manifestacao(**dados)


def _denuncia(**overrides) -> Denuncia:
    dados = {
        "tipo": TipoManifestacao.DENUNCIA,
        "tipo_denuncia": TipoDenuncia.CORRUPAO,
        "assunto": "Irregularidade em contrato",
        "descricao": "Denúncia sobre contrato municipal.",
        "cidadao": _cidadao(anonimo=True),
        "orgao_destino": "Controladoria",
        "local_fato": "Prefeitura",
        "data_fato": date(2026, 1, 10),
        "status": StatusManifestacao.REGISTRADA,
    }
    dados.update(overrides)
    return Denuncia(**dados)


def _pedido_lai(**overrides) -> PedidoLai:
    dados = {
        "assunto": "Dados do orçamento",
        "descricao": "Solicito a cópia do orçamento municipal.",
        "cidadao": _cidadao(),
        "orgao_destino": "Contabilidade",
        "informacao_solicitada": "Relação de despesas de 2026",
        "fundamentacao": "Transparência ativa",
    }
    dados.update(overrides)
    return PedidoLai(**dados)


# ===========================================================================
# RN-OUV-001 — Protocolo
# ===========================================================================


class TestProtocolo:
    def test_gerar_formata_com_seis_digitos(self):
        protocolo = Protocolo.gerar(2026, 42)
        assert protocolo.codigo == "2026-000042"
        assert protocolo.numero == "000042"

    @pytest.mark.parametrize(
        "numero",
        ["12345", "1234567", "abcdef"],
    )
    def test_numero_invalido_rejeitado(self, numero):
        with pytest.raises(ValueError, match="6 dígitos"):
            Protocolo(numero=numero, ano=2026)

    @pytest.mark.parametrize("numero", ["", None])
    def test_numero_vazio_rejeitado(self, numero):
        with pytest.raises(ValueError, match="número e ano"):
            Protocolo(numero=numero, ano=2026)

    def test_str_retorna_codigo(self):
        assert str(Protocolo.gerar(2026, 7)) == "2026-000007"


# ===========================================================================
# RN-OUV-010 — Transições de status
# ===========================================================================


class TestTransicoesDeStatus:
    @pytest.mark.parametrize(
        ("origem", "destino"),
        [
            (StatusManifestacao.REGISTRADA, StatusManifestacao.EM_ANALISE),
            (StatusManifestacao.REGISTRADA, StatusManifestacao.ENCAMINHADA),
            (StatusManifestacao.REGISTRADA, StatusManifestacao.CANCELADA),
            (StatusManifestacao.EM_ANALISE, StatusManifestacao.EM_TRATAMENTO),
            (StatusManifestacao.ENCAMINHADA, StatusManifestacao.EM_TRATAMENTO),
            (StatusManifestacao.EM_TRATAMENTO, StatusManifestacao.RESPONDIDA),
            (StatusManifestacao.AGUARDANDO_COMPLEMENTACAO, StatusManifestacao.RESPONDIDA),
            (StatusManifestacao.RESPONDIDA, StatusManifestacao.CONCLUIDA),
            (StatusManifestacao.RESPONDIDA, StatusManifestacao.ARQUIVADA),
            (StatusManifestacao.CONCLUIDA, StatusManifestacao.ARQUIVADA),
        ],
    )
    def test_transicao_valida_permitida(self, origem, destino):
        assert origem.pode_transicionar_para(destino) is True

    @pytest.mark.parametrize(
        ("origem", "destino"),
        [
            # Não se pula a triagem.
            (StatusManifestacao.REGISTRADA, StatusManifestacao.RESPONDIDA),
            (StatusManifestacao.REGISTRADA, StatusManifestacao.CONCLUIDA),
            (StatusManifestacao.EM_ANALISE, StatusManifestacao.RESPONDIDA),
            # Estados finais não avançam.
            (StatusManifestacao.ARQUIVADA, StatusManifestacao.CONCLUIDA),
            (StatusManifestacao.CANCELADA, StatusManifestacao.EM_ANALISE),
            (StatusManifestacao.EM_TRATAMENTO, StatusManifestacao.CONCLUIDA),
        ],
    )
    def test_transicao_invalida_proibida(self, origem, destino):
        assert origem.pode_transicionar_para(destino) is False

    def test_alterar_status_atualiza_campos_de_auditoria(self):
        m = _manifestacao()
        m.alterar_status(StatusManifestacao.EM_ANALISE, usuario="ouvidor-01")
        assert m.status is StatusManifestacao.EM_ANALISE
        assert m.updated_by == "ouvidor-01"
        assert m.updated_at is not None

    def test_alterar_status_invalido_lanca_erro(self):
        m = _manifestacao()
        with pytest.raises(EstadoInvalidoError, match="Transição inválida"):
            m.alterar_status(StatusManifestacao.CONCLUIDA, usuario="ouvidor-01")


# ===========================================================================
# RN-OUV-020 e LAI art. 11 — Prazos
# ===========================================================================


class TestCalculadoraPrazo:
    @pytest.mark.parametrize(
        ("tipo", "dias"),
        [
            (TipoManifestacao.SUGESTAO, 20),
            (TipoManifestacao.ELOGIO, 20),
            (TipoManifestacao.RECLAMACAO, 30),
            (TipoManifestacao.SOLICITACAO, 30),
            (TipoManifestacao.DENUNCIA, 30),
            (TipoManifestacao.PEDIDO_ACESSO_INFORMACAO, 20),
        ],
    )
    def test_prazo_por_tipo(self, tipo, dias):
        """Lei 12.527/2011 art. 11: LAI = 20 dias."""
        inicio = date(2026, 1, 1)
        prazo = CalculadoraPrazo.calcular(tipo, inicio)
        assert prazo.data_limite == inicio + timedelta(days=dias)
        assert prazo.prorrogado is False

    def test_prorrogacao_soma_dez_dias(self):
        """LAI art. 11 §1º — prorrogação por mais 10 dias."""
        inicio = date(2026, 1, 1)
        prazo = CalculadoraPrazo.calcular(
            TipoManifestacao.PEDIDO_ACESSO_INFORMACAO, inicio, prorrogacao=True
        )
        assert prazo.data_limite == inicio + timedelta(days=30)
        assert prazo.prorrogado is True

    def test_calcular_prorrogacao_avanca_dez_dias(self):
        base = CalculadoraPrazo.calcular(TipoManifestacao.RECLAMACAO, date(2026, 1, 1))
        nova = CalculadoraPrazo.calcular_prorrogacao(base, "Informação complementar")
        assert nova.data_limite == base.data_limite + timedelta(days=10)
        assert nova.justificativa_prorrogacao == "Informação complementar"
        assert nova.data_prorrogacao == date.today()

    def test_prorrogacao_duplicada_rejeitada(self):
        base = CalculadoraPrazo.calcular(TipoManifestacao.RECLAMACAO, date(2026, 1, 1))
        primeira = CalculadoraPrazo.calcular_prorrogacao(base, "motivo")
        with pytest.raises(RegraNegocioError, match="já foi prorrogado"):
            CalculadoraPrazo.calcular_prorrogacao(primeira, "outro")

    def test_vencimento(self):
        vencido = PrazoResposta(data_limite=date.today() - timedelta(days=1), dias_uteis=20)
        vigente = PrazoResposta(data_limite=date.today() + timedelta(days=5), dias_uteis=20)
        assert vencido.vencido is True
        assert vigente.vencido is False
        assert vigente.dias_restantes == 5

    def test_prorrogar_prazo_na_entidade(self):
        m = _manifestacao()
        m.prorrogar_prazo("Informação complementar", usuario="ouvidor-01")
        assert m.prazo.prorrogado is True
        assert m.prazo.justificativa_prorrogacao == "Informação complementar"

    def test_prorrogar_sem_prazo_rejeitado(self):
        with pytest.raises(RegraNegocioError, match="Não há prazo"):
            _manifestacao(prazo=None).prorrogar_prazo("motivo")

    def test_prorrogar_duas_vezes_rejeitado(self):
        m = _manifestacao()
        m.prorrogar_prazo("primeira")
        with pytest.raises(RegraNegocioError, match="já foi prorrogado"):
            m.prorrogar_prazo("segunda")

    def test_verificar_prazo_sem_prazo_nao_vence(self):
        assert _manifestacao(prazo=None).verificar_prazo() is False


# ===========================================================================
# RN-OUV-030 e LGPD — Dados do cidadão
# ===========================================================================


class TestDadosCidadao:
    def test_cpf_invalido_rejeitado(self):
        with pytest.raises(ValueError, match="CPF inválido"):
            DadosCidadao(nome="X", cpf="11111111111")

    def test_email_invalido_rejeitado(self):
        with pytest.raises(ValueError, match="E-mail inválido"):
            DadosCidadao(nome="X", email="email-sem-arroba")

    def test_nome_obrigatorio_quando_identificado(self):
        with pytest.raises(ValueError, match="Nome é obrigatório"):
            DadosCidadao(nome="", anonimo=False)

    def test_anonimo_nao_exige_nome(self):
        assert DadosCidadao(nome="", anonimo=True).anonimo is True

    def test_mascaramento_cpf_e_email(self):
        """RN-OUV-030 — o domínio entrega dados prontos para exibição."""
        exibicao = _cidadao().para_exibicao()
        assert exibicao["cpf"] == "***.982.***-25"
        assert exibicao["email"] == "m***@exemplo.com"
        assert exibicao["nome"] == "Maria Souza"

    def test_exibicao_anonima_nao_traz_identificacao(self):
        assert _cidadao(anonimo=True).para_exibicao() == {"anonimo": True}

    def test_servico_lgpd_mascara(self):
        assert ServicoLGPD.mascarar_para_exibicao(_cidadao())["cpf"].startswith("***")

    def test_servico_lgpd_anonimiza(self):
        anonimo = ServicoLGPD.anonimizar_dados_cidadao(_cidadao())
        assert anonimo.anonimo is True
        assert anonimo.cpf is None

    @pytest.mark.parametrize(
        ("papel", "esperado"),
        [
            ("ouvidor", True),
            ("corregedor", True),
            ("auditor", True),
            # ADR-0008 §2.3: administração técnica não acessa o dado sensível.
            ("admin", False),
            ("servidor", False),
        ],
    )
    def test_acesso_a_dados_sensiveis_por_papel(self, papel, esperado):
        assert ServicoLGPD.pode_acessar_dados_sensiveis(papel) is esperado


# ===========================================================================
# RN-OUV-002 — Validação estrutural
# ===========================================================================


class TestValidacaoManifestacao:
    def test_manifestacao_valida_nao_lanca(self):
        _manifestacao().validar()  # não deve levantar

    @pytest.mark.parametrize(
        ("campo", "mensagem"),
        [
            ("assunto", "Assunto é obrigatório"),
            ("descricao", "Descrição é obrigatória"),
            ("orgao_destino", "Órgão de destino é obrigatório"),
        ],
    )
    def test_campos_obrigatorios(self, campo, mensagem):
        with pytest.raises(RegraNegocioError, match=mensagem):
            _manifestacao(**{campo: ""}).validar()

    def test_manifestacao_anonima_sem_identificacao_rejeitada(self):
        """RN-OUV-002 — apenas denúncia pode ser anônima."""
        m = _manifestacao(cidadao=_cidadao(anonimo=True))
        with pytest.raises(RegraNegocioError, match="exigem identificação"):
            m.validar()

    def test_manifestacao_sem_cidadao_rejeitada(self):
        with pytest.raises(RegraNegocioError, match="exigem identificação"):
            _manifestacao(cidadao=None).validar()

    def test_denuncia_anonima_e_aceita(self):
        """RN-OUV-002 — denúncia anônima é permitida."""
        d = _denuncia()
        d.validar()  # não deve levantar
        assert d.tipo is TipoManifestacao.DENUNCIA

    def test_denuncia_sem_local_rejeitada(self):
        d = _denuncia(local_fato="")
        with pytest.raises(RegraNegocioError, match="Local do fato"):
            d.validar()

    def test_denuncia_sem_data_rejeitada(self):
        d = _denuncia(data_fato=None)
        with pytest.raises(RegraNegocioError, match="Data do fato"):
            d.validar()


# ===========================================================================
# Manifestação — resposta e avaliação
# ===========================================================================


class TestRespostaEAvaliacao:
    def test_responde_somente_em_tratamento(self):
        m = _manifestacao()
        with pytest.raises(EstadoInvalidoError, match="em tratamento"):
            m.registrar_resposta("Resposta", FormaResposta.PORTAL, "ouvidor-01")

    def test_resposta_muda_status_para_respondida(self):
        m = _manifestacao(status=StatusManifestacao.EM_TRATAMENTO)
        m.registrar_resposta("O buraco foi reparado.", FormaResposta.EMAIL, "ouvidor-01")
        assert m.status is StatusManifestacao.RESPONDIDA
        assert m.resposta == "O buraco foi reparado."
        assert m.data_resposta == date.today()

    def test_avaliacao_exige_status_respondida(self):
        with pytest.raises(EstadoInvalidoError, match="respondidas"):
            _manifestacao().avaliar(5)

    @pytest.mark.parametrize("nota", [0, 6, -1])
    def test_avaliacao_fora_da_faixa_rejeitada(self, nota):
        m = _manifestacao(status=StatusManifestacao.RESPONDIDA)
        with pytest.raises(RegraNegocioError, match="entre 1 e 5"):
            m.avaliar(nota)

    def test_avaliacao_valida_conclui_manifestacao(self):
        m = _manifestacao(status=StatusManifestacao.RESPONDIDA)
        m.avaliar(4, "Atendimento rápido")
        assert m.avaliacao_cidadao == 4
        assert m.status is StatusManifestacao.CONCLUIDA


# ===========================================================================
# Denúncia — encaminhamento e sigilo
# ===========================================================================


class TestDenuncia:
    @pytest.mark.parametrize(
        ("orgao", "atributo"),
        [
            ("MP", "encaminhada_mp"),
            ("PF", "encaminhada_pf"),
            ("TCE", "encaminhada_tce"),
        ],
    )
    def test_encaminhar_marca_orgao_correspondente(self, orgao, atributo):
        d = _denuncia()
        d.encaminhar_orgao_externo(orgao, "MP-2026-001", "ouvidor-01")
        assert getattr(d, atributo) is True
        assert d.numero_inquerito == "MP-2026-001"
        assert d.status is StatusManifestacao.ENCAMINHADA

    def test_encaminhar_aceita_minusculo(self):
        d = _denuncia()
        d.encaminhar_orgao_externo("mp", "X-1", "ouvidor-01")
        assert d.encaminhada_mp is True

    def test_dados_sigilosos_negados_a_nao_autorizado(self):
        """RN-OUV-030 — o domínio barra o acesso não autorizado."""
        d = _denuncia(cidadao=_cidadao())
        with pytest.raises(AcessoNegadoError, match="restrito"):
            d.get_dados_sigilosos(usuario_autorizado=False)

    def test_dados_sigilosos_mascarados_para_autorizado(self):
        d = _denuncia(cidadao=_cidadao())
        dados = d.get_dados_sigilosos(usuario_autorizado=True)
        assert dados["cpf"] == "***.982.***-25"

    def test_dados_sigilosos_vazio_sem_cidadao(self):
        d = _denuncia(cidadao=None)
        assert d.get_dados_sigilosos(usuario_autorizado=True) == {}

    def test_concluir_investigacao(self):
        d = _denuncia(status=StatusManifestacao.EM_TRATAMENTO)
        d.concluir_investigacao("Procedente", "controlador-01")
        assert d.resultado_investigacao == "Procedente"
        assert d.status is StatusManifestacao.CONCLUIDA


# ===========================================================================
# Pedido LAI
# ===========================================================================


class TestPedidoLai:
    def test_valido_ajusta_o_tipo(self):
        p = _pedido_lai()
        p.validar()
        assert p.tipo is TipoManifestacao.PEDIDO_ACESSO_INFORMACAO

    def test_sem_informacao_solicitada_rejeitado(self):
        with pytest.raises(RegraNegocioError, match="Informação solicitada"):
            _pedido_lai(informacao_solicitada="").validar()

    def test_sem_fundamentacao_rejeitado(self):
        """LAI art. 24 — a fundamentação é obrigatória."""
        with pytest.raises(RegraNegocioError, match="Fundamentação é obrigatória"):
            _pedido_lai(fundamentacao="").validar()

    def test_sigilo_nao_publico_exige_fundamentacao(self):
        with pytest.raises(RegraNegocioError, match="Fundamentação do sigilo"):
            _pedido_lai(nivel_sigilo=NivelSigilo.SIGILOSO).validar()

    def test_classificar_sigilo(self):
        p = _pedido_lai()
        p.classificar_sigilo(NivelSigilo.RESTRITO, "Dados pessoais", "ouvidor-01")
        assert p.nivel_sigilo is NivelSigilo.RESTRITO
        assert p.fundamentacao_sigilo == "Dados pessoais"
        assert p.updated_by == "ouvidor-01"

    def test_interpor_recurso_cria_novo_pedido_vinculado(self):
        """LAI art. 15 — recurso de pedido negado."""
        original = _pedido_lai()
        recurso = original.interpor_recurso(original.id)
        assert recurso.is_recurso is True
        assert recurso.pedido_original_id == original.id
        assert recurso.assunto == f"Recurso - {original.assunto}"
        assert recurso.fundamentacao.startswith("RECURSO:")

    def test_decidir_recurso_deferido_conclui(self):
        recurso = _pedido_lai(is_recurso=True)
        recurso.decidir_recurso(True, "Deferido", "ouvidor-01")
        assert recurso.decisao_recurso == "deferido"
        assert recurso.status is StatusManifestacao.CONCLUIDA

    def test_decidir_recurso_indeferido_arquiva(self):
        recurso = _pedido_lai(is_recurso=True)
        recurso.decidir_recurso(False, "Indeferido", "ouvidor-01")
        assert recurso.decisao_recurso == "indeferido"
        assert recurso.status is StatusManifestacao.ARQUIVADA

    def test_decidir_pedido_que_nao_e_recurso_rejeitado(self):
        with pytest.raises(RegraNegocioError, match="não é um recurso"):
            _pedido_lai().decidir_recurso(True, "motivo", "ouvidor-01")


# ===========================================================================
# Serviços de domínio
# ===========================================================================


class TestValidadorManifestacao:
    def test_avisa_ausencia_de_prazo(self):
        avisos = ValidadorManifestacao().validar_criacao(_manifestacao(prazo=None))
        assert any("prazo" in a.lower() for a in avisos)

    def test_avisa_denuncia_identificada(self):
        d = _denuncia(cidadao=_cidadao(), prazo=None)
        avisos = ValidadorManifestacao().validar_criacao(d)
        assert any("sigilo" in a.lower() for a in avisos)

    def test_manifestacao_completa_sem_avisos(self):
        assert ValidadorManifestacao().validar_criacao(_manifestacao()) == []

    def test_validar_resposta_bloqueia_status_invalido(self):
        with pytest.raises(RegraNegocioError, match="Não é possível responder"):
            ValidadorManifestacao().validar_resposta(_manifestacao())

    def test_validar_resposta_permite_em_tratamento(self):
        ValidadorManifestacao().validar_resposta(
            _manifestacao(status=StatusManifestacao.EM_TRATAMENTO)
        )

    def test_validar_transicao_bloqueia_pulo_de_etapa(self):
        with pytest.raises(RegraNegocioError):
            ValidadorManifestacao().validar_transicao_status(
                StatusManifestacao.REGISTRADA, StatusManifestacao.RESPONDIDA
            )


class TestPrioridade:
    @pytest.mark.parametrize(
        ("valor", "rotulo"),
        [
            (Prioridade.BAIXA, "Baixa"),
            (Prioridade.NORMAL, "Normal"),
            (Prioridade.ALTA, "Alta"),
            (Prioridade.URGENTE, "Urgente"),
        ],
    )
    def test_rotulos(self, valor, rotulo):
        assert valor.rotulo == rotulo


class TestExclusaoLogica:
    def test_excluir_marca_is_deleted(self):
        m = _manifestacao()
        m.excluir()
        assert m.is_deleted is True
        assert m.updated_at is not None


class TestAdicionarAnexo:
    def test_anexo_e_adicionado(self):
        m = _manifestacao()
        anexo = Anexo(
            id="a1",
            nome_arquivo="foto.jpg",
            tipo_mime="image/jpeg",
            tamanho_bytes=1024,
            url="https://exemplo/foto.jpg",
        )
        m.adicionar_anexo(anexo)
        assert m.anexos == [anexo]


class TestEnumsDeSuporte:
    def test_canais_falabr(self):
        assert {c.value for c in CanalRecebimento} >= {
            "portal_cidadao",
            "presencial",
            "telefone",
            "email",
            "correios",
            "aplicativo",
            "outro",
        }

    @pytest.mark.parametrize(
        ("nivel", "anos"),
        [
            (NivelSigilo.PUBLICO, 0),
            (NivelSigilo.RESTRITO, 10),
            (NivelSigilo.SIGILOSO, 25),
            (NivelSigilo.ULTRA_SIGILOSO, 50),
        ],
    )
    def test_prazos_de_sigilo_conforme_lai(self, nivel, anos):
        """Lei 12.527/2011 art. 27 — prazos de guarda por nível de sigilo."""
        assert nivel.prazo_maximo_anos == anos
