# 007 – Regras-de-Negocio – Administração Tributária

#### Regras-de-Negocio – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-007

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **as regras de negócio** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Regras implementadas

| Identificador | Descrição | Fonte |
| --- | --- | --- |
| RN-TRI-001 | CPF/CNPJ do contribuinte é único e validado | `src/modules/sigmun_tributos` |
| RN-TRI-002 | inscrição municipal é um atributo do cadastro, mas não substitui | `src/modules/sigmun_tributos` |
| RN-TRI-010 | inscrição imobiliária é única no município | `src/modules/sigmun_tributos` |
| RN-TRI-011 | o IPTU é calculado sobre o valor venal aplicando a alíquota | `src/modules/sigmun_tributos` |
| RN-TRI-020 | o lançamento constitui o crédito tributário com base de cálculo | `src/modules/sigmun_tributos` |
| RN-TRI-021 | o valor total do lançamento é tributo + juros + multa | `src/modules/sigmun_tributos` |
| RN-TRI-022 | um lançamento pago ou já inscrito em dívida ativa não pode ser | `src/modules/sigmun_tributos` |
| RN-TRI-030 | a inscrição em dívida ativa formaliza créditos vencidos e não | `src/modules/sigmun_tributos` |
| RN-TRI-031 | valores atualizados (juros e multa) podem ser recompostos até a | `src/modules/sigmun_tributos` |
| RN-TRI-040 | a certidão negativa é emitida somente quando o contribuinte não | `src/modules/sigmun_tributos` |
| RN-TRI-041 | a certidão positiva com efeitos de negativa cobre as demais | `src/modules/sigmun_tributos` |

---

# 3. Cobertura

Regras referenciadas no código: **11**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 007-Administracao-Tributaria-Regras-de-Negocio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
