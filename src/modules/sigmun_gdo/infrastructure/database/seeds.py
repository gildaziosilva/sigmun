"""Seed de dados iniciais do domínio Gestão Documental (DOM-GDO).

Popula o plano de classificação documental inicial e as tabelas de
temporalidade padrão, conforme especificado no artefato
`020-Plano-de-Implantacao` (Onda 1 — Fundação).

A execução é IDEMPOTENTE: registros já existentes (identificados pelo
código) não são recriados, permitindo execução repetida sem duplicação.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from .models import (
    ClassificacaoDocumentalModel,
    TabelaTemporalidadeModel,
    TipoDocumentalModel,
)

# ---------------------------------------------------------------------------
# Plano de classificação documental inicial
# (hierarquia: nivel 1 = classes, nivel 2 = subclasses)
# ---------------------------------------------------------------------------

PLANO_CLASSIFICACAO_INICIAL: list[dict] = [
    # --- Nível 1 ---
    {
        "codigo": "01",
        "nome": "Administração Geral",
        "descricao": "Atos normativos e administrativos gerais do município",
        "nivel": 1,
        "classificacao_pai": None,
        "prazo_retencao": 0,
    },
    {
        "codigo": "02",
        "nome": "Gestão de Pessoas",
        "descricao": "Documentos de recursos humanos e gestão de servidores",
        "nivel": 1,
        "classificacao_pai": None,
        "prazo_retencao": 0,
    },
    {
        "codigo": "03",
        "nome": "Compras e Contratações",
        "descricao": "Processos de aquisição de bens e serviços",
        "nivel": 1,
        "classificacao_pai": None,
        "prazo_retencao": 0,
    },
    {
        "codigo": "04",
        "nome": "Orçamento e Finanças",
        "descricao": "Planejamento orçamentário e execução financeira",
        "nivel": 1,
        "classificacao_pai": None,
        "prazo_retencao": 0,
    },
    # --- Nível 2 (dependem do pai) ---
    {
        "codigo": "01.01",
        "nome": "Atos Normativos",
        "descricao": "Decretos, portarias e regulamentos municipais",
        "nivel": 2,
        "classificacao_pai": "01",
        "prazo_retencao": 0,
    },
    {
        "codigo": "01.02",
        "nome": "Correspondências Oficiais",
        "descricao": "Ofícios, memorandos e comunicações oficiais",
        "nivel": 2,
        "classificacao_pai": "01",
        "prazo_retencao": 180,
    },
    {
        "codigo": "02.01",
        "nome": "Folha de Pagamento",
        "descricao": "Documentos de processamento da folha de pagamento",
        "nivel": 2,
        "classificacao_pai": "02",
        "prazo_retencao": 60,
    },
    {
        "codigo": "03.01",
        "nome": "Processos Licitatórios",
        "descricao": "Editais, atas e contratos de licitações",
        "nivel": 2,
        "classificacao_pai": "03",
        "prazo_retencao": 60,
    },
    {
        "codigo": "04.01",
        "nome": "Leis Orçamentárias",
        "descricao": "LOA, LDO e PPA do município",
        "nivel": 2,
        "classificacao_pai": "04",
        "prazo_retencao": 0,
    },
]

# ---------------------------------------------------------------------------
# Tabelas de temporalidade iniciais
# ---------------------------------------------------------------------------

TABELAS_TEMPORALIDADE_INICIAIS: list[dict] = [
    {
        "codigo": "TEMP-001",
        "nome": "Documentos de uso corrente",
        "prazo_tempo": 12,
        "unidade_tempo": "meses",
        "evento_fim": "encerramento",
        "tipo_destinacao": "eliminacao",
    },
    {
        "codigo": "TEMP-002",
        "nome": "Documentos fiscais",
        "prazo_tempo": 5,
        "unidade_tempo": "anos",
        "evento_fim": "encerramento_exercicio",
        "tipo_destinacao": "eliminacao",
    },
    {
        "codigo": "TEMP-003",
        "nome": "Processos licitatórios",
        "prazo_tempo": 10,
        "unidade_tempo": "anos",
        "evento_fim": "encerramento_contrato",
        "tipo_destinacao": "guarda_permanente",
    },
    {
        "codigo": "TEMP-004",
        "nome": "Atos normativos",
        "prazo_tempo": 0,
        "unidade_tempo": "anos",
        "evento_fim": "emissao",
        "tipo_destinacao": "guarda_permanente",
    },
]

# ---------------------------------------------------------------------------
# Tipos documentais iniciais (tabela de referência `gdo.tipos_documentais`)
# ---------------------------------------------------------------------------

TIPOS_DOCUMENTAIS_INICIAIS: list[dict] = [
    {
        "codigo": "TD-OFICIO",
        "nome": "Ofício",
        "descricao": "Comunicação oficial entre autoridades e entidades",
    },
    {
        "codigo": "TD-MEMORANDO",
        "nome": "Memorando",
        "descricao": "Comunicação oficial entre unidades administrativas",
    },
    {
        "codigo": "TD-REQUISICAO",
        "nome": "Requisição",
        "descricao": "Pedido formal de bens, serviços ou providências",
    },
    {
        "codigo": "TD-PORTARIA",
        "nome": "Portaria",
        "descricao": "Ato administrativo de competência de autoridade",
    },
    {
        "codigo": "TD-DECRETO",
        "nome": "Decreto",
        "descricao": "Ato normativo do Chefe do Executivo",
    },
    {
        "codigo": "TD-EDITAL",
        "nome": "Edital",
        "descricao": "Instrumento de convocação de licitações e certames",
    },
    {
        "codigo": "TD-ATA",
        "nome": "Ata",
        "descricao": "Registro formal de reuniões e sessões",
    },
    {
        "codigo": "TD-RELATORIO",
        "nome": "Relatório",
        "descricao": "Documento de prestação de contas e informação",
    },
    {
        "codigo": "TD-CIRCULAR",
        "nome": "Circular",
        "descricao": "Comunicação oficial dirigida a múltiplos destinatários",
    },
    {
        "codigo": "TD-CERTIDAO",
        "nome": "Certidão",
        "descricao": "Declaração formal sobre fatos e atos administrativos",
    },
    {
        "codigo": "TD-CONTRATO",
        "nome": "Contrato",
        "descricao": "Instrumento jurídico de acordos e convênios",
    },
    {
        "codigo": "TD-PARECER",
        "nome": "Parecer",
        "descricao": "Manifestação técnica ou jurídica sobre matéria formal",
    },
]


def _criar_classificacao(session: Session, dados: dict) -> ClassificacaoDocumentalModel:
    return ClassificacaoDocumentalModel(
        codigo=dados["codigo"],
        nome=dados["nome"],
        descricao=dados["descricao"],
        nivel=dados["nivel"],
        classificacao_pai_id=dados.get("classificacao_pai_id"),
        prazo_retencao=dados["prazo_retencao"],
    )


def _criar_temporalidade(session: Session, dados: dict) -> TabelaTemporalidadeModel:
    return TabelaTemporalidadeModel(
        codigo=dados["codigo"],
        nome=dados["nome"],
        prazo_tempo=dados["prazo_tempo"],
        unidade_tempo=dados["unidade_tempo"],
        evento_fim=dados["evento_fim"],
        tipo_destinacao=dados["tipo_destinacao"],
        is_ativo=True,
    )


def _criar_tipo_documental(session: Session, dados: dict) -> TipoDocumentalModel:
    model = TipoDocumentalModel(
        codigo=dados["codigo"],
        nome=dados["nome"],
        descricao=dados["descricao"],
        is_ativo=True,
    )
    session.add(model)
    return model


def popular_seed_gdo(session: Session) -> dict:
    """Popula o schema `gdo` com os dados iniciais (idempotente).

    Retorna um relatório com a quantidade de registros criados e já
    existentes por categoria. O `commit` fica a cargo do chamador.
    """
    resultado = {
        "classificacoes_criadas": 0,
        "classificacoes_existentes": 0,
        "temporalidades_criadas": 0,
        "temporalidades_existentes": 0,
        "tipos_documentais_criados": 0,
        "tipos_documentais_existentes": 0,
    }

    # --- Plano de classificação (pais antes de filhos) ---
    codigos_existentes = {
        codigo for (codigo,) in session.query(ClassificacaoDocumentalModel.codigo).all()
    }

    criados_por_codigo: dict[str, str] = {}
    for dados in PLANO_CLASSIFICACAO_INICIAL:
        if dados["codigo"] in codigos_existentes:
            resultado["classificacoes_existentes"] += 1
            continue
        pai_id = None
        if dados["classificacao_pai"]:
            pai_id = criados_por_codigo.get(dados["classificacao_pai"])
            if pai_id is None:
                pai = (
                    session.query(ClassificacaoDocumentalModel)
                    .filter(ClassificacaoDocumentalModel.codigo == dados["classificacao_pai"])
                    .first()
                )
                pai_id = str(pai.id) if pai else None
        model = _criar_classificacao(session, {**dados, "classificacao_pai_id": pai_id})
        session.add(model)
        session.flush()
        criados_por_codigo[dados["codigo"]] = str(model.id)
        resultado["classificacoes_criadas"] += 1

    # --- Tabelas de temporalidade ---
    codigos_temp_existentes = {
        codigo for (codigo,) in session.query(TabelaTemporalidadeModel.codigo).all()
    }
    for dados in TABELAS_TEMPORALIDADE_INICIAIS:
        if dados["codigo"] in codigos_temp_existentes:
            resultado["temporalidades_existentes"] += 1
            continue
        session.add(_criar_temporalidade(session, dados))
        resultado["temporalidades_criadas"] += 1

    # --- Tipos documentais (tabela de referência) ---
    codigos_tipo_existentes = {
        codigo for (codigo,) in session.query(TipoDocumentalModel.codigo).all()
    }
    for dados in TIPOS_DOCUMENTAIS_INICIAIS:
        if dados["codigo"] in codigos_tipo_existentes:
            resultado["tipos_documentais_existentes"] += 1
            continue
        session.add(_criar_tipo_documental(session, dados))
        resultado["tipos_documentais_criados"] += 1

    session.flush()
    return resultado


def executar_seed_gdo(session: Session) -> dict:
    """Executa o seed e confirma a transação."""
    resultado = popular_seed_gdo(session)
    session.commit()
    return resultado


__all__ = [
    "PLANO_CLASSIFICACAO_INICIAL",
    "TABELAS_TEMPORALIDADE_INICIAIS",
    "TIPOS_DOCUMENTAIS_INICIAIS",
    "popular_seed_gdo",
    "executar_seed_gdo",
]
