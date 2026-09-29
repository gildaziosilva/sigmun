"""Dados demonstrativos (DEMO) do DOM-OBR — Obras e Infraestrutura.

Os registros aqui definidos são FICTÍCIOS, criados apenas para demonstrar as
telas administrativas. Não representam cadastro real de obras, empresas ou
medições do Município de Camacan-BA.

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

AUTOR_SEED = "seed-obr"
HOJE = date.today()


@dataclass(frozen=True)
class ObraSeed:
    """Obra pública a ser criada."""

    numero: str
    nome: str
    descricao: str
    tipo: str
    situacao: str
    fonte_recurso: str
    valor_orcado: float
    valor_contratado: float
    empresa_contratada: str
    responsavel_tecnico: str
    bairro: str
    inicio_dias: int
    prazo_dias: int


OBRAS_DEMO: tuple[ObraSeed, ...] = (
    ObraSeed(
        "OBR-2026-001",
        "Pavimentacao asfaltica da Rua da Matriz",
        "Recapeamento em asfalto da Rua da Matriz, trecho de 1,2 km.",
        "pavimentacao",
        "em_execucao",
        "orcamento_proprio",
        480_000.0,
        452_000.0,
        "Construtora Exemplo LTDA",
        "Eng. Ana Souza",
        "Centro",
        -60,
        120,
    ),
    ObraSeed(
        "OBR-2026-002",
        "Drenagem e aguas pluviais do bairro Nova Esperanca",
        "Implantacao de galerias e bocas de lobo em 3.200 m de extensão.",
        "drenagem",
        "em_execucao",
        "convenio_estadual",
        890_000.0,
        850_000.0,
        "Engenharia Noroeste S.A.",
        "Eng. Bruno Lima",
        "Nova Esperanca",
        -30,
        180,
    ),
    ObraSeed(
        "OBR-2026-003",
        "Reforma e pintura da Escola Municipal",
        "Reforma da cobertura, pintura e adequacy hidrossanitaria.",
        "reforma",
        "contratada",
        "orcamento_proprio",
        175_000.0,
        168_000.0,
        "Reformas Central LTDA",
        "Eng. Carla Dias",
        "Centro",
        15,
        90,
    ),
    ObraSeed(
        "OBR-2026-004",
        "Iluminacao publica da Avenida Principal",
        "Substituicao de 180 luminarias por LED e nova rede.",
        "iluminacao",
        "em_licitacao",
        "convenio_federal",
        320_000.0,
        0.0,
        "",
        "Eng. Daniel Reis",
        "Centro",
        45,
        150,
    ),
    ObraSeed(
        "OBR-2025-018",
        "Construcao de praca publica",
        "Praca com piso intertravado, Quadra e paisagismo.",
        "praca",
        "concluida",
        "orcamento_proprio",
        260_000.0,
        249_000.0,
        "Construtora Exemplo LTDA",
        "Eng. Ana Souza",
        "Comercio",
        -240,
        -30,
    ),
)


@dataclass(frozen=True)
class MedicaoSeed:
    """Medição físico-financeira a ser criada."""

    obra_numero: str
    numero: str
    tipo: str
    percentual: float
    valor: float
    aprovar: bool


MEDICOES_DEMO: tuple[MedicaoSeed, ...] = (
    MedicaoSeed("OBR-2026-001", "MED-01", "avanco", 35.0, 158_200.0, True),
    MedicaoSeed("OBR-2026-001", "MED-02", "avanco", 20.0, 90_400.0, False),
    MedicaoSeed("OBR-2026-002", "MED-01", "etapa", 25.0, 212_500.0, True),
    MedicaoSeed("OBR-2026-002", "MED-02", "etapa", 15.0, 127_500.0, True),
    MedicaoSeed("OBR-2025-018", "MED-FINAL", "final", 100.0, 249_000.0, True),
)


@dataclass(frozen=True)
class EtapaSeed:
    """Etapa de execução a ser criada."""

    obra_numero: str
    numero: str
    descricao: str
    tipo: str
    percentual_previsto: float
    percentual_realizado: float
    situacao: str


ETAPAS_DEMO: tuple[EtapaSeed, ...] = (
    EtapaSeed(
        "OBR-2026-001",
        "ET-01",
        "Terraplanagem e sub-base",
        "terraplanagem",
        40.0,
        100.0,
        "concluida",
    ),
    EtapaSeed(
        "OBR-2026-001", "ET-02", "Ligacao e recapeamento", "pavimentacao", 45.0, 55.0, "em_execucao"
    ),
    EtapaSeed("OBR-2026-001", "ET-03", "Sinalizacao", "acabamento", 15.0, 0.0, "pendente"),
    EtapaSeed(
        "OBR-2026-002", "ET-01", "Escavacao das galerias", "terraplanagem", 50.0, 100.0, "concluida"
    ),
    EtapaSeed(
        "OBR-2026-002", "ET-02", "Assentamento de tubos", "instalacao", 35.0, 40.0, "em_execucao"
    ),
    EtapaSeed(
        "OBR-2025-018", "ET-01", "Obra civil da praca", "estrutura", 60.0, 100.0, "concluida"
    ),
    EtapaSeed(
        "OBR-2025-018", "ET-02", "Paisagismo e iluminacao", "paisagismo", 40.0, 100.0, "concluida"
    ),
)


@dataclass(frozen=True)
class DespesaSeed:
    """Despesa financeira a ser criada."""

    obra_numero: str
    descricao: str
    tipo: str
    valor: float
    credor: str


DESPESAS_DEMO: tuple[DespesaSeed, ...] = (
    DespesaSeed(
        "OBR-2026-001",
        "Repasse da medicao MED-01",
        "repasse",
        120_000.0,
        "Construtora Exemplo LTDA",
    ),
    DespesaSeed(
        "OBR-2026-001", "Material de brita graduada", "material", 38_200.0, "Pedreira Vale Verde"
    ),
    DespesaSeed(
        "OBR-2026-002",
        "Repasse da medicao MED-01",
        "repasse",
        180_000.0,
        "Engenharia Noroeste S.A.",
    ),
    DespesaSeed(
        "OBR-2025-018", "Repasse da medicao final", "repasse", 249_000.0, "Construtora Exemplo LTDA"
    ),
)


@dataclass(frozen=True)
class VistoriaSeed:
    """Vistoria fiscalizadora a ser criada."""

    obra_numero: str
    tipo: str
    parecer: str
    percentual_verificado: float
    fiscal: str
    dias_atras: int


VISTORIAS_DEMO: tuple[VistoriaSeed, ...] = (
    VistoriaSeed("OBR-2026-001", "periodica", "aprovado", 35.0, "Fiscal Joana Reis", -20),
    VistoriaSeed(
        "OBR-2026-001", "parcial", "aprovado_com_ressalvas", 55.0, "Fiscal Joana Reis", -5
    ),
    VistoriaSeed("OBR-2026-002", "periodica", "aprovado", 40.0, "Fiscal Marcos Alves", -10),
    VistoriaSeed("OBR-2025-018", "final", "aprovado", 100.0, "Fiscal Marcos Alves", -20),
)


def data_da_obra(obra: ObraSeed) -> tuple[date, date]:
    """Datas prevista e real de início/fim, derivadas dos offsets do seed."""
    return (
        HOJE + timedelta(days=obra.inicio_dias),
        HOJE + timedelta(days=obra.prazo_dias),
    )
