# 015 – Arquitetura-de-Servicos – Indicadores e Desempenho

#### Arquitetura-de-Servicos – Indicadores e Desempenho

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IND-015

**Domínio:** Indicadores e Desempenho

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Indicadores-e-Desempenho.md`
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

Este artefato descreve **a arquitetura de serviços** do domínio Indicadores e Desempenho (`DOM-IND`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Camadas

| Camada | Conteúdo |
| --- | --- |
| presentation | Routers FastAPI e schemas Pydantic |
| application | Casos de uso, comandos e queries |
| domain | Entidades, objetos de valor e regras |
| infrastructure | Repositórios SQLAlchemy e modelos ORM |

---

# 3. Serviços previstos

| Prefixo | Operações |
| --- | --- |
| /api/v1/ind | 1 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 015-Indicadores-e-Desempenho-Arquitetura-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
