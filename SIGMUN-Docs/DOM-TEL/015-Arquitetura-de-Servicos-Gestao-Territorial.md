# 015 – Arquitetura de Serviços – Gestão Territorial

#### Arquitetura de Serviços – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-015

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

Este artefato descreve a arquitetura interna do módulo `sigmun_territorial`, adotando a
estrutura em camadas do SIGMUN.

---

# 2. Camadas

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/sigmun_territorial/domain` | Entidades, invariantes e exceções de negócio |
| Aplicação | `src/modules/sigmun_territorial/application` | Ports (contratos) e casos de uso |
| Infraestrutura | `src/modules/sigmun_territorial/infrastructure` | Modelos ORM, repositórios e seeds |
| Apresentação | `src/modules/sigmun_territorial/presentation` | Schemas de entrada e saída e endpoints |

* A camada de domínio não depende de infraestrutura nem de framework web.
* A camada de apresentação converte exceções de domínio em respostas HTTP.

---

# 3. Componentes

| Componente | Quantidade | Responsabilidade |
| --- | | --- | |
| Entidades de domínio | 4 | Invariantes e transições de estado |
| Casos de uso | 12 | Orquestração de regras e persistência |
| Paths REST | 15 | Contrato HTTP versionado |
| Tabelas | 4 | Persistência relacional |


---

# 4. Ports e Adaptadores

* `application/interfaces.py` define `Protocol`s de repositório por agregado.
* `infrastructure/repositories` implementa cada port com SQLAlchemy.
* `presentation/api/deps.py` injeta os adaptadores como dependências do FastAPI.

---

# 5. Fluxo de uma Requisição

1. O endpoint valida a entrada pelo schema Pydantic.
2. O caso de uso aplica as regras de negócio sobre a entidade.
3. O repositório persiste a entidade e devolve a entidade gravada.
4. O mapeador converte a entidade na resposta HTTP.

---

# 6. Testabilidade

As regras são exercitadas por testes unitários com repositórios simulados, pela
substituição do port; a persistência é verificada em testes de integração sobre
PostgreSQL.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 015-Arquitetura-de-Servicos-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
