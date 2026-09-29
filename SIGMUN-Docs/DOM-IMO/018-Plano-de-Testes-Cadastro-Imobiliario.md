# 018 – Plano de Testes – Cadastro Imobiliário

#### Plano de Testes – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-018

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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

Este artefato define a estratégia de verificação do domínio de Cadastro Imobiliário,
abrangendo regras de negócio, persistência, contrato de API e integração.

---

# 2. Níveis de Teste

| Nível | Escopo | Técnica | Artefatos |
| --- | --- | --- | --- |
| Unitário | Regras e casos de uso | Ports simulados | `tests/unit/` |
| Integração | Persistência, migração e seeds | PostgreSQL real | `tests/integration/` |
| Contrato | Compatibilidade da API | OpenAPI publicado | Verificação de paths |
| End-to-end | Fluxo completo do usuário | Round-trip HTTP | Roteiro de verificação |
| Estático | Qualidade do código | `ruff` e `mypy` | Módulo de aplicação |

---

# 3. Cobertura de Regras

| Regra | Testes que a exercitam |
| --- | |
| RN-IMO-001 | 0 teste(s) |
| RN-IMO-002 | 0 teste(s) |
| RN-IMO-003 | 0 teste(s) |
| RN-IMO-004 | 0 teste(s) |
| RN-IMO-005 | 0 teste(s) |
| RN-IMO-006 | 0 teste(s) |
| RN-IMO-007 | 0 teste(s) |


---

# 4. Suíte de Testes Unitários

| Arquivo | Classe | Testes |
| --- | | --- | |
| `tests/unit/test_imo_avaliacao_use_cases.py` | TestAvaliacao | 14 |
| `tests/unit/test_imo_avaliacao_use_cases.py` | TestOcupacao | 1 |
| `tests/unit/test_imo_geometria_use_cases.py` | TestGeometria | 11 |
| `tests/unit/test_imo_geometria_use_cases.py` | TestCaracteristica | 5 |
| `tests/unit/test_imo_imoveis_use_cases.py` | TestImovel | 17 |
| `tests/unit/test_imo_imoveis_use_cases.py` | TestProprietario | 10 |


**Total de testes de unidade:** 58

> A contagem refere-se a **funções de teste** (`def test_*`). Casos gerados por
> parametrização (`pytest.mark.parametrize`) são contados uma única vez, embora
> gerem múltiplas execuções na suíte.

---

# 5. Testes de Integração

* `tests/integration/` verifica a aplicação das migrações, a idempotência do
  seed DEMO e a limpeza dos dados.
* As invariantes unique e check são exercitadas contra o banco real.

---

# 6. Critérios de Saída

* Todos os testes unitários e de integração aprovados.
* `ruff check` e `mypy` sem erros no módulo.
* `npm run build` do frontend administrativo sem erros.
* Round-trip E2E das operações de escrita, leitura e transição.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 018-Plano-de-Testes-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
