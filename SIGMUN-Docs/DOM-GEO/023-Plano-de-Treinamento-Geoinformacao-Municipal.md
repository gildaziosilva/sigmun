# 023 – Plano de Treinamento – Geoinformação Municipal

#### Plano de Treinamento – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-023

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
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

Este artefato define o plano de capacitação dos usuários do domínio de
Geoinformação Municipal.

---

# 2. Públicos-Alvo

| Público | Foco do treinamento |
| --- | --- |
| Técnico de cadastro | Operação diária e validação de cadastros |
| Comissão de valores | Elaboração, aprovação e revogação da planta |
| Avaliador fiscal | Apuração do valor venal e consulta de valores |
| Suporte técnico | Diagnóstico de incidentes e execução de carga |

---

# 3. Conteúdo Programático

| Módulo | Carga horária | Conteúdo |
| --- | --- | --- |
| Fundamentos do domínio | 4h | Conceitos, entidades e vínculos entre cadastros |
| Operação cadastral | 8h | Cadastro, alteração, filtros e exclusão lógica |
| Regras e validações | 4h | RN-GEO-001 (Unicidade do Código da Camada); RN-GEO-002 (Unicidade do Código do Mapa); RN-GEO-003 (Integridade da Geometria do Elemento); RN-GEO-004 (Ciclo de Vida do Mapa e Congelamento da Composição); RN-GEO-005 (Coerência Cartográfica do Mapa e do Serviço); RN-GEO-006 (Ciclo de Vida da Camada e Exigência de URL de Serviço); RN-GEO-007 (Validação do Serviço Geoespacial); RN-GEO-008 (Vinculação do Elemento Geoespacial e da Composição) |
| Integração com outros domínios | 2h | Consulta da planta de valores e contratos |
| Prática com seed DEMO | 4h | Carga, consulta e limpeza de dados de teste |

---

# 4. Metodologia

* Treinamento presencial com acesso ao ambiente de homologação.
* Exercícios práticos com o seed DEMO, sem risco aos dados de produção.
* Avaliação por conclusão de caso prático.

---

# 5. Critérios de Aprovação

* Participação de 100% da carga horária.
* Conclusão correta do caso prático proposto.
* Compreensão das regras que geram as recusas mais frequentes.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 023-Plano-de-Treinamento-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
