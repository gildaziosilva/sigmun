# 023 – Plano de Treinamento – Contabilidade Pública

#### Plano de Treinamento – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-023

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato define o plano de treinamento do domínio de Contabilidade Pública,
identificando o público-alvo, o conteúdo por perfil, a metodologia e os critérios de
aprovação.

---

# 2. Público-Alvo

| Perfil | Conhecimento prévio | Carga horária estimada |
| --- | --- | --- |
| Contador da execução orçamentária | Contabilidade básica | 16 h |
| Ordenador de despesa | Gestão pública | 8 h |
| Tesoureiro | Operação financeira | 8 h |
| Gestor do plano de contas | PCASP | 12 h |
| Contador da conciliação | Conciliação bancária | 8 h |
| Controle interno | Auditoria | 8 h |
| Administrators do sistema | Operação de TI | 8 h |

**Total estimado:** 68 horas de carga horária por perfil.

---

# 3. Conteúdo por Perfil

## 3.1 Contador da execução orçamentária

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Fundamentos | Fases da despesa (Lei 4.320/64), dotação, empenho, liquidação, pagamento | 4 |
| Empenho | Emissão, numeração por exercício, estorno, anulação, cancelamento | 3 |
| Liquidação | Direito adquirido, documento fiscal, saldo a liquidar | 3 |
| Pagamento | Ordem bancária, saldo a pagar, liquidação confirmada | 2 |
| Lançamento contábil | Partidas dobradas, contas analíticas do PCASP | 3 |
| Erros comuns | Duplicidade de número, saldo insuficiente, liquidação não confirmada | 1 |

## 3.2 Ordenador de despesa

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Autorização | Fluxo de aprovação e sua relação com a segregação de funções | 3 |
| Cancelamento | Quando cancelar e quando anular; consequências no orçamento | 2 |
| Consulta | Consulta da execução e verificação de saldo | 2 |
| Responsabilidade | Consequências da autorização e dever de responsabilização | 1 |

## 3.3 Tesoureiro

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Pagamento | Pré-requisitos da liquidação, saldo a pagar | 3 |
| Execução | Programação, efetivação e cancelamento | 3 |
| Controle | Conferência de conta bancária e número da ordem | 2 |

## 3.4 Gestor do plano de contas

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| PCASP | Estrutura, classes, grupos e naturezas de saldo | 4 |
| Hierarquia | Contas sintéticas e analíticas | 2 |
| Uso | Lançamento em conta válida, ativação e desativação | 3 |
| Carga | Importação e validação do plano municipal | 3 |

## 3.5 Contador da conciliação

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Conciliação | Saldo contábil contra extrato, competência | 4 |
| Divergência | Diagnóstico e justificativa | 3 |
| Registro | Lançamento da conciliação e acompanhamento | 1 |

## 3.6 Controle interno

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Consulta | Extrato da execução e verificação por exercício | 3 |
| Auditoria | Autoria, trilha e responsabilização | 3 |
| Irregularidades | Como reportar e quais sinais observar | 2 |

## 3.7 Administração do sistema

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Operação | Implantação, Health-check e logs | 2 |
| Persistência | Schema `con`, migrations, backup e recuperação | 3 |
| Permissões | Perfis e segregação de funções | 2 |
| Incidentes | Diagnóstico de falhas comuns e escalonamento | 1 |

---

# 4. Metodologia

| Fase | Descrição |
| --- | --- |
| 1. Conceitual | Aula expositiva sobre as fases da despesa e a norma aplicável |
| 2. Prático | Hands-on com o ambiente de homologação |
| 3. Cenários | Estudo de casos de erros frequentes e suas causas |
| 4. Avaliação | Prova prática com cenário completo do ciclo da despesa |

**Recursos:** manuais do usuário, artefatos 000 a 026 do domínio, diagrama do ciclo
da despesa e do estado do empenho.

---

# 5. Critérios de Aprovação

| Critério | Peso | Resultado mínimo |
| --- | --- | --- |
| Prova teórica | 30 % | 70 % de acerto |
| Cenário prático completo | 40 % | Executar o ciclo sem erro |
| Identificação de erros | 30 % | 70 % de acerto |

**Aprovação mínima:** 70 % no total **e** execução completa do cenário prático.

O cenário prático exige que o servidor emita um empenho sobre dotação de teste, liquide,
pague, registre o lançamento, anule um segundo empenho e consulte a execução.

---

# 6. Cronograma

| Etapa | Prazo | Responsável |
| --- | --- | --- |
| Elaboração dos materiais | Após a conclusão da Onda 5 | Equipe SIGMUN |
| Treinamento de multiplicadores | 1 semana antes | Contabilidade municipal |
| Treinamento dos perfis | Semana de implantação | Equipe SIGMUN |
| Reforço | 30 dias após | Contabilidade municipal |
| Avaliação de eficácia | 60 dias após | Controle interno |

---

# 7. Riscos

| Risco | Mitigação |
| --- | --- |
| Treinamento antes da exposição da API | Treinar apenas após a Onda 2 |
| Resistência de servidores habituados ao controle manual | Destacar a rastreabilidade e a segurança |
| Baixa participação | Sessões por turno e material assíncrono |
| Baixa retenção sem uso real | Acompanhamento na primeira semana |
| Divergência entre material e sistema | Validar materiais contra o ambiente de homologação |


---

Este artefato define o plano de treinamento do domínio de Contabilidade Pública,
identificando o público-alvo, o conteúdo por perfil, a metodologia e os critérios de
aprovação.

---

# 2. Público-Alvo

| Perfil | Conhecimento prévio | Carga horária estimada |
| --- | --- | --- |
| Contador da execução orçamentária | Contabilidade básica | 16 h |
| Ordenador de despesa | Gestão pública | 8 h |
| Tesoureiro | Operação financeira | 8 h |
| Gestor do plano de contas | PCASP | 12 h |
| Contador da conciliação | Conciliação bancária | 8 h |
| Controle interno | Auditoria | 8 h |
| Administrators do sistema | Operação de TI | 8 h |

**Total estimado:** 68 horas de carga horária por perfil.

---

# 3. Conteúdo por Perfil

## 3.1 Contador da execução orçamentária

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Fundamentos | Fases da despesa (Lei 4.320/64), dotação, empenho, liquidação, pagamento | 4 |
| Empenho | Emissão, numeração por exercício, estorno, anulação, cancelamento | 3 |
| Liquidação | Direito adquirido, documento fiscal, saldo a liquidar | 3 |
| Pagamento | Ordem bancária, saldo a pagar, liquidação confirmada | 2 |
| Lançamento contábil | Partidas dobradas, contas analíticas do PCASP | 3 |
| Erros comuns | Duplicidade de número, saldo insuficiente, liquidação não confirmada | 1 |

## 3.2 Ordenador de despesa

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Autorização | Fluxo de aprovação e sua relação com a segregação de funções | 3 |
| Cancelamento | Quando cancelar e quando anular; consequências no orçamento | 2 |
| Consulta | Consulta da execução e verificação de saldo | 2 |
| Responsabilidade | Consequências da autorização e dever de responsabilização | 1 |

## 3.3 Tesoureiro

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Pagamento | Pré-requisitos da liquidação, saldo a pagar | 3 |
| Execução | Programação, efetivação e cancelamento | 3 |
| Controle | Conferência de conta bancária e número da ordem | 2 |

## 3.4 Gestor do plano de contas

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| PCASP | Estrutura, classes, grupos e naturezas de saldo | 4 |
| Hierarquia | Contas sintéticas e analíticas | 2 |
| Uso | Lançamento em conta válida, ativação e desativação | 3 |
| Carga | Importação e validação do plano municipal | 3 |

## 3.5 Contador da conciliação

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Conciliação | Saldo contábil contra extrato, competência | 4 |
| Divergência | Diagnóstico e justificativa | 3 |
| Registro | Lançamento da conciliação e acompanhamento | 1 |

## 3.6 Controle interno

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Consulta | Extrato da execução e verificação por exercício | 3 |
| Auditoria | Autoria, trilha e responsabilização | 3 |
| Irregularidades | Como reportar e quais sinais observar | 2 |

## 3.7 Administração do sistema

| Módulo | Conteúdo | Horas |
| --- | --- | --- |
| Operação | Implantação, Health-check e logs | 2 |
| Persistência | Schema `con`, migrations, backup e recuperação | 3 |
| Permissões | Perfis e segregação de funções | 2 |
| Incidentes | Diagnóstico de falhas comuns e escalonamento | 1 |

---

# 4. Metodologia

| Fase | Descrição |
| --- | --- |
| 1. Conceitual | Aula expositiva sobre as fases da despesa e a norma aplicável |
| 2. Prático | Hands-on com o ambiente de homologação |
| 3. Cenários | Estudo de casos de erros frequentes e suas causas |
| 4. Avaliação | Prova prática com cenário completo do ciclo da despesa |

**Recursos:** manuais do usuário, artefatos 000 a 026 do domínio, diagrama do ciclo
da despesa e do estado do empenho.

---

# 5. Critérios de Aprovação

| Critério | Peso | Resultado mínimo |
| --- | --- | --- |
| Prova teórica | 30 % | 70 % de acerto |
| Cenário prático completo | 40 % | Executar o ciclo sem erro |
| Identificação de erros | 30 % | 70 % de acerto |

**Aprovação mínima:** 70 % no total **e** execução completa do cenário prático.

O cenário prático exige que o servidor emita um empenho sobre dotação de teste, liquide,
pague, registre o lançamento, anule um segundo empenho e consulte a execução.

---

# 6. Cronograma

| Etapa | Prazo | Responsável |
| --- | --- | --- |
| Elaboração dos materiais | Após a conclusão da Onda 5 | Equipe SIGMUN |
| Treinamento de multiplicadores | 1 semana antes | Contabilidade municipal |
| Treinamento dos perfis | Semana de implantação | Equipe SIGMUN |
| Reforço | 30 dias após | Contabilidade municipal |
| Avaliação de eficácia | 60 dias após | Controle interno |

---

# 7. Riscos

| Risco | Mitigação |
| --- | --- |
| Treinamento antes da exposição da API | Treinar apenas após a Onda 2 |
| Resistência de servidores habituados ao controle manual | Destacar a rastreabilidade e a segurança |
| Baixa participação | Sessões por turno e material assíncrono |
| Baixa retenção sem uso real | Acompanhamento na primeira semana |
| Divergência entre material e sistema | Validar materiais contra o ambiente de homologação |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 023-Plano-de-Treinamento-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
