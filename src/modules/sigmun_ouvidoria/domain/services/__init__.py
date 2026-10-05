"""Serviços de domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal).

Regras de negócio transversais e coordenação entre entidades.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..entities import Denuncia, Manifestacao
from ..exceptions import ProtocoloJaExistenteError, RegraNegocioError
from ..value_objects import (
    DadosCidadao,
    PrazoResposta,
    Protocolo,
    StatusManifestacao,
    TipoManifestacao,
)


@dataclass
class GeradorProtocolo:
    """Serviço de geração de protocolo único (RN-OUV-001).

    Formato: AAAA-NNNNNN (ano + sequencial de 6 dígitos).
    """

    def __init__(self, repositorio_protocolos) -> None:
        self._repo = repositorio_protocolos

    def gerar(self, ano: int) -> Protocolo:
        """Gera próximo protocolo do ano."""
        sequencial = self._repo.obter_proximo_sequencial(ano)
        return Protocolo.gerar(ano, sequencial)

    def validar_unicidade(self, protocolo: Protocolo) -> bool:
        """Verifica se protocolo já existe."""
        return not self._repo.existe_protocolo(protocolo.codigo)

    def registrar(self, protocolo: Protocolo) -> None:
        """Registra protocolo como utilizado."""
        if not self.validar_unicidade(protocolo):
            raise ProtocoloJaExistenteError(f"Protocolo {protocolo.codigo} já existe")
        self._repo.registrar_protocolo(protocolo)


class CalculadoraPrazo:
    """Serviço de cálculo de prazos conforme legislação (RN-OUV-020)."""

    PRAZOS_BASE = {
        TipoManifestacao.SUGESTAO: 20,
        TipoManifestacao.ELOGIO: 20,
        TipoManifestacao.RECLAMACAO: 30,
        TipoManifestacao.SOLICITACAO: 30,
        TipoManifestacao.DENUNCIA: 30,
        TipoManifestacao.PEDIDO_ACESSO_INFORMACAO: 20,  # LAI Art. 11
    }

    @classmethod
    def calcular(
        cls, tipo: TipoManifestacao, data_registro: date, prorrogacao: bool = False
    ) -> PrazoResposta:
        """Calcula prazo de resposta."""
        base = cls.PRAZOS_BASE.get(tipo, 20)
        if prorrogacao:
            base += 10  # LAI Art. 11 §1º
        from datetime import timedelta

        data_limite = data_registro + timedelta(days=base)
        return PrazoResposta(
            data_limite=data_limite,
            dias_uteis=base,
            prorrogado=prorrogacao,
        )

    @classmethod
    def calcular_prorrogacao(cls, prazo_atual: PrazoResposta, justificativa: str) -> PrazoResposta:
        """Calcula nova data com prorrogação de 10 dias."""
        if prazo_atual.prorrogado:
            raise RegraNegocioError("Prazo já foi prorrogado")
        from datetime import timedelta

        nova_data = prazo_atual.data_limite + timedelta(days=10)
        return PrazoResposta(
            data_limite=nova_data,
            dias_uteis=prazo_atual.dias_uteis + 10,
            prorrogado=True,
            data_prorrogacao=date.today(),
            justificativa_prorrogacao=justificativa,
        )


class ValidadorManifestacao:
    """Validador de regras de negócio transversais."""

    def __init__(self, repo_cidadao=None) -> None:
        self._repo_cidadao = repo_cidadao

    def validar_criacao(self, manifestacao: Manifestacao) -> list[str]:
        """Valida regras para criação.
        Retorna lista de avisos (não bloqueantes).
        """
        avisos = []
        if (
            manifestacao.tipo == TipoManifestacao.DENUNCIA
            and manifestacao.cidadao
            and not manifestacao.cidadao.anonimo
        ):
            avisos.append("Denúncia identificada - dados do denunciante serão protegidos (sigilo)")
        if not manifestacao.prazo:
            avisos.append("Prazo de resposta não definido - será calculado automaticamente")
        return avisos

    def validar_resposta(self, manifestacao: Manifestacao) -> None:
        """Valida se pode responder."""
        if manifestacao.status not in (
            StatusManifestacao.EM_TRATAMENTO,
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
        ):
            raise RegraNegocioError(
                f"Não é possível responder manifestação com status {manifestacao.status.rotulo}"
            )
        if manifestacao.verificar_prazo():
            # Alerta mas não bloqueia
            pass

    def validar_transicao_status(self, atual: StatusManifestacao, novo: StatusManifestacao) -> None:
        """Valida transição de status."""
        if not atual.pode_transicionar_para(novo):
            raise RegraNegocioError(f"Transição inválida: {atual.rotulo} -> {novo.rotulo}")


class ServicoEncaminhamento:
    """Serviço de encaminhamento de manifestações/denúncias."""

    ORGAOS_EXTERNOS = {
        "MP": "Ministério Público",
        "PF": "Polícia Federal",
        "TCE": "Tribunal de Contas do Estado",
        "TCU": "Tribunal de Contas da União",
        "CGU": "Controladoria-Geral da União",
    }

    @classmethod
    def encaminhar_denuncia(
        cls, denuncia: Denuncia, orgao: str, numero_processo: str, usuario: str
    ) -> None:
        """Encaminha denúncia a órgão externo."""
        if orgao.upper() not in cls.ORGAOS_EXTERNOS:
            raise RegraNegocioError(f"Órgão {orgao} não reconhecido")
        denuncia.encaminhar_orgao_externo(orgao, numero_processo, usuario)
        # Disparar evento de integração

    @classmethod
    def encaminhar_manifestacao(
        cls, manifestacao: Manifestacao, setor_destino: str, usuario: str
    ) -> None:
        """Encaminha manifestação para setor interno."""
        manifestacao.setor_responsavel = setor_destino
        manifestacao.alterar_status(StatusManifestacao.ENCAMINHADA, usuario)


class ServicoEstatisticas:
    """Serviço de estatísticas e indicadores da ouvidoria."""

    def __init__(self, repo_manifestacao, repo_denuncia, repo_pedido_lai) -> None:
        self._repo_m = repo_manifestacao
        self._repo_d = repo_denuncia
        self._repo_l = repo_pedido_lai

    def indicadores_gerais(self, ano: int) -> dict:
        """Retorna indicadores gerais do ano."""
        total = (
            self._repo_m.contar_por_ano(ano)
            + self._repo_d.contar_por_ano(ano)
            + self._repo_l.contar_por_ano(ano)
        )
        respondidas = (
            self._repo_m.contar_por_status_ano(StatusManifestacao.RESPONDIDA, ano)
            + self._repo_d.contar_por_status_ano(StatusManifestacao.RESPONDIDA, ano)
            + self._repo_l.contar_por_status_ano(StatusManifestacao.RESPONDIDA, ano)
        )
        concluidas = (
            self._repo_m.contar_por_status_ano(StatusManifestacao.CONCLUIDA, ano)
            + self._repo_d.contar_por_status_ano(StatusManifestacao.CONCLUIDA, ano)
            + self._repo_l.contar_por_status_ano(StatusManifestacao.CONCLUIDA, ano)
        )
        vencidas = (
            self._repo_m.contar_prazo_vencido_ano(ano)
            + self._repo_d.contar_prazo_vencido_ano(ano)
            + self._repo_l.contar_prazo_vencido_ano(ano)
        )
        return {
            "total": total,
            "respondidas": respondidas,
            "concluidas": concluidas,
            "vencidas": vencidas,
            "taxa_resposta": round((respondidas / total * 100) if total > 0 else 0, 2),
            "taxa_conclusao": round((concluidas / total * 100) if total > 0 else 0, 2),
        }

    def indicadores_por_tipo(self, ano: int) -> dict:
        """Retorna indicadores por tipo de manifestação."""
        return {
            "manifestacoes": self._repo_m.estatisticas_por_tipo(ano),
            "denuncias": self._repo_d.estatisticas_por_tipo(ano),
            "pedidos_lai": self._repo_l.estatisticas_por_tipo(ano),
        }

    def manifestacoes_vencendo_prazo(self, dias: int = 5) -> list[Manifestacao]:
        """Lista manifestações com prazo vencendo em X dias."""
        return (
            self._repo_m.buscar_vencendo_prazo(dias)
            + self._repo_d.buscar_vencendo_prazo(dias)
            + self._repo_l.buscar_vencendo_prazo(dias)
        )


class ServicoLGPD:
    """Serviço de conformidade LGPD para dados do cidadão."""

    @staticmethod
    def anonimizar_dados_cidadao(cidadao: DadosCidadao) -> DadosCidadao:
        """Retorna versão anonimizada dos dados."""
        return DadosCidadao(
            nome="*** ANÔNIMO ***",
            cpf=None,
            email=None,
            telefone=None,
            endereco=None,
            anonimo=True,
        )

    @staticmethod
    def mascarar_para_exibicao(cidadao: DadosCidadao) -> dict:
        """Mascara dados para exibição em telas/relatórios."""
        return cidadao.para_exibicao()

    @staticmethod
    def pode_acessar_dados_sensiveis(usuario_perfil: str, eh_ouvidor: bool = False) -> bool:
        """Verifica se usuário pode acessar dados sensíveis (denunciante).

        ADR-0008 §2.3: apenas papéis **funcionais** de proteção ao cidadão
        acessam a identificação do denunciante — `ouvidor`, `corregedor` e
        `auditor`.

        `admin` (administração técnica do sistema) **não** é autoridade
        funcional sobre a identidade de um denunciante, e por isso está
        deliberadamente ausente da lista. A separação entre função técnica e
        funcional é o requisito do ADR.
        """
        perfis_autorizados = ["ouvidor", "corregedor", "auditor"]
        return usuario_perfil.lower() in perfis_autorizados or eh_ouvidor


__all__ = [
    "GeradorProtocolo",
    "CalculadoraPrazo",
    "ValidadorManifestacao",
    "ServicoEncaminhamento",
    "ServicoEstatisticas",
    "ServicoLGPD",
]
