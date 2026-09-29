"""Seeds de dados DEMO do DOM-OBR — Obras e Infraestrutura.

Grava obras, etapas, medições, despesas e vistorias usando os use cases reais
do domínio (as regras de negócio e o recálculo físico-financeiro são respeitados).

IMPORTANTE:
- Os dados são DEMONSTRATIVOS e fictícios (ver `seeds_dados.py`).
- O seed é executado sob demanda (não no startup da API).
- É idempotente: reexecutar não duplica registros.
- Não realiza commit: o controle transacional pertence ao chamador.

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import ColumnElement

from ...application.use_cases import (
    AprovarMedicaoUseCase,
    CadastrarEtapaInput,
    CadastrarEtapaUseCase,
    CadastrarObraInput,
    CadastrarObraUseCase,
    RegistrarDespesaInput,
    RegistrarDespesaUseCase,
    RegistrarMedicaoInput,
    RegistrarMedicaoUseCase,
    RegistrarVistoriaInput,
    RegistrarVistoriaUseCase,
)
from ...domain.entities import SituacaoEtapa, SituacaoObra
from ...domain.exceptions import DomObrDomainError
from ..repositories import (
    SQLAlchemyDespesaRepository,
    SQLAlchemyEtapaRepository,
    SQLAlchemyMedicaoRepository,
    SQLAlchemyObraRepository,
    SQLAlchemyVistoriaRepository,
)
from .seeds_dados import (
    AUTOR_SEED,
    DESPESAS_DEMO,
    ETAPAS_DEMO,
    HOJE,
    MEDICOES_DEMO,
    OBRAS_DEMO,
    VISTORIAS_DEMO,
    data_da_obra,
)

__all__ = [
    "AUTOR_SEED",
    "OBRAS_DEMO",
    "ETAPAS_DEMO",
    "MEDICOES_DEMO",
    "DESPESAS_DEMO",
    "VISTORIAS_DEMO",
    "popular_seed_obr",
    "limpar_seed_obr",
]


def _criar_obras(session: Session) -> tuple[dict[str, str], int]:
    """Cria as obras ausentes. Retorna ids por número e quantidade criada."""
    repo = SQLAlchemyObraRepository(session)
    use_case = CadastrarObraUseCase(repo)
    ids: dict[str, str] = {}
    criados = 0
    for item in OBRAS_DEMO:
        existente = repo.get_by_numero(item.numero)
        if existente is not None:
            ids[item.numero] = existente.id
            continue
        inicio, fim = data_da_obra(item)
        obra = use_case.execute(
            CadastrarObraInput(
                numero=item.numero,
                nome=item.nome,
                descricao=item.descricao,
                tipo=item.tipo,
                fonte_recurso=item.fonte_recurso,
                valor_orcado=item.valor_orcado,
                valor_contratado=item.valor_contratado,
                empresa_contratada=item.empresa_contratada,
                responsavel_tecnico=item.responsavel_tecnico,
                bairro=item.bairro,
                data_inicio_prevista=inicio,
                data_fim_prevista=fim,
                autor_id=AUTOR_SEED,
            )
        )
        ids[item.numero] = obra.id
        criados += 1

        # Situações derivadas do seed, aplicadas respeitando o ciclo de vida
        # (RN-OBR-002): o cadastro sempre nasce em PLANEJADA e cada transição
        # exige a situação anterior válida. A conclusão é adiada para depois
        # das medições, em `_concluir_obras`.
        if item.situacao in ("em_execucao", "concluida"):
            obra.situacao = SituacaoObra.CONTRATADA
            obra.iniciar_execucao(inicio)
        elif item.situacao == "em_licitacao":
            obra.situacao = SituacaoObra.EM_LICITACAO

        repo.save(obra)
    return ids, criados


def _concluir_obras(session: Session, obras: dict[str, str]) -> int:
    """Conclui as obras do seed cuja execução terminou.

    A conclusão é adiada para depois das medições porque exige 100% do avanço
    físico (RN-OBR-005) — é a própria medição final que comprova a obra.
    """
    repo = SQLAlchemyObraRepository(session)
    concluidas = 0
    for item in OBRAS_DEMO:
        if item.situacao != "concluida":
            continue
        obra_id = obras.get(item.numero)
        obra = repo.get_by_id(obra_id) if obra_id else None
        if obra is None or obra.situacao is SituacaoObra.CONCLUIDA:
            continue
        _, fim = data_da_obra(item)
        obra.concluir(fim)
        repo.save(obra)
        concluidas += 1
    return concluidas


def _criar_etapas(session: Session, obras: dict[str, str]) -> int:
    """Cria as etapas das obras existentes."""
    repo = SQLAlchemyEtapaRepository(session)
    repo_obras = SQLAlchemyObraRepository(session)
    use_case = CadastrarEtapaUseCase(repo, repo_obras)
    criados = 0
    for item in ETAPAS_DEMO:
        obra_id = obras.get(item.obra_numero)
        if obra_id is None:
            continue
        if any(e.numero == item.numero for e in repo.list_by_obra(obra_id)):
            continue
        use_case.execute(
            CadastrarEtapaInput(
                obra_id=obra_id,
                numero=item.numero,
                descricao=item.descricao,
                tipo=item.tipo,
                percentual_previsto=item.percentual_previsto,
                responsavel="Eng. Fiscal da Obra",
                autor_id=AUTOR_SEED,
            )
        )
        # Situações derivadas do seed (RN-OBR-007).
        etapas = repo.list_by_obra(obra_id)
        alvo = next((e for e in etapas if e.numero == item.numero), None)
        if alvo is not None:
            alvo.percentual_realizado = item.percentual_realizado
            alvo.situacao = SituacaoEtapa(item.situacao)
            repo.save(alvo)
        criados += 1
    return criados


def _criar_medicoes(session: Session, obras: dict[str, str]) -> int:
    """Cria e, quando aplicável, aprova as medições das obras."""
    repo = SQLAlchemyMedicaoRepository(session)
    repo_obras = SQLAlchemyObraRepository(session)
    repo_despesas = SQLAlchemyDespesaRepository(session)
    registrar = RegistrarMedicaoUseCase(repo, repo_obras, repo_despesas)
    aprovar = AprovarMedicaoUseCase(repo, repo_obras, repo_despesas)
    criados = 0
    for item in MEDICOES_DEMO:
        obra_id = obras.get(item.obra_numero)
        if obra_id is None or repo.get_by_numero_obra(item.numero, obra_id) is not None:
            continue
        medicao = registrar.execute(
            RegistrarMedicaoInput(
                obra_id=obra_id,
                numero=item.numero,
                tipo=item.tipo,
                percentual_fisico=item.percentual,
                valor_medido=item.valor,
                responsavel_tecnico="Eng. Fiscal da Obra",
                autor_id=AUTOR_SEED,
            )
        )
        if item.aprovar:
            aprovar.execute(medicao.id, AUTOR_SEED)
        criados += 1
    return criados


def _criar_despesas(session: Session, obras: dict[str, str]) -> int:
    """Cria as despesas financeiras das obras."""
    repo = SQLAlchemyDespesaRepository(session)
    repo_obras = SQLAlchemyObraRepository(session)
    repo_medicoes = SQLAlchemyMedicaoRepository(session)
    use_case = RegistrarDespesaUseCase(repo, repo_obras, repo_medicoes)
    criados = 0
    for item in DESPESAS_DEMO:
        obra_id = obras.get(item.obra_numero)
        if obra_id is None:
            continue
        if any(d.descricao == item.descricao for d in repo.list_by_obra(obra_id)):
            continue
        try:
            use_case.execute(
                RegistrarDespesaInput(
                    obra_id=obra_id,
                    descricao=item.descricao,
                    tipo=item.tipo,
                    valor=item.valor,
                    credor=item.credor,
                    autor_id=AUTOR_SEED,
                )
            )
        except DomObrDomainError:
            # Despesa acima do saldo medido é ignorada: o seed respeita a
            # RN-OBR-006 e não inventa pagamento sem medicao approved.
            continue
        criados += 1
    return criados


def _criar_vistorias(session: Session, obras: dict[str, str]) -> int:
    """Cria as vistorias fiscalizadoras das obras."""
    repo = SQLAlchemyVistoriaRepository(session)
    repo_obras = SQLAlchemyObraRepository(session)
    use_case = RegistrarVistoriaUseCase(repo, repo_obras)
    criados = 0
    for item in VISTORIAS_DEMO:
        obra_id = obras.get(item.obra_numero)
        if obra_id is None:
            continue
        use_case.execute(
            RegistrarVistoriaInput(
                obra_id=obra_id,
                data=HOJE + timedelta(days=item.dias_atras),
                tipo=item.tipo,
                parecer=item.parecer,
                percentual_fisico_verificado=item.percentual_verificado,
                fiscal=item.fiscal,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def popular_seed_obr(session: Session) -> dict[str, int]:
    """Popula os dados demonstrativos do DOM-OBR.

    Não realiza commit: o controle transacional pertence ao chamador. É
    idempotente: reexecutar não duplica registros.

    Retorna um resumo com as quantidades criadas nesta execução.
    """
    obras, obras_criadas = _criar_obras(session)
    etapas_criadas = _criar_etapas(session, obras)
    medicoes_criadas = _criar_medicoes(session, obras)
    despesas_criadas = _criar_despesas(session, obras)
    vistorias_criadas = _criar_vistorias(session, obras)
    # A conclusão vai por último: depende do avanço físico acumulado pelas
    # medições aprovadas (RN-OBR-005).
    obras_concluidas = _concluir_obras(session, obras)

    session.flush()

    return {
        "obras_criadas": obras_criadas,
        "etapas_criadas": etapas_criadas,
        "medicoes_criadas": medicoes_criadas,
        "despesas_criadas": despesas_criadas,
        "vistorias_criadas": vistorias_criadas,
        "obras_concluidas": obras_concluidas,
    }


def limpar_seed_obr(session: Session) -> dict[str, int]:
    """Remove os registros criados pelo seed do DOM-OBR.

    A ordem respeita as dependências lógicas: despesas e vistorias primeiro,
    depois medições e etapas e, por fim, as obras.

    Retorna as quantidades removidas por tabela.
    """
    from .models import (
        DespesaObraModel,
        EtapaObraModel,
        MedicaoObraModel,
        ObraModel,
        VistoriaObraModel,
    )

    numeros = {o.numero for o in OBRAS_DEMO}
    obra_ids = [
        str(m.id)
        for m in session.query(ObraModel).filter(ObraModel.numero.in_(numeros)).all()
    ]

    def _apagar(
        model: type[Any], filtro: ColumnElement[bool] | None
    ) -> int:
        query = session.query(model)
        if filtro is not None:
            query = query.filter(filtro)
        return int(query.delete(synchronize_session=False) or 0)

    removidos = {
        "despesas": _apagar(
            DespesaObraModel,
            DespesaObraModel.obra_id.in_(obra_ids) if obra_ids else None,
        ),
        "vistorias": _apagar(
            VistoriaObraModel,
            VistoriaObraModel.obra_id.in_(obra_ids) if obra_ids else None,
        ),
        "medicoes": _apagar(
            MedicaoObraModel,
            MedicaoObraModel.obra_id.in_(obra_ids) if obra_ids else None,
        ),
        "etapas": _apagar(
            EtapaObraModel,
            EtapaObraModel.obra_id.in_(obra_ids) if obra_ids else None,
        ),
        "obras": _apagar(ObraModel, ObraModel.numero.in_(numeros)),
    }

    session.flush()
    return removidos
