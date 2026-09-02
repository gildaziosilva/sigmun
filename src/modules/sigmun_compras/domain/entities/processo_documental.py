"""Entidade ProcessoDocumental do domínio Gestão de Compras.

Baseado em:
  - Modelo Físico / migration 20260820_01 (Tabela: core.processos_documentais)
  - UC-COMPRAS-013 – Abrir Processo de Contratação
  - RN-COMPRAS-025 – Processo Único
  - RN-COMPRAS-004 – Integridade do Histórico

Regras de negócio implementadas:
  - Unicidade cadastral: par (numero, ano) é único (constraint
    ``uq_processos_documentais_numero_ano``)
  - Identificação completa: numero, ano e assunto obrigatórios;
    vínculo à unidade administrativa responsável (RN-COMPRAS-028)
  - Soft-delete preserva histórico (RN-COMPRAS-004)
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from src.shared.compat import UTC

_ANO_MINIMO = 1900
_ANO_MAXIMO = 2100


class ProcessoDocumental:
    """Entidade ProcessoDocumental — processo administrativo documentado."""

    def __init__(
        self,
        id: UUID | None = None,
        unidade_id: UUID | None = None,
        numero: str = "",
        ano: int = 0,
        assunto: str = "",
        descricao: str | None = None,
        created_at: datetime | None = None,
        created_by: UUID | None = None,
        updated_at: datetime | None = None,
        updated_by: UUID | None = None,
        deleted_at: datetime | None = None,
        deleted_by: UUID | None = None,
    ) -> None:
        if unidade_id is None:
            raise ValueError("unidade_id é obrigatório (RN-COMPRAS-028)")
        self.id: UUID = id or uuid4()
        self.unidade_id: UUID = unidade_id
        self.numero: str = self._validar_numero(numero)
        self.ano: int = self._validar_ano(ano)
        self.assunto: str = self._validar_assunto(assunto)
        self.descricao: str | None = descricao.strip() if descricao else None
        self.created_at: datetime = created_at or datetime.now(UTC)
        self.created_by: UUID | None = created_by
        self.updated_at: datetime = updated_at or datetime.now(UTC)
        self.updated_by: UUID | None = updated_by
        self.deleted_at: datetime | None = deleted_at
        self.deleted_by: UUID | None = deleted_by

    # -- Validações -----------------------------------------------------------

    @staticmethod
    def _validar_numero(numero: str) -> str:
        if numero is None or not numero.strip():
            raise ValueError("numero do processo é obrigatório")
        return numero.strip()

    @staticmethod
    def _validar_ano(ano: int) -> int:
        ano = int(ano)
        if not _ANO_MINIMO <= ano <= _ANO_MAXIMO:
            raise ValueError(
                f"ano deve estar entre {_ANO_MINIMO} e {_ANO_MAXIMO}: {ano}"
            )
        return ano

    @staticmethod
    def _validar_assunto(assunto: str) -> str:
        if assunto is None or not assunto.strip():
            raise ValueError("assunto do processo é obrigatório")
        return assunto.strip()

    # -- Comportamentos de domínio -------------------------------------------

    def atualizar_dados(
        self,
        numero: str | None = None,
        ano: int | None = None,
        assunto: str | None = None,
        descricao: str | None = None,
        usuario_id: UUID | None = None,
    ) -> None:
        """Atualiza campos informados (RN-COMPRAS-028/029)."""
        # RN-COMPRAS-004: não operar sobre processos excluídos.
        if self.foi_excluido():
            raise ValueError(
                "Processo excluído não pode ser atualizado (RN-COMPRAS-004)"
            )
        if numero is not None:
            self.numero = self._validar_numero(numero)
        if ano is not None:
            self.ano = self._validar_ano(ano)
        if assunto is not None:
            self.assunto = self._validar_assunto(assunto)
        if descricao is not None:
            self.descricao = descricao.strip() or None
        self.updated_at = datetime.now(UTC)
        if usuario_id:
            self.updated_by = usuario_id

    def excluir(self, usuario_id: UUID) -> None:
        """Marca o processo como excluído (soft-delete, RN-COMPRAS-004)."""
        self.deleted_at = datetime.now(UTC)
        self.deleted_by = usuario_id

    def foi_excluido(self) -> bool:
        """Retorna True se o processo foi logicamente excluído."""
        return self.deleted_at is not None


__all__ = ["ProcessoDocumental"]
