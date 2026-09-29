"""Seeds de dados DEMO do DOM-IMO — Cadastro Imobiliário.

Grava imóveis, vínculos de propriedade, avaliações, características
construtivas e geometrias usando os use cases reais do domínio.

IMPORTANTE:
- Os dados são DEMONISTRATIVOS e fictícios (ver `seeds_dados.py`).
- O seed depende do DOM-TEL populado (logradouros e bairros de referência).
- É executado sob demanda e não realiza commit.
- É idempotente: reexecutar não duplica registros.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import ColumnElement

from ...application.use_cases import (
    AvaliarImovelInput,
    AvaliarImovelUseCase,
    CadastrarImovelInput,
    CadastrarImovelUseCase,
    CancelarAvaliacaoUseCase,
    RegistrarCaracteristicaInput,
    RegistrarCaracteristicaUseCase,
    RegistrarGeometriaInput,
    RegistrarGeometriaUseCase,
    VincularProprietarioInput,
    VincularProprietarioUseCase,
)
from ..repositories import (
    SQLAlchemyAvaliacaoRepository,
    SQLAlchemyCaracteristicaRepository,
    SQLAlchemyGeometriaRepository,
    SQLAlchemyImovelRepository,
    SQLAlchemyProprietarioRepository,
)
from .seeds_dados import (
    ANO_AVALIACAO,
    AUTOR_SEED,
    AVALIACOES_DEMO,
    CARACTERISTICAS_DEMO,
    GEOMETRIAS_DEMO,
    IMOVEIS_DEMO,
    PROPRIETARIOS_DEMO,
)

__all__ = [
    "AUTOR_SEED",
    "ANO_AVALIACAO",
    "IMOVEIS_DEMO",
    "PROPRIETARIOS_DEMO",
    "AVALIACOES_DEMO",
    "CARACTERISTICAS_DEMO",
    "GEOMETRIAS_DEMO",
    "popular_seed_imo",
    "limpar_seed_imo",
]


def _contexto_tel(session: Session) -> tuple[dict[str, str], dict[str, str]]:
    """Resolve as referências do DOM-TEL usadas pelos imóveis demo.

    Retorna dois mapas:
        inscricao -> logradouro_id
        logradouro_id -> bairro_id

    Os logradouros são resolvidos pelo código cadastral (contrato de integração
    com o DOM-TEL, sem FK entre schemas).
    """
    from src.modules.sigmun_territorial.infrastructure.database.models import (
        LogradouroModel,
    )
    from src.modules.sigmun_territorial.infrastructure.repositories import (
        SQLAlchemyLogradouroRepository,
    )

    repo = SQLAlchemyLogradouroRepository(session)
    por_inscricao: dict[str, str] = {}
    for item in IMOVEIS_DEMO:
        logradouro = repo.get_by_codigo(item.logradouro_codigo)
        if logradouro is None:
            raise RuntimeError(
                f"Logradouro {item.logradouro_codigo} ausente: "
                "execute o seed do DOM-TEL antes do seed do DOM-IMO"
            )
        por_inscricao[item.inscricao] = logradouro.id

    bairro_por_logradouro = {
        str(m.id): str(m.bairro_id) for m in session.query(LogradouroModel).all()
    }
    return por_inscricao, bairro_por_logradouro


def _criar_imoveis(session: Session) -> tuple[dict[str, str], int]:
    """Cadastra os imóveis demo. Retorna mapa `inscricao -> imovel_id` e quantidade."""
    repo = SQLAlchemyImovelRepository(session)
    use_case = CadastrarImovelUseCase(repo)
    logradouro_por_inscricao, bairro_por_logradouro = _contexto_tel(session)
    ids: dict[str, str] = {}
    criados = 0
    for item in IMOVEIS_DEMO:
        existente = repo.get_by_inscricao(item.inscricao)
        if existente is not None:
            ids[item.inscricao] = existente.id
            continue
        logradouro_id = logradouro_por_inscricao[item.inscricao]
        imovel = use_case.execute(
            CadastrarImovelInput(
                inscricao_imobiliaria=item.inscricao,
                logradouro_id=logradouro_id,
                bairro_id=bairro_por_logradouro[logradouro_id],
                numero=item.numero,
                complemento=item.complemento,
                tipo=item.tipo,
                tipo_propriedade=item.tipo_propriedade,
                area_terreno_m2=item.area_terreno_m2,
                area_construida_m2=item.area_construida_m2,
                ano_construcao=item.ano_construcao,
                autor_id=AUTOR_SEED,
            )
        )
        ids[item.inscricao] = imovel.id
        criados += 1
    return ids, criados


def _criar_proprietarios(session: Session, imoveis: dict[str, str]) -> int:
    """Vincula os proprietários demo aos respectivos imóveis (RN-IMO-006)."""
    repo = SQLAlchemyProprietarioRepository(session)
    imoveis_repo = SQLAlchemyImovelRepository(session)
    use_case = VincularProprietarioUseCase(repo, imoveis_repo)
    criados = 0
    for item in PROPRIETARIOS_DEMO:
        imovel_id = imoveis[item.inscricao]
        if repo.get_by_imovel_e_cpf(imovel_id, item.cpf) is not None:
            continue
        use_case.execute(
            VincularProprietarioInput(
                imovel_id=imovel_id,
                nome=item.nome,
                cpf=item.cpf,
                vinculo=item.vinculo,
                principal=item.principal,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def _criar_caracteristicas(session: Session, imoveis: dict[str, str]) -> int:
    """Registra as características construtivas demo (RN-IMO-003)."""
    repo = SQLAlchemyCaracteristicaRepository(session)
    imoveis_repo = SQLAlchemyImovelRepository(session)
    use_case = RegistrarCaracteristicaUseCase(repo, imoveis_repo)
    criados = 0
    for item in CARACTERISTICAS_DEMO:
        imovel_id = imoveis[item.inscricao]
        if repo.get_by_imovel(imovel_id) is not None:
            continue
        use_case.execute(
            RegistrarCaracteristicaInput(
                imovel_id=imovel_id,
                obra=item.obra,
                numero_pavimentos=item.numero_pavimentos,
                observacao=item.observacao,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def _criar_geometrias(session: Session, imoveis: dict[str, str]) -> int:
    """Registra as geometrias georreferenciadas demo (RN-IMO-007)."""
    repo = SQLAlchemyGeometriaRepository(session)
    imoveis_repo = SQLAlchemyImovelRepository(session)
    use_case = RegistrarGeometriaUseCase(repo, imoveis_repo)
    criados = 0
    for item in GEOMETRIAS_DEMO:
        imovel_id = imoveis[item.inscricao]
        if repo.get_by_imovel(imovel_id) is not None:
            continue
        use_case.execute(
            RegistrarGeometriaInput(
                imovel_id=imovel_id,
                geometria=item.geometria,
                latitude=item.latitude,
                longitude=item.longitude,
                vertices=[dict(v) for v in item.vertices],
                precisao_m=item.precisao_m,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1
    return criados


def _criar_avaliacoes(session: Session, imoveis: dict[str, str]) -> tuple[int, int]:
    """Aplica as avaliações demo. Retorna (criadas, canceladas)."""
    repo = SQLAlchemyAvaliacaoRepository(session)
    imoveis_repo = SQLAlchemyImovelRepository(session)
    use_case = AvaliarImovelUseCase(repo, imoveis_repo)
    cancelar = CancelarAvaliacaoUseCase(repo)
    criadas = 0
    canceladas = 0
    for item in AVALIACOES_DEMO:
        imovel_id = imoveis[item.inscricao]
        existente = repo.get_by_imovel_e_ano(imovel_id, item.ano)
        if existente is not None:
            continue
        avaliacao = use_case.execute(
            AvaliarImovelInput(
                imovel_id=imovel_id,
                ano=item.ano,
                valor_terreno_m2_unitario=item.valor_terreno_m2_unitario,
                valor_construcao_m2_unitario=item.valor_construcao_m2_unitario,
                aliquota_percent=item.aliquota_percent,
                concluir=item.concluir,
                autor_id=AUTOR_SEED,
            )
        )
        criadas += 1
        # Exercício anterior em rascunho é cancelado, evidenciando RN-IMO-005.
        if item.ano < ANO_AVALIACAO and not item.concluir:
            cancelar.execute(avaliacao.id, "Revisão cadastral do imóvel")
            canceladas += 1
    return criadas, canceladas


def popular_seed_imo(session: Session) -> dict[str, int]:
    """Popula os dados demonstrativos do DOM-IMO.

    Não realiza commit: o controle transacional pertence ao chamador. É
    idempotente: reexecutar não duplica registros. Requer o DOM-TEL populado.

    Retorna um resumo com as quantidades criadas nesta execução:
        imoveis_criados
        proprietarios_criados
        caracteristicas_criadas
        geometrias_criadas
        avaliacoes_criadas
        avaliacoes_canceladas
    """
    imoveis, imoveis_criados = _criar_imoveis(session)
    proprietarios_criados = _criar_proprietarios(session, imoveis)
    caracteristicas_criadas = _criar_caracteristicas(session, imoveis)
    geometrias_criadas = _criar_geometrias(session, imoveis)
    avaliacoes_criadas, avaliacoes_canceladas = _criar_avaliacoes(session, imoveis)

    session.flush()

    return {
        "imoveis_criados": imoveis_criados,
        "proprietarios_criados": proprietarios_criados,
        "caracteristicas_criadas": caracteristicas_criadas,
        "geometrias_criadas": geometrias_criadas,
        "avaliacoes_criadas": avaliacoes_criadas,
        "avaliacoes_canceladas": avaliacoes_canceladas,
    }


def limpar_seed_imo(session: Session) -> dict[str, int]:
    """Remove os registros criados pelo seed do DOM-IMO.

    A ordem respeita as dependências lógicas: avaliações, geometrias e
    características primeiro, depois proprietários e imóveis.

    Retorna as quantidades removidas por tabela.
    """
    from .models import (
        AvaliacaoImovelModel,
        CaracteristicaImovelModel,
        GeometriaImovelModel,
        ImovelModel,
        ProprietarioImovelModel,
    )

    inscricoes = {i.inscricao for i in IMOVEIS_DEMO}
    imovel_ids = [
        str(m.id)
        for m in session.query(ImovelModel)
        .filter(ImovelModel.inscricao_imobiliaria.in_(inscricoes))
        .all()
    ]

    def _apagar(model: type[Any], filtro: ColumnElement[bool] | None) -> int:
        query = session.query(model)
        if filtro is not None:
            query = query.filter(filtro)
        return int(query.delete(synchronize_session=False) or 0)

    removidos: dict[str, int] = {
        "avaliacoes": _apagar(
            AvaliacaoImovelModel,
            AvaliacaoImovelModel.imovel_id.in_(imovel_ids) if imovel_ids else None,
        ),
        "geometrias": _apagar(
            GeometriaImovelModel,
            GeometriaImovelModel.imovel_id.in_(imovel_ids) if imovel_ids else None,
        ),
        "caracteristicas": _apagar(
            CaracteristicaImovelModel,
            CaracteristicaImovelModel.imovel_id.in_(imovel_ids) if imovel_ids else None,
        ),
        "proprietarios": _apagar(
            ProprietarioImovelModel,
            ProprietarioImovelModel.imovel_id.in_(imovel_ids) if imovel_ids else None,
        ),
        "imoveis": _apagar(ImovelModel, ImovelModel.inscricao_imobiliaria.in_(inscricoes)),
    }

    session.flush()
    return removidos
