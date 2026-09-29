"""Dados demonstrativos (DEMO) do DOM-IMO — Cadastro Imobiliário.

Os registros aqui definidos são FICTÍCIOS, criados apenas para demonstrar as
telas administrativas. Não representam cadastro real de imóveis ou
proprietários do Município de Camacan-BA.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

AUTOR_SEED = "seed-imo"
ANO_AVALIACAO = date.today().year


@dataclass(frozen=True)
class ImovelSeed:
    """Unidade imobiliária a ser criada."""

    inscricao: str
    logradouro_codigo: str
    numero: str
    complemento: str
    tipo: str
    tipo_propriedade: str
    area_terreno_m2: float
    area_construida_m2: float
    ano_construcao: int | None


IMOVEIS_DEMO: tuple[ImovelSeed, ...] = (
    ImovelSeed("INS-2026-0001", "LG-001", "120", "Casa", "casa", "proprio", 200.0, 120.0, 2015),
    ImovelSeed("INS-2026-0002", "LG-001", "124", "", "lote", "proprio", 300.0, 0.0, None),
    ImovelSeed("INS-2026-0003", "LG-002", "450", "Sala 3", "loja", "alugado", 500.0, 260.0, 2010),
    ImovelSeed("INS-2026-0004", "LG-004", "88", "", "casa", "proprio", 180.0, 95.0, 2018),
    ImovelSeed("INS-2026-0005", "LG-004", "92", "", "terreno", "invencionado", 220.0, 0.0, None),
    ImovelSeed(
        "INS-2026-0006", "LG-005", "35", "Galpao 1", "galpao", "cedido", 1200.0, 640.0, 2005
    ),
    ImovelSeed(
        "INS-2026-0007", "LG-002", "900", "Bloco A", "apartamento", "proprio", 150.0, 450.0, 2012
    ),
    ImovelSeed("INS-2026-0008", "LG-003", "s/n", "", "lote", "proprio", 800.0, 0.0, None),
)


@dataclass(frozen=True)
class ProprietarioSeed:
    """Vínculo de propriedade a ser criado."""

    inscricao: str
    nome: str
    cpf: str
    vinculo: str
    principal: bool


PROPRIETARIOS_DEMO: tuple[ProprietarioSeed, ...] = (
    ProprietarioSeed("INS-2026-0001", "Maria Aparecida Souza", "12345678909", "titular", True),
    ProprietarioSeed("INS-2026-0001", "Joao Pedro Souza", "12345678917", "parceiro", False),
    ProprietarioSeed("INS-2026-0002", "Jose Carlos Lima", "23456789008", "titular", True),
    ProprietarioSeed("INS-2026-0003", "Ana Paula Ferreira", "34567890007", "titular", True),
    ProprietarioSeed("INS-2026-0004", "Rita de Cassia Lima", "23456789016", "titular", True),
    ProprietarioSeed("INS-2026-0005", "Carlos Eduardo Reis", "45678900123", "titular", True),
    ProprietarioSeed("INS-2026-0006", "Bento Ferreira", "34567890015", "titular", True),
    ProprietarioSeed(
        "INS-2026-0006", "Construtora Horizonte LTDA", "11222333000181", "parceiro", False
    ),
    ProprietarioSeed("INS-2026-0007", "Beatriz Oliveira Rocha", "56789012345", "titular", True),
    ProprietarioSeed(
        "INS-2026-0008", "Prefeitura Municipal de Camacan", "00000000000191", "titular", True
    ),
)


@dataclass(frozen=True)
class AvaliacaoSeed:
    """Avaliação de valor venal a ser criada."""

    inscricao: str
    ano: int
    valor_terreno_m2_unitario: float
    valor_construcao_m2_unitario: float
    aliquota_percent: float
    concluir: bool


AVALIACOES_DEMO: tuple[AvaliacaoSeed, ...] = (
    AvaliacaoSeed("INS-2026-0001", ANO_AVALIACAO, 180.00, 950.00, 2.50, True),
    AvaliacaoSeed("INS-2026-0002", ANO_AVALIACAO, 180.00, 950.00, 2.50, True),
    AvaliacaoSeed("INS-2026-0003", ANO_AVALIACAO, 320.00, 1450.00, 2.50, True),
    AvaliacaoSeed("INS-2026-0004", ANO_AVALIACAO - 1, 105.00, 690.00, 2.00, True),
    AvaliacaoSeed("INS-2026-0005", ANO_AVALIACAO - 1, 105.00, 690.00, 2.00, False),
)


@dataclass(frozen=True)
class CaracteristicaSeed:
    """Característica construtiva a ser criada."""

    inscricao: str
    obra: str
    numero_pavimentos: int
    observacao: str


CARACTERISTICAS_DEMO: tuple[CaracteristicaSeed, ...] = (
    CaracteristicaSeed("INS-2026-0001", "residencial", 1, "Construção em alvenaria, sem reforma"),
    CaracteristicaSeed("INS-2026-0003", "comercial", 2, "Loja com mezanino"),
    CaracteristicaSeed("INS-2026-0004", "residencial", 1, "Casa térrea"),
    CaracteristicaSeed("INS-2026-0006", "industrial", 1, "Galpao em estrutura metálica"),
    CaracteristicaSeed("INS-2026-0007", "residencial", 4, "Edifício de 4 pavimentos"),
)


@dataclass(frozen=True)
class GeometriaSeed:
    """Geometria georreferenciada do lote a ser criada."""

    inscricao: str
    geometria: str
    latitude: float
    longitude: float
    vertices: tuple[dict[str, float], ...]
    precisao_m: float


GEOMETRIAS_DEMO: tuple[GeometriaSeed, ...] = (
    GeometriaSeed(
        "INS-2026-0001",
        "poligono",
        -13.12890,
        -39.49060,
        (
            {"latitude": -13.12895, "longitude": -39.49070},
            {"latitude": -13.12895, "longitude": -39.49050},
            {"latitude": -13.12885, "longitude": -39.49050},
            {"latitude": -13.12885, "longitude": -39.49070},
        ),
        0.30,
    ),
    GeometriaSeed(
        "INS-2026-0003",
        "poligono",
        -13.12900,
        -39.49120,
        (
            {"latitude": -13.12910, "longitude": -39.49140},
            {"latitude": -13.12910, "longitude": -39.49100},
            {"latitude": -13.12890, "longitude": -39.49100},
            {"latitude": -13.12890, "longitude": -39.49140},
        ),
        0.40,
    ),
    GeometriaSeed(
        "INS-2026-0004",
        "ponto",
        -13.14200,
        -39.47500,
        ({"latitude": -13.14200, "longitude": -39.47500},),
        1.00,
    ),
    GeometriaSeed(
        "INS-2026-0007",
        "linha",
        -13.13300,
        -39.49800,
        (
            {"latitude": -13.13300, "longitude": -39.49800},
            {"latitude": -13.13380, "longitude": -39.49860},
        ),
        0.80,
    ),
)
