# 003 – Mapa-de-Processos – Administração Tributária

#### Mapa-de-Processos – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-003

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

Este artefato detalha **o mapa de processos** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Processos do domínio

| Identificador | Processo | Descrição | Regras |
| --- | --- | --- | --- |
| PRO-TRI-001 | Cadastrar contribuinte | Registra contribuinte com documento. | RN-TRI-001 |
| PRO-TRI-002 | Cadastrar imóvel | Registra imóvel e vincula contribuinte. | RN-TRI-010, RN-TRI-011 |
| PRO-TRI-003 | Lançar e pagar | Lança crédito e registra pagamento. | RN-TRI-020, RN-TRI-021, RN-TRI-022 |
| PRO-TRI-004 | Inscrever em dívida ativa | Inscreve, baixa e emite certidão. | RN-TRI-030, RN-TRI-031, RN-TRI-040 |

---

# 3. Fluxo de trabalho

Captura → validação → classificação → gravação → consulta → atualização → exclusão lógica, conforme as regras do domínio.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 003-Administracao-Tributaria-Mapa-de-Processos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
