# 013 – Modelo de Dados – Gestão de Compras e Contratações

#### Modelo de Dados – Gestão de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Gestão de Compras e Contratações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS-ADR.md
* 000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md
* 000-Dominio-Gestao-de-Compras-e-Contratacoes.md
* 001-Mapa-de-Atores-Gestao-de-Compras-e-Contratacoes.md
* 002-Mapa-de-Capacidades-Gestao-de-Compras-e-Contratacoes.md
* 003-Mapa-de-Processos-Gestao-de-Compras-e-Contratacoes.md
* 004-Mapa-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
* 005-Casos-de-Uso-Gestao-de-Compras-e-Contratacoes.md
* 006-Historias-de-Usuario-Gestao-de-Compras-e-Contratacoes.md
* 007-Regras-de-Negocio-Gestao-de-Compras-e-Contratacoes.md
* 008-Requisitos-Funcionais-Gestao-de-Compras-e-Contratacoes.md
* 009-Requisitos-Nao-Funcionais-Gestao-de-Compras-e-Contratacoes.md
* 010-Especificacoes-Gestao-de-Compras-e-Contratacoes.md
* 011-Criterios-de-Aceitacao-Gestao-de-Compras-e-Contratacoes.md
* 012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md
* 009-Arquitetura-de-Dados.md

---

# 1. Finalidade

Este documento define o **Modelo de Dados conceitual e lógico do Domínio de Gestão de Compras e Contratações do SIGMUN**.

O modelo estabelece as principais entidades, relacionamentos, atributos, identificadores, estados e regras de integridade necessários para representar o ciclo de vida das demandas de compras e contratações municipais.

O modelo deverá servir como referência para:

* arquitetura de dados;
* modelagem lógica;
* modelagem física;
* desenvolvimento de serviços;
* desenvolvimento de APIs;
* persistência de dados;
* relatórios;
* indicadores;
* auditoria;
* integração com outros domínios;
* migração de dados;
* testes;
* rastreabilidade.

---

# 2. Objetivos

São objetivos deste modelo:

1. estabelecer uma visão corporativa dos dados do domínio;
2. identificar as principais entidades de negócio;
3. estabelecer relacionamentos entre entidades;
4. definir identificadores e chaves;
5. preservar integridade referencial;
6. evitar duplicidade de informações;
7. garantir rastreabilidade do ciclo de contratação;
8. permitir auditoria dos eventos;
9. permitir integração com outros domínios;
10. preparar o domínio para implementação tecnológica.

---

# 3. Princípios de Modelagem

O modelo deverá observar os princípios corporativos do SIGMUN.

## 3.1 Fonte Única da Verdade

Cada informação deverá possuir uma fonte de autoridade claramente definida.

---

## 3.2 Não Duplicação Desnecessária

Informações corporativas existentes em outros domínios não deverão ser replicadas sem justificativa arquitetural.

Exemplos:

* pessoas;
* unidades administrativas;
* fornecedores;
* órgãos;
* usuários;
* documentos;
* contratos;
* centros de custo;
* dotações orçamentárias.

Quando apropriado, o domínio deverá utilizar referências às entidades corporativas.

---

## 3.3 Rastreabilidade

Toda contratação deverá permitir reconstruir sua trajetória:

```text
Demanda
   ↓
Planejamento
   ↓
Processo
   ↓
Contratação
   ↓
Contrato
   ↓
Execução
   ↓
Fiscalização
   ↓
Medição
   ↓
Pagamento
   ↓
Encerramento
```

---

## 3.4 Auditoria

Eventos relevantes deverão ser rastreáveis por:

* usuário;
* data e hora;
* operação;
* entidade;
* registro afetado;
* origem;
* resultado.

---

## 3.5 Histórico

Informações relevantes não deverão ser simplesmente sobrescritas quando a alteração representar uma mudança de estado ou de decisão administrativa.

Quando necessário, deverá ser mantido histórico.

---

# 4. Escopo

O modelo contempla principalmente:

* demandas;
* planejamento;
* processos de contratação;
* itens;
* fornecedores;
* procedimentos de contratação;
* propostas;
* julgamentos;
* adjudicação;
* homologação;
* contratos;
* itens contratados;
* execução;
* entregas;
* medições;
* fiscalização;
* alterações;
* ocorrências;
* encerramento.

Não fazem parte do núcleo deste modelo:

* contabilidade;
* tesouraria;
* folha;
* patrimônio;
* almoxarifado;
* orçamento.

Esses domínios poderão manter relacionamentos de integração com Gestão de Compras e Contratações.

---

# 5. Visão Conceitual

O modelo conceitual pode ser representado de forma simplificada:

```text
Unidade Administrativa
        │
        ▼
      Demanda
        │
        ▼
Planejamento da Contratação
        │
        ▼
Processo de Contratação
        │
        ├──────────────► Item da Contratação
        │                       │
        │                       ▼
        │                  Proposta
        │
        ▼
Procedimento
        │
        ▼
Resultado da Contratação
        │
        ▼
Contrato
        │
        ▼
Item do Contrato
        │
        ├──────────────► Entrega
        │
        ├──────────────► Medição
        │
        ├──────────────► Ocorrência
        │
        └──────────────► Fiscalização
        │
        ▼
Alterações
        │
        ▼
Encerramento
```

---

# 6. Entidades Principais

As principais entidades do domínio são:

| Código          | Entidade                    |
| --------------- | --------------------------- |
| ENT-COMPRAS-001 | Demanda                     |
| ENT-COMPRAS-002 | Planejamento da Contratação |
| ENT-COMPRAS-003 | Processo de Contratação     |
| ENT-COMPRAS-004 | Item da Contratação         |
| ENT-COMPRAS-005 | Procedimento de Contratação |
| ENT-COMPRAS-006 | Proposta                    |
| ENT-COMPRAS-007 | Fornecedor                  |
| ENT-COMPRAS-008 | Resultado da Contratação    |
| ENT-COMPRAS-009 | Contrato                    |
| ENT-COMPRAS-010 | Item do Contrato            |
| ENT-COMPRAS-011 | Entrega                     |
| ENT-COMPRAS-012 | Medição                     |
| ENT-COMPRAS-013 | Fiscalização                |
| ENT-COMPRAS-014 | Ocorrência                  |
| ENT-COMPRAS-015 | Alteração Contratual        |
| ENT-COMPRAS-016 | Encerramento                |

---

# 7. Entidade Demanda

**Código:** ENT-COMPRAS-001

Representa a necessidade administrativa que origina uma possível aquisição ou contratação.

## 7.1 Atributos

| Campo                   | Tipo Conceitual | Obrigatório |
| ----------------------- | --------------- | ----------- |
| id_demanda              | UUID            | Sim         |
| numero_demanda          | Identificador   | Sim         |
| unidade_requisitante_id | UUID            | Sim         |
| solicitante_id          | UUID            | Sim         |
| descricao               | Texto           | Sim         |
| justificativa           | Texto           | Sim         |
| prioridade              | Enumeração      | Sim         |
| data_solicitacao        | Data/Hora       | Sim         |
| valor_estimado          | Decimal         | Não         |
| status                  | Enumeração      | Sim         |
| criado_em               | Data/Hora       | Sim         |
| atualizado_em           | Data/Hora       | Sim         |

---

# 8. Entidade Planejamento da Contratação

**Código:** ENT-COMPRAS-002

Representa o planejamento realizado para transformar uma demanda em contratação estruturada.

## 8.1 Atributos

| Campo                  | Tipo Conceitual | Obrigatório |
| ---------------------- | --------------- | ----------- |
| id_planejamento        | UUID            | Sim         |
| demanda_id             | UUID            | Sim         |
| objeto                 | Texto           | Sim         |
| justificativa          | Texto           | Sim         |
| estimativa_valor       | Decimal         | Sim         |
| prazo_estimado         | Inteiro         | Não         |
| estrategia_contratacao | Texto           | Não         |
| status                 | Enumeração      | Sim         |
| responsavel_id         | UUID            | Sim         |
| criado_em              | Data/Hora       | Sim         |
| atualizado_em          | Data/Hora       | Sim         |

---

# 9. Entidade Processo de Contratação

**Código:** ENT-COMPRAS-003

Representa o processo administrativo que formaliza a contratação.

## 9.1 Atributos

| Campo                  | Tipo Conceitual | Obrigatório |
| ---------------------- | --------------- | ----------- |
| id_processo            | UUID            | Sim         |
| numero_processo        | Identificador   | Sim         |
| planejamento_id        | UUID            | Não         |
| unidade_responsavel_id | UUID            | Sim         |
| objeto                 | Texto           | Sim         |
| valor_estimado         | Decimal         | Sim         |
| modalidade             | Enumeração      | Sim         |
| fundamento_legal       | Texto           | Não         |
| data_abertura          | Data/Hora       | Sim         |
| status                 | Enumeração      | Sim         |
| responsavel_id         | UUID            | Sim         |
| criado_em              | Data/Hora       | Sim         |
| atualizado_em          | Data/Hora       | Sim         |

---

# 10. Entidade Item da Contratação

**Código:** ENT-COMPRAS-004

Representa cada bem, serviço ou solução que compõe uma contratação.

## 10.1 Atributos

| Campo                   | Tipo Conceitual | Obrigatório |
| ----------------------- | --------------- | ----------- |
| id_item                 | UUID            | Sim         |
| processo_id             | UUID            | Sim         |
| codigo_item             | Identificador   | Sim         |
| descricao               | Texto           | Sim         |
| unidade_medida          | Referência      | Sim         |
| quantidade              | Decimal         | Sim         |
| valor_unitario_estimado | Decimal         | Sim         |
| valor_total_estimado    | Decimal         | Sim         |
| especificacao           | Texto           | Sim         |
| status                  | Enumeração      | Sim         |

---

# 11. Entidade Procedimento de Contratação

**Código:** ENT-COMPRAS-005

Representa o procedimento utilizado para selecionar a solução ou fornecedor.

## 11.1 Atributos

| Campo             | Tipo Conceitual | Obrigatório |
| ----------------- | --------------- | ----------- |
| id_procedimento   | UUID            | Sim         |
| processo_id       | UUID            | Sim         |
| modalidade        | Enumeração      | Sim         |
| tipo_julgamento   | Enumeração      | Sim         |
| data_inicio       | Data/Hora       | Sim         |
| data_encerramento | Data/Hora       | Não         |
| status            | Enumeração      | Sim         |

---

# 12. Entidade Proposta

**Código:** ENT-COMPRAS-006

Representa uma proposta apresentada por fornecedor em determinado procedimento.

## 12.1 Atributos

| Campo             | Tipo Conceitual | Obrigatório |
| ----------------- | --------------- | ----------- |
| id_proposta       | UUID            | Sim         |
| procedimento_id   | UUID            | Sim         |
| fornecedor_id     | UUID            | Sim         |
| data_apresentacao | Data/Hora       | Sim         |
| valor_total       | Decimal         | Sim         |
| prazo_entrega     | Inteiro         | Não         |
| validade          | Data            | Não         |
| status            | Enumeração      | Sim         |

---

# 13. Entidade Fornecedor

**Código:** ENT-COMPRAS-007

Representa o fornecedor participante ou contratado.

O fornecedor deverá preferencialmente ser referenciado a partir do **Cadastro Único Municipal** ou cadastro corporativo correspondente.

## 13.1 Atributos de Referência

| Campo                        | Tipo Conceitual | Obrigatório |
| ---------------------------- | --------------- | ----------- |
| fornecedor_id                | UUID            | Sim         |
| identificacao_corporativa_id | UUID            | Sim         |
| situacao                     | Enumeração      | Sim         |

O domínio não deverá duplicar desnecessariamente os dados cadastrais do fornecedor.

---

# 14. Entidade Resultado da Contratação

**Código:** ENT-COMPRAS-008

Representa o resultado formal do procedimento de contratação.

## 14.1 Atributos

| Campo            | Tipo Conceitual | Obrigatório |
| ---------------- | --------------- | ----------- |
| id_resultado     | UUID            | Sim         |
| procedimento_id  | UUID            | Sim         |
| fornecedor_id    | UUID            | Sim         |
| valor_homologado | Decimal         | Sim         |
| data_resultado   | Data/Hora       | Sim         |
| resultado        | Enumeração      | Sim         |
| observacao       | Texto           | Não         |

---

# 15. Entidade Contrato

**Código:** ENT-COMPRAS-009

Representa o instrumento formal de contratação.

## 15.1 Atributos

| Campo               | Tipo Conceitual | Obrigatório |
| ------------------- | --------------- | ----------- |
| id_contrato         | UUID            | Sim         |
| numero_contrato     | Identificador   | Sim         |
| processo_id         | UUID            | Sim         |
| fornecedor_id       | UUID            | Sim         |
| objeto              | Texto           | Sim         |
| valor_inicial       | Decimal         | Sim         |
| data_assinatura     | Data            | Sim         |
| inicio_vigencia     | Data            | Sim         |
| fim_vigencia        | Data            | Sim         |
| status              | Enumeração      | Sim         |
| instrumento_id      | UUID            | Não         |
| gestor_contrato_id  | UUID            | Sim         |
| fiscal_principal_id | UUID            | Sim         |
| criado_em           | Data/Hora       | Sim         |
| atualizado_em       | Data/Hora       | Sim         |

---

# 16. Entidade Item do Contrato

**Código:** ENT-COMPRAS-010

Representa os itens efetivamente contratados.

## 16.1 Atributos

| Campo                 | Tipo Conceitual | Obrigatório |
| --------------------- | --------------- | ----------- |
| id_item_contrato      | UUID            | Sim         |
| contrato_id           | UUID            | Sim         |
| item_contratacao_id   | UUID            | Sim         |
| quantidade_contratada | Decimal         | Sim         |
| valor_unitario        | Decimal         | Sim         |
| valor_total           | Decimal         | Sim         |
| saldo_quantidade      | Decimal         | Sim         |
| saldo_valor           | Decimal         | Sim         |
| status                | Enumeração      | Sim         |

---

# 17. Entidade Entrega

**Código:** ENT-COMPRAS-011

Representa a entrega de bens ou execução de serviços associada ao contrato.

## 17.1 Atributos

| Campo                      | Tipo Conceitual | Obrigatório |
| -------------------------- | --------------- | ----------- |
| id_entrega                 | UUID            | Sim         |
| item_contrato_id           | UUID            | Sim         |
| data_entrega               | Data/Hora       | Sim         |
| quantidade                 | Decimal         | Sim         |
| valor                      | Decimal         | Sim         |
| local_entrega              | Texto           | Não         |
| responsavel_recebimento_id | UUID            | Sim         |
| status                     | Enumeração      | Sim         |
| observacao                 | Texto           | Não         |

---

# 18. Entidade Medição

**Código:** ENT-COMPRAS-012

Representa o registro formal de medição da execução contratual.

## 18.1 Atributos

| Campo                 | Tipo Conceitual | Obrigatório |
| --------------------- | --------------- | ----------- |
| id_medicao            | UUID            | Sim         |
| contrato_id           | UUID            | Sim         |
| periodo_inicio        | Data            | Sim         |
| periodo_fim           | Data            | Sim         |
| valor_medido          | Decimal         | Sim         |
| percentual_execucao   | Decimal         | Não         |
| fiscal_responsavel_id | UUID            | Sim         |
| data_medicao          | Data            | Sim         |
| status                | Enumeração      | Sim         |
| observacao            | Texto           | Não         |

---

# 19. Entidade Fiscalização

**Código:** ENT-COMPRAS-013

Representa as atividades de acompanhamento e fiscalização do contrato.

## 19.1 Atributos

| Campo           | Tipo Conceitual | Obrigatório |
| --------------- | --------------- | ----------- |
| id_fiscalizacao | UUID            | Sim         |
| contrato_id     | UUID            | Sim         |
| fiscal_id       | UUID            | Sim         |
| tipo            | Enumeração      | Sim         |
| data            | Data/Hora       | Sim         |
| descricao       | Texto           | Sim         |
| resultado       | Enumeração      | Sim         |
| observacao      | Texto           | Não         |

---

# 20. Entidade Ocorrência

**Código:** ENT-COMPRAS-014

Representa fatos relevantes ocorridos durante o ciclo de contratação ou execução contratual.

## 20.1 Atributos

| Campo           | Tipo Conceitual | Obrigatório |
| --------------- | --------------- | ----------- |
| id_ocorrencia   | UUID            | Sim         |
| contrato_id     | UUID            | Não         |
| processo_id     | UUID            | Não         |
| tipo            | Enumeração      | Sim         |
| descricao       | Texto           | Sim         |
| data_ocorrencia | Data/Hora       | Sim         |
| gravidade       | Enumeração      | Sim         |
| responsavel_id  | UUID            | Sim         |
| status          | Enumeração      | Sim         |

---

# 21. Entidade Alteração Contratual

**Código:** ENT-COMPRAS-015

Representa alterações realizadas em contrato.

Podem incluir:

* aditivos;
* supressões;
* acréscimos;
* prorrogações;
* reajustes;
* repactuações;
* revisões;
* alterações de responsáveis.

## 21.1 Atributos

| Campo              | Tipo Conceitual | Obrigatório |
| ------------------ | --------------- | ----------- |
| id_alteracao       | UUID            | Sim         |
| contrato_id        | UUID            | Sim         |
| tipo               | Enumeração      | Sim         |
| numero_instrumento | Identificador   | Não         |
| justificativa      | Texto           | Sim         |
| valor_anterior     | Decimal         | Não         |
| valor_novo         | Decimal         | Não         |
| vigencia_anterior  | Data            | Não         |
| vigencia_nova      | Data            | Não         |
| data_assinatura    | Data            | Sim         |
| status             | Enumeração      | Sim         |

---

# 22. Entidade Encerramento

**Código:** ENT-COMPRAS-016

Representa o encerramento formal do contrato ou processo.

## 22.1 Atributos

| Campo             | Tipo Conceitual | Obrigatório |
| ----------------- | --------------- | ----------- |
| id_encerramento   | UUID            | Sim         |
| contrato_id       | UUID            | Sim         |
| data_encerramento | Data            | Sim         |
| motivo            | Enumeração      | Sim         |
| resultado         | Enumeração      | Sim         |
| saldo_final       | Decimal         | Não         |
| responsavel_id    | UUID            | Sim         |
| observacao        | Texto           | Não         |

---

# 23. Relacionamentos Principais

| Origem           | Cardinalidade | Destino              |
| ---------------- | ------------- | -------------------- |
| Demanda          | 1:N           | Planejamento         |
| Planejamento     | 1:N           | Processo             |
| Processo         | 1:N           | Item da Contratação  |
| Processo         | 1:N           | Procedimento         |
| Procedimento     | 1:N           | Proposta             |
| Fornecedor       | 1:N           | Proposta             |
| Procedimento     | 1:N           | Resultado            |
| Processo         | 1:N           | Contrato             |
| Contrato         | 1:N           | Item do Contrato     |
| Item do Contrato | 1:N           | Entrega              |
| Contrato         | 1:N           | Medição              |
| Contrato         | 1:N           | Fiscalização         |
| Contrato         | 1:N           | Ocorrência           |
| Contrato         | 1:N           | Alteração Contratual |
| Contrato         | 1:1           | Encerramento         |

---

# 24. Relacionamentos com Dados Corporativos

O domínio deverá integrar-se preferencialmente às seguintes entidades corporativas:

| Dado                   | Fonte de Autoridade              |
| ---------------------- | -------------------------------- |
| Pessoa                 | Cadastro Único Municipal         |
| Unidade Administrativa | Estrutura Organizacional         |
| Usuário                | Gestão de Identidade             |
| Fornecedor             | Cadastro Corporativo             |
| Documento              | Gestão Documental                |
| Dotação                | Orçamento/Finanças               |
| Empenho                | Execução Orçamentária            |
| Pagamento              | Tesouraria                       |
| Material               | Almoxarifado/Patrimônio          |
| Bem                    | Patrimônio                       |
| Município              | Cadastro Territorial/Corporativo |

---

# 25. Identificadores

Os identificadores internos deverão preferencialmente utilizar UUID.

Exemplo:

```text
id_contrato = UUID
```

Os identificadores administrativos deverão ser armazenados separadamente quando possuírem significado operacional.

Exemplo:

```text
id_contrato
numero_contrato
```

Isso evita utilizar o número administrativo como chave primária.

---

# 26. Auditoria

As entidades críticas deverão possuir metadados de auditoria.

Estrutura conceitual:

| Campo          | Finalidade                        |
| -------------- | --------------------------------- |
| criado_em      | Data de criação                   |
| criado_por     | Usuário responsável               |
| atualizado_em  | Última atualização                |
| atualizado_por | Usuário responsável               |
| excluido_em    | Exclusão lógica, quando aplicável |
| excluido_por   | Responsável pela exclusão         |
| versao         | Controle de versão                |

---

# 27. Integridade Referencial

O modelo deverá impedir:

* contrato sem processo válido;
* item de contrato sem contrato;
* proposta sem fornecedor;
* medição sem contrato;
* entrega sem item contratado;
* alteração sem contrato;
* encerramento sem contrato.

---

# 28. Integridade Financeira

Valores financeiros deverão observar:

* precisão decimal adequada;
* moeda oficial;
* separação entre valor unitário e total;
* controle de arredondamento;
* histórico de alterações;
* consistência entre quantidade e valor.

Exemplo:

```text
valor_total = quantidade × valor_unitario
```

O sistema deverá impedir inconsistências decorrentes de alteração isolada dos valores calculados.

---

# 29. Controle de Saldos

O contrato deverá permitir controlar:

```text
Quantidade Contratada
        ↓
Quantidade Executada
        ↓
Quantidade Disponível
```

e:

```text
Valor Contratado
        ↓
Valor Executado
        ↓
Saldo Contratual
```

Os saldos deverão ser derivados ou controlados de forma transacional, evitando inconsistências.

---

# 30. Estados

As entidades que possuem ciclo de vida deverão utilizar estados controlados.

Exemplo para Processo:

```text
RASCUNHO
EM_INSTRUCAO
EM_ANALISE
EM_PROCEDIMENTO
EM_JULGAMENTO
HOMOLOGADO
CONTRATADO
ENCERRADO
CANCELADO
ARQUIVADO
```

Exemplo para Contrato:

```text
EM_ELABORACAO
ASSINADO
VIGENTE
SUSPENSO
ENCERRADO
RESCINDIDO
EXTINTO
```

Os estados definitivos deverão ser refinados durante a especificação técnica.

---

# 31. Histórico de Estados

Alterações de estado relevantes deverão gerar histórico.

Estrutura conceitual:

```text
HistoricoEstado
-------------------------
id
entidade
entidade_id
estado_anterior
estado_novo
data_hora
usuario_id
motivo
```

---

# 32. Documentos

Documentos não deverão ser armazenados diretamente nas entidades de negócio quando existir o domínio corporativo de Gestão Documental.

O modelo deverá manter referências:

```text
documento_id
```

Exemplos:

* termo de referência;
* estudo técnico;
* edital;
* proposta;
* contrato;
* aditivo;
* relatório de fiscalização;
* comprovante de entrega;
* termo de encerramento.

---

# 33. Eventos

O domínio deverá estar preparado para arquitetura orientada a eventos.

Exemplos:

```text
DemandaCriada
DemandaAprovada
ProcessoAberto
ProcessoEncaminhado
ProcedimentoIniciado
PropostaRecebida
ResultadoHomologado
ContratoAssinado
ContratoIniciado
EntregaRegistrada
MedicaoRegistrada
OcorrenciaRegistrada
ContratoAlterado
ContratoEncerrado
```

Os eventos deverão ser detalhados no Modelo de Integração.

---

# 34. Dados Sensíveis

Embora a maior parte dos dados do domínio seja de natureza administrativa e pública, poderão existir informações que exijam proteção.

Exemplos:

* dados pessoais de usuários;
* dados de representantes;
* informações pessoais de fornecedores;
* dados de autenticação;
* documentos com informações protegidas;
* informações classificadas.

O modelo deverá respeitar as políticas de segurança e LGPD do SIGMUN.

---

# 35. Dados Públicos

O modelo deverá permitir a identificação de dados potencialmente publicáveis.

Exemplos:

* número do processo;
* objeto;
* modalidade;
* fornecedor;
* valor contratado;
* vigência;
* situação;
* resultados;
* contratos;
* aditivos;
* execução contratual.

A publicação deverá respeitar a **Política de Classificação da Informação e Publicação de Artefatos**.

---

# 36. Normalização

O modelo lógico deverá buscar normalização adequada, evitando:

* redundância;
* dependências indevidas;
* atributos multivalorados;
* duplicidade de entidades;
* inconsistências de atualização.

Desnormalizações poderão ser adotadas somente quando houver justificativa arquitetural, especialmente para:

* relatórios;
* analytics;
* indicadores;
* desempenho;
* integração;
* leitura em larga escala.

---

# 37. Modelo de Dados e Analytics

O modelo transacional deverá servir como fonte para o ecossistema analítico do SIGMUN.

Indicadores possíveis:

* quantidade de contratações;
* valor contratado;
* valor executado;
* economia obtida;
* prazo médio;
* quantidade de processos;
* contratos ativos;
* contratos próximos do vencimento;
* concentração de fornecedores;
* índice de execução;
* índice de atrasos;
* ocorrências contratuais.

A modelagem analítica deverá ser definida separadamente no domínio de BI, Analytics e IA.

---

# 38. Segurança dos Dados

O modelo deverá suportar:

* controle de acesso;
* segregação de funções;
* trilha de auditoria;
* classificação da informação;
* proteção de dados pessoais;
* histórico de alterações;
* controle de integridade;
* rastreabilidade.

---

# 39. Segregação de Responsabilidades

O modelo deverá permitir distinguir, quando aplicável:

```text
Solicitante
     ≠
Responsável pelo Planejamento
     ≠
Responsável pelo Procedimento
     ≠
Ordenador
     ≠
Gestor do Contrato
     ≠
Fiscal do Contrato
```

Essa separação é fundamental para controles internos.

---

# 40. Requisitos para Modelo Físico

O futuro modelo físico deverá definir:

* tabelas;
* colunas;
* tipos de dados;
* chaves primárias;
* chaves estrangeiras;
* índices;
* constraints;
* sequences, quando aplicável;
* triggers, quando justificadas;
* particionamento, quando necessário;
* estratégias de retenção;
* políticas de backup.

Essas definições não fazem parte do modelo conceitual deste documento.

---

# 41. Estratégia de Persistência

A tecnologia de persistência deverá ser definida na arquitetura de software e dados do SIGMUN.

Este documento não deverá criar dependência prematura de:

* PostgreSQL;
* MySQL;
* MariaDB;
* SQL Server;
* Oracle;
* MongoDB;
* outra tecnologia.

A escolha deverá observar os padrões corporativos de arquitetura.

---

# 42. Integrações Previstas

O domínio deverá possuir integração potencial com:

* Cadastro Único Municipal;
* Gestão Orçamentária;
* Gestão Financeira;
* Gestão Documental;
* Gestão de Identidade;
* Gestão Patrimonial;
* Almoxarifado;
* Portal da Transparência;
* BI e Analytics;
* Notificações;
* assinatura eletrônica;
* sistemas externos de governo;
* sistemas nacionais relacionados a contratações públicas.

---

# 43. Regras de Integridade Essenciais

O modelo deverá garantir, no mínimo:

1. um contrato deve estar vinculado a um processo;
2. um item contratado deve pertencer a um contrato;
3. uma entrega deve estar vinculada a um item contratado;
4. uma medição deve estar vinculada a um contrato;
5. uma fiscalização deve estar vinculada a um contrato;
6. uma alteração deve estar vinculada a um contrato;
7. um encerramento deve estar vinculado a um contrato;
8. uma proposta deve estar vinculada a um fornecedor;
9. valores não poderão ser negativos quando a regra de negócio não permitir;
10. datas deverão respeitar a sequência lógica do ciclo de vida.

---

# 44. Rastreabilidade

Este modelo deverá estar relacionado aos seguintes artefatos:

```text
CAP
 ↓
PROC
 ↓
SERV
 ↓
UC
 ↓
HU
 ↓
RN
 ↓
RF
 ↓
ESP
 ↓
MODELO DE DADOS
 ↓
CA
 ↓
TESTES
```

Cada entidade relevante deverá possuir rastreabilidade até os requisitos que justificam sua existência.

---

# 45. Evolução do Modelo

Alterações no modelo deverão considerar:

* impacto sobre processos;
* impacto sobre requisitos;
* impacto sobre integrações;
* impacto sobre APIs;
* impacto sobre relatórios;
* impacto sobre indicadores;
* impacto sobre migrações;
* impacto sobre dados existentes;
* impacto sobre segurança;
* impacto sobre auditoria.

Alterações estruturais significativas deverão ser registradas por ADR.

---

# 46. Migração

Quando o SIGMUN incorporar dados provenientes de sistemas legados, deverá existir:

* mapeamento origem-destino;
* dicionário de dados;
* regras de transformação;
* tratamento de duplicidades;
* validação de integridade;
* reconciliação;
* auditoria da migração;
* plano de rollback quando aplicável.

---

# 47. Qualidade dos Dados

O domínio deverá monitorar:

| Dimensão        | Objetivo                           |
| --------------- | ---------------------------------- |
| Completude      | Dados obrigatórios preenchidos     |
| Consistência    | Dados coerentes entre entidades    |
| Unicidade       | Ausência de duplicidade indevida   |
| Atualidade      | Dados atualizados                  |
| Integridade     | Relacionamentos válidos            |
| Rastreabilidade | Origem e alterações identificáveis |

---

# 48. Dicionário de Dados

O modelo lógico deverá posteriormente gerar um dicionário detalhado contendo:

```text
Entidade
Campo
Descrição
Tipo
Tamanho
Obrigatório
Domínio de valores
Chave
Relacionamento
Regra de validação
Classificação
Fonte de autoridade
Observações
```

O dicionário deverá ser mantido como artefato próprio quando o modelo atingir nível suficiente de detalhamento.

---

# 49. Modelo Futuro de Dados Físicos

A evolução esperada é:

```text
Modelo Conceitual
        ↓
Modelo Lógico
        ↓
Dicionário de Dados
        ↓
Modelo Físico
        ↓
DDL
        ↓
Migração
        ↓
Testes
```

Este documento representa principalmente a primeira e segunda etapas.

---

# 50. Critérios de Aceitação do Modelo

O modelo será considerado adequado quando:

* as principais entidades do domínio estiverem identificadas;
* os relacionamentos principais estiverem definidos;
* as entidades corporativas externas estiverem identificadas;
* não houver duplicação conceitual indevida;
* as regras de integridade essenciais estiverem representadas;
* o ciclo de vida da contratação estiver representado;
* os requisitos funcionais relevantes possuírem correspondência no modelo;
* os dados críticos forem auditáveis;
* o modelo permitir futura implementação física;
* o modelo estiver alinhado à arquitetura corporativa do SIGMUN.

---

# 51. Próximos Artefatos

Após este documento, recomenda-se seguir com:

```text
014-Modelo-de-Integracao-Gestao-de-Compras-e-Contratacoes.md
015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md
016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md
017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md
018-Plano-de-Testes-Gestao-de-Compras-e-Contratacoes.md
019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md
020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md
```

---

# 52. Controle de Versões

| Versão | Data       | Descrição                                                                 |
| ------ | ---------- | ------------------------------------------------------------------------- |
| 1.0    | 2026-08-12 | Criação do Modelo de Dados do Domínio de Gestão de Compras e Contratações |

---

**Documento:** 013-Modelo-de-Dados-Gestao-de-Compras-e-Contratacoes.md

**Última atualização:** 2026-08-12

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

