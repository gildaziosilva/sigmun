"""Value Objects do domínio DOM-OUV (Ouvidoria FalaBR / e-OUV municipal)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum


class TipoManifestacao(Enum):
    """Tipos de manifestação conforme FalaBR / e-OUV."""

    SUGESTAO = "sugestao"
    ELOGIO = "elogio"
    RECLAMACAO = "reclamacao"
    SOLICITACAO = "solicitacao"
    DENUNCIA = "denuncia"
    PEDIDO_ACESSO_INFORMACAO = "pedido_acesso_informacao"

    @property
    def rotulo(self) -> str:
        return {
            TipoManifestacao.SUGESTAO: "Sugestão",
            TipoManifestacao.ELOGIO: "Elogio",
            TipoManifestacao.RECLAMACAO: "Reclamação",
            TipoManifestacao.SOLICITACAO: "Solicitação",
            TipoManifestacao.DENUNCIA: "Denúncia",
            TipoManifestacao.PEDIDO_ACESSO_INFORMACAO: "Pedido de Acesso à Informação (LAI)",
        }[self]


class StatusManifestacao(Enum):
    """Status da manifestação (fluxo FalaBR)."""

    REGISTRADA = "registrada"
    EM_ANALISE = "em_analise"
    ENCAMINHADA = "encaminhada"
    EM_TRATAMENTO = "em_tratamento"
    AGUARDANDO_COMPLEMENTACAO = "aguardando_complementacao"
    RESPONDIDA = "respondida"
    CONCLUIDA = "concluida"
    ARQUIVADA = "arquivada"
    CANCELADA = "cancelada"

    @property
    def rotulo(self) -> str:
        return {
            StatusManifestacao.REGISTRADA: "Registrada",
            StatusManifestacao.EM_ANALISE: "Em Análise",
            StatusManifestacao.ENCAMINHADA: "Encaminhada",
            StatusManifestacao.EM_TRATAMENTO: "Em Tratamento",
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO: "Aguardando Complementação",
            StatusManifestacao.RESPONDIDA: "Respondida",
            StatusManifestacao.CONCLUIDA: "Concluída",
            StatusManifestacao.ARQUIVADA: "Arquivada",
            StatusManifestacao.CANCELADA: "Cancelada",
        }[self]

    def pode_transicionar_para(self, novo: StatusManifestacao) -> bool:
        """Valida transições permitidas (RN-OUV-010)."""
        transicoes = {
            StatusManifestacao.REGISTRADA: {
                StatusManifestacao.EM_ANALISE,
                StatusManifestacao.ENCAMINHADA,
                StatusManifestacao.CANCELADA,
            },
            StatusManifestacao.EM_ANALISE: {
                StatusManifestacao.ENCAMINHADA,
                StatusManifestacao.EM_TRATAMENTO,
                StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
                StatusManifestacao.CANCELADA,
            },
            StatusManifestacao.ENCAMINHADA: {
                StatusManifestacao.EM_TRATAMENTO,
                StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
                StatusManifestacao.CANCELADA,
            },
            StatusManifestacao.EM_TRATAMENTO: {
                StatusManifestacao.RESPONDIDA,
                StatusManifestacao.AGUARDANDO_COMPLEMENTACAO,
                StatusManifestacao.CANCELADA,
            },
            StatusManifestacao.AGUARDANDO_COMPLEMENTACAO: {
                StatusManifestacao.EM_TRATAMENTO,
                StatusManifestacao.RESPONDIDA,
                StatusManifestacao.CANCELADA,
            },
            StatusManifestacao.RESPONDIDA: {
                StatusManifestacao.CONCLUIDA,
                StatusManifestacao.ARQUIVADA,
            },
            StatusManifestacao.CONCLUIDA: {
                StatusManifestacao.ARQUIVADA,
            },
            StatusManifestacao.ARQUIVADA: set(),
            StatusManifestacao.CANCELADA: set(),
        }
        return novo in transicoes.get(self, set())


class NivelSigilo(Enum):
    """Níveis de sigilo conforme LAI (Lei 12.527/2011)."""

    PUBLICO = "publico"
    RESTRITO = "restrito"
    SIGILOSO = "sigiloso"
    ULTRA_SIGILOSO = "ultra_sigiloso"

    @property
    def prazo_maximo_anos(self) -> int:
        return {
            NivelSigilo.PUBLICO: 0,
            NivelSigilo.RESTRITO: 10,
            NivelSigilo.SIGILOSO: 25,
            NivelSigilo.ULTRA_SIGILOSO: 50,
        }[self]

    @property
    def rotulo(self) -> str:
        return {
            NivelSigilo.PUBLICO: "Público",
            NivelSigilo.RESTRITO: "Restrito",
            NivelSigilo.SIGILOSO: "Sigiloso",
            NivelSigilo.ULTRA_SIGILOSO: "Ultra-sigiloso",
        }[self]


class CanalRecebimento(Enum):
    """Canais de recebimento da manifestação."""

    PORTAL_CIDADAO = "portal_cidadao"
    PRESENCIAL = "presencial"
    TELEFONE = "telefone"
    EMAIL = "email"
    CORREIOS = "correios"
    APLICATIVO = "aplicativo"
    OUTRO = "outro"


class TipoDenuncia(Enum):
    """Classificação da denúncia."""

    CORRUPAO = "corrupcao"
    IMPROBIDADE = "improbidade"
    ASSEDIO = "assedio"
    DESVIO_VERBA = "desvio_verba"
    NEPOTISMO = "nepotismo"
    FRAUDE_LICITACAO = "fraude_licitacao"
    OUTRO = "outro"


class FormaResposta(Enum):
    """Forma de resposta ao cidadão."""

    PORTAL = "portal"
    EMAIL = "email"
    CORREIOS = "correios"
    PRESENCIAL = "presencial"
    TELEFONE = "telefone"


@dataclass(frozen=True)
class Protocolo:
    """Protocolo único da manifestação (AAAA-NNNNNN)."""

    numero: str
    ano: int

    def __post_init__(self) -> None:
        if not self.numero or not self.ano:
            raise ValueError("Protocolo deve ter número e ano")
        if not re.match(r"^\d{6}$", self.numero):
            raise ValueError("Número do protocolo deve ter 6 dígitos")

    @property
    def codigo(self) -> str:
        return f"{self.ano}-{self.numero}"

    @classmethod
    def gerar(cls, ano: int, sequencial: int) -> Protocolo:
        return cls(numero=f"{sequencial:06d}", ano=ano)

    def __str__(self) -> str:
        return self.codigo


@dataclass(frozen=True)
class DadosCidadao:
    """Dados do cidadão manifestante (LGPD - minimização)."""

    nome: str
    cpf: str | None = None
    email: str | None = None
    telefone: str | None = None
    endereco: str | None = None
    anonimo: bool = False

    def __post_init__(self) -> None:
        if not self.anonimo and not self.nome:
            raise ValueError("Nome é obrigatório para manifestação não anônima")
        if self.cpf and not self._validar_cpf(self.cpf):
            raise ValueError("CPF inválido")
        if self.email and not self._validar_email(self.email):
            raise ValueError("E-mail inválido")

    @staticmethod
    def _validar_cpf(cpf: str) -> bool:
        cpf = re.sub(r"\D", "", cpf)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            if digito != int(cpf[i]):
                return False
        return True

    @staticmethod
    def _validar_email(email: str) -> bool:
        return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))

    def para_exibicao(self) -> dict:
        """Retorna dados seguros para exibição (LGPD)."""
        if self.anonimo:
            return {"anonimo": True}
        return {
            "nome": self.nome,
            "cpf": self._mascarar_cpf(self.cpf) if self.cpf else None,
            "email": self._mascarar_email(self.email) if self.email else None,
            "telefone": self.telefone,
            "endereco": self.endereco,
        }

    @staticmethod
    def _mascarar_cpf(cpf: str) -> str:
        cpf = re.sub(r"\D", "", cpf)
        return f"***.{cpf[3:6]}.***-{cpf[9:]}" if len(cpf) == 11 else "***"

    @staticmethod
    def _mascarar_email(email: str) -> str:
        if "@" not in email:
            return "***"
        local, dominio = email.split("@", 1)
        return f"{local[0]}***@{dominio}"


@dataclass(frozen=True)
class PrazoResposta:
    """Prazo de resposta conforme tipo e legislação."""

    data_limite: date
    dias_uteis: int
    prorrogado: bool = False
    data_prorrogacao: date | None = None
    justificativa_prorrogacao: str = ""

    @property
    def vencido(self) -> bool:
        return date.today() > self.data_limite

    @property
    def dias_restantes(self) -> int:
        delta = self.data_limite - date.today()
        return max(0, delta.days)

    @classmethod
    def calcular(
        cls, tipo: TipoManifestacao, data_registro: date, prorrogacao: bool = False
    ) -> PrazoResposta:
        """Calcula prazo conforme legislação (RN-OUV-020)."""
        prazos_base = {
            TipoManifestacao.SUGESTAO: 20,
            TipoManifestacao.ELOGIO: 20,
            TipoManifestacao.RECLAMACAO: 30,
            TipoManifestacao.SOLICITACAO: 30,
            TipoManifestacao.DENUNCIA: 30,
            TipoManifestacao.PEDIDO_ACESSO_INFORMACAO: 20,
        }
        base = prazos_base.get(tipo, 20)
        if prorrogacao:
            base += 10
        from datetime import timedelta

        data_limite = data_registro + timedelta(days=base)
        return cls(data_limite=data_limite, dias_uteis=base, prorrogado=prorrogacao)


@dataclass(frozen=True)
class Anexo:
    """Anexo da manifestação."""

    id: str
    nome_arquivo: str
    tipo_mime: str
    tamanho_bytes: int
    url: str
    descricao: str = ""
    criado_em: datetime = None  # type: ignore

    def __post_init__(self) -> None:
        if self.criado_em is None:
            object.__setattr__(self, "criado_em", datetime.utcnow())


__all__ = [
    "TipoManifestacao",
    "StatusManifestacao",
    "NivelSigilo",
    "CanalRecebimento",
    "TipoDenuncia",
    "FormaResposta",
    "Protocolo",
    "DadosCidadao",
    "PrazoResposta",
    "Anexo",
]
