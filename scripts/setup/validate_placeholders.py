# -*- coding: utf-8 -*-
"""Validacao Etapa 3: verifica 27 artefatos por diretorio DOM-*, sem mistura de idiomas.

Uso:
    python validate_placeholders.py
"""
import re
from pathlib import Path

BASE = Path(r"C:\ProjetosPython\sigmun-v1\sigmun-v1\SIGMUN-Docs")

# Os 27 prefixos de artefatos esperados (000-026)
PREFIXOS = [
    "000-Dominio", "001-Mapa-de-Atores", "002-Mapa-de-Capacidades",
    "003-Mapa-de-Processos", "004-Mapa-de-Servicos", "005-Casos-de-Uso",
    "006-Historias-de-Usuario", "007-Regras-de-Negocio",
    "008-Requisitos-Funcionais", "009-Requisitos-Nao-Funcionais",
    "010-Especificacoes", "011-Criterios-de-Aceitacao",
    "012-Matriz-de-Rastreabilidade", "013-Modelo-de-Dados",
    "014-Modelo-de-Integracao", "015-Arquitetura-de-Servicos",
    "016-Modelo-de-Seguranca", "017-Modelo-de-Auditoria",
    "018-Plano-de-Testes", "019-Casos-de-Teste", "020-Plano-de-Implantacao",
    "021-Checklist-de-Prontidao-para-Producao", "022-Plano-de-Migracao-de-Dados",
    "023-Plano-de-Treinamento", "024-Plano-de-Suporte-e-Operacao",
    "025-Estrutura-Tecnica", "026-Modelo-de-Dominio",
]

# Os 32 dominios (exclui DOM-COMPRAS-001 que e o piloto)
DOMS = [
    "DOM-GOV", "DOM-PLA", "DOM-GDO", "DOM-TRI", "DOM-ORC", "DOM-CON",
    "DOM-PES", "DOM-CPT", "DOM-PAT", "DOM-FRO", "DOM-TEL", "DOM-IMO",
    "DOM-GEO", "DOM-OBR", "DOM-SAU", "DOM-EDU", "DOM-ASS", "DOM-MAM",
    "DOM-DEC", "DOM-CUM", "DOM-ATE", "DOM-OUV", "DOM-DAD", "DOM-MET",
    "DOM-IND", "DOM-ANA", "DOM-IDN", "DOM-SEG", "DOM-INT", "DOM-MOB",
    "DOM-INF", "DOM-DIA",
]

# Palavras em ingles a detectar no conteudo
PALAVRAS_INGLES = [
    "placeholder", "under development", "in progress",
    "draft", "backlog", "todo",
]


def main():
    erros = 0
    total_files = 0
    ingles = 0
    mojibake = 0
    fmt_ok = 0
    fmt_err = 0
    naming_err = 0

    # 1. DOM-COMPRAS-001 preservado
    pilot = BASE / "DOM-COMPRAS-001"
    pfiles = sorted(f.name for f in pilot.glob("*.md"))
    if len(pfiles) == 27:
        print("[OK] DOM-COMPRAS-001 preservado - 27 arquivos")
    else:
        print("[ERRO] DOM-COMPRAS-001 deveria ter 27, tem " + str(len(pfiles)))
        erros += 1

    # 2. Os 32 dominios + piloto
    for d in DOMS + ["DOM-COMPRAS-001"]:
        dd = BASE / d
        if not dd.exists():
            print("[ERRO] " + d + " nao existe")
            erros += 1
            continue
        files = sorted(f.name for f in dd.glob("*.md"))
        total_files += len(files)
        if len(files) != 27:
            print("[ERRO] " + d + " tem " + str(len(files)) +
                  " arquivos (esperado 27)")
            erros += 1
        elif d != "DOM-COMPRAS-001":
            print("[OK] " + d + " - 27 artefatos")
        # nomenclatura
        for p in PREFIXOS:
            found = any(f.startswith(p + "-") and f.endswith(".md")
                        for f in files)
            if not found:
                print("  [ERRO] " + d + " - falta artefato: " + p)
                erros += 1
                naming_err += 1

    # 3. Conteudo: idioma, mojibake, formato
    for d in DOMS:
        dd = BASE / d
        for f in sorted(dd.glob("*.md")):
            content = f.read_text(encoding="utf-8", errors="replace")
            # mojibake
            if re.search(r"[\xc3][\xa0-\xb7]", content):
                mojibake += 1
                print("  [MOJIBAKE] " + d + "/" + f.name)
            # ingles no corpo (exclui nomes entre backticks)
            body_lines = [l for l in content.split("\n")
                          if not l.strip().startswith("* `")]
            body = "\n".join(body_lines)
            for word in PALAVRAS_INGLES:
                if re.search(r"\b" + re.escape(word) + r"\b", body, re.I):
                    ingles += 1
                    print("  [INGLES] " + d + "/" + f.name + ": " + word)
                    break
            # formato padronizado (apenas 001-026)
            if f.name.startswith("000-"):
                continue
            if "**Status:** Em elaboracao" in content or \
               "**Status:** Em elaboração" in content:
                fmt_ok += 1
            else:
                fmt_err += 1
                print("  [FORMATO] " + d + "/" + f.name)

    print()
    print("=" * 60)
    print("RELATORIO DE VALIDACAO - Etapa 3")
    print("=" * 60)
    print("Diretorios verificados:          " + str(len(DOMS) + 1) +
          " (32 + piloto)")
    print("Total de arquivos .md em DOM-*:   " + str(total_files))
    print("Erros criticos:                  " + str(erros))
    print("Erros de nomenclatura:           " + str(naming_err))
    print("Problemas de mojibake:           " + str(mojibake))
    print("Palavras em ingles no conteudo:  " + str(ingles))
    print("Formato padronizado OK:          " + str(fmt_ok) +
          " / Erro: " + str(fmt_err))
    print()
    if erros == 0 and mojibake == 0 and ingles == 0 and fmt_err == 0:
        print("VALIDACAO: PASSOU")
    else:
        print("VALIDACAO: FALHOU")


if __name__ == "__main__":
    main()
