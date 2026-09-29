"""Interfaces (ports) dos repositórios do DOM-OBR — Obras e Infraestrutura."""

from __future__ import annotations

from typing import Protocol

from ..domain.entities import DespesaObra, EtapaObra, MedicaoObra, Obra, VistoriaObra


class RepositorioObra(Protocol):
    """Port de persistência de obras públicas."""

    def save(self, obra: Obra) -> Obra:
        """Persiste uma obra."""
        ...

    def get_by_id(self, obra_id: str) -> Obra | None:
        """Busca obra por id."""
        ...

    def get_by_numero(self, numero: str) -> Obra | None:
        """Busca obra pelo número cadastral."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[Obra]:
        """Lista obras paginadas, opcionalmente por situação."""
        ...


class RepositorioEtapa(Protocol):
    """Port de persistência de etapas de obra."""

    def save(self, etapa: EtapaObra) -> EtapaObra:
        """Persiste uma etapa."""
        ...

    def get_by_id(self, etapa_id: str) -> EtapaObra | None:
        """Busca etapa por id."""
        ...

    def list_by_obra(self, obra_id: str) -> list[EtapaObra]:
        """Lista as etapas de uma obra."""
        ...


class RepositorioMedicao(Protocol):
    """Port de persistência de medições físico-financeiras."""

    def save(self, medicao: MedicaoObra) -> MedicaoObra:
        """Persiste uma medição."""
        ...

    def get_by_id(self, medicao_id: str) -> MedicaoObra | None:
        """Busca medição por id."""
        ...

    def get_by_numero_obra(self, numero: str, obra_id: str) -> MedicaoObra | None:
        """Busca medição pelo número dentro da obra."""
        ...

    def list_by_obra(self, obra_id: str) -> list[MedicaoObra]:
        """Lista as medições de uma obra."""
        ...


class RepositorioDespesa(Protocol):
    """Port de persistência de despesas financeiras de obra."""

    def save(self, despesa: DespesaObra) -> DespesaObra:
        """Persiste uma despesa."""
        ...

    def get_by_id(self, despesa_id: str) -> DespesaObra | None:
        """Busca despesa por id."""
        ...

    def list_by_obra(self, obra_id: str) -> list[DespesaObra]:
        """Lista as despesas de uma obra."""
        ...


class RepositorioVistoria(Protocol):
    """Port de persistência de vistorias de obra."""

    def save(self, vistoria: VistoriaObra) -> VistoriaObra:
        """Persiste uma vistoria."""
        ...

    def get_by_id(self, vistoria_id: str) -> VistoriaObra | None:
        """Busca vistoria por id."""
        ...

    def list_by_obra(self, obra_id: str) -> list[VistoriaObra]:
        """Lista as vistorias de uma obra."""
        ...


__all__ = [
    "RepositorioObra",
    "RepositorioEtapa",
    "RepositorioMedicao",
    "RepositorioDespesa",
    "RepositorioVistoria",
]
