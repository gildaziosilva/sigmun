# -*- coding: utf-8 -*-
"""Gera os artefatos 000-Dominio-<nome>.md para os domínios do SIGMUN (pt-BR).

Base: Mapa-de-Dominios.md §50 (Mapa Consolidado de Domínios) e template do
domínio-piloto DOM-COMPRAS-001.
"""
from __future__ import annotations

from pathlib import Path

BASE = Path(r"C:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs")

# (código, nome do domínio, slug do arquivo)
DOMAINS = [
    ("DOM-GOV", "Governança Municipal", "Governanca-Municipal"),
    ("DOM-PLA", "Planejamento Governamental", "Planejamento-Governamental"),
    ("DOM-GDO", "Gestão Documental", "Gestao-Documental"),
    ("DOM-TRI", "Administração Tributária", "Administracao-Tributaria"),
    ("DOM-ORC", "Orçamento Público", "Orcamento-Publico"),
    ("DOM-CON", "Contabilidade Pública", "Contabilidade-Publica"),
    ("DOM-PES", "Gestão de Pessoas", "Gestao-de-Pessoas"),
    ("DOM-CPT", "Gestão de Competências", "Gestao-de-Competencias"),
    ("DOM-PAT", "Gestão Patrimonial", "Gestao-Patrimonial"),
    ("DOM-FRO", "Gestão de Frota", "Gestao-de-Frota"),
    ("DOM-TEL", "Gestão Territorial", "Gestao-Territorial"),
    ("DOM-IMO", "Cadastro Imobiliário", "Cadastro-Imobiliario"),
    ("DOM-GEO", "Geoinformação Municipal", "Geoinformacao-Municipal"),
    ("DOM-OBR", "Obras e Infraestrutura", "Obras-e-Infraestrutura"),
    ("DOM-SAU", "Saúde Pública", "Saude-Publica"),
    ("DOM-EDU", "Educação Pública", "Educacao-Publica"),
    ("DOM-ASS", "Assistência Social", "Assistencia-Social"),
    ("DOM-MAM", "Meio Ambiente", "Meio-Ambiente"),
    ("DOM-DEC", "Desenvolvimento Econômico", "Desenvolvimento-Economico"),
    ("DOM-CUM", "Cadastro Único Municipal", "Cadastro-Unico-Municipal"),
    ("DOM-ATE", "Atendimento ao Cidadão", "Atendimento-ao-Cidadao"),
    ("DOM-OUV", "Ouvidoria", "Ouvidoria"),
    ("DOM-DAD", "Dados Corporativos", "Dados-Corporativos"),
    ("DOM-MET", "Metadados Corporativos", "Metadados-Corporativos"),
    ("DOM-IND", "Indicadores e Desempenho", "Indicadores-e-Desempenho"),
    ("DOM-ANA", "Analytics e Inteligência", "Analytics-e-Inteligencia"),
    ("DOM-IDN", "Identidade e Acesso", "Identidade-e-Acesso"),
    ("DOM-SEG", "Segurança da Informação", "Seguranca-da-Informacao"),
    ("DOM-INT", "Integração e Interoperabilidade", "Integracao-e-Interoperabilidade"),
    ("DOM-MOB", "Mobilidade e Serviços de Campo", "Mobilidade-e-Servicos-de-Campo"),
    ("DOM-INF", "Infraestrutura Tecnológica", "Infraestrutura-Tecnologica"),
    ("DOM-DIA", "Gestão de Diárias, Viagens e Deslocamentos", "Gestao-de-Diarias-Viagens-e-Deslocamentos"),
]

CHECK_LIST = [
    "000-Dominio-{slug}.md",
    "001-Mapa-de-Atores-{slug}.md",
    "002-Mapa-de-Capacidades-{slug}.md",
    "003-Mapa-de-Processos-{slug}.md",
    "004-Mapa-de-Servicos-{slug}.md",
    "005-Casos-de-Uso-{slug}.md",
    "006-Historias-de-Usuario-{slug}.md",
    "007-Regras-de-Negocio-{slug}.md",
    "008-Requisitos-Funcionais-{slug}.md",
    "009-Requisitos-Nao-Funcionais-{slug}.md",
    "010-Especificacoes-{slug}.md",
    "011-Criterios-de-Aceitacao-{slug}.md",
    "012-Matriz-de-Rastreabilidade-{slug}.md",
    "013-Modelo-de-Dados-{slug}.md",
    "014-Modelo-de-Integracao-{slug}.md",
    "015-Arquitetura-de-Servicos-{slug}.md",
    "016-Modelo-de-Seguranca-{slug}.md",
    "017-Modelo-de-Auditoria-{slug}.md",
    "018-Plano-de-Testes-{slug}.md",
    "019-Casos-de-Teste-{slug}.md",
    "020-Plano-de-Implantacao-{slug}.md",
    "021-Checklist-de-Prontidao-para-Producao-{slug}.md",
    "022-Plano-de-Migracao-de-Dados-{slug}.md",
    "023-Plano-de-Treinamento-{slug}.md",
    "024-Plano-de-Suporte-e-Operacao-{slug}.md",
    "025-Estrutura-Tecnica-{slug}.md",
    "026-Modelo-de-Dominio-{slug}.md",
]
def _descricao_artefato(nome_arquivo):
    """Retorna a descrição curta do artefato a partir do nome do arquivo."""
    mape = {
        "001-Mapa-de-Atores": "atores do domínio",
        "002-Mapa-de-Capacidades": "capacidades do domínio",
        "003-Mapa-de-Processos": "processos do domínio",
        "004-Mapa-de-Servicos": "serviços do domínio",
        "005-Casos-de-Uso": "casos de uso",
        "006-Historias-de-Usuario": "histórias de usuário",
        "007-Regras-de-Negocio": "regras de negócio",
        "008-Requisitos-Funcionais": "requisitos funcionais",
        "009-Requisitos-Nao-Funcionais": "requisitos não funcionais",
        "010-Especificacoes": "especificações",
        "011-Criterios-de-Aceitacao": "critérios de aceitação",
        "012-Matriz-de-Rastreabilidade": "matriz de rastreabilidade",
        "013-Modelo-de-Dados": "modelo de dados do domínio",
        "014-Modelo-de-Integracao": "modelo de integração",
        "015-Arquitetura-de-Servicos": "arquitetura de serviços",
        "016-Modelo-de-Seguranca": "modelo de segurança",
        "017-Modelo-de-Auditoria": "modelo de auditoria",
        "018-Plano-de-Testes": "plano de testes",
        "019-Casos-de-Teste": "casos de teste",
        "020-Plano-de-Implantacao": "plano de implantação",
        "021-Checklist-de-Prontidao-para-Producao": "checklist de prontidão para produção",
        "022-Plano-de-Migracao-de-Dados": "plano de migração de dados",
        "023-Plano-de-Treinamento": "plano de treinamento",
        "024-Plano-de-Suporte-e-Operacao": "plano de suporte e operação",
        "025-Estrutura-Tecnica": "estrutura técnica",
        "026-Modelo-de-Dominio": "modelo de domínio",
    }
    for chave, desc in mape.items():
        if nome_arquivo.startswith(chave):
            return desc
    return nome_arquivo
def generar_documento(codigo, nome, slug):
    """Gera o conteúdo do artefato 000-Dominio-<nome>.md em pt-BR."""
    header = (
        f"# 000 – Domínio de {nome}\n\n"
        f"#### Domínio de {nome}\n\n"
        "**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal\n\n"
        f"**Código:** {codigo}\n\n"
        f"**Domínio:** {nome}\n\n"
        "**Versão:** 1.0\n\n"
        "**Status:** Vigente\n\n"
        "**Classificação da Informação:** Pública\n\n"
        "**Documento(s) Relacionado(s):**\n\n"
        "* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md\n"
        "* 000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md\n"
        "* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md\n"
        "* 000C-HIERARQUIA-DOCUMENTAL.md\n"
        "* 000D-MODELO-DE-DOCUMENTO.md\n"
        "* 000F-Registro-de-Decisoes-Arquiteturais(ADR).md\n"
        "* 000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md\n"
        "* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md\n"
        "* 030-Roadmap-de-Implementacao-dos-Dominios.md\n"
        "* Mapa-de-Dominios.md\n"
        "* Modelo-Conceitual.md\n"
        "* Modelo-Logico.md\n"
        "* Modelo-Fisico.md\n"
        "* Dicionario-de-dados.md\n\n"
        "---\n\n"
    )
    finalidade = (
        f"# 1. Finalidade\n\n"
        f"O **Domínio de {nome}** (`{codigo}`) representa o conjunto de capacidades, processos, "
        f"serviços, informações, regras e interações relacionados à área de {nome.lower()} no "
        "âmbito da Administração Pública Municipal.\n\n"
        "Este documento define a razão de ser do domínio, seus objetivos, escopo, seus "
        "relacionamentos com outros domínios do SIGMUN e a estratégia de evolução, servindo de "
        "ponto de partida para os demais artefatos do domínio.\n\n"
        "---\n\n"
    )
    return header + finalidade + _corpo(nome, slug) + _artefatos(slug) + _versionamento(slug)


def _corpo(nome, slug):
    """Seções 2 a 5 do documento (objetivos, visão, escopo, relacionamentos)."""
    objetivos = (
        "# 2. Objetivos do Domínio\n\n"
        "São objetivos do domínio:\n\n"
        "* estruturar e organizar as informações relacionadas;\n"
        "* promover padronização dos procedimentos;\n"
        "* reduzir retrabalho;\n"
        "* reduzir duplicidade de informações;\n"
        "* aumentar a rastreabilidade dos processos;\n"
        "* centralizar informações relevantes;\n"
        "* apoiar a tomada de decisão;\n"
        "* disponibilizar informações para gestão;\n"
        "* permitir geração de indicadores;\n"
        "* preservar documentos e evidências;\n"
        "* integrar informações com outros domínios do SIGMUN.\n\n"
        "---\n\n"
    )
    visao = (
        "# 3. Visão do Domínio\n\n"
        f"O domínio **{nome}** deverá permitir que as informações e processos relacionados sejam "
        "tratados de forma integrada, confiável e rastreável, apoiando a gestão municipal.\n\n"
        "Visão conceitual:\n\n"
        "```text\n"
        "Necessidade\n    ↓\nCaptura e registro\n    ↓\nOrganização\n    ↓\nGestão e controle\n    ↓\n"
        "Transparência\n    ↓\nInformação gerencial\n```\n\n"
        "---\n\n"
    )
    escopo = (
        "# 4. Escopo\n\n"
        "O domínio compreende, em nível corporativo:\n\n"
        "* levantamento e organização de informações do domínio;\n"
        "* apoio aos processos municipais relacionados;\n"
        "* definição de entidades e dados relevantes;\n"
        "* articulação com serviços e requisitos;\n"
        "* geração de indicadores e relatórios;\n"
        "* integração com outros domínios do SIGMUN.\n\n"
        "O detalhamento de cada processo e requisito será realizado nos respectivos artefatos.\n\n"
        "---\n\n"
    )
    relacionamentos = (
        "# 5. Relacionamentos do Domínio\n\n"
        f"O domínio **{nome}** mantém relacionamentos com outros domínios do SIGMUN, os quais "
        "serão detalhados nos artefatos de modelo de dados e integração:\n\n"
        "* compartilhamento de informação mestra (pessoa, unidade administrativa, fornecedor);\n"
        "* consumo ou provisão de serviços;\n"
        "* integração com os domínios funcionais e tecnológicos;\n"
        "* uso de identidade e acesso (DOM-IDN);\n"
        "* registro de auditoria e indicadores.\n\n"
        "---\n\n"
    )
    return objetivos + visao + escopo + relacionamentos


def _artefatos(slug):
    """Seção 6 – lista dos 27 artefatos do domínio."""
    # exclui o próprio 000 para não repetir
    nomes = [c.format(slug=slug) for c in CHECK_LIST if not c.startswith("000-")]
    lista = "\n".join(
        f"{i+1}. `{nome}` – {_descricao_artefato(nome)}" for i, nome in enumerate(nomes)
    )
    return (
        "# 6. Artefatos Relacionados\n\n"
        "A partir deste documento serão produzidos progressivamente os artefatos do domínio:\n\n"
        f"{lista}\n\n"
        "---\n\n"
    )


def _versionamento(slug):
    return (
        "# 7. Versionamento\n\n"
        "| Versão | Data       | Descrição                                    |\n"
        "| ------ | ---------- | -------------------------------------------- |\n"
        "| 1.0    | 2026-08-20 | Criação do documento de definição do domínio |\n\n"
        "---\n\n"
        f"**Documento:** 000-Dominio-{slug}.md\n\n"
        "**Última atualização:** 2026-08-20\n\n"
        "**Responsável:** Equipe SIGMUN\n\n"
        "**Status da revisão:** Vigente\n"
    )


def main():
    """Cria o arquivo 000-Dominio-<nome>.md em cada diretório DOM-* (pt-BR)."""
    criados, erros = [], []
    for codigo, nome, slug in DOMAINS:
        pasta = BASE / codigo
        if not pasta.exists():
            erros.append(f"{codigo}: diretório não encontrado")
            continue
        destino = pasta / f"000-Dominio-{slug}.md"
        try:
            conteudo = generar_documento(codigo, nome, slug)
            destino.write_text(conteudo, encoding="utf-8")
            criados.append(f"{codigo}: {destino.name}")
        except OSError as exc:
            erros.append(f"{codigo}: {exc}")
    print("=== ARQUIVOS CRIADOS ===")
    for c in criados:
        print(" OK ", c)
    print("=== ERROS ===")
    for e in erros:
        print(" ERRO ", e)
    print(f"Total criados: {len(criados)} | Erros: {len(erros)}")


if __name__ == "__main__":
    main()