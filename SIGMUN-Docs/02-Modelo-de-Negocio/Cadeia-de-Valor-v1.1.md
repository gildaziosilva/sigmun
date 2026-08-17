# Cadeia de Valor

#### Cadeia de Valor

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Negócio

**Versão:** 1.1 – Revisada

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000E-GUIA-DE-CONTRIBUICAO.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
* 001-Termo-de-Abertura.md
* 002-Visao-do-Projeto.md
* 003-Objetivos-Estrategicos.md
* 004-Modelo-de-Governanca.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Secretarias.md
* Mapa-de-Servicos.md
* Modelo-de-Competencias.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md
* Casos-de-Uso.md
* Criterios-de-Aceitacao.md
* 04-Conhecimento-Corporativo/000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md
* 021-Governanca-de-Dados.md
* 022-Arquitetura-de-BI-Analytics-e-IA.md
* 013-Experiencia-do-Usuario.md
* 014-Processos.md
* 015-Relatorios-Indicadores-e-BI.md
* 016-Gestao-Documental.md
* 017-Gestao-de-Identidade.md
* 018-Notificacoes.md
* 019-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo.md

---

# Controle de Versões

| Versão | Data       | Descrição                                                                                                                                                                               |
| ------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0    | 2026-08-11 | Criação da Cadeia de Valor Corporativa do SIGMUN                                                                                                                                        |
| 1.1    | 2026-08-11 | Revisão estrutural, correção da classificação dos macroprocessos, ampliação da rastreabilidade e integração com casos de uso, requisitos, critérios de aceitação, dados e valor público |

---

# 1. Finalidade

Este documento estabelece a **Cadeia de Valor Corporativa do SIGMUN**, identificando como recursos, capacidades, pessoas, processos, informações, dados e tecnologia são organizados para transformar necessidades da sociedade em serviços, resultados, impactos e valor público.

A Cadeia de Valor constitui referência corporativa para:

* arquitetura de negócio;
* arquitetura de processos;
* definição de capacidades;
* definição de serviços;
* identificação de atores;
* identificação de domínios;
* definição de módulos;
* definição de requisitos;
* definição de casos de uso;
* definição de critérios de aceitação;
* arquitetura de dados;
* arquitetura de integração;
* arquitetura de aplicações;
* arquitetura de tecnologia;
* definição de indicadores;
* planejamento estratégico;
* governança;
* gestão do conhecimento;
* evolução do SIGMUN.

A Cadeia de Valor não representa apenas a estrutura do software.

Ela representa **como o Município gera valor para a sociedade e como o SIGMUN apoia essa geração de valor**.

---

# 2. Conceito de Valor no SIGMUN

O SIGMUN adota o conceito de **Valor Público** como elemento central de sua arquitetura de negócio.

O valor não é limitado à eficiência administrativa ou à digitalização de processos.

O valor público compreende, entre outros aspectos:

* melhoria dos serviços públicos;
* eficiência na utilização dos recursos;
* redução de desperdícios;
* transparência;
* melhoria da qualidade das informações;
* fortalecimento da capacidade institucional;
* participação social;
* continuidade administrativa;
* tomada de decisão baseada em evidências;
* melhoria da experiência do cidadão;
* melhoria da qualidade das políticas públicas;
* aumento da capacidade de planejamento;
* melhoria da prestação de contas;
* redução de riscos;
* melhoria da gestão territorial;
* preservação do conhecimento institucional;
* desenvolvimento da maturidade digital municipal.

O SIGMUN é, portanto, **meio para geração de valor público**, e não o objetivo final da cadeia.

---

# 3. Modelo Conceitual da Cadeia de Valor

A Cadeia de Valor do SIGMUN deve ser compreendida como uma transformação contínua:

```text
NECESSIDADES DA SOCIEDADE
          ↓
PLANEJAMENTO ESTRATÉGICO
          ↓
CAPACIDADES MUNICIPAIS
          ↓
PROCESSOS
          ↓
SERVIÇOS E ENTREGAS
          ↓
RESULTADOS
          ↓
IMPACTOS
          ↓
VALOR PÚBLICO
```

O ciclo não termina no valor público.

Os resultados devem ser avaliados para alimentar novamente o planejamento:

```text
Valor Público
      ↓
Avaliação
      ↓
Aprendizado
      ↓
Melhoria
      ↓
Novo Planejamento
      ↓
Novas Capacidades
      ↓
Novos Serviços
      ↓
Novos Resultados
```

---

# 4. Cadeia de Valor de Alto Nível

A Cadeia de Valor de Alto Nível do SIGMUN é composta por **seis grandes etapas estratégicas**, que representam o fluxo de transformação de necessidades sociais em valor público:

```text
                    NECESSIDADES DA SOCIEDADE
                              │
                              ▼
                 ┌───────────────────────────┐
                 │   PLANEJAR O MUNICÍPIO    │
                 └─────────────┬─────────────┘
                               ▼
                 ┌───────────────────────────┐
                 │    GERIR RECURSOS E       │
                 │       CAPACIDADES         │
                 └─────────────┬─────────────┘
                               ▼
                 ┌───────────────────────────┐
                 │   EXECUTAR POLÍTICAS      │
                 │        PÚBLICAS            │
                 └─────────────┬─────────────┘
                               ▼
                 ┌───────────────────────────┐
                 │    PRESTAR SERVIÇOS       │
                 │        PÚBLICOS            │
                 └─────────────┬─────────────┘
                               ▼
                 ┌───────────────────────────┐
                 │ MONITORAR, AVALIAR E      │
                 │       PRESTAR CONTAS      │
                 └─────────────┬─────────────┘
                               ▼
                 ┌───────────────────────────┐
                 │   APRENDER, INOVAR E      │
                 │        EVOLUIR             │
                 └─────────────┬─────────────┘
                               ▼
                        VALOR PÚBLICO
```

Essa visão de alto nível é complementada pelos macroprocessos corporativos definidos neste documento.

---

# 5. Estrutura da Cadeia de Valor

A Cadeia de Valor Corporativa é composta por:

1. **Processos Estratégicos**
2. **Processos de Gestão e Governança**
3. **Processos Finalísticos**
4. **Processos de Suporte**
5. **Processos Transversais**

Essa classificação não substitui os 11 macroprocessos corporativos. Ela estabelece uma **visão arquitetural complementar** para sua organização.

---

# 6. Processos Estratégicos

São responsáveis por direcionar o Município e transformar necessidades sociais e prioridades governamentais em objetivos, políticas, planos e decisões.

Incluem:

* planejamento estratégico;
* planejamento governamental;
* definição de objetivos;
* gestão de políticas públicas;
* planejamento de programas;
* planejamento de projetos;
* gestão de portfólio;
* monitoramento estratégico;
* gestão de riscos estratégicos.

---

# 7. Processos de Gestão e Governança

Garantem que a administração municipal opere de forma íntegra, transparente, controlada e alinhada aos objetivos institucionais.

Incluem:

* governança;
* gestão de riscos;
* controle interno;
* auditoria;
* compliance;
* transparência;
* prestação de contas;
* gestão de indicadores;
* gestão de desempenho;
* gestão da informação;
* governança de dados;
* gestão do conhecimento;
* gestão da mudança.

---

# 8. Processos Finalísticos

Representam as atividades diretamente relacionadas à geração de serviços e resultados para a sociedade.

Incluem, conforme a estrutura municipal:

* educação;
* saúde;
* assistência social;
* obras;
* infraestrutura;
* meio ambiente;
* desenvolvimento econômico;
* cultura;
* esporte;
* mobilidade;
* segurança e defesa civil;
* atendimento ao cidadão;
* serviços urbanos;
* desenvolvimento territorial;
* demais políticas públicas municipais.

---

# 9. Processos de Suporte

Garantem os recursos necessários à operação municipal.

Incluem:

* gestão de pessoas;
* gestão financeira;
* gestão contábil;
* gestão patrimonial;
* gestão de compras;
* gestão de contratos;
* gestão documental;
* tecnologia da informação;
* gestão de dados;
* jurídico;
* comunicação;
* logística;
* administração interna.

---

# 10. Processos Transversais

Algumas capacidades e processos atravessam praticamente toda a administração municipal.

São considerados transversais:

* governança;
* gestão de dados;
* segurança da informação;
* proteção de dados pessoais;
* gestão documental;
* gestão de identidade;
* gestão de processos;
* gestão de indicadores;
* gestão do conhecimento;
* gestão de riscos;
* auditoria;
* notificações;
* integração;
* gestão de informações;
* gestão de tecnologia.

Esses elementos não devem ser tratados como pertencentes exclusivamente a uma secretaria ou módulo.

---

# 11. Macroprocesso 01 – Planejar o Município

## Objetivo

Transformar necessidades sociais, políticas públicas, prioridades governamentais e evidências em planejamento estruturado.

## Principais atividades

* diagnóstico municipal;
* planejamento estratégico;
* planejamento governamental;
* elaboração de planos;
* definição de metas;
* definição de programas;
* planejamento orçamentário;
* definição de indicadores;
* priorização de projetos;
* gestão de portfólio.

## Resultados

* planos municipais;
* programas;
* metas;
* indicadores;
* orçamento;
* carteira de projetos;
* prioridades governamentais.

---

# 12. Macroprocesso 02 – Gerir Recursos Públicos

## Objetivo

Garantir disponibilidade, alocação, controle e utilização adequada dos recursos municipais.

## Principais atividades

* arrecadação;
* planejamento financeiro;
* orçamento;
* contabilidade;
* tesouraria;
* gestão de despesas;
* gestão de receitas;
* gestão patrimonial;
* controle fiscal.

## Resultados

* recursos disponíveis;
* equilíbrio fiscal;
* transparência financeira;
* controle dos gastos públicos;
* informações contábeis;
* capacidade de financiamento das políticas públicas.

---

# 13. Macroprocesso 03 – Adquirir e Contratar

## Objetivo

Disponibilizar bens, serviços, obras e soluções necessários ao funcionamento e à execução das políticas municipais.

## Principais atividades

* planejamento de contratação;
* compras;
* licitações;
* contratação direta;
* gestão de fornecedores;
* gestão de contratos;
* fiscalização contratual;
* avaliação de fornecedores.

## Resultados

* bens adquiridos;
* serviços contratados;
* contratos administrados;
* fornecedores avaliados;
* contratações controladas;
* recursos aplicados conforme planejamento.

---

# 14. Macroprocesso 04 – Gerir Pessoas

## Objetivo

Garantir disponibilidade, desenvolvimento, valorização e adequada gestão das pessoas que compõem a administração municipal.

## Principais atividades

* cadastro funcional;
* admissão;
* movimentação;
* folha de pagamento;
* benefícios;
* capacitação;
* avaliação;
* gestão de competências;
* planejamento da força de trabalho;
* aposentadoria;
* desligamento.

## Resultados

* servidores administrados;
* competências desenvolvidas;
* folha processada;
* força de trabalho planejada;
* conhecimento institucional preservado.

---

# 15. Macroprocesso 05 – Executar Políticas Públicas

## Objetivo

Transformar o planejamento governamental em ações concretas e resultados para a sociedade.

## Principais atividades

* execução de programas;
* execução de projetos;
* gestão de serviços;
* aplicação de recursos;
* acompanhamento de metas;
* execução de ações territoriais;
* monitoramento de políticas.

## Resultados

* políticas executadas;
* projetos entregues;
* metas alcançadas;
* serviços disponibilizados;
* recursos aplicados;
* resultados produzidos.

---

# 16. Macroprocesso 06 – Prestar Serviços Públicos

## Objetivo

Entregar serviços públicos acessíveis, eficientes, integrados e de qualidade à população.

## Principais atividades

* atendimento;
* solicitação de serviços;
* processamento;
* acompanhamento;
* comunicação com o cidadão;
* execução de serviços;
* avaliação da satisfação;
* gestão de manifestações.

## Resultados

* serviços prestados;
* solicitações atendidas;
* cidadãos atendidos;
* prazos monitorados;
* satisfação medida;
* demandas solucionadas.

---

# 17. Macroprocesso 07 – Gerir Território e Patrimônio Municipal

## Objetivo

Administrar os ativos físicos, territoriais, imobiliários e de infraestrutura do Município.

## Principais atividades

* cadastro imobiliário;
* cadastro territorial;
* gestão de imóveis;
* obras;
* infraestrutura;
* iluminação pública;
* equipamentos públicos;
* patrimônio;
* manutenção urbana;
* georreferenciamento;
* gestão territorial.

## Resultados

* território conhecido;
* patrimônio controlado;
* infraestrutura administrada;
* manutenção planejada;
* ativos municipais rastreáveis.

---

# 18. Macroprocesso 08 – Gerir Dados e Informações

## Objetivo

Garantir que os dados municipais sejam confiáveis, protegidos, acessíveis, integrados e úteis para a tomada de decisão.

## Principais atividades

* captura;
* armazenamento;
* integração;
* qualidade;
* governança;
* classificação;
* gestão de metadados;
* análise;
* compartilhamento;
* publicação;
* proteção;
* preservação.

## Resultados

* dados confiáveis;
* informações integradas;
* indicadores;
* relatórios;
* conhecimento institucional;
* inteligência municipal;
* suporte à decisão baseada em evidências.

A gestão de dados deverá ser considerada simultaneamente:

* capacidade;
* processo;
* ativo institucional;
* elemento transversal da arquitetura.

---

# 19. Macroprocesso 09 – Governar e Controlar

## Objetivo

Assegurar conformidade, transparência, controle, integridade, ética e gestão adequada dos riscos da administração municipal.

## Principais atividades

* governança;
* auditoria;
* controle interno;
* gestão de riscos;
* compliance;
* transparência;
* prestação de contas;
* controle de processos;
* integridade;
* acompanhamento de recomendações.

## Resultados

* conformidade;
* transparência;
* redução de riscos;
* melhoria dos controles;
* integridade institucional;
* prestação de contas.

---

# 20. Macroprocesso 10 – Monitorar e Avaliar Resultados

## Objetivo

Avaliar o desempenho das políticas, programas, processos, serviços e iniciativas municipais.

## Principais atividades

* coleta de indicadores;
* análise de desempenho;
* comparação de metas;
* benchmarking;
* avaliação de políticas;
* produção de relatórios;
* análise preditiva;
* monitoramento de resultados;
* avaliação de impacto.

## Resultados

* indicadores;
* painéis gerenciais;
* avaliações;
* alertas;
* recomendações;
* evidências para decisão.

---

# 21. Macroprocesso 11 – Aprender, Inovar e Evoluir

## Objetivo

Promover melhoria contínua da administração municipal e ampliar sua capacidade institucional.

## Principais atividades

* gestão do conhecimento;
* inovação;
* pesquisa;
* experimentação;
* avaliação de resultados;
* identificação de boas práticas;
* gestão da mudança;
* melhoria de processos;
* capacitação;
* compartilhamento de conhecimento.

## Resultados

* novas soluções;
* processos melhorados;
* conhecimento institucional;
* inovação;
* boas práticas;
* evolução da maturidade municipal.

---

# 22. Cadeia de Valor do Cidadão

A perspectiva do cidadão deverá ser considerada em toda a cadeia de valor.

```text
NECESSIDADE
     ↓
SOLICITAÇÃO
     ↓
ATENDIMENTO
     ↓
PROCESSAMENTO
     ↓
ENTREGA DO SERVIÇO
     ↓
AVALIAÇÃO
     ↓
FEEDBACK
     ↓
MELHORIA
```

O SIGMUN deverá permitir rastrear esse ciclo sempre que aplicável.

A jornada do cidadão deverá ser considerada independentemente da secretaria responsável pelo serviço.

---

# 23. Cadeia de Valor dos Dados

Os dados deverão seguir um ciclo de geração de valor:

```text
DADO
 ↓
CAPTURA
 ↓
VALIDAÇÃO
 ↓
INTEGRAÇÃO
 ↓
ARMAZENAMENTO
 ↓
QUALIFICAÇÃO
 ↓
ANÁLISE
 ↓
INFORMAÇÃO
 ↓
CONHECIMENTO
 ↓
INTELIGÊNCIA
 ↓
DECISÃO
 ↓
AÇÃO
 ↓
RESULTADO
```

Esse ciclo constitui uma das bases da arquitetura de dados, BI, Analytics e Inteligência do SIGMUN.

Transversalmente deverão ser considerados:

* governança;
* qualidade;
* segurança;
* privacidade;
* classificação;
* metadados;
* auditoria;
* retenção;
* descarte.

---

# 24. Cadeia de Valor da Informação

A informação deverá ser tratada como ativo institucional.

```text
DADOS
  ↓
INFORMAÇÃO
  ↓
CONHECIMENTO
  ↓
INTELIGÊNCIA
  ↓
DECISÃO
  ↓
POLÍTICA PÚBLICA
  ↓
RESULTADO SOCIAL
  ↓
VALOR PÚBLICO
```

O objetivo da arquitetura de informação não é apenas armazenar dados.

É transformar dados em conhecimento capaz de melhorar decisões e resultados públicos.

---

# 25. Capacidades Organizacionais

A Cadeia de Valor deverá ser associada ao **Mapa de Capacidades do SIGMUN**.

Exemplos:

| Capacidade             | Processos Relacionados               |
| ---------------------- | ------------------------------------ |
| Gestão Financeira      | Orçamento, Contabilidade, Tesouraria |
| Gestão de Pessoas      | RH, Folha, Competências              |
| Gestão de Contratos    | Compras, Licitações, Fiscalização    |
| Gestão de Dados        | Governança, Qualidade, Analytics     |
| Gestão Territorial     | Cadastro, Obras, Patrimônio          |
| Gestão de Serviços     | Atendimento, Solicitações            |
| Governança             | Riscos, Controle, Compliance         |
| Gestão Documental      | Protocolo, Documentos, Arquivamento  |
| Gestão de Identidade   | Usuários, Perfis, Autorização        |
| Gestão do Conhecimento | Conhecimento, Aprendizado, Melhoria  |
| Gestão de Indicadores  | Monitoramento, Avaliação, Desempenho |

A capacidade representa **o que o Município precisa ser capaz de fazer**, independentemente de qual secretaria, sistema ou tecnologia realize a atividade.

---

# 26. Relação com os Módulos do SIGMUN

Os módulos do sistema não deverão ser definidos exclusivamente pela estrutura organizacional das secretarias.

A arquitetura deverá priorizar:

* processos;
* capacidades;
* dados;
* serviços;
* integrações;
* jornadas;
* casos de uso;
* valor público.

Um módulo poderá atender diferentes secretarias quando houver processos, dados ou capacidades compartilhados.

Da mesma forma, uma secretaria poderá utilizar diversos módulos para executar seus processos.

Portanto:

```text
Secretaria ≠ Módulo
```

e:

```text
Processo → pode atravessar várias Secretarias
Capacidade → pode ser compartilhada
Serviço → pode envolver vários Módulos
Dado → pode ser utilizado por vários Processos
```

---

# 27. Relação com a Arquitetura Corporativa

A Cadeia de Valor será referência para as principais arquiteturas do SIGMUN.

## 27.1 Arquitetura de Negócio

Define:

* processos;
* capacidades;
* serviços;
* organizações;
* responsabilidades;
* atores;
* jornadas.

## 27.2 Arquitetura de Dados

Define:

* entidades;
* informações;
* domínios de dados;
* indicadores;
* metadados;
* qualidade;
* governança.

## 27.3 Arquitetura de Aplicações

Define:

* sistemas;
* módulos;
* componentes;
* serviços;
* APIs;
* integrações.

## 27.4 Arquitetura de Tecnologia

Define:

* infraestrutura;
* plataformas;
* redes;
* dispositivos;
* serviços tecnológicos.

A Cadeia de Valor constitui uma ponte entre essas arquiteturas.

---

# 28. Relação com Atores

Cada etapa relevante da Cadeia de Valor deverá possuir atores identificados.

Exemplos:

* cidadão;
* servidor;
* gestor;
* secretário;
* prefeito;
* fornecedor;
* empresa;
* órgão de controle;
* sistema externo;
* agente de campo.

A relação detalhada deverá ser mantida no `Mapa-de-Atores.md`.

---

# 29. Relação com Serviços

Os serviços municipais representam uma das principais formas de materialização do valor público.

A relação deverá seguir:

```text
Necessidade
    ↓
Capacidade
    ↓
Processo
    ↓
Serviço
    ↓
Entrega
    ↓
Resultado
    ↓
Valor Público
```

Os serviços deverão ser catalogados no `Mapa-de-Servicos.md` e relacionados aos respectivos processos e capacidades.

---

# 30. Relação com Casos de Uso

A Cadeia de Valor deverá alimentar a identificação dos casos de uso.

A relação será:

```text
Ator
  ↓
Serviço
  ↓
Processo
  ↓
Caso de Uso
  ↓
Requisito
  ↓
Implementação
```

Os casos de uso corporativos são mantidos no `Casos-de-Uso.md`.

---

# 31. Relação com Requisitos

Os requisitos deverão possuir origem rastreável na Cadeia de Valor sempre que aplicável.

Um requisito não deverá existir isoladamente quando puder ser relacionado a:

* objetivo;
* capacidade;
* processo;
* serviço;
* caso de uso;
* regra de negócio;
* necessidade do usuário.

---

# 32. Relação com Critérios de Aceitação

Os critérios de aceitação representam a forma verificável de confirmar que um requisito foi corretamente atendido.

A cadeia deverá seguir:

```text
Necessidade
    ↓
Processo
    ↓
Serviço
    ↓
Caso de Uso
    ↓
Requisito
    ↓
Critério de Aceitação
    ↓
Teste
    ↓
Evidência
    ↓
Aceite
```

Essa relação deverá ser mantida pelo Framework Corporativo de Gestão de Requisitos e Rastreabilidade.

---

# 33. Relação com Indicadores

Cada macroprocesso deverá possuir indicadores capazes de medir, conforme aplicabilidade:

* eficiência;
* eficácia;
* efetividade;
* qualidade;
* custo;
* prazo;
* satisfação;
* risco;
* produtividade;
* impacto social;
* resultado público.

Os indicadores deverão ser relacionados aos objetivos estratégicos correspondentes.

---

# 34. Rastreabilidade Corporativa

A Cadeia de Valor deverá permitir rastreabilidade bidirecional.

A visão completa deverá ser:

```text
Objetivo Estratégico
        ↓
Necessidade Pública
        ↓
Capacidade
        ↓
Macroprocesso
        ↓
Processo
        ↓
Atividade
        ↓
Serviço
        ↓
Ator
        ↓
Caso de Uso
        ↓
Regra de Negócio
        ↓
Requisito
        ↓
Critério de Aceitação
        ↓
Caso de Teste
        ↓
Sistema / Módulo
        ↓
Dado
        ↓
Indicador
        ↓
Resultado
        ↓
Impacto
        ↓
Valor Público
```

Também deverá ser possível percorrer a cadeia no sentido inverso.

Essa rastreabilidade será fundamental para:

* governança;
* arquitetura;
* gestão de requisitos;
* testes;
* auditoria;
* gestão de mudanças;
* avaliação de resultados.

---

# 35. Outputs, Resultados, Impactos e Valor Público

O SIGMUN deverá distinguir quatro níveis de geração de valor.

## 35.1 Entrega

Aquilo que foi produzido diretamente pelo processo.

Exemplos:

* documento;
* licença;
* atendimento;
* obra;
* pagamento;
* benefício.

## 35.2 Resultado

Efeito direto produzido pela entrega.

Exemplos:

* solicitação atendida;
* escola funcionando;
* tributo arrecadado;
* serviço concluído.

## 35.3 Impacto

Mudança produzida na realidade social.

Exemplos:

* redução da evasão escolar;
* redução de doenças;
* melhoria da mobilidade;
* redução de tempo de atendimento.

## 35.4 Valor Público

Valor gerado para a sociedade como consequência das ações e resultados do Município.

```text
Recursos
   ↓
Capacidades
   ↓
Processos
   ↓
Entregas
   ↓
Resultados
   ↓
Impactos
   ↓
VALOR PÚBLICO
```

---

# 36. Gestão da Cadeia de Valor

A Cadeia de Valor deverá ser revisada sempre que houver:

* mudança estratégica;
* criação de novo serviço;
* alteração relevante de processo;
* mudança legislativa;
* implantação de novo módulo;
* alteração organizacional significativa;
* identificação de nova capacidade;
* alteração relevante de política pública;
* mudança significativa no modelo de atendimento;
* mudança tecnológica com impacto no negócio.

---

# 37. Indicadores da Cadeia de Valor

O SIGMUN deverá acompanhar indicadores como:

* processos mapeados;
* processos digitalizados;
* processos integrados;
* serviços digitais;
* processos automatizados;
* redução de retrabalho;
* redução de tempo;
* redução de custos;
* satisfação dos usuários;
* qualidade dos dados;
* integração entre sistemas;
* disponibilidade dos serviços;
* resultados das políticas públicas;
* maturidade digital municipal;
* eficiência administrativa;
* efetividade das políticas públicas.

---

# 38. Princípio da Geração de Valor

Toda iniciativa relevante do SIGMUN deverá responder, sempre que aplicável:

1. Qual necessidade pública está sendo atendida?
2. Qual objetivo estratégico está relacionado?
3. Qual capacidade municipal é necessária?
4. Qual processo está envolvido?
5. Qual serviço será entregue?
6. Quem é o ator?
7. Qual caso de uso representa a interação?
8. Qual requisito deverá ser atendido?
9. Qual critério permitirá verificar o atendimento?
10. Qual dado será utilizado?
11. Qual resultado será produzido?
12. Como o resultado será medido?
13. Qual impacto poderá ser produzido?
14. Qual valor será gerado para a sociedade?

---

# 39. Princípio da Integração

O SIGMUN deverá evitar a criação de:

* processos isolados;
* cadastros duplicados;
* informações redundantes;
* integrações desnecessárias;
* funcionalidades repetidas.

Sempre que possível:

> **Capturar uma vez, utilizar muitas vezes.**

Os dados deverão ser compartilhados entre processos autorizados, respeitando:

* governança de dados;
* segurança;
* privacidade;
* classificação da informação;
* legislação aplicável;
* necessidade de acesso;
* rastreabilidade.

---

# 40. Princípio da Transversalidade

A arquitetura do SIGMUN deverá reconhecer que determinadas capacidades não pertencem exclusivamente a uma secretaria.

São exemplos:

* identidade;
* cadastro;
* dados;
* documentos;
* processos;
* notificações;
* indicadores;
* auditoria;
* segurança;
* integração;
* conhecimento.

Esses elementos deverão ser tratados como **capacidades corporativas compartilhadas**.

---

# 41. Princípio da Melhoria Contínua

A Cadeia de Valor deverá funcionar como um ciclo contínuo:

```text
PLANEJAR
   ↓
EXECUTAR
   ↓
MEDIR
   ↓
AVALIAR
   ↓
APRENDER
   ↓
MELHORAR
   ↓
PLANEJAR NOVAMENTE
```

O ciclo deverá utilizar dados, indicadores, evidências, conhecimento e feedback dos usuários.

---

# 42. Princípio da Centralidade do Cidadão

O cidadão deverá ser considerado como referência central da geração de valor público.

Isso significa que a arquitetura deverá considerar:

* necessidade;
* acesso;
* jornada;
* atendimento;
* prazo;
* qualidade;
* transparência;
* acessibilidade;
* satisfação;
* resultado;
* feedback.

O SIGMUN deverá evitar que a estrutura interna da Prefeitura determine, por si só, a experiência do cidadão.

---

# 43. Princípio da Tecnologia como Meio

A tecnologia deverá ser tratada como meio para viabilizar capacidades, processos e serviços.

A ordem de decisão deverá ser preferencialmente:

```text
Necessidade
   ↓
Valor
   ↓
Processo
   ↓
Capacidade
   ↓
Serviço
   ↓
Requisito
   ↓
Tecnologia
```

Não deverá ocorrer o inverso:

```text
Tecnologia
   ↓
Funcionalidade
   ↓
Processo
   ↓
Necessidade
```

---

# 44. Princípios Arquiteturais Relacionados

A Cadeia de Valor deverá permanecer alinhada aos princípios fundamentais do SIGMUN:

> **Transparência por padrão.**

> **Segurança por princípio.**

> **Classificação da Informação por política.**

> **Aberto sempre que possível, restrito sempre que necessário.**

> **Tecnologia como meio. Valor público como finalidade.**

---

# 45. Cadeia de Valor e Conhecimento Corporativo

A Cadeia de Valor deverá alimentar o conhecimento institucional do Município.

A relação deverá ser:

```text
Processos
   ↓
Dados
   ↓
Informação
   ↓
Conhecimento
   ↓
Boas Práticas
   ↓
Aprendizado Institucional
   ↓
Melhoria
```

O conhecimento produzido deverá ser catalogado e preservado conforme o `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`.

---

# 46. Cadeia de Valor e Maturidade Digital

A evolução da Cadeia de Valor deverá contribuir para a avaliação da maturidade digital municipal.

Poderão ser avaliados:

* processos digitalizados;
* processos integrados;
* serviços digitais;
* dados governados;
* automação;
* interoperabilidade;
* experiência do cidadão;
* uso de indicadores;
* capacidade analítica;
* governança;
* segurança;
* inovação;
* melhoria contínua.

A Cadeia de Valor deverá, portanto, constituir uma das bases conceituais para os modelos nacionais de avaliação de maturidade digital municipal.

---

# 47. Cadeia de Valor e Arquitetura de Dados

Cada etapa relevante da cadeia poderá gerar, consumir ou transformar dados.

A arquitetura deverá identificar:

* dados de entrada;
* dados produzidos;
* dados compartilhados;
* dados derivados;
* indicadores;
* metadados;
* informações públicas;
* informações restritas;
* informações pessoais.

A governança deverá garantir qualidade, segurança, disponibilidade e rastreabilidade.

---

# 48. Cadeia de Valor e Arquitetura de Integração

Processos municipais raramente operam de forma totalmente isolada.

A cadeia deverá identificar necessidades de integração entre:

* secretarias;
* órgãos;
* sistemas;
* Município e Estado;
* Município e União;
* Município e órgãos de controle;
* Município e instituições financeiras;
* Município e cidadãos;
* Município e empresas.

A integração deverá ser orientada por processos e necessidades de negócio.

---

# 49. Cadeia de Valor e Serviços de Campo

Quando o serviço municipal ocorrer fora das unidades administrativas, a cadeia deverá considerar:

* atividade de campo;
* mobilidade;
* funcionamento Offline First;
* coleta de evidências;
* geolocalização quando aplicável;
* sincronização;
* auditoria;
* integração em tempo adequado.

Isso é particularmente relevante para:

* fiscalização;
* obras;
* manutenção;
* saúde;
* assistência social;
* serviços urbanos;
* inspeções;
* atividades territoriais.

---

# 50. Governança da Cadeia de Valor

A Cadeia de Valor deverá possuir governança corporativa.

As alterações relevantes deverão ser:

* registradas;
* analisadas;
* versionadas;
* aprovadas conforme alçada;
* relacionadas aos documentos afetados;
* avaliadas quanto ao impacto arquitetural;
* comunicadas aos responsáveis.

Alterações arquiteturais relevantes deverão ser registradas por meio de ADR.

---

# 51. Responsabilidades

## Governança

Responsável por assegurar alinhamento institucional.

## Arquitetura Corporativa

Responsável pela coerência entre estratégia, negócio, processos, dados, aplicações e tecnologia.

## Áreas de Negócio

Responsáveis por validar processos, serviços e resultados.

## Gestão de Processos

Responsável pelo mapeamento e evolução dos processos.

## Gestão de Dados

Responsável pela governança e qualidade dos dados.

## Gestão de Requisitos

Responsável pela rastreabilidade entre necessidades e requisitos.

## Qualidade

Responsável pela verificação e validação das entregas.

---

# 52. Artefatos Derivados

A Cadeia de Valor deverá servir de origem ou referência para:

* Mapa de Atores;
* Mapa de Capacidades;
* Mapa de Domínios;
* Mapa de Processos;
* Mapa de Secretarias;
* Mapa de Serviços;
* Modelo de Competências;
* Modelo de Governança Administrativa;
* Glossário de Negócio;
* Casos de Uso;
* Regras de Negócio;
* Requisitos;
* Critérios de Aceitação;
* Matriz de Rastreabilidade;
* Modelo de Dados;
* Catálogo de Indicadores;
* Arquitetura de Aplicações;
* Arquitetura de Integração.

---

# 53. Matriz de Correspondência Corporativa

| Elemento               | Documento de Referência                                                 |
| ---------------------- | ----------------------------------------------------------------------- |
| Objetivos              | 003-Objetivos-Estrategicos.md                                           |
| Atores                 | Mapa-de-Atores.md                                                       |
| Capacidades            | Mapa-de-Capacidades.md                                                  |
| Domínios               | Mapa-de-Dominios.md                                                     |
| Processos              | Mapa-de-Processos.md                                                    |
| Secretarias            | Mapa-de-Secretarias.md                                                  |
| Serviços               | Mapa-de-Servicos.md                                                     |
| Competências           | Modelo-de-Competencias.md                                               |
| Governança             | Modelo-de-Governanca-Administrativa.md                                  |
| Conceitos              | Glossario-de-Negocio.md                                                 |
| Casos de Uso           | Casos-de-Uso.md                                                         |
| Critérios de Aceitação | Criterios-de-Aceitacao.md                                               |
| Requisitos             | 000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md |
| Conhecimento           | 000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md                             |
| Arquitetura            | Documentos da Arquitetura Corporativa                                   |

---

# 54. Critério para Criação de Novos Elementos

A criação de um novo macroprocesso deverá ocorrer somente quando houver justificativa arquitetural ou de negócio.

Antes de criar um novo macroprocesso, deverá ser avaliado se o novo elemento pode ser representado como:

* processo;
* subprocesso;
* capacidade;
* serviço;
* atividade;
* domínio;
* função transversal.

Isso evita a proliferação desnecessária de macroprocessos.

---

# 55. Princípio de Independência Organizacional

A Cadeia de Valor não deverá ser confundida com o organograma municipal.

O organograma representa:

> **quem está organizado onde.**

A Cadeia de Valor representa:

> **como o Município transforma recursos e capacidades em valor público.**

Portanto, mudanças na estrutura das secretarias não deverão necessariamente produzir mudanças na Cadeia de Valor.

---

# 56. Princípio de Estabilidade Arquitetural

A Cadeia de Valor deverá possuir maior estabilidade que:

* organogramas;
* estruturas de secretarias;
* sistemas;
* fornecedores;
* tecnologias;
* módulos.

Isso permitirá que a arquitetura corporativa sobreviva às mudanças administrativas e tecnológicas.

---

# 57. Princípio de Continuidade Administrativa

A Cadeia de Valor deverá contribuir para preservar a capacidade institucional do Município durante mudanças de governo, gestão ou estrutura administrativa.

Processos, capacidades, conhecimento, dados e serviços essenciais deverão possuir continuidade documentada.

---

# 58. Princípio de Evidência

As decisões de evolução da Cadeia de Valor deverão ser apoiadas, sempre que possível, por:

* dados;
* indicadores;
* estudos;
* avaliações;
* auditorias;
* evidências de usuários;
* legislação;
* análises de processos;
* resultados observados.

---

# 59. Visão Integrada da Cadeia de Valor

A visão consolidada deverá ser:

```text
                 NECESSIDADES DA SOCIEDADE
                           ↓
                    OBJETIVOS PÚBLICOS
                           ↓
                     PLANEJAMENTO
                           ↓
                     CAPACIDADES
                           ↓
                    MACROPROCESSOS
                           ↓
                       PROCESSOS
                           ↓
                        SERVIÇOS
                           ↓
                         ATORES
                           ↓
                      CASOS DE USO
                           ↓
                       REQUISITOS
                           ↓
                 CRITÉRIOS DE ACEITAÇÃO
                           ↓
                    IMPLEMENTAÇÃO
                           ↓
                         TESTES
                           ↓
                       ENTREGAS
                           ↓
                       RESULTADOS
                           ↓
                        IMPACTOS
                           ↓
                     VALOR PÚBLICO
                           ↓
                    MONITORAMENTO
                           ↓
                      APRENDIZADO
                           ↓
                     MELHORIA CONTÍNUA
                           │
                           └───────────────► NOVO CICLO
```

---

# 60. Disposições Finais

A Cadeia de Valor do SIGMUN constitui **referência corporativa para compreender como recursos, capacidades, processos, dados, tecnologia, conhecimento e pessoas são transformados em serviços, resultados, impactos e valor público**.

Este documento deverá servir como elo entre:

* estratégia;
* negócio;
* capacidades;
* processos;
* serviços;
* atores;
* casos de uso;
* requisitos;
* critérios de aceitação;
* dados;
* sistemas;
* indicadores;
* resultados;
* impactos;
* valor público.

A Cadeia de Valor não deverá ser utilizada apenas como instrumento documental.

Ela deverá ser utilizada como instrumento de **governança, arquitetura, planejamento, priorização, desenvolvimento, avaliação e melhoria contínua**.

O princípio fundamental permanece:

> **Tecnologia como meio. Valor público como finalidade.**

---

**Documento:** Cadeia-de-Valor.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
