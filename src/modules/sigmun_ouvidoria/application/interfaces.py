"""Interfaces (ports) dos repositórios do DOM-OUV."""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from ..domain.entities import Denuncia, Manifestacao, PedidoLai
from ..domain.value_objects import (
    Anexo,
    Protocolo,
    StatusManifestacao,
)


class RepositorioProtocolo(Protocol):
    """Port de controle de protocolos."""

    def obter_proximo_sequencial(self, ano: int) -> int:
        """Retorna próximo número sequencial do ano."""
        ...

    def existe_protocolo(self, codigo: str) -> bool:
        """Verifica se protocolo já existe."""
        ...

    def registrar_protocolo(self, protocolo: Protocolo) -> None:
        """Registra protocolo como utilizado."""
        ...


class RepositorioAnexo(Protocol):
    """Port de persistência de anexos."""

    def save(self, anexo: Anexo, manifestacao_id: UUID) -> Anexo:
        """Persiste um anexo."""
        ...

    def get_by_id(self, anexo_id: UUID) -> Anexo | None:
        """Busca anexo por id."""
        ...

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list[Anexo]:
        """Lista anexos da manifestação."""
        ...


class RepositorioTramitacao(Protocol):
    """Port de persistência de tramitações."""

    def save(
        self,
        manifestacao_id: UUID,
        status_anterior: StatusManifestacao | None,
        status_novo: StatusManifestacao,
        observacao: str,
        usuario_id: str,
    ) -> None:
        """Registra tramitação."""
        ...

    def list_by_manifestacao(self, manifestacao_id: UUID) -> list[dict]:
        """Lista tramitações da manifestação."""
        ...


class RepositorioManifestacao(Protocol):
    """Port de persistência de manifestações genéricas."""

    def save(self, manifestacao: Manifestacao) -> Manifestacao:
        """Persiste uma manifestação."""
        ...

    def get_by_id(self, manifestacao_id: str) -> Manifestacao | None:
        """Busca manifestação por id."""
        ...

    def get_by_protocolo(self, protocolo: str) -> Manifestacao | None:
        """Busca manifestação por protocolo."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[Manifestacao]:
        """Lista manifestações paginadas com filtros."""
        ...

    def count_all(self, filtros: dict | None = None) -> int:
        """Conta total de manifestações com filtros."""
        ...

    def contar_por_ano(self, ano: int) -> int:
        """Conta manifestações do ano."""
        ...

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        """Conta manifestações por status no ano."""
        ...

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        """Conta manifestações com prazo vencido no ano."""
        ...

    def estatisticas_por_tipo(self, ano: int) -> dict:
        """Estatísticas por tipo no ano."""
        ...

    def buscar_vencendo_prazo(self, dias: int) -> list[Manifestacao]:
        """Busca manifestações com prazo vencendo em X dias."""
        ...


class RepositorioDenuncia(Protocol):
    """Port de persistência de denúncias."""

    def save(self, denuncia: Denuncia) -> Denuncia:
        """Persiste uma denúncia."""
        ...

    def get_by_id(self, denuncia_id: str) -> Denuncia | None:
        """Busca denúncia por id."""
        ...

    def get_by_protocolo(self, protocolo: str) -> Denuncia | None:
        """Busca denúncia por protocolo."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[Denuncia]:
        """Lista denúncias paginadas com filtros."""
        ...

    def count_all(self, filtros: dict | None = None) -> int:
        """Conta total de denúncias com filtros."""
        ...

    def contar_por_ano(self, ano: int) -> int:
        """Conta denúncias do ano."""
        ...

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        """Conta denúncias por status no ano."""
        ...

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        """Conta denúncias com prazo vencido no ano."""
        ...

    def estatisticas_por_tipo(self, ano: int) -> dict:
        """Estatísticas por tipo de denúncia no ano."""
        ...

    def buscar_vencendo_prazo(self, dias: int) -> list[Denuncia]:
        """Busca denúncias com prazo vencendo em X dias."""
        ...


class RepositorioPedidoLai(Protocol):
    """Port de persistência de pedidos LAI."""

    def save(self, pedido: PedidoLai) -> PedidoLai:
        """Persiste um pedido LAI."""
        ...

    def get_by_id(self, pedido_id: str) -> PedidoLai | None:
        """Busca pedido LAI por id."""
        ...

    def get_by_protocolo(self, protocolo: str) -> PedidoLai | None:
        """Busca pedido LAI por protocolo."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, filtros: dict | None = None
    ) -> list[PedidoLai]:
        """Lista pedidos LAI paginados com filtros."""
        ...

    def count_all(self, filtros: dict | None = None) -> int:
        """Conta total de pedidos LAI com filtros."""
        ...

    def contar_por_ano(self, ano: int) -> int:
        """Conta pedidos LAI do ano."""
        ...

    def contar_por_status_ano(self, status: StatusManifestacao, ano: int) -> int:
        """Conta pedidos LAI por status no ano."""
        ...

    def contar_prazo_vencido_ano(self, ano: int) -> int:
        """Conta pedidos LAI com prazo vencido no ano."""
        ...

    def estatisticas_por_tipo(self, ano: int) -> dict:
        """Estatísticas por nível de sigilo no ano."""
        ...

    def buscar_vencendo_prazo(self, dias: int) -> list[PedidoLai]:
        """Busca pedidos LAI com prazo vencendo em X dias."""
        ...


__all__ = [
    "RepositorioProtocolo",
    "RepositorioAnexo",
    "RepositorioTramitacao",
    "RepositorioManifestacao",
    "RepositorioDenuncia",
    "RepositorioPedidoLai",
]
