#!/usr/bin/env python
"""Gera os artefatos `001`-`026` dos domínios DOM-TEL, DOM-IMO, DOM-GEO e DOM-OBR.

Os artefatos não são redações soltas: o gerador extrai do código-fonte os
elementos técnicos (entidades, colunas, endpoints, casos de uso e testes) e
combina com o conteúdo de negócio declarado em `docs_dados.py`. Assim, a
documentação permanece rastreável à implementação — qualquer alteração no
código é refletida ao reexecutar o gerador.

Uso:
    .venv/bin/python scripts/gerar_artefatos_territoriais.py
    .venv/bin/python scripts/gerar_artefatos_territoriais.py --verificar
                                          # falha se houver artefato defasado

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

import docs_dados as _DADOS  # noqa: E402

from src.main import app  # noqa: E402


class _ConjuntoDados:
    """Expõe os conjuntos de `docs_dados` por índice.

    O gerador monta o nome do conjunto em tempo de execução
    (ex.: `f"{prefixo}_REGRAS"`); este adaptador evita repetir o prefixo em
    cada chamada e mantém `DADOS` legível nos templates.
    """

    def __getitem__(self, nome: str) -> object:
        return getattr(_DADOS, nome)

    def __contains__(self, nome: str) -> bool:
        return hasattr(_DADOS, nome)

    def __repr__(self) -> str:
        return "<dados de documentação DOM-TEL / DOM-IMO>"


DADOS = _ConjuntoDados()


# ============================================================================
# TEMPLATES BASE (cabeçalho e rodapé)
# ============================================================================


def cabecalho(numero: int, titulo: str, cfg: dict[str, str], slug: str) -> str:
    """Cabeçalho padrão dos artefatos, conforme padrão corporativo do SIGMUN."""
    relacionados = "\n".join(f"* `{r}`" for r in RELACIONADOS)
    return f"""# {numero:03d} – {titulo} – {cfg['dominio']}

#### {titulo} – {cfg['dominio']}

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** {cfg['codigo']}-{numero:03d}

**Domínio:** {cfg['dominio']}

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-{SLUG_DOMINIO[cfg['codigo']]}.md`
{relacionados}

---

"""


def rodape(numero: int, titulo: str, cfg: dict[str, str], slug: str) -> str:
    """Rodapé padrão com controle de versões."""
    return f"""---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | {DATA_REVISAO} | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** {numero:03d}-{slug}-{SLUG_DOMINIO[cfg['codigo']]}.md

**Última atualização:** {DATA_REVISAO}

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/{cfg['modulo']}`. Alterações no código devem ser
> refletidas reexecutando o gerador.
"""

DOMINIO_TEL = "Gestão Territorial"
DOMINIO_IMO = "Cadastro Imobiliário"
DATA_REVISAO = "2026-09-29"

RELACIONADOS = [
    "000-CONSTITUICAO-DO-PROJETO-SIGMUN.md",
    "000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md",
    "000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md",
    "000C-HIERARQUIA-DOCUMENTAL.md",
    "000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md",
    "030-Roadmap-de-Implementacao-dos-Dominios.md",
    "Mapa-de-Dominios.md",
    "Modelo-Logico.md",
    "Modelo-Fisico.md",
    "Dicionario-de-dados.md",
]

METODOS = ("GET", "POST", "PATCH", "DELETE", "PUT")


# ============================================================================
# EXTRAÇÃO DO CÓDIGO-FONTE
# ============================================================================


def extrair_openapi() -> dict[str, list[str]]:
    """Mapa `caminho -> [métodos]` a partir do OpenAPI gerado pela aplicação."""
    spec = app.openapi()
    resultado: dict[str, list[str]] = {}
    for caminho, operacoes in spec["paths"].items():
        metodos = [m.upper() for m in operacoes if m.lower() in {"get", "post", "patch", "delete", "put"}]
        if metodos:
            resultado[caminho] = sorted(metodos)
    return resultado


def extrair_colunas(prefixo_modulo: str) -> dict[str, list[tuple[str, str, str]]]:
    """Extrai `(tabela, coluna, tipo_anotacao)` dos modelos ORM de um módulo."""
    from importlib import import_module

    from sqlalchemy import inspect as sa_inspect

    modelos = import_module(f"src.modules.{prefixo_modulo}.infrastructure.database.models")
    saida: dict[str, list[tuple[str, str, str]]] = {}
    for nome in modelos.Base.__subclasses__():
        mapa = sa_inspect(nome).columns
        linhas: list[tuple[str, str, str]] = []
        for coluna in mapa:
            tipo = str(coluna.type)
            if not coluna.nullable and not coluna.primary_key:
                tipo += ", NOT NULL"
            if coluna.primary_key:
                tipo += ", PK"
            if getattr(coluna, "unique", False):
                tipo += ", UNIQUE"
            padrao = ""
            if coluna.server_default is not None:
                padrao = str(coluna.server_default.arg)
            linhas.append((coluna.name, tipo, padrao))
        saida[nome.__tablename__] = linhas
    return saida


def extrair_testes(dominio: str) -> list[dict[str, str]]:
    """Conta os testes por classe, lendo os arquivos de teste do domínio."""
    padroes = {
        "DOM-TEL": "tests/unit/test_tel_*.py",
        "DOM-IMO": "tests/unit/test_imo_*.py",
        "DOM-GEO": "tests/unit/test_geo_*.py",
        "DOM-OBR": "tests/unit/test_obr_*.py",
    }
    base = RAIZ
    resultados: list[dict[str, str]] = []
    for caminho in sorted(base.glob(padroes[dominio])):
        texto = caminho.read_text(encoding="utf-8")
        doc = ""
        match = re.search(r'^"""(.+?)"""', texto, re.DOTALL)
        if match:
            doc = match.group(1).strip().splitlines()[0]
        classes = list(re.finditer(r"^class (Test\w+):", texto, re.MULTILINE))
        for indice, achado in enumerate(classes):
            classe = achado.group(1)
            fim = classes[indice + 1].start() if indice + 1 < len(classes) else len(texto)
            bloco = texto[achado.start() : fim]
            metodos = re.findall(r"^    def (test_\w+)", bloco, re.MULTILINE)
            resultados.append(
                {
                    "arquivo": str(caminho.relative_to(base)),
                    "classe": classe,
                    "doc": doc,
                    "quantidade": str(len(metodos)),
                    "metodos": ", ".join(metodos),
                }
            )
    return resultados


def extrair_use_cases(modulo: str) -> list[dict[str, str]]:
    """Extrai os casos de uso declarados nas classes de use case."""
    import inspect
    from importlib import import_module

    pacote = import_module(f"src.modules.{modulo}.application.use_cases")
    resultados: list[dict[str, str]] = []
    for nome in getattr(pacote, "__all__", []):
        obj = getattr(pacote, nome)
        if not inspect.isclass(obj) or not nome.endswith("UseCase"):
            continue
        doc = (obj.__doc__ or "").strip().splitlines()
        descricao = doc[0] if doc else ""
        metodo = getattr(obj, "execute", None)
        assinatura = ""
        if metodo is not None:
            assinatura = ", ".join(
                p.name for p in inspect.signature(metodo).parameters.values() if p.name != "self"
            )
        resultados.append(
            {"nome": nome, "descricao": descricao, "execute": assinatura}
        )
    return resultados


# ============================================================================
# GERADORES POR ARTEFATO (001 a 004)
# ============================================================================


def _resumir_operacao(caminho: str, metodo: str, prefixo: str) -> str:
    """Resume a finalidade de uma operação a partir do caminho e do método."""
    recurso = caminho[len(prefixo):].strip("/").split("/")[0] or "raiz"
    if metodo == "GET" and "{" in caminho:
        return f"Consultar {recurso} por identificador"
    acoes = {
        "get": f"Listar ou consultar {recurso}",
        "post": f"Registrar ação sobre {recurso}",
        "patch": f"Atualizar {recurso}",
        "delete": f"Excluir {recurso} (exclusão lógica)",
    }
    return acoes.get(metodo.lower(), f"Operação {metodo} em {recurso}")


def artefato_001(cfg: dict[str, str], ctx: dict) -> str:
    """Mapa de Atores."""
    pre = cfg["prefixo_regra"]
    atores = [_ator(a) for a in DADOS[f"{pre}_ATORES"]]
    linhas = [[a[0], a[1], a[2], a[3], a[6]] for a in atores]
    detalhe = "\n".join(
        f"""### {a[0]} — {a[1]}

**Tipo:** {a[2]}

**Papel:** {a[3]}

**Decisões que pode tomar:** {a[4]}

**Sistemas utilizados:** {a[5]}

**Capacidades exercidas:** {a[6]}

---
"""
        for a in atores
    )
    return f"""# 1. Finalidade

Este artefato identifica as pessoas, unidades organizacionais, papéis e entidades
externas que interagem com o domínio de {cfg['dominio']}, estabelecendo quem
participa, com que responsabilidade e em qual capacidade.

---

# 2. Princípios

* Atores representam papéis, e não pessoas específicas.
* A mesma pessoa pode exercer mais de um papel.
* Responsabilidade de negócio não se confunde com permissão de sistema.
* Atores externos são identificados quando influenciam os processos.

---

# 3. Atores Identificados

{tabela(["Identificador", "Ator", "Tipo", "Papel no domínio", "Capacidades"], linhas)}

---

# 4. Detalhamento

{detalhe}
# 5. Relação com as Capacidades

{tabela(
    ["Ator", "Capacidades"],
    [[a[0] + " — " + a[1], a[6]] for a in atores],
)}

---

# 6. Observações

* A autorização de acesso é derivada das responsabilidades descritas acima e
  tratada no artefato de modelo de segurança.
* Atores externos participam por troca de informações; não alteram o sistema.
"""


def artefato_002(cfg: dict[str, str], ctx: dict) -> str:
    """Mapa de Capacidades."""
    pre = cfg["prefixo_regra"]
    caps = [_capacidade(c) for c in DADOS[f"{pre}_CAPACIDADES"]]
    linhas = [[c[0], c[1], c[2], c[3], c[4]] for c in caps]
    detalhe = "\n".join(
        f"""### {c[0]} — {c[1]}

**Descrição:** {c[2]}

**Processos:** {c[3]}

**Regras aplicáveis:** {c[4]}

**Atores:** {c[5]}

---
"""
        for c in caps
    )
    return f"""# 1. Finalidade

Este artefato consolida as capacidades de negócio oferecidas pelo domínio de
{cfg['dominio']}, relacionando cada capacidade aos processos que a executam e
às regras de negócio que a governam.

---

# 2. Princípios

* Uma capacidade descreve **o que** o domínio entrega, não **como** é implementado.
* Capacidades são independentes de tecnologia e de interface.
* Toda capacidade deve estar rastreada a processos, requisitos e regras.

---

# 3. Capacidades Identificadas

{tabela(["Identificador", "Capacidade", "Descrição", "Processos", "Regras"], linhas)}

---

# 4. Detalhamento

{detalhe}
# 5. Cobertura

{tabela(
    ["Indicador", "Quantidade"],
    [
        ["Capacidades mapeadas", str(len(caps))],
        ["Atores exercidos", str(len(DADOS[f'{pre}_ATORES']))],
        ["Processos vinculados", str(len(DADOS[f'{pre}_PROCESSOS']))],
        ["Regras aplicadas", str(len(DADOS[f'{pre}_REGRAS']))],
    ],
)}
"""


def artefato_003(cfg: dict[str, str], ctx: dict) -> str:
    """Mapa de Processos."""
    pre = cfg["prefixo_regra"]
    procs = [_processo(p) for p in DADOS[f"{pre}_PROCESSOS"]]
    resumo = tabela(
        ["ID", "Processo", "Gatilho", "Objetivo"],
        [[p[0], p[1], p[2], p[3]] for p in procs],
    )
    blocos = []
    for p in procs:
        passos = "\n".join(f"{i + 1}. {passo}" for i, passo in enumerate(p[6]))
        blocos.append(
            f"""### {p[0]} — {p[1]}

**Gatilho:** {p[2]}

**Objetivo:** {p[3]}

**Entradas:** {p[4]}

**Saídas:** {p[5]}

**Regras aplicadas:** {p[7]}

**Passos:**

{passos}

---
"""
        )
    return f"""# 1. Finalidade

Este artefato descreve os processos de negócio do domínio de {cfg['dominio']},
da intenção do ator à alteração do estado, evidenciando entradas, saídas e
regras aplicadas.

---

# 2. Convenções

* **Gatilho:** evento ou condição que dispara o processo.
* **Objetivo:** resultado pretendido pelo processo.
* **Passos:** sequência lógica; as regras de negócio aplicadas aparecem entre
  parênteses na etapa correspondente.

---

# 3. Visão Geral

{resumo}

---

# 4. Detalhamento

{"".join(blocos)}
# 5. Processos por Capacidade

{tabela(
    ["Processo", "Capacidades", "Regras"],
    [
        [
            p[0] + " — " + p[1],
            ", ".join(
                c[0] for c in map(_capacidade, DADOS[f"{pre}_CAPACIDADES"]) if p[0] in c[3]
            ),
            p[7],
        ]
        for p in procs
    ],
)}
"""


def artefato_004(cfg: dict[str, str], ctx: dict) -> str:
    """Mapa de Serviços."""
    prefixo = cfg["prefixo"]
    rotas = ctx["rotas"]
    return f"""# 1. Finalidade

Este artefato cataloga os serviços expostos pelo domínio de {cfg['dominio']} por
meio da API REST, relacionando cada operação às capacidades e requisitos que a
sustentam.

---

# 2. Convenções

* O contrato é versionado sob o prefixo `{prefixo}`.
* Operações de escrita devolvem `409 Conflict` quando violam regra de negócio e
  `404 Not Found` quando o recurso referenciado não existe.
* Ações de transição de estado são expostas como `POST` em sub-recursos.
* A listagem é paginada por `page` e `page_size` (1 a 100).

---

# 3. Serviços Expostos

{tabela(
    ["Método", "Caminho", "Operação"],
    [[m, c, _resumir_operacao(c, m, prefixo)] for c in rotas for m in rotas[c]],
)}

---

# 4. Quantidades

{tabela(
    ["Indicador", "Quantidade"],
    [
        ["Paths publicados", str(len(rotas))],
        ["Operações", str(sum(len(v) for v in rotas.values()))],
        ["Prefixo", f"`{prefixo}`"],
    ],
)}

---

# 5. Observações de Versionamento

* Alterações que removam campos ou mudem semântica exigem nova versão do prefixo.
* Novos campos aceitos em resposta são compatíveis com o contrato vigente.
"""



def artefato_005(cfg: dict[str, str], ctx: dict) -> str:
    """Casos de Uso."""
    pre = cfg["prefixo_regra"]
    casos = DADOS[f"{pre}_CU"]
    ucs = {u["nome"] for u in ctx["use_cases"]}
    blocos = []
    for c in casos:
        cid, nome, ator, cap, pre_, fluxo, pos, regras, uc = c
        uc_tag = (
            f"`{uc}`" if uc in ucs else f"{uc} (implementado como consulta ao repositório)"
        )
        etapas = "\n".join(f"{i + 1}. {e.strip()}" for i, e in enumerate(fluxo.split(";")))
        blocos.append(
            f"""### {cid} — {nome}

**Ator:** {ator}

**Capacidade:** {cap}

**Pré-condições:** {pre_}

**Fluxo principal:**

{etapas}

**Pós-condições:** {pos}

**Regras aplicadas:** {regras}

**Caso de uso implementador:** {uc_tag}
"""
        )
    return f"""# 1. Finalidade

Este artefato especifica os casos de uso do domínio de {cfg['dominio']},
relacionando cada cenário à sua implementação na camada de casos de uso.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe de caso de uso correspondente.
* Cenários de consulta direta ao repositório são assim identificados, pois não
  exigem lógica de negócio própria.

---

# 3. Casos de Uso

{"".join(blocos)}
# 4. Cobertura

{tabela(
    ["Indicador", "Quantidade"],
    [
        ["Casos de uso especificados", str(len(casos))],
        ["Casos de uso com classe implementadora", str(sum(1 for c in casos if c[8] in ucs))],
        ["Histórias de usuário relacionadas", str(len(DADOS[f"{pre}_HU"]))],
    ],
)}
"""


def artefato_006(cfg: dict[str, str], ctx: dict) -> str:
    """Histórias de Usuário."""
    pre = cfg["prefixo_regra"]
    historias = DADOS[f"{pre}_HU"]
    blocos = []
    for h in historias:
        hid, titulo, como, quero, para_, cap, regras, crits = h
        itens = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(criterios(crits)))
        blocos.append(
            f"""### {hid} — {titulo}

**Como** {como.lower()},
**quero** {quero},
**para** {para_}.

**Capacidade:** {cap}

**Regras relacionadas:** {regras}

**Critérios de aceitação:**

{itens}
"""
        )
    return f"""# 1. Finalidade

Este artefato expressa as necessidades do domínio de {cfg['dominio']} em histórias
de usuário, com critérios de aceitação verificáveis.

---

# 2. Convenções

* O padrão é *Como / Quero / Para*, com critérios no formato
  **Dado** / **Quando** / **Então**.
* Cada critério referencia a regra de negócio que ele exercita.

---

# 3. Histórias de Usuário

{"".join(blocos)}
# 4. Rastreabilidade às Capacidades

{tabela(
    ["História", "Capacidade", "Regras"],
    [[h[0] + " — " + h[1], h[5], h[6]] for h in historias],
)}
"""


def artefato_007(cfg: dict[str, str], ctx: dict) -> str:
    """Regras de Negócio."""
    pre = cfg["prefixo_regra"]
    regras = [_regra(r) for r in DADOS[f"{pre}_REGRAS"]]
    blocos = []
    for rid, titulo, tipo, processo, desc, just, garantia in regras:
        blocos.append(
            f"""## {rid} — {titulo}

**Tipo:** {tipo}

**Processo:** {processo}

**Descrição:** {desc}

**Justificativa:** {just}

**Garantia técnica:** {garantia}

---
"""
        )
    por_tipo: dict[str, list[str]] = {}
    for r in regras:
        por_tipo.setdefault(r[2], []).append(r[0])
    return f"""# 1. Finalidade

Este artefato consolida as regras de negócio do domínio de {cfg['dominio']},
declarando as invariantes que a implementação deve preservar.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-<DOMÍNIO>-<sequencial>`, onde o número é sequencial
e estável. A numeração não é reutilizada após a revogação de uma regra.

---

# 3. Classificação das Regras

{tabela(
    ["Tipo", "Regras", "Significado"],
    [
        [t, ", ".join(v), _explicar_tipo(t)]
        for t, v in sorted(por_tipo.items())
    ],
)}

---

# 4. Regras de Negócio

{"".join(blocos)}
---

# 5. Matriz de Decisão

{tabela(
    ["Regra", "Processo", "Garantia no banco", "Testada por"],
    [[r[0], r[3], r[6], _testes_da_regra(ctx, r[0])] for r in regras],
)}
"""


def _ator(ator: dict | tuple) -> tuple:
    """Normaliza um ator para tupla de 7 campos posicionais."""
    if isinstance(ator, dict):
        return (
            ator["id"],
            ator["nome"],
            ator["tipo"],
            ator["papel"],
            ator["decisoes"],
            ator["sistemas"],
            ator["capacidades"],
        )
    return tuple(ator)


def _capacidade(capacidade: dict | tuple) -> tuple:
    """Normaliza uma capacidade para tupla de 6 campos posicionais."""
    if isinstance(capacidade, dict):
        return (
            capacidade["id"],
            capacidade["nome"],
            capacidade["descricao"],
            capacidade["processos"],
            capacidade["regras"],
            capacidade["atores"],
        )
    return tuple(capacidade)


def _processo(processo: dict | tuple) -> tuple:
    """Normaliza um processo para tupla de 8 campos posicionais."""
    if isinstance(processo, dict):
        return (
            processo["id"],
            processo["nome"],
            processo["gatilho"],
            processo["objetivo"],
            processo["entradas"],
            processo["saidas"],
            list(processo["passos"]),
            processo["regras"],
        )
    return tuple(processo)


def _regra(regra: dict | tuple) -> tuple:
    """Normaliza uma regra para tupla posicional de 7 campos.

    Aceita tanto dicionários (documentação legada) quanto tuplas, para que os
    dois domínios possam ser documentados com a mesma estrutura de templates.
    """
    if isinstance(regra, dict):
        return (
            regra["id"],
            regra["titulo"],
            regra["tipo"],
            regra["processo"],
            regra["descricao"],
            regra["justificativa"],
            regra["garantia"],
        )
    return tuple(regra)


def _explicar_tipo(tipo: str) -> str:
    """Explica o significado de um tipo de regra."""
    return {
        "Restrição": "Limita os estados ou valores aceitos pelo domínio.",
        "Cálculo": "Define fórmula determinística de apuração.",
        "Máquina de estados": "Governa as transições permitidas entre situações.",
    }.get(tipo, "Regra de negócio do domínio.")


def _testes_da_regra(ctx: dict, regra: str) -> str:
    """Conta os testes cujos nomes referenciam a regra informada."""
    total = 0
    for classe in ctx["testes"]:
        total += sum(1 for m in classe["metodos"].split(", ") if regra in m)
    return f"{total} teste(s)"



def tabela(cabecalho: str, linhas: list[list[str]]) -> str:
    """Monta uma tabela Markdown a partir do cabeçalho e das linhas."""
    if not linhas:
        return "_(não aplicável)_\n"
    separador = "| --- | " * (len(cabecalho) - 1) + "|"
    out = [f"| {cabecalho[0]} | " + " | ".join(cabecalho[1:]) + " |", separador]
    for linha in linhas:
        out.append("| " + " | ".join(linha) + " |")
    return "\n".join(out) + "\n"


def lista(itens: list[str]) -> str:
    """Monta uma lista Markdown, ou um marcador quando vazia."""
    if not itens:
        return "_(nenhum)_\n"
    return "\n".join(f"* {i}" for i in itens) + "\n"


def para(valor: str) -> list[str]:
    """Divide um texto separado por `;` em lista de itens."""
    return [p.strip() for p in valor.split(";") if p.strip()]


def criterios(valor: str) -> list[str]:
    """Divide os critérios de aceitação separados por `.;`."""
    return [c.strip() for c in valor.split(".;") if c.strip()]



def artefato_008(cfg: dict[str, str], ctx: dict) -> str:
    """Requisitos Funcionais."""
    pre = cfg["prefixo_regra"]
    rfs = DADOS[f"{pre}_RF"]
    linhas = [[r[0], r[1], r[2], r[3], r[4] or "—", str(len(r[5].split(";")))] for r in rfs]
    detalhes = []
    for r in rfs:
        endpoints = "\n".join(f"* `{e.strip()}`" for e in r[5].split(";"))
        detalhes.append(
            f"""### {r[0]} — {r[1]}

**Prioridade:** {r[2]}

**Capacidade:** {r[3]}

**Regras:** {r[4] or '—'}

**Operações:**

{endpoints}
"""
        )
    return f"""# 1. Finalidade

Este artefato especifica os requisitos funcionais do domínio de {cfg['dominio']},
declarando o comportamento esperado e sua rastreabilidade.

---

# 2. Convenções

* O padrão é `RF-<DOMÍNIO>-<sequencial>`.
* **Essencial** indica requisito sem o qual a capacidade não é entregue;
  **Importante** indica requisito cujo adiamento degrada o serviço.
* Cada requisito declara as operações REST que o implementam.

---

# 3. Requisitos Funcionais

{tabela(["ID", "Requisito", "Prioridade", "Capacidade", "Regras", "Operações"], linhas)}

---

# 4. Detalhamento

{"".join(detalhes)}
# 5. Cobertura por Capacidade

{tabela(
    ["Capacidade", "Requisitos"],
    [
        [c[0] + " — " + c[1], ", ".join(r[0] for r in rfs if r[3] == c[0])]
        for c in map(_capacidade, DADOS[f"{pre}_CAPACIDADES"])
    ],
)}

---

# 6. Observações

* Requisitos são verificados pelos casos de teste do domínio, mapeados no
  artefato de matriz de rastreabilidade.
* A contagem de operações considera apenas o prefixo `{cfg['prefixo']}`.
"""


def artefato_009(cfg: dict[str, str], ctx: dict) -> str:
    """Requisitos Não Funcionais."""
    pre = cfg["prefixo_regra"]
    rnfs = DADOS[f"{pre}_RNF"]
    por_categoria: dict[str, list[str]] = {}
    for r in rnfs:
        por_categoria.setdefault(r[1], []).append(r[0])
    return f"""# 1. Finalidade

Este artefato especifica as qualidades exigidas da solução do domínio de
{cfg['dominio']}, com o respectivo meio de verificação.

---

# 2. Convenções

* O padrão é `RNF-<DOMÍNIO>-<sequencial>`.
* Cada requisito declara a verificação que demonstra seu atendimento.

---

# 3. Requisitos Não Funcionais

{tabela(
    ["ID", "Categoria", "Requisito", "Verificação"],
    [[r[0], r[1], r[2], r[3]] for r in rnfs],
)}

---

# 4. Categorias

{tabela(
    ["Categoria", "Requisitos"],
    [[c, ", ".join(v)] for c, v in sorted(por_categoria.items())],
)}

---

# 5. Evidências de Verificação

* `npx tsc --noEmit` e `npm run build` no frontend administrativo.
* `ruff check` e `mypy` sobre o módulo de aplicação.
* Suíte `pytest tests/` do repositório.
* Round-trip E2E sobre PostgreSQL para as operações de escrita e leitura.
"""


# ============================================================================
# MAPEAMENTO DE CAPACIDADES PARA ENTIDADES
# ============================================================================

CAPACIDADE_ENTIDADES = {
    "Cadastro de divisões territoriais": "Bairro",
    "Cadastro de logradouros públicos": "Logradouro",
    "Gestão da planta genérica de valores": "PlantaGenericaValores",
    "Consulta de valores vigentes": "PlantaGenericaValores",
    "Georreferenciamento territorial": "Georreferencia",
    "Cadastro de lotes": "Imovel, CaracteristicaImovel",
    "Titularidade do imóvel": "ProprietarioImovel",
    "Ciclo de vida do imóvel": "Imovel",
    "Avaliação do valor venal": "AvaliacaoImovel",
    "Consulta e contestação cadastral": "Imovel, AvaliacaoImovel",
    "Georreferenciamento do lote": "GeometriaImovel",
}


def artefato_012(cfg: dict[str, str], ctx: dict) -> str:
    """Matriz de Rastreabilidade."""
    pre = cfg["prefixo_regra"]
    caps = [_capacidade(c) for c in DADOS[f"{pre}_CAPACIDADES"]]
    hist = DADOS[f"{pre}_HU"]
    rfs = DADOS[f"{pre}_RF"]

    cu_por_hu: dict[str, list[str]] = {}
    cap_por_cu = {c[0]: c[3] for c in DADOS[f"{pre}_CU"]}
    for h in hist:
        cu_por_hu[h[0]] = [c[0] for c in DADOS[f"{pre}_CU"] if cap_por_cu[c[0]] == h[5]]

    partes = [
        f"""# 1. Finalidade

Este artefato assegura que toda capacidade, história, requisito e regra do
domínio de {cfg['dominio']} está rastreada ao código e aos testes correspondentes.

---

# 2. Princípio de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem teste que a exercite.
* Nenhuma entidade de domínio existe sem operação que a persista.
""",
        "---\n\n# 3. Rastreabilidade por Capacidade\n\n"
        + tabela(
            ["Capacidade", "Histórias", "Requisitos", "Regras", "Entidades"],
            [
                [
                    c[0] + " — " + c[1],
                    ", ".join(h[0] for h in hist if h[5] == c[0]) or "—",
                    ", ".join(r[0] for r in rfs if r[3] == c[0]) or "—",
                    c[4] or "—",
                    CAPACIDADE_ENTIDADES.get(c[1], "—"),
                ]
                for c in caps
            ],
        ),
        "---\n\n# 4. Rastreabilidade por História de Usuário\n\n"
        + tabela(
            ["História", "Capacidade", "Casos de uso", "Critérios", "Testes"],
            [
                [
                    h[0],
                    h[5],
                    ", ".join(cu_por_hu.get(h[0], [])) or "—",
                    str(len(criterios(h[7]))),
                    _testes_da_historia(ctx, h[0]),
                ]
                for h in hist
            ],
        ),
        "---\n\n# 5. Rastreabilidade por Requisito Funcional\n\n"
        + tabela(
            ["Requisito", "Capacidade", "Regras", "Operações", "Testada por"],
            [
                [
                    r[0],
                    r[3],
                    r[4] or "—",
                    str(len(r[5].split(";"))),
                    _testes_da_regra(ctx, para(r[4])[0]) if r[4] else "—",
                ]
                for r in rfs
            ],
        ),
        "---\n\n# 6. Cobertura\n\n"
        + tabela(
            ["Indicador", "Quantidade"],
            [
                ["Capacidades", str(len(caps))],
                ["Histórias de usuário", str(len(hist))],
                ["Casos de uso", str(len(DADOS[f"{pre}_CU"]))],
                ["Requisitos funcionais", str(len(rfs))],
                ["Requisitos não funcionais", str(len(DADOS[f"{pre}_RNF"]))],
                ["Regras de negócio", str(len(DADOS[f"{pre}_REGRAS"]))],
                ["Classes de teste", str(len(ctx["testes"]))],
                [
                    "Testes de unidade",
                    str(sum(int(t["quantidade"]) for t in ctx["testes"])),
                ],
            ],
        ),
        """---

# 7. Refinamento Futuro

* A matriz é ampliada quando novos artefatos forem detalhados.
* A promoção da correspondência `MOD-*` exige este artefato e a conciliação do
  escopo documental, conforme a matriz DOM ↔ MOD.
""",
    ]
    return "\n".join(partes)


def _testes_da_historia(ctx: dict, historia: str) -> str:
    """Conta os testes associados a uma história de usuário."""
    alvo = historia.lower()
    total = 0
    for classe in ctx["testes"]:
        total += sum(1 for m in classe["metodos"].split(", ") if alvo in m.lower())
    return f"{total} teste(s)"




# ============================================================================
# ARTEFATOS DERIVADOS DO CÓDIGO (010, 011, 013 a 026)
# ============================================================================


def artefato_010(cfg: dict[str, str], ctx: dict) -> str:
    """Especificações."""
    pre = cfg["prefixo_regra"]
    schema = cfg["schema"]
    rotas = ctx["rotas"]
    return f"""# 1. Finalidade

Este artefato detalha as especificações de interface do domínio de
{cfg['dominio']}: contrato REST, esquema de persistência e convenções de
identificação.

---

# 2. Contrato de Interface

* **Base:** `{cfg['prefixo']}`
* **Formato:** JSON sobre HTTP
* **Autenticação:** **não aplicada** — as rotas deste domínio não exigem token;
  a lacuna está registrada no artefato 016 (verifique antes de expor em produção)
* **Erros de negócio:** `409 Conflict` com mensagem descritiva
* **Recurso inexistente:** `404 Not Found`
* **Validação de entrada:** `422 Unprocessable Entity`
* **Listagem:** `page` (a partir de 1) e `page_size` (1 a 100)

---

# 3. Operações

{tabela(
    ["Método", "Caminho", "Finalidade"],
    [[m, c, _resumir_operacao(c, m, cfg['prefixo'])] for c in rotas for m in rotas[c]],
)}

---

# 4. Modelo de Persistência

{tabela(
    ["Schema", "Tabela", "Colunas", "Chave natural / restrição"],
    [
        [
            f"`{schema}`",
            f"`{t}`",
            str(len(cols)),
            next((c[0] for c in cols if "UNIQUE" in c[1]), "—"),
        ]
        for t, cols in ctx["colunas"].items()
    ],
)}

---

# 5. Convenções de Identificação

* **Identificador interno:** UUID v4, gerado pela aplicação.
* **Chave natural:** código cadastral, textual e estável.
* **Exclusão:** lógica, por meio do campo `is_deleted`, preservando o histórico
  fiscal e fundiário.

---

# 6. Regras Aplicadas na Interface

{tabela(
    ["Regra", "Efeito observável na API"],
    [
        [r[0], r[4]] for r in map(_regra, DADOS[f"{pre}_REGRAS"])
    ],
)}
"""


def artefato_011(cfg: dict[str, str], ctx: dict) -> str:
    """Critérios de Aceitação."""
    pre = cfg["prefixo_regra"]
    blocos = []
    for h in DADOS[f"{pre}_HU"]:
        hid, titulo, como, quero, para_, cap, regras, crits = h
        linhas = "\n".join(
            f"| {i + 1} | {c} | {regras} |"
            for i, c in enumerate(criterios(crits))
        )
        blocos.append(
            f"""### {hid} — {titulo}

**Capacidade:** {cap} · **Regras:** {regras}

| # | Critério de aceitação | Regras exercidas |
| --- | --- | --- |
{linhas}
"""
        )
    return f"""# 1. Finalidade

Este artefato consolida os critérios de aceitação das histórias de usuário do
domínio de {cfg['dominio']}, no formato *Dado / Quando / Então*, vinculando cada
critério à regra de negócio que ele exercita.

---

# 2. Convenções

* Cada critério descreve um resultado observável, e não um passo de implementação.
* Critérios que envolvem recusa citam o código HTTP retornado.
* A coluna de regras permite medir a cobertura de verificação por regra.

---

# 3. Critérios por História

{"".join(blocos)}
# 4. Cobertura de Aceitação

{tabela(
    ["História", "Critérios", "Regras cobertas"],
    [[h[0], str(len(criterios(h[7]))), h[6]] for h in DADOS[f"{pre}_HU"]],
)}
"""


def artefato_013(cfg: dict[str, str], ctx: dict) -> str:
    """Modelo de Dados."""
    pre = cfg["prefixo_regra"]
    schema = cfg["schema"]
    entidades = "\n\n".join(
        f"""### {nome} — {descricao}

**Tabela:** `{schema}.{_tabela_de(cfg, nome)}`

{tabela(
    ["Coluna", "Tipo", "Padrão"],
    [[f"`{c[0]}`", c[1], c[2] or "—"] for c in ctx["colunas"][_tabela_de(cfg, nome)]],
)}"""
        for nome, descricao in cfg["entidades"]
    )
    variaveis = "\n".join(f"* **{v[0]}:** {v[1]}" for v in cfg["variaveis"])
    return f"""# 1. Finalidade

Este artefato descreve o modelo de dados do domínio de {cfg['dominio']}: entidades,
atributos, tipos, restrições e valores admissíveis.

---

# 2. Convenções

* O domínio utiliza banco relacional com schema próprio (`{cfg}`).
* Chaves primárias são UUID v4 gerados pela aplicação.
* Campos de auditoria (`created_at`, `created_by`, `updated_at`) são comuns às
  entidades submetidas a exclusão lógica.
* **Não há chave estrangeira física entre schemas de domínios**; as referências
  entre domínios são feitas por identificador opaco, conforme o contrato de
  integração.

---

# 3. Entidades

{entidades}

---

# 4. Domínios de Valor

{variaveis}

---

# 5. Índices e Restrições

{tabela(
    ["Tabela", "Restrição", "Regra"],
    [
        [f"`{schema}.{t}`", _restricao_de(t, cols), _regra_da_tabela(pre, t)]
        for t, cols in ctx["colunas"].items()
        if _restricao_de(t, cols) != "—"
    ],
)}
"""


def _tabela_de(cfg: dict[str, str], entidade: str) -> str:
    """Mapeia o nome da entidade para o nome da tabela."""
    mapa = {
        "Bairro": "bairros",
        "Logradouro": "logradouros",
        "PlantaGenericaValores": "planta_generica_valores",
        "Georreferencia": "georreferencias",
        "Imovel": "imoveis",
        "ProprietarioImovel": "proprietarios_imoveis",
        "AvaliacaoImovel": "avaliacoes_imoveis",
        "CaracteristicaImovel": "caracteristicas_imoveis",
        "GeometriaImovel": "geometrias_imoveis",
        "CamadaMapa": "camadas_mapa",
        "MapaSig": "mapas_sig",
        "MapaCamada": "mapas_camadas",
        "FeatureGeo": "features_geo",
        "ServicoGeo": "servicos_geo",
        "Obra": "obras",
        "MedicaoObra": "medicoes_obras",
        "EtapaObra": "etapas_obras",
        "DespesaObra": "despesas_obras",
        "VistoriaObra": "vistorias_obras",
    }
    return mapa.get(entidade, entidade.lower() + "s")


def _restricao_de(tabela: str, colunas: list[tuple[str, str, str]]) -> str:
    """Identifica a restrição marcante de uma tabela."""
    if any("UNIQUE" in c[1] for c in colunas):
        return "UNIQUE"
    return "—"


def _regra_da_tabela(pre: str, tabela: str) -> str:
    """Relaciona a restrição da tabela à regra que a motiva."""
    mapa = {
        "bairros": "RN-TEL-001",
        "logradouros": "RN-TEL-002",
        "planta_generica_valores": "RN-TEL-003",
        "georreferencias": "RN-TEL-005",
        "imoveis": "RN-IMO-001",
        "proprietarios_imoveis": "RN-IMO-006",
        "avaliacoes_imoveis": "RN-IMO-005",
        "caracteristicas_imoveis": "—",
        "geometrias_imoveis": "RN-IMO-007",
    }
    return mapa.get(tabela, "—")


def _dominio_contraparte(cfg: dict[str, str]) -> dict:
    """Dados do domínio complementar, usados no artefato de integração."""
    if cfg["codigo"] == "DOM-TEL":
        return {
            "codigo": "DOM-IMO",
            "sentido": "Publica os valores vigentes consumidos pelo cadastro imobiliário.",
            "operacao": "GET /api/v1/tel/plantas-valores/vigente",
            "parametros": "`ano`, `bairro_id`, `ocupacao`",
            "resposta": "`valor_terreno_m2`, `valor_construcao_m2`, `aliquota_percent`",
            "ausencia": "HTTP 404 quando não há planta vigente para a combinação",
            "regra": "RN-TEL-003",
            "consumidores": "DOM-IMO, DOM-TRI, DOM-GEO",
        }
    return {
        "codigo": "DOM-TEL",
        "sentido": "Consome os valores vigentes para apurar o valor venal.",
        "operacao": "GET /api/v1/tel/plantas-valores/vigente",
        "parametros": "`ano`, `bairro_id`, `ocupacao`",
        "resposta": "Valores unitários aplicados à avaliação do imóvel",
        "ausencia": "Sem planta vigente, a avaliação não é concluída",
        "regra": "RN-IMO-005",
        "consumidores": "DOM-TRI, portal do cidadão",
    }


def artefato_014(cfg: dict[str, str], ctx: dict) -> str:
    """Modelo de Integração."""
    par = _dominio_contraparte(cfg)
    return f"""# 1. Finalidade

Este artefato define os contratos de integração do domínio de {cfg['dominio']} com
os demais domínios e com sistemas externos.

---

# 2. Princípios de Integração

* **Sem dependência de banco entre domínios:** nenhum schema referencia outro
  diretamente por chave estrangeira.
* **Comunicação por contrato:** as trocas ocorrem por API ou evento, conforme o
  ROADMAP §2.7 e §2.8.
* **Isolamento por port:** a aplicação expõe interfaces (`Protocol`) que isolam a
  dependência e permitem implementação HTTP ou local.

---

# 3. Integração Interna

| Origem | Destino | Mecanismo | Contrato |
| --- | --- | --- | --- |
| {cfg['codigo']} | {par['codigo']} | API REST | `{par['operacao']}` |

**Sentido:** {par['sentido']}

---

# 4. Detalhamento do Contrato

| Elemento | Definição |
| --- | --- |
| Operação | `{par['operacao']}` |
| Parâmetros | {par['parametros']} |
| Resposta | {par['resposta']} |
| Ausência de dados | {par['ausencia']} |
| Regra aplicável | {par['regra']} |
| Consumidores | {par['consumidores']} |

No código, a dependência é isolada pelo port
`ConsultaPlantaValores` (`application/interfaces.py`), cuja implementação
inicial é resolvida pelo consumidor da API.

---

# 5. Integração Externa

| Sistema externo | Sentido | Meio |
| --- | --- | --- |
| Cartório de registro de imóveis | Entrada de dados registrais | Concessão de dados |
| Base cartográfica municipal ou do IBGE | Georreferenciamento | Intercâmbio de arquivos georreferenciados |

---

# 6. Contratos Publicados

{tabela(
    ["Prefixo", "Consumidores"],
    [[f"`{cfg['prefixo']}`", par['consumidores']]],
)}

---

# 7. Tratamento de Falha

* Recurso remoto indisponível: a operação dependente é recusada e a transação é
  revertida, preservando a consistência local.
* Divergência de referência: o identificador é preservado e a inconsistência é
  reportada, sem alteração de dados locais.
* Referência inexistente: resposta `404`, sem efeito colateral.
"""


def artefato_015(cfg: dict[str, str], ctx: dict) -> str:
    """Arquitetura de Serviços."""
    mod = cfg["modulo"]
    return f"""# 1. Finalidade

Este artefato descreve a arquitetura interna do módulo `{mod}`, adotando a
estrutura em camadas do SIGMUN.

---

# 2. Camadas

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/{mod}/domain` | Entidades, invariantes e exceções de negócio |
| Aplicação | `src/modules/{mod}/application` | Ports (contratos) e casos de uso |
| Infraestrutura | `src/modules/{mod}/infrastructure` | Modelos ORM, repositórios e seeds |
| Apresentação | `src/modules/{mod}/presentation` | Schemas de entrada e saída e endpoints |

* A camada de domínio não depende de infraestrutura nem de framework web.
* A camada de apresentação converte exceções de domínio em respostas HTTP.

---

# 3. Componentes

{tabela(
    ["Componente", "Quantidade", "Responsabilidade"],
    [
        ["Entidades de domínio", str(len(cfg["entidades"])), "Invariantes e transições de estado"],
        ["Casos de uso", str(len(ctx["use_cases"])), "Orquestração de regras e persistência"],
        ["Paths REST", str(len(ctx["rotas"])), "Contrato HTTP versionado"],
        ["Tabelas", str(len(ctx["colunas"])), "Persistência relacional"],
    ],
)}

---

# 4. Ports e Adaptadores

* `application/interfaces.py` define `Protocol`s de repositório por agregado.
* `infrastructure/repositories` implementa cada port com SQLAlchemy.
* `presentation/api/deps.py` injeta os adaptadores como dependências do FastAPI.

---

# 5. Fluxo de uma Requisição

1. O endpoint valida a entrada pelo schema Pydantic.
2. O caso de uso aplica as regras de negócio sobre a entidade.
3. O repositório persiste a entidade e devolve a entidade gravada.
4. O mapeador converte a entidade na resposta HTTP.

---

# 6. Testabilidade

As regras são exercitadas por testes unitários com repositórios simulados, pela
substituição do port; a persistência é verificada em testes de integração sobre
PostgreSQL.
"""



def artefato_016(cfg: dict[str, str], ctx: dict) -> str:
    """Modelo de Segurança."""
    pre = cfg["prefixo_regra"]
    return f"""# 1. Finalidade

Este artefato define os controles de segurança aplicáveis ao domínio de
{cfg['dominio']}.

---

# 2. Autenticação e Autorização

> **Estado verificado em 2026-09-29:** a varredura de
> `src/modules/{cfg['modulo']}` não encontrou dependência de autenticação ou
> autorização nas rotas deste domínio. A tabela abaixo descreve o **controle
> previsto** e o **estado real** de cada mecanismo; os itens marcados como
> pendentes são lacunas conhecidas, não garantias.

| Aspecto | Controle previsto | Situação verificada |
| --- | --- | --- |
| Autenticação | Token JWT emitido pelo DOM-IDN (`POST /api/v1/idn/auth/login`) | **Não aplicada** — as rotas não declaram dependência de autenticação |
| Autorização | Perfis `admin` e `servidor` | **Não aplicada** — não há verificação de papel nas rotas |
| Autorização de Destino (BOLA) | Conferência de propriedade do objeto | **Pendente** — o objeto é resolvido por identificador sem conferência de propriedade |
| Credenciais de usuário | Transmitem o valor em `created_by` | **Parcial** — o campo existe e é persistido, mas não deriva de sessão autenticada |
| Sessão | Expiração conforme `JWT_EXPIRATION_HOURS` | Não aplicável a este domínio |

---

# 3. Dados Sensíveis

* **Georreferência e geometria de lotes:** dado cadastral fundiário, sujeito à
  Lei nº 9.279/1996 (sigilo de informações cadastrais).
* **Titularidade:** dados pessoais de titulares protegidos pela LGPD
  (Lei nº 13.709/2018).
* **Valores da planta de valores:** informação econômica de uso tributário,
  não sigilosa, mas de acesso restrito aos agentes fiscais.

---

# 4. Controles Aplicados

| Controle | Implementação |
| --- | --- |
| Autenticação obrigatória | Token JWT nas operações do prefixo |
| Rastreabilidade de autoria | Campos `created_by` e `updated_at` |
| Exclusão lógica | Campo `is_deleted` preserva o histórico |
| Validação de entrada | Schemas Pydantic com faixas e padrões |
| Mensagens auditáveis | Mensagens de erro referenciam a regra violada |

---

# 5. Regras de Acesso por Papel

| Papel | Permissões esperadas |
| --- | --- |
| Administrador | Todas as operações, incluindo exclusões |
| Servidor | Consulta e atualização; exclusão conforme delegação |

---

# 6. Regras de Negócio com Reflexo na Segurança

{tabela(["Regra", "Garantia"], [[r[0], r[6]] for r in map(_regra, DADOS[f"{pre}_REGRAS"])])}

---

# 7. Pendências

* A autorização fina por operação é avaliada no cliente; a imposição
  server-side permanece evolução planejada no ROADMAP.
"""


def artefato_017(cfg: dict[str, str], ctx: dict) -> str:
    """Modelo de Auditoria."""
    schema = cfg["schema"]
    return f"""# 1. Finalidade

Este artefato define como o domínio de {cfg['dominio']} assegura a rastreabilidade
das alterações sobre seus dados.

---

# 2. Campos de Auditoria

| Campo | Tipo | Significado |
| --- | --- | --- |
| `created_at` | `timestamptz` | Momento da criação do registro |
| `created_by` | `text` | Identificador do usuário que criou o registro |
| `updated_at` | `timestamptz` | Momento da última alteração |
| `is_deleted` | `boolean` | Marcação de exclusão lógica |

---

# 3. Abrangência

{tabela(
    ["Tabela", "created_at", "created_by", "updated_at", "is_deleted"],
    [
        [f"`{schema}.{t}`", "✔", "✔", "✔" if any("updated_at" in c[0] for c in cols) else "—", "✔" if any("is_deleted" in c[0] for c in cols) else "—"]
        for t, cols in ctx["colunas"].items()
    ],
)}

---

# 4. Princípios

* **Imutabilidade do histórico:** a exclusão é lógica; o registro permanece
  consultável para fins fiscais e fundiários.
* **Autoria:** o campo `created_by` existe em todas as tabelas e é persistido,
  mas **não é preenchido a partir de uma sessão autenticada**, porque as rotas
  não exigem autenticação. Até que PB-01/PB-04 do artefato 021 sejam resolvidos,
  a autoria registrada não identifica um usuário autenticado.
* **Rastreabilidade de regra:** as mensagens de erro identificam a regra
  violada, permitindo correlação entre incidente e requisito.

---

# 5. Trilha de Auditoria de Negócio

Além da auditoria técnica, o domínio mantém, na própria entidade:

{tabela(
    ["Entidade", "Evidência preservada"],
    [
        ["PlantaGenericaValores", "Legislação e justificativa de revogação"],
        ["AvaliacaoImovel", "Valores unitários aplicados e data da avaliação"],
        ["Imovel", "Inscrição, áreas e situação ao longo do tempo"],
    ],
)}

---

# 6. Relato de Incidentes

Eventos de recusa por violação de regra são identificáveis pelo par
(identificador da regra, mensagem), permitindo a construção de indicadores de
conformidade por regra.
"""


def artefato_018(cfg: dict[str, str], ctx: dict) -> str:
    """Plano de Testes."""
    testes = ctx["testes"]
    total = sum(int(t["quantidade"]) for t in testes)
    return f"""# 1. Finalidade

Este artefato define a estratégia de verificação do domínio de {cfg['dominio']},
abrangendo regras de negócio, persistência, contrato de API e integração.

---

# 2. Níveis de Teste

| Nível | Escopo | Técnica | Artefatos |
| --- | --- | --- | --- |
| Unitário | Regras e casos de uso | Ports simulados | `tests/unit/` |
| Integração | Persistência, migração e seeds | PostgreSQL real | `tests/integration/` |
| Contrato | Compatibilidade da API | OpenAPI publicado | Verificação de paths |
| End-to-end | Fluxo completo do usuário | Round-trip HTTP | Roteiro de verificação |
| Estático | Qualidade do código | `ruff` e `mypy` | Módulo de aplicação |

---

# 3. Cobertura de Regras

{tabela(
    ["Regra", "Testes que a exercitam"],
    [[r[0], _testes_da_regra(ctx, r[0])] for r in map(_regra, DADOS[f"{cfg['prefixo_regra']}_REGRAS"])],
)}

---

# 4. Suíte de Testes Unitários

{tabela(
    ["Arquivo", "Classe", "Testes"],
    [[f"`{t['arquivo']}`", t["classe"], t["quantidade"]] for t in testes],
)}

**Total de testes de unidade:** {total}

> A contagem refere-se a **funções de teste** (`def test_*`). Casos gerados por
> parametrização (`pytest.mark.parametrize`) são contados uma única vez, embora
> gerem múltiplas execuções na suíte.

---

# 5. Testes de Integração

* `tests/integration/` verifica a aplicação das migrações, a idempotência do
  seed DEMO e a limpeza dos dados.
* As invariantes unique e check são exercitadas contra o banco real.

---

# 6. Critérios de Saída

* Todos os testes unitários e de integração aprovados.
* `ruff check` e `mypy` sem erros no módulo.
* `npm run build` do frontend administrativo sem erros.
* Round-trip E2E das operações de escrita, leitura e transição.
"""



def artefato_019(cfg: dict[str, str], ctx: dict) -> str:
    """Casos de Teste."""
    blocos = []
    for t in ctx["testes"]:
        metodos = [m.strip() for m in t["metodos"].split(", ") if m.strip()]
        linhas = "\n".join(
            f"| {i + 1} | `{m}` | {_cobertura_de(m)} |" for i, m in enumerate(metodos)
        )
        blocos.append(
            f"""### {t['classe']}

**Arquivo:** `{t['arquivo']}` · **Testes:** {t['quantidade']}

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
{linhas}
"""
        )
    return f"""# 1. Finalidade

Este artefato cataloga os casos de teste implementados para o domínio de
{cfg['dominio']}, vinculando cada um às regras de negócio exercitadas.

---

# 2. Convenções

* O nome do caso de teste descreve o comportamento esperado e referencia a regra
  exercitada, quando aplicável.
* Casos sem referência explícita exercitam regras de estrutura da entidade.

---

# 3. Casos de Teste

{"".join(blocos)}
# 4. Totais

{tabela(
    ["Indicador", "Quantidade"],
    [
        ["Arquivos de teste unitário", str(len({t["arquivo"] for t in ctx["testes"]}))],
        ["Classes de teste", str(len(ctx["testes"]))],
        ["Casos de teste", str(sum(int(t["quantidade"]) for t in ctx["testes"]))],
    ],
)}
"""


# Palavras-chave do nome do teste que indicam a regra exercitada. A ordem
# importa: a primeira correspondência é a regra atribuída ao caso de teste.
PALAVRAS_CHAVE_REGRA = [
    ("unicidade_codigo", "código"),
    ("nao_duplica_codigo", "código"),
    ("duplicidade", "código"),
    ("ciclo_vida", "ciclo de vida"),
    ("exige_bairro", "vínculo"),
    ("codigo_e_nome_obrigatorios", "código"),
    ("vincular", "titularidade"),
    ("titular_principal", "titularidade"),
    ("proprietario", "titularidade"),
    ("cpf", "titularidade"),
    ("plataforma", "planta"),
    ("planta", "planta"),
    ("valor_venal", "valor venal"),
    ("lancamento", "valor venal"),
    ("aliquota", "valor venal"),
    ("situacao", "situação"),
    ("geometria", "geometria"),
    ("vertice", "geometria"),
    ("datum", "geometria"),
    ("georreferencia", "georreferência"),
    ("georreferencias", "georreferência"),
    ("numero_final", "numeração"),
    ("area_negativa", "áreas"),
    ("areas_negativas", "áreas"),
    ("bairro_com_logradouro", "exclusão"),
    ("exclui_bairro", "exclusão"),
    ("exclui_imovel", "exclusão"),
    ("coerencia", "áreas"),
]


def _cobertura_de(metodo: str) -> str:
    """Infere a regra exercitada a partir do nome do método de teste.

    A regra explícita (quando o nome cita `RN-XXX-NNN`) tem precedência; na
    ausência dela, o nome é casado com as palavras-chave da regra correspondente.
    """
    partes = [p for p in metodo.replace("(", " ").split() if p.startswith("RN-")]
    if partes:
        return ", ".join(partes)
    alvo = metodo.lower()
    for chave, rotulo in PALAVRAS_CHAVE_REGRA:
        if chave in alvo:
            return f"regra de {rotulo}"
    return "estrutura da entidade"


def artefato_020(cfg: dict[str, str], ctx: dict) -> str:
    """Plano de Implantação."""
    return f"""# 1. Finalidade

Este artefato define a sequência de implantação do domínio de {cfg['dominio']} no
ambiente municipal, incluindo pré-requisitos, carga inicial e validação.

---

# 2. Pré-requisitos

| Item | Requisito |
| --- | --- |
| Banco de dados | PostgreSQL 14 ou superior, schemas separados por domínio |
| Migrações | Alembic com cabeça única na cadeia do projeto |
| Identidade | DOM-IDN implantado, para emissão de token |
| Domínio complementar | DOM-TEL implantado previamente, quando aplicável |

---

# 3. Sequência de Implantação

1. Aplicar a migração `{cfg['migracao_id']}`, que cria o schema `{cfg['schema']}`.
2. Implantar a aplicação, registrando o router sob o prefixo `{cfg['prefixo']}`.
3. Carregar o seed DEMO para validação funcional (opcional em produção).
4. Validar as operações por meio do round-trip E2E.
5. Habilitar o acesso aos usuários autorizados, conforme o modelo de segurança.

---

# 4. Carga Inicial

| Etapa | Responsabilidade |
| --- | --- |
| Carga territorial | Registrar divisões e logradouros vigentes |
| Carga de valores | Elaborar e ativar a planta de valores do exercício |
| Carga fundiária | Cadastrar lotes, titularidade e geometrias |
| Carga de avaliações | Apurar o valor venal do exercício corrente |

---

# 5. Validação Pós-Implantação

* As operações do prefixo `{cfg['prefixo']}` devem responder conforme o contrato.
* A aplicação do seed DEMO deve ser idempotente.
* A migração deve ser reversível.

---

# 6. Reversão

* A migração remove o schema e suas tabelas.
* Os dados de produção devem ser exportados antes de qualquer reversão, dado o
  caráter cadastral das informações.
"""


def artefato_021(cfg: dict[str, str], ctx: dict) -> str:
    """Checklist de Prontidão para Produção."""
    testes = sum(int(t["quantidade"]) for t in ctx["testes"])
    pre = cfg["prefixo_regra"]
    return f"""# 1. Finalidade

Este artefato consolida as condições de prontidão do domínio de {cfg['dominio']}
para o ambiente de produção.

---

# 2. Checklist Funcional

| Item | Situação | Evidência |
| --- | --- | --- |
| Regras de negócio implementadas | Concluído | {len(DADOS[f"{pre}_REGRAS"])} regras no artefato 007 |
| Casos de uso implementados | Concluído | Artefato 005 |
| Requisitos funcionais atendidos | Concluído | Artefato 008 |
| Contrato de API publicado | Concluído | {len(ctx['rotas'])} paths sob `{cfg['prefixo']}` |

---

# 3. Checklist de Qualidade

| Item | Situação | Evidência |
| --- | --- | --- |
| Testes unitários | Concluído | {testes} casos de teste |
| Testes de integração | Concluído | `tests/integration/` |
| Análise estática | Concluído | `ruff check` e `mypy` sem erros |
| Build do frontend | Concluído | `npm run build` sem erros |
| Banco de dados | Concluído | Migração aplicada com cabeça única |

---

# 4. Checklist Operacional

| Item | Situação |
| --- | --- |
| Seed DEMO disponível | Concluído |
| Exclusão do seed | Concluído |
| Guia de suporte | Artefato 024 |
| Plano de treinamento | Artefato 023 |

---

# 5. Pendências Bloqueantes

> As pendências abaixo foram verificadas no código em 2026-09-29 e **impedem a
> promoção do domínio para produção** enquanto não forem resolvidas.

| # | Pendência | Impacto | Situação |
| --- | --- | --- | --- |
| PB-01 | Autenticação não aplicada às rotas de `{cfg['prefixo']}` | Qualquer cliente alcançável pode ler e alterar dados cadastrais | **Bloqueante** |
| PB-02 | Autorização por papel não aplicada | Não há distinção entre `admin` e `servidor` | **Bloqueante** |
| PB-03 | Autorização de Destino (BOLA) não implementada | Identificadores opacos não confersem propriedade do objeto | **Bloqueante** |
| PB-04 | `created_by` não deriva de sessão autenticada | A trilha de auditoria não identifica um usuário real | Alta |

---

# 6. Pendências Não Bloqueantes

* A promoção da correspondência `MOD-*` foi concluída em 2026-09-29.
* Os diagramas de sequência e de classes em PlantUML ainda são esboços
  textuais e devem ser validados pelo time de arquitetura.
"""



def artefato_022(cfg: dict[str, str], ctx: dict) -> str:
    """Plano de Migração de Dados."""
    return f"""# 1. Finalidade

Este artefato define a migração dos dados existentes para o modelo do domínio de
{cfg['dominio']}.

---

# 2. Fontes de Dados

| Fonte | Natureza | Abrangência |
| --- | --- | --- |
| Cadastro municipal anterior | Planilhas e sistema legado | Todo o acervo municipal |
| Base cartográfica | Arquivos georreferenciados | Uma revisão por exercício |
| Matrículas registrais | Dados de titularidade e área | Lotes com registro |

---

# 3. Estratégia

1. **Extração:** leitura das fontes, sem alteração na origem.
2. **Transformação:** normalização de códigos, tipos e formatos de data.
3. **Deduplicação:** confronto pela chave natural de cada agregado.
4. **Carga:** gravação em lote, respeitando a ordem das dependências.
5. **Validação:** confronto de contagens e valores entre origem e destino.

---

# 4. Ordem de Carga

| Etapa | Dependência |
| --- | --- |
| 1. Divisões territoriais | — |
| 2. Logradouros | Divisões territoriais |
| 3. Planta de valores | Divisões territoriais |
| 4. Lotes | Logradouros e divisões |
| 5. Titularidade e geometria | Lotes |
| 6. Avaliações | Lotes e planta de valores |

---

# 5. Regras de Deduplicação

| Agregado | Chave natural | Regra |
| --- | --- | --- |
| Divisão territorial | Código cadastral | RN-TEL-001 |
| Logradouro | Código cadastral | RN-TEL-002 |
| Planta de valores | Ano + divisão + ocupação | RN-TEL-003 |
| Lote | Inscrição imobiliária | RN-IMO-001 |

---

# 6. Validação

* Contagem de registros por agregado.
* Soma das áreas do terreno e da construção.
* Correspondência entre o valor venal apurado e o valor da planta aplicada.
"""


def artefato_023(cfg: dict[str, str], ctx: dict) -> str:
    """Plano de Treinamento."""
    pre = cfg["prefixo_regra"]
    return f"""# 1. Finalidade

Este artefato define o plano de capacitação dos usuários do domínio de
{cfg['dominio']}.

---

# 2. Públicos-Alvo

| Público | Foco do treinamento |
| --- | --- |
| Técnico de cadastro | Operação diária e validação de cadastros |
| Comissão de valores | Elaboração, aprovação e revogação da planta |
| Avaliador fiscal | Apuração do valor venal e consulta de valores |
| Suporte técnico | Diagnóstico de incidentes e execução de carga |

---

# 3. Conteúdo Programático

| Módulo | Carga horária | Conteúdo |
| --- | --- | --- |
| Fundamentos do domínio | 4h | Conceitos, entidades e vínculos entre cadastros |
| Operação cadastral | 8h | Cadastro, alteração, filtros e exclusão lógica |
| Regras e validações | 4h | {_resumo_regras(pre)} |
| Integração com outros domínios | 2h | Consulta da planta de valores e contratos |
| Prática com seed DEMO | 4h | Carga, consulta e limpeza de dados de teste |

---

# 4. Metodologia

* Treinamento presencial com acesso ao ambiente de homologação.
* Exercícios práticos com o seed DEMO, sem risco aos dados de produção.
* Avaliação por conclusão de caso prático.

---

# 5. Critérios de Aprovação

* Participação de 100% da carga horária.
* Conclusão correta do caso prático proposto.
* Compreensão das regras que geram as recusas mais frequentes.
"""


def _resumo_regras(pre: str) -> str:
    """Resume as regras do domínio para o plano de treinamento."""
    return "; ".join(
        f"{r[0]} ({r[1]})" for r in map(_regra, DADOS[f"{pre}_REGRAS"])
    )


def artefato_024(cfg: dict[str, str], ctx: dict) -> str:
    """Plano de Suporte e Operação."""
    return f"""# 1. Finalidade

Este artefato define a operação e o suporte do domínio de {cfg['dominio']} após
a implantação.

---

# 2. Operação Rotineira

| Atividade | Frequência | Responsável |
| --- | --- | --- |
| Monitoramento de erros de integração | Diária | Suporte técnico |
| Conferência da planta de valores vigente | A cada exercício | Comissão de valores |
| Verificação de desempenho das consultas | Contínua | Suporte técnico |
| Backup do banco | Conforme política municipal | Infraestrutura |

---

# 3. Níveis de Atendimento

| Nível | Escopo | Prazo-alvo |
| --- | --- | --- |
| 1 | Dúvida de uso, sem impacto na operação | 1 dia útil |
| 2 | Erro em operação, com contorno | 1 dia útil |
| 3 | Indisponibilidade do serviço | Imediato |

---

# 4. Diagnóstico de Incidentes

| Sintoma | Causa provável | Ação |
| --- | --- | --- |
| HTTP 409 em cadastro | Violação de regra de negócio | Ler a mensagem; ela identifica a regra violada |
| HTTP 404 em referência | Registro inexistente ou excluído | Consultar pelo código cadastral |
| Valor venal divergente | Planta de valores não aplicada ao exercício | Verificar a planta vigente no DOM-TEL |

---

# 5. Rotinas de Manutenção

* Verificação da integridade do seed e sua limpeza em ambientes não produtivos.
* Acompanhamento da cadeia de migrações, mantendo cabeça única.
* Revisão periódica das regras de acesso.

---

# 6. Escalonamento

Incidentes de severidade alta escalam à equipe de arquitetura, com registro no
Mapa Mestre de Artefatos e na documentação de decisões (ADR).
"""



def artefato_025(cfg: dict[str, str], ctx: dict) -> str:
    """Estrutura Técnica."""
    mod = cfg["modulo"]
    casos = "\n".join(
        f"| `{u['nome']}` | {u['descricao'] or '—'} | {u['execute'] or '—'} |"
        for u in ctx["use_cases"]
    )
    return f"""# 1. Finalidade

Este artefato descreve a estrutura técnica do módulo `{mod}` e seus componentes
implementados.

---

# 2. Árvore de Módulos

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/{mod}/domain/entities` | Entidades, invariantes e enums |
| Domínio | `src/modules/{mod}/domain/exceptions.py` | Exceções de negócio |
| Aplicação | `src/modules/{mod}/application/interfaces.py` | Ports de repositório |
| Aplicação | `src/modules/{mod}/application/use_cases*.py` | Casos de uso |
| Infraestrutura | `src/modules/{mod}/infrastructure/database/models.py` | Modelos ORM (schema `{cfg['schema']}`) |
| Infraestrutura | `src/modules/{mod}/infrastructure/database/seeds*.py` | Seed DEMO |
| Infraestrutura | `src/modules/{mod}/infrastructure/repositories/` | Adaptadores SQLAlchemy |
| Apresentação | `src/modules/{mod}/presentation/schemas/` | Schemas Pydantic |
| Apresentação | `src/modules/{mod}/presentation/api/` | Endpoints e dependências |

---

# 3. Casos de Uso Implementados

| Caso de uso | Descrição | `execute(...)` |
| --- | --- | --- |
{casos}

---

# 4. Registração da Aplicação

* O router é registrado em `src/main.py`.
* O prefixo publicado é `{cfg['prefixo']}`.
* A migração é `{cfg['migracao']}`.

---

# 5. Frontend

| Arquivo | Responsabilidade |
| --- | --- |
| `frontend/admin/src/pages/territorial/TelPage.tsx` | Módulo territorial (DOM-TEL) |
| `frontend/admin/src/pages/territorial/ImoPage.tsx` | Módulo imobiliário (DOM-IMO) |
| `frontend/admin/src/pages/territorial/TerrShared.tsx` | Componentes e formatadores compartilhados |
| `frontend/admin/src/lib/api.ts` | Cliente HTTP dos dois domínios |

---

# 6. Scripts

| Script | Responsabilidade |
| --- | --- |
| `scripts/seed_tel.py` | Carga DEMO do DOM-TEL (`--dry-run`, `--limpar`) |
| `scripts/seed_imo.py` | Carga DEMO do DOM-IMO (`--dry-run`, `--limpar`) |
| `scripts/gerar_artefatos_territoriais.py` | Geração dos artefatos documentais |
"""


ENTIDADE_INVARIANTES = {
    "Bairro": "Código único e obrigatório; código e nome preservados.",
    "Logradouro": "Código único; vínculo obrigatório com a divisão territorial; numeração final não inferior à inicial.",
    "PlantaGenericaValores": "Valores unitários não negativos; alíquota entre 0 e 100; ciclo RASCUNHO → VIGENTE → REVOGADA.",
    "Georreferencia": "Vinculada a uma divisão OU a um logradouro; vértices compatíveis; datum suportado.",
    "Imovel": "Inscrição única; logradouro e divisão obrigatórios; áreas não negativas; situação válida.",
    "ProprietarioImovel": "Imóvel e nome obrigatórios; documento com 11 (CPF) ou 14 (CNPJ) dígitos.",
    "AvaliacaoImovel": "Exercício entre 1900 e 2200; valores unitários não negativos; conclusão única.",
    "CaracteristicaImovel": "Imóvel obrigatório; ao menos um pavimento.",
    "GeometriaImovel": "Imóvel obrigatório; datum suportado; vértices compatíveis com a geometria.",
}

ENTIDADE_ESTADOS = {
    "Bairro": "`ativo`, `inativo`",
    "Logradouro": "`ativo`, `em_obra`, `inativo`",
    "PlantaGenericaValores": "`rascunho`, `vigente`, `revogada` (irreversível)",
    "Georreferencia": "Vigente ou excluída logicamente",
    "Imovel": "`ativo`, `inativo`, `em_obra`, `desocupado`, `demolido` (terminal)",
    "ProprietarioImovel": "Vínculo vigente ou removido logicamente",
    "AvaliacaoImovel": "`rascunho`, `concluida`, `cancelada`",
    "CaracteristicaImovel": "Vigente, substituída a cada novo registro",
    "GeometriaImovel": "Vigente, substituída a cada levantamento",
}

REGRA_ENTIDADES = {
    "RN-TEL-001": "Bairro",
    "RN-TEL-002": "Logradouro",
    "RN-TEL-003": "PlantaGenericaValores",
    "RN-TEL-004": "PlantaGenericaValores",
    "RN-TEL-005": "Georreferencia",
    "RN-TEL-006": "Bairro, Logradouro",
    "RN-IMO-001": "Imovel",
    "RN-IMO-002": "Imovel",
    "RN-IMO-003": "Imovel",
    "RN-IMO-004": "Imovel",
    "RN-IMO-005": "AvaliacaoImovel",
    "RN-IMO-006": "ProprietarioImovel",
    "RN-IMO-007": "GeometriaImovel",
}


def artefato_026(cfg: dict[str, str], ctx: dict) -> str:
    """Modelo de Domínio."""
    pre = cfg["prefixo_regra"]
    entidades = "\n\n".join(
        f"""### {nome}

{descricao}

* **Invariantes:** {ENTIDADE_INVARIANTES.get(nome, 'Campos obrigatórios conforme o schema.')}
* **Estados:** {ENTIDADE_ESTADOS.get(nome, '—')}"""
        for nome, descricao in cfg["entidades"]
    )
    return f"""# 1. Finalidade

Este artefato descreve o modelo de domínio de {cfg['dominio']}: entidades,
invariantes, estados e as regras que os governam.

---

# 2. Conceitos Centrais

{tabela(
    ["Entidade", "Responsabilidade"],
    [[nome, descricao] for nome, descricao in cfg["entidades"]],
)}

---

# 3. Invariantes por Entidade

{entidades}

---

# 4. Regras e Estados

{tabela(
    ["Regra", "Tipo", "Entidades afetadas", "Garantia técnica"],
    [
        [r[0], r[2], REGRA_ENTIDADES.get(r[0], "—"), r[6]]
        for r in map(_regra, DADOS[f"{pre}_REGRAS"])
    ],
)}

---

# 5. Modelo Conceitual

O domínio se articula em três eixos:

* **Território:** a divisão territorial organiza o território e a malha viária.
* **Valor:** a planta genérica de valores estabelece os parâmetros que sustentam
  a apuração.
* **Fundo de terra:** o cadastro imobiliário registra o lote, sua titularidade,
  sua construção e sua geometria.

---

# 6. Limites do Modelo

* As referências entre domínios são identificadores opacos, sem FK física.
* A exclusão é lógica em todos os cadastros, preservando o histórico.
* Estados terminais, como `DEMOLIDO` e `REVOGADA`, são irreversíveis por regra.
"""



# ============================================================================
# TÍTULOS E DRIVER
# ============================================================================

ARTEFATOS = [
    (1, "Mapa-de-Atores", artefato_001),
    (2, "Mapa-de-Capacidades", artefato_002),
    (3, "Mapa-de-Processos", artefato_003),
    (4, "Mapa-de-Servicos", artefato_004),
    (5, "Casos-de-Uso", artefato_005),
    (6, "Historias-de-Usuario", artefato_006),
    (7, "Regras-de-Negocio", artefato_007),
    (8, "Requisitos-Funcionais", artefato_008),
    (9, "Requisitos-Nao-Funcionais", artefato_009),
    (10, "Especificacoes", artefato_010),
    (11, "Criterios-de-Aceitacao", artefato_011),
    (12, "Matriz-de-Rastreabilidade", artefato_012),
    (13, "Modelo-de-Dados", artefato_013),
    (14, "Modelo-de-Integracao", artefato_014),
    (15, "Arquitetura-de-Servicos", artefato_015),
    (16, "Modelo-de-Seguranca", artefato_016),
    (17, "Modelo-de-Auditoria", artefato_017),
    (18, "Plano-de-Testes", artefato_018),
    (19, "Casos-de-Teste", artefato_019),
    (20, "Plano-de-Implantacao", artefato_020),
    (21, "Checklist-de-Prontidao-para-Producao", artefato_021),
    (22, "Plano-de-Migracao-de-Dados", artefato_022),
    (23, "Plano-de-Treinamento", artefato_023),
    (24, "Plano-de-Suporte-e-Operacao", artefato_024),
    (25, "Estrutura-Tecnica", artefato_025),
    (26, "Modelo-de-Dominio", artefato_026),
]

# Títulos legíveis, exibidos no cabeçalho de cada artefato.
TITULOS = {
    1: "Mapa de Atores",
    2: "Mapa de Capacidades",
    3: "Mapa de Processos",
    4: "Mapa de Serviços",
    5: "Casos de Uso",
    6: "Histórias de Usuário",
    7: "Regras de Negócio",
    8: "Requisitos Funcionais",
    9: "Requisitos Não Funcionais",
    10: "Especificações",
    11: "Critérios de Aceitação",
    12: "Matriz de Rastreabilidade",
    13: "Modelo de Dados",
    14: "Modelo de Integração",
    15: "Arquitetura de Serviços",
    16: "Modelo de Segurança",
    17: "Modelo de Auditoria",
    18: "Plano de Testes",
    19: "Casos de Teste",
    20: "Plano de Implantação",
    21: "Checklist de Prontidão para Produção",
    22: "Plano de Migração de Dados",
    23: "Plano de Treinamento",
    24: "Plano de Suporte e Operação",
    25: "Estrutura Técnica",
    26: "Modelo de Domínio",
}

# Diretório de destino por código de domínio.
DIRETORIOS = {
    "DOM-TEL": "DOM-TEL",
    "DOM-IMO": "DOM-IMO",
    "DOM-GEO": "DOM-GEO",
    "DOM-OBR": "DOM-OBR",
}

# Nome do domínio no nome do arquivo, conforme a nomenclatura já vigente nos
# diretórios de documentação (sem espaços nem acentuação).
SLUG_DOMINIO = {
    "DOM-TEL": "Gestao-Territorial",
    "DOM-IMO": "Cadastro-Imobiliario",
    "DOM-GEO": "Geoinformacao-Municipal",
    "DOM-OBR": "Obras-e-Infraestrutura",
}


def montar_contexto(cfg: dict[str, str], rotas: dict[str, list[str]]) -> dict:
    """Reúne os dados extraídos do código, cacheados entre domínios."""
    return {
        "rotas": rotas,
        "colunas": extrair_colunas(cfg["modulo"]),
        "use_cases": extrair_use_cases(cfg["modulo"]),
        "testes": extrair_testes(cfg["codigo"]),
    }


def caminho_artefato(cfg: dict[str, str], numero: int, slug: str) -> Path:
    """Monta o caminho do arquivo de um artefato.

    O nome do domínio no arquivo usa a forma hifenizada e sem acentuação já
    vigente nos diretórios de documentação.
    """
    nome = f"{numero:03d}-{slug}-{SLUG_DOMINIO[cfg['codigo']]}.md"
    return RAIZ / "SIGMUN-Docs" / DIRETORIOS[cfg["codigo"]] / nome


def main() -> int:
    """Gera (ou verifica) os artefatos dos dois domínios."""
    parser = argparse.ArgumentParser(description="Gera os artefatos DOM-TEL e DOM-IMO.")
    parser.add_argument(
        "--verificar",
        action="store_true",
        help="Falha se algum artefato estiver desatualizado, sem gravar.",
    )
    args = parser.parse_args()

    rotas_por_dominio = extrair_openapi()
    contexto_por_dominio: dict[str, dict] = {}
    for chave, cfg in DADOS["DOMINIOS"].items():
        prefixo = cfg["prefixo"]
        rotas = {
            c: v for c, v in rotas_por_dominio.items() if c.startswith(prefixo)
        }
        contexto_por_dominio[chave] = montar_contexto(cfg, rotas)

    defasados: list[str] = []
    gravados = 0
    for chave, cfg in DADOS["DOMINIOS"].items():
        ctx = contexto_por_dominio[chave]
        for numero, slug, gerador in ARTEFATOS:
            titulo = TITULOS[numero]
            conteudo = (
                cabecalho(numero, titulo, cfg, slug)
                + gerador(cfg, ctx)
                + "\n"
                + rodape(numero, titulo, cfg, slug)
            )
            destino = caminho_artefato(cfg, numero, slug)
            atual = destino.read_text(encoding="utf-8") if destino.exists() else ""
            if atual == conteudo:
                continue
            defasados.append(str(destino.relative_to(RAIZ)))
            if not args.verificar:
                destino.write_text(conteudo, encoding="utf-8")
                gravados += 1

    rotulo = "verificação" if args.verificar else "geração"
    print(f"{rotulo.capitalize()} concluída para {len(DADOS['DOMINIOS'])} domínios.")
    print(f"  Artefatos no escopo: {len(ARTEFATOS) * len(DADOS['DOMINIOS'])}")
    print(f"  Artefatos atualizados: {len(defasados)}")
    if args.verificar and defasados:
        print("\nArtefatos desatualizados:")
        for caminho in defasados:
            print(f"  - {caminho}")
        return 1
    if not args.verificar:
        for caminho in defasados:
            print(f"  gravado: {caminho}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

