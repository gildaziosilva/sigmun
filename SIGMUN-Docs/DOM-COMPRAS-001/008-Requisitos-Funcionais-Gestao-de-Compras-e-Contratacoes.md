# 008 – Requisitos Funcionais – Gestão de Compras e Contratações

#### Requisitos Funcionais – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
* 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
* 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
* 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
* 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
* 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Servicos.md
* Modelo-de-Competencias.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md

---

# 1. Finalidade

Este documento define os **Requisitos Funcionais do Domínio de Gestão de Compras e Contratações** do SIGMUN.

Os requisitos funcionais descrevem comportamentos, funcionalidades, operações e respostas que o sistema deverá oferecer para atender às necessidades identificadas nas:

* capacidades;
* processos;
* serviços;
* casos de uso;
* histórias de usuário;
* regras de negócio.

Os requisitos deste documento deverão servir como base para:

* especificações;
* desenvolvimento;
* testes;
* critérios de aceitação;
* integrações;
* estimativas;
* planejamento de releases;
* rastreabilidade.

---

# 2. Convenção de Identificação

Os requisitos funcionais utilizarão o padrão:

```text
RF-COMPRAS-XXX
```

Exemplo:

```text
RF-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida do requisito.

---

# 3. Estrutura do Requisito

Cada requisito deverá possuir:

* identificador;
* título;
* descrição;
* origem;
* regra de negócio relacionada;
* prioridade;
* dependências;
* observações, quando aplicável.

Modelo:

```text
RF-COMPRAS-XXX – Título

O sistema deverá ...

Origem:
HU-COMPRAS-XXX

Regras:
RN-COMPRAS-XXX

Prioridade:
P1
```

---

# 4. Classificação de Prioridade

| Prioridade | Significado            |
| ---------- | ---------------------- |
| P0         | Essencial / bloqueante |
| P1         | Alta                   |
| P2         | Média                  |
| P3         | Baixa                  |

A prioridade poderá ser revista durante o planejamento do produto.

---

# 5. Requisitos Funcionais – Planejamento

## RF-COMPRAS-001 – Registrar Planejamento de Contratação

O sistema deverá permitir registrar uma contratação planejada.

**Origem:**

* HU-COMPRAS-001

**Regras relacionadas:**

* RN-COMPRAS-005
* RN-COMPRAS-008

**Prioridade:** P1

---

## RF-COMPRAS-002 – Consultar Planejamento de Contratações

O sistema deverá permitir consultar as contratações planejadas.

**Origem:**

* HU-COMPRAS-001
* HU-COMPRAS-056

**Regras relacionadas:**

* RN-COMPRAS-005
* RN-COMPRAS-007

**Prioridade:** P1

---

## RF-COMPRAS-003 – Consolidar Necessidades

O sistema deverá permitir identificar e consolidar necessidades semelhantes.

**Origem:**

* HU-COMPRAS-002

**Regras relacionadas:**

* RN-COMPRAS-006

**Prioridade:** P1

---

## RF-COMPRAS-004 – Classificar Prioridade da Contratação

O sistema deverá permitir classificar a prioridade de uma contratação conforme critérios configurados.

**Origem:**

* HU-COMPRAS-003

**Regras relacionadas:**

* RN-COMPRAS-007

**Prioridade:** P1

---

# 6. Requisitos Funcionais – Necessidades e Requisições

## RF-COMPRAS-005 – Registrar Necessidade

O sistema deverá permitir registrar uma necessidade de compra ou contratação.

**Origem:**

* HU-COMPRAS-004

**Regras relacionadas:**

* RN-COMPRAS-001
* RN-COMPRAS-009
* RN-COMPRAS-010

**Prioridade:** P0

---

## RF-COMPRAS-006 – Identificar Unidade Requisitante

O sistema deverá registrar a unidade administrativa responsável pela solicitação.

**Origem:**

* HU-COMPRAS-004
* HU-COMPRAS-005

**Regras relacionadas:**

* RN-COMPRAS-009

**Prioridade:** P0

---

## RF-COMPRAS-007 – Identificar Requisitante

O sistema deverá registrar o usuário responsável pelo registro da necessidade.

**Origem:**

* HU-COMPRAS-004

**Regras relacionadas:**

* RN-COMPRAS-009
* RN-COMPRAS-110

**Prioridade:** P0

---

## RF-COMPRAS-008 – Registrar Justificativa

O sistema deverá permitir registrar a justificativa da necessidade.

**Origem:**

* HU-COMPRAS-004

**Regras relacionadas:**

* RN-COMPRAS-010

**Prioridade:** P0

---

## RF-COMPRAS-009 – Registrar Objeto

O sistema deverá permitir registrar a descrição do objeto pretendido.

**Origem:**

* HU-COMPRAS-005
* HU-COMPRAS-008

**Regras relacionadas:**

* RN-COMPRAS-011
* RN-COMPRAS-016

**Prioridade:** P0

---

## RF-COMPRAS-010 – Registrar Quantidade

O sistema deverá permitir informar a quantidade necessária para cada item quando aplicável.

**Origem:**

* HU-COMPRAS-005

**Regras relacionadas:**

* RN-COMPRAS-012
* RN-COMPRAS-013

**Prioridade:** P0

---

## RF-COMPRAS-011 – Registrar Unidade de Medida

O sistema deverá permitir informar a unidade de medida dos itens quantificáveis.

**Origem:**

* HU-COMPRAS-005

**Regras relacionadas:**

* RN-COMPRAS-013

**Prioridade:** P1

---

## RF-COMPRAS-012 – Anexar Documento à Requisição

O sistema deverá permitir anexar documentos à requisição.

**Origem:**

* HU-COMPRAS-005

**Regras relacionadas:**

* RN-COMPRAS-014
* RN-COMPRAS-060

**Prioridade:** P1

---

## RF-COMPRAS-013 – Submeter Requisição

O sistema deverá permitir submeter uma requisição para análise.

**Origem:**

* HU-COMPRAS-005

**Regras relacionadas:**

* RN-COMPRAS-027
* RN-COMPRAS-105
* RN-COMPRAS-106

**Prioridade:** P0

---

## RF-COMPRAS-014 – Aprovar Requisição

O sistema deverá permitir que usuário autorizado aprove ou rejeite uma requisição.

**Origem:**

* HU-COMPRAS-006

**Regras relacionadas:**

* RN-COMPRAS-015
* RN-COMPRAS-074

**Prioridade:** P0

---

## RF-COMPRAS-015 – Consultar Situação da Requisição

O sistema deverá permitir ao solicitante consultar a situação atual de sua requisição.

**Origem:**

* HU-COMPRAS-007

**Regras relacionadas:**

* RN-COMPRAS-106
* RN-COMPRAS-107

**Prioridade:** P1

---

# 7. Requisitos Funcionais – Especificação

## RF-COMPRAS-016 – Registrar Especificação do Objeto

O sistema deverá permitir registrar a especificação detalhada do objeto.

**Origem:**

* HU-COMPRAS-008

**Regras relacionadas:**

* RN-COMPRAS-016
* RN-COMPRAS-018

**Prioridade:** P0

---

## RF-COMPRAS-017 – Validar Especificação

O sistema deverá permitir registrar a validação da especificação do objeto.

**Origem:**

* HU-COMPRAS-009

**Regras relacionadas:**

* RN-COMPRAS-019

**Prioridade:** P1

---

## RF-COMPRAS-018 – Registrar Observações Técnicas

O sistema deverá permitir registrar informações técnicas complementares relacionadas ao objeto.

**Origem:**

* HU-COMPRAS-008
* HU-COMPRAS-009

**Regras relacionadas:**

* RN-COMPRAS-018

**Prioridade:** P1

---

# 8. Requisitos Funcionais – Pesquisa de Preços

## RF-COMPRAS-019 – Registrar Pesquisa de Preços

O sistema deverá permitir registrar uma pesquisa de preços.

**Origem:**

* HU-COMPRAS-010

**Regras relacionadas:**

* RN-COMPRAS-020
* RN-COMPRAS-022

**Prioridade:** P0

---

## RF-COMPRAS-020 – Registrar Fonte de Preço

O sistema deverá permitir registrar a fonte utilizada para cada informação de preço.

**Origem:**

* HU-COMPRAS-010

**Regras relacionadas:**

* RN-COMPRAS-020
* RN-COMPRAS-021

**Prioridade:** P0

---

## RF-COMPRAS-021 – Registrar Data da Pesquisa

O sistema deverá registrar a data da obtenção de cada informação utilizada na pesquisa.

**Origem:**

* HU-COMPRAS-010

**Regras relacionadas:**

* RN-COMPRAS-022

**Prioridade:** P1

---

## RF-COMPRAS-022 – Calcular Estimativa de Preço

O sistema deverá permitir calcular ou registrar a estimativa de preço da contratação conforme metodologia definida.

**Origem:**

* HU-COMPRAS-011

**Regras relacionadas:**

* RN-COMPRAS-023

**Prioridade:** P0

---

## RF-COMPRAS-023 – Consultar Histórico de Preços

O sistema deverá permitir consultar preços históricos relacionados a objetos ou itens.

**Origem:**

* HU-COMPRAS-012

**Regras relacionadas:**

* RN-COMPRAS-024

**Prioridade:** P1

---

# 9. Requisitos Funcionais – Processo de Contratação

## RF-COMPRAS-024 – Abrir Processo de Contratação

O sistema deverá permitir abrir um processo administrativo de contratação.

**Origem:**

* HU-COMPRAS-013

**Regras relacionadas:**

* RN-COMPRAS-025
* RN-COMPRAS-026

**Prioridade:** P0

---

## RF-COMPRAS-025 – Gerar Identificador do Processo

O sistema deverá gerar identificador único para o processo.

**Origem:**

* HU-COMPRAS-013

**Regras relacionadas:**

* RN-COMPRAS-002

**Prioridade:** P0

---

## RF-COMPRAS-026 – Instruir Processo

O sistema deverá permitir incluir e organizar documentos e informações necessárias à instrução do processo.

**Origem:**

* HU-COMPRAS-014

**Regras relacionadas:**

* RN-COMPRAS-026
* RN-COMPRAS-060

**Prioridade:** P0

---

## RF-COMPRAS-027 – Controlar Pendências Processuais

O sistema deverá permitir registrar e acompanhar pendências que impeçam o avanço do processo.

**Origem:**

* HU-COMPRAS-014

**Regras relacionadas:**

* RN-COMPRAS-027

**Prioridade:** P1

---

## RF-COMPRAS-028 – Registrar Procedimento

O sistema deverá permitir registrar os dados do procedimento de contratação.

**Origem:**

* HU-COMPRAS-015

**Regras relacionadas:**

* RN-COMPRAS-026

**Prioridade:** P0

---

## RF-COMPRAS-029 – Registrar Atos do Procedimento

O sistema deverá permitir registrar os atos relevantes realizados durante o procedimento.

**Origem:**

* HU-COMPRAS-016

**Regras relacionadas:**

* RN-COMPRAS-028
* RN-COMPRAS-029

**Prioridade:** P0

---

## RF-COMPRAS-030 – Registrar Análise de Propostas

O sistema deverá permitir registrar a análise das propostas recebidas.

**Origem:**

* HU-COMPRAS-017

**Regras relacionadas:**

* RN-COMPRAS-028

**Prioridade:** P0

---

## RF-COMPRAS-031 – Registrar Julgamento

O sistema deverá permitir registrar o resultado do julgamento das propostas.

**Origem:**

* HU-COMPRAS-017

**Regras relacionadas:**

* RN-COMPRAS-028

**Prioridade:** P0

---

## RF-COMPRAS-032 – Registrar Decisão

O sistema deverá permitir registrar a decisão da autoridade competente.

**Origem:**

* HU-COMPRAS-018

**Regras relacionadas:**

* RN-COMPRAS-015
* RN-COMPRAS-028

**Prioridade:** P0

---

# 10. Requisitos Funcionais – Fornecedores

## RF-COMPRAS-033 – Cadastrar Fornecedor

O sistema deverá permitir cadastrar fornecedor.

**Origem:**

* HU-COMPRAS-019

**Regras relacionadas:**

* RN-COMPRAS-030
* RN-COMPRAS-031

**Prioridade:** P0

---

## RF-COMPRAS-034 – Consultar Fornecedor

O sistema deverá permitir consultar dados cadastrais de fornecedor.

**Origem:**

* HU-COMPRAS-020

**Regras relacionadas:**

* RN-COMPRAS-030

**Prioridade:** P1

---

## RF-COMPRAS-035 – Consultar Histórico do Fornecedor

O sistema deverá permitir consultar o histórico do relacionamento do fornecedor com o Município.

**Origem:**

* HU-COMPRAS-021

**Regras relacionadas:**

* RN-COMPRAS-032
* RN-COMPRAS-033

**Prioridade:** P1

---

# 11. Requisitos Funcionais – Formalização

## RF-COMPRAS-036 – Formalizar Contratação

O sistema deverá permitir registrar a formalização de uma contratação.

**Origem:**

* HU-COMPRAS-022

**Regras relacionadas:**

* RN-COMPRAS-034

**Prioridade:** P0

---

## RF-COMPRAS-037 – Registrar Instrumento de Contratação

O sistema deverá permitir registrar o instrumento correspondente à contratação.

**Origem:**

* HU-COMPRAS-023

**Regras relacionadas:**

* RN-COMPRAS-035

**Prioridade:** P0

---

# 12. Requisitos Funcionais – Gestão Contratual

## RF-COMPRAS-038 – Registrar Contrato

O sistema deverá permitir registrar um contrato.

**Origem:**

* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-036
* RN-COMPRAS-037
* RN-COMPRAS-038
* RN-COMPRAS-039

**Prioridade:** P0

---

## RF-COMPRAS-039 – Gerar Identificador do Contrato

O sistema deverá gerar identificador único para o contrato.

**Origem:**

* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-036

**Prioridade:** P0

---

## RF-COMPRAS-040 – Registrar Vigência

O sistema deverá permitir registrar o período de vigência do contrato.

**Origem:**

* HU-COMPRAS-024
* HU-COMPRAS-027

**Regras relacionadas:**

* RN-COMPRAS-037
* RN-COMPRAS-046

**Prioridade:** P0

---

## RF-COMPRAS-041 – Registrar Valor Contratual

O sistema deverá permitir registrar o valor contratual quando aplicável.

**Origem:**

* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-039
* RN-COMPRAS-099

**Prioridade:** P0

---

## RF-COMPRAS-042 – Acompanhar Contrato

O sistema deverá permitir consultar e acompanhar a situação do contrato.

**Origem:**

* HU-COMPRAS-025

**Regras relacionadas:**

* RN-COMPRAS-040

**Prioridade:** P0

---

## RF-COMPRAS-043 – Registrar Obrigação Contratual

O sistema deverá permitir registrar obrigações relacionadas ao contrato.

**Origem:**

* HU-COMPRAS-026

**Regras relacionadas:**

* RN-COMPRAS-040

**Prioridade:** P1

---

## RF-COMPRAS-044 – Acompanhar Obrigações

O sistema deverá permitir acompanhar o cumprimento das obrigações contratuais.

**Origem:**

* HU-COMPRAS-026

**Regras relacionadas:**

* RN-COMPRAS-043

**Prioridade:** P1

---

# 13. Requisitos Funcionais – Fiscalização

## RF-COMPRAS-045 – Designar Fiscal

O sistema deverá permitir registrar a designação de fiscal de contrato.

**Origem:**

* HU-COMPRAS-028

**Regras relacionadas:**

* RN-COMPRAS-041
* RN-COMPRAS-109

**Prioridade:** P0

---

## RF-COMPRAS-046 – Registrar Fiscalização

O sistema deverá permitir registrar atividades de fiscalização.

**Origem:**

* HU-COMPRAS-029

**Regras relacionadas:**

* RN-COMPRAS-042
* RN-COMPRAS-043

**Prioridade:** P0

---

## RF-COMPRAS-047 – Registrar Evidência de Fiscalização

O sistema deverá permitir vincular evidências às atividades de fiscalização.

**Origem:**

* HU-COMPRAS-029

**Regras relacionadas:**

* RN-COMPRAS-043

**Prioridade:** P1

---

## RF-COMPRAS-048 – Registrar Não Conformidade

O sistema deverá permitir registrar não conformidades relacionadas à execução contratual.

**Origem:**

* HU-COMPRAS-030

**Regras relacionadas:**

* RN-COMPRAS-044

**Prioridade:** P0

---

## RF-COMPRAS-049 – Acompanhar Tratamento de Não Conformidade

O sistema deverá permitir acompanhar o tratamento de não conformidades.

**Origem:**

* HU-COMPRAS-031

**Regras relacionadas:**

* RN-COMPRAS-045

**Prioridade:** P1

---

# 14. Requisitos Funcionais – Ocorrências

## RF-COMPRAS-050 – Registrar Ocorrência Contratual

O sistema deverá permitir registrar ocorrências relacionadas à execução do contrato.

**Origem:**

* HU-COMPRAS-032

**Regras relacionadas:**

* RN-COMPRAS-043
* RN-COMPRAS-044

**Prioridade:** P1

---

## RF-COMPRAS-051 – Acompanhar Ocorrência

O sistema deverá permitir acompanhar o tratamento das ocorrências registradas.

**Origem:**

* HU-COMPRAS-033

**Regras relacionadas:**

* RN-COMPRAS-045

**Prioridade:** P1

---

# 15. Requisitos Funcionais – Alterações Contratuais

## RF-COMPRAS-052 – Solicitar Alteração Contratual

O sistema deverá permitir registrar uma solicitação de alteração contratual.

**Origem:**

* HU-COMPRAS-034

**Regras relacionadas:**

* RN-COMPRAS-049

**Prioridade:** P1

---

## RF-COMPRAS-053 – Registrar Aditivo

O sistema deverá permitir registrar instrumento aditivo relacionado ao contrato.

**Origem:**

* HU-COMPRAS-035

**Regras relacionadas:**

* RN-COMPRAS-050
* RN-COMPRAS-051

**Prioridade:** P0

---

## RF-COMPRAS-054 – Registrar Prorrogação

O sistema deverá permitir registrar uma prorrogação contratual.

**Origem:**

* HU-COMPRAS-036

**Regras relacionadas:**

* RN-COMPRAS-048

**Prioridade:** P1

---

## RF-COMPRAS-055 – Registrar Reajuste ou Revisão

O sistema deverá permitir registrar reajustes ou revisões aplicáveis ao contrato.

**Origem:**

* HU-COMPRAS-037

**Regras relacionadas:**

* RN-COMPRAS-052
* RN-COMPRAS-099

**Prioridade:** P1

---

# 16. Requisitos Funcionais – Recebimento

## RF-COMPRAS-056 – Registrar Entrega

O sistema deverá permitir registrar a entrega de bens ou serviços.

**Origem:**

* HU-COMPRAS-038

**Regras relacionadas:**

* RN-COMPRAS-053

**Prioridade:** P0

---

## RF-COMPRAS-057 – Conferir Entrega

O sistema deverá permitir registrar a conferência da entrega.

**Origem:**

* HU-COMPRAS-039

**Regras relacionadas:**

* RN-COMPRAS-054

**Prioridade:** P0

---

## RF-COMPRAS-058 – Registrar Aceite

O sistema deverá permitir registrar o aceite de uma entrega.

**Origem:**

* HU-COMPRAS-040

**Regras relacionadas:**

* RN-COMPRAS-055

**Prioridade:** P0

---

## RF-COMPRAS-059 – Registrar Divergência

O sistema deverá permitir registrar divergências identificadas no recebimento.

**Origem:**

* HU-COMPRAS-041

**Regras relacionadas:**

* RN-COMPRAS-056

**Prioridade:** P1

---

# 17. Requisitos Funcionais – Encerramento

## RF-COMPRAS-060 – Registrar Encerramento da Execução

O sistema deverá permitir registrar o encerramento da execução contratual.

**Origem:**

* HU-COMPRAS-042

**Regras relacionadas:**

* RN-COMPRAS-057

**Prioridade:** P1

---

## RF-COMPRAS-061 – Encerrar Contrato

O sistema deverá permitir registrar o encerramento de um contrato.

**Origem:**

* HU-COMPRAS-043

**Regras relacionadas:**

* RN-COMPRAS-058

**Prioridade:** P0

---

## RF-COMPRAS-062 – Arquivar Processo

O sistema deverá permitir encaminhar processo concluído para arquivamento.

**Origem:**

* HU-COMPRAS-044

**Regras relacionadas:**

* RN-COMPRAS-059

**Prioridade:** P1

---

# 18. Requisitos Funcionais – Gestão Documental

## RF-COMPRAS-063 – Anexar Documento

O sistema deverá permitir anexar documentos aos processos e contratos.

**Origem:**

* HU-COMPRAS-045

**Regras relacionadas:**

* RN-COMPRAS-060

**Prioridade:** P0

---

## RF-COMPRAS-064 – Consultar Documento

O sistema deverá permitir consultar documentos conforme as permissões do usuário.

**Origem:**

* HU-COMPRAS-046

**Regras relacionadas:**

* RN-COMPRAS-061
* RN-COMPRAS-063

**Prioridade:** P0

---

## RF-COMPRAS-065 – Registrar Evidência

O sistema deverá permitir registrar evidências relacionadas aos processos e contratos.

**Origem:**

* HU-COMPRAS-047

**Regras relacionadas:**

* RN-COMPRAS-043
* RN-COMPRAS-060

**Prioridade:** P1

---

# 19. Requisitos Funcionais – Transparência

## RF-COMPRAS-066 – Consultar Contratações Públicas

O sistema deverá disponibilizar informações classificadas como públicas sobre contratações.

**Origem:**

* HU-COMPRAS-048

**Regras relacionadas:**

* RN-COMPRAS-064
* RN-COMPRAS-065

**Prioridade:** P0

---

## RF-COMPRAS-067 – Consultar Contratos Públicos

O sistema deverá disponibilizar informações públicas sobre contratos.

**Origem:**

* HU-COMPRAS-049

**Regras relacionadas:**

* RN-COMPRAS-064
* RN-COMPRAS-065

**Prioridade:** P0

---

## RF-COMPRAS-068 – Consultar Processos Publicáveis

O sistema deverá permitir consultar informações publicáveis dos processos.

**Origem:**

* HU-COMPRAS-050

**Regras relacionadas:**

* RN-COMPRAS-064
* RN-COMPRAS-066

**Prioridade:** P1

---

## RF-COMPRAS-069 – Exportar Dados Públicos

O sistema deverá permitir exportar informações classificadas como públicas, conforme os formatos disponibilizados.

**Origem:**

* HU-COMPRAS-051

**Regras relacionadas:**

* RN-COMPRAS-064
* RN-COMPRAS-067

**Prioridade:** P1

---

# 20. Requisitos Funcionais – Controle e Auditoria

## RF-COMPRAS-070 – Consultar Trilha de Auditoria

O sistema deverá permitir que usuários autorizados consultem a trilha de auditoria.

**Origem:**

* HU-COMPRAS-052

**Regras relacionadas:**

* RN-COMPRAS-068
* RN-COMPRAS-071

**Prioridade:** P0

---

## RF-COMPRAS-071 – Registrar Procedimento de Controle

O sistema deverá permitir registrar procedimentos de controle interno.

**Origem:**

* HU-COMPRAS-053

**Regras relacionadas:**

* RN-COMPRAS-068

**Prioridade:** P1

---

## RF-COMPRAS-072 – Registrar Achado

O sistema deverá permitir registrar achados de auditoria.

**Origem:**

* HU-COMPRAS-054

**Regras relacionadas:**

* RN-COMPRAS-068

**Prioridade:** P1

---

## RF-COMPRAS-073 – Acompanhar Recomendação

O sistema deverá permitir registrar e acompanhar recomendações de auditoria.

**Origem:**

* HU-COMPRAS-055

**Regras relacionadas:**

* RN-COMPRAS-068
* RN-COMPRAS-071

**Prioridade:** P1

---

# 21. Requisitos Funcionais – Indicadores e Gestão

## RF-COMPRAS-074 – Consultar Indicadores

O sistema deverá permitir consultar indicadores relacionados às compras e contratações.

**Origem:**

* HU-COMPRAS-056

**Regras relacionadas:**

* RN-COMPRAS-085
* RN-COMPRAS-086

**Prioridade:** P1

---

## RF-COMPRAS-075 – Gerar Relatório Gerencial

O sistema deverá permitir gerar relatórios gerenciais do domínio.

**Origem:**

* HU-COMPRAS-057

**Regras relacionadas:**

* RN-COMPRAS-085

**Prioridade:** P1

---

## RF-COMPRAS-076 – Consultar Painel Gerencial

O sistema deverá permitir consultar painel gerencial consolidado.

**Origem:**

* HU-COMPRAS-058

**Regras relacionadas:**

* RN-COMPRAS-085
* RN-COMPRAS-087

**Prioridade:** P1

---

# 22. Requisitos Funcionais – Alertas e Notificações

## RF-COMPRAS-077 – Gerenciar Alertas

O sistema deverá permitir gerar e acompanhar alertas relacionados a prazos, pendências e ocorrências.

**Origem:**

* HU-COMPRAS-059

**Regras relacionadas:**

* RN-COMPRAS-046
* RN-COMPRAS-088

**Prioridade:** P1

---

## RF-COMPRAS-078 – Enviar Notificação

O sistema deverá permitir enviar notificações aos usuários ou grupos responsáveis.

**Origem:**

* HU-COMPRAS-060

**Regras relacionadas:**

* RN-COMPRAS-089
* RN-COMPRAS-090

**Prioridade:** P1

---

# 23. Requisitos Funcionais – Integrações

## RF-COMPRAS-079 – Integrar com Orçamento

O sistema deverá disponibilizar e receber informações necessárias à integração com o domínio orçamentário.

**Origem:**

* HU-COMPRAS-061

**Regras relacionadas:**

* RN-COMPRAS-078
* RN-COMPRAS-112

**Prioridade:** P0

---

## RF-COMPRAS-080 – Integrar com Financeiro

O sistema deverá disponibilizar e receber informações necessárias à integração financeira.

**Origem:**

* HU-COMPRAS-062

**Regras relacionadas:**

* RN-COMPRAS-079
* RN-COMPRAS-100

**Prioridade:** P0

---

## RF-COMPRAS-081 – Integrar com Contabilidade

O sistema deverá disponibilizar informações necessárias aos registros contábeis.

**Origem:**

* HU-COMPRAS-063

**Regras relacionadas:**

* RN-COMPRAS-080

**Prioridade:** P0

---

## RF-COMPRAS-082 – Integrar com Patrimônio

O sistema deverá disponibilizar informações de bens adquiridos para o domínio de patrimônio.

**Origem:**

* HU-COMPRAS-064

**Regras relacionadas:**

* RN-COMPRAS-081

**Prioridade:** P1

---

## RF-COMPRAS-083 – Integrar com Almoxarifado

O sistema deverá disponibilizar informações necessárias ao recebimento e controle de materiais.

**Origem:**

* HU-COMPRAS-065

**Regras relacionadas:**

* RN-COMPRAS-082

**Prioridade:** P1

---

## RF-COMPRAS-084 – Integrar com Gestão Documental

O sistema deverá permitir integração com o serviço corporativo de gestão documental.

**Origem:**

* HU-COMPRAS-066

**Regras relacionadas:**

* RN-COMPRAS-083

**Prioridade:** P0

---

## RF-COMPRAS-085 – Integrar com Transparência

O sistema deverá disponibilizar informações publicáveis ao mecanismo corporativo de transparência.

**Origem:**

* HU-COMPRAS-067

**Regras relacionadas:**

* RN-COMPRAS-084

**Prioridade:** P0

---

# 24. Requisitos Funcionais – Controle de Estados

## RF-COMPRAS-086 – Controlar Estado das Entidades

O sistema deverá controlar os estados das principais entidades do domínio.

**Origem:**

* HU-COMPRAS-005
* HU-COMPRAS-007
* HU-COMPRAS-024
* HU-COMPRAS-043

**Regras relacionadas:**

* RN-COMPRAS-105
* RN-COMPRAS-106

**Prioridade:** P0

---

## RF-COMPRAS-087 – Validar Transição de Estado

O sistema deverá validar se uma transição de estado é permitida antes de executá-la.

**Origem:**

* HU-COMPRAS-007

**Regras relacionadas:**

* RN-COMPRAS-105
* RN-COMPRAS-106

**Prioridade:** P0

---

## RF-COMPRAS-088 – Registrar Histórico de Estado

O sistema deverá registrar o histórico das mudanças de estado relevantes.

**Origem:**

* HU-COMPRAS-007

**Regras relacionadas:**

* RN-COMPRAS-107

**Prioridade:** P0

---

# 25. Requisitos Funcionais – Dados e Cadastros

## RF-COMPRAS-089 – Validar Dados Obrigatórios

O sistema deverá validar o preenchimento dos dados obrigatórios antes da conclusão das operações correspondentes.

**Origem:**

* HU-COMPRAS-005
* HU-COMPRAS-013
* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-095

**Prioridade:** P0

---

## RF-COMPRAS-090 – Validar Consistência dos Dados

O sistema deverá validar a consistência dos dados registrados conforme as regras aplicáveis.

**Origem:**

* HU-COMPRAS-004
* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-096

**Prioridade:** P0

---

## RF-COMPRAS-091 – Preservar Histórico

O sistema deverá preservar o histórico das alterações relevantes.

**Origem:**

* HU-COMPRAS-021
* HU-COMPRAS-024

**Regras relacionadas:**

* RN-COMPRAS-097

**Prioridade:** P0

---

## RF-COMPRAS-092 – Utilizar Cadastro Corporativo

O sistema deverá utilizar cadastros corporativos oficiais quando estes existirem.

**Origem:**

* HU-COMPRAS-019

**Regras relacionadas:**

* RN-COMPRAS-098
* RN-COMPRAS-111
* RN-COMPRAS-112

**Prioridade:** P0

---

# 26. Requisitos Funcionais – Exceções

## RF-COMPRAS-093 – Registrar Exceção

O sistema deverá permitir registrar exceções previstas nos processos.

**Origem:**

* HU-COMPRAS-018
* HU-COMPRAS-034

**Regras relacionadas:**

* RN-COMPRAS-102
* RN-COMPRAS-103

**Prioridade:** P1

---

## RF-COMPRAS-094 – Registrar Justificativa da Exceção

O sistema deverá exigir justificativa quando a regra de negócio determinar sua obrigatoriedade.

**Origem:**

* HU-COMPRAS-018

**Regras relacionadas:**

* RN-COMPRAS-103

**Prioridade:** P1

---

## RF-COMPRAS-095 – Registrar Autoridade da Exceção

O sistema deverá registrar a autoridade responsável pela aprovação da exceção quando aplicável.

**Origem:**

* HU-COMPRAS-018

**Regras relacionadas:**

* RN-COMPRAS-104

**Prioridade:** P1

---

# 27. Requisitos Funcionais – Responsabilidades

## RF-COMPRAS-096 – Registrar Responsável pelo Processo

O sistema deverá permitir identificar o responsável pelo processo.

**Origem:**

* HU-COMPRAS-013

**Regras relacionadas:**

* RN-COMPRAS-108

**Prioridade:** P0

---

## RF-COMPRAS-097 – Registrar Responsável pelo Contrato

O sistema deverá permitir identificar o responsável pelo contrato quando aplicável.

**Origem:**

* HU-COMPRAS-024
* HU-COMPRAS-025

**Regras relacionadas:**

* RN-COMPRAS-109

**Prioridade:** P0

---

## RF-COMPRAS-098 – Registrar Responsável pelo Ato

O sistema deverá registrar o usuário responsável pela realização de atos relevantes.

**Origem:**

* HU-COMPRAS-016

**Regras relacionadas:**

* RN-COMPRAS-028
* RN-COMPRAS-110

**Prioridade:** P0

---

# 28. Requisitos Funcionais – Operação Offline

## RF-COMPRAS-099 – Registrar Atividade Offline

O sistema deverá permitir registrar atividades previamente habilitadas para operação offline.

**Origem:**

* HU-COMPRAS-029

**Regras relacionadas:**

* RN-COMPRAS-091

**Prioridade:** P1

---

## RF-COMPRAS-100 – Sincronizar Registros Offline

O sistema deverá permitir sincronizar posteriormente registros realizados sem conectividade.

**Origem:**

* HU-COMPRAS-029

**Regras relacionadas:**

* RN-COMPRAS-092
* RN-COMPRAS-093

**Prioridade:** P1

---

## RF-COMPRAS-101 – Tratar Conflitos de Sincronização

O sistema deverá permitir o tratamento de conflitos decorrentes da sincronização.

**Origem:**

* HU-COMPRAS-029

**Regras relacionadas:**

* RN-COMPRAS-094

**Prioridade:** P2

---

# 29. Requisitos Funcionais – Auditoria e Histórico

## RF-COMPRAS-102 – Registrar Operação de Auditoria

O sistema deverá registrar operações relevantes para fins de auditoria.

**Origem:**

* HU-COMPRAS-052

**Regras relacionadas:**

* RN-COMPRAS-068
* RN-COMPRAS-069

**Prioridade:** P0

---

## RF-COMPRAS-103 – Proteger Registro de Auditoria

O sistema deverá proteger os registros de auditoria contra alterações não autorizadas.

**Origem:**

* HU-COMPRAS-052

**Regras relacionadas:**

* RN-COMPRAS-070

**Prioridade:** P0

---

# 30. Requisitos Funcionais – Governança

## RF-COMPRAS-104 – Registrar Decisão de Negócio

O sistema deverá permitir registrar decisões relevantes relacionadas ao domínio quando aplicável.

**Origem:**

* HU-COMPRAS-018

**Regras relacionadas:**

* RN-COMPRAS-114

**Prioridade:** P2

---

## RF-COMPRAS-105 – Registrar Mudança de Regra

O sistema deverá permitir manter o histórico das alterações relevantes nas regras de negócio.

**Origem:**

* HU-COMPRAS-034

**Regras relacionadas:**

* RN-COMPRAS-115

**Prioridade:** P2

---

# 31. Requisitos Funcionais Transversais

Os seguintes requisitos deverão ser considerados em todas as funcionalidades do domínio, conforme aplicabilidade:

## RF-COMPRAS-106 – Controle de Acesso

O sistema deverá controlar o acesso às funcionalidades conforme as permissões do usuário.

**Regras relacionadas:**

* RN-COMPRAS-075
* RN-COMPRAS-076
* RN-COMPRAS-077

**Prioridade:** P0

---

## RF-COMPRAS-107 – Segregação de Funções

O sistema deverá aplicar as regras configuradas de segregação de funções.

**Regras relacionadas:**

* RN-COMPRAS-072
* RN-COMPRAS-073
* RN-COMPRAS-074

**Prioridade:** P0

---

## RF-COMPRAS-108 – Registro de Data e Hora

O sistema deverá registrar data e hora das operações relevantes.

**Regras relacionadas:**

* RN-COMPRAS-029
* RN-COMPRAS-069

**Prioridade:** P0

---

## RF-COMPRAS-109 – Registro do Usuário

O sistema deverá identificar o usuário responsável por operações relevantes.

**Regras relacionadas:**

* RN-COMPRAS-069
* RN-COMPRAS-110

**Prioridade:** P0

---

## RF-COMPRAS-110 – Histórico de Alterações

O sistema deverá manter histórico das alterações relevantes realizadas nos registros do domínio.

**Regras relacionadas:**

* RN-COMPRAS-004
* RN-COMPRAS-033
* RN-COMPRAS-050
* RN-COMPRAS-097

**Prioridade:** P0

---

# 32. Matriz Consolidada de Requisitos

| Faixa                | Área                       |
| -------------------- | -------------------------- |
| RF-COMPRAS-001 a 004 | Planejamento               |
| RF-COMPRAS-005 a 015 | Necessidades e Requisições |
| RF-COMPRAS-016 a 018 | Especificação              |
| RF-COMPRAS-019 a 023 | Pesquisa de Preços         |
| RF-COMPRAS-024 a 032 | Processo de Contratação    |
| RF-COMPRAS-033 a 035 | Fornecedores               |
| RF-COMPRAS-036 a 037 | Formalização               |
| RF-COMPRAS-038 a 044 | Gestão Contratual          |
| RF-COMPRAS-045 a 049 | Fiscalização               |
| RF-COMPRAS-050 a 051 | Ocorrências                |
| RF-COMPRAS-052 a 055 | Alterações Contratuais     |
| RF-COMPRAS-056 a 059 | Recebimento                |
| RF-COMPRAS-060 a 062 | Encerramento               |
| RF-COMPRAS-063 a 065 | Gestão Documental          |
| RF-COMPRAS-066 a 069 | Transparência              |
| RF-COMPRAS-070 a 073 | Auditoria                  |
| RF-COMPRAS-074 a 076 | Indicadores                |
| RF-COMPRAS-077 a 078 | Alertas e Notificações     |
| RF-COMPRAS-079 a 085 | Integrações                |
| RF-COMPRAS-086 a 088 | Estados                    |
| RF-COMPRAS-089 a 092 | Dados                      |
| RF-COMPRAS-093 a 095 | Exceções                   |
| RF-COMPRAS-096 a 098 | Responsabilidades          |
| RF-COMPRAS-099 a 101 | Operação Offline           |
| RF-COMPRAS-102 a 103 | Auditoria                  |
| RF-COMPRAS-104 a 105 | Governança                 |
| RF-COMPRAS-106 a 110 | Requisitos Transversais    |

---

# 33. Rastreabilidade

A relação entre os artefatos deverá seguir:

```text
SERV-COMPRAS
      ↓
UC-COMPRAS
      ↓
HU-COMPRAS
      ↓
RN-COMPRAS
      ↓
RF-COMPRAS
      ↓
CA-COMPRAS
      ↓
TEST-COMPRAS
```

Cada requisito funcional deverá possuir pelo menos uma origem identificável, salvo requisitos transversais devidamente justificados.

---

# 34. Requisitos Derivados

Um requisito funcional poderá ser derivado de:

* uma história de usuário;
* uma regra de negócio;
* um caso de uso;
* uma necessidade de integração;
* uma política corporativa;
* uma necessidade de auditoria;
* uma obrigação normativa.

Quando o requisito não possuir origem direta em uma história de usuário, sua origem deverá ser explicitamente registrada.

---

# 35. Requisitos Compostos

Quando um requisito possuir complexidade elevada, deverá ser decomposto em requisitos menores.

Exemplo:

```text
RF-COMPRAS-038
Registrar Contrato
       ↓
RF-COMPRAS-039
Identificar Contrato
       ↓
RF-COMPRAS-040
Registrar Vigência
       ↓
RF-COMPRAS-041
Registrar Valor
```

Essa decomposição deverá favorecer:

* entendimento;
* implementação;
* testes;
* rastreabilidade;
* estimativa.

---

# 36. Critérios para Validação dos Requisitos

Um requisito funcional deverá ser considerado adequadamente definido quando for:

* necessário;
* claro;
* não ambíguo;
* verificável;
* rastreável;
* consistente;
* implementável;
* testável;
* suficientemente atômico.

---

# 37. Requisitos Legais

Os requisitos que dependerem de legislação deverão possuir referência normativa posteriormente.

Não se deverá considerar este documento como fonte jurídica.

A validação normativa deverá ocorrer antes da implementação de qualquer comportamento cuja obrigatoriedade dependa exclusivamente de legislação específica.

---

# 38. Requisitos e Configuração

Sempre que uma regra puder variar conforme:

* Município;
* órgão;
* unidade;
* modalidade;
* tipo de contratação;
* legislação aplicável;
* política administrativa;

deverá ser avaliada a possibilidade de parametrização em vez de codificação rígida.

---

# 39. Requisitos e Integração

As integrações deverão preferencialmente utilizar serviços corporativos existentes.

O domínio não deverá criar funcionalidades duplicadas quando já existir capacidade corporativa equivalente.

---

# 40. Requisitos e Dados Corporativos

Quando uma entidade possuir cadastro mestre corporativo, o requisito deverá referenciar o cadastro oficial.

Exemplos:

* pessoas;
* fornecedores;
* unidades administrativas;
* órgãos;
* usuários;
* documentos;
* centros de custo;
* unidades orçamentárias.

---

# 41. Requisitos e Auditoria

Operações consideradas relevantes para controle deverão possuir capacidade de auditoria.

A definição final do conjunto de operações auditáveis deverá ser refinada durante a especificação.

---

# 42. Requisitos e Transparência

A disponibilização de informações públicas deverá ocorrer por meio dos mecanismos corporativos de transparência.

O domínio deverá fornecer os dados necessários, respeitando:

* classificação da informação;
* proteção de dados;
* segurança;
* integridade;
* rastreabilidade.

---

# 43. Requisitos e Operação de Campo

As funcionalidades destinadas à fiscalização e outras atividades de campo deverão ser avaliadas quanto à necessidade de:

* operação offline;
* captura de evidências;
* georreferenciamento;
* fotografias;
* documentos;
* assinatura;
* sincronização.

Esses aspectos deverão ser detalhados nos requisitos não funcionais e nas especificações correspondentes.

---

# 44. Cobertura Inicial

Este documento cobre as necessidades funcionais identificadas nas **67 histórias de usuário** do domínio.

Entretanto, a cobertura deverá ser validada formalmente na Matriz de Rastreabilidade.

O objetivo é garantir:

```text
67 Histórias
       ↓
Requisitos Funcionais
       ↓
Regras de Negócio
       ↓
Critérios de Aceitação
       ↓
Testes
```

Nenhuma história deverá permanecer sem tratamento justificado.

---

# 45. Pendências para Refinamento

Os seguintes pontos deverão ser detalhados nos próximos artefatos:

* regras legais específicas;
* campos de cada entidade;
* estados completos das entidades;
* permissões detalhadas;
* fluxos alternativos;
* exceções;
* critérios de aceitação;
* integrações;
* APIs;
* eventos;
* requisitos de segurança;
* requisitos de desempenho;
* requisitos de disponibilidade;
* requisitos de auditoria;
* requisitos de acessibilidade;
* requisitos de operação offline.

---

# 46. Próximos Artefatos

A sequência recomendada após este documento é:

```text
008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
                    ↓
009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
                    ↓
010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
                    ↓
011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
                    ↓
012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
```

---

# 47. Registro no Mapa Mestre

**Identificador do artefato:**

`RF-MAP-COMPRAS-001`

**Tipo:**

Requisitos Funcionais.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

**Status:**

Vigente.

---

# 48. Controle de Versões

| Versão | Data       | Descrição                                                                        |
| ------ | ---------- | -------------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação dos Requisitos Funcionais do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
