"""Entidade RegistroAuditoria da trilha de auditoria do domínio Compras.

Baseado em:
  - 017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
    (seção 7 – Categorias de Eventos; seção 26 – Estrutura do Registro;
     seções 30/31/32/33/34 – UTC, correlation_id, identificador de negócio,
     estado anterior/posterior, justificativa)

Requisitos atendidos:
  - identifica origem, usuário, recurso, operação, data/hora e resultado;
  - utiliza UTC como padrão temporal;
  - suporta correlation_id para reconstrução de operações distribuídas;
  - suporta identificador de negócio (businessKey) além do técnico;
  - registra apenas dados de rastreabilidade (LGPD – seção 64).

Imutabilidade (seção 37): a entidade não expõe métodos de alteração —
registros de auditoria são append-only.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from src.shared.compat import UTC


class CategoriaEventoAuditoria(str, Enum):
    """Categorias de eventos (017-Modelo-de-Auditoria, seção 7)."""

    AUTENTICACAO = "AUTENTICACAO"
    AUTORIZACAO = "AUTORIZACAO"
    ACESSO = "ACESSO"
    CRIACAO = "CRIACAO"
    ALTERACAO = "ALTERACAO"
    EXCLUSAO = "EXCLUSAO"
    APROVACAO = "APROVACAO"
    REJEICAO = "REJEICAO"
    CANCELAMENTO = "CANCELAMENTO"
    ASSINATURA = "ASSINATURA"
    PUBLICACAO = "PUBLICACAO"
    EXECUCAO = "EXECUCAO"
    INTEGRACAO = "INTEGRACAO"
    EXPORTACAO = "EXPORTACAO"
    IMPORTACAO = "IMPORTACAO"
    SEGURANCA = "SEGURANCA"
    ADMINISTRACAO = "ADMINISTRACAO"


class ResultadoEventoAuditoria(str, Enum):
    """Resultado da operação auditada."""

    SUCESSO = "SUCESSO"
    ERRO = "ERRO"


class RegistroAuditoria:
    """Registro imutável de um evento de auditoria."""

    ORIGEM_PADRAO = "gestao-compras"

    def __init__(
        self,
        id: UUID | None = None,
        ocorrido_em: datetime | None = None,
        categoria: CategoriaEventoAuditoria = CategoriaEventoAuditoria.ALTERACAO,
        tipo_evento: str = "",
        ator_id: UUID | None = None,
        ator_perfil: str | None = None,
        origem: str = ORIGEM_PADRAO,
        operacao: str = "",
        recurso_tipo: str = "",
        recurso_id: UUID | None = None,
        chave_negocio: str | None = None,
        resultado: ResultadoEventoAuditoria = ResultadoEventoAuditoria.SUCESSO,
        correlation_id: UUID | None = None,
        justificativa: str | None = None,
        detalhes: dict[str, Any] | None = None,
        created_at: datetime | None = None,
    ) -> None:
        self.id: UUID = id or uuid4()
        self.ocorrido_em: datetime = ocorrido_em or datetime.now(UTC)
        self.categoria: CategoriaEventoAuditoria = self._validar_categoria(categoria)
        self.tipo_evento: str = self._validar_texto(tipo_evento, "tipo_evento")
        self.ator_id: UUID | None = ator_id
        self.ator_perfil: str | None = (
            ator_perfil.strip() if ator_perfil else None
        )
        self.origem: str = self._validar_texto(origem, "origem")
        self.operacao: str = self._validar_texto(operacao, "operacao")
        self.recurso_tipo: str = self._validar_texto(recurso_tipo, "recurso_tipo")
        self.recurso_id: UUID | None = recurso_id
        self.chave_negocio: str | None = (
            chave_negocio.strip() if chave_negocio else None
        )
        self.resultado: ResultadoEventoAuditoria = self._validar_resultado(resultado)
        self.correlation_id: UUID | None = correlation_id
        self.justificativa: str | None = (
            justificativa.strip() if justificativa else None
        )
        self.detalhes: dict[str, Any] | None = detalhes
        self.created_at: datetime = created_at or datetime.now(UTC)

    # -- Validações -------------------------------------------------------------

    @staticmethod
    def _validar_categoria(
        categoria: CategoriaEventoAuditoria,
    ) -> CategoriaEventoAuditoria:
        if not isinstance(categoria, CategoriaEventoAuditoria):
            raise ValueError(f"Categoria de evento inválida: {categoria}")
        return categoria

    @staticmethod
    def _validar_resultado(
        resultado: ResultadoEventoAuditoria,
    ) -> ResultadoEventoAuditoria:
        if not isinstance(resultado, ResultadoEventoAuditoria):
            raise ValueError(f"Resultado inválido: {resultado}")
        return resultado

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        valor_normalizado = (valor or "").strip()
        if not valor_normalizado:
            raise ValueError(f"{campo} é obrigatório no registro de auditoria")
        return valor_normalizado


__all__ = [
    "CategoriaEventoAuditoria",
    "ResultadoEventoAuditoria",
    "RegistroAuditoria",
]
