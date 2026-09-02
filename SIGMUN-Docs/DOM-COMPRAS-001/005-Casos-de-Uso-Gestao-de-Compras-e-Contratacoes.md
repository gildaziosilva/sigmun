# 005 – Casos de Uso – Gestão de Compras e Contratações

#### Casos de Uso – Gestão de Compras e Contratações

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

Este documento define os **Casos de Uso do Domínio de Gestão de Compras e Contratações** do SIGMUN.

Os casos de uso representam as interações relevantes entre atores e o sistema para realização dos serviços de negócio identificados no:

`004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md`

Este documento constitui uma ponte entre:

```text
Serviços de Negócio
        ↓
Casos de Uso
        ↓
Histórias de Usuário
        ↓
Requisitos Funcionais
        ↓
Regras de Negócio
        ↓
Critérios de Aceitação
        ↓
Testes
```

---

# 2. Objetivos

Os casos de uso deverão:

* representar as principais interações entre atores e SIGMUN;
* preservar a rastreabilidade dos serviços;
* identificar responsabilidades;
* definir resultados esperados;
* estabelecer uma base para requisitos funcionais;
* permitir derivação de histórias de usuário;
* apoiar a definição dos critérios de aceitação;
* apoiar planejamento de testes;
* evitar funcionalidades desconectadas dos processos de negócio.

---

# 3. Convenção de Identificação

Os casos de uso do domínio utilizarão o padrão:

```text
UC-COMPRAS-XXX
```

Exemplo:

```text
UC-COMPRAS-001
```

O identificador deverá permanecer estável durante o ciclo de vida do artefato.

---

# 4. Atores Principais

Os principais atores considerados neste documento são:

| Código          | Ator                                |
| --------------- | ----------------------------------- |
| ACT-COMPRAS-001 | Servidor / Usuário Interno          |
| ACT-COMPRAS-002 | Unidade Requisitante                |
| ACT-COMPRAS-003 | Unidade de Compras                  |
| ACT-COMPRAS-004 | Gestor                              |
| ACT-COMPRAS-005 | Autoridade Competente               |
| ACT-COMPRAS-006 | Agente Responsável pela Contratação |
| ACT-COMPRAS-007 | Equipe de Apoio                     |
| ACT-COMPRAS-008 | Fiscal de Contrato                  |
| ACT-COMPRAS-009 | Gestor de Contrato                  |
| ACT-COMPRAS-010 | Fornecedor                          |
| ACT-COMPRAS-011 | Controle Interno                    |
| ACT-COMPRAS-012 | Auditor                             |
| ACT-COMPRAS-013 | Cidadão                             |
| ACT-COMPRAS-014 | Órgão de Controle                   |
| ACT-COMPRAS-015 | Sistema Corporativo                 |

---

# 5. Organização dos Casos de Uso

Os casos de uso serão organizados por ciclo de vida:

```text
Planejamento
     ↓
Necessidade
     ↓
Requisição
     ↓
Especificação
     ↓
Pesquisa de Preços
     ↓
Processo de Contratação
     ↓
Seleção / Julgamento
     ↓
Formalização
     ↓
Execução Contratual
     ↓
Fiscalização
     ↓
Recebimento
     ↓
Alterações
     ↓
Encerramento
     ↓
Transparência
     ↓
Controle e Auditoria
```

---

# 6. Casos de Uso – Planejamento

## UC-COMPRAS-001 – Planejar Contratações

**Serviço relacionado:**

`SERV-COMPRAS-001 – Planejar Contratações`

**Atores principais:**

* Unidade de Compras;
* Gestor.

**Objetivo:**

Permitir o planejamento das contratações previstas para determinado período.

**Pré-condições:**

* usuário autenticado;
* usuário autorizado;
* período de planejamento disponível.

**Fluxo principal:**

1. Usuário acessa o planejamento.
2. Sistema apresenta as informações existentes.
3. Usuário registra uma necessidade de contratação.
4. Usuário informa os dados necessários.
5. Sistema valida as informações.
6. Sistema registra o planejamento.
7. Sistema disponibiliza a contratação para acompanhamento.

**Pós-condições:**

* planejamento registrado;
* necessidade vinculada ao planejamento.

---

## UC-COMPRAS-002 – Consolidar Necessidades

**Serviço relacionado:**

`SERV-COMPRAS-002`

**Atores:**

* Unidade de Compras;
* Gestor.

**Objetivo:**

Consolidar necessidades semelhantes ou relacionadas.

**Fluxo principal:**

1. Usuário consulta necessidades.
2. Sistema apresenta demandas disponíveis.
3. Usuário seleciona necessidades compatíveis.
4. Sistema apresenta possibilidades de consolidação.
5. Usuário confirma.
6. Sistema registra a consolidação.

---

## UC-COMPRAS-003 – Priorizar Contratações

**Serviço relacionado:**

`SERV-COMPRAS-003`

**Atores:**

* Gestor;
* Unidade de Compras.

**Objetivo:**

Definir prioridades para as contratações.

---

# 7. Casos de Uso – Necessidades e Requisições

## UC-COMPRAS-004 – Registrar Necessidade

**Serviço:**

`SERV-COMPRAS-004`

**Atores:**

* Servidor;
* Unidade Requisitante.

**Objetivo:**

Registrar uma necessidade de aquisição ou contratação.

**Fluxo principal:**

1. Usuário inicia o registro.
2. Sistema apresenta formulário.
3. Usuário informa a necessidade.
4. Usuário informa justificativa.
5. Usuário informa quantidade estimada.
6. Usuário anexa documentos quando necessário.
7. Sistema valida os dados.
8. Sistema registra a necessidade.
9. Sistema gera identificador.

---

## UC-COMPRAS-005 – Solicitar Compra ou Contratação

**Serviço:**

`SERV-COMPRAS-005`

**Atores:**

* Unidade Requisitante;
* Servidor.

**Objetivo:**

Formalizar a solicitação de compra ou contratação.

**Fluxo principal:**

1. Usuário seleciona uma necessidade.
2. Sistema apresenta os dados.
3. Usuário complementa a requisição.
4. Usuário informa itens ou serviços.
5. Usuário informa quantidades.
6. Usuário informa justificativa.
7. Sistema valida.
8. Usuário envia a requisição.
9. Sistema registra a solicitação.
10. Sistema encaminha para aprovação.

---

## UC-COMPRAS-006 – Aprovar Requisição

**Serviço:**

`SERV-COMPRAS-006`

**Atores:**

* Gestor;
* Autoridade Competente.

**Objetivo:**

Analisar e decidir sobre uma requisição.

**Fluxos possíveis:**

```text
Aprovar
Devolver
Rejeitar
```

---

## UC-COMPRAS-007 – Acompanhar Requisição

**Serviço:**

`SERV-COMPRAS-007`

**Atores:**

* Servidor;
* Gestor;
* Unidade Requisitante.

**Objetivo:**

Permitir o acompanhamento do status da requisição.

---

# 8. Casos de Uso – Especificação

## UC-COMPRAS-008 – Especificar Objeto

**Serviço:**

`SERV-COMPRAS-008`

**Atores:**

* Unidade Requisitante;
* Equipe técnica.

**Objetivo:**

Definir as características do objeto.

---

## UC-COMPRAS-009 – Validar Especificação

**Serviço:**

`SERV-COMPRAS-009`

**Atores:**

* Unidade Requisitante;
* Unidade de Compras.

**Objetivo:**

Validar a especificação antes do prosseguimento.

---

# 9. Casos de Uso – Pesquisa de Preços

## UC-COMPRAS-010 – Registrar Pesquisa de Preços

**Serviço:**

`SERV-COMPRAS-010`

**Atores:**

* Unidade de Compras.

**Objetivo:**

Registrar fontes e informações utilizadas na pesquisa.

---

## UC-COMPRAS-011 – Calcular Estimativa de Preço

**Serviço:**

`SERV-COMPRAS-011`

**Atores:**

* Unidade de Compras.

**Objetivo:**

Produzir o valor estimado da contratação.

---

## UC-COMPRAS-012 – Consultar Histórico de Preços

**Serviço:**

`SERV-COMPRAS-012`

**Atores:**

* Unidade de Compras;
* Gestor.

---

# 10. Casos de Uso – Processo de Contratação

## UC-COMPRAS-013 – Abrir Processo de Contratação

**Serviço:**

`SERV-COMPRAS-013`

**Atores:**

* Unidade de Compras.

**Objetivo:**

Criar o processo administrativo de contratação.

---

## UC-COMPRAS-014 – Instruir Processo

**Serviço:**

`SERV-COMPRAS-014`

**Atores:**

* Unidade de Compras;
* Servidor responsável.

---

## UC-COMPRAS-015 – Preparar Procedimento de Contratação

**Serviço:**

`SERV-COMPRAS-015`

**Atores:**

* Unidade de Compras;
* Agente Responsável.

---

## UC-COMPRAS-016 – Conduzir Procedimento

**Serviço:**

`SERV-COMPRAS-016`

**Atores:**

* Agente Responsável;
* Equipe de Apoio;
* Fornecedor.

---

## UC-COMPRAS-017 – Analisar e Julgar Propostas

**Serviço:**

`SERV-COMPRAS-017`

**Atores:**

* Agente Responsável;
* Equipe de Apoio.

---

## UC-COMPRAS-018 – Registrar Decisão

**Serviço:**

`SERV-COMPRAS-018`

**Atores:**

* Autoridade Competente.

---

# 11. Casos de Uso – Fornecedores

## UC-COMPRAS-019 – Cadastrar Fornecedor

**Serviço:**

`SERV-COMPRAS-019`

**Atores:**

* Unidade de Compras;
* Fornecedor.

---

## UC-COMPRAS-020 – Consultar Fornecedor

**Serviço:**

`SERV-COMPRAS-020`

**Atores:**

* Unidade de Compras;
* Gestor.

---

## UC-COMPRAS-021 – Consultar Histórico do Fornecedor

**Serviço:**

`SERV-COMPRAS-021`

**Atores:**

* Unidade de Compras;
* Gestor;
* Controle Interno.

---

# 12. Casos de Uso – Formalização

## UC-COMPRAS-022 – Formalizar Contratação

**Serviço:**

`SERV-COMPRAS-022`

**Atores:**

* Autoridade Competente;
* Fornecedor.

---

## UC-COMPRAS-023 – Gerenciar Instrumento de Contratação

**Serviço:**

`SERV-COMPRAS-023`

**Atores:**

* Unidade de Compras;
* Gestor de Contrato.

---

# 13. Casos de Uso – Gestão Contratual

## UC-COMPRAS-024 – Registrar Contrato

**Serviço:**

`SERV-COMPRAS-024`

**Atores:**

* Unidade de Compras.

---

## UC-COMPRAS-025 – Acompanhar Contrato

**Serviço:**

`SERV-COMPRAS-025`

**Atores:**

* Gestor;
* Fiscal;
* Unidade de Compras.

---

## UC-COMPRAS-026 – Gerenciar Obrigações Contratuais

**Serviço:**

`SERV-COMPRAS-026`

**Atores:**

* Gestor de Contrato;
* Fiscal.

---

## UC-COMPRAS-027 – Controlar Vigência

**Serviço:**

`SERV-COMPRAS-027`

**Atores:**

* Gestor;
* Unidade de Compras.

**Sistema deverá:**

* acompanhar datas;
* identificar proximidade do vencimento;
* gerar alertas;
* registrar alterações.

---

# 14. Casos de Uso – Fiscalização

## UC-COMPRAS-028 – Designar Fiscal

**Serviço:**

`SERV-COMPRAS-028`

**Atores:**

* Autoridade Competente;
* Gestor.

---

## UC-COMPRAS-029 – Registrar Fiscalização

**Serviço:**

`SERV-COMPRAS-029`

**Atores:**

* Fiscal.

**Possíveis evidências:**

* relatório;
* documento;
* fotografia;
* localização;
* observação;
* assinatura;
* registro de ocorrência.

---

## UC-COMPRAS-030 – Registrar Não Conformidade

**Serviço:**

`SERV-COMPRAS-030`

**Atores:**

* Fiscal;
* Gestor.

---

## UC-COMPRAS-031 – Acompanhar Correção

**Serviço:**

`SERV-COMPRAS-031`

**Atores:**

* Fiscal;
* Gestor;
* Fornecedor.

---

# 15. Casos de Uso – Ocorrências

## UC-COMPRAS-032 – Registrar Ocorrência Contratual

**Serviço:**

`SERV-COMPRAS-032`

**Atores:**

* Fiscal;
* Gestor.

---

## UC-COMPRAS-033 – Acompanhar Ocorrência

**Serviço:**

`SERV-COMPRAS-033`

**Atores:**

* Fiscal;
* Gestor.

---

# 16. Casos de Uso – Alterações Contratuais

## UC-COMPRAS-034 – Solicitar Alteração Contratual

**Serviço:**

`SERV-COMPRAS-034`

**Atores:**

* Gestor;
* Fiscal;
* Unidade de Compras.

---

## UC-COMPRAS-035 – Gerenciar Aditivo

**Serviço:**

`SERV-COMPRAS-035`

**Atores:**

* Unidade de Compras;
* Autoridade Competente;
* Fornecedor.

---

## UC-COMPRAS-036 – Gerenciar Prorrogação

**Serviço:**

`SERV-COMPRAS-036`

**Atores:**

* Gestor;
* Unidade de Compras;
* Autoridade Competente.

---

## UC-COMPRAS-037 – Gerenciar Reajuste ou Revisão

**Serviço:**

`SERV-COMPRAS-037`

**Atores:**

* Unidade de Compras;
* Gestor;
* Fornecedor.

---

# 17. Casos de Uso – Recebimento

## UC-COMPRAS-038 – Registrar Entrega

**Serviço:**

`SERV-COMPRAS-038`

**Atores:**

* Unidade Requisitante;
* Fiscal;
* Fornecedor.

---

## UC-COMPRAS-039 – Conferir Entrega

**Serviço:**

`SERV-COMPRAS-039`

**Atores:**

* Unidade Requisitante;
* Fiscal.

---

## UC-COMPRAS-040 – Registrar Aceite

**Serviço:**

`SERV-COMPRAS-040`

**Atores:**

* Fiscal;
* Unidade Requisitante.

---

## UC-COMPRAS-041 – Registrar Recusa ou Divergência

**Serviço:**

`SERV-COMPRAS-041`

**Atores:**

* Fiscal;
* Unidade Requisitante.

---

# 18. Casos de Uso – Encerramento

## UC-COMPRAS-042 – Encerrar Execução

**Serviço:**

`SERV-COMPRAS-042`

**Atores:**

* Gestor;
* Fiscal.

---

## UC-COMPRAS-043 – Encerrar Contrato

**Serviço:**

`SERV-COMPRAS-043`

**Atores:**

* Gestor;
* Autoridade Competente.

---

## UC-COMPRAS-044 – Arquivar Processo

**Serviço:**

`SERV-COMPRAS-044`

**Atores:**

* Unidade de Compras;
* Gestão Documental.

---

# 19. Casos de Uso – Gestão Documental

## UC-COMPRAS-045 – Anexar Documento

**Serviço:**

`SERV-COMPRAS-045`

**Atores:**

* Usuários autorizados.

---

## UC-COMPRAS-046 – Consultar Documentos

**Serviço:**

`SERV-COMPRAS-046`

**Atores:**

* Usuários autorizados;
* Controle Interno;
* Auditor.

---

## UC-COMPRAS-047 – Gerenciar Evidências

**Serviço:**

`SERV-COMPRAS-047`

**Atores:**

* Fiscal;
* Gestor;
* Auditor.

---

# 20. Casos de Uso – Transparência

## UC-COMPRAS-048 – Consultar Contratações

**Serviço:**

`SERV-COMPRAS-048`

**Atores:**

* Cidadão;
* Órgão de Controle.

---

## UC-COMPRAS-049 – Consultar Contratos

**Serviço:**

`SERV-COMPRAS-049`

**Atores:**

* Cidadão;
* Órgão de Controle.

---

## UC-COMPRAS-050 – Consultar Processos

**Serviço:**

`SERV-COMPRAS-050`

**Atores:**

* Cidadão;
* Órgão de Controle.

---

## UC-COMPRAS-051 – Exportar Dados Públicos

**Serviço:**

`SERV-COMPRAS-051`

**Atores:**

* Cidadão;
* Sistemas externos.

---

# 21. Casos de Uso – Controle e Auditoria

## UC-COMPRAS-052 – Consultar Trilha de Auditoria

**Serviço:**

`SERV-COMPRAS-052`

**Atores:**

* Controle Interno;
* Auditor;
* Órgão de Controle.

---

## UC-COMPRAS-053 – Executar Controle

**Serviço:**

`SERV-COMPRAS-053`

**Atores:**

* Controle Interno.

---

## UC-COMPRAS-054 – Registrar Achado de Auditoria

**Serviço:**

`SERV-COMPRAS-054`

**Atores:**

* Auditor;
* Controle Interno.

---

## UC-COMPRAS-055 – Acompanhar Recomendação

**Serviço:**

`SERV-COMPRAS-055`

**Atores:**

* Controle Interno;
* Gestor.

---

# 22. Casos de Uso – Indicadores

## UC-COMPRAS-056 – Consultar Indicadores

**Serviço:**

`SERV-COMPRAS-056`

**Atores:**

* Gestor;
* Unidade de Compras;
* Controle Interno.

---

## UC-COMPRAS-057 – Gerar Relatório Gerencial

**Serviço:**

`SERV-COMPRAS-057`

**Atores:**

* Gestor;
* Unidade de Compras.

---

## UC-COMPRAS-058 – Consultar Painel Gerencial

**Serviço:**

`SERV-COMPRAS-058`

**Atores:**

* Gestores;
* Administração Superior.

---

# 23. Casos de Uso – Alertas e Notificações

## UC-COMPRAS-059 – Gerenciar Alertas

**Serviço:**

`SERV-COMPRAS-059`

**Atores:**

* Gestor;
* Unidade de Compras.

---

## UC-COMPRAS-060 – Enviar Notificação

**Serviço:**

`SERV-COMPRAS-060`

**Atores:**

* Sistema SIGMUN;
* Usuário.

---

# 24. Casos de Uso – Integrações

## UC-COMPRAS-061 – Integrar com Orçamento

**Serviço:**

`SERV-COMPRAS-061`

**Ator:**

* Sistema Orçamentário.

---

## UC-COMPRAS-062 – Integrar com Financeiro

**Serviço:**

`SERV-COMPRAS-062`

**Ator:**

* Sistema Financeiro.

---

## UC-COMPRAS-063 – Integrar com Contabilidade

**Serviço:**

`SERV-COMPRAS-063`

**Ator:**

* Sistema Contábil.

---

## UC-COMPRAS-064 – Integrar com Patrimônio

**Serviço:**

`SERV-COMPRAS-064`

**Ator:**

* Sistema Patrimonial.

---

## UC-COMPRAS-065 – Integrar com Almoxarifado

**Serviço:**

`SERV-COMPRAS-065`

**Ator:**

* Sistema de Almoxarifado.

---

## UC-COMPRAS-066 – Integrar com Gestão Documental

**Serviço:**

`SERV-COMPRAS-066`

**Ator:**

* Sistema de Gestão Documental.

---

## UC-COMPRAS-067 – Integrar com Transparência

**Serviço:**

`SERV-COMPRAS-067`

**Atores:**

* Portal de Transparência;
* Sistemas externos.

---

# 25. Matriz de Rastreabilidade Serviço × Caso de Uso

| Serviço          | Caso de Uso    |
| ---------------- | -------------- |
| SERV-COMPRAS-001 | UC-COMPRAS-001 |
| SERV-COMPRAS-002 | UC-COMPRAS-002 |
| SERV-COMPRAS-003 | UC-COMPRAS-003 |
| SERV-COMPRAS-004 | UC-COMPRAS-004 |
| SERV-COMPRAS-005 | UC-COMPRAS-005 |
| SERV-COMPRAS-006 | UC-COMPRAS-006 |
| SERV-COMPRAS-007 | UC-COMPRAS-007 |
| SERV-COMPRAS-008 | UC-COMPRAS-008 |
| SERV-COMPRAS-009 | UC-COMPRAS-009 |
| SERV-COMPRAS-010 | UC-COMPRAS-010 |
| SERV-COMPRAS-011 | UC-COMPRAS-011 |
| SERV-COMPRAS-012 | UC-COMPRAS-012 |
| SERV-COMPRAS-013 | UC-COMPRAS-013 |
| SERV-COMPRAS-014 | UC-COMPRAS-014 |
| SERV-COMPRAS-015 | UC-COMPRAS-015 |
| SERV-COMPRAS-016 | UC-COMPRAS-016 |
| SERV-COMPRAS-017 | UC-COMPRAS-017 |
| SERV-COMPRAS-018 | UC-COMPRAS-018 |
| SERV-COMPRAS-019 | UC-COMPRAS-019 |
| SERV-COMPRAS-020 | UC-COMPRAS-020 |
| SERV-COMPRAS-021 | UC-COMPRAS-021 |
| SERV-COMPRAS-022 | UC-COMPRAS-022 |
| SERV-COMPRAS-023 | UC-COMPRAS-023 |
| SERV-COMPRAS-024 | UC-COMPRAS-024 |
| SERV-COMPRAS-025 | UC-COMPRAS-025 |
| SERV-COMPRAS-026 | UC-COMPRAS-026 |
| SERV-COMPRAS-027 | UC-COMPRAS-027 |
| SERV-COMPRAS-028 | UC-COMPRAS-028 |
| SERV-COMPRAS-029 | UC-COMPRAS-029 |
| SERV-COMPRAS-030 | UC-COMPRAS-030 |
| SERV-COMPRAS-031 | UC-COMPRAS-031 |
| SERV-COMPRAS-032 | UC-COMPRAS-032 |
| SERV-COMPRAS-033 | UC-COMPRAS-033 |
| SERV-COMPRAS-034 | UC-COMPRAS-034 |
| SERV-COMPRAS-035 | UC-COMPRAS-035 |
| SERV-COMPRAS-036 | UC-COMPRAS-036 |
| SERV-COMPRAS-037 | UC-COMPRAS-037 |
| SERV-COMPRAS-038 | UC-COMPRAS-038 |
| SERV-COMPRAS-039 | UC-COMPRAS-039 |
| SERV-COMPRAS-040 | UC-COMPRAS-040 |
| SERV-COMPRAS-041 | UC-COMPRAS-041 |
| SERV-COMPRAS-042 | UC-COMPRAS-042 |
| SERV-COMPRAS-043 | UC-COMPRAS-043 |
| SERV-COMPRAS-044 | UC-COMPRAS-044 |
| SERV-COMPRAS-045 | UC-COMPRAS-045 |
| SERV-COMPRAS-046 | UC-COMPRAS-046 |
| SERV-COMPRAS-047 | UC-COMPRAS-047 |
| SERV-COMPRAS-048 | UC-COMPRAS-048 |
| SERV-COMPRAS-049 | UC-COMPRAS-049 |
| SERV-COMPRAS-050 | UC-COMPRAS-050 |
| SERV-COMPRAS-051 | UC-COMPRAS-051 |
| SERV-COMPRAS-052 | UC-COMPRAS-052 |
| SERV-COMPRAS-053 | UC-COMPRAS-053 |
| SERV-COMPRAS-054 | UC-COMPRAS-054 |
| SERV-COMPRAS-055 | UC-COMPRAS-055 |
| SERV-COMPRAS-056 | UC-COMPRAS-056 |
| SERV-COMPRAS-057 | UC-COMPRAS-057 |
| SERV-COMPRAS-058 | UC-COMPRAS-058 |
| SERV-COMPRAS-059 | UC-COMPRAS-059 |
| SERV-COMPRAS-060 | UC-COMPRAS-060 |
| SERV-COMPRAS-061 | UC-COMPRAS-061 |
| SERV-COMPRAS-062 | UC-COMPRAS-062 |
| SERV-COMPRAS-063 | UC-COMPRAS-063 |
| SERV-COMPRAS-064 | UC-COMPRAS-064 |
| SERV-COMPRAS-065 | UC-COMPRAS-065 |
| SERV-COMPRAS-066 | UC-COMPRAS-066 |
| SERV-COMPRAS-067 | UC-COMPRAS-067 |

---

# 26. Relação com Processos

A relação principal deverá seguir:

```text
PROC-COMPRAS
      ↓
SERV-COMPRAS
      ↓
UC-COMPRAS
```

Cada caso de uso deverá estar relacionado a pelo menos um serviço.

Quando um processo envolver múltiplos serviços, poderão existir múltiplos casos de uso associados.

---

# 27. Relação com Histórias de Usuário

Cada caso de uso deverá servir como fonte para uma ou mais histórias de usuário.

Exemplo:

```text
UC-COMPRAS-005
Solicitar Compra ou Contratação
          ↓
HU-COMPRAS-001
Como servidor, quero registrar uma solicitação...
          ↓
RF-COMPRAS-001
O sistema deve permitir registrar...
```

---

# 28. Relação com Requisitos Funcionais

Os requisitos funcionais serão derivados dos casos de uso.

Exemplo:

```text
UC-COMPRAS-005
       ↓
RF-COMPRAS-001
RF-COMPRAS-002
RF-COMPRAS-003
...
```

---

# 29. Relação com Regras de Negócio

As regras de negócio deverão ser associadas aos casos de uso quando condicionarem ou restringirem seu comportamento.

Exemplo:

```text
UC-COMPRAS-006
Aprovar Requisição
       ↓
RN-COMPRAS-001
Somente usuário autorizado poderá aprovar.
```

---

# 30. Relação com Critérios de Aceitação

Cada caso de uso deverá possuir critérios de aceitação derivados de seus fluxos.

Exemplo:

```text
UC-COMPRAS-005
       ↓
CA-COMPRAS-001
A requisição deve ser registrada...
```

---

# 31. Casos de Uso Transversais

Algumas funcionalidades serão transversais ao domínio.

Exemplos:

* autenticação;
* autorização;
* auditoria;
* notificações;
* documentos;
* evidências;
* assinatura;
* integração;
* classificação da informação.

Esses recursos deverão ser preferencialmente tratados como serviços corporativos reutilizáveis.

---

# 32. Segurança

Os casos de uso deverão respeitar:

* autenticação;
* autorização;
* segregação de funções;
* menor privilégio;
* rastreabilidade;
* auditoria;
* classificação da informação;
* proteção de dados.

---

# 33. Transparência

Os casos de uso de transparência deverão respeitar a política:

> **Aberto sempre que possível, restrito sempre que necessário.**

A informação disponibilizada publicamente deverá respeitar:

* legislação;
* classificação da informação;
* proteção de dados pessoais;
* segurança;
* regras de transparência.

---

# 34. Operação Offline First

Casos de uso realizados em campo, especialmente:

* fiscalização;
* recebimento;
* inspeção;
* registro de evidências;

deverão considerar a arquitetura **Offline First** definida pelo SIGMUN.

O caso de uso deverá permitir, quando aplicável:

```text
Captura
   ↓
Armazenamento local seguro
   ↓
Validação
   ↓
Sincronização
   ↓
Processamento no servidor
   ↓
Confirmação
```

---

# 35. Critérios de Qualidade

Um caso de uso será considerado adequadamente definido quando possuir:

* identificador;
* nome;
* serviço relacionado;
* ator;
* objetivo;
* pré-condições quando aplicáveis;
* fluxo principal;
* fluxos alternativos quando necessários;
* pós-condições;
* regras de negócio relacionadas;
* requisitos derivados;
* critérios de aceitação;
* rastreabilidade.

---

# 36. Evolução dos Casos de Uso

A descrição detalhada dos fluxos deverá ocorrer progressivamente.

Este documento estabelece o **inventário e a estrutura inicial** dos casos de uso.

Os detalhes operacionais deverão ser refinados nos documentos:

* `Historias-de-Usuario.md`;
* `Requisitos-Funcionais.md`;
* `Requisitos-Nao-Funcionais.md`;
* `Regras-de-Negocio.md`;
* `Especificacoes.md`;
* `Criterrios-de-Aceitacao.md`;
* `Matriz-de-Rastreabilidade.md`.

---

# 37. Rastreabilidade Completa

A cadeia de rastreabilidade do domínio deverá seguir:

```text
Domínio
  ↓
Capacidade
  ↓
Processo
  ↓
Serviço
  ↓
Caso de Uso
  ↓
História de Usuário
  ↓
Requisito Funcional
  ↓
Regra de Negócio
  ↓
Especificação
  ↓
Critério de Aceitação
  ↓
Teste
  ↓
Implementação
```

---

# 38. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`UC-MAP-COMPRAS-001`

**Tipo:**

Mapa de Casos de Uso.

**Domínio:**

Gestão de Compras e Contratações.

**Versão:**

1.0.

---

# 39. Próximo Artefato

Após a consolidação deste documento, o próximo artefato recomendado é:

`006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md`

A partir dele serão derivadas as histórias de usuário vinculadas aos casos de uso.

A sequência recomendada será:

```text
004-Mapa-de-Servicos
        ↓
005-Casos-de-Uso
        ↓
006-Historias-de-Usuario
        ↓
007-Requisitos-Funcionais
        ↓
008-Requisitos-Nao-Funcionais
        ↓
009-Regras-de-Negocio
        ↓
010-Especificacoes
        ↓
011-Criterios-de-Aceitacao
        ↓
012-Matriz-de-Rastreabilidade
```

---

# Controle de Versões

| Versão | Data       | Descrição                                                                      |
| ------ | ---------- | ------------------------------------------------------------------------------ |
| 1.0    | 2026-08-11 | Criação do Mapa de Casos de Uso do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
