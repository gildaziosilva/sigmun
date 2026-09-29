"""Dados demonstrativos (DEMO) do DOM-TEL — Gestão Territorial.

Os registros aqui definidos são FICTÍCIOS, criados apenas para demonstrar as
telas administrativas. Não representam cadastro real de bairros, logradouros
ou valores do Município de Camacan-BA.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

AUTOR_SEED = "seed-tel"
ANO_PGV = date.today().year


@dataclass(frozen=True)
class BairroSeed:
    """Divisão territorial a ser criada."""

    codigo: str
    nome: str
    tipo: str
    populacao_estimada: int
    area_km2: float
    latitude: float
    longitude: float


BAIRROS_DEMO: tuple[BairroSeed, ...] = (
    BairroSeed("BR-CENTRO", "Centro", "bairro", 12500, 4.2, -13.1289, -39.4906),
    BairroSeed("BR-NOVA-ESPERANCA", "Nova Esperanca", "bairro", 8400, 6.8, -13.1420, -39.4750),
    BairroSeed("BR-COMERCIO", "Comercio", "setor", 3100, 2.1, -13.1330, -39.5010),
    BairroSeed("BR-ZONA-RURAL", "Zona Rural", "zona_rural", 5600, 210.5, -13.2100, -39.4200),
)


@dataclass(frozen=True)
class LogradouroSeed:
    """Logradouro público a ser criado."""

    codigo: str
    nome: str
    tipo: str
    bairro_codigo: str
    cep: str
    numero_inicial: int
    numero_final: int


LOGRADOUROS_DEMO: tuple[LogradouroSeed, ...] = (
    LogradouroSeed("LG-001", "Rua da Matriz", "rua", "BR-CENTRO", "45880-000", 1, 250),
    LogradouroSeed("LG-002", "Avenida Principal", "avenida", "BR-CENTRO", "45880-000", 1, 900),
    LogradouroSeed("LG-003", "Praca da Prefeitura", "praca", "BR-CENTRO", "45880-000", 0, 0),
    LogradouroSeed("LG-004", "Rua das Flores", "rua", "BR-NOVA-ESPERANCA", "45880-010", 1, 320),
    LogradouroSeed("LG-005", "Rua do Comercio", "rua", "BR-COMERCIO", "45880-020", 1, 180),
    LogradouroSeed("LG-006", "Estrada do Abrigo", "estrada", "BR-ZONA-RURAL", "45880-900", 0, 0),
)


@dataclass(frozen=True)
class PlantaValoresSeed:
    """Planta genérica de valores a ser criada."""

    ano: int
    bairro_codigo: str
    ocupacao: str
    valor_terreno_m2: float
    valor_construcao_m2: float
    aliquota_percent: float
    legislacao: str
    ativar: bool


PLANTAS_DEMO: tuple[PlantaValoresSeed, ...] = (
    PlantaValoresSeed(
        ANO_PGV,
        "BR-CENTRO",
        "residencial",
        180.00,
        950.00,
        2.50,
        "Lei Municipal 1.234/2026",
        True,
    ),
    PlantaValoresSeed(
        ANO_PGV,
        "BR-CENTRO",
        "comercial",
        320.00,
        1450.00,
        2.50,
        "Lei Municipal 1.234/2026",
        True,
    ),
    PlantaValoresSeed(
        ANO_PGV,
        "BR-NOVA-ESPERANCA",
        "residencial",
        120.00,
        780.00,
        2.00,
        "Lei Municipal 1.234/2026",
        True,
    ),
    PlantaValoresSeed(
        ANO_PGV,
        "BR-CENTRO",
        "industrial",
        210.00,
        1100.00,
        2.50,
        "Lei Municipal 1.234/2026",
        False,  # rascunho (RN-TEL-004)
    ),
    PlantaValoresSeed(
        ANO_PGV - 1,
        "BR-CENTRO",
        "residencial",
        150.00,
        880.00,
        2.50,
        "Lei Municipal 987/2025",
        True,  # exercício anterior, revogada no seed
    ),
)


@dataclass(frozen=True)
class GeorreferenciaSeed:
    """Georreferência territorial a ser criada."""

    bairro_codigo: str
    geometria: str
    latitude: float
    longitude: float
    vertices: tuple[dict[str, float], ...]
    precisao_m: float


GEORREFERENCIAS_DEMO: tuple[GeorreferenciaSeed, ...] = (
    GeorreferenciaSeed(
        "BR-CENTRO",
        "poligono",
        -13.1289,
        -39.4906,
        (
            {"latitude": -13.1250, "longitude": -39.4880},
            {"latitude": -13.1250, "longitude": -39.4930},
            {"latitude": -13.1330, "longitude": -39.4930},
            {"latitude": -13.1330, "longitude": -39.4880},
        ),
        0.50,
    ),
    GeorreferenciaSeed(
        "BR-NOVA-ESPERANCA",
        "ponto",
        -13.1420,
        -39.4750,
        ({"latitude": -13.1420, "longitude": -39.4750},),
        1.00,
    ),
    GeorreferenciaSeed(
        "BR-ZONA-RURAL",
        "linha",
        -13.2100,
        -39.4200,
        (
            {"latitude": -13.2100, "longitude": -39.4200},
            {"latitude": -13.2600, "longitude": -39.3800},
        ),
        2.50,
    ),
)
