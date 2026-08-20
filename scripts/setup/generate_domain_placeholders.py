# -*- coding: utf-8 -*-
"""Gera os 26 placeholders padronizados (001-026) para cada domínio do SIGMUN.

Tudo em português do Brasil (pt-BR). Não altera o diretório DOM-COMPRAS-001.
"""
from __future__ import annotations

from pathlib import Path

BASE = Path(r"C:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs")
EXCLUIR = {"DOM-COMPRAS-001"}

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
]

# (prefixo do arquivo, título humano, descrição curta do artefato)
ARTEFATOS = [
    ("001-Mapa-de-Atores", "Mapa de Atores", "identificação dos atores"),
    ("002-Mapa-de-Capacidades", "Mapa de Capacidades", "mapa de capacidades"),
    ("003-Mapa-de-Processos", "Mapa de Processos", "mapa de processos"),
    ("004-Mapa-de-Servicos", "Mapa de Serviços", "mapa de serviços"),
    ("005-Casos-de-Uso", "Casos de Uso", "casos de uso"),
    ("006-Historias-de-Usuario", "Histórias de Usuário", "histórias de usuário"),
    ("007-Regras-de-Negocio", "Regras de Negócio", "regras de negócio"),
    ("008-Requisitos-Funcionais", "Requisitos Funcionais", "requisitos funcionais"),
    ("009-Requisitos-Nao-Funcionais", "Requisitos Não Funcionais", "requisitos não funcionais"),
    ("010-Especificacoes", "Especificações", "especificações"),
    ("011-Criterios-de-Aceitacao", "Critérios de Aceitação", "critérios de aceitação"),
    ("012-Matriz-de-Rastreabilidade", "Matriz de Rastreabilidade", "matriz de rastreabilidade"),
    ("013-Modelo-de-Dados", "Modelo de Dados", "modelo de dados do domínio"),
    ("014-Modelo-de-Integracao", "Modelo de Integração", "modelo de integração"),
    ("015-Arquitetura-de-Servicos", "Arquitetura de Serviços", "arquitetura de serviços"),
    ("016-Modelo-de-Seguranca", "Modelo de Segurança", "modelo de segurança"),
    ("017-Modelo-de-Auditoria", "Modelo de Auditoria", "modelo de auditoria"),
    ("018-Plano-de-Testes", "Plano de Testes", "plano de testes"),
    ("019-Casos-de-Teste", "Casos de Teste", "casos de teste"),
    ("020-Plano-de-Implantacao", "Plano de Implantação", "plano de implantação"),
    ("021-Checklist-de-Prontidao-para-Producao", "Checklist de Prontidão para Produção", "checklist de prontidão para produção"),
    ("022-Plano-de-Migracao-de-Dados", "Plano de Migração de Dados", "plano de migração de dados"),
    ("023-Plano-de-Treinamento", "Plano de Treinamento", "plano de treinamento"),
    ("024-Plano-de-Suporte-e-Operacao", "Plano de Suporte e Operação", "plano de suporte e operação"),
    ("025-Estrutura-Tecnica", "Estrutura Técnica", "estrutura técnica"),
    ("026-Modelo-de-Dominio", "Modelo de Domínio", "modelo de domínio"),
]


def gerar_placeholder(codigo: str, nome: str, slug: str,
                       prefixo: str, titulo: str, descricao: str) -> str:
    """Gera o conteúdo padronizado de esboço para um artefato do domínio (pt-BR).

    O esboço segue o padrão corporativo do SIGMUN, sinalizando claramente
    que o conteúdo está **em elaboração** e será preenchido progressivamente.
    """
    numero = prefixo.split("-")[0]  # e.g. "001" do "001-Mapa-de-Atores"
    documento = f"{prefixo}-{slug}.md"
    codigo_artefato = f"{codigo}-{numero}"

    return (
        f"# {numero} – {titulo} – {nome}\n"
        f"\n"
        f"#### {titulo} – {nome}\n"
        f"\n"
        f"**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal\n"
        f"\n"
        f"**Código:** {codigo_artefato}\n"
        f"\n"
        f"**Domínio:** {nome}\n"
        f"\n"
        f"**Versão:** 1.0\n"
        f"\n"
        f"**Status:** Em elaboração\n"
        f"\n"
        f"**Classificação da Informação:** Pública\n"
        f"\n"
        f"**Documento(s) Relacionado(s):**\n"
        f"\n"
        f"* `000-Dominio-{slug}.md`\n"
        f"* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`\n"
        f"* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`\n"
        f"* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`\n"
        f"* `000D-MODELO-DE-DOCUMENTO.md`\n"
        f"* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`\n"
        f"* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`\n"
        f"\n"
        f"---\n"
        f"\n"
        f"# 1. Finalidade\n"
        f"\n"
        f"O **{titulo} – {nome}** (`{codigo}`) tem como finalidade mapear e definir "
        f"{descricao} do domínio.\n"
        f"\n"
        f"Este artefato é um **esboço inicial padronizado** da arquitetura corporativa "
        f"do SIGMUN. O conteúdo será preenchido progressivamente conforme a modelagem "
        f"detalhada do domínio **{nome}** (`{codigo}`) avance.\n"
        f"\n"
        f"---\n"
        f"\n"
        f"# 2. Escopo e Diretrizes\n"
        f"\n"
        f"As informações deste documento estão em elaboração e serão atualizadas "
        f"periodicamente pela Equipe SIGMUN de acordo com o andamento da modelagem "
        f"do domínio **{nome}**.\n"
        f"\n"
        f"Até que o esboço seja substituído por conteúdo específico, considere que:\n"
        f"\n"
        f"* a estrutura deste artefato segue o padrão corporativo adotado pelo SIGMUN;\n"
        f"* as seções aqui apresentadas servirão de guia para a elaboração detalhada;\n"
        f"* o preenchimento deve observar as convenções definidas em "
        f"`000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`.\n"
        f"\n"
        f"---\n"
        f"\n"
        f"# 3. Versionamento\n"
        f"\n"
        f"| Versão | Data       | Descrição                                           |\n"
        f"| ------ | ---------- | --------------------------------------------------- |\n"
        f"| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato   |\n"
        f"\n"
        f"---\n"
        f"\n"
        f"**Documento:** {documento}\n"
        f"\n"
        f"**Última atualização:** 2026-08-20\n"
        f"\n"
        f"**Responsável:** Equipe SIGMUN\n"
        f"\n"
        f"**Status da revisão:** Em elaboração\n"
    )


def main():
    """Cria os 26 esboços padronizados (001-026) para cada domínio do SIGMUN (pt-BR).

    Omite o domínio-piloto ``DOM-COMPRAS-001`` (já completo) e qualquer domínio
    listado em ``EXCLUIR``.
    """
    criados, erros = [], []
    for codigo, nome, slug in DOMAINS:
        if codigo in EXCLUIR:
            continue
        pasta = BASE / codigo
        if not pasta.exists():
            erros.append(f"{codigo}: diretório não encontrado")
            continue
        for prefixo, titulo, descricao in ARTEFATOS:
            destino = pasta / f"{prefixo}-{slug}.md"
            try:
                conteudo = gerar_placeholder(
                    codigo, nome, slug, prefixo, titulo, descricao)
                destino.write_text(conteudo, encoding="utf-8")
                criados.append(f"{codigo}: {destino.name}")
            except OSError as exc:
                erros.append(f"{codigo}/{destino.name}: {exc}")
    print("=== ARQUIVOS CRIADOS ===")
    for c in criados:
        print(" OK ", c)
    print("=== ERROS ===")
    for e in erros:
        print(" ERRO ", e)
    print(f"Total criados: {len(criados)} | Erros: {len(erros)}")


if __name__ == "__main__":
    main()