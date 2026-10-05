# 011 – Criterios-de-Aceitacao – Segurança da Informação

#### Criterios-de-Aceitacao – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-011

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **os critérios de aceitação** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Critérios

| ID | Categoria | Critério | Verificação |
| --- | --- | --- | --- |
| CA-SEG-001 | Confidencialidade | Credencial nunca é exposta; apenas metadado e situação. | Teste automatizado |
| CA-SEG-002 | Revogação | Credencial e chave revogadas não podem ser reutilizadas. | Teste automatizado |
| CA-SEG-003 | Auditoria | Política, controle, credencial e incidente registram autor e data. | Teste automatizado |
| CA-SEG-004 | Segregação | Permissões do próprio domínio seguem o princípio do menor privilégio. | Teste automatizado |
| CA-SEG-005 | Compatibilidade | Sem chave estrangeira entre schemas. | Teste automatizado |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 011-Seguranca-da-Informacao-Criterios-de-Aceitacao.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
