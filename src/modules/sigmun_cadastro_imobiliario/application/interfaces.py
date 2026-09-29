"""Interfaces (ports) dos repositórios e do contrato com o DOM-TEL (DOM-IMO)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from ..domain.entities import (
    AvaliacaoImovel,
    CaracteristicaImovel,
    GeometriaImovel,
    Imovel,
    ProprietarioImovel,
)


class RepositorioImovel(Protocol):
    """Port de persistência das unidades imobiliárias."""

    def save(self, imovel: Imovel) -> Imovel:
        """Persiste um imóvel."""
        ...

    def get_by_id(self, imovel_id: str) -> Imovel | None:
        """Busca imóvel por id."""
        ...

    def get_by_inscricao(self, inscricao: str) -> Imovel | None:
        """Busca imóvel pela inscrição imobiliária (RN-IMO-001)."""
        ...

    def list_by_logradouro(self, logradouro_id: str) -> list[Imovel]:
        """Lista imóveis de um logradouro."""
        ...

    def list_by_bairro(self, bairro_id: str) -> list[Imovel]:
        """Lista imóveis de um bairro."""
        ...

    def list_all(
        self, page: int = 1, page_size: int = 20, situacao: str | None = None
    ) -> list[Imovel]:
        """Lista imóveis paginados, opcionalmente por situação."""
        ...


class RepositorioProprietario(Protocol):
    """Port de persistência dos vínculos de propriedade."""

    def save(self, proprietario: ProprietarioImovel) -> ProprietarioImovel:
        """Persiste um vínculo de propriedade."""
        ...

    def get_by_id(self, vinculo_id: str) -> ProprietarioImovel | None:
        """Busca vínculo por id."""
        ...

    def get_by_imovel_e_cpf(self, imovel_id: str, cpf: str) -> ProprietarioImovel | None:
        """Busca vínculo pelo imóvel e pelo CPF."""
        ...

    def get_principal(self, imovel_id: str) -> ProprietarioImovel | None:
        """Busca o proprietário titular principal do imóvel (RN-IMO-006)."""
        ...

    def list_by_imovel(self, imovel_id: str) -> list[ProprietarioImovel]:
        """Lista vínculos de um imóvel."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[ProprietarioImovel]:
        """Lista vínculos paginados."""
        ...


class RepositorioAvaliacao(Protocol):
    """Port de persistência das avaliações de valor venal."""

    def save(self, avaliacao: AvaliacaoImovel) -> AvaliacaoImovel:
        """Persiste uma avaliação."""
        ...

    def get_by_id(self, avaliacao_id: str) -> AvaliacaoImovel | None:
        """Busca avaliação por id."""
        ...

    def get_by_imovel_e_ano(self, imovel_id: str, ano: int) -> AvaliacaoImovel | None:
        """Busca avaliação do imóvel para o exercício."""
        ...

    def list_by_imovel(self, imovel_id: str) -> list[AvaliacaoImovel]:
        """Lista avaliações de um imóvel."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[AvaliacaoImovel]:
        """Lista avaliações paginadas."""
        ...


class RepositorioCaracteristica(Protocol):
    """Port de persistência das características construtivas."""

    def save(self, caracteristica: CaracteristicaImovel) -> CaracteristicaImovel:
        """Persiste uma característica construtiva."""
        ...

    def get_by_id(self, caracteristica_id: str) -> CaracteristicaImovel | None:
        """Busca característica por id."""
        ...

    def get_by_imovel(self, imovel_id: str) -> CaracteristicaImovel | None:
        """Busca a característica construtiva vigente do imóvel."""
        ...

    def list_by_imovel(self, imovel_id: str) -> list[CaracteristicaImovel]:
        """Lista características de um imóvel."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[CaracteristicaImovel]:
        """Lista características paginadas."""
        ...


class RepositorioGeometria(Protocol):
    """Port de persistência das geometrias georreferenciadas dos lotes."""

    def save(self, geometria: GeometriaImovel) -> GeometriaImovel:
        """Persiste uma geometria de lote."""
        ...

    def get_by_id(self, geometria_id: str) -> GeometriaImovel | None:
        """Busca geometria por id."""
        ...

    def get_by_imovel(self, imovel_id: str) -> GeometriaImovel | None:
        """Busca a geometria vigente do lote (RN-IMO-007)."""
        ...

    def list_all(self, page: int = 1, page_size: int = 20) -> list[GeometriaImovel]:
        """Lista geometrias paginadas."""
        ...


@dataclass(frozen=True)
class ValoresPlanta:
    """Valores unitários vigentes da planta genérica de valores.

    Contrato de integração com o DOM-TEL (ROADMAP §2.8): o DOM-IMO não acessa
    o schema `tel`; recebe os valores já resolvidos pelo consumidor da API
    `GET /api/v1/tel/plantas-valores/vigente`.
    """

    ano: int
    bairro_id: str
    ocupacao: str
    valor_terreno_m2: float
    valor_construcao_m2: float
    aliquota_percent: float
    planta_id: str = ""


class ConsultaPlantaValores(Protocol):
    """Port de consulta dos valores unitários vigentes (contrato com o DOM-TEL)."""

    def valores_vigentes(self, ano: int, bairro_id: str, ocupacao: str) -> ValoresPlanta | None:
        """Retorna a planta genérica de valores vigente, ou None."""
        ...


__all__ = [
    "RepositorioImovel",
    "RepositorioProprietario",
    "RepositorioAvaliacao",
    "RepositorioCaracteristica",
    "RepositorioGeometria",
    "ValoresPlanta",
    "ConsultaPlantaValores",
]
