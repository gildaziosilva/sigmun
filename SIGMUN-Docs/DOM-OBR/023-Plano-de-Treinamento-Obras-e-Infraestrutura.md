# 023 – Plano de Treinamento – Obras e Infraestrutura

#### Plano de Treinamento – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-023

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
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
Obras e Infraestrutura.

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
| Regras e validações | 4h | RN-OBR-001 (Unicidade do Número da Obra); RN-OBR-002 (Ciclo de Vida da Obra); RN-OBR-003 (Pré-condições para Iniciar a Execução); RN-OBR-004 (Coerência Físico-Financeira da Obra); RN-OBR-005 (Ciclo de Vida da Medição e Composição do Avanço); RN-OBR-006 (Limite da Despesa ao Valor Medido); RN-OBR-007 (Ciclo de Vida da Etapa e Escala de Percentuais); RN-OBR-008 (Registro de Vistoria Fiscalizadora) |
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

**Documento:** 023-Plano-de-Treinamento-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
