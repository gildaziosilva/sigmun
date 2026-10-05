# 004 – Mapa-de-Servicos – Gestão Patrimonial

#### Mapa-de-Servicos – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-004

**Domínio:** Gestão Patrimonial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Patrimonial.md`
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

Este artefato detalha **o mapa de serviços** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/pat`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| GET | `/api/v1/pat/bens` | bens | Listar Bens |
| POST | `/api/v1/pat/bens` | bens | Cadastrar Bem |
| GET | `/api/v1/pat/bens/{bem_id}` | bens | Obter Bem |
| POST | `/api/v1/pat/bens/{bem_id}/baixar` | bens | Baixar Bem |
| GET | `/api/v1/pat/bens/{bem_id}/depreciacoes` | bens | Listar Depreciacoes |
| POST | `/api/v1/pat/bens/{bem_id}/depreciar` | bens | Depreciar Bem |
| POST | `/api/v1/pat/transferencias` | transferencias | Transferir Bem |
| POST | `/api/v1/pat/transferencias/{transferencia_id}/concluir` | transferencias | Concluir Transferencia |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| bens | 6 |
| transferencias | 2 |

---

# 4. Lacunas a validar

* Definir a tabela de depreciação por tipo de bem.
* Definir a integração de baixa com o DOM-CON.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Gestao-Patrimonial-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
