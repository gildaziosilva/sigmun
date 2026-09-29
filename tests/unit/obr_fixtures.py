"""Fixtures compartilhados pelos testes do DOM-OBR (Obras e Infraestrutura)."""

from __future__ import annotations

from datetime import date, timedelta
from unittest.mock import MagicMock

from src.modules.sigmun_obras.application.interfaces import (
    RepositorioDespesa,
    RepositorioEtapa,
    RepositorioMedicao,
    RepositorioObra,
    RepositorioVistoria,
)
from src.modules.sigmun_obras.domain.entities import (
    DespesaObra,
    EtapaObra,
    MedicaoObra,
    Obra,
    SituacaoMedicao,
    SituacaoObra,
)

HOJE = date(2026, 9, 29)


def _obra(situacao: SituacaoObra = SituacaoObra.PLANEJADA, obra_id: str = "obra-1") -> Obra:
    """Obra de referência: orçada, contratada e com datas previstas."""
    return Obra(
        numero="OBR-2026-001",
        nome="Pavimentacao da Rua Principal",
        tipo="pavimentacao",
        situacao=situacao,
        valor_orcado=100_000.0,
        valor_contratado=90_000.0,
        empresa_contratada="Construtora Exemplo LTDA",
        data_inicio_prevista=HOJE,
        data_fim_prevista=HOJE + timedelta(days=120),
        responsavel_tecnico="Eng. Responsavel",
    )


def _obra_em_execucao(obra_id: str = "obra-1") -> Obra:
    """Obra contratada com execução iniciada (aceita medições, RN-OBR-005)."""
    obra = _obra(SituacaoObra.CONTRATADA, obra_id)
    obra.iniciar_execucao(HOJE)
    return obra


def _medicao(
    percentual: float = 30.0,
    valor: float = 27_000.0,
    situacao: SituacaoMedicao = SituacaoMedicao.REGISTRADA,
    medicao_id: str = "med-1",
) -> MedicaoObra:
    return MedicaoObra(
        obra_id="obra-1",
        numero="MED-01",
        percentual_fisico=percentual,
        valor_medido=valor,
        situacao=situacao,
        responsavel_tecnico="Eng. Responsavel",
        data=HOJE,
    )


def _despesa(valor: float = 10_000.0, despesa_id: str = "desp-1") -> DespesaObra:
    return DespesaObra(
        obra_id="obra-1",
        descricao="Repasse do medicao 1",
        tipo="repasse",
        valor=valor,
        data=HOJE,
        credor="Construtora Exemplo LTDA",
    )


def _etapa(percentual_previsto: float = 40.0, etapa_id: str = "etapa-1") -> EtapaObra:
    return EtapaObra(
        obra_id="obra-1",
        numero="ET-01",
        descricao="Estrutura",
        percentual_previsto=percentual_previsto,
        responsavel="Eng. Responsavel",
    )


def repo_obra(obra: Obra | None = None) -> MagicMock:
    """Cria um port de obras simulado."""
    repo = MagicMock(spec=RepositorioObra)
    repo.get_by_id = MagicMock(return_value=obra)
    repo.get_by_numero = MagicMock(return_value=obra)
    repo.save = MagicMock(side_effect=lambda o: o)
    repo.list_all = MagicMock(return_value=[obra] if obra else [])
    return repo


def repo_medicao(*medicoes: MedicaoObra) -> MagicMock:
    """Cria um port de medições simulado.

    O port reflete o comportamento do repositório real: `save` persiste a
    entidade e as listagens subsequentes a enxergam, o que permite verificar o
    recálculo do avanço da obra (RN-OBR-005).
    """
    repo = MagicMock(spec=RepositorioMedicao)
    arma: list[MedicaoObra] = list(medicoes)
    alvo = arma[0] if arma else None
    repo.get_by_id = MagicMock(return_value=alvo)
    repo.get_by_numero_obra = MagicMock(return_value=alvo)

    def _save(medicao: MedicaoObra) -> MedicaoObra:
        for indice, existente in enumerate(arma):
            if existente.id == medicao.id:
                arma[indice] = medicao
                return medicao
        arma.append(medicao)
        return medicao

    repo.save = MagicMock(side_effect=_save)
    repo.list_by_obra = MagicMock(side_effect=lambda _obra_id: list(arma))
    return repo


def repo_despesa(*despesas: DespesaObra) -> MagicMock:
    """Cria um port de despesas simulado (mesma semântica de `repo_medicao`)."""
    repo = MagicMock(spec=RepositorioDespesa)
    arma: list[DespesaObra] = list(despesas)
    alvo = arma[0] if arma else None
    repo.get_by_id = MagicMock(return_value=alvo)

    def _save(despesa: DespesaObra) -> DespesaObra:
        for indice, existente in enumerate(arma):
            if existente.id == despesa.id:
                arma[indice] = despesa
                return despesa
        arma.append(despesa)
        return despesa

    repo.save = MagicMock(side_effect=_save)
    repo.list_by_obra = MagicMock(
        side_effect=lambda _obra_id: [d for d in arma if not d.is_deleted]
    )
    return repo


def repo_etapa(etapa: EtapaObra | None = None) -> MagicMock:
    """Cria um port de etapas simulado."""
    repo = MagicMock(spec=RepositorioEtapa)
    repo.get_by_id = MagicMock(return_value=etapa)
    repo.save = MagicMock(side_effect=lambda e: e)
    repo.list_by_obra = MagicMock(return_value=[etapa] if etapa else [])
    return repo


def repo_vistoria() -> MagicMock:
    """Cria um port de vistorias simulado."""
    repo = MagicMock(spec=RepositorioVistoria)
    repo.get_by_id = MagicMock(return_value=None)
    repo.save = MagicMock(side_effect=lambda v: v)
    repo.list_by_obra = MagicMock(return_value=[])
    return repo
