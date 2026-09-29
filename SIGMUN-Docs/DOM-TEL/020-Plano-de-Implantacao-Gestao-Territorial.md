# 020 – Plano de Implantação – Gestão Territorial

#### Plano de Implantação – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-020

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato define a sequência de implantação do domínio de Gestão Territorial no
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

1. Aplicar a migração `20260929_01_dom_tel_models`, que cria o schema `tel`.
2. Implantar a aplicação, registrando o router sob o prefixo `/api/v1/tel`.
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

* As operações do prefixo `/api/v1/tel` devem responder conforme o contrato.
* A aplicação do seed DEMO deve ser idempotente.
* A migração deve ser reversível.

---

# 6. Reversão

* A migração remove o schema e suas tabelas.
* Os dados de produção devem ser exportados antes de qualquer reversão, dado o
  caráter cadastral das informações.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 020-Plano-de-Implantacao-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
