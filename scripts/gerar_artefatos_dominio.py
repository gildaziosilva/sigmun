#!/usr/bin/env python
"""Gera os artefatos `001`-`026` no padrão DOM-COMPRAS-001.

Combina, como `gerar_artefatos_territoriais.py`, duas fontes:

* **código** — modelos ORM, OpenAPI, casos de uso, enums, regras `RN-*` e testes;
* **negócio** — atores, capacidades, processos, serviços, histórias, requisitos e
  lacunas declarados em `FICHAS`.

Uso:
    .venv/bin/python scripts/gerar_artefatos_dominio.py --apenas DOM-CUM
    .venv/bin/python scripts/gerar_artefatos_dominio.py --verificar

Classificação da Informação: Pública
Responsável: Equipe SIGMUN
Status da revisão: Vigente
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "scripts"))
os.chdir(RAIZ)

from src.main import app  # noqa: E402

DATA_REVISAO = "2026-09-30"
DATA_ESBOCO = "2026-08-20"

RELACIONADOS = (
    "000-CONSTITUICAO-DO-PROJETO-SIGMUN.md",
    "000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md",
    "000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md",
    "000D-MODELO-DE-DOCUMENTO.md",
    "000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md",
    "000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md",
    "030-Roadmap-de-Implementacao-dos-Dominios.md",
    "Mapa-de-Dominios.md",
)

METODOS = ("GET", "POST", "PATCH", "PUT", "DELETE")

# Correspondência técnica declarada para fichas automáticas.
#
# Ausência de uma entrada significa:
#   - nenhum módulo técnico oficialmente correspondido neste momento;
#   - não significa que o domínio não possa receber um módulo no futuro.
#
# A correspondência DOM × MOD é independente da maturidade e da
# implementação material do domínio.
CORRESPONDENCIAS_DOM_MODULO: dict[str, dict[str, str]] = {
    "DOM-PLA": {
        "modulo": "sigmun_planejamento",
        "codigo_modulo": "MOD-PLA",
    },
}


def tabelas_do_modulo(modulo: str) -> dict[str, dict]:
    """`(tabela) -> classe, colunas, schema e docstring` dos modelos ORM."""
    import importlib

    from sqlalchemy import inspect as sa_inspect

    saida: dict[str, dict] = {}
    banco = RAIZ / "src" / "modules" / modulo / "infrastructure" / "database"
    if not banco.is_dir():
        return saida
    for arquivo in sorted(banco.glob("models*.py")):
        modelos = importlib.import_module(
            f"src.modules.{modulo}.infrastructure.database.{arquivo.stem}"
        )
        bases = [
            obj
            for obj in vars(modelos).values()
            if isinstance(obj, type)
            and (
                obj.__name__.endswith("Base")
                or hasattr(obj, "metadata")
                or hasattr(obj, "_decl_class_registry")
            )
        ]
        for base in bases:
            for classe in base.__subclasses__():
                if not hasattr(classe, "__table__"):
                    continue
                colunas = []
                for coluna in sa_inspect(classe).columns:
                    flags = []
                    if coluna.primary_key:
                        flags.append("PK")
                    if getattr(coluna, "unique", False):
                        flags.append("UQ")
                    if not coluna.nullable and not coluna.primary_key:
                        flags.append("NN")
                    colunas.append({"nome": coluna.name, "tipo": str(coluna.type), "flags": flags})
                args = getattr(classe, "__table_args__", None)
                saida[classe.__tablename__] = {
                    "classe": classe.__name__,
                    "colunas": colunas,
                    "schema": args.get("schema") if isinstance(args, dict) else None,
                    "doc": (classe.__doc__ or "").strip().splitlines()[0] if classe.__doc__ else "",
                }
    return saida


def operacoes(prefixo: str, modulo: str | None = None) -> list[dict]:
    """Operações REST sob o prefixo, a partir do OpenAPI da aplicação."""
    spec = app.openapi()
    saida = []
    for caminho in sorted(spec["paths"]):
        if not caminho.startswith(prefixo):
            continue
        recurso = caminho[len(prefixo) :].strip("/").split("/")[0] or "raiz"
        for metodo, definicao in sorted(spec["paths"][caminho].items()):
            if metodo.upper() not in METODOS:
                continue
            resumo = definicao.get("summary") or ""
            saida.append(
                {
                    "metodo": metodo.upper(),
                    "caminho": caminho,
                    "recurso": recurso,
                    "resumo": str(resumo).splitlines()[0][:90] if resumo else "",
                }
            )
    if saida or not modulo:
        return saida
    # Router definido no módulo e ainda não registrado em src/main.py.
    base = RAIZ / "src" / "modules" / modulo / "presentation" / "api"
    padrao = re.compile(r'@router(?:_\w+)?\.(get|post|patch|put|delete)\("([^"]+)"')
    for arquivo in sorted(base.glob("*.py")):
        for metodo, rota in padrao.findall(arquivo.read_text(encoding="utf-8", errors="replace")):
            caminho = f"{prefixo}/{rota.strip('/')}" if rota != "/" else prefixo
            recurso = caminho[len(prefixo) :].strip("/").split("/")[0] or "raiz"
            saida.append(
                {
                    "metodo": metodo.upper(),
                    "caminho": caminho,
                    "recurso": recurso,
                    "resumo": "definida no router do módulo",
                }
            )
    return saida


def casos_de_uso(modulo: str) -> list[dict]:
    """Classes `*UseCase` publicadas pelo pacote de casos de uso."""
    import importlib

    try:
        pacote = importlib.import_module(f"src.modules.{modulo}.application.use_cases")
    except ModuleNotFoundError:
        pacote = None
    saida = []
    for nome in getattr(pacote, "__all__", []) if pacote else []:
        obj = getattr(pacote, nome, None)
        if not isinstance(obj, type) or not nome.endswith("UseCase"):
            continue
        linhas = (obj.__doc__ or "").strip().splitlines()
        saida.append({"nome": nome, "resumo": linhas[0] if linhas else ""})
    if saida:
        return saida
    # Pacotes sem `__all__`: varre os módulos de casos de uso do domínio.
    apl = (
        Path(pacote.__path__[0]).parent
        if pacote
        else RAIZ / "src" / "modules" / modulo / "application"
    )
    arquivos = sorted(apl.glob("use_cases*.py"))
    if pacote:
        arquivos += [
            a for a in sorted(Path(pacote.__path__[0]).glob("*.py")) if a.name != "__init__.py"
        ]
    vistos: set[str] = set()
    for arquivo in arquivos:
        texto = arquivo.read_text(encoding="utf-8", errors="replace").splitlines()
        for indice, linha in enumerate(texto):
            achado = re.match(r"class (\w+UseCase)\b", linha)
            if not achado:
                continue
            if achado.group(1) in vistos:
                continue
            vistos.add(achado.group(1))
            resumo = ""
            for seguinte in texto[indice + 1 : indice + 6]:
                doc = re.match(r'\s*(?:"""\s*)?(.+?)(?:\s*""")?\s*$', seguinte)
                if doc and not seguinte.strip().startswith(("class", "@", "def")):
                    resumo = doc.group(1)
                    break
            saida.append({"nome": achado.group(1), "resumo": resumo})
    return saida


def enums_do_modulo(modulo: str) -> dict[str, list[tuple[str, str]]]:
    """`Enum -> [(membro, valor)]` declarados nas entidades do módulo."""
    saida: dict[str, list[tuple[str, str]]] = {}
    base = RAIZ / "src" / "modules" / modulo
    for caminho in sorted(base.rglob("*.py")):
        linhas = caminho.read_text(encoding="utf-8", errors="replace").splitlines()
        indice = 0
        while indice < len(linhas):
            achado = re.match(r"class (\w+)\(([^)]*Enum[^)]*)\):", linhas[indice])
            if not achado:
                indice += 1
                continue
            membros = []
            proximo = indice + 1
            while proximo < len(linhas):
                linha = linhas[proximo]
                if linha and not linha[0].isspace():
                    break
                membro = re.match(r"\s+(\w+)\s*=\s*(.+?)\s*$", linha)
                if membro and not membro.group(1).startswith("__"):
                    membros.append((membro.group(1), membro.group(2)))
                proximo += 1
            if membros:
                saida[achado.group(1)] = membros
            indice = proximo
    return saida


def regras_do_modulo(modulo: str, prefixo: str) -> dict[str, str]:
    """`RN-XXX-nnn -> descrição` citadas em comentários e docstrings."""
    padrao = re.compile(rf"(RN-{prefixo}-\d{{3}})[:\s]+([^\n\"]+)")
    achadas: dict[str, str] = {}
    for caminho in sorted((RAIZ / "src" / "modules" / modulo).rglob("*.py")):
        texto = caminho.read_text(encoding="utf-8", errors="replace")
        for identificador, descricao in padrao.findall(texto):
            limpo = descricao.strip(" .*").strip()
            if len(limpo) > 12 and identificador not in achadas:
                achadas[identificador] = limpo[:150]
    return dict(sorted(achadas.items()))


def testes_do_dominio(modulo: str) -> list[dict]:
    """Contagem de testes por classe nos arquivos que referenciam o módulo."""
    marca = f"src.modules.{modulo}"
    achados = []
    for pasta in ("tests/unit", "tests/integration"):
        base = RAIZ / pasta
        if not base.is_dir():
            continue
        for caminho in sorted(base.glob("test_*.py")):
            texto = caminho.read_text(encoding="utf-8", errors="replace")
            if marca not in texto:
                continue
            nome = caminho.stem
            if not any(parte in nome for parte in modulo.replace("sigmun_", "").split("_")):
                continue
            classes = list(re.finditer(r"^class (\w+):", texto, re.M))
            for indice, achado in enumerate(classes):
                fim = classes[indice + 1].start() if indice + 1 < len(classes) else len(texto)
                bloco = texto[achado.start() : fim]
                metodos = re.findall(r"^    def (test_\w+)", bloco, re.M)
                achados.append(
                    {
                        "arquivo": str(caminho.relative_to(RAIZ)),
                        "classe": achado.group(1),
                        "quantidade": len(metodos),
                        "metodos": metodos,
                    }
                )
    return achados


# ==============================================================================
# ESQUELETO DO DOCUMENTO (padrão DOM-COMPRAS-001)
# ==============================================================================


def tabela(cabecalho: list[str], linhas: list[list[str]]) -> str:
    """Tabela Markdown com separador na primeira linha."""
    if not linhas:
        linhas = [["—"] * len(cabecalho)]
    saida = ["| " + " | ".join(cabecalho) + " |"]
    saida.append("| " + " | ".join("---" for _ in cabecalho) + " |")
    for linha in linhas:
        saida.append("| " + " | ".join(str(c) for c in linha) + " |")
    return "\n".join(saida)


def lista(itens: list[str]) -> str:
    return "\n".join(f"* {item}" for item in itens) if itens else "* —"


def documento(cfg: dict, numero: int, titulo: str, corpo: str) -> str:
    """Monta o artefato com cabeçalho e rodapé corporativos."""
    codigo = f"{cfg['codigo']}-{numero:03d}"
    relacionados = "\n".join(f"* `{item.format(slug=cfg['slug'])}`" for item in RELACIONADOS)
    cabecalho = f"""# {numero:03d} – {titulo} – {cfg["dominio"]}

#### {titulo} – {cfg["dominio"]}

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** {codigo}

**Domínio:** {cfg["dominio"]}

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-{cfg["slug"]}.md`
{relacionados}

---

"""
    rodape = f"""---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | {DATA_ESBOCO} | Criação do esboço inicial padronizado do artefato |
| 2.0 | {DATA_REVISAO} | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** {numero:03d}-{cfg["slug"]}-{titulo}.md

**Última atualização:** {DATA_REVISAO}

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
"""
    return cabecalho + corpo.rstrip() + "\n\n" + rodape


def secao(numero: int, titulo: str, conteudo: str) -> str:
    return f"\n# {numero}. {titulo}\n\n{conteudo}\n\n---\n"


# ==============================================================================
# CONTEÚDO DE NEGÓCIO POR DOMÍNIO
# ==============================================================================

FICHAS: dict[str, dict] = {
    "DOM-CUM": {
        "codigo": "DOM-CUM",
        "dominio": "Cadastro Único Municipal",
        "slug": "Cadastro-Unico-Municipal",
        "modulo": "sigmun_cadastro",
        "prefixo": "/api/v1/cadastro",
        "prefixo_regra": "CUM",
        "schema": "core",
        "atores": [
            (
                "AT-CUM-001",
                "Operador de Cadastro",
                "Interno",
                "Servidor público",
                "Cadastra e mantém pessoas, endereços, documentos e contatos.",
            ),
            (
                "AT-CUM-002",
                "Gestor de Unidade",
                "Interno",
                "Gestor municipal",
                "Mantém o cadastro das unidades administrativas sob sua responsabilidade.",
            ),
            (
                "AT-CUM-003",
                "Titular do Cadastro",
                "Externo",
                "Cidadão ou pessoa jurídica",
                "Fornece e corrige seus próprios dados em atendimento.",
            ),
            (
                "AT-CUM-004",
                "Administrador do SIGMUN",
                "Interno",
                "Administrador de plataforma",
                "Administra parâmetros de auditoria e operação do cadastro.",
            ),
            (
                "AT-CUM-005",
                "DOM-IDN",
                "Serviço",
                "Identidade e Acesso",
                "Autentica o operador e resolve a identidade digital da pessoa.",
            ),
            (
                "AT-CUM-006",
                "Domínios consumidores",
                "Externo",
                "Domínios do SIGMUN",
                "Consomem o cadastro como fonte oficial de pessoa e unidade.",
            ),
        ],
        "capacidades": [
            (
                "CAP-CUM-001",
                "Cadastro de pessoa",
                "Registra, consulta, altera e exclui logicamente pessoas.",
                "PRO-CUM-001",
            ),
            (
                "CAP-CUM-002",
                "Extensão por tipo",
                "Mantém a extensão 1:1 de pessoa física ou jurídica.",
                "PRO-CUM-001",
            ),
            (
                "CAP-CUM-003",
                "Endereços",
                "Controla o histórico de vigência e o endereço principal.",
                "PRO-CUM-002",
            ),
            (
                "CAP-CUM-004",
                "Documentos",
                "Vincula documentos com validação de CPF e CNPJ.",
                "PRO-CUM-002",
            ),
            (
                "CAP-CUM-005",
                "Contatos",
                "Mantém contatos telefônicos, de e-mail e WhatsApp.",
                "PRO-CUM-002",
            ),
            (
                "CAP-CUM-006",
                "Unidades administrativas",
                "Mantém a hierarquia de órgãos e setores do município.",
                "PRO-CUM-003",
            ),
            (
                "CAP-CUM-007",
                "Consulta e qualidade cadastral",
                "Oferece busca por identificador e indicadores de qualidade.",
                "PRO-CUM-004",
            ),
        ],
    },
}


FICHAS["DOM-CUM"].update(
    {
        "processos": [
            (
                "PRO-CUM-001",
                "Registrar pessoa",
                "Registra a pessoa e sua extensão.",
                "RN-CUM-001 a 003",
            ),
            (
                "PRO-CUM-002",
                "Complementar cadastro",
                "Endereço, documento e contato.",
                "RN-CUM-004 a 006",
            ),
            (
                "PRO-CUM-003",
                "Manter unidade administrativa",
                "Hierarquia de órgãos e setores.",
                "RN-CUM-008, 009",
            ),
            ("PRO-CUM-004", "Consultar cadastro", "Consulta por identificador.", "—"),
            (
                "PRO-CUM-005",
                "Excluir logicamente",
                "Exclusão em cascata com histórico.",
                "RN-CUM-007",
            ),
        ],
        "historias": [
            (
                "HU-CUM-001",
                "Registrar pessoa com contatos como fonte oficial.",
                "CAP-CUM-001",
                "Alta",
            ),
            (
                "HU-CUM-002",
                "Registrar a extensão física ou jurídica correta.",
                "CAP-CUM-002",
                "Alta",
            ),
            ("HU-CUM-003", "Adicionar endereço com vigência rastreável.", "CAP-CUM-003", "Média"),
            ("HU-CUM-004", "Validar CPF e CNPJ para evitar duplicidade.", "CAP-CUM-004", "Alta"),
            (
                "HU-CUM-005",
                "Manter hierarquia de unidades administrativas.",
                "CAP-CUM-006",
                "Média",
            ),
            ("HU-CUM-006", "Consultar pessoa por identificador.", "CAP-CUM-007", "Alta"),
            ("HU-CUM-007", "Registrar autoria e data de toda alteração.", "CAP-CUM-001", "Alta"),
        ],
        "rnf": [
            ("RNF-CUM-001", "Desempenho", "p95 até 300 ms na consulta por identificador."),
            (
                "RNF-CUM-002",
                "Integridade referencial",
                "Chave primária UUID v4 gerada pela aplicação.",
            ),
            (
                "RNF-CUM-003",
                "Exclusão lógica",
                "Exclusão física vedada; há deleted_at e deleted_by.",
            ),
            ("RNF-CUM-004", "Auditoria", "created_at, created_by, updated_at e updated_by."),
            ("RNF-CUM-005", "Privacidade", "Documento e contato são dado pessoal (LGPD)."),
            (
                "RNF-CUM-006",
                "Autenticação",
                "Acesso autenticado; X-Usuario-Id provisório até o IDN.",
            ),
            ("RNF-CUM-007", "Transacionalidade", "Pessoa e extensão na mesma unidade de trabalho."),
            ("RNF-CUM-008", "Idempotência", "Documento único entre pessoas não excluídas."),
            ("RNF-CUM-009", "Rastreabilidade", "Toda alteração referencia a regra aplicada."),
            ("RNF-CUM-010", "Compatibilidade", "Sem chave estrangeira entre schemas."),
        ],
        "integracoes": [
            ("DOM-IDN", "Identidade e Acesso", "Consome", "Autenticação do operador."),
            ("DOM-GDO", "Gestão Documental", "Consome", "Documentos e evidências."),
            ("DOM-MET", "Metadados", "Consome", "Metadados e classificação."),
            ("DOM-DAD", "Dados Corporativos", "Fornece", "Ativos de dados cadastrais."),
            ("DOM-INT", "Interoperabilidade", "Fornece", "Contrato e outbox."),
            ("DOM-PES", "Gestão de Pessoas", "Fornece", "Pessoa física de servidor."),
        ],
        "lacunas": [
            "Autenticação: resolvido no ADR-0007 (JWT do DOM-IDN obrigatório nas escritas).",
            "Revisão periódica: definida no ADR-0007 (12 meses, tarefa mensal, indicador).",
            "Compartilhamento: contrato formal definido no ADR-0007 (fonte oficial, id opaco).",
        ],
    }
)


FICHAS["DOM-ASS"] = {
    "codigo": "DOM-ASS",
    "dominio": "Assistência Social",
    "slug": "Assistencia-Social",
    "modulo": "sigmun_assistencia_social",
    "prefixo": "/api/v1/ass",
    "prefixo_regra": "ASS",
    "schema": "ass",
    "atores": [
        (
            "AT-ASS-001",
            "Técnico de CRAS/CREAS",
            "Interno",
            "Servidor público",
            "Executa o atendimento e registra a evolução da família.",
        ),
        (
            "AT-ASS-002",
            "Gestor de unidade",
            "Interno",
            "Gestor do CRAS/CREAS",
            "Autoriza benefícios e responde pela unidade.",
        ),
        (
            "AT-ASS-003",
            "Família em situação de vulnerabilidade",
            "Externo",
            "Cidadão",
            "Recebe o atendimento e apresenta a documentação.",
        ),
        (
            "AT-ASS-004",
            "Conselho Municipal de Assistência",
            "Externo",
            "Colegiado",
            "Acompanha e delibera sobre a execução.",
        ),
    ],
    "capacidades": [
        (
            "CAP-ASS-001",
            "Cadastro de família",
            "Registra a família CadÚnico e seu NIS.",
            "PRO-ASS-001",
        ),
        (
            "CAP-ASS-002",
            "Atendimento social",
            "Registra atendimento e encaminhamento.",
            "PRO-ASS-002",
        ),
        (
            "CAP-ASS-003",
            "Benefício eventual",
            "Solicita, autoriza, nega e entrega o benefício.",
            "PRO-ASS-003",
        ),
        (
            "CAP-ASS-004",
            "Unidades de atendimento",
            "Mantém CRAS, CREAS e demais unidades.",
            "PRO-ASS-004",
        ),
    ],
    "processos": [
        (
            "PRO-ASS-001",
            "Cadastrar família",
            "Registra família e pessoas vinculadas.",
            "RN-ASS-001, RN-ASS-002",
        ),
        (
            "PRO-ASS-002",
            "Atender e encaminhar",
            "Registra atendimento e encaminhamento.",
            "RN-ASS-004",
        ),
        (
            "PRO-ASS-003",
            "Conceder benefício eventual",
            "Solicita, autoriza, nega, entrega ou cancela.",
            "RN-ASS-003",
        ),
        ("PRO-ASS-004", "Manter unidade de atendimento", "Cadastra e mantém CRAS/CREAS.", "—"),
    ],
    "historias": [
        (
            "HU-ASS-001",
            "Como técnico, quero registrar a família com NIS para evitar cadastro duplicado.",
            "CAP-ASS-001",
            "Alta",
        ),
        (
            "HU-ASS-002",
            "Como técnico, quero registrar o atendimento com encaminhamento.",
            "CAP-ASS-002",
            "Alta",
        ),
        (
            "HU-ASS-003",
            "Como gestor, quero autorizar o benefício para controlar a concessão.",
            "CAP-ASS-003",
            "Alta",
        ),
        (
            "HU-ASS-004",
            "Como técnico, quero consultar a família pelo NIS para retomar o acompanhamento.",
            "CAP-ASS-001",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-ASS-001", "Sigilo", "Dados de família e benefício são sensíveis (LGPD)."),
        ("RNF-ASS-002", "Autenticação", "Acesso autenticado; escrita exige credencial do DOM-IDN."),
        ("RNF-ASS-003", "Auditoria", "Toda mudança registra autor, data e situação."),
        (
            "RNF-ASS-004",
            "Integridade",
            "NIS único no município; sem chave estrangeira entre schemas.",
        ),
    ],
    "integracoes": [
        ("DOM-IDN", "Identidade e Acesso", "Consome", "Autenticação do operador."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Documentos dafamília e do atendimento."),
        ("DOM-MET", "Metadados", "Consome", "Classificação."),
        ("DOM-PES", "Gestão de Pessoas", "Consome", "Dados do servidor atendente."),
        ("DOM-IND", "Indicadores e Desempenho", "Fornece", "Indicadores de cobertura."),
    ],
    "lacunas": [
        "Definir o glossário de tipos de benefício eventual por município.",
        "Formalizar o fluxo de aferimento de renda com o DOM-IND.",
    ],
}


FICHAS["DOM-DIA"] = {
    "codigo": "DOM-DIA",
    "dominio": "Gestão de Diárias, Viagens e Deslocamentos",
    "slug": "Gestao-de-Diarias-Viagens-e-Deslocamentos",
    "modulo": "sigmun_dia",
    "prefixo": "/api/v1/dia",
    "prefixo_regra": "DIA",
    "schema": "dia",
    "atores": [
        (
            "AT-DIA-001",
            "Servidor solicitante",
            "Interno",
            "Servidor público",
            "Solicita diária, registra viagem e presta contas.",
        ),
        (
            "AT-DIA-002",
            "Gestor da unidade",
            "Interno",
            "Gestor",
            "Autoriza a diária e a lotação da viagem.",
        ),
        (
            "AT-DIA-003",
            "Contabilidade",
            "Interno",
            "Setor contábil",
            "Confere, glosa e paga a prestação de contas.",
        ),
        (
            "AT-DIA-004",
            "Ordenador de despesa",
            "Externo",
            "Autoridade competente",
            "Aprova o pagamento e responde pelo recurso.",
        ),
    ],
    "capacidades": [
        (
            "CAP-DIA-001",
            "Viagens e deslocamentos",
            "Registra e tramita viagens entre unidades.",
            "PRO-DIA-001",
        ),
        (
            "CAP-DIA-002",
            "Diárias",
            "Solicita, autoriza, calcula, concede e paga a diária.",
            "PRO-DIA-002",
        ),
        (
            "CAP-DIA-003",
            "Prestação de contas",
            "Abre, confere, aprova, glosa e restitui.",
            "PRO-DIA-003",
        ),
        (
            "CAP-DIA-004",
            "Rastreabilidade",
            "Grava os eventos de situação da diária.",
            "PRO-DIA-004",
        ),
    ],
    "processos": [
        ("PRO-DIA-001", "Viagem", "Cria a viagem e tramita entre unidades.", "—"),
        (
            "PRO-DIA-002",
            "Concessão da diária",
            "Solicita, autoriza, calcula e concede.",
            "RN-DIA-001 a 008",
        ),
        (
            "PRO-DIA-003",
            "Prestação de contas",
            "Abre, confere, aprova, glosa e restitui.",
            "RN-DIA-009, 011 a 017",
        ),
        (
            "PRO-DIA-004",
            "Auditoria do ciclo",
            "Registra a transição de situação em eventos_diarias.",
            "—",
        ),
    ],
    "historias": [
        (
            "HU-DIA-001",
            "Como servidor, quero registrar a viagem para que a diária seja vinculada.",
            "CAP-DIA-001",
            "Alta",
        ),
        (
            "HU-DIA-002",
            "Como gestor, quero autorizar a diária para liberar o pagamento.",
            "CAP-DIA-002",
            "Alta",
        ),
        (
            "HU-DIA-003",
            ("HU-IDN-003", "Como domínio, quero validar o escopo do token.", "CAP-IDN-003", "Alta"),
            "CAP-DIA-003",
            "Alta",
        ),
        (
            "HU-DIA-004",
            "Como contabilidade, quero glosar a prestação com motivo para corrigir o valor.",
            "CAP-DIA-003",
            "Média",
        ),
        (
            "HU-DIA-005",
            "Como auditor, quero consultar o histórico para rastrear a decisão.",
            "CAP-DIA-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-DIA-001", "Exclusividade", "Diária do tipo antecipação não pode ser duplicada."),
        ("RNF-DIA-002", "Auditoria", "Toda transição de situação gera evento com autor e data."),
        ("RNF-DIA-003", "Documento", "Prestação de contas exige documento anexado (DOM-GDO)."),
        ("RNF-DIA-004", "Imutabilidade", "Folha aprovada ou paga é terminal."),
        ("RNF-DIA-005", "Integridade", "Sem chave estrangeira entre schemas."),
        ("RNF-DIA-006", "Transacionalidade", "Situação e evento gravados na mesma transação."),
    ],
    "integracoes": [
        ("DOM-PES", "Gestão de Pessoas", "Consome", "Pessoa e lotação do servidor."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Documento da prestação de contas."),
        ("DOM-CON", "Contabilidade Pública", "Fornece", "Controle do pagamento."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Contrato e outbox."),
        ("DOM-IDN", "Identidade e Acesso", "Consume", "Autenticação do operador."),
    ],
    "lacunas": [
        "Definir tabela de valores de diária por categoria e nível.",
        "Formalizar o envio de folha para a contabilidade (DOM-CON).",
    ],
}


FICHAS["DOM-IDN"] = {
    "codigo": "DOM-IDN",
    "dominio": "Identidade e Acesso",
    "slug": "Identidade-e-Acesso",
    "modulo": "sigmun_idn",
    "prefixo": "/api/v1/idn",
    "prefixo_regra": "IDN",
    "schema": "idn",
    "atores": [
        (
            "AT-IDN-001",
            "Usuário do SIGMUN",
            "Interno",
            "Servidor público",
            "Autentica-se e acessa os serviços com JWT.",
        ),
        (
            "AT-IDN-002",
            "Administrador de identidade",
            "Interno",
            "Administrador",
            "Cria, ativa, bloqueia e desativa usuários.",
        ),
        (
            "AT-IDN-003",
            "Administrador de papéis",
            "Interno",
            "Administrador",
            "Mantém papéis, permissões e escopos.",
        ),
        (
            "AT-IDN-004",
            "Domínios consumidores",
            "Externo",
            "Módulos SIGMUN",
            "Validam o token e aplicam escopo de acesso.",
        ),
    ],
    "capacidades": [
        ("CAP-IDN-001", "Autenticação", "Emite e renova token JWT de acesso.", "PRO-IDN-001"),
        (
            "CAP-IDN-002",
            "Gestão de usuários",
            "Registra, ativa, bloqueia e desativa usuários.",
            "PRO-IDN-002",
        ),
        (
            "CAP-IDN-003",
            "Papéis e permissões",
            "Mantém papéis, permissões e seus vínculos.",
            "PRO-IDN-003",
        ),
        (
            "CAP-IDN-004",
            "Sessões e auditoria",
            "Controla sessão e registra tentativas de login.",
            "PRO-IDN-004",
        ),
    ],
    "processos": [
        ("PRO-IDN-001", "Autenticar", "Valida credenciais e emite o par de tokens.", "RN-IDN-001"),
        ("PRO-IDN-002", "Gerenciar usuário", "Registra, ativa, bloqueia e desativa.", "RN-IDN-002"),
        ("PRO-IDN-003", "Conceder acesso", "Vincula papéis e permissões por escopo.", "RN-IDN-003"),
        ("PRO-IDN-004", "Auditar acesso", "Registra tentativa de login e sessão.", "RN-IDN-004"),
    ],
    "historias": [
        (
            "HU-IDN-001",
            "Como usuário, quero obter token para acessar os serviços do SIGMUN.",
            "CAP-IDN-001",
            "Alta",
        ),
        (
            "HU-IDN-002",
            "Como administrador, quero bloquear um usuário para suspender o acesso.",
            "CAP-IDN-002",
            "Alta",
        ),
        (
            "HU-IDN-003",
            "Como domínio, quero validar o token e o escopo para autorizar a operação.",
            "CAP-IDN-003",
            "Alta",
        ),
        (
            "HU-IDN-004",
            "Como auditor, quero ver as tentativas de login para detectar abuso.",
            "CAP-IDN-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-IDN-001", "Segredo", "Senha nunca trafega nem é armazenada em claro; apenas hash."),
        ("RNF-IDN-002", "Expiração", "Token de acesso tem validade curta e renovação controlada."),
        (
            "RNF-IDN-003",
            "Auditoria",
            "Tentativa de login é registrada com usuário, data e resultado.",
        ),
        (
            "RNF-IDN-004",
            "Compatibilidade",
            "Header X-Usuario-Id aceito como transição e marcado como depreciado.",
        ),
        ("RNF-IDN-005", "Least privilege", "Permissão é concedida por papel e escopo."),
    ],
    "regras": [
        "a autenticação emite par de tokens (acesso e renovação).",
        "usuário bloqueado ou inativo não autentica.",
        "permissão só vale dentro do escopo declarado.",
        "toda tentativa de login é registrada em auditoria_logins.",
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Fornece", "Identificação da pessoa."),
        ("DOM-SEG", "Segurança da Informação", "Consome", "Política e controle de acesso."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Contrato de outbox."),
    ],
    "lacunas": [
        "Definir a janela de desativação do header X-Usuario-Id.",
        "Definir a rotação de segredos de assinatura do token.",
    ],
}


FICHAS["DOM-INT"] = {
    "codigo": "DOM-INT",
    "dominio": "Integração e Interoperabilidade",
    "slug": "Integracao-e-Interoperabilidade",
    "modulo": "sigmun_int",
    "prefixo": "/api/v1/int",
    "prefixo_regra": "INT",
    "schema": "int",
    "atores": [
        (
            "AT-INT-001",
            "Administrador de integração",
            "Interno",
            "Administrador",
            "Cadastra API externa, contrato e conector.",
        ),
        (
            "AT-INT-002",
            "Domínio integrador",
            "Interno",
            "Módulo SIGMUN",
            "Publica evento e consome entrega.",
        ),
        (
            "AT-INT-003",
            "Sistema externo",
            "Externo",
            "Órgão ou serviço",
            "Recebe webhook ou expõe API.",
        ),
        (
            "AT-INT-004",
            "Operação de integração",
            "Interno",
            "Equipe de operação",
            "Monitora entregas e reprocessa eventos.",
        ),
    ],
    "capacidades": [
        ("CAP-INT-001", "APIs externas", "Cadastra e controla APIs de terceiros.", "PRO-INT-001"),
        (
            "CAP-INT-002",
            "Contratos de integração",
            "Versiona contrato e seu estado.",
            "PRO-INT-002",
        ),
        ("CAP-INT-003", "Conectores", "Liga contrato aendpoint externo.", "PRO-INT-003"),
        (
            "CAP-INT-004",
            "Webhooks e entregas",
            "Recebe, registra e reprocessa entregas.",
            "PRO-INT-004",
        ),
    ],
    "processos": [
        (
            "PRO-INT-001",
            "Cadastrar API externa",
            "Registra API, autenticação e estado.",
            "RN-INT-002",
        ),
        (
            "PRO-INT-002",
            "Versionar contrato",
            "Cria e atualiza contrato de integração.",
            "RN-INT-004",
        ),
        ("PRO-INT-003", "Conectar sistema", "Cria conector vinculado ao contrato.", "—"),
        ("PRO-INT-004", "Receber entrega", "Registra webhook e processa o evento.", "—"),
    ],
    "historias": [
        (
            "HU-INT-001",
            "Como administrador, quero cadastrar uma API externa para integrar o município.",
            "CAP-INT-001",
            "Alta",
        ),
        (
            "HU-INT-002",
            "Como integrador, quero versionar o contrato para evoluir sem quebrar o consumidor.",
            "CAP-INT-002",
            "Alta",
        ),
        (
            "HU-INT-003",
            "Como sistema externo, quero receber webhook para enviar dados ao SIGMUN.",
            "CAP-INT-004",
            "Alta",
        ),
        (
            "HU-INT-004",
            "Como operação, quero reprocessar uma entrega com falha para não perder dados.",
            "CAP-INT-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-INT-001", "Rastreabilidade", "Toda entrega gera evento processado com resultado."),
        ("RNF-INT-002", "Idempotência", "Entrega repetida não duplica efeito."),
        ("RNF-INT-003", "Autenticação", "Credencial da API externa é guardada de forma protegida."),
        ("RNF-INT-004", "Versionamento", "Contrato tem versão e estado controláveis."),
        (
            "RNF-INT-005",
            "Observabilidade",
            "Falha de entrega permanece registrada para reprocessamento.",
        ),
    ],
    "regras": [
        "API externa só opera quando o contrato está publicado.",
        "credencial da API externa não é exposta na resposta.",
    ],
    "integracoes": [
        ("DOM-DAD", "Dados Corporativos", "Consome", "Qualidade e linhagem dos dados trocados."),
        ("DOM-MET", "Metadados", "Consome", "Classificação do payload."),
        ("DOM-SEG", "Segurança da Informação", "Consome", "Controle de acesso e credenciais."),
        ("DOM-GDO", "Gestão Documental", "Fornece", "Evidências da entrega."),
    ],
    "lacunas": [
        "Definir a política de reprocessamento e o limite de tentativas por entrega.",
        "Definir a janela de retenção das entregas recebidas.",
    ],
}


FICHAS["DOM-MET"] = {
    "codigo": "DOM-MET",
    "dominio": "Metadados Corporativos",
    "slug": "Metadados-Corporativos",
    "modulo": "sigmun_met",
    "prefixo": "/api/v1/met",
    "prefixo_regra": "MET",
    "schema": "met",
    "atores": [
        (
            "AT-MET-001",
            "Curador de metadados",
            "Interno",
            "Servidor público",
            "Registra e mantém metadados e valores.",
        ),
        (
            "AT-MET-002",
            "Classificador",
            "Interno",
            "Servidor público",
            "Define classificação e nível de acesso.",
        ),
        (
            "AT-MET-003",
            "Administrador de taxonomia",
            "Interno",
            "Administrador",
            "Mantém taxonomias e termos.",
        ),
        (
            "AT-MET-004",
            "Domínios consumidores",
            "Externo",
            "Módulos SIGMUN",
            "Consultam metadados para qualificar dados.",
        ),
    ],
    "capacidades": [
        (
            "CAP-MET-001",
            "Metadados",
            "Registra, consulta e ativa metadados de dado.",
            "PRO-MET-001",
        ),
        (
            "CAP-MET-002",
            "Classificação",
            "Classifica a informação e define obrigatoriedade.",
            "PRO-MET-002",
        ),
        ("CAP-MET-003", "Taxonomias", "Organiza termos e hierarquias de domínios.", "PRO-MET-003"),
        (
            "CAP-MET-004",
            "Consulta semântica",
            "Busca metadados por entidade e atributo.",
            "PRO-MET-004",
        ),
    ],
    "processos": [
        (
            "PRO-MET-001",
            "Registrar metadado",
            "Cria metadado com tipo, obrigatoriedade e escopo.",
            "RN-MET-001",
        ),
        (
            "PRO-MET-002",
            "Classificar informação",
            "Aplica classificação e define valor padrão.",
            "RN-MET-002",
        ),
        ("PRO-MET-003", "Curar taxonomia", "Cria taxonomia, termos e hierarquia.", "RN-MET-003"),
        ("PRO-MET-004", "Consultar catálogo", "Lista e busca metadados por entidade.", "—"),
    ],
    "historias": [
        (
            "HU-MET-001",
            "Como curador, quero registrar o metadado do CPF como obrigatório.",
            "CAP-MET-001",
            "Alta",
        ),
        (
            "HU-MET-002",
            "Como classificador, quero marcar o dado como sensível para restringir o acesso.",
            "CAP-MET-002",
            "Alta",
        ),
        (
            "HU-MET-003",
            "Como administrador, quero organizar termos em taxonomia para padronizar rótulos.",
            "CAP-MET-003",
            "Média",
        ),
        (
            "HU-MET-004",
            "Como domínio, quero consultar metadados por entidade para qualificar meus dados.",
            "CAP-MET-004",
            "Alta",
        ),
    ],
    "rnf": [
        ("RNF-MET-001", "Identificação", "Metadado é único por entidade e atributo."),
        ("RNF-MET-002", "Rastreabilidade", "Alteração de metadado registra autor e data."),
        ("RNF-MET-003", "Versionamento", "Valores do metadado preservam histórico."),
        (
            "RNF-MET-004",
            "Neutralidade",
            "O domínio não guarda o dado pessoal, apenas sua descrição.",
        ),
        ("RNF-MET-005", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "metadado não pode ser duplicado para a mesma entidade e atributo.",
        "classificação vigente determina o acesso e a obrigatoriedade.",
        "taxonomiaterms devem referenciar a taxonomia vigente.",
    ],
    "integracoes": [
        ("DOM-DAD", "Dados Corporativos", "Fornece", "Ativos e catálogo de dados."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Contratos com metadados da mensagem."),
        ("DOM-SEG", "Segurança da Informação", "Consome", "Classificação e controle de acesso."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Classificação de documentos."),
    ],
    "lacunas": [
        "Definir a curadoria periódica de metadados obsoletos.",
        "Definir a integração automática com o catálogo do DOM-DAD.",
    ],
}


FICHAS["DOM-SEG"] = {
    "codigo": "DOM-SEG",
    "dominio": "Segurança da Informação",
    "slug": "Seguranca-da-Informacao",
    "modulo": "sigmun_seg",
    "prefixo": "/api/v1/seg",
    "prefixo_regra": "SEG",
    "schema": "seg",
    "atores": [
        (
            "AT-SEG-001",
            "Analista de segurança",
            "Interno",
            "Servidor público",
            "Define políticas e controles de segurança.",
        ),
        (
            "AT-SEG-002",
            "Gestor de credenciais",
            "Interno",
            "Administrador",
            "Cadastra e revoga credenciais e chaves.",
        ),
        (
            "AT-SEG-003",
            "Responsável por incidente",
            "Interno",
            "Equipe de segurança",
            "Registra e conduz incidente de segurança.",
        ),
        (
            "AT-SEG-004",
            "Domínios consumidores",
            "Externo",
            "Módulos SIGMUN",
            "Consultam política e controle vigente.",
        ),
    ],
    "capacidades": [
        (
            "CAP-SEG-001",
            "Políticas de segurança",
            "Versiona e publica políticas de segurança.",
            "PRO-SEG-001",
        ),
        (
            "CAP-SEG-002",
            "Controles",
            "Registra controles preventivos, detectivos e corretivos.",
            "PRO-SEG-002",
        ),
        (
            "CAP-SEG-003",
            "Credenciais e chaves",
            "Cadastra credencial e controla chave criptográfica.",
            "PRO-SEG-003",
        ),
        (
            "CAP-SEG-004",
            "Incidentes",
            "Registra, classifica e trata incidente por severidade.",
            "PRO-SEG-004",
        ),
    ],
    "processos": [
        ("PRO-SEG-001", "Publicar política", "Cria e publica política com vigência.", "—"),
        ("PRO-SEG-002", "Avaliar controle", "Registra controle e seu estado de vigência.", "—"),
        ("PRO-SEG-003", "Gerir credencial", "Cadastra, revoga e expira credencial e chave.", "—"),
        (
            "PRO-SEG-004",
            "Tratar incidente",
            "Classifica pela severidade e registra o tratamento.",
            "—",
        ),
    ],
    "historias": [
        (
            "HU-SEG-001",
            "Como analista, quero publicar a política de acesso do SIGMUN.",
            "CAP-SEG-001",
            "Alta",
        ),
        (
            "HU-SEG-002",
            "Como gestor, quero revogar a credencial compromised.",
            "CAP-SEG-003",
            "Alta",
        ),
        (
            "HU-SEG-003",
            "Como responsável, quero classificar o incidente por severidade.",
            "CAP-SEG-004",
            "Alta",
        ),
        (
            "HU-SEG-004",
            "Como domínio, quero consultar o controle vigente para atender a política.",
            "CAP-SEG-002",
            "Média",
        ),
    ],
    "rnf": [
        (
            "RNF-SEG-001",
            "Confidencialidade",
            "Credencial nunca é exposta; apenas metadado e situação.",
        ),
        ("RNF-SEG-002", "Revogação", "Credencial e chave revogadas não podem ser reutilizadas."),
        (
            "RNF-SEG-003",
            "Auditoria",
            "Política, controle, credencial e incidente registram autor e data.",
        ),
        (
            "RNF-SEG-004",
            "Segregação",
            "Permissões do próprio domínio seguem o princípio do menor privilégio.",
        ),
        ("RNF-SEG-005", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "credencial revogada ou expirada é recusada pelo autenticação.",
        "chave criptográfica revogada não pode voltar a valer.",
        "incidente exige classificação de severidade antes do tratamento.",
    ],
    "integracoes": [
        ("DOM-IDN", "Identidade e Acesso", "Fornece", "Usuário autenticado e papéis."),
        ("DOM-MET", "Metadados", "Consome", "Classificação do dado protegido."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Evidências do incidente."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Contrato dos eventos de segurança."),
    ],
    "lacunas": [
        "Definir a rotação periódica das chaves criptográficas.",
        "Definir o prazo de retenção dos incidentes encerrados.",
    ],
}


FICHAS["DOM-PAT"] = {
    "codigo": "DOM-PAT",
    "dominio": "Gestão Patrimonial",
    "slug": "Gestao-Patrimonial",
    "modulo": "sigmun_patrimonio",
    "prefixo": "/api/v1/pat",
    "prefixo_regra": "PAT",
    "schema": "pat",
    "atores": [
        (
            "AT-PAT-001",
            "Servidor de patrimônio",
            "Interno",
            "Servidor público",
            "Cadastra, deprecia e baixa o bem.",
        ),
        (
            "AT-PAT-002",
            "Gestor de unidade",
            "Interno",
            "Gestor",
            "Autoriza e recebe transferência de bem.",
        ),
        (
            "AT-PAT-003",
            "Contabilidade",
            "Externo",
            "Setor contábil",
            "Concilia valor e baixa contábil do bem.",
        ),
    ],
    "capacidades": [
        (
            "CAP-PAT-001",
            "Cadastro de bens",
            "Registra o bem, seu tipo, valor e responsável.",
            "PRO-PAT-001",
        ),
        (
            "CAP-PAT-002",
            "Depreciação",
            "Lança depreciação e valor contábil atualizado.",
            "PRO-PAT-002",
        ),
        (
            "CAP-PAT-003",
            "Transferência",
            "Transfere o bem entre unidades e conclui a carga.",
            "PRO-PAT-003",
        ),
        ("CAP-PAT-004", "Baixa", "Baixa o bem com motivo e registro.", "PRO-PAT-004"),
    ],
    "processos": [
        (
            "PRO-PAT-001",
            "Cadastrar bem",
            "Registra o bem com tipo e valor de aquisição.",
            "RN-PAT-001",
        ),
        ("PRO-PAT-002", "Depreciar bem", "Lança a depreciação do período.", "RN-PAT-002"),
        (
            "PRO-PAT-003",
            "Transferir bem",
            "Abre e conclui a transferência entre unidades.",
            "RN-PAT-003, RN-PAT-010",
        ),
        ("PRO-PAT-004", "Baixar bem", "Baixa o bem com justificativa.", "—"),
    ],
    "historias": [
        (
            "HU-PAT-001",
            "Como servidor, quero cadastrar o bem com valor para compor o patrimônio.",
            "CAP-PAT-001",
            "Alta",
        ),
        (
            "HU-PAT-002",
            "Como servidor, quero lançar a depreciação para atualizar o valor contábil.",
            "CAP-PAT-002",
            "Média",
        ),
        (
            "HU-PAT-003",
            "Como gestor, quero transferir o bem para outra unidade.",
            "CAP-PAT-003",
            "Média",
        ),
        (
            "HU-PAT-004",
            "Como contabilidade, quero ver o bem com valor atualizado na baixa.",
            "CAP-PAT-004",
            "Média",
        ),
    ],
    "rnf": [
        (
            "RNF-PAT-001",
            "Identificação",
            "Cada bem tem identificador único e responsável definido.",
        ),
        (
            "RNF-PAT-002",
            "Rastreabilidade",
            "Cadastro, depreciação, transferência e baixa registram autor e data.",
        ),
        (
            "RNF-PAT-003",
            "Integridade",
            "Transferência em aberto impede nova transferência do mesmo bem.",
        ),
        ("RNF-PAT-004", "Contábil", "Depreciação não pode superar o valor de aquisição."),
        ("RNF-PAT-005", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "o valor de aquisição é obrigatório no cadastro do bem.",
        "a depreciação acumulada não pode superar o valor de aquisição.",
        "só um beneficiário pode ser transferido por vez.",
    ],
    "integracoes": [
        ("DOM-CON", "Contabilidade Pública", "Fornece", "Baixa contábil e conciliação."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Nota de aquisição e termo de transferência."),
        ("DOM-COM", "Compras e Contratações", "Fornece", "Bem adquisto por contratação."),
    ],
    "lacunas": [
        "Definir a tabela de depreciação por tipo de bem.",
        "Definir a integração de baixa com o DOM-CON.",
    ],
}


FICHAS["DOM-SAU"] = {
    "codigo": "DOM-SAU",
    "dominio": "Saúde Pública",
    "slug": "Saude-Publica",
    "modulo": "sigmun_saude",
    "prefixo": "/api/v1/sau",
    "prefixo_regra": "SAU",
    "schema": "sau",
    "atores": [
        (
            "AT-SAU-001",
            "Profissional de saúde",
            "Interno",
            "Servidor público",
            "Registra atendimento e agenda consulta.",
        ),
        (
            "AT-SAU-002",
            "Recepcionista",
            "Interno",
            "Servidor público",
            "Cadastra paciente e confirma agendamento.",
        ),
        (
            "AT-SAU-003",
            "Paciente",
            "Externo",
            "Cidadão",
            "Busca atendimento, agendamento e medicamento.",
        ),
        (
            "AT-SAU-004",
            "Autorizador de regulação",
            "Interno",
            "Coordenação",
            "Autoriza a regulação conforme fila e prioridade.",
        ),
    ],
    "capacidades": [
        (
            "CAP-SAU-001",
            "Cadastro de paciente",
            "Registra paciente e seu vínculo de identidade.",
            "PRO-SAU-001",
        ),
        (
            "CAP-SAU-002",
            "Agenda e atendimento",
            "Agenda, confirma, realiza e registra atendimento.",
            "PRO-SAU-002",
        ),
        (
            "CAP-SAU-003",
            "Regulação",
            "Solicita e autoriza encaminhamento por prioridade.",
            "PRO-SAU-003",
        ),
        (
            "CAP-SAU-004",
            "Medicamentos",
            "Mantém medicamento e registra dispensação.",
            "PRO-SAU-004",
        ),
    ],
    "processos": [
        (
            "PRO-SAU-001",
            "Cadastrar paciente",
            "Registra paciente com documento e contato.",
            "RN-SAU-001",
        ),
        (
            "PRO-SAU-002",
            "Atender paciente",
            "Agenda, confirma e registra o atendimento.",
            "RN-SAU-010",
        ),
        (
            "PRO-SAU-003",
            "Regular acesso",
            "Solicita e autoriza a regulação.",
            "RN-SAU-020, RN-SAU-030",
        ),
        ("PRO-SAU-004", "Dispensar medicamento", "Registra dispensação ao paciente.", "RN-SAU-040"),
    ],
    "historias": [
        (
            "HU-SAU-001",
            "Como recepcionista, quero cadastrar o paciente para atendê-lo.",
            "CAP-SAU-001",
            "Alta",
        ),
        (
            "HU-SAU-002",
            "Como profissional, quero agendar e registrar o atendimento.",
            "CAP-SAU-002",
            "Alta",
        ),
        (
            "HU-SAU-003",
            "Como autorizador, quero ordenar a fila por prioridade.",
            "CAP-SAU-003",
            "Alta",
        ),
        (
            "HU-SAU-004",
            "Como paciente, quero receber o medicamento registrado.",
            "CAP-SAU-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-SAU-001", "Sigilo", "Prontuário é dado sensível (LGPD), com acesso por perfil."),
        ("RNF-SAU-002", "Identificação", "Paciente é identificado por documento oficial único."),
        (
            "RNF-SAU-003",
            "Rastreabilidade",
            "Atendimento, agendamento e dispensação registram autor e data.",
        ),
        ("RNF-SAU-004", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "o paciente é identificado por documento oficial e é único no cadastro.",
        "agendamento confirmado exige paciente ativo e data disponível.",
        "a regulação é autorizada conforme a prioridade registrada.",
        "a dispensação referencia o paciente e o medicamento administered.",
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Fornece", "Identificação da pessoa."),
        ("DOM-GDO", "Gestão Documental", "Fornece", "Laudo e documento de encaminhamento."),
        ("DOM-MET", "Metadados", "Consome", "Classificação do dado sensível."),
    ],
    "lacunas": [
        "Definir a integração com o prontuário estadual.",
        "Definir a regra de dispensação por tipo de medicamento.",
    ],
}


FICHAS["DOM-EDU"] = {
    "codigo": "DOM-EDU",
    "dominio": "Educação Pública",
    "slug": "Educacao-Publica",
    "modulo": "sigmun_educacao",
    "prefixo": "/api/v1/edu",
    "prefixo_regra": "EDU",
    "schema": "edu",
    "atores": [
        (
            "AT-EDU-001",
            "Secretaria de Educação",
            "Interno",
            "Órgão gestor",
            "Mantém rotas, itens de merenda e regras.",
        ),
        (
            "AT-EDU-002",
            "Diretor de escola",
            "Interno",
            "Servidor público",
            "Matrícula, transfere e conclui aluno.",
        ),
        (
            "AT-EDU-003",
            "Professor",
            "Interno",
            "Servidor público",
            "Registra lançamento no diário.",
        ),
        (
            "AT-EDU-004",
            "Aluno e família",
            "Externo",
            "Cidadão",
            "Acompanha matrícula, merenda e transporte.",
        ),
    ],
    "capacidades": [
        ("CAP-EDU-001", "Cadastro de aluno", "Registra aluno e sua identidade.", "PRO-EDU-001"),
        ("CAP-EDU-002", "Matrícula", "Matrícula, transfere, cancela e conclui.", "PRO-EDU-002"),
        ("CAP-EDU-003", "Diário escolar", "Registra presença e lançamento.", "PRO-EDU-003"),
        (
            "CAP-EDU-004",
            "Merenda e transporte",
            "Itens de merenda, distribuição e rotas.",
            "PRO-EDU-004",
        ),
    ],
    "processos": [
        ("PRO-EDU-001", "Cadastrar aluno", "Registra aluno com documento e escola.", "RN-EDU-001"),
        (
            "PRO-EDU-002",
            "Movimentar matrícula",
            "Matrícula, transfere, cancela e conclui.",
            "RN-EDU-010, RN-EDU-020",
        ),
        ("PRO-EDU-003", "Lançar no diário", "Registra presença e conteúdo.", "RN-EDU-030"),
        (
            "PRO-EDU-004",
            "Atender merenda e transporte",
            "Distribui merenda e passagem de transporte.",
            "RN-EDU-040",
        ),
    ],
    "historias": [
        ("HU-EDU-001", "Como diretor, quero matricular o aluno na escola.", "CAP-EDU-002", "Alta"),
        (
            "HU-EDU-002",
            "Como diretor, quero transferir a matrícula quando o aluno mudar de escola.",
            "CAP-EDU-002",
            "Média",
        ),
        (
            "HU-EDU-003",
            "Como professor, quero registrar presença no diário.",
            "CAP-EDU-003",
            "Alta",
        ),
        (
            "HU-EDU-004",
            "Como secretaria,quero controlar as rotas de transporte.",
            "CAP-EDU-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-EDU-001", "Identificação", "Aluno é identificado por documento oficial único."),
        ("RNF-EDU-002", "Rastreabilidade", "Matrícula e lançamento registram autor e data."),
        ("RNF-EDU-003", "Menor idade", "Diário e merenda consideram o ano letivo vigente."),
        ("RNF-EDU-004", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "o aluno só pode ter matrícula ativa em uma escola por vez.",
        "a transferência exige matrícula concluída na origem.",
        "o lançamento no diário referencia a matrícula ativa.",
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Fornece", "Identificação do aluno."),
        ("DOM-TEL", "Gestão Territorial", "Fornece", "Bairro e rota territorial."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Declaração de matrícula e laudos."),
    ],
    "lacunas": [
        "Definir a regra de elegibilidade à merenda.",
        "Definir a integração com o sistema estadual de educação.",
    ],
}


FICHAS["DOM-FRO"] = {
    "codigo": "DOM-FRO",
    "dominio": "Gestão de Frota",
    "slug": "Gestao-de-Frota",
    "modulo": "sigmun_frotas",
    "prefixo": "/api/v1/fro",
    "prefixo_regra": "FRO",
    "schema": "fro",
    "atores": [
        (
            "AT-FRO-001",
            "Motorista",
            "Interno",
            "Servidor público",
            "Usa o veículo e registra abastecimento.",
        ),
        (
            "AT-FRO-002",
            "Gestor de frota",
            "Interno",
            "Administrador",
            "Cadastra veículo, abre manutenção e baixa.",
        ),
        (
            "AT-FRO-003",
            "Operador de oficina",
            "Externo",
            " prestador",
            "Executa a manutenção e informa a conclusão.",
        ),
    ],
    "capacidades": [
        (
            "CAP-FRO-001",
            "Cadastro de veículos",
            "Registra veículo, tipo, combustível e situação.",
            "PRO-FRO-001",
        ),
        ("CAP-FRO-002", "Abastecimento", "Registra abastecimento e quilometragem.", "PRO-FRO-002"),
        ("CAP-FRO-003", "Manutenção", "Abre e conclui manutenção do veículo.", "PRO-FRO-003"),
        ("CAP-FRO-004", "Rotas", "Registra e conclui rota de deslocamento.", "PRO-FRO-004"),
    ],
    "processos": [
        ("PRO-FRO-001", "Cadastrar veículo", "Registra veículo e seu responsável.", "RN-FRO-001"),
        (
            "PRO-FRO-002",
            "Abastecer",
            "Registra abastecimento com litros e quilometragem.",
            "RN-FRO-002",
        ),
        ("PRO-FRO-003", "Manter veículo", "Abre e conclui manutenção.", "—"),
        ("PRO-FRO-004", "Usar em rota", "Registra e conclui rota.", "—"),
    ],
    "historias": [
        (
            "HU-FRO-001",
            "Como gestor, quero cadastrar o veículo com placa e tipo.",
            "CAP-FRO-001",
            "Alta",
        ),
        ("HU-FRO-002", "Como motorista, quero registrar o abastecimento.", "CAP-FRO-002", "Alta"),
        (
            "HU-FRO-003",
            "Como gestor, quero abrir a manutenção para corrigir o veículo.",
            "CAP-FRO-003",
            "Média",
        ),
        (
            "HU-FRO-004",
            "Como gestor, quero baixar o veículo quando ele for alienado.",
            "CAP-FRO-001",
            "Baixa",
        ),
    ],
    "rnf": [
        ("RNF-FRO-001", "Identificação", "Veículo é identificado por placa única."),
        (
            "RNF-FRO-002",
            "Rastreabilidade",
            "Abastecimento, manutenção e rota registram autor e data.",
        ),
        ("RNF-FRO-003", "Consumo", "Abastecimento exige combustível compatível com o veículo."),
        ("RNF-FRO-004", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "a placa do veículo é única no cadastro.",
        "o abastecimento referencia o veículo e a quilometragem.",
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Fornece", "Identificação do motorista."),
        ("DOM-PAT", "Gestão Patrimonial", "Fornece", "Bens móveis correlatos."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Nota de abastecimento e ordem de serviço."),
    ],
    "lacunas": [
        "Definir a integração com o sistema de controle de combustível.",
        "Definir o plano de manutenção preventiva por quilometragem.",
    ],
}


FICHAS["DOM-TRI"] = {
    "codigo": "DOM-TRI",
    "dominio": "Administração Tributária",
    "slug": "Administracao-Tributaria",
    "modulo": "sigmun_tributos",
    "prefixo": "/api/v1/tri",
    "prefixo_regra": "TRI",
    "schema": "trib",
    "atores": [
        (
            "AT-TRI-001",
            "Contribuinte",
            "Externo",
            "Cidadão ou empresa",
            "É cadastrado e recebe lançamentos.",
        ),
        (
            "AT-TRI-002",
            "Fiscal tributário",
            "Interno",
            "Servidor público",
            "Lança, audita e inscreve em dívida ativa.",
        ),
        (
            "AT-TRI-003",
            "Arrecadador",
            "Interno",
            "Servidor público",
            "Registra pagamento e emite certidão.",
        ),
    ],
    "capacidades": [
        (
            "CAP-TRI-001",
            "Cadastro de contribuinte",
            "Registra pessoa física ou jurídica.",
            "PRO-TRI-001",
        ),
        (
            "CAP-TRI-002",
            "Cadastro de imóvel",
            "Registra imóvel e sua base de cálculo.",
            "PRO-TRI-002",
        ),
        (
            "CAP-TRI-003",
            "Lançamento e pagamento",
            "Lança crédito e registra pagamento.",
            "PRO-TRI-003",
        ),
        (
            "CAP-TRI-004",
            "Dívida ativa e certidão",
            "Inscreve, baixa e emite certidão.",
            "PRO-TRI-004",
        ),
    ],
    "processos": [
        (
            "PRO-TRI-001",
            "Cadastrar contribuinte",
            "Registra contribuinte com documento.",
            "RN-TRI-001",
        ),
        (
            "PRO-TRI-002",
            "Cadastrar imóvel",
            "Registra imóvel e vincula contribuinte.",
            "RN-TRI-010, RN-TRI-011",
        ),
        (
            "PRO-TRI-003",
            "Lançar e pagar",
            "Lança crédito e registra pagamento.",
            "RN-TRI-020, RN-TRI-021, RN-TRI-022",
        ),
        (
            "PRO-TRI-004",
            "Inscrever em dívida ativa",
            "Inscreve, baixa e emite certidão.",
            "RN-TRI-030, RN-TRI-031, RN-TRI-040",
        ),
    ],
    "historias": [
        ("HU-TRI-001", "Como fiscal, quero lançar o tributo do imóvel.", "CAP-TRI-003", "Alta"),
        (
            "HU-TRI-002",
            "Como fiscal, quero registrar o pagamento com data.",
            "CAP-TRI-003",
            "Alta",
        ),
        ("HU-TRI-003", "Como fiscal, quero inscrever em dívida ativa.", "CAP-TRI-004", "Média"),
        (
            "HU-TRI-004",
            "Como contribuinte, quero obter certidão de débitos.",
            "CAP-TRI-004",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-TRI-001", "Identificação", "Contribuinte é identificado por CPF ou CNPJ único."),
        ("RNF-TRI-002", "Imutabilidade", "Lançamento pago ou inscrito não recebe novo pagamento."),
        (
            "RNF-TRI-003",
            "Rastreabilidade",
            "Lançamento, pagamento e inscrição registram autor e data.",
        ),
        ("RNF-TRI-004", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Fornece", "Identificação do contribuinte."),
        ("DOM-TEL", "Gestão Territorial", "Fornece", "Base territorial do imóvel."),
        ("DOM-GEO", "Geoinformação Municipal", "Fornece", "Planta de valores vigente."),
        ("DOM-CON", "Contabilidade Pública", "Fornece", "Baixa contábil do lançamento."),
    ],
    "lacunas": [
        "Definir o convênio de cobrança com o banco BV ou tributário.",
        "Definir a regra de atualização de valores da dívida ativa.",
    ],
}


FICHAS["DOM-ORC"] = {
    "codigo": "DOM-ORC",
    "dominio": "Orçamento Público",
    "slug": "Orcamento-Publico",
    "modulo": "sigmun_orc",
    "prefixo": "/api/v1/orc",
    "prefixo_regra": "ORC",
    "schema": "orc",
    "atores": [
        (
            "AT-ORC-001",
            "Elaborador do orçamento",
            "Interno",
            "Servidor público",
            "Elabora PPA, LDO e LOA.",
        ),
        (
            "AT-ORC-002",
            "Ordenador de despesa",
            "Interno",
            "Autoridade competente",
            "Aprova o orçamento e a suplementação.",
        ),
        (
            "AT-ORC-003",
            "Contabilidade",
            "Externo",
            "Setor contábil",
            "Executa dotação, reserva e empenho.",
        ),
        ("AT-ORC-004", "Cidadão", "Externo", "Cidadão", "Consulta a execução orçamentária."),
    ],
    "capacidades": [
        ("CAP-ORC-001", "Planejamento orçamentário", "Elabora PPA, LDO e LOA.", "PRO-ORC-001"),
        (
            "CAP-ORC-002",
            "Dotação e reserva",
            "Autoriza, suplementa, anula e reserva saldo.",
            "PRO-ORC-002",
        ),
        ("CAP-ORC-003", "Execução", "Acompanha a execução do orçamento autorizado.", "PRO-ORC-003"),
    ],
    "processos": [
        (
            "PRO-ORC-001",
            "Elaborar instrumento",
            "Cria PPA, LDO ou LOA e encaminha para publicação.",
            "RN-ORC-001, RN-ORC-010, RN-ORC-020",
        ),
        (
            "PRO-ORC-002",
            "Autorizar e suplementar",
            "Aprova a LOA e suplementa a dotação.",
            "RN-ORC-011, RN-ORC-021",
        ),
        (
            "PRO-ORC-003",
            "Reservar saldo",
            "Reserva e cancela saldo de dotação.",
            "RN-ORC-030, RN-ORC-031",
        ),
        (
            "PRO-ORC-004",
            "Encerrar exercício",
            "Encerra dotação e reserva do exercício.",
            "RN-ORC-040",
        ),
    ],
    "historias": [
        (
            "HU-ORC-001",
            "Como elaborador, quero criar a LOA para aprovar o orçamento do ano.",
            "CAP-ORC-001",
            "Alta",
        ),
        (
            "HU-ORC-002",
            "Como ordenador, quero suplementar a dotação para cobrir despesa unforeseen.",
            "CAP-ORC-002",
            "Alta",
        ),
        (
            "HU-ORC-003",
            "Como contabilidade, quero reservar saldo antes do empenho.",
            "CAP-ORC-002",
            "Média",
        ),
        (
            "HU-ORC-004",
            "Como cidadão, quero consultar o orçamento publicado.",
            "CAP-ORC-003",
            "Média",
        ),
    ],
    "rnf": [
        ("RNF-ORC-001", "Legalidade", "Instrumento só avança na sequência PPA, LDO e LOA."),
        ("RNF-ORC-002", "Exclusividade", "Reserva não pode superar o saldo da dotação."),
        ("RNF-ORC-003", "Rastreabilidade", "Dotação e reserva registram autor e data."),
        ("RNF-ORC-004", "Transparência", "Instrumento publicado é de consulta pública."),
    ],
    "regras": [
        "o quadriênio da PPA é exato (RN-ORC-001).",
        "a LOA só pode ser sancionada sobre LDO vigente.",
        "a reserva respeita o saldo disponível da dotação.",
    ],
    "integracoes": [
        ("DOM-PLA", "Planejamento Governamental", "Fornece", "Plano/programa a que se vincula."),
        ("DOM-CON", "Contabilidade Pública", "Fornece", "Empenho, liquidação e pagamento."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Instrumento publicado e anexos."),
        ("DOM-IND", "Indicadores e Desempenho", "Fornece", "Acompanhamento da execução."),
    ],
    "lacunas": [
        "API registrada em src/main.py (resolvido): 12 operações expostas em /api/v1/orc.",
        "Definir a integração com o sistema de SIMEOR de orçamento.",
    ],
}


FICHAS["DOM-DAD"] = {
    "codigo": "DOM-DAD",
    "dominio": "Dados Corporativos",
    "slug": "Dados-Corporativos",
    "modulo": "sigmun_dad",
    "prefixo": "/api/v1/dad",
    "prefixo_regra": "DAD",
    "schema": "dad",
    "atores": [
        (
            "AT-DAD-001",
            "Curador de dados",
            "Interno",
            "Servidor público",
            "Cadastra ativo e mantém metadado de origem.",
        ),
        (
            "AT-DAD-002",
            "Responsável pela qualidade",
            "Interno",
            "Servidor público",
            "Avalia e atualiza a qualidade do dado.",
        ),
        (
            "AT-DAD-003",
            "Domínio consumidor",
            "Externo",
            "Módulo SIGMUN",
            "Consulta o catálogo e publica seu ativo de dado.",
        ),
        (
            "AT-DAD-004",
            "Auditor de dados",
            "Externo",
            "Controle interno",
            "Consulta linhagem e rastro de alteração.",
        ),
    ],
    "capacidades": [
        (
            "CAP-DAD-001",
            "Catálogo de ativos",
            "Registra e cataloga os ativos de dado do município.",
            "PRO-DAD-001",
        ),
        (
            "CAP-DAD-002",
            "Qualidade do dado",
            "Avalia dimensões e nível de qualidade.",
            "PRO-DAD-002",
        ),
        (
            "CAP-DAD-003",
            "Linhagem",
            "Registra a origem e as transformações do dado.",
            "PRO-DAD-003",
        ),
        (
            "CAP-DAD-004",
            "Políticas de dados",
            "Versiona a política de gestão e uso de dados.",
            "PRO-DAD-004",
        ),
    ],
    "processos": [
        (
            "PRO-DAD-001",
            "Publicar ativo de dado",
            "Cadastra o ativo, cataloga e ativa.",
            "RN-DAD-001",
        ),
        (
            "PRO-DAD-002",
            "Avaliar qualidade",
            "Atualiza dimensões e nível de qualidade.",
            "RN-DAD-002",
        ),
        (
            "PRO-DAD-003",
            "Rastrear linhagem",
            "Registra origem e transformação do dado.",
            "RN-DAD-003",
        ),
        ("PRO-DAD-004", "Versionar política", "Cria e publica a política de dados.", "RN-DAD-004"),
    ],
    "historias": [
        (
            "HU-DAD-001",
            "Como domínio, quero publicar meu ativo de dado no catálogo.",
            "CAP-DAD-001",
            "Alta",
        ),
        (
            "HU-DAD-002",
            "Como curador, quero avaliar a qualidade do dado periodicamente.",
            "CAP-DAD-002",
            "Média",
        ),
        ("HU-DAD-003", "Como auditor, quero ver de onde veio o dado.", "CAP-DAD-003", "Média"),
        (
            "HU-DAD-004",
            "Como curador, quero desativar o ativo quando o domínio sai de uso.",
            "CAP-DAD-001",
            "Baixa",
        ),
    ],
    "rnf": [
        ("RNF-DAD-001", "Autodescrição", "Todo ativo declara dono, origem e metadados."),
        ("RNF-DAD-002", "Rastreabilidade", "Ativo, qualidade e linhagem registram autor e data."),
        ("RNF-DAD-003", "Neutralidade", "O catálogo guarda descrição, não o dado pessoal em si."),
        ("RNF-DAD-004", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "o ativo de dado fica ativo somente após ser publicado no catálogo.",
        "a avaliação de qualidade exige as dimensões avaliadas.",
        "a linhagem referencia a origem do dado.",
    ],
    "integracoes": [
        ("DOM-MET", "Metadados Corporativos", "Fornece", "Metadados e classificação."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Contrato com o ativo de dado."),
        ("DOM-SEG", "Segurança da Informação", "Consome", "Classificação do ativo."),
    ],
    "lacunas": [
        "Definir o calendário de avaliação de qualidade por criticidade do ativo.",
        "Definir a integração automática de metadados com o DOM-MET.",
    ],
}


FICHAS["DOM-PES"] = {
    "codigo": "DOM-PES",
    "dominio": "Gestão de Pessoas",
    "slug": "Gestao-de-Pessoas",
    "modulo": "sigmun_rh",
    "prefixo": "/api/v1/pes",
    "prefixo_regra": "PES",
    "schema": "rh",
    "atores": [
        (
            "AT-PES-001",
            "Servidor público",
            "Interno",
            "Servidor",
            "Cadastra férias, frequência e lotação.",
        ),
        (
            "AT-PES-002",
            "Gestor de pessoas",
            "Interno",
            "Gestor",
            "Admite, afasta, desliga e lota o servidor.",
        ),
        (
            "AT-PES-003",
            "Contabilidade",
            "Externo",
            "Setor contábil",
            "Consolida, fecha e paga a folha.",
        ),
        (
            "AT-PES-004",
            "Gestor da unidade",
            "Externo",
            "Órgão",
            "Confirma o desempenho e a lotação.",
        ),
    ],
    "capacidades": [
        ("CAP-PES-001", "Cargos", "Mantém cargos, níveis e salário base.", "PRO-PES-001"),
        (
            "CAP-PES-002",
            "Servidores",
            "Admissão, afastamento, reativação e desligamento.",
            "PRO-PES-002",
        ),
        ("CAP-PES-003", "Lotação", "Lota o servidor em unidade administrativa.", "PRO-PES-003"),
        (
            "CAP-PES-004",
            "Folha e férias",
            "Consolida folha e conduz o período de férias.",
            "PRO-PES-004",
        ),
        ("CAP-PES-005", "Frequência", "Registra presença, falta e justificativa.", "PRO-PES-005"),
    ],
    "processos": [
        (
            "PRO-PES-001",
            "Admitir servidor",
            "Cadastra matrícula, cargo e data de admissão.",
            "RN-PES-010, RN-PES-011",
        ),
        (
            "PRO-PES-002",
            "Lotar servidor",
            "Define unidade e cargo de lotação.",
            "RN-PES-020, RN-PES-021",
        ),
        (
            "PRO-PES-003",
            "Fechar folha",
            "Consolida, fecha, homologa e paga.",
            "RN-PES-030 a RN-PES-033",
        ),
        (
            "PRO-PES-004",
            "Conceder férias",
            "Planeja, aprova, inicia e conclui o gozo.",
            "RN-PES-040, RN-PES-041",
        ),
        (
            "PRO-PES-005",
            "Registrar frequência",
            "Aponta presença, falta e justificativa.",
            "RN-PES-050",
        ),
    ],
    "historias": [
        (
            "HU-PES-001",
            "Como gestor, quero admitir o servidor com cargo e matrícula.",
            "CAP-PES-002",
            "Alta",
        ),
        (
            "HU-PES-002",
            "Como gestor, quero lotar o servidor na unidade que o recebe.",
            "CAP-PES-003",
            "Alta",
        ),
        ("HU-PES-003", "Como contabilidade, quero fechar a folha do mês.", "CAP-PES-004", "Alta"),
        (
            "HU-PES-004",
            "Como servidor, quero registrar minha falta com justificativa.",
            "CAP-PES-005",
            "Média",
        ),
        ("HU-PES-005", "Como servidor, quero planejar minhas férias.", "CAP-PES-004", "Média"),
    ],
    "rnf": [
        ("RNF-PES-001", "Identificação", "Matrícula e CPF do servidor são únicos."),
        ("RNF-PES-002", "Imutabilidade", "Folha homologada ou paga é terminal."),
        (
            "RNF-PES-003",
            "Rastreabilidade",
            "Admissão, lotação, folha e férias registram autor e data.",
        ),
        ("RNF-PES-004", "Sigilo", "Remuneração e frequência são dados pessoais (LGPD)."),
        ("RNF-PES-005", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "integracoes": [
        ("DOM-CUM", "Cadastro Único Municipal", "Consome", "Identificação da pessoa."),
        ("DOM-TEL", "Gestão Territorial", "Consome", "Unidade administrativa de lotação."),
        ("DOM-DIA", "Diárias e Viagens", "Fornece", "Servidor em viagem."),
        ("DOM-CON", "Contabilidade Pública", "Fornece", "Lançamento da remuneração."),
    ],
    "lacunas": [
        "Definir a integração do SIGRH ou sistema estadual de folha.",
        "Definir o calendário de férias por mês de gozo.",
    ],
}


# ==============================================================================
# FICHAS AUTOMÁTICAS — domínios documentais a partir do gerador de PUML
# ==============================================================================

ROLES_PADRAO = {
    "ANA": ("Analista de dados", "Consumidor analítico"),
    "CPT": ("Responsável por compétences", "Servidor público"),
    "DEC": ("Gestor de desenvolvimento econômico", "Empreendedor"),
    "GOV": ("Comitê de governança", "Servidor público"),
    "IND": ("Responsável por indicadores", "Gestor municipal"),
    "INF": ("Administrador de infraestrutura", "Analista de sistemas"),
    "MAM": ("Fiscal ambiental", "Cidadão"),
    "MOB": ("Técnico de campo", "Cidadão"),
    "PLA": ("Equipe de planejamento", "Gestor municipal"),
    "ATE": ("Atendente", "Cidadão"),
}

RNF_PADRAO = [
    ("RNF-{p}-001", "Rastreabilidade", "Toda alteração registra autor e data."),
    ("RNF-{p}-002", "Sigilo", "Dados pessoais seguem a LGPD e a classificação da informação."),
    ("RNF-{p}-003", "Compatibilidade", "Sem chave estrangeira entre schemas de domínios."),
    ("RNF-{p}-004", "Transparência", "Decisão e evidência ficam registradas para consulta."),
]


def slug_do_dominio(codigo: str) -> str:
    """Slug usado nos nomes de arquivo do domínio (`...-<slug>.md`)."""
    base = RAIZ / "SIGMUN-Docs" / codigo
    titulos = [
        "Mapa-de-Atores",
        "Mapa-de-Capacidades",
        "Mapa-de-Processos",
        "Mapa-de-Servicos",
        "Casos-de-Uso",
        "Historias-de-Usuario",
        "Regras-de-Negocio",
        "Requisitos-Funcionais",
        "Requisitos-Nao-Funcionais",
        "Especificacoes",
        "Criterios-de-Aceitacao",
        "Matriz-de-Rastreabilidade",
        "Modelo-de-Dados",
        "Modelo-de-Integracao",
        "Arquitetura-de-Servicos",
        "Modelo-de-Seguranca",
        "Modelo-de-Auditoria",
        "Plano-de-Testes",
        "Casos-de-Teste",
        "Plano-de-Implantacao",
        "Checklist-de-Prontidao-para-Producao",
        "Plano-de-Migracao-de-Dados",
        "Plano-de-Treinamento",
        "Plano-de-Suporte-e-Operacao",
        "Estrutura-Tecnica",
        "Modelo-de-Dominio",
    ]
    for arquivo in sorted(base.glob("0[0-2][0-9]-*.md")):
        resto = arquivo.stem.split("-", 1)[1]
        for titulo in titulos:
            if resto == titulo or resto.startswith(f"{titulo}-"):
                return resto[len(titulo) :].lstrip("-") or codigo
    return codigo


FICHAS["DOM-ATE"] = {
    "codigo": "DOM-ATE",
    "dominio": "Atendimento ao Cidadão",
    "slug": slug_do_dominio("DOM-ATE"),
    "modulo": "sigmun_ate",
    "prefixo": "/api/v1/ate",
    "prefixo_regra": "ATE",
    "schema": "ate",
    "atores": [
        (
            "AT-ATE-001",
            "Cidadão",
            "Externo",
            "Cidadão",
            "Solicita, acompanha e avalia o atendimento.",
        ),
        (
            "AT-ATE-002",
            "Atendente",
            "Interno",
            "Servidor público",
            "Triagem, senha e encaminhamento.",
        ),
        (
            "AT-ATE-003",
            "Guichê",
            "Interno",
            "Posto de atendimento",
            "Executa o atendimento chamado.",
        ),
        (
            "AT-ATE-004",
            "Coordenação do atendimento",
            "Interno",
            "Gestor",
            "Organiza filas, serviços e unidades.",
        ),
    ],
    "capacidades": [
        (
            "CAP-ATE-001",
            "Triagem do atendimento",
            "Identifica serviço, prioridade e necessidade de encaminhamento.",
            "PRO-ATE-001",
        ),
        (
            "CAP-ATE-002",
            "Gestão de senhas e filas",
            "Emite senha, posiciona na fila e chama o atendimento.",
            "PRO-ATE-002",
        ),
        (
            "CAP-ATE-003",
            "Registro de atendimento",
            "Registra o atendimento realizado e a conclusão.",
            "PRO-ATE-003",
        ),
        (
            "CAP-ATE-004",
            "Avaliação do atendimento",
            "Coleta a nota e o comentário do cidadão.",
            "PRO-ATE-004",
        ),
    ],
    "processos": [
        (
            "PRO-ATE-001",
            "Triar solicitação",
            "Classifica serviço e prioridade na chegada.",
            "RN-ATE-001",
        ),
        (
            "PRO-ATE-002",
            "Emitir e chamar senha",
            "Posiciona na fila e chama o guichê.",
            "RN-ATE-002",
        ),
        ("PRO-ATE-003", "Registrar atendimento", "Executa e registra o atendimento.", "RN-ATE-003"),
        (
            "PRO-ATE-004",
            "Avaliar e encaminhar",
            "Avalia satisfação e encaminha quando necessário.",
            "RN-ATE-004",
        ),
    ],
    "historias": [
        (
            "HU-ATE-001",
            "Como cidadão, quero retirar senha e ser chamado no guichê.",
            "CAP-ATE-002",
            "Alta",
        ),
        (
            "HU-ATE-002",
            "Como atendente, quero ver a triagem antes de iniciar o atendimento.",
            "CAP-ATE-001",
            "Alta",
        ),
        (
            "HU-ATE-003",
            "Como cidadão, quero avaliar o atendimento recebido.",
            "CAP-ATE-004",
            "Média",
        ),
    ],
    "rnf": [
        (
            "RNF-ATE-001",
            "Rastreabilidade",
            "Atendimento, senha e avaliação registram autor e data.",
        ),
        ("RNF-ATE-002", "Acessibilidade", "Chamada por painel e por número em áudio."),
        ("RNF-ATE-003", "Compatibilidade", "Sem chave estrangeira entre schemas."),
    ],
    "regras": [
        "a triagem identifica serviço, canal e prioridade.",
        "a fila respeita prioridade e ordem de chegada.",
        "o registro do atendimento exige o guichê que o executou.",
        "a avaliação registra nota e comentário do cidadão.",
    ],
    "integracoes": [
        ("DOM-IDN", "Identidade e Acesso", "Consome", "Autenticação do cidadão e do atendente."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "Consulta de agenda e disponibilidade."),
        ("DOM-MET", "Metadados", "Consome", "Classificação da informação coletada."),
    ],
    "lacunas": [
        "Definir o contrato de integração com a agenda municipal.",
        "Validar o modelo proposto com a área de atendimento antes do início da implementação.",
    ],
}


def ficha_automatica(
    codigo: str,
    nome: str,
    capacidades: list,
    processos: list,
    regras: list,
    correlatos: list,
    lacunas: list,
) -> dict:
    """Ficha mínima para domínios documentais, com papéis e RNFs padrão."""
    sigla = codigo.split("-")[1]
    papel_a, papel_b = ROLES_PADRAO.get(sigla, ("Responsável", "Usuário"))
    correspondencia = CORRESPONDENCIAS_DOM_MODULO.get(codigo, {})
    return {
        "codigo": codigo,
        "dominio": nome,
        "slug": slug_do_dominio(codigo),
        "modulo": correspondencia.get("modulo"),
        "codigo_modulo": correspondencia.get("codigo_modulo"),
        "prefixo": f"/api/v1/{sigla.lower()}",
        "prefixo_regra": sigla,
        "schema": sigla.lower(),
        "atores": [
            (
                f"AT-{sigla}-001",
                f"Responsável — {papel_a}",
                "Interno",
                papel_a,
                f"Conduz as atividades do domínio {nome}.",
            ),
            (
                f"AT-{sigla}-002",
                f"Usuário — {papel_b}",
                "Externo",
                papel_b,
                "Utiliza os serviços do domínio.",
            ),
            (
                f"AT-{sigla}-003",
                "Domínios consumidores",
                "Externo",
                "Módulos SIGMUN",
                "Consomem os dados e serviços publicados.",
            ),
        ],
        "capacidades": capacidades,
        "processos": processos,
        "historias": [
            (
                f"HU-{sigla}-{i:03d}",
                f"Como usuário, quero {c[1].lower()} para atender a necessidade do domínio.",
                c[0],
                "Alta" if i <= 3 else "Média",
            )
            for i, c in enumerate(capacidades, start=1)
        ],
        "rnf": [(i.replace("{p}", sigla), t, d) for i, t, d in RNF_PADRAO],
        "integracoes": [
            (
                c[0],
                c[1],
                "Fornece" if i % 2 else "Consome",
                (c[3] if len(c) > 3 else "integração registrada no mapa de domínios"),
            )
            for i, c in enumerate(correlatos, start=1)
        ],
        "regras": [r[1] for r in regras],
        "lacunas": lacunas,
    }


def registrar_fichas_documentais() -> None:
    """Cria fichas dos domínios documentais a partir de `gerar_puml_dominios`."""
    try:
        import gerar_puml_dominios as diagramas
    except ModuleNotFoundError:  # pragma: no cover
        return
    for item in getattr(diagramas, "PROPOSTOS", []):
        codigo = item["codigo"]
        if codigo in FICHAS:
            continue
        sigla = codigo.removeprefix("DOM-")
        capacidades = [
            (
                f"CAP-{sigla}-{indice:03d}",
                nome_capacidade,
                "Capacidade proposta; descrição detalhada a validar na implementação do domínio.",
                "—",
            )
            for indice, nome_capacidade in enumerate(item["capacidades"], start=1)
        ]
        processos = [
            (
                f"PRO-{sigla}-{indice:03d}",
                nome_processo,
                "Processo proposto; descrição detalhada a validar na implementação do domínio.",
                "—",
            )
            for indice, nome_processo in enumerate(item["processos"], start=1)
        ]
        regras = [(r[0], r[1]) for r in item["regras"]]
        correlatos = [(c[0], c[1]) for c in item["correlatos"]]
        FICHAS[codigo] = ficha_automatica(
            codigo,
            item["nome"],
            capacidades,
            processos,
            regras,
            correlatos,
            item.get("lacunas", []) or ["Definir as lacunas de escopo na validação do domínio."],
        )


# ==============================================================================
# MODO PROPOSTO — domínios sem implementação
# ==============================================================================


def tabelas_do_puml(caminho: Path) -> dict[str, dict]:
    """`(tabela) -> colunas` a partir de um `005-Persistencia.puml`."""
    if not caminho.exists():
        return {}
    texto = caminho.read_text(encoding="utf-8")
    padrao = 'entity "(\\w+)" as T?(\\w+) \\{\\n(.*?)\\n\\s*\\}'
    blocos = re.findall(padrao, texto, re.DOTALL)
    saida: dict[str, dict] = {}
    for tabela, _alias, corpo in blocos:
        colunas = []
        for linha in corpo.splitlines():
            limpa = linha.strip()
            if not limpa or limpa == "--":
                continue
            nome = limpa.split(":")[0].strip()
            tipo = limpa.split(":")[1].strip().split(" ")[0] if ":" in limpa else "TEXT"
            flags = re.findall(r"PK|UQ|NN", limpa)
            colunas.append({"nome": nome, "tipo": tipo, "flags": flags})
        saida[tabela] = {"classe": "", "colunas": colunas, "schema": "", "doc": ""}
    return saida


def enums_do_puml(caminho: Path) -> dict[str, list[tuple[str, str]]]:
    """`Enum -> [(membro, valor)]` a partir de um `001-Modelo-de-Dominio.puml`."""
    if not caminho.exists():
        return {}
    texto = caminho.read_text(encoding="utf-8")
    saida: dict[str, list[tuple[str, str]]] = {}
    for nome, corpo in re.findall(r"enum (\w+) \{\n(.*?)\n\s*\}", texto, re.DOTALL):
        membros = []
        for linha in corpo.splitlines():
            achado = re.match(r"\s*(\w+)\s*=\s*(.+?)\s*$", linha)
            if achado:
                membros.append((achado.group(1), achado.group(2)))
        if membros:
            saida[nome] = membros
    return saida


def transicoes_do_puml(caminho: Path) -> list[str]:
    """Transições de uma `003-Maquina-de-Estados.puml`."""
    if not caminho.exists():
        return []
    texto = caminho.read_text(encoding="utf-8")
    linhas = [
        linha.strip()
        for linha in texto.splitlines()
        if re.match(r"^\[*\]\s*-->|^\w+\s*-->", linha.strip())
    ]
    declarados = re.findall(r"^state (\w+)", texto, re.M)
    return linhas + [f"state {estado}" for estado in declarados]


def modelo_proposto(cfg: dict) -> dict:
    """Constrói o contexto a partir dos diagramas propostos do próprio domínio."""
    cfg["pre"] = cfg["prefixo_regra"]
    base = RAIZ / "SIGMUN-Docs" / cfg["codigo"] / "puml"
    cfg["tabelas"] = tabelas_do_puml(base / "005-Persistencia.puml")
    cfg["enums"] = enums_do_puml(base / "001-Modelo-de-Dominio.puml")
    cfg["estados_puml"] = transicoes_do_puml(base / "003-Maquina-de-Estados.puml")
    cfg["operacoes"] = [
        {
            "metodo": "PLANEJADO",
            "caminho": f"{cfg['prefixo']}",
            "recurso": "proposto",
            "resumo": "API proposta; sem implementação registrada",
        }
    ]
    cfg["casos"] = [
        {"nome": item[1].replace(" ", ""), "resumo": item[1]} for item in cfg["capacidades"]
    ]
    cfg["regras_codigo"] = {
        f"RN-{cfg['prefixo_regra']}-{indice:03d}": texto
        for indice, texto in enumerate(cfg.get("regras", []), start=1)
    }
    cfg["testes"] = []
    cfg["proposto"] = True
    return cfg


FICHAS["DOM-OUV"] = {
    "codigo": "DOM-OUV",
    "dominio": "Ouvidoria",
    "slug": "Ouvidoria",
    "modulo": "sigmun_ouvidoria",
    "prefixo": "/api/v1/ou",
    "prefixo_regra": "OU",
    "schema": "ouv",
    "atores": [
        (
            "AT-OU-001",
            "Cidadão",
            "Externo",
            "Cidadão",
            "Registra manifestação, denúncia ou pedido de informação.",
        ),
        (
            "AT-OU-002",
            "Ouvidor",
            "Interno",
            "Servidor público",
            "Triagem, encaminhamento e resposta.",
        ),
        (
            "AT-OU-003",
            "Órgão competente",
            "Externo",
            "Unidade municipal",
            "Recebe o encaminhamento e presta a informação.",
        ),
        (
            "AT-OU-004",
            "Controle interno",
            "Externo",
            "Controle",
            "Acompanha prazo, conclusão e satisfação do cidadão.",
        ),
    ],
    "capacidades": [
        (
            "CAP-OU-001",
            "Recepção de manifestação",
            "Registra a manifestação e gera protocolo.",
            "PRO-OU-001",
        ),
        (
            "CAP-OU-002",
            "Triagem e classificação",
            "Classifica a matéria e define o fluxo.",
            "PRO-OU-002",
        ),
        ("CAP-OU-003", "Encaminhamento", "Encaminha a órgão responsável com prazo.", "PRO-OU-003"),
        (
            "CAP-OU-004",
            "Resposta e LAI",
            "Produz resposta e trata pedido de informação.",
            "PRO-OU-004",
        ),
        (
            "CAP-OU-005",
            "Prazos e avaliação",
            "Controla prazo e mede satisfação do cidadão.",
            "PRO-OU-005",
        ),
    ],
    "processos": [
        (
            "PRO-OU-001",
            "Receber manifestação",
            "Registra a manifestação e abre protocolo.",
            "RN-OU-001",
        ),
        ("PRO-OU-002", "Triar e classificar", "Define tipo, prioridade e sigilo.", "RN-OU-002"),
        (
            "PRO-OU-003",
            "Encaminhar e tratar",
            "Encaminha ao órgão e registra o tratamento.",
            "RN-OU-003",
        ),
        (
            "PRO-OU-004",
            "Responder e avaliar",
            "Responde e registra a satisfação do cidadão.",
            "RN-OU-004",
        ),
    ],
    "historias": [
        (
            "HU-OU-001",
            "Como cidadão, quero registrar uma manifestação e receber protocolo.",
            "CAP-OU-001",
            "Alta",
        ),
        (
            "HU-OU-002",
            "Como ouvidor, quero classificar a manifestação para definir o fluxo.",
            "CAP-OU-002",
            "Alta",
        ),
        (
            "HU-OU-003",
            "Como ouvidor, quero encaminhar ao órgão com prazo definido.",
            "CAP-OU-003",
            "Alta",
        ),
        (
            "HU-OU-004",
            "Como cidadão, quero pedir informação pública e receber resposta.",
            "CAP-OU-004",
            "Alta",
        ),
    ],
    "rnf": [
        ("RNF-OU-001", "Sigilo", "Denúncia pode proteger a identidade do manifestante."),
        ("RNF-OU-002", "Prazo", "Todo encaminhamento tem prazo de resposta."),
        (
            "RNF-OU-003",
            "Rastreabilidade",
            "Manifestação, encaminhamento e resposta registram autor e data.",
        ),
        ("RNF-OU-004", "Transparência", "Resposta segue a classificação da informação."),
    ],
    "regras": [
        "toda manifestação recebe protocolo e prazo.",
        "a denúncia admite proteção de identidade.",
        "o pedido de informação segue prazo próprio e admite recurso.",
        "o encerramento não apaga o histórico da manifestação.",
    ],
    "integracoes": [
        ("DOM-IDN", "Identidade e Acesso", "Consome", "Autenticação do manifestante."),
        ("DOM-GDO", "Gestão Documental", "Consome", "Anexos e peças da manifestação."),
        ("DOM-INT", "Interoperabilidade", "Fornece", "FalaBR / e-OUV e sistemas externos."),
    ],
    "lacunas": [
        "Definir o prazo legal por tipo de manifestação e por LAI.",
        "Definir a integração com o FalaBR / e-OUV.",
    ],
}


# ==============================================================================
# CONTEXTO: código + ficha de negócio
# ==============================================================================


def contexto(codigo: str) -> dict:
    """Reúne a ficha de negócio com os fatos extraídos do código.

    Domínios sem implementação (sem modelos, rotas e casos de uso) usam o
    **modo proposto**, em que os fatos vêm dos diagramas propostos do próprio
    domínio e os artefatos declaram essa condição.
    """
    cfg = dict(FICHAS[codigo])
    cfg["proposto"] = False

    # Sem correspondência técnica declarada, o gerador não pode
    # inventar um caminho em src/modules. O domínio permanece no
    # modo proposto, alimentado pelos artefatos PUML.
    if not cfg.get("modulo"):
        return modelo_proposto(cfg)

    if not tabelas_do_modulo(cfg["modulo"]) and not operacoes(
        cfg["prefixo"], cfg["modulo"]
    ):
        return modelo_proposto(cfg)
    cfg["pre"] = cfg["prefixo_regra"]
    cfg["tabelas"] = tabelas_do_modulo(cfg["modulo"])
    cfg["operacoes"] = operacoes(cfg["prefixo"], cfg["modulo"])
    cfg["casos"] = casos_de_uso(cfg["modulo"])
    cfg["enums"] = enums_do_modulo(cfg["modulo"])
    informadas = {
        f"RN-{cfg['pre']}-{indice:03d}": texto
        for indice, texto in enumerate(cfg.get("regras", []), start=1)
    }
    cfg["regras_codigo"] = {**informadas, **regras_do_modulo(cfg["modulo"], cfg["pre"])}
    cfg["testes"] = testes_do_dominio(cfg["modulo"])
    return cfg


def linha_coluna(coluna: dict) -> str:
    """`nome : TIPO <<flags>>` como nos diagramas de persistência."""
    marca = ""
    if "PK" in coluna["flags"]:
        marca = " <<PK>>"
    elif coluna["flags"]:
        marca = " <<" + ", ".join(f for f in ("UQ", "NN") if f in coluna["flags"]) + ">>"
    return f"{coluna['nome']} : {coluna['tipo']}{marca}"


# ==============================================================================
# ARTEFATOS 001 a 026
# ==============================================================================


def artefatos(ctx: dict) -> dict[int, tuple[str, str]]:
    cfg = ctx
    pre = cfg["pre"]
    d = cfg["dominio"]
    saida: dict[int, tuple[str, str]] = {}

    def fin(que: str) -> str:
        if cfg.get("proposto"):
            return (
                f"Este artefato descreve **{que}** do domínio {d} "
                f"(`{cfg['codigo']}`) em caráter **proposto**. "
                "O conteúdo técnico e de negócio deverá ser validado "
                "antes da implementação."
            )

        modulo = cfg.get("modulo")
        return (
            f"Este artefato detalha **{que}** do domínio {d} "
            f"(`{cfg['codigo']}`), com base na implementação material "
            f"identificada em `src/modules/{modulo}` e no conteúdo de "
            "negócio declarado no gerador."
        )

    # 001 — Atores
    corpo = secao(1, "Finalidade", fin("o mapa de atores")) + secao(
        2,
        "Atores do domínio",
        tabela(
            ["Identificador", "Ator", "Classificação", "Papel", "Responsabilidade"],
            [list(a) for a in cfg["atores"]],
        ),
    )
    corpo += secao(
        3,
        "Matriz ator × capacidade",
        tabela(
            ["Ator", "Capacidades"],
            [
                [a[0], ", ".join(c[0] for c in cfg["capacidades"] if a[0] == "AT-CUM-001")]
                for a in cfg["atores"]
            ],
        ),
    )
    corpo += secao(4, "Lacunas a validar", lista(cfg["lacunas"]))
    saida[1] = ("Mapa-de-Atores", corpo)

    # 002 — Capacidades
    saida[2] = (
        "Mapa-de-Capacidades",
        secao(1, "Finalidade", fin("o mapa de capacidades"))
        + secao(
            2,
            "Capacidades",
            tabela(
                ["Identificador", "Capacidade", "Descrição", "Processo"],
                [list(c) for c in cfg["capacidades"]],
            ),
        )
        + secao(
            3,
            "Processos por capacidade",
            tabela(
                ["Processo", "Descrição", "Regras"],
                [list(p) for p in cfg["processos"]],
            ),
        ),
    )

    # 003 — Processos
    saida[3] = (
        "Mapa-de-Processos",
        secao(1, "Finalidade", fin("o mapa de processos"))
        + secao(
            2,
            "Processos do domínio",
            tabela(
                ["Identificador", "Processo", "Descrição", "Regras"],
                [list(p) for p in cfg["processos"]],
            ),
        )
        + secao(
            3,
            "Fluxo de trabalho",
            "Captura → validação → classificação → gravação → consulta → "
            "atualização → exclusão lógica, conforme as regras do domínio.",
        ),
    )

    # 004 — Serviços
    saida[4] = (
        "Mapa-de-Servicos",
        secao(1, "Finalidade", fin("o mapa de serviços"))
        + secao(
            2,
            (
                f"Operações previstas em `{cfg['prefixo']}`"
                if cfg.get("proposto")
                else f"Operações publicadas em `{cfg['prefixo']}`"
            ),
            tabela(
                ["Método", "Caminho", "Recurso", "Resumo"],
                [
                    [o["metodo"], f"`{o['caminho']}`", o["recurso"], o["resumo"] or "—"]
                    for o in cfg["operacoes"]
                ],
            ),
        )
        + secao(
            3,
            (
                "Recursos previstos"
                if cfg.get("proposto")
                else "Recursos publicados"
            ),
            tabela(
                ["Recurso", "Operações"],
                [
                    [
                        recurso,
                        str(sum(1 for o in cfg["operacoes"] if o["recurso"] == recurso)),
                    ]
                    for recurso in dict.fromkeys(o["recurso"] for o in cfg["operacoes"])
                ],
            ),
        )
        + secao(4, "Lacunas a validar", lista(cfg["lacunas"])),
    )

    # 005 — Casos de uso
    saida[5] = (
        "Casos-de-Uso",
        secao(1, "Finalidade", fin("os casos de uso"))
        + secao(
            2,
            "Casos de uso propostos" if cfg.get("proposto") else "Casos de uso implementados",
            tabela(
                ["Identificador", "Caso de uso", "Classe", "Resumo"],
                [
                    [
                        f"CU-{pre}-{indice:03d}",
                        item["nome"].removesuffix("UseCase"),
                        f"`{item['nome']}`",
                        item["resumo"] or "—",
                    ]
                    for indice, item in enumerate(cfg["casos"], start=1)
                ],
            ),
        )
        + secao(
            3,
            "Cobertura",
            (
                (
                    f"Casos de uso previstos: **{len(cfg['casos'])}**. "
                    f"Operações previstas: **{len(cfg['operacoes'])}**."
                )
                if cfg.get("proposto")
                else (
                    f"Casos de uso no código: **{len(cfg['casos'])}**. "
                    f"Operações publicadas: **{len(cfg['operacoes'])}**."
                )
            ),
        ),
    )

    # 006 — Histórias de usuário
    saida[6] = (
        "Historias-de-Usuario",
        secao(1, "Finalidade", fin("as histórias de usuário"))
        + secao(
            2,
            "Histórias",
            tabela(
                ["Identificador", "História", "Capacidade", "Prioridade"],
                [list(h) for h in cfg["historias"]],
            ),
        ),
    )

    # 007 — Regras de negócio
    regras = sorted(cfg["regras_codigo"])
    saida[7] = (
        "Regras-de-Negocio",
        secao(1, "Finalidade", fin("as regras de negócio"))
        + secao(
            2,
            "Regras propostas" if cfg.get("proposto") else "Regras implementadas",
            tabela(
                ["Identificador", "Descrição", "Fonte"],
                [
                    [
                        identificador,
                        descricao,
                        (
                            "modelo proposto"
                            if cfg.get("proposto")
                            else f"`src/modules/{cfg['modulo']}`"
                        ),
                    ]
                    for identificador, descricao in cfg["regras_codigo"].items()
                ],
            ),
        )
        + secao(
            3,
            "Cobertura",
            f"Regras referenciadas no código: **{len(regras)}**.",
        ),
    )
    # 008 — Requisitos funcionais
    requisitos = [
        [
            f"RF-{pre}-{indice:03d}",
            f"{o['metodo']} {o['caminho']}",
            "Alta" if o["metodo"] in {"POST", "DELETE"} else "Média",
            o["recurso"],
            "CAP-" + pre + "-001",
        ]
        for indice, o in enumerate(cfg["operacoes"], start=1)
    ]
    saida[8] = (
        "Requisitos-Funcionais",
        secao(1, "Finalidade", fin("os requisitos funcionais"))
        + secao(
            2,
            "Requisitos",
            tabela(["ID", "Requisito", "Prioridade", "Recurso", "Capacidade"], requisitos),
        )
        + secao(
            3,
            "Cobertura",
            (
                f"Operações previstas: **{len(cfg['operacoes'])}**."
                if cfg.get("proposto")
                else f"Operações publicadas: **{len(cfg['operacoes'])}**."
            ),
        ),
    )

    # 009 — Requisitos não funcionais
    saida[9] = (
        "Requisitos-Nao-Funcionais",
        secao(1, "Finalidade", fin("os requisitos não funcionais"))
        + secao(
            2, "Requisitos", tabela(["ID", "Categoria", "Requisito"], [list(r) for r in cfg["rnf"]])
        ),
    )

    # 010 — Especificações
    saida[10] = (
        "Especificacoes",
        secao(1, "Finalidade", fin("as especificações"))
        + secao(
            2,
            (
                "Contratos previstos"
                if cfg.get("proposto")
                else "Contratos publicados"
            ),
            tabela(
                ["Método", "Caminho", "Recurso", "Corpo"],
                [
                    [o["metodo"], f"`{o['caminho']}`", o["recurso"], "JSON (payload do domínio)"]
                    for o in cfg["operacoes"]
                ],
            ),
        )
        + secao(
            3,
            "Validações aplicadas",
            tabela(
                ["Regra", "Validação"],
                [[r, d] for r, d in cfg["regras_codigo"].items()],
            ),
        ),
    )

    # 011 — Critérios de aceitação
    criterios = [
        [f"CA-{pre}-{i:03d}", r[1], r[2], "Teste automatizado"]
        for i, r in enumerate(cfg["rnf"], start=1)
    ]
    saida[11] = (
        "Criterios-de-Aceitacao",
        secao(1, "Finalidade", fin("os critérios de aceitação"))
        + secao(2, "Critérios", tabela(["ID", "Categoria", "Critério", "Verificação"], criterios)),
    )

    # 012 — Matriz de rastreabilidade
    matriz = []
    for indice, caso in enumerate(cfg["casos"], start=1):
        matriz.append(
            [
                f"CU-{pre}-{indice:03d}",
                caso["nome"].removesuffix("UseCase"),
                cfg["historias"][(indice - 1) % len(cfg["historias"])][0],
                f"RF-{pre}-{min(indice, len(cfg['operacoes'])):03d}",
                "RF-CUM-001",
            ]
        )
    saida[12] = (
        "Matriz-de-Rastreabilidade",
        secao(1, "Finalidade", fin("a matriz de rastreabilidade"))
        + secao(
            2,
            "Caso de uso × história × requisito",
            tabela(["Caso de uso", "Classe", "História", "Requisito", "Regra"], matriz),
        ),
    )

    # 013 — Modelo de dados
    blocos = []
    for nome_tabela, info in sorted(cfg["tabelas"].items()):
        linhas = [
            [linha_coluna(c), "NOT NULL" if "NN" in c["flags"] else "opcional"]
            for c in info["colunas"]
        ]
        blocos.append(
            f"### {nome_tabela} (`{info['classe']}`)\n\n"
            + tabela(["Coluna", "Obrigatoriedade"], linhas)
        )
    saida[13] = (
        "Modelo-de-Dados",
        secao(1, "Finalidade", fin("o modelo de dados"))
        + secao(2, f"Tabelas no schema `{cfg['schema']}`", "\n\n".join(blocos)),
    )

    # 014 — Modelo de integração
    saida[14] = (
        "Modelo-de-Integracao",
        secao(1, "Finalidade", fin("o modelo de integração"))
        + secao(
            2,
            "Princípios",
            lista(
                [
                    "Sem chave estrangeira entre schemas de domínios.",
                    "Comunicação por contrato (API ou evento).",
                    (
                        f"Contrato previsto em `{cfg['prefixo']}`."
                        if cfg.get("proposto")
                        else f"Contrato publicado em `{cfg['prefixo']}`."
                    ),
                ]
            ),
        )
        + secao(
            3,
            "Integrações",
            tabela(
                ["Domínio", "Nome", "Sentido", "Finalidade"], [list(i) for i in cfg["integracoes"]]
            ),
        ),
    )

    # 015 — Arquitetura de serviços
    saida[15] = (
        "Arquitetura-de-Servicos",
        secao(1, "Finalidade", fin("a arquitetura de serviços"))
        + secao(
            2,
            "Camadas",
            tabela(
                ["Camada", "Conteúdo"],
                [
                    ["presentation", "Routers FastAPI e schemas Pydantic"],
                    ["application", "Casos de uso, comandos e queries"],
                    ["domain", "Entidades, objetos de valor e regras"],
                    ["infrastructure", "Repositórios SQLAlchemy e modelos ORM"],
                ],
            ),
        )
        + secao(
            3,
            "Serviços previstos" if cfg.get("proposto") else "Serviços publicados",
            tabela(["Prefixo", "Operações"], [[cfg["prefixo"], len(cfg["operacoes"])]]),
        ),
    )

    # 016 — Modelo de segurança
    seguranca = [
        r for r in cfg["rnf"] if r[1] in {"Autenticação", "Privacidade", "Exclusão lógica"}
    ]
    saida[16] = (
        "Modelo-de-Seguranca",
        secao(1, "Finalidade", fin("o modelo de segurança"))
        + secao(
            2,
            "Controles aplicáveis",
            tabela(["ID", "Categoria", "Controle"], [list(r) for r in seguranca]),
        )
        + secao(3, "Papéis", tabela(["Ator", "Acesso"], [[a[0], a[1]] for a in cfg["atores"]])),
    )

    # 017 — Modelo de auditoria
    auditoria = sorted(
        {
            c["nome"]
            for i in cfg["tabelas"].values()
            for c in i["colunas"]
            if c["nome"]
            in {"created_at", "created_by", "updated_at", "updated_by", "deleted_at", "deleted_by"}
        }
    )
    saida[17] = (
        "Modelo-de-Auditoria",
        secao(1, "Finalidade", fin("o modelo de auditoria"))
        + secao(
            2,
            "Colunas de auditoria",
            tabela(
                ["Coluna", "Presente em"],
                [[c, f"{len(cfg['tabelas'])} tabelas"] for c in auditoria],
            ),
        )
        + secao(
            3, "Princípio", "Toda alteração registra autor e data; a exclusão é lógica e auditável."
        ),
    )

    # 018 — Plano de testes
    saida[18] = (
        "Plano-de-Testes",
        secao(1, "Finalidade", fin("o plano de testes"))
        + secao(
            2,
            "Suítes por classe",
            tabela(
                ["Arquivo", "Classe", "Testes"],
                [[f"`{t['arquivo']}`", t["classe"], t["quantidade"]] for t in cfg["testes"]],
            ),
        ),
    )

    # 019 — Casos de teste
    metodos = [
        [f"CT-{pre}-{i:03d}", f"`{t['classe']}.{m}`"]
        for i, (t, m) in enumerate(((t, m) for t in cfg["testes"] for m in t["metodos"]), start=1)
    ]
    saida[19] = (
        "Casos-de-Teste",
        secao(1, "Finalidade", fin("os casos de teste"))
        + secao(2, "Testes", tabela(["ID", "Teste"], metodos)),
    )

    # 020 — Plano de implantação
    saida[20] = (
        "Plano-de-Implantacao",
        secao(1, "Finalidade", fin("o plano de implantação"))
        + secao(
            2,
            "Fases",
            tabela(
                ["Fase", "Conteúdo"],
                [
                    ["1. Schema", f"Migrações que criam as {len(cfg['tabelas'])} tabelas"],
                    ["2. API", f"Registro do router em `{cfg['prefixo']}`"],
                    ["3. Segurança", "Autenticação e autorização"],
                    ["4. Integração", "Consumidores e metadados"],
                ],
            ),
        ),
    )

    # 021 — Checklist de prontidão
    itens = [
        [
            "Esquema de persistência",
            "PROPOSTO" if cfg.get("proposto") else "OK",
            (
                f"{len(cfg['tabelas'])} tabelas previstas"
                if cfg.get("proposto")
                else f"{len(cfg['tabelas'])} tabelas mapeadas"
            ),
        ],
        [
            "API publicada",
            "PROPOSTA" if cfg.get("proposto") else "OK",
            (
                f"Contrato previsto em `{cfg['prefixo']}`"
                if cfg.get("proposto")
                else f"{len(cfg['operacoes'])} operações em `{cfg['prefixo']}`"
            ),
        ],
        [
            "Regras propostas" if cfg.get("proposto") else "Regras implementadas",
            "NÃO APLICÁVEL" if cfg.get("proposto") else "OK",
            (
                f"{len(cfg['regras_codigo'])} regras propostas"
                if cfg.get("proposto")
                else f"{len(cfg['regras_codigo'])} regras"
            ),
        ],
        [
            "Suíte de testes",
            "NÃO APLICÁVEL" if cfg.get("proposto") else "OK",
            (
                "Testes serão definidos na implementação"
                if cfg.get("proposto")
                else f"{sum(t['quantidade'] for t in cfg['testes'])} testes"
            ),
        ],
        ["Autenticação das escritas", "OK", "JWT do DOM-IDN obrigatório (ADR-0007)"],
        ["Compatibilidade legada", "EM TRANSIÇÃO", "Header X-Usuario-Id aceito e depreciado"],
        ["Revisão periódica", "OK", "Política de 12 meses definida no ADR-0007"],
        ["Compartilhamento de pessoa", "OK", "Contrato formal no ADR-0007"],
    ]
    saida[21] = (
        "Checklist-de-Prontidao-para-Producao",
        secao(1, "Finalidade", fin("o checklist de prontidão"))
        + secao(2, "Itens", tabela(["Item", "Situação", "Evidência"], itens)),
    )

    # 022 — Plano de migração de dados
    saida[22] = (
        "Plano-de-Migracao-de-Dados",
        secao(1, "Finalidade", fin("o plano de migração de dados"))
        + secao(
            2,
            "Tabelas",
            tabela(
                ["Tabela", "Colunas", "Classe ORM"],
                [
                    [n, len(i["colunas"]), f"`{i['classe']}`"]
                    for n, i in sorted(cfg["tabelas"].items())
                ],
            ),
        )
        + secao(3, "Estratégia", "Carga inicial por migração Alembic; sem conversão de legado."),
    )

    # 023 — Plano de treinamento
    saida[23] = (
        "Plano-de-Treinamento",
        secao(1, "Finalidade", fin("o plano de treinamento"))
        + secao(
            2,
            "Públicos",
            tabela(
                ["Público", "Conteúdo"],
                [
                    [a[1], "Regras de negócio e operação do serviço"]
                    for a in cfg["atores"]
                    if a[2] == "Interno"
                ],
            ),
        )
        + secao(
            3, "Carga horária sugerida", "4 horas por papel, com foco nas regras de validação."
        ),
    )

    # 024 — Plano de suporte e operação
    saida[24] = (
        "Plano-de-Suporte-e-Operacao",
        secao(1, "Finalidade", fin("o plano de suporte e operação"))
        + secao(
            2,
            "Operação",
            tabela(
                ["Item", "Definição"],
                [
                    ["Monitoramento", "Métricas de disponibilidade e erro por operação"],
                    ["Incidentes", "Registro com severidade, responsável e encerramento"],
                    ["Ciclo de vida", "Exclusão lógica preserva histórico para auditoria"],
                ],
            ),
        ),
    )

    # 025 — Estrutura técnica
    modulo = cfg.get("modulo")
    arquivos = []
    if modulo:
        arquivos = sorted(
            str(p.relative_to(RAIZ))
            for p in (RAIZ / "src/modules" / modulo).rglob("*.py")
            if "__pycache__" not in str(p)
        )

    estrutura_titulo = (
        f"Módulo `{modulo}`"
        if modulo
        else "Estrutura técnica prevista"
    )
    estrutura_conteudo = (
        tabela(
            ["Arquivo", "Linhas"],
            [
                [
                    f"`{a}`",
                    len(
                        (RAIZ / a)
                        .read_text(encoding="utf-8", errors="replace")
                        .splitlines()
                    ),
                ]
                for a in arquivos
            ],
        )
        if arquivos
        else "Nenhuma estrutura técnica implementada foi identificada."
    )

    saida[25] = (
        "Estrutura-Tecnica",
        secao(1, "Finalidade", fin("a estrutura técnica"))
        + secao(2, estrutura_titulo, estrutura_conteudo),
    )

    # 026 — Modelo de domínio
    entidades = [
        [n, f"`{i['classe']}`", len(i["colunas"])] for n, i in sorted(cfg["tabelas"].items())
    ]
    dominio_enum = "\n".join(
        f"### {nome}\n\n" + tabela(["Membro", "Valor"], [[m, v] for m, v in membros])
        for nome, membros in cfg["enums"].items()
    )
    saida[26] = (
        "Modelo-de-Dominio",
        secao(1, "Finalidade", fin("o modelo de domínio"))
        + secao(2, "Entidades", tabela(["Tabela", "Classe", "Atributos"], entidades))
        + secao(3, "Domínios de valor", dominio_enum)
        + secao(
            4,
            "Regras",
            tabela(["ID", "Descrição"], [[r, d] for r, d in cfg["regras_codigo"].items()]),
        ),
    )

    return saida


# ==============================================================================
# ESCRITA DOS ARTEFATOS
# ==============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apenas", action="append", help="Domínios a gerar.")
    parser.add_argument("--verificar", action="store_true", help="Falha se defasado.")
    args = parser.parse_args()
    registrar_fichas_documentais()

    alterados = 0
    for codigo in sorted(FICHAS):
        if args.apenas and codigo not in args.apenas:
            continue
        ctx = contexto(codigo)
        pasta = RAIZ / "SIGMUN-Docs" / codigo
        for numero, (titulo, corpo) in sorted(artefatos(ctx).items()):
            destino = pasta / f"{numero:03d}-{titulo}-{ctx['slug']}.md"
            conteudo = documento(ctx, numero, titulo, corpo)
            if destino.exists() and destino.read_text(encoding="utf-8") == conteudo:
                continue
            alterados += 1
            if args.verificar:
                print(f"DEFASADO: {destino.relative_to(RAIZ)}")
                continue
            destino.write_text(conteudo, encoding="utf-8")
            print(f"gerado: {destino.relative_to(RAIZ)} ({len(conteudo)} bytes)")
    print(f"artefatos escritos: {alterados}")
    return 1 if args.verificar and alterados else 0


if __name__ == "__main__":
    raise SystemExit(main())
