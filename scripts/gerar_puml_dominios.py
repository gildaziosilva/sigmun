#!/usr/bin/env python
"""Gera os diagramas PUML dos domínios SIGMUN que estão sem conteúdo.

Dois grupos são cobertos:

* **Implementados** (DOM-CUM, DOM-DIA, DOM-GEO, DOM-IMO, DOM-OBR, DOM-TEL): os
  seis diagramas são derivados do código — modelos ORM, OpenAPI, casos de uso,
  enums e regras — pelo mesmo critério de ``gerar_artefatos_territoriais.py``.
* **Propostos** (DOM-ANA, DOM-CPT, DOM-DEC, DOM-GOV, DOM-IND, DOM-INF,
  DOM-MAM, DOM-MOB, DOM-PLA): domínios documentais sem módulo implementado
  segundo a matriz 031; os diagramas registram o **modelo proposto**, a partir
  de ``000-Dominio-*.md`` e de ``Mapa-de-Dominios.md``, e assim se declaram.

Além dos domínios, o gerador também produz os seis diagramas de
``01-Arquitetura-Corporativa`` (``000-Arquitetura-Geral`` a
``005-Infraestrutura``), derivados da estrutura real do repositório: módulos de
``src/``, frontends, aplicativos móveis, Alembic e serviços do
``docker-compose.yml``.

Uso:
    .venv/bin/python scripts/gerar_puml_dominios.py
    .venv/bin/python scripts/gerar_puml_dominios.py --apenas DOM-IND

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

import argparse
import importlib
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "scripts"))
os.chdir(RAIZ)

import docs_dados as _DADOS  # noqa: E402

from src.main import app  # noqa: E402

DATA = "2026-09-30"


# ==============================================================================
# EXTRAÇÃO DO CÓDIGO-FONTE (domínios implementados)
# ==============================================================================


def extrair_tabelas(modulo: str) -> dict[str, dict]:
    """`(tabela) -> nome da classe, colunas e docstring` dos modelos ORM."""
    from sqlalchemy import inspect as sa_inspect

    modelos = importlib.import_module(f"src.modules.{modulo}.infrastructure.database.models")
    bases = [
        obj
        for nome, obj in vars(modelos).items()
        if isinstance(obj, type) and nome.endswith("Base") and obj.__module__ == modelos.__name__
    ]
    saida: dict[str, dict] = {}
    for base in bases:
        for classe in base.__subclasses__():
            info = sa_inspect(classe)
            colunas = []
            for coluna in info.columns:
                flags: list[str] = []
                if coluna.primary_key:
                    flags.append("PK")
                if getattr(coluna, "unique", False):
                    flags.append("UQ")
                if not coluna.nullable and not coluna.primary_key:
                    flags.append("NN")
                colunas.append(
                    {
                        "nome": coluna.name,
                        "tipo": str(coluna.type),
                        "flags": flags,
                    }
                )
            saida[classe.__tablename__] = {
                "classe": classe.__name__,
                "colunas": colunas,
                "doc": (classe.__doc__ or "").strip().splitlines()[0] if classe.__doc__ else "",
            }
    return saida


def extrair_operacoes(prefixo: str) -> tuple[int, list[tuple[str, str]]]:
    """`(quantidade, [(caminho, métodos)])` das operações sob o prefixo."""
    spec = app.openapi()
    total = 0
    caminhos: list[tuple[str, str]] = []
    for caminho in sorted(spec["paths"]):
        if not caminho.startswith(prefixo):
            continue
        metodos = sorted(
            m.upper()
            for m in spec["paths"][caminho]
            if m.lower() in {"get", "post", "patch", "delete", "put"}
        )
        if metodos:
            total += len(metodos)
            caminhos.append((caminho, "/".join(metodos)))
    return total, caminhos


def extrair_use_cases(modulo: str) -> list[str]:
    """Nomes das classes de caso de uso publicadas pelo pacote do módulo."""
    pacote = importlib.import_module(f"src.modules.{modulo}.application.use_cases")
    return [
        nome
        for nome in getattr(pacote, "__all__", [])
        if isinstance(getattr(pacote, nome), type) and nome.endswith("UseCase")
    ]


def extrair_enums(modulo: str) -> dict[str, list[tuple[str, str]]]:
    """`(Enum) -> [(membro, valor)]` declarados nas entidades do módulo."""
    saida: dict[str, list[tuple[str, str]]] = {}
    base = RAIZ / "src" / "modules" / modulo
    for caminho in sorted(base.rglob("*.py")):
        linhas = caminho.read_text(encoding="utf-8", errors="replace").splitlines()
        indice = 0
        while indice < len(linhas):
            cabecalho = re.match(r"class (\w+)\(([^)]*Enum[^)]*)\):", linhas[indice])
            if not cabecalho:
                indice += 1
                continue
            nome = cabecalho.group(1)
            membros: list[tuple[str, str]] = []
            proximo = indice + 1
            while proximo < len(linhas):
                linha = linhas[proximo]
                if linha and not linha[0].isspace():
                    break
                achado = re.match(r"\s+(\w+)\s*=\s*(.+?)\s*$", linha)
                if achado and not achado.group(1).startswith("__"):
                    valor = achado.group(2).split("#")[0].strip()
                    if valor.startswith(("'", '"')):
                        membros.append((achado.group(1), valor))
                proximo += 1
            if membros:
                saida[nome] = membros
            indice = proximo
    return saida


def extrair_regras(modulo: str, codigo: str) -> list[str]:
    """Identificadores `RN-XXX-###` citados no código do módulo."""
    achadas: set[str] = set()
    padrao = re.compile(rf"RN-{codigo}-\d{{3}}")
    for caminho in (RAIZ / "src" / "modules" / modulo).rglob("*.py"):
        texto = caminho.read_text(encoding="utf-8", errors="replace")
        achadas.update(padrao.findall(texto))
    return sorted(achadas)


def regras_documentadas(prefixo: str) -> list[tuple[str, str]]:
    """`(id, descrição)` das regras declaradas em `docs_dados`.

    Aceita as duas formas usadas no arquivo: dicionário (`id`, `descricao`) e
    tupla `(id, título, tipo, processo, descrição, ...)`.
    """
    saida: list[tuple[str, str]] = []
    for item in getattr(_DADOS, f"{prefixo}_REGRAS", []):
        if isinstance(item, dict):
            saida.append((item["id"], item["descricao"]))
        else:
            saida.append((item[0], item[4]))
    return saida


# ==============================================================================
# TIPOS, HELPERS DE RENDERIZAÇÃO E EMISSORES
# ==============================================================================

TIPO_DOMINIO = {
    "UUID": "string",
    "TEXT": "string",
    "VARCHAR": "string",
    "CHAR": "string",
    "INTEGER": "int",
    "BIGINT": "int",
    "SMALLINT": "int",
    "FLOAT": "decimal",
    "FLOAT8": "decimal",
    "DOUBLE PRECISION": "decimal",
    "NUMERIC": "decimal",
    "BOOLEAN": "bool",
    "DATE": "date",
    "DATETIME": "datetime",
    "TIMESTAMP": "datetime",
    "TIMESTAMPTZ": "datetime",
    "JSON": "json",
    "JSONB": "json",
}


def tipo_dominio(tipo_sql: str) -> str:
    chave = tipo_sql.split("(")[0].split("[")[0].strip().upper()
    return TIPO_DOMINIO.get(chave, "string")


def coluna_sql(coluna: dict) -> str:
    """`nome : TIPO <<flags>>` no formato dos diagramas de persistência."""
    linha = f"{coluna['nome']} : {coluna['tipo']}"
    flags = [f for f in coluna["flags"] if f != "PK"]
    if "PK" in coluna["flags"]:
        linha += " <<PK>>"
    elif flags:
        ordenadas = [f for f in ("UQ", "NN") if f in flags]
        linha += f" <<{', '.join(ordenadas)}>>"
    return linha


def legenda(codigo: str, nome: str, tipo: str, subtipo: str, status: str) -> str:
    return (
        "legend\n"
        "SIGMUN\n"
        f"{codigo} — {nome}\n"
        f"{tipo} — {subtipo}\n"
        "Classificação da Informação: Pública\n"
        "Responsável: Equipe SIGMUN\n"
        f"Status da revisão: {status}\n"
        "endlegend"
    )


def nota_listagem(titulo: str, itens: list[str], limite: int = 6) -> str:
    """Bloco de nota com lista; além do limite, resume com `e mais N`."""
    linhas = [titulo, ""]
    for item in itens[:limite]:
        linhas.append(f"- {item}")
    if len(itens) > limite:
        linhas.append(f"- e mais {len(itens) - limite}")
    return "\n".join(linhas)


def envolver(conteudo: str) -> str:
    return f"```plantuml\n{conteudo.rstrip()}\n```\n"


def verbo_de_caso_de_uso(nome: str) -> str:
    raiz = nome.replace("UseCase", "")
    if raiz.startswith(("Cadastrar", "Registrar", "Adicionar", "Vincular")):
        return "POST"
    if raiz.startswith(("Atualizar", "Alterar")):
        return "PATCH"
    if raiz.startswith(("Listar", "Consultar")):
        return "GET"
    if raiz.startswith(("Excluir", "Remover", "Inativar", "Revogar")):
        return "DELETE"
    return "POST"


TRANSVERSAIS = (
    ("DOM-IDN", "Identidade e Acesso", "IDN"),
    ("DOM-GDO", "Gestão Documental", "GDO"),
    ("DOM-MET", "Metadados", "MET"),
    ("DOM-INT", "Interoperabilidade", "INT"),
)


def transversais(m: dict, incluir_int: bool = False) -> list[tuple[str, str, str]]:
    """Serviços transversais do diagrama, sem repetir os correlatos do domínio."""
    correlatos = {sigla for sigla, _ in m["correlatos"]}
    return [
        item
        for item in TRANSVERSAIS
        if item[2] != "AUD" and item[0] not in correlatos and (incluir_int or item[2] != "INT")
    ]


# ------------------------------------------------------------------------------
# 000 — Visão Arquitetural
# ------------------------------------------------------------------------------


def arquivo_000(m: dict) -> str:
    implementado = m["implementado"]
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Visão Arquitetural",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Visão Arquitetural",
            "Arquitetura do domínio",
            m["status"],
        ),
        "",
        "skinparam componentStyle rectangle",
        "skinparam packageStyle rectangle",
        "",
        'package "Usuários e Canais" {',
        '  actor "Servidor\\npúblico" as User',
        '  component "Portal Web\\nSIGMUN" as Portal',
        "}",
        "",
        f'package "{m["codigo"]} — {m["nome"]}" {{',
        f'  component "API\\n{m["prefixo"]}" as API',
    ]
    exibiveis = m["capacidades"][:6]
    for indice, item in enumerate(exibiveis):
        linhas.append(f'  component "{item.replace("UseCase", "")}" as UC{indice}')
    linhas.append("}")

    if m["correlatos"]:
        linhas += ["", 'package "Domínios Correlatos" {']
        for sigla, nome in m["correlatos"]:
            linhas.append(f'  component "{sigla}\\n{nome}" as D{sigla[4:]}')
        linhas.append("}")

    linhas += ["", 'package "Serviços Transversais" {']
    for sigla, rotulo, alias in transversais(m):
        linhas.append(f'  component "{sigla}\\n{rotulo}" as {alias}')
    linhas.append('  component "Auditoria" as AUD')
    linhas += [
        "}",
        "",
        f'database "PostgreSQL\\nschema {m["schema"]}" as DB',
        "",
        "User --> Portal : executa rotina",
        "Portal --> API : operações do domínio",
        "",
    ]
    for indice, item in enumerate(exibiveis):
        acao = verbo_de_caso_de_uso(item) if implementado else "previsto"
        linhas.append(f"API --> UC{indice} : {acao}")
    linhas.append("")

    rotulo_correlato = "troca de dados" if implementado else "troca de dados (prevista)"
    for sigla, _ in m["correlatos"]:
        linhas.append(f"API --> D{sigla[4:]} : {rotulo_correlato}")

    rotulos_transversais = {
        "IDN": "autenticação e autorização",
        "GDO": "documentos",
        "MET": "metadados",
    }
    disponiveis = {alias for _, _, alias in transversais(m)}
    for alias in ("IDN", "GDO", "MET"):
        if alias in disponiveis:
            linhas.append(f"API --> {alias} : {rotulos_transversais[alias]}")
    linhas.append("API --> AUD : eventos de auditoria")
    linhas.append("")
    for indice in range(len(exibiveis)):
        linhas.append(f"UC{indice} --> DB : persistência")
    linhas.append("")

    if implementado:
        nota_api = (
            f"note right of API\n"
            f"O {m['codigo']} cobre {m['nome']}.\n\n"
            f"A API expõe {m['operacoes']} operações\n"
            f"em 1 prefixo.\n\n"
            f"{len(m['use_cases'])} casos de uso no código.\n"
            f"end note"
        )
        rotulo_regras = f"Regras de negócio ({len(m['regras'])}):"
        rotulo_tabelas = f"{len(m['tabelas'])} tabelas mapeadas:"
    else:
        nota_api = (
            f"note right of API\n"
            f"O {m['codigo']} cobre {m['nome']}.\n\n"
            f"Modelo proposto: o domínio não possui\n"
            f"módulo implementado (matriz 031).\n\n"
            f"Capacidades previstas para {m['prefixo']}.\n"
            f"end note"
        )
        rotulo_regras = f"Regras propostas ({len(m['regras'])}):"
        rotulo_tabelas = f"{len(m['tabelas'])} tabelas propostas:"

    linhas += [
        nota_api,
        "",
        "note bottom of API",
        nota_listagem(rotulo_regras, [r for r, _ in m["regras"]]),
        "end note",
        "",
        "note bottom of DB",
        nota_listagem(rotulo_tabelas, [t["tabela"] for t in m["tabelas"]]),
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


# ------------------------------------------------------------------------------
# 001 — Modelo de Domínio
# ------------------------------------------------------------------------------


def arquivo_001(m: dict) -> str:
    rotulo_regras = (
        f"Regras de negócio ({len(m['regras'])}):"
        if m["implementado"]
        else f"Regras propostas ({len(m['regras'])}):"
    )
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Modelo de Domínio",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Modelo de Domínio",
            "Entidades e regras de negócio",
            m["status"],
        ),
        "",
        "hide methods",
        "hide stereotypes",
        "skinparam classAttributeIconSize 0",
        "",
        f'package "Entidades de {m["codigo"]}" {{',
        "",
    ]
    for entidade in m["entidades"]:
        linhas.append(f"class {entidade['classe']} <<Entity>> {{")
        for nome, tipo in entidade["atributos"]:
            linhas.append(f"  +{nome}: {tipo}")
        linhas.append("}")
        linhas.append("")
    linhas.append("}")

    if m["enums"]:
        linhas += ["", 'package "Enumerações" {', ""]
        for nome, membros in m["enums"].items():
            linhas.append(f"enum {nome} {{")
            for membro, valor in membros:
                linhas.append(f"  {membro} = {valor.replace(chr(34), chr(39))}")
            linhas.append("}")
            linhas.append("")
        linhas.append("}")

    linhas += [
        "",
        "' =========================================================",
        "' RELACIONAMENTOS",
        "' =========================================================",
        "",
    ]
    for pai, filho, coluna in m["relacoes"]:
        linhas.append(f'{pai} "1" *-- "0..*" {filho} : "{coluna}"')
    if m["relacoes"]:
        linhas.append("")
    for classe, enum in m["enum_links"]:
        linhas.append(f"{classe} --> {enum}")

    linhas += [
        "",
        f"note right of {m['central']}",
        nota_listagem(rotulo_regras, [f"{r}:\n  {t}" for r, t in m["regras"]]),
        "end note",
        "",
        f"note bottom of {m['central']}",
    ]
    if m["implementado"]:
        comportamentos = m["use_cases"]
        rotulo_comportamentos = f"Comportamentos ({len(comportamentos)}):"
    else:
        comportamentos = m["capacidades"]
        rotulo_comportamentos = f"Capacidades previstas ({len(comportamentos)}):"
    linhas.append(nota_listagem(rotulo_comportamentos, comportamentos, limite=10))
    linhas += ["end note", "", "@enduml"]
    return envolver("\n".join(linhas))


# ------------------------------------------------------------------------------
# 002 — Processos
# ------------------------------------------------------------------------------


def arquivo_002(m: dict) -> str:
    etapas = m["use_cases"] if m["implementado"] else m["processos"]
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Processos",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Processos",
            "Fluxo do caso de uso principal",
            m["status"],
        ),
        "",
        "start",
        "",
    ]
    for etapa in etapas[:10]:
        rotulo = etapa.replace("UseCase", "")
        rotulo = re.sub(r"(?<!^)(?=[A-Z])", " ", rotulo).strip()
        linhas.append(f":{rotulo};")
    if len(etapas) > 10:
        excedente = "casos de uso" if m["implementado"] else "etapas"
        linhas.append(f":E mais {len(etapas) - 10} {excedente};")
    linhas += ["", ":Registrar evento de auditoria;", "stop", "", "note left"]

    linhas.append(f"A rotina gira em torno de {m['central']}.")
    linhas.append("")
    if m["implementado"]:
        linhas.append(f"Casos de uso no código: {len(m['use_cases'])}.")
        linhas.append(f"Entidades do domínio: {len(m['entidades'])}.")
        linhas.append(f"Tabelas mapeadas: {len(m['tabelas'])}.")
    else:
        linhas.append(f"Modelo proposto: capacidades previstas: {len(m['capacidades'])}.")
        linhas.append(f"Entidades propostas: {len(m['entidades'])}.")
        linhas.append(f"Tabelas propostas: {len(m['tabelas'])}.")
    linhas += [
        "end note",
        "",
        "note right",
        nota_listagem(f"Validações ({len(m['regras'])}):", [r for r, _ in m["regras"]]),
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


# ------------------------------------------------------------------------------
# 003 — Máquina de Estados
# ------------------------------------------------------------------------------


def arquivo_003(m: dict) -> str:
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Máquina de Estados",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Máquina de Estados",
            "Ciclo de vida das entidades",
            m["status"],
        ),
        "",
        "hide empty description",
        "",
    ]
    linhas += m["estados"]
    for nota in m["notas_003"]:
        linhas += ["", nota]
    linhas += ["", "@enduml"]
    return envolver("\n".join(linhas))


# ------------------------------------------------------------------------------
# 004 — Integrações
# ------------------------------------------------------------------------------


def arquivo_004(m: dict) -> str:
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Integrações",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Integrações",
            "Troca de dados com outros domínios",
            m["status"],
        ),
        "",
        "skinparam componentStyle rectangle",
        "skinparam packageStyle rectangle",
        "",
        'package "Domínio de Origem" {',
        f'  component "{m["codigo"]}\\n{m["nome"]}" as ORIGEM',
        "}",
        "",
    ]
    if m["correlatos"]:
        linhas += ['package "Domínios Destino" {']
        for sigla, nome in m["correlatos"]:
            linhas.append(f'  component "{sigla}\\n{nome}" as D{sigla[4:]}')
        linhas += ["}", ""]

    linhas += ['package "Serviços Transversais" {']
    for sigla, rotulo, alias in transversais(m, incluir_int=True):
        linhas.append(f'  component "{sigla}\\n{rotulo}" as {alias}')
    linhas.append('  component "Auditoria" as AUD')
    linhas += [
        "}",
        "",
        'database "PostgreSQL" as DB',
        "",
    ]
    rotulo = "dados do domínio" if m["implementado"] else "dados do domínio (prevista)"
    for sigla, _ in m["correlatos"]:
        linhas.append(f"ORIGEM --> D{sigla[4:]} : {rotulo}")
    rotulos_transversais = {
        "IDN": "autenticação",
        "GDO": "anexos e documentos",
        "MET": "metadados",
        "INT": "troca de dados",
    }
    disponiveis = {alias for _, _, alias in transversais(m, incluir_int=True)}
    for alias in ("IDN", "GDO", "MET", "INT"):
        if alias in disponiveis:
            linhas.append(f"ORIGEM --> {alias} : {rotulos_transversais[alias]}")
    linhas += [
        "ORIGEM --> AUD : trilha de auditoria",
        "ORIGEM --> DB : persistência própria",
        "",
    ]
    if m["implementado"]:
        nota_origem = (
            f"note right of ORIGEM\n"
            f"{m['codigo']} como origem da integração.\n\n"
            f"Publica em {m['prefixo']}.\n"
            f"{m['operacoes']} operações disponíveis.\n\n"
            f"Entidade central: {m['central']}.\n"
            f"end note"
        )
    else:
        nota_origem = (
            f"note right of ORIGEM\n"
            f"{m['codigo']} como origem da integração.\n\n"
            f"Modelo proposto: o domínio não possui\n"
            f"módulo implementado (matriz 031).\n\n"
            f"Contratos previstos em {m['prefixo']}.\n"
            f"Entidade central: {m['central']}.\n"
            f"end note"
        )
    linhas += [
        nota_origem,
        "",
        "note bottom of AUD",
        "Todo evento com efeito no orçamento\n"
        "ou no patrimônio é registrado com\n"
        "autor, data e valor antes e depois.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


# ------------------------------------------------------------------------------
# 005 — Persistência
# ------------------------------------------------------------------------------


def arquivo_005(m: dict) -> str:
    linhas = [
        "@startuml",
        f"title {m['codigo']} — Persistência",
        "",
        legenda(
            m["codigo"],
            m["nome"],
            "Persistência",
            "Tabelas e colunas",
            m["status"],
        ),
        "",
        "hide methods",
        "hide stereotypes",
        "skinparam classAttributeIconSize 0",
        "",
        f'package "PostgreSQL — schema {m["schema"]}" {{',
        "",
    ]
    for tabela in m["tabelas"]:
        linhas.append(f'  entity "{tabela["tabela"]}" as T{tabela["tabela"]} {{')
        for coluna in tabela["colunas"]:
            linhas.append(f"    {coluna_sql(coluna)}")
        linhas.append("  }")
        linhas.append("")
    linhas.append("}")

    linhas += [
        "",
        "' =================================================",
        "' RELACIONAMENTOS",
        "' =================================================",
        "",
    ]
    if not m["implementado"]:
        for pai, filho, coluna in m["relacoes"]:
            tabela_pai = m["tabela_de_classe"][pai]
            tabela_filho = m["tabela_de_classe"][filho]
            linhas.append(f'{tabela_pai} ||--o{{ {tabela_filho} : "{coluna}"')
        linhas.append("")

    rotulo_colunas = "colunas mapeadas" if m["implementado"] else "colunas propostas"
    for tabela in m["tabelas"]:
        linhas += [
            f"note right of T{tabela['tabela']}",
            tabela["classe"],
            "",
            f"{len(tabela['colunas'])} {rotulo_colunas}.",
        ]
        if tabela["doc"]:
            linhas += ["", tabela["doc"]]
        linhas += ["end note", ""]

    rotulo_tabelas = "tabelas" if m["implementado"] else "tabelas propostas"
    linhas += [
        f"note left of T{m['tabelas'][0]['tabela']}",
        f"{len(m['tabelas'])} {rotulo_tabelas} no schema {m['schema']}.",
        "",
        "Colunas de auditoria (created_at, updated_at,",
        "created_by, is_deleted) seguem o padrão corporativo.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


# ==============================================================================
# CONFIGURAÇÃO — DOMÍNIOS IMPLEMENTADOS
# ==============================================================================

IMPLEMENTADOS = {
    "DOM-CUM": {
        "nome": "Cadastro Único Municipal",
        "modulo": "sigmun_cadastro",
        "prefixo": "/api/v1/cadastro",
        "schema": "core",
        "status": "Em elaboração",
        "central": "Pessoa",
        "correlatos": [("DOM-PES", "Gestão de Pessoas"), ("DOM-IDN", "Identidade e Acesso")],
        "refs": {
            "pessoa": "pessoas",
            "unidade": "unidades_administrativas",
            "unidade_pai": "unidades_administrativas",
        },
        "enum_links": [
            ("Pessoa", "TipoPessoa"),
            ("Pessoa", "CategoriaPessoa"),
            ("Pessoa", "Sexo"),
            ("Endereco", "TipoEndereco"),
            ("Documento", "TipoDocumento"),
            ("Contato", "TipoContato"),
        ],
        "regras_texto": {
            "RN-CUM-001": "a pessoa é física ou jurídica e sua extensão é obrigatória e única.",
            "RN-CUM-002": "o CPF é validado por dígitos verificadores e armazenado sem máscara.",
            "RN-CUM-003": "o CNPJ é validado por dígitos verificadores e armazenado sem máscara.",
            "RN-CUM-004": "o número de documento é único entre pessoas não excluídas.",
            "RN-CUM-005": "há no máximo um endereço principal por pessoa.",
            "RN-CUM-006": "documento e contato principais são únicos no agregado da pessoa.",
            "RN-CUM-007": "a exclusão é lógica e em cascata: pessoa, extensão e dados filhos.",
            "RN-CUM-008": "a hierarquia de unidades administrativas não pode conter ciclos.",
            "RN-CUM-009": "sigla, código IBGE e código SIAFI são únicos entre unidades ativas.",
        },
        "estados": [
            "[*] --> Ativa : registro da pessoa (RN-CUM-001)",
            "Ativa --> Excluida : exclusão lógica (RN-CUM-007)",
            "Excluida --> [*]",
            "state Ativa",
            "state Excluida",
        ],
        "notas_003": [
            "note right of Ativa\n"
            "Não existe coluna de situação no\n"
            "agregado Pessoa: o ciclo de vida é\n"
            "implícito nas operações de negócio e\n"
            "registrado por deleted_at.\n\n"
            "Pessoa física e pessoa jurídica são\n"
            "extensões 1:1 da pessoa (RN-CUM-001).\n"
            "end note",
            "note bottom of Excluida\n"
            "A exclusão atinge a pessoa, a extensão\n"
            "e os filhos (endereços, documentos,\n"
            "contatos), preservando o histórico.\n"
            "end note",
        ],
    },
    "DOM-TEL": {
        "nome": "Gestão Territorial",
        "modulo": "sigmun_territorial",
        "prefixo": "/api/v1/tel",
        "schema": "tel",
        "status": "Vigente",
        "central": "Bairro",
        "correlatos": [
            ("DOM-IMO", "Cadastro Imobiliário"),
            ("DOM-GEO", "Geoinformação Municipal"),
            ("DOM-TRI", "Administração Tributária"),
        ],
        "refs": {"bairro": "bairros", "logradouro": "logradouros"},
        "enum_links": [
            ("Bairro", "TipoBairro"),
            ("Bairro", "SituacaoBairro"),
            ("Logradouro", "TipoLogradouro"),
            ("Logradouro", "SituacaoLogradouro"),
            ("PlantaGenericaValores", "TipoOcupacaoImovel"),
            ("PlantaGenericaValores", "SituacaoPlantaValores"),
            ("Georreferencia", "DatumGeorreferencia"),
            ("Georreferencia", "TipoGeometria"),
        ],
        "regras_texto": None,
        "estados": [
            "[*] --> Rascunho : cadastro da planta (RN-TEL-003)",
            "Rascunho --> Vigente : ativar (RN-TEL-003)",
            "Vigente --> Revogada : revogar com justificativa (RN-TEL-004)",
            "Revogada --> [*]",
            "state Rascunho",
            "state Vigente",
            "state Revogada",
        ],
        "notas_003": [
            "note right of Vigente\n"
            "Divisões territoriais e logradouros\n"
            "circulam entre ativo e inativo.\n\n"
            "A divisão com logradouros ativos não\n"
            "pode ser excluída (RN-TEL-006).\n"
            "end note",
            "note bottom of Revogada\n"
            "Não há retorno a partir de REVOGADA:\n"
            "preserva-se a memória histórica dos\n"
            "valores aplicados a cada exercício.\n"
            "end note",
        ],
    },
    "DOM-IMO": {
        "nome": "Cadastro Imobiliário",
        "modulo": "sigmun_cadastro_imobiliario",
        "prefixo": "/api/v1/imo",
        "schema": "imo",
        "status": "Vigente",
        "central": "Imovel",
        "correlatos": [
            ("DOM-TEL", "Gestão Territorial"),
            ("DOM-GEO", "Geoinformação Municipal"),
        ],
        "refs": {"imovel": "imoveis"},
        "enum_links": [
            ("Imovel", "TipoImovel"),
            ("Imovel", "SituacaoImovel"),
            ("Imovel", "TipoPropriedade"),
            ("ProprietarioImovel", "TipoVinculo"),
            ("AvaliacaoImovel", "SituacaoAvaliacao"),
            ("CaracteristicaImovel", "TipoObra"),
        ],
        "regras_texto": None,
        "estados": [
            "[*] --> Ativo : cadastro do imóvel (RN-IMO-001)",
            "Ativo --> EmObra : início de obra (RN-IMO-004)",
            "Ativo --> Inativo : suspensão de uso (RN-IMO-004)",
            "Inativo --> Ativo : reativação (RN-IMO-004)",
            "EmObra --> Ativo : obra concluída (RN-IMO-004)",
            "Ativo --> Desocupado : ocupação encerrada",
            "Desocupado --> Ativo : nova ocupação",
            "Ativo --> Demolido : demolição registrada",
            "Demolido --> [*]",
            "state Ativo",
            "state EmObra",
            "state Inativo",
            "state Desocupado",
            "state Demolido",
        ],
        "notas_003": [
            "note right of Demolido\n"
            "A alteração de situação é feita por\n"
            "uso dedicado da API e respeita a\n"
            "máquina de estados (RN-IMO-004).\n"
            "end note",
            "note bottom of Ativo\n"
            "A avaliação de valor venal percorre\n"
            "RASCUNHO -> CONCLUIDA | CANCELADA\n"
            "(RN-IMO-005).\n"
            "end note",
        ],
    },
    "DOM-GEO": {
        "nome": "Geoinformação Municipal",
        "modulo": "sigmun_geoinformacao",
        "prefixo": "/api/v1/geo",
        "schema": "geo",
        "status": "Vigente",
        "central": "MapaSig",
        "correlatos": [
            ("DOM-TEL", "Gestão Territorial"),
            ("DOM-TRI", "Administração Tributária"),
        ],
        "refs": {"mapa": "mapas_sig", "camada": "camadas_mapa"},
        "enum_links": [
            ("CamadaMapa", "TipoCamadaMapa"),
            ("CamadaMapa", "FormatoCamada"),
            ("CamadaMapa", "SituacaoCamadaMapa"),
            ("CamadaMapa", "DatumGeografico"),
            ("MapaSig", "TipoMapaSig"),
            ("MapaSig", "SituacaoMapaSig"),
            ("MapaSig", "DatumGeografico"),
            ("FeatureGeo", "TipoGeometria"),
            ("FeatureGeo", "DatumGeografico"),
            ("ServicoGeo", "TipoServicoGeo"),
            ("ServicoGeo", "SituacaoServicoGeo"),
        ],
        "regras_texto": None,
        "estados": [
            "[*] --> MapaRascunho : cadastro do mapa (RN-GEO-002)",
            "MapaRascunho --> MapaPublicado : publicar no geoportal (RN-GEO-004)",
            "MapaPublicado --> MapaArquivado : arquivar (RN-GEO-004)",
            "MapaRascunho --> [*] : exclusão lógica (RN-GEO-004)",
            "MapaArquivado --> [*] : exclusão lógica (RN-GEO-004)",
            "",
            "[*] --> CamadaRascunho : cadastro da camada (RN-GEO-001)",
            "CamadaRascunho --> CamadaAtiva : ativar (RN-GEO-006)",
            "CamadaAtiva --> CamadaDesativada : desativar (RN-GEO-006)",
            "CamadaRascunho --> [*] : exclusão lógica (RN-GEO-006)",
            "state MapaRascunho",
            "state MapaPublicado",
            "state MapaArquivado",
            "state CamadaRascunho",
            "state CamadaAtiva",
            "state CamadaDesativada",
        ],
        "notas_003": [
            "note right of MapaPublicado\n"
            "A composição mapa-camada é exigida\n"
            "para publicar (RN-GEO-004 e RN-GEO-008)\n"
            "e preserva ordem e opacidade.\n"
            "end note",
            "note bottom of CamadaAtiva\n"
            "Serviço geoespacial percorre\n"
            "ATIVO -> INATIVO | MANUTENCAO\n"
            "(RN-GEO-007).\n"
            "end note",
        ],
    },
    "DOM-OBR": {
        "nome": "Obras e Infraestrutura",
        "modulo": "sigmun_obras",
        "prefixo": "/api/v1/obr",
        "schema": "obr",
        "status": "Vigente",
        "central": "Obra",
        "correlatos": [("DOM-TEL", "Gestão Territorial")],
        "refs": {"obra": "obras", "medicao": "medicoes_obras"},
        "enum_links": [
            ("Obra", "TipoObra"),
            ("Obra", "SituacaoObra"),
            ("Obra", "FonteRecurso"),
            ("Obra", "TipoContratacao"),
            ("MedicaoObra", "TipoMedicao"),
            ("MedicaoObra", "SituacaoMedicao"),
            ("EtapaObra", "TipoEtapa"),
            ("EtapaObra", "SituacaoEtapa"),
            ("DespesaObra", "TipoDespesa"),
            ("VistoriaObra", "TipoVistoria"),
            ("VistoriaObra", "ParecerVistoria"),
        ],
        "regras_texto": None,
        "estados": [
            "[*] --> Planejada : cadastro da obra (RN-OBR-001)",
            "Planejada --> EmLicitacao : iniciar contratação",
            "EmLicitacao --> Contratada : contrato formalizado",
            "Contratada --> EmExecucao : iniciar execução (RN-OBR-003)",
            "EmExecucao --> Suspensa : suspender execução (RN-OBR-002)",
            "Suspensa --> EmExecucao : retomar execução",
            "EmExecucao --> Concluida : concluir com avanço físico de 100% (RN-OBR-005)",
            "EmExecucao --> Cancelada : cancelar obra (RN-OBR-002)",
            "Concluida --> [*]",
            "Cancelada --> [*]",
            "state Planejada",
            "state EmLicitacao",
            "state Contratada",
            "state EmExecucao",
            "state Suspensa",
            "state Concluida",
            "state Cancelada",
        ],
        "notas_003": [
            "note right of EmExecucao\n"
            "A medição percorre REGISTRADA ->\n"
            "CONFERIDA -> APROVADA | GLOSADA |\n"
            "CANCELADA (RN-OBR-005).\n\n"
            "A etapa percorre PENDENTE ->\n"
            "EM_EXECUCAO -> CONCLUIDA |\n"
            "ATRASADA | CANCELADA (RN-OBR-007).\n"
            "end note",
            "note bottom of Concluida\n"
            "O percentual físico é recomposto a\n"
            "partir das medições aprovadas; o\n"
            "financeiro, a partir das despesas.\n"
            "end note",
        ],
    },
    "DOM-DIA": {
        "nome": "Diárias e Viagens",
        "modulo": "sigmun_dia",
        "prefixo": "/api/v1/dia",
        "schema": "dia",
        "status": "Vigente",
        "central": "Diaria",
        "correlatos": [("DOM-PES", "Gestão de Pessoas")],
        "refs": {
            "viagem": "viagens",
            "diaria": "diarias",
            "prestacao": "prestacoes_contas",
        },
        "enum_links": [
            ("Diaria", "StatusDiaria"),
            ("Diaria", "CategoriaDiaria"),
        ],
        "regras_texto": {
            "RN-DIA-001": "solicitação inicial da diária.",
            "RN-DIA-002": "autorização da diária com o valor autorizado.",
            "RN-DIA-003": "cálculo do valor total da diária.",
            "RN-DIA-004": "autorização da diária.",
            "RN-DIA-005": "cálculo do valor da diária.",
            "RN-DIA-006": "confirmação da concessão da diária.",
            "RN-DIA-007": "início do período de prestação de contas.",
            "RN-DIA-008": "registro do pagamento e reversão para pagamento.",
            "RN-DIA-009": "a prestação de contas exige documento anexado no DOM-GDO.",
            "RN-DIA-011": "aprovação da prestação de contas.",
            "RN-DIA-012": "glosa da prestação de contas.",
            "RN-DIA-013": "restituição do valor glosado.",
            "RN-DIA-015": "aprovação exige diária paga e prestação de contas aberta.",
            "RN-DIA-016": "glosa exige diária paga, prestação aberta, motivo e valor.",
            "RN-DIA-017": "restituição exige diária paga e prestação de contas glosada.",
        },
        "estados": [
            "[*] --> Solicitada : solicitar diária (RN-DIA-001)",
            "Solicitada --> Autorizada : autorizar diária (RN-DIA-004)",
            "Autorizada --> Calculada : calcular valor (RN-DIA-005)",
            "Calculada --> Concedida : confirmar concessão (RN-DIA-006)",
            "Concedida --> EmPrestacao : iniciar prestação de contas (RN-DIA-007)",
            "EmPrestacao --> Paga : registrar pagamento (RN-DIA-008)",
            "Paga --> Concedida : reverter para pagamento (RN-DIA-008)",
            "Paga --> Aprovada : aprovar prestação de contas (RN-DIA-015)",
            "Paga --> Glosa : glosar prestação de contas (RN-DIA-016)",
            "Glosa --> Restituida : restituir valor glosado (RN-DIA-017)",
            "Solicitada --> Cancelada : cancelar diária",
            "Concedida --> Cancelada : cancelar diária",
            "Aprovada --> [*]",
            "Restituida --> [*]",
            "Cancelada --> [*]",
            "state Solicitada",
            "state Autorizada",
            "state Calculada",
            "state Concedida",
            "state EmPrestacao",
            "state Paga",
            "state Aprovada",
            "state Glosa",
            "state Restituida",
            "state Cancelada",
        ],
        "notas_003": [
            "note right of Paga\n"
            "A prestação de contas exige documento\n"
            "anexado no DOM-GDO (RN-DIA-009) e cada\n"
            "transição é gravada em dia.eventos_diarias,\n"
            "preservando o histórico de status.\n"
            "end note",
            "note bottom of Glosa\n"
            "A restituição exige diária paga e\n"
            "prestação glosada (RN-DIA-017).\n\n"
            "TipoDeslocamento existe na entidade\n"
            "Viagem e não é persistido (ver 005).\n"
            "end note",
        ],
    },
}


# ==============================================================================
# MONTAGEM DO MODELO — DOMÍNIOS IMPLEMENTADOS
# ==============================================================================


def montar_implementado(codigo: str, cfg: dict) -> dict:
    """Deriva do código o modelo normalizado usado pelos emissores."""
    nome = cfg["nome"]
    bruto = extrair_tabelas(cfg["modulo"])
    uso = extrair_use_cases(cfg["modulo"])
    operacoes, _ = extrair_operacoes(cfg["prefixo"])

    tabelas = []
    entidades = []
    tabela_de_classe: dict[str, str] = {}
    for tabela in sorted(bruto):
        info = bruto[tabela]
        classe = info["classe"].removesuffix("Model")
        tabela_de_classe[classe] = tabela
        tabelas.append(
            {
                "tabela": tabela,
                "classe": info["classe"],
                "colunas": info["colunas"],
                "doc": info["doc"],
            }
        )
        entidades.append(
            {
                "classe": classe,
                "atributos": [(c["nome"], tipo_dominio(c["tipo"])) for c in info["colunas"]],
            }
        )

    relacoes: list[tuple[str, str, str]] = []
    for tabela in sorted(bruto):
        filho = bruto[tabela]["classe"].removesuffix("Model")
        for coluna in bruto[tabela]["colunas"]:
            nome_coluna = coluna["nome"]
            if not nome_coluna.endswith("_id"):
                continue
            destino = cfg["refs"].get(nome_coluna[:-3])
            if destino not in bruto:
                continue
            pai = bruto[destino]["classe"].removesuffix("Model")
            relacoes.append((pai, filho, nome_coluna))

    ids = extrair_regras(cfg["modulo"], codigo.split("-")[1])
    if cfg.get("regras_texto"):
        regras = [(i, cfg["regras_texto"][i]) for i in ids if i in cfg["regras_texto"]]
    else:
        texto = dict(regras_documentadas(codigo.split("-")[1]))
        regras = [(i, texto.get(i, "")) for i in ids]

    return {
        "codigo": codigo,
        "nome": nome,
        "schema": cfg["schema"],
        "prefixo": cfg["prefixo"],
        "status": cfg["status"],
        "implementado": True,
        "central": cfg["central"],
        "correlatos": cfg["correlatos"],
        "capacidades": uso,
        "use_cases": uso,
        "operacoes": operacoes,
        "regras": regras,
        "tabelas": tabelas,
        "tabela_de_classe": tabela_de_classe,
        "entidades": entidades,
        "enums": extrair_enums(cfg["modulo"]),
        "enum_links": [
            (c, e) for c, e in cfg["enum_links"] if any(ent["classe"] == c for ent in entidades)
        ],
        "relacoes": relacoes,
        "estados": cfg["estados"],
        "notas_003": cfg["notas_003"],
        "processos": [],
    }


# ==============================================================================
# CONFIGURAÇÃO — DOMÍNIOS PROPOSTOS (sem módulo implementado)
# ==============================================================================


def entidade(
    classe: str, tabela: str, doc: str, atributos: list[str], auditoria: bool = True
) -> dict:
    """Monta entidade e tabela a partir de `nome:tipoDeDomínio:TIPO_SQL[:flags]`."""
    colunas = [{"nome": "id", "tipo": "UUID", "flags": ["PK"]}]
    lista: list[tuple[str, str]] = [("id", "string")]
    for item in atributos:
        partes = item.split(":")
        nome, tdom, tsql = partes[0], partes[1], partes[2]
        colunas.append(
            {
                "nome": nome,
                "tipo": tsql,
                "flags": partes[3].split(",") if len(partes) > 3 else [],
            }
        )
        lista.append((nome, tdom))
    if auditoria:
        colunas += [
            {"nome": "created_at", "tipo": "TIMESTAMPTZ", "flags": ["NN"]},
            {"nome": "updated_at", "tipo": "TIMESTAMPTZ", "flags": []},
            {"nome": "created_by", "tipo": "TEXT", "flags": []},
            {"nome": "is_deleted", "tipo": "BOOLEAN", "flags": ["NN"]},
        ]
        lista += [
            ("created_at", "datetime"),
            ("updated_at", "datetime"),
            ("created_by", "string"),
            ("is_deleted", "bool"),
        ]
    return {
        "classe": classe,
        "tabela": tabela,
        "doc": doc,
        "colunas": colunas,
        "atributos": lista,
    }


PROPOSTOS = [
    {
        "codigo": "DOM-GOV",
        "nome": "Governança Municipal",
        "schema": "gov",
        "prefixo": "/api/v1/gov",
        "status": "Em elaboração",
        "central": "PoliticaGovernanca",
        "correlatos": [
            ("DOM-PLA", "Planejamento Governamental"),
            ("DOM-IND", "Indicadores e Desempenho"),
            ("DOM-DAD", "Dados Corporativos"),
        ],
        "capacidades": [
            "Governança Corporativa",
            "Gestão de Políticas",
            "Gestão de Riscos",
            "Compliance",
            "Governança Digital",
        ],
        "processos": [
            "Elaborar a política",
            "Submeter à revisão",
            "Aprovar e publicar",
            "Identificar e tratar riscos",
            "Executar os controles de conformidade",
            "Registrar a deliberação do colegiado",
            "Monitorar indicadores de governança",
            "Revisar ou revogar a política",
        ],
        "regras": [
            (
                "RN-GOV-001",
                "toda política declara escopo, responsável, vigência e situação.",
            ),
            (
                "RN-GOV-002",
                "todo risco tem dono, classificação de probabilidade e impacto.",
            ),
            (
                "RN-GOV-003",
                "o controle de conformidade registra a evidência e o resultado da verificação.",
            ),
            (
                "RN-GOV-004",
                "a deliberação vincula-se à política, risco ou controle e guarda histórico.",
            ),
        ],
        "enums": {
            "TipoPolitica": [
                ("POLITICA", '"politica"'),
                ("DIRETRIZ", '"diretriz"'),
                ("NORMA", '"norma"'),
                ("PROCEDIMENTO", '"procedimento"'),
            ],
            "NivelRisco": [
                ("BAIXO", '"baixo"'),
                ("MEDIO", '"medio"'),
                ("ALTO", '"alto"'),
                ("CRITICO", '"critico"'),
            ],
            "SituacaoGovernanca": [
                ("RASCUNHO", '"rascunho"'),
                ("EM_REVISAO", '"em_revisao"'),
                ("VIGENTE", '"vigente"'),
                ("REVOGADA", '"revogada"'),
            ],
        },
        "enum_links": [
            ("PoliticaGovernanca", "TipoPolitica"),
            ("PoliticaGovernanca", "SituacaoGovernanca"),
            ("RiscoGovernanca", "NivelRisco"),
            ("ControleCompliance", "SituacaoGovernanca"),
        ],
        "entidades": [
            entidade(
                "PoliticaGovernanca",
                "politicas_governanca",
                "Política, diretriz, norma ou procedimento de governança.",
                [
                    "codigo:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "escopo:texto:TEXT",
                    "responsavel:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                    "vigencia_inicio:date:DATE:NN",
                    "vigencia_fim:date:DATE",
                ],
            ),
            entidade(
                "RiscoGovernanca",
                "riscos_governanca",
                "Risco corporativo com dono, classificação e tratamento.",
                [
                    "codigo:string:TEXT:NN",
                    "descricao:texto:TEXT:NN",
                    "categoria:string:TEXT:NN",
                    "probabilidade:string:TEXT:NN",
                    "impacto:string:TEXT:NN",
                    "nivel:string:TEXT:NN",
                    "dono:string:TEXT:NN",
                    "tratamento:texto:TEXT",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "ControleCompliance",
                "controles_compliance",
                "Controle de conformidade com evidência e resultado.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "periodicidade:string:TEXT:NN",
                    "responsavel:string:TEXT:NN",
                    "evidencia:texto:TEXT",
                    "resultado:string:TEXT",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "DeliberacaoGoverno",
                "deliberacoes",
                "Deliberação de colegiado vinculada a política, risco ou controle.",
                [
                    "numero:string:TEXT:NN",
                    "data:date:DATE:NN",
                    "orgao:string:TEXT:NN",
                    "ementa:texto:TEXT:NN",
                    "vinculo:string:TEXT:NN",
                    "referencia_id:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
        ],
        "relacoes": [
            ("PoliticaGovernanca", "DeliberacaoGoverno", "referencia_id"),
            ("RiscoGovernanca", "DeliberacaoGoverno", "referencia_id"),
            ("ControleCompliance", "DeliberacaoGoverno", "referencia_id"),
        ],
        "estados": [
            "[*] --> Rascunho : elaboração da política",
            "Rascunho --> EmRevisao : submeter à revisão",
            "EmRevisao --> Vigente : aprovar e publicar",
            "EmRevisao --> Rascunho : devolver com ressalvas",
            "Vigente --> EmRevisao : programa de revisão",
            "Vigente --> Revogada : revogação formal",
            "Revogada --> [*]",
            "state Rascunho",
            "state EmRevisao",
            "state Vigente",
            "state Revogada",
        ],
        "notas_003": [
            "note right of Vigente\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "Riscos e controles acompanham a\n"
            "política a que se referem.\n"
            "end note",
            "note bottom of Revogada\n"
            "A revogação preserva o histórico;\n"
            "nenhuma política é apagada fisicamente.\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-PLA",
        "nome": "Planejamento Governamental",
        "schema": "pla",
        "prefixo": "/api/v1/pla",
        "status": "Em elaboração",
        "central": "Projeto",
        "correlatos": [
            ("DOM-ORC", "Orçamento Público"),
            ("DOM-IND", "Indicadores e Desempenho"),
            ("DOM-GOV", "Governança Municipal"),
        ],
        "capacidades": [
            "Planejamento Estratégico",
            "Gestão de Programas",
            "Gestão de Projetos",
            "Metas e Indicadores",
            "Acompanhamento de Resultados",
        ],
        "processos": [
            "Elaborar o plano estratégico",
            "Aprovar o plano",
            "Estruturar os programas",
            "Definir projetos e responsáveis",
            "Fixar metas e prazos",
            "Acompanhar a execução",
            "Avaliar resultados",
            "Encerrar ou replanejar",
        ],
        "regras": [
            (
                "RN-PLA-001",
                "programa pertence a um plano estratégico e projeto pertence a um programa.",
            ),
            ("RN-PLA-002", "meta declara indicador de referência, valor base, valor alvo e prazo."),
            (
                "RN-PLA-003",
                "projeto concluído exige encerramento formal com o resultado registrado.",
            ),
            (
                "RN-PLA-004",
                "resultados vão ao DOM-IND como valores, sem duplicar o indicador.",
            ),
        ],
        "enums": {
            "SituacaoPlanejamento": [
                ("RASCUNHO", '"rascunho"'),
                ("EM_APROVACAO", '"em_aprovacao"'),
                ("APROVADO", '"aprovado"'),
                ("EM_EXECUCAO", '"em_execucao"'),
                ("SUSPENSO", '"suspenso"'),
                ("CONCLUIDO", '"concluido"'),
                ("CANCELADO", '"cancelado"'),
            ],
            "TipoMeta": [
                ("PERCENTUAL", '"percentual"'),
                ("VALOR", '"valor"'),
                ("QUANTIDADE", '"quantidade"'),
            ],
        },
        "enum_links": [
            ("PlanoEstrategico", "SituacaoPlanejamento"),
            ("Programa", "SituacaoPlanejamento"),
            ("Projeto", "SituacaoPlanejamento"),
            ("Meta", "TipoMeta"),
            ("Meta", "SituacaoPlanejamento"),
        ],
        "entidades": [
            entidade(
                "PlanoEstrategico",
                "planos_estrategicos",
                "Plano estratégico do município no exercício.",
                [
                    "codigo:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "exercicio_inicio:int:INTEGER:NN",
                    "exercicio_fim:int:INTEGER:NN",
                    "visao:texto:TEXT",
                    "missao:texto:TEXT",
                    "situacao:string:TEXT:NN",
                    "data_aprovacao:date:DATE",
                ],
            ),
            entidade(
                "Programa",
                "programas",
                "Programa de governo vinculado a um plano estratégico.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "plano_id:string:TEXT:NN",
                    "objetivo:texto:TEXT:NN",
                    "valor_previsto:decimal:FLOAT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "Projeto",
                "projetos",
                "Projeto de execução vinculado a um programa.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "programa_id:string:TEXT:NN",
                    "responsavel:string:TEXT:NN",
                    "data_inicio:date:DATE",
                    "data_fim_prevista:date:DATE",
                    "custo_previsto:decimal:FLOAT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "Meta",
                "metas",
                "Meta de programa com valor base, alvo e prazo.",
                [
                    "codigo:string:TEXT:NN",
                    "descricao:texto:TEXT:NN",
                    "programa_id:string:TEXT:NN",
                    "indicador_ref:string:TEXT",
                    "valor_base:decimal:FLOAT",
                    "valor_alvo:decimal:FLOAT:NN",
                    "prazo:date:DATE:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
        ],
        "relacoes": [
            ("PlanoEstrategico", "Programa", "plano_id"),
            ("Programa", "Projeto", "programa_id"),
            ("Programa", "Meta", "programa_id"),
        ],
        "estados": [
            "[*] --> Planejado : projeto aprovado",
            "Planejado --> EmExecucao : iniciar execução",
            "EmExecucao --> Suspenso : suspender execução",
            "Suspenso --> EmExecucao : retomar execução",
            "EmExecucao --> Concluido : encerramento formal (RN-PLA-003)",
            "EmExecucao --> Cancelado : cancelar projeto",
            "Concluido --> [*]",
            "Cancelado --> [*]",
            "state Planejado",
            "state EmExecucao",
            "state Suspenso",
            "state Concluido",
            "state Cancelado",
        ],
        "notas_003": [
            "note right of EmExecucao\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "Plano, programas e metas percorrem\n"
            "RASCUNHO -> EM_APROVACAO -> APROVADO\n"
            "-> EM_EXECUCAO -> CONCLUIDO.\n"
            "end note",
            "note bottom of Concluido\n"
            "O resultado é convertido em valor de\n"
            "indicador para o DOM-IND (RN-PLA-004)\n"
            "e em execução orçamentária para o\n"
            "DOM-ORC.\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-CPT",
        "nome": "Gestão de Competências",
        "schema": "cpt",
        "prefixo": "/api/v1/cpt",
        "status": "Em elaboração",
        "central": "Competencia",
        "correlatos": [
            ("DOM-PES", "Gestão de Pessoas"),
            ("DOM-IND", "Indicadores e Desempenho"),
        ],
        "capacidades": [
            "Catálogo de Competências",
            "Avaliação de Lacunas",
            "Planos de Desenvolvimento",
            "Capacitações",
            "Qualificações",
        ],
        "processos": [
            "Mapear as competências do município",
            "Avaliar o nível atual do servidor",
            "Identificar as lacunas",
            "Definir o plano de desenvolvimento",
            "Ofertar a capacitação",
            "Gerenciar as inscrições",
            "Executar e avaliar a capacitação",
            "Registrar o resultado",
        ],
        "regras": [
            (
                "RN-CPT-001",
                "lacuna é a diferença entre o nível esperado e o nível avaliado da competência.",
            ),
            (
                "RN-CPT-002",
                "capacitação só recebe inscrição com inscrições abertas e vaga disponível.",
            ),
            (
                "RN-CPT-003",
                "a pessoa é referenciada por identificador opaco do DOM-PES.",
            ),
            (
                "RN-CPT-004",
                "a conclusão registra resultado e pode atualizar a avaliação da competência.",
            ),
        ],
        "enums": {
            "CategoriaCompetencia": [
                ("TECNICA", '"tecnica"'),
                ("COMPORTAMENTAL", '"comportamental"'),
                ("GERENCIAL", '"gerencial"'),
            ],
            "ModalidadeCapacitacao": [
                ("PRESENCIAL", '"presencial"'),
                ("EAD", '"ead"'),
                ("BLENDED", '"blended"'),
                ("MENTORIA", '"mentoria"'),
            ],
            "SituacaoCapacitacao": [
                ("PLANEJADA", '"planejada"'),
                ("INSCRICOES_ABERTAS", '"inscricoes_abertas"'),
                ("EM_ANDAMENTO", '"em_andamento"'),
                ("CONCLUIDA", '"concluida"'),
                ("CANCELADA", '"cancelada"'),
            ],
        },
        "enum_links": [
            ("Competencia", "CategoriaCompetencia"),
            ("Capacitacao", "ModalidadeCapacitacao"),
            ("Capacitacao", "SituacaoCapacitacao"),
            ("PlanoDesenvolvimento", "SituacaoCapacitacao"),
        ],
        "entidades": [
            entidade(
                "Competencia",
                "competencias",
                "Competência, habilidade ou qualificação do catálogo.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "categoria:string:TEXT:NN",
                    "nivel_referencia:decimal:FLOAT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "Capacitacao",
                "capacitacoes",
                "Capacitação ou treinamento ofertado.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "modalidade:string:TEXT:NN",
                    "carga_horativa:int:INTEGER:NN",
                    "situacao:string:TEXT:NN",
                    "data_inicio:date:DATE",
                    "data_fim:date:DATE",
                ],
            ),
            entidade(
                "AvaliacaoCompetencia",
                "avaliacoes_competencia",
                "Nível avaliado e esperado de uma pessoa em uma competência.",
                [
                    "pessoa_id:string:TEXT:NN",
                    "competencia_id:string:TEXT:NN",
                    "nivel_atual:decimal:FLOAT:NN",
                    "nivel_esperado:decimal:FLOAT:NN",
                    "avaliador:string:TEXT:NN",
                    "data_avaliacao:date:DATE:NN",
                    "observacao:texto:TEXT",
                ],
            ),
            entidade(
                "PlanoDesenvolvimento",
                "planos_desenvolvimento",
                "Ação individual para reduzir uma lacuna de competência.",
                [
                    "pessoa_id:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "competencia_id:string:TEXT:NN",
                    "capacitacao_id:string:TEXT",
                    "acao:string:TEXT:NN",
                    "prazo:date:DATE:NN",
                    "situacao:string:TEXT:NN",
                    "resultado:string:TEXT",
                ],
            ),
        ],
        "relacoes": [
            ("Competencia", "AvaliacaoCompetencia", "competencia_id"),
            ("Competencia", "PlanoDesenvolvimento", "competencia_id"),
            ("Capacitacao", "PlanoDesenvolvimento", "capacitacao_id"),
        ],
        "estados": [
            "[*] --> Planejada : programação da capacitação",
            "Planejada --> InscricoesAbertas : abrir inscrições (RN-CPT-002)",
            "InscricoesAbertas --> EmAndamento : encerrar inscrições e iniciar",
            "EmAndamento --> Concluida : avaliação aplicada (RN-CPT-004)",
            "Planejada --> Cancelada : cancelar oferta",
            "InscricoesAbertas --> Cancelada : cancelar oferta",
            "EmAndamento --> Cancelada : cancelar oferta",
            "Concluida --> [*]",
            "Cancelada --> [*]",
            "state Planejada",
            "state InscricoesAbertas",
            "state EmAndamento",
            "state Concluida",
            "state Cancelada",
        ],
        "notas_003": [
            "note right of EmAndamento\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "A pessoa participante é referenciada\n"
            "por identificador do DOM-PES (RN-CPT-003).\n"
            "end note",
            "note bottom of Concluida\n"
            "O resultado atualiza o nível avaliado\n"
            "da competência e alimenta o plano de\n"
            "desenvolvimento (RN-CPT-004).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-MAM",
        "nome": "Meio Ambiente",
        "schema": "mam",
        "prefixo": "/api/v1/mam",
        "status": "Em elaboração",
        "central": "LicenciamentoAmbiental",
        "correlatos": [
            ("DOM-TEL", "Gestão Territorial"),
            ("DOM-GEO", "Geoinformação Municipal"),
            ("DOM-MOB", "Mobilidade e Serviços de Campo"),
        ],
        "capacidades": [
            "Licenciamento Ambiental",
            "Fiscalização",
            "Resíduos Sólidos",
            "Recursos Naturais",
            "Áreas Protegidas",
            "Monitoramento Ambiental",
        ],
        "processos": [
            "Requerer a licença",
            "Analisar a documentação",
            "Emitir a licença com condições",
            "Operar sob monitoramento",
            "Fiscalizar a atividade",
            "Aplicar a providência",
            "Adequar no prazo assinalado",
            "Renovar, suspender ou revogar",
        ],
        "regras": [
            (
                "RN-MAM-001",
                "a licença tem validade e condições; vencida, ela não autoriza a atividade.",
            ),
            ("RN-MAM-002", "resultado não conforme gera prazo de adequação e nova vistoria."),
            (
                "RN-MAM-003",
                "o monitoramento compara o valor medido com o limite legal.",
            ),
            (
                "RN-MAM-004",
                "a referência territorial vem do DOM-TEL ou DOM-GEO, sem cópia.",
            ),
        ],
        "enums": {
            "TipoLicenciamento": [
                ("LICENCA", '"licenca"'),
                ("AUTORIZACAO", '"autorizacao"'),
                ("OUTORGA", '"outorga"'),
                ("APROVACAO", '"aprovacao"'),
            ],
            "SituacaoLicenciamento": [
                ("SOLICITADO", '"solicitado"'),
                ("EM_ANALISE", '"em_analise"'),
                ("LICENCIADO", '"licenciado"'),
                ("NEGADO", '"negado"'),
                ("SUSPENSO", '"suspenso"'),
                ("REVOGADO", '"revogado"'),
            ],
            "ResultadoFiscalizacao": [
                ("CONFORME", '"conforme"'),
                ("NAO_CONFORME", '"nao_conforme"'),
                ("PENDENTE", '"pendente"'),
            ],
        },
        "enum_links": [
            ("LicenciamentoAmbiental", "TipoLicenciamento"),
            ("LicenciamentoAmbiental", "SituacaoLicenciamento"),
            ("FiscalizacaoAmbiental", "ResultadoFiscalizacao"),
        ],
        "entidades": [
            entidade(
                "LicenciamentoAmbiental",
                "licencimentos_ambientais",
                "Licença, autorização ou outorga da atividade ambiental.",
                [
                    "numero:string:TEXT:NN",
                    "empreendimento:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "atividade:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                    "data_emissao:date:DATE",
                    "validade_ate:date:DATE",
                    "condicoes:texto:TEXT",
                ],
            ),
            entidade(
                "FiscalizacaoAmbiental",
                "fiscalizacoes_ambientais",
                "Auto de fiscalização com resultado e prazo de adequação.",
                [
                    "numero:string:TEXT:NN",
                    "licenca_id:string:TEXT",
                    "data:date:DATE:NN",
                    "agente:string:TEXT:NN",
                    "objeto:string:TEXT:NN",
                    "resultado:string:TEXT:NN",
                    "prazo_adequacao:date:DATE",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "MonitoramentoAmbiental",
                "monitoramentos_ambientais",
                "Medição de parâmetro ambiental comparada ao limite legal.",
                [
                    "licenca_id:string:TEXT",
                    "parametro:string:TEXT:NN",
                    "data:date:DATE:NN",
                    "valor:decimal:FLOAT:NN",
                    "unidade:string:TEXT:NN",
                    "limite_legal:decimal:FLOAT",
                    "conformidade:string:TEXT:NN",
                    "observacao:texto:TEXT",
                ],
            ),
            entidade(
                "AreaProtegida",
                "areas_protegidas",
                "Unidade ou área protegida do município.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "categoria:string:TEXT:NN",
                    "area_km2:decimal:FLOAT:NN",
                    "nivel_protecao:string:TEXT:NN",
                    "bairro_id:string:TEXT",
                    "situacao:string:TEXT:NN",
                ],
            ),
        ],
        "relacoes": [
            ("LicenciamentoAmbiental", "FiscalizacaoAmbiental", "licenca_id"),
            ("LicenciamentoAmbiental", "MonitoramentoAmbiental", "licenca_id"),
        ],
        "estados": [
            "[*] --> Solicitado : protocolo do requerimento",
            "Solicitado --> EmAnalise : análise documental",
            "EmAnalise --> Licenciado : emitir a licença (RN-MAM-001)",
            "EmAnalise --> Negado : exigência não atendida",
            "Licenciado --> Suspenso : suspensão por infração (RN-MAM-002)",
            "Suspenso --> Licenciado : regularização comprovada",
            "Licenciado --> Revogado : revogação formal",
            "Negado --> [*]",
            "Revogado --> [*]",
            "state Solicitado",
            "state EmAnalise",
            "state Licenciado",
            "state Negado",
            "state Suspenso",
            "state Revogado",
        ],
        "notas_003": [
            "note right of EmAnalise\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "A atividade é localizada por\n"
            "identificador do DOM-TEL ou DOM-GEO\n"
            "(RN-MAM-004).\n"
            "end note",
            "note bottom of Licenciado\n"
            "A licença declara validade e condições\n"
            "(RN-MAM-001). A fiscalização pode gerar\n"
            "prazo de adequação (RN-MAM-002) e o\n"
            "monitoramento registra a conformidade\n"
            "(RN-MAM-003).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-DEC",
        "nome": "Desenvolvimento Econômico",
        "schema": "dec",
        "prefixo": "/api/v1/dec",
        "status": "Em elaboração",
        "central": "ProgramaDesenvolvimento",
        "correlatos": [
            ("DOM-CUM", "Cadastro Único Municipal"),
            ("DOM-IND", "Indicadores e Desempenho"),
        ],
        "capacidades": [
            "Programas de Desenvolvimento",
            "Empreendimentos",
            "Projetos de Investimento",
            "Emprego e Renda",
            "Economia Local",
        ],
        "processos": [
            "Propor o programa de desenvolvimento",
            "Aprovar e publicar o programa",
            "Cadastrar o empreendimento",
            "Avaliar a adesão ao programa",
            "Registrar o projeto de investimento",
            "Acompanhar investimento e empregos",
            "Aferir os resultados",
            "Encerrar ou renovar o programa",
        ],
        "regras": [
            (
                "RN-DEC-001",
                "o empreendimento referencia a pessoa jurídica do DOM-CUM por identificador opaco.",
            ),
            ("RN-DEC-002", "a adesão ao programa exige programa em execução e vaga disponível."),
            (
                "RN-DEC-003",
                "o projeto registra investimento e empregos previstos e realizados.",
            ),
            (
                "RN-DEC-004",
                "os resultados são repassados ao DOM-IND como valores de indicador econômico.",
            ),
        ],
        "enums": {
            "SetorEconomico": [
                ("AGROPECUARIA", '"agropecuaria"'),
                ("INDUSTRIA", '"industria"'),
                ("SERVICOS", '"servicos"'),
                ("COMERCIO", '"comercio"'),
            ],
            "PorteEmpresa": [
                ("ME", '"me"'),
                ("EPP", '"epp"'),
                ("DEMAIS", '"demais"'),
            ],
            "SituacaoPrograma": [
                ("PROPOSTO", '"proposto"'),
                ("APROVADO", '"aprovado"'),
                ("EM_EXECUCAO", '"em_execucao"'),
                ("CONCLUIDO", '"concluido"'),
                ("CANCELADO", '"cancelado"'),
            ],
        },
        "enum_links": [
            ("Empreendimento", "SetorEconomico"),
            ("Empreendimento", "PorteEmpresa"),
            ("ProgramaDesenvolvimento", "SituacaoPrograma"),
            ("ProjetoInvestimento", "SituacaoPrograma"),
        ],
        "entidades": [
            entidade(
                "ProgramaDesenvolvimento",
                "programas_desenvolvimento",
                "Programa municipal de fomento e desenvolvimento.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "objetivo:texto:TEXT:NN",
                    "publico:texto:TEXT",
                    "orcamento:decimal:FLOAT:NN",
                    "situacao:string:TEXT:NN",
                    "data_inicio:date:DATE",
                    "data_fim:date:DATE",
                ],
            ),
            entidade(
                "Empreendimento",
                "empreendimentos",
                "Empreendimento local vinculado a pessoa jurídica do DOM-CUM.",
                [
                    "codigo:string:TEXT:NN",
                    "pessoa_id:string:TEXT",
                    "nome:string:TEXT:NN",
                    "setor:string:TEXT:NN",
                    "porte:string:TEXT:NN",
                    "bairro_id:string:TEXT",
                    "data_abertura:date:DATE",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "ProjetoInvestimento",
                "projetos_investimento",
                "Investimento previsto e realizado com geração de empregos.",
                [
                    "codigo:string:TEXT:NN",
                    "empreendimento_id:string:TEXT:NN",
                    "descricao:texto:TEXT:NN",
                    "investimento_previsto:decimal:FLOAT:NN",
                    "empregos_previstos:int:INTEGER:NN",
                    "empregos_realizados:int:INTEGER",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "ParticipacaoPrograma",
                "participacoes_programa",
                "Adesão de empreendimento a um programa em execução.",
                [
                    "programa_id:string:TEXT:NN",
                    "empreendimento_id:string:TEXT:NN",
                    "data_ingresso:date:DATE:NN",
                    "situacao:string:TEXT:NN",
                    "resultado:texto:TEXT",
                ],
            ),
        ],
        "relacoes": [
            ("ProgramaDesenvolvimento", "ParticipacaoPrograma", "programa_id"),
            ("Empreendimento", "ParticipacaoPrograma", "empreendimento_id"),
            ("Empreendimento", "ProjetoInvestimento", "empreendimento_id"),
        ],
        "estados": [
            "[*] --> Proposto : proposição do programa",
            "Proposto --> Aprovado : aprovação do colegiado",
            "Aprovado --> EmExecucao : publicar e abrir adesões",
            "EmExecucao --> Concluido : encerramento com resultado (RN-DEC-004)",
            "EmExecucao --> Cancelado : cancelar programa",
            "Concluido --> [*]",
            "Cancelado --> [*]",
            "state Proposto",
            "state Aprovado",
            "state EmExecucao",
            "state Concluido",
            "state Cancelado",
        ],
        "notas_003": [
            "note right of EmExecucao\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "O empreendimento referencia a pessoa\n"
            "jurídica do DOM-CUM por identificador\n"
            "(RN-DEC-001); adesões somente com o\n"
            "programa em execução (RN-DEC-002).\n"
            "end note",
            "note bottom of Concluido\n"
            "Investimento e empregos aferidos no\n"
            "encerramento alimentam os indicadores\n"
            "econômicos do DOM-IND (RN-DEC-003 e\n"
            "RN-DEC-004).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-IND",
        "nome": "Indicadores e Desempenho",
        "schema": "ind",
        "prefixo": "/api/v1/ind",
        "status": "Em elaboração",
        "central": "Indicador",
        "correlatos": [
            ("DOM-DAD", "Dados Corporativos"),
            ("DOM-PLA", "Planejamento Governamental"),
            ("DOM-ANA", "Analytics e Inteligência"),
        ],
        "capacidades": [
            "Indicadores Estratégicos",
            "Indicadores Operacionais",
            "Indicadores de Políticas Públicas",
            "Metas",
            "Resultados",
            "Painéis",
        ],
        "processos": [
            "Definir o indicador",
            "Validar fonte e fórmula",
            "Fixar a meta do exercício",
            "Coletar os valores",
            "Validar a coleta",
            "Publicar no painel",
            "Revisar ou descontinuar",
        ],
        "regras": [
            (
                "RN-IND-001",
                "o indicador declara fórmula, unidade, periodicidade e fonte.",
            ),
            ("RN-IND-002", "a meta é anual e declara valor base, valor alvo, prazo e responsável."),
            ("RN-IND-003", "o valor coletado só é publicado após validação do responsável."),
            (
                "RN-IND-004",
                "a fonte é referenciada ao DOM-DAD por identificador; sem cópia.",
            ),
        ],
        "enums": {
            "CategoriaIndicador": [
                ("ESTRATEGICO", '"estrategico"'),
                ("OPERACIONAL", '"operacional"'),
                ("POLITICA_PUBLICA", '"politica_publica"'),
            ],
            "Periodicidade": [
                ("MENSAL", '"mensal"'),
                ("TRIMESTRAL", '"trimestral"'),
                ("SEMESTRAL", '"semestral"'),
                ("ANUAL", '"anual"'),
            ],
            "SituacaoIndicador": [
                ("RASCUNHO", '"rascunho"'),
                ("EM_VALIDACAO", '"em_validacao"'),
                ("PUBLICADO", '"publicado"'),
                ("DESCONTINUADO", '"descontinuado"'),
            ],
        },
        "enum_links": [
            ("Indicador", "CategoriaIndicador"),
            ("Indicador", "Periodicidade"),
            ("Indicador", "SituacaoIndicador"),
            ("MetaIndicador", "SituacaoIndicador"),
        ],
        "entidades": [
            entidade(
                "Indicador",
                "indicadores",
                "Indicador corporativo com fórmula, unidade e fonte de dados.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "categoria:string:TEXT:NN",
                    "formula:texto:TEXT:NN",
                    "unidade:string:TEXT:NN",
                    "periodicidade:string:TEXT:NN",
                    "fonte_ref:string:TEXT:NN",
                    "responsavel:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "MetaIndicador",
                "metas_indicador",
                "Meta anual de um indicador com valor base e alvo.",
                [
                    "indicador_id:string:TEXT:NN",
                    "exercicio:int:INTEGER:NN",
                    "valor_base:decimal:FLOAT",
                    "valor_alvo:decimal:FLOAT:NN",
                    "prazo:date:DATE:NN",
                    "responsavel:string:TEXT",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "ColetaIndicador",
                "coletas_indicador",
                "Valor apurado do indicador em um período.",
                [
                    "indicador_id:string:TEXT:NN",
                    "exercicio:int:INTEGER:NN",
                    "periodo:string:TEXT:NN",
                    "valor:decimal:FLOAT:NN",
                    "fonte:string:TEXT:NN",
                    "data_coleta:date:DATE:NN",
                    "validado:bool:BOOLEAN:NN",
                    "observacao:texto:TEXT",
                ],
            ),
            entidade(
                "Painel",
                "paineis",
                "Painel de indicadores publicado para um público definido.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "publico:bool:BOOLEAN:NN",
                    "periodicidade:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                    "ultimo_atualizacao:datetime:TIMESTAMPTZ",
                ],
            ),
        ],
        "relacoes": [
            ("Indicador", "MetaIndicador", "indicador_id"),
            ("Indicador", "ColetaIndicador", "indicador_id"),
        ],
        "estados": [
            "[*] --> Rascunho : definição do indicador",
            "Rascunho --> EmValidacao : validar fonte e fórmula (RN-IND-001)",
            "EmValidacao --> Publicado : publicar após validação (RN-IND-003)",
            "EmValidacao --> Rascunho : devolver com ressalvas",
            "Publicado --> EmValidacao : programa de revisão",
            "Publicado --> Descontinuado : descontinuar com justificativa",
            "Descontinuado --> [*]",
            "state Rascunho",
            "state EmValidacao",
            "state Publicado",
            "state Descontinuado",
        ],
        "notas_003": [
            "note right of EmValidacao\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "O indicador é domínio mestre (mapa de\n"
            "domínios) e referencia a fonte no\n"
            "DOM-DAD por identificador (RN-IND-004).\n"
            "end note",
            "note bottom of Publicado\n"
            "Cada coleta possui um responsável e\n"
            "entra no painel somente após validação\n"
            "(RN-IND-003); a meta do exercício é\n"
            "anual (RN-IND-002).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-ANA",
        "nome": "Analytics e Inteligência",
        "schema": "ana",
        "prefixo": "/api/v1/ana",
        "status": "Em elaboração",
        "central": "Analise",
        "correlatos": [
            ("DOM-DAD", "Dados Corporativos"),
            ("DOM-IND", "Indicadores e Desempenho"),
            ("DOM-MET", "Metadados Corporativos"),
        ],
        "capacidades": [
            "Análise de Dados",
            "Estatística",
            "Modelos Preditivos",
            "Ciência de Dados e IA",
            "Apoio à Decisão",
        ],
        "processos": [
            "Formular a pergunta de negócio",
            "Selecionar a fonte de dados",
            "Preparar e transformar os dados",
            "Treinar ou calibrar o modelo",
            "Executar a análise",
            "Validar o resultado",
            "Publicar a recomendação",
            "Monitorar o modelo em uso",
        ],
        "regras": [
            (
                "RN-ANA-001",
                "a fonte referencia ativo do DOM-DAD por identificador; sem cópia.",
            ),
            ("RN-ANA-002", "modelo em produção declara versão, métrica e data de treinamento."),
            ("RN-ANA-003", "a análise registra fonte, modelo quando houver, responsável e data."),
            (
                "RN-ANA-004",
                "resultado aplicado a decisão pública é rastreável até a análise que o originou.",
            ),
        ],
        "enums": {
            "TipoModeloAnalitico": [
                ("ESTATISTICO", '"estatistico"'),
                ("PREDITIVO", '"preditivo"'),
                ("CLUSTERIZACAO", '"clusterizacao"'),
                ("IA", '"ia"'),
            ],
            "SituacaoAnalitica": [
                ("RASCUNHO", '"rascunho"'),
                ("EM_VALIDACAO", '"em_validacao"'),
                ("EM_PRODUCAO", '"em_producao"'),
                ("DESCONTINUADO", '"descontinuado"'),
            ],
        },
        "enum_links": [
            ("ModeloAnalitico", "TipoModeloAnalitico"),
            ("ModeloAnalitico", "SituacaoAnalitica"),
            ("Analise", "SituacaoAnalitica"),
        ],
        "entidades": [
            entidade(
                "FonteAnalitica",
                "fontes_analiticas",
                "Fonte de dados analítica referenciada no DOM-DAD.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "tipo:string:TEXT:NN",
                    "referencia:string:TEXT:NN",
                    "periodicidade:string:TEXT:NN",
                    "ultima_atualizacao:datetime:TIMESTAMPTZ",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "ModeloAnalitico",
                "modelos_analiticos",
                "Modelo estatístico, preditivo ou de IA em uso.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "tipo:string:TEXT:NN",
                    "tecnologia:string:TEXT:NN",
                    "versao:string:TEXT:NN",
                    "metrica:string:TEXT:NN",
                    "treinado_em:date:DATE:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "Analise",
                "analises",
                "Análise executada com fonte, modelo e responsável.",
                [
                    "codigo:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "fonte_id:string:TEXT:NN",
                    "modelo_id:string:TEXT",
                    "responsavel:string:TEXT:NN",
                    "data_execucao:date:DATE:NN",
                    "resultado:texto:TEXT",
                    "visibilidade:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "Recomendacao",
                "recomendacoes",
                "Recomendação decorrente da análise para a decisão.",
                [
                    "analise_id:string:TEXT:NN",
                    "destinatario:string:TEXT:NN",
                    "recomendacao:texto:TEXT:NN",
                    "prioridade:string:TEXT:NN",
                    "data:date:DATE:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
        ],
        "relacoes": [
            ("FonteAnalitica", "Analise", "fonte_id"),
            ("ModeloAnalitico", "Analise", "modelo_id"),
            ("Analise", "Recomendacao", "analise_id"),
        ],
        "estados": [
            "[*] --> Rascunho : desenho do modelo",
            "Rascunho --> EmValidacao : treinar e avaliar",
            "EmValidacao --> EmProducao : aprovar em produção (RN-ANA-002)",
            "EmValidacao --> Rascunho : ajustar desenho",
            "EmProducao --> Descontinuado : descontinuar versão",
            "Descontinuado --> [*]",
            "state Rascunho",
            "state EmValidacao",
            "state EmProducao",
            "state Descontinuado",
        ],
        "notas_003": [
            "note right of EmValidacao\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "A fonte é referência externa ao domínio\n"
            "(RN-ANA-001) e a análise registra\n"
            "responsável e data (RN-ANA-003).\n"
            "end note",
            "note bottom of EmProducao\n"
            "Cada análise permanece rastreável: a\n"
            "recomendação referencia a análise de\n"
            "origem (RN-ANA-004).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-MOB",
        "nome": "Mobilidade e Serviços de Campo",
        "schema": "mob",
        "prefixo": "/api/v1/mob",
        "status": "Em elaboração",
        "central": "OrdemCampo",
        "correlatos": [
            ("DOM-GEO", "Geoinformação Municipal"),
            ("DOM-TEL", "Gestão Territorial"),
        ],
        "capacidades": [
            "Dispositivos Móveis",
            "Aplicativos de Campo",
            "Ordens de Serviço",
            "Captura de Evidências",
            "Geolocalização",
            "Sincronização e Operação Offline",
        ],
        "processos": [
            "Vincular o dispositivo",
            "Distribuir a ordem de serviço",
            "Assinar a ordem no campo",
            "Executar com registro offline",
            "Capturar evidências e geoponto",
            "Sincronizar os registros",
            "Tratar conflitos de sincronização",
            "Concluir e liberar a ordem",
        ],
        "regras": [
            (
                "RN-MOB-001",
                "o dispositivo é vinculado a pessoa e mantém a última sincronização.",
            ),
            (
                "RN-MOB-002",
                "a ordem executa offline e só conclui após sincronizar.",
            ),
            (
                "RN-MOB-003",
                "a evidência preserva data de captura, geolocalização e integridade do arquivo.",
            ),
            (
                "RN-MOB-004",
                "conflito de sincronização não sobrescreve dado sem decisão.",
            ),
        ],
        "enums": {
            "TipoOrdemCampo": [
                ("VISTORIA", '"vistoria"'),
                ("COLETA", '"coleta"'),
                ("MANUTENCAO", '"manutencao"'),
                ("LEVANTAMENTO", '"levantamento"'),
                ("OUTRO", '"outro"'),
            ],
            "SituacaoOrdemCampo": [
                ("ABERTA", '"aberta"'),
                ("ASSINADA", '"assinada"'),
                ("EM_CAMPO", '"em_campo"'),
                ("CONCLUIDA", '"concluida"'),
                ("CANCELADA", '"cancelada"'),
            ],
            "SituacaoSincronizacao": [
                ("EM_ANDAMENTO", '"em_andamento"'),
                ("CONCLUIDA", '"concluida"'),
                ("COM_CONFLITO", '"com_conflito"'),
                ("FALHA", '"falha"'),
            ],
        },
        "enum_links": [
            ("OrdemCampo", "TipoOrdemCampo"),
            ("OrdemCampo", "SituacaoOrdemCampo"),
            ("RegistroSincronizacao", "SituacaoSincronizacao"),
        ],
        "entidades": [
            entidade(
                "DispositivoMovel",
                "dispositivos_moveis",
                "Dispositivo vinculado a um servidor e ao aplicativo de campo.",
                [
                    "codigo:string:TEXT:NN",
                    "identificador:string:TEXT:NN",
                    "modelo:string:TEXT",
                    "pessoa_id:string:TEXT",
                    "versao_app:string:TEXT",
                    "ultimo_acesso:datetime:TIMESTAMPTZ",
                    "sincronizado_em:datetime:TIMESTAMPTZ",
                    "situacao:string:TEXT:NN",
                ],
            ),
            entidade(
                "OrdemCampo",
                "ordens_campo",
                "Ordem de serviço executada em campo, inclusive offline.",
                [
                    "numero:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "dispositivo_id:string:TEXT",
                    "responsavel_id:string:TEXT",
                    "bairro_id:string:TEXT",
                    "prioridade:int:INTEGER:NN",
                    "situacao:string:TEXT:NN",
                    "data_abertura:date:DATE:NN",
                    "data_conclusao:date:DATE",
                ],
            ),
            entidade(
                "EvidenciaCampo",
                "evidencias_campo",
                "Foto, áudio, texto ou geoponto capturado em campo.",
                [
                    "ordem_id:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "arquivo_ref:string:TEXT",
                    "latitude:decimal:FLOAT:NN",
                    "longitude:decimal:FLOAT:NN",
                    "data_captura:datetime:TIMESTAMPTZ:NN",
                    "hash:string:TEXT",
                    "sincronizada:bool:BOOLEAN:NN",
                    "observacao:texto:TEXT",
                ],
            ),
            entidade(
                "RegistroSincronizacao",
                "sincronizacoes",
                "Execução de sincronização entre dispositivo e servidor.",
                [
                    "dispositivo_id:string:TEXT:NN",
                    "data_inicio:datetime:TIMESTAMPTZ:NN",
                    "data_fim:datetime:TIMESTAMPTZ",
                    "registros_enviados:int:INTEGER:NN",
                    "registros_recebidos:int:INTEGER",
                    "conflitos:int:INTEGER:NN",
                    "situacao:string:TEXT:NN",
                ],
            ),
        ],
        "relacoes": [
            ("DispositivoMovel", "OrdemCampo", "dispositivo_id"),
            ("OrdemCampo", "EvidenciaCampo", "ordem_id"),
            ("DispositivoMovel", "RegistroSincronizacao", "dispositivo_id"),
        ],
        "estados": [
            "[*] --> Aberta : distribuição da ordem",
            "Aberta --> Assinada : aceite pelo servidor (RN-MOB-001)",
            "Assinada --> EmCampo : início da execução",
            "EmCampo --> AguardandoSincronizacao : execução offline concluída",
            "AguardandoSincronizacao --> Concluida : sincronização sem conflito (RN-MOB-002)",
            "AguardandoSincronizacao --> EmCampo : conflito de sincronização (RN-MOB-004)",
            "Aberta --> Cancelada : cancelar ordem",
            "EmCampo --> Cancelada : cancelar ordem",
            "Concluida --> [*]",
            "Cancelada --> [*]",
            "state Aberta",
            "state Assinada",
            "state EmCampo",
            "state AguardandoSincronizacao",
            "state Concluida",
            "state Cancelada",
        ],
        "notas_003": [
            "note right of EmCampo\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "A evidência preserva data, geolocalização\n"
            "e integridade do arquivo (RN-MOB-003).\n"
            "end note",
            "note bottom of AguardandoSincronizacao\n"
            "A ordem só é concluída depois da\n"
            "sincronização (RN-MOB-002); conflito\n"
            "exige decisão explícita e não\n"
            "sobrescreve o dado local (RN-MOB-004).\n"
            "end note",
        ],
    },
    {
        "codigo": "DOM-INF",
        "nome": "Infraestrutura Tecnológica",
        "schema": "inf",
        "prefixo": "/api/v1/inf",
        "status": "Em elaboração",
        "central": "RecursoInfraestrutura",
        "correlatos": [
            ("DOM-SEG", "Segurança da Informação"),
            ("DOM-DAD", "Dados Corporativos"),
            ("DOM-INT", "Integração e Interoperabilidade"),
        ],
        "capacidades": [
            "Computação e Armazenamento",
            "Redes",
            "Bancos de Dados",
            "Nuvem",
            "Dispositivos",
            "Ambientes",
        ],
        "processos": [
            "Catalogar o recurso",
            "Vincular o recurso ao ambiente",
            "Monitorar as métricas",
            "Tratar o incidente",
            "Executar a manutenção programada",
            "Descomissionar o recurso",
            "Atualizar o inventário",
        ],
        "regras": [
            (
                "RN-INF-001",
                "o recurso pertence a um ambiente e registra tipo e situação.",
            ),
            ("RN-INF-002", "métrica coletada além do limite gera status de atenção ou crítico."),
            (
                "RN-INF-003",
                "o incidente tem severidade, responsável, data de abertura e data de encerramento.",
            ),
            (
                "RN-INF-004",
                "ativos de dados são referenciados no DOM-DAD por identificador.",
            ),
        ],
        "enums": {
            "TipoRecursoInfra": [
                ("SERVIDOR", '"servidor"'),
                ("ESTOQUE", '"estoque"'),
                ("REDE", '"rede"'),
                ("BANCO", '"banco"'),
                ("NUVEM", '"nuvem"'),
                ("DISPOSITIVO", '"dispositivo"'),
            ],
            "SituacaoRecurso": [
                ("DISPONIVEL", '"disponivel"'),
                ("MANUTENCAO", '"manutencao"'),
                ("INDISPONIVEL", '"indisponivel"'),
                ("DESCOMISSIONADO", '"descomissionado"'),
            ],
            "StatusMonitoramento": [
                ("OK", '"ok"'),
                ("ATENCAO", '"atencao"'),
                ("CRITICO", '"critico"'),
            ],
        },
        "enum_links": [
            ("RecursoInfraestrutura", "TipoRecursoInfra"),
            ("RecursoInfraestrutura", "SituacaoRecurso"),
            ("MonitoramentoInfra", "StatusMonitoramento"),
        ],
        "entidades": [
            entidade(
                "AmbienteInfraestrutura",
                "ambientes_infraestrutura",
                "Ambiente de execução por finalidade e criticidade.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "responsavel:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "situacao:string:TEXT:NN",
                    "ultimo_check:datetime:TIMESTAMPTZ",
                ],
            ),
            entidade(
                "RecursoInfraestrutura",
                "recursos_infraestrutura",
                "Recurso de computação, armazenamento, rede, banco ou nuvem.",
                [
                    "codigo:string:TEXT:NN",
                    "nome:string:TEXT:NN",
                    "tipo:string:TEXT:NN",
                    "ambiente_id:string:TEXT:NN",
                    "capacidade:string:TEXT",
                    "provedor:string:TEXT",
                    "identificador_externo:string:TEXT",
                    "situacao:string:TEXT:NN",
                    "data_aquisicao:date:DATE",
                    "garantia_ate:date:DATE",
                ],
            ),
            entidade(
                "MonitoramentoInfra",
                "monitoramentos_infraestrutura",
                "Métrica coletada do recurso e confrontada com o limite.",
                [
                    "recurso_id:string:TEXT:NN",
                    "metrica:string:TEXT:NN",
                    "valor:decimal:FLOAT:NN",
                    "unidade:string:TEXT:NN",
                    "limite:decimal:FLOAT",
                    "status:string:TEXT:NN",
                    "coletado_em:datetime:TIMESTAMPTZ:NN",
                ],
            ),
            entidade(
                "IncidenteInfra",
                "incidentes_infraestrutura",
                "Incidente operacional com severidade e responsáveis.",
                [
                    "numero:string:TEXT:NN",
                    "titulo:string:TEXT:NN",
                    "descricao:texto:TEXT",
                    "recurso_id:string:TEXT",
                    "severidade:string:TEXT:NN",
                    "aberto_em:datetime:TIMESTAMPTZ:NN",
                    "fechado_em:datetime:TIMESTAMPTZ",
                    "responsavel:string:TEXT:NN",
                    "situacao:string:TEXT:NN",
                    "causa:texto:TEXT",
                ],
            ),
        ],
        "relacoes": [
            ("AmbienteInfraestrutura", "RecursoInfraestrutura", "ambiente_id"),
            ("RecursoInfraestrutura", "MonitoramentoInfra", "recurso_id"),
            ("RecursoInfraestrutura", "IncidenteInfra", "recurso_id"),
        ],
        "estados": [
            "[*] --> Disponivel : catalogação do recurso (RN-INF-001)",
            "Disponivel --> Manutencao : manutenção programada",
            "Manutencao --> Disponivel : manutenção concluída",
            "Disponivel --> Indisponivel : incidente crítico (RN-INF-003)",
            "Indisponivel --> Disponivel : resolução do incidente",
            "Disponivel --> Descomissionado : baixa do recurso",
            "Descomissionado --> [*]",
            "state Disponivel",
            "state Manutencao",
            "state Indisponivel",
            "state Descomissionado",
        ],
        "notas_003": [
            "note right of Disponivel\n"
            "Modelo proposto: o domínio não possui\n"
            "módulo implementado (matriz 031).\n\n"
            "O ativo de dado hospedado é referenciado\n"
            "no DOM-DAD (RN-INF-004) e o ambiente\n"
            "determina a criticidade.\n"
            "end note",
            "note bottom of Indisponivel\n"
            "Métrica acima do limite gera status de\n"
            "atenção ou crítico (RN-INF-002); o\n"
            "incidente é encerrado com causa e\n"
            "responsável registrados.\n"
            "end note",
        ],
    },
]


# ==============================================================================
# MONTAGEM DO MODELO — DOMÍNIOS PROPOSTOS
# ==============================================================================


def montar_proposto(cfg: dict) -> dict:
    """Normaliza a configuração declarada do domínio sem implementação."""
    entidades = cfg["entidades"]
    return {
        "codigo": cfg["codigo"],
        "nome": cfg["nome"],
        "schema": cfg["schema"],
        "prefixo": cfg["prefixo"],
        "status": cfg["status"],
        "implementado": False,
        "central": cfg["central"],
        "correlatos": cfg["correlatos"],
        "capacidades": cfg["capacidades"],
        "processos": cfg["processos"],
        "use_cases": [],
        "operacoes": 0,
        "regras": cfg["regras"],
        "tabelas": [
            {
                "tabela": item["tabela"],
                "classe": item["classe"],
                "colunas": item["colunas"],
                "doc": item["doc"],
            }
            for item in entidades
        ],
        "tabela_de_classe": {item["classe"]: item["tabela"] for item in entidades},
        "entidades": [
            {"classe": item["classe"], "atributos": item["atributos"]} for item in entidades
        ],
        "enums": cfg["enums"],
        "enum_links": cfg["enum_links"],
        "relacoes": cfg["relacoes"],
        "estados": cfg["estados"],
        "notas_003": cfg["notas_003"],
    }


# ==============================================================================
# ARQUITETURA CORPORATIVA (01-Arquitetura-Corporativa)
# ==============================================================================

DIRETORIO_ARQUITETURA = "01-Arquitetura-Corporativa"
NOMES_ARQUIVOS_ARQUITETURA = (
    "000-Arquitetura-Geral.puml",
    "001-Contexto-do-Sistema.puml",
    "002-Componentes.puml",
    "003-Fluxo-de-Dados.puml",
    "004-Integracoes.puml",
    "005-Infraestrutura.puml",
)


def extrair_servicos_compose() -> list[dict]:
    """Serviços do `docker-compose.yml` com imagem, container e portas."""
    linhas = (RAIZ / "docker-compose.yml").read_text(encoding="utf-8").splitlines()
    servicos: list[dict] = []
    atual: dict | None = None
    volume = re.compile(r"^  (postgres_data|redis_data|sigmun-network):")
    for linha in linhas:
        inicio = re.match(r"^  ([a-z0-9_-]+):\s*$", linha)
        if inicio:
            atual = {"nome": inicio.group(1), "ports": []}
            if not volume.match(linha):
                servicos.append(atual)
            continue
        if atual is None:
            continue
        atributo = re.match(r"^    (image|container_name):\s*(.+)$", linha)
        if atributo:
            atual[atributo.group(1)] = atributo.group(2).strip()
        elif re.match(r"^    build:\s*$", linha):
            atual["build"] = "Dockerfile do repositório"
        elif re.match(r"^    command:\s*(.+)$", linha):
            atual["command"] = linha.strip().split(": ", 1)[-1][:80]
        elif re.match(r'^      - "\d+:\d+"\s*$', linha):
            atual["ports"].append(linha.strip().strip('- "'))
    return servicos


def fatos_repositorio() -> dict:
    """Estrutura real do código, usada como evidência nos diagramas."""
    modulos = sorted(
        p.name
        for p in (RAIZ / "src" / "modules").glob("sigmun_*")
        if p.is_dir() and not p.name.startswith("__")
    )
    implementados = sorted(
        nome
        for nome in modulos
        if any(
            caminho.stat().st_size > 1000
            for caminho in (RAIZ / "src" / "modules" / nome).rglob("*.py")
        )
    )
    return {
        "modulos": modulos,
        "modulos_implementados": implementados,
        "camadas_core": sorted(
            p.name
            for p in (RAIZ / "src" / "core").iterdir()
            if p.is_dir() and not p.name.startswith("__")
        ),
        "compartilhado": sorted(
            p.name
            for p in (RAIZ / "src" / "shared").iterdir()
            if p.is_dir() and not p.name.startswith("__")
        ),
        "frontends": sorted(p.name for p in (RAIZ / "frontend").iterdir() if p.is_dir()),
        "mobiles": sorted(p.name for p in (RAIZ / "mobile").iterdir() if p.is_dir()),
        "infra": sorted(p.name for p in (RAIZ / "infra").iterdir() if p.is_dir()),
        "servicos": extrair_servicos_compose(),
    }


def cabecalho_arquetura(tipo: str, subtipo: str, status: str = "Vigente") -> list[str]:
    return [
        "@startuml",
        f"title SIGMUN — {tipo}",
        "",
        legenda("SIGMUN", "Arquitetura Corporativa", tipo, subtipo, status),
        "",
        "skinparam componentStyle rectangle",
        "skinparam packageStyle rectangle",
        "",
    ]


def arquitetura_000() -> str:
    fatos = fatos_repositorio()
    linhas = cabecalho_arquetura("Arquitetura Geral", "Camadas do sistema")
    linhas += [
        'package "Interfaces" {',
        '  component "Portal Administrativo\\nfrontend/admin" as ADMIN',
        '  component "Portal do Cidadão\\nfrontend/portal-cidadao" as PCID',
        '  component "Portal do Fornecedor\\nfrontend/portal-fornecedor" as PFOR',
        '  component "Aplicativos Móveis\\nmobile/*" as MOV',
        "}",
        "",
        'package "Aplicação — SIGMUN" {',
        '  component "API REST\\nFastAPI · /api/v1" as API',
        '  component "src/core\\naplicação · domínio ·\\ninfraestrutura · apresentação" as CORE',
        f'  component "src/modules\\n{len(fatos["modulos"])} domínios (Bounded Context)" as MODS',
        '  component "src/shared\\nconfig · segurança ·\\ntarefas · middleware" as SHARED',
        "}",
        "",
        'package "Dados e Plataforma" {',
        '  database "PostgreSQL 15\\nschemas por domínio" as PG',
        '  database "Redis 7" as REDIS',
        '  component "Alembic\\nalembic/versions" as MIG',
        '  component "Celery\\nworker · beat · flower" as CELERY',
        "}",
        "",
        "ADMIN --> API : HTTP / REST",
        "PCID --> API : HTTP / REST",
        "PFOR --> API : HTTP / REST",
        "MOV --> API : HTTP / REST",
        "",
        "API --> CORE",
        "CORE --> MODS",
        "CORE --> SHARED",
        "SHARED --> CELERY : tarefas assíncronas",
        "",
        "CORE --> PG : SQLAlchemy",
        "SHARED --> REDIS : cache",
        "CELERY --> PG",
        "CELERY --> REDIS",
        "MIG --> PG : migrações",
        "",
        "note right of CORE",
        "Arquitetura em quatro camadas no núcleo",
        "(application, domain, infrastructure e",
        "presentation) e uma camada de módulos",
        "por domínio, com verificação de dependência.",
        "end note",
        "",
        "note bottom of API",
        "Contrato externo único:",
        "API REST sob /api/v1.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


def arquitetura_001() -> str:
    fatos = fatos_repositorio()
    linhas = cabecalho_arquetura("Contexto do Sistema", "Atores e fronteiras")
    linhas += [
        'actor "Cidadão" as Cidadao',
        'actor "Servidor Público" as Servidor',
        'actor "Gestor Municipal" as Gestor',
        'actor "Fornecedor" as Fornecedor',
        'actor "Administrador do SIGMUN" as Admin',
        "",
        'rectangle "SIGMUN — Sistema Integrado de Gestão Municipal" as SIGMUN',
        "",
        'rectangle "Serviços de Identidade e Acesso\\nDOM-IDN" as IDN',
        'rectangle "Segurança da Informação\\nDOM-SEG" as SEG',
        'rectangle "Gestão Documental\\nDOM-GDO" as GDO',
        'rectangle "Metadados Corporativos\\nDOM-MET" as MET',
        'rectangle "Interoperabilidade\\nDOM-INT" as INT',
        'rectangle "Auditoria\\ntrilha de eventos" as AUD',
        'rectangle "Sistemas externos\\nFalaBR / e-OUV · IBGE · cartório" as EXT',
        "",
        "Cidadao --> SIGMUN : consulta e solicita serviços",
        "Servidor --> SIGMUN : executa processos",
        "Gestor --> SIGMUN : acompanha e decide",
        "Fornecedor --> SIGMUN : participa de processos",
        "Admin --> SIGMUN : administra a plataforma",
        "",
        "SIGMUN --> IDN : autenticação e autorização",
        "SIGMUN --> SEG : políticas e controles de acesso",
        "SIGMUN --> GDO : documentos e evidências",
        "SIGMUN --> MET : metadados e classificação",
        "SIGMUN --> INT : troca de dados entre domínios",
        "SIGMUN --> AUD : eventos",
        "SIGMUN --> EXT : integrações externas",
        "",
        "note bottom of SIGMUN",
        "Fronteira única de dados: a API REST sob",
        f"/api/v1 e {len(fatos['modulos'])} módulos de domínio",
        "em src/modules.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


def arquitetura_002() -> str:
    fatos = fatos_repositorio()
    linhas = [
        "@startuml",
        "title SIGMUN — Componentes",
        "",
        legenda(
            "SIGMUN",
            "Arquitetura Corporativa",
            "Componentes",
            "Mapa de componentes do código",
            "Vigente",
        ),
        "",
        "skinparam componentStyle rectangle",
        "skinparam packageStyle rectangle",
        "",
        'package "src/core — núcleo compartilhado" {',
    ]
    rotulos_core = {
        "application": "Aplicação (use cases e portas)",
        "domain": "Domínio (entidades e regras)",
        "infrastructure": "Infraestrutura (repositórios)",
        "presentation": "Apresentação (APIs e schemas)",
    }
    for camada in fatos["camadas_core"]:
        linhas.append(f'  component "{rotulos_core.get(camada, camada)}" as C_{camada}')
    linhas += [
        "}",
        "",
        'package "src/modules — domínios" {',
    ]
    implementados = set(fatos["modulos_implementados"])
    for modulo in fatos["modulos"]:
        marca = "●" if modulo in implementados else "○"
        linhas.append(f'  component "{marca} {modulo}" as M_{modulo}')
    linhas += [
        "}",
        "",
        'package "src/shared — compartilhado" {',
    ]
    rotulos_shared = {
        "config": "Configuração e Celery",
        "constants": "Constantes",
        "exceptions": "Exceções",
        "middleware": "Middleware",
        "security": "Segurança",
        "tasks": "Tarefas assíncronas",
        "utils": "Utilitários",
    }
    for item in fatos["compartilhado"]:
        linhas.append(f'  component "{rotulos_shared.get(item, item)}" as S_{item}')
    linhas += [
        "}",
        "",
        'package "Interfaces" {',
        '  component "frontend/admin" as F_admin',
        '  component "frontend/portal-cidadao" as F_cidadao',
        '  component "frontend/portal-fornecedor" as F_fornecedor',
        '  component "mobile/*" as MOB',
        "}",
        "",
        'package "Persistência e Infraestrutura" {',
        '  component "alembic/versions" as MIG',
        '  component "infra/docker" as IDOCKER',
        '  component "infra/kubernetes" as IKUBE',
        '  component "infra/terraform" as ITF',
        '  component "docker-compose.yml" as COMPOSE',
        "}",
        "",
        "F_admin --> C_presentation : HTTP / REST",
        "F_cidadao --> C_presentation : HTTP / REST",
        "F_fornecedor --> C_presentation : HTTP / REST",
        "MOB --> C_presentation : HTTP / REST",
        "",
        "C_presentation --> C_application",
        "C_application --> C_domain",
        "C_infrastructure --> C_domain",
        "C_infrastructure --> MIG",
        "",
        "note right of C_presentation",
        "As interfaces HTTP de todos os domínios",
        "são registradas em src/main.py.",
        "end note",
        "",
        "note bottom of M_sigmun_territorial",
        "● módulo com implementação identificada\\n○ módulo preparado (scaffolding)",
        "end note",
        "",
        "note bottom of COMPOSE",
        "Ambiente local com PostgreSQL 15, Redis 7,",
        "backend, três frontends, worker, beat e flower.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


def arquitetura_003() -> str:
    linhas = cabecalho_arquetura("Fluxo de Dados", "Ciclo de uma requisição")
    linhas += [
        "start",
        ":Usuário envia requisição HTTP;",
        ":Roteador valida esquema e autentica;",
        ":Caso de uso aplica a regra de negócio;",
        ":Entidade é alterada ou consultada;",
        ":Repositório persiste no schema do domínio;",
        ":Evento de auditoria é registrado;",
        ":Resposta JSON é serializada;",
        ":Resposta HTTP ao usuário;",
        "",
        "if (tarefa assíncrona?) then (yes)",
        "  :Publicar na fila Celery;",
        "  :Worker processa fora do ciclo da requisição;",
        "  :Atualizar o estado no PostgreSQL;",
        "  :Registrar resultado na outbox;",
        "else (no)",
        "  :Concluir a transação;",
        "endif",
        "",
        ":Cache Redis atualizado quando aplicável;",
        "stop",
        "",
        "note left",
        "Fluxo síncrono: interface, API, caso de uso,",
        "domínio, infraestrutura e PostgreSQL.",
        "",
        "Sem chave estrangeira entre schemas de",
        "domínios: a relação é feita por",
        "identificador opaco e contrato (DOM-INT).",
        "end note",
        "",
        "note right",
        "Transação: a escrita e o evento de auditoria",
        "ocorrem na mesma unidade de trabalho;",
        "a falha reverte a operação.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


def arquitetura_004() -> str:
    fatos = fatos_repositorio()
    linhas = cabecalho_arquetura("Integrações", "Troca de dados entre componentes")
    linhas += [
        'package "Domínios" {',
        '  component "Domínio de origem\\nsrc/modules/sigmun_*" as ORIGEM',
        '  component "Domínio consumidor\\nsrc/modules/sigmun_*" as DESTINO',
        "}",
        "",
        'package "Serviços Transversais SIGMUN" {',
        '  component "DOM-IDN\\nIdentidade e Acesso" as IDN',
        '  component "DOM-GDO\\nGestão Documental" as GDO',
        '  component "DOM-MET\\nMetadados Corporativos" as MET',
        '  component "DOM-SEG\\nSegurança da Informação" as SEG',
        '  component "DOM-INT\\nInteroperabilidade" as INT',
        '  component "DOM-DAD\\nDados Corporativos" as DAD',
        '  component "Auditoria\\ntrilha de eventos" as AUD',
        "}",
        "",
        'package "Sistemas Externos" {',
        '  component "FalaBR / e-OUV" as EOU',
        '  component "IBGE e base cartográfica" as IBGE',
        '  component "Cartório de registro de imóveis" as CARTORIO',
        '  component "Governos federal e estadual" as OUTROS_GOV',
        "}",
        "",
        'database "PostgreSQL\\nschemas por domínio" as PG',
        'database "Redis 7" as REDIS',
        "",
        "ORIGEM --> DESTINO : API REST interna ou evento",
        "ORIGEM --> IDN : autenticação e autorização",
        "ORIGEM --> GDO : documentos e anexos",
        "ORIGEM --> MET : metadados e classificação",
        "ORIGEM --> SEG : políticas de segurança",
        "ORIGEM --> DAD : dados corporativos mestres",
        "ORIGEM --> INT : contrato de interoperabilidade",
        "ORIGEM --> AUD : eventos",
        "ORIGEM --> PG : próprio schema",
        "DESTINO --> REDIS : cache",
        "",
        "ORIGEM --> EOU : recepção de manifestação",
        "ORIGEM --> IBGE : base territorial",
        "ORIGEM --> CARTORIO : dados registrais",
        "ORIGEM --> OUTROS_GOV : convênios e transferências",
        "",
        "note right of ORIGEM",
        f"{len(fatos['modulos'])} módulos em src/modules;",
        "cada módulo publica seu próprio prefixo",
        "de API e mantém o schema próprio.",
        "end note",
        "",
        "note bottom of INT",
        "Nenhuma chave estrangeira cruza schemas:",
        "as referências entre domínios são feitas",
        "por identificador opaco, conforme contrato.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


def arquitetura_005() -> str:
    fatos = fatos_repositorio()
    linhas = cabecalho_arquetura("Infraestrutura", "Serviços e ambientes")
    linhas += ['package "Ambiente local — docker-compose.yml" {']
    alias = {}
    for indice, servico in enumerate(fatos["servicos"]):
        detalhes = [servico.get("image") or servico.get("build") or ""]
        if servico.get("ports"):
            detalhes.append("portas " + ", ".join(servico["ports"]))
        rotulo = "\\n".join(parte for parte in detalhes if parte)
        nome = f"SVC{indice}"
        alias[servico["nome"]] = nome
        linhas.append(f'  component "{servico["nome"]}\\n{rotulo}" as {nome}')
    linhas += [
        "}",
        "",
        'package "Persistência" {',
        '  database "PostgreSQL 15\\nschema sigmun e schemas por domínio" as PG',
        '  database "Redis 7-alpine" as REDIS',
        '  component "Alembic\\nalembic/versions" as MIG',
        '  component "init.sql\\ninfra/docker/database" as INIT',
        "}",
        "",
        'package "Implantação" {',
    ]
    rotulos_infra = {
        "docker": "Dockerfiles e banco local",
        "kubernetes": "Manifestos de orquestração",
        "terraform": "Provisionamento de infraestrutura",
    }
    for indice, item in enumerate(fatos["infra"]):
        linhas.append(f'  component "{item}\\n{rotulos_infra.get(item, "")}" as INFRA{indice}')
    worker = alias.get("worker", "SVC0")
    linhas += [
        "}",
        "",
        f"{worker} --> PG : filas celery, gdo.outbox e gdo.expurgo",
        f"{alias.get('beat', worker)} --> {worker} : agenda tarefas periódicas",
        "",
        "note bottom of PG",
        "Banco do sistema: schema core (cadastro)",
        "e um schema por domínio implementado.",
        "end note",
        "",
        f"note bottom of {worker}",
        "Processamento assíncrono com Celery;",
        "o beat agenda as tarefas e o flower",
        "acompanha as filas.",
        "end note",
        "",
        "@enduml",
    ]
    return envolver("\n".join(linhas))


ARQUIVOS = {
    "000": ("000-Visao-Arquitetural.puml", arquivo_000),
    "001": ("001-Modelo-de-Dominio.puml", arquivo_001),
    "002": ("002-Processos.puml", arquivo_002),
    "003": ("003-Maquina-de-Estados.puml", arquivo_003),
    "004": ("004-Integracoes.puml", arquivo_004),
    "005": ("005-Persistencia.puml", arquivo_005),
}

MARCADORES = (
    "package ",
    "class ",
    "enum ",
    "entity ",
    "state ",
    "database ",
    "component ",
    "actor ",
)


def precisa_gerar(caminho: Path) -> bool:
    """Verdadeiro para arquivo inexistente, vazio ou apenas com a legenda."""
    if not caminho.exists():
        return True
    texto = caminho.read_text(encoding="utf-8", errors="replace").strip()
    if not texto:
        return True
    linhas = texto.splitlines()
    if any(linha.strip() == "start" for linha in linhas):
        return False
    return not any(marcador in texto for marcador in MARCADORES)


def gerar_dominio(codigo: str, modelo: dict) -> list[Path]:
    base = RAIZ / "SIGMUN-Docs" / codigo / "puml"
    base.mkdir(parents=True, exist_ok=True)
    gerados: list[Path] = []
    for nome_arquivo, emissor in ARQUIVOS.values():
        caminho = base / nome_arquivo
        if not precisa_gerar(caminho):
            continue
        caminho.write_text(emissor(modelo), encoding="utf-8")
        gerados.append(caminho)
    return gerados


EMISSORES_ARQUITETURA = (
    arquitetura_000,
    arquitetura_001,
    arquitetura_002,
    arquitetura_003,
    arquitetura_004,
    arquitetura_005,
)


def gerar_arquitetura() -> list[Path]:
    base = RAIZ / "SIGMUN-Docs" / DIRETORIO_ARQUITETURA / "puml"
    base.mkdir(parents=True, exist_ok=True)
    gerados: list[Path] = []
    for nome_arquivo, emissor in zip(
        NOMES_ARQUIVOS_ARQUITETURA, EMISSORES_ARQUITETURA, strict=True
    ):
        caminho = base / nome_arquivo
        if not precisa_gerar(caminho):
            continue
        caminho.write_text(emissor(), encoding="utf-8")
        gerados.append(caminho)
    return gerados


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apenas",
        action="append",
        help="Gera somente os domínios informados (ex.: --apenas DOM-IND).",
    )
    parser.add_argument(
        "--sem-arquitetura",
        action="store_true",
        help="Não gera os seis diagramas de 01-Arquitetura-Corporativa.",
    )
    args = parser.parse_args()

    total = 0
    for codigo, cfg in sorted(IMPLEMENTADOS.items()):
        if args.apenas and codigo not in args.apenas:
            continue
        gerados = gerar_dominio(codigo, montar_implementado(codigo, cfg))
        total += len(gerados)
        print(f"{codigo} (implementado): {len(gerados)} arquivo(s)")
    for cfg in PROPOSTOS:
        codigo = cfg["codigo"]
        if args.apenas and codigo not in args.apenas:
            continue
        gerados = gerar_dominio(codigo, montar_proposto(cfg))
        total += len(gerados)
        print(f"{codigo} (proposto): {len(gerados)} arquivo(s)")
    if not args.sem_arquitetura and not args.apenas:
        gerados = gerar_arquitetura()
        total += len(gerados)
        print(f"{DIRETORIO_ARQUITETURA}: {len(gerados)} arquivo(s)")
    print(f"Total de arquivos gerados: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
