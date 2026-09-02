# 000C – Hierarquia Documental do SIGMUN

#### Hierarquia Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Governança Corporativa

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000E-GUIA-DE-CONTRIBUICAO.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
* 001-Termo-de-Abertura.md
* 002-Visao-do-Projeto.md
* 003-Objetivos-Estrategicos.md
* 004-Modelo-de-Governanca.md
* Cadeia-de-Valor-v1.1.md
* Mapa-de-Atores-v1.0.md
* Mapa-de-Capacidades-v1.0.md
* Mapa-de-Dominios-v1.0.md
* Mapa-de-Processos-v1.0.md
* Mapa-de-Secretarias-v1.0.md
* Mapa-de-Servicos-v1.0.md
* Casos-de-Uso-v1.0.md
* Criterios-de-Aceitacao-v1.0.md
* 04-Conhecimento-Corporativo/000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md

---

# 1. Finalidade

Este documento estabelece a **Hierarquia Documental Corporativa do SIGMUN**, definindo como os documentos, artefatos, modelos, registros e demais elementos documentais do projeto devem ser classificados, identificados, relacionados, versionados, aprovados, publicados, substituídos, arquivados e descartados.

A Hierarquia Documental tem como objetivos:

* estabelecer uma organização documental coerente;
* evitar duplicidade de documentos;
* estabelecer autoridade entre documentos;
* garantir rastreabilidade;
* facilitar localização e compreensão dos artefatos;
* estabelecer regras de versionamento;
* preservar o histórico das decisões;
* garantir continuidade institucional;
* facilitar auditorias;
* apoiar governança;
* facilitar onboarding de colaboradores;
* preservar o conhecimento corporativo;
* garantir coerência entre arquitetura, negócio, requisitos e implementação.

---

# 2. Princípios Documentais

A gestão documental do SIGMUN deverá observar os seguintes princípios.

## 2.1. Documento Único por Finalidade

Cada documento deverá possuir uma finalidade claramente definida.

Não deverão existir documentos diferentes com o mesmo propósito sem justificativa formal.

---

## 2.2. Fonte Oficial

Para cada informação corporativa deverá existir uma **fonte oficial de referência**.

Outros documentos poderão referenciar essa informação, mas não deverão reproduzi-la de forma divergente.

---

## 2.3. Rastreabilidade

Todo documento relevante deverá permitir identificar:

* origem;
* responsável;
* versão;
* data;
* status;
* documentos relacionados;
* decisões relacionadas;
* artefatos derivados.

---

## 2.4. Versionamento

Alterações relevantes deverão gerar nova versão do documento.

As versões anteriores não deverão ser apagadas quando houver necessidade de preservação histórica, regulatória, arquitetural ou de auditoria.

---

## 2.5. Clareza

O nome do documento deverá indicar claramente seu conteúdo.

---

## 2.6. Estabilidade

Documentos corporativos deverão possuir identificadores estáveis sempre que possível.

Alterações de conteúdo não deverão provocar alteração arbitrária da identidade lógica do documento.

---

## 2.7. Separação entre Documento e Versão

O conceito lógico do documento é diferente de uma versão específica.

Exemplo:

```text
Documento lógico:
Cadeia de Valor

Versão:
1.1
```

No sistema de arquivos, entretanto, como diferentes versões precisam coexistir, o nome físico deverá incorporar a versão.

---

# 3. Modelo de Hierarquia

A documentação do SIGMUN será organizada segundo os seguintes níveis:

```text
NÍVEL 0
Constituição e Fundamentos
        ↓
NÍVEL 1
Governança Corporativa
        ↓
NÍVEL 2
Arquitetura Corporativa
        ↓
NÍVEL 3
Modelo de Negócio
        ↓
NÍVEL 4
Requisitos e Especificações
        ↓
NÍVEL 5
Arquitetura de Dados
        ↓
NÍVEL 6
Arquitetura de Aplicações e Módulos
        ↓
NÍVEL 7
Integrações e APIs
        ↓
NÍVEL 8
Segurança, LGPD e Conformidade
        ↓
NÍVEL 9
Desenvolvimento
        ↓
NÍVEL 10
Testes e Qualidade
        ↓
NÍVEL 11
Implantação e Operação
        ↓
NÍVEL 12
Conhecimento, Indicadores e Evolução
```

Essa hierarquia representa dependência e precedência arquitetural, e não necessariamente uma relação rígida de subordinação.

---

# 4. Nível 0 – Constituição e Fundamentos

Representa a base institucional e normativa do SIGMUN.

Inclui:

* constituição do projeto;
* visão;
* princípios;
* objetivos;
* fundamentos;
* documentos fundacionais;
* padrões corporativos.

Exemplos:

```text
000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
000C-HIERARQUIA-DOCUMENTAL-v1.0.md
000D-MODELO-DE-DOCUMENTO.md
000E-GUIA-DE-CONTRIBUICAO.md
000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
```

---

# 5. Nível 1 – Governança Corporativa

Estabelece como o projeto é governado.

Inclui:

* governança;
* políticas;
* gestão de riscos;
* compliance;
* auditoria;
* gestão de mudanças;
* gestão de partes interessadas;
* gestão de continuidade;
* gestão de crises;
* gestão da informação;
* governança de dados.

Exemplos:

```text
001-Termo-de-Abertura.md
002-Visao-do-Projeto.md
003-Objetivos-Estrategicos.md
004-Modelo-de-Governanca.md
005-Governanca-Corporativa.md
006-Governanca-da-Arquitetura.md
007-Gestao-do-Portfolio.md
008-Gestao-de-Riscos.md
009-Etica-Integridade-e-Compliance.md
010-Plano-de-Comunicacao.md
```

---

# 6. Nível 2 – Arquitetura Corporativa

Define a estrutura integrada da organização, negócio, informação, aplicações e tecnologia.

Inclui:

* arquitetura de negócio;
* arquitetura de dados;
* arquitetura de software;
* arquitetura de integração;
* arquitetura de segurança;
* arquitetura de implantação;
* experiência do usuário;
* arquitetura tecnológica;
* arquitetura de dispositivos móveis;
* serviços de campo.

---

# 7. Nível 3 – Modelo de Negócio

Representa como o Município funciona e gera valor público.

Inclui:

* Cadeia de Valor;
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
* Critérios de Aceitação.

Exemplo:

```text
Cadeia-de-Valor-v1.1.md
```

---

# 8. Nível 4 – Requisitos e Especificações

Define o que o SIGMUN deverá realizar.

Inclui:

* requisitos de negócio;
* requisitos funcionais;
* requisitos não funcionais;
* regras de negócio;
* casos de uso;
* histórias de usuário;
* critérios de aceitação;
* especificações;
* matriz de rastreabilidade.

A gestão deverá observar o:

```text
000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
```

---

# 9. Nível 5 – Arquitetura de Dados

Define como os dados serão estruturados, governados, protegidos e utilizados.

Inclui:

* modelo conceitual;
* modelo lógico;
* modelo físico;
* dicionário de dados;
* catálogo de dados;
* metadados;
* entidades;
* domínios;
* qualidade;
* governança;
* ciclo de vida;
* integração;
* indicadores.

---

# 10. Nível 6 – Arquitetura de Aplicações e Módulos

Define as soluções de software que suportam os processos municipais.

Inclui:

* módulos;
* componentes;
* serviços;
* aplicações;
* microsserviços, quando aplicável;
* componentes reutilizáveis;
* interfaces;
* dependências.

A estrutura de aplicações deverá ser derivada das necessidades de negócio e não exclusivamente da estrutura das secretarias.

---

# 11. Nível 7 – Integrações e APIs

Define a interoperabilidade do SIGMUN.

Inclui:

* APIs;
* contratos de integração;
* eventos;
* mensagens;
* integrações externas;
* integrações internas;
* padrões de interoperabilidade;
* autenticação;
* autorização;
* monitoramento.

---

# 12. Nível 8 – Segurança, LGPD e Conformidade

Concentra os documentos relacionados à proteção das informações e conformidade legal.

Inclui:

* segurança da informação;
* proteção de dados pessoais;
* LGPD;
* classificação da informação;
* controle de acesso;
* identidade;
* auditoria;
* continuidade;
* recuperação;
* gestão de vulnerabilidades;
* resposta a incidentes.

---

# 13. Nível 9 – Desenvolvimento

Representa os artefatos relacionados à implementação.

Inclui:

* padrões de código;
* arquitetura de componentes;
* convenções;
* bibliotecas;
* componentes;
* repositórios;
* pipelines;
* configuração;
* documentação técnica.

---

# 14. Nível 10 – Testes e Qualidade

Define e registra a verificação da solução.

Inclui:

* estratégia de testes;
* planos de teste;
* casos de teste;
* testes funcionais;
* testes de integração;
* testes de segurança;
* testes de desempenho;
* testes de usabilidade;
* evidências;
* defeitos;
* aceite.

---

# 15. Nível 11 – Implantação e Operação

Documenta a disponibilização e operação do SIGMUN.

Inclui:

* implantação;
* infraestrutura;
* configuração;
* ambientes;
* migração;
* treinamento;
* operação;
* monitoramento;
* suporte;
* continuidade;
* recuperação de desastre;
* procedimentos operacionais.

---

# 16. Nível 12 – Conhecimento, Indicadores e Evolução

Representa o conhecimento produzido durante a vida do SIGMUN.

Inclui:

* conhecimento corporativo;
* indicadores;
* BI;
* Analytics;
* IA;
* estudos;
* boas práticas;
* lições aprendidas;
* inovação;
* maturidade digital;
* avaliação;
* evolução.

Referência principal:

```text
04-Conhecimento-Corporativo/
000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md
```

---

# 17. Classificação dos Documentos

Todo documento deverá pertencer a uma categoria.

As principais categorias são:

## 17.1. Documento Fundacional

Estabelece princípios, conceitos ou estruturas fundamentais.

Exemplo:

```text
000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
```

---

## 17.2. Política

Estabelece princípios obrigatórios e diretrizes institucionais.

---

## 17.3. Norma

Estabelece requisitos ou padrões obrigatórios.

---

## 17.4. Manual

Explica como determinada atividade deverá ser executada.

---

## 17.5. Plano

Define ações, responsabilidades, prazos e recursos.

---

## 17.6. Modelo

Define uma estrutura reutilizável.

---

## 17.7. Framework

Define uma estrutura metodológica ou conceitual reutilizável.

---

## 17.8. Arquitetura

Define estrutura, princípios, componentes e relacionamentos.

---

## 17.9. Mapa

Representa visualmente ou estruturalmente um domínio.

---

## 17.10. Catálogo

Relaciona elementos organizados de determinado domínio.

---

## 17.11. Registro

Registra fatos, decisões, eventos ou ocorrências.

Exemplo:

```text
000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
```

---

## 17.12. Especificação

Define características detalhadas de uma solução ou componente.

---

## 17.13. Relatório

Apresenta análise, resultados ou evidências.

---

# 18. Identificação dos Documentos

Os documentos deverão utilizar identificadores estáveis sempre que fizerem parte de uma sequência corporativa.

Formato:

```text
<IDENTIFICADOR>-<NOME-DESCRITIVO>-v<VERSÃO>.md
```

Exemplo:

```text
000C-HIERARQUIA-DOCUMENTAL-v1.0.md
```

Quando o documento fizer parte de uma estrutura numerada, o identificador deverá ser preservado entre versões.

---

# 19. Convenção de Nomes

Os nomes deverão:

* utilizar linguagem clara;
* evitar caracteres especiais;
* evitar espaços;
* utilizar hífen para separação;
* preservar o identificador;
* utilizar nomenclatura consistente;
* refletir o conteúdo.

Exemplo:

```text
Mapa-de-Processos-v1.0.md
```

Evitar:

```text
mapa processos final.md
MapaProcessosNovo.md
Mapa_de_Processos_FINAL2.md
```

---

# 20. Convenção de Versionamento

O SIGMUN adotará:

```text
MAJOR.MINOR
```

Exemplo:

```text
1.0
1.1
1.2
2.0
```

---

# 21. Versão MAJOR

O incremento de MAJOR ocorrerá quando houver alteração estrutural ou conceitual significativa.

Exemplo:

```text
1.4 → 2.0
```

Pode ocorrer quando:

* a finalidade do documento mudar;
* a estrutura conceitual for reformulada;
* princípios fundamentais forem alterados;
* houver quebra de compatibilidade;
* a arquitetura definida anteriormente for substituída.

---

# 22. Versão MINOR

O incremento de MINOR ocorrerá quando houver evolução compatível.

Exemplo:

```text
1.0 → 1.1
1.1 → 1.2
```

Pode ocorrer quando houver:

* inclusão de conteúdo;
* melhoria estrutural;
* detalhamento;
* ampliação;
* correção conceitual sem ruptura;
* atualização de referências.

---

# 23. Correções sem Nova Versão

Correções puramente editoriais poderão ser realizadas sem alteração da versão quando não modificarem o significado do documento.

Exemplos:

* ortografia;
* pontuação;
* formatação;
* links quebrados;
* pequenos ajustes de Markdown.

Entretanto, a decisão de não alterar a versão deverá ser utilizada com parcimônia.

---

# 24. Preservação de Versões

Versões relevantes deverão ser preservadas.

Exemplo:

```text
Cadeia-de-Valor-v1.0.md
Cadeia-de-Valor-v1.1.md
Cadeia-de-Valor-v2.0.md
```

A versão mais recente não deverá apagar automaticamente as anteriores.

---

# 25. Documento Vigente

Somente uma versão deverá possuir o status:

```text
Vigente
```

para determinada finalidade documental.

Exemplo:

```text
Cadeia-de-Valor-v1.1.md
```

Status:

```text
Vigente
```

Enquanto:

```text
Cadeia-de-Valor-v1.0.md
```

poderá possuir:

```text
Superado
```

---

# 26. Estados do Documento

Os documentos poderão assumir os seguintes estados:

```text
Rascunho
Em Revisão
Aprovado
Vigente
Superado
Obsoleto
Arquivado
Cancelado
```

---

# 27. Rascunho

Documento em elaboração.

Não deverá ser utilizado como fonte normativa oficial.

---

# 28. Em Revisão

Documento submetido a análise formal.

Ainda não deverá substituir a versão vigente.

---

# 29. Aprovado

Documento formalmente aprovado, aguardando ou iniciando sua entrada em vigor.

---

# 30. Vigente

Documento atualmente válido e utilizado como referência oficial.

---

# 31. Superado

Documento substituído por uma versão posterior.

Deverá permanecer disponível quando houver necessidade de histórico.

---

# 32. Obsoleto

Documento que deixou de possuir validade ou utilidade operacional.

---

# 33. Arquivado

Documento preservado para fins históricos, legais, de auditoria ou conhecimento institucional.

---

# 34. Cancelado

Documento que deixou de ser desenvolvido ou foi formalmente retirado antes de sua entrada em vigor.

---

# 35. Cabeçalho Corporativo

Todo documento corporativo deverá possuir cabeçalho padronizado.

Modelo:

```markdown
#### Nome do Documento

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** <Domínio>

**Versão:** <Versão>

**Status:** <Status>

**Classificação da Informação:** <Classificação>

**Documento(s) Relacionado(s):**

- <Documento 1>
- <Documento 2>
```

---

# 36. Rodapé Corporativo

Todo documento deverá possuir rodapé padronizado.

Modelo:

```markdown
**Documento:** <Nome-do-Arquivo>

**Última atualização:** <AAAA-MM-DD>

**Responsável:** Equipe SIGMUN

**Status da revisão:** <Status>
```

---

# 37. Controle de Versões Interno

Documentos estruturantes deverão possuir histórico de versões.

Modelo:

```markdown
# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |
| 1.1 | AAAA-MM-DD | Revisão |
```

---

# 38. Relacionamento entre Documentos

Documentos deverão indicar explicitamente seus relacionamentos.

Os relacionamentos poderão representar:

* dependência;
* origem;
* derivação;
* referência;
* complementação;
* substituição;
* aprovação;
* decisão;
* implementação.

---

# 39. Documento Fonte e Documento Derivado

Quando um documento deriva de outro, isso deverá ser explicitamente indicado.

Exemplo:

```text
Cadeia de Valor
      ↓
Mapa de Processos
      ↓
Casos de Uso
      ↓
Requisitos
      ↓
Critérios de Aceitação
```

O documento derivado não deverá contradizer o documento fonte sem uma decisão formal que justifique a alteração.

---

# 40. Hierarquia de Autoridade

Quando houver conflito entre documentos, deverá ser considerada a seguinte ordem:

```text
Constituição do Projeto
        ↓
Princípios Corporativos
        ↓
Políticas
        ↓
Normas
        ↓
Arquitetura
        ↓
Modelos Corporativos
        ↓
Processos
        ↓
Procedimentos
        ↓
Especificações
        ↓
Implementação
```

Documentos inferiores não deverão contrariar documentos superiores sem aprovação formal.

---

# 41. Resolução de Conflitos

Quando dois documentos apresentarem informações conflitantes:

1. identificar o conflito;
2. identificar os documentos envolvidos;
3. determinar a autoridade de cada documento;
4. verificar a versão vigente;
5. analisar o impacto;
6. registrar a decisão;
7. atualizar os documentos afetados;
8. registrar ADR quando aplicável.

---

# 42. Registro de Decisões Arquiteturais

Decisões arquiteturais relevantes deverão ser registradas no:

```text
000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
```

Uma decisão registrada em ADR deverá ser referenciada pelos documentos afetados.

---

# 43. Relação com Requisitos

Documentos de negócio deverão possuir rastreabilidade até requisitos quando aplicável.

A relação deverá seguir:

```text
Objetivo
 ↓
Capacidade
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
```

---

# 44. Relação com Conhecimento Corporativo

Documentos que produzam conhecimento institucional relevante deverão ser registrados no catálogo corporativo de conhecimento.

Referência:

```text
04-Conhecimento-Corporativo/
000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md
```

---

# 45. Classificação da Informação

Todo documento deverá possuir classificação.

Classificações possíveis incluem:

* Pública;
* Uso Interno;
* Restrita;
* Confidencial.

A classificação deverá obedecer à Política de Classificação da Informação e Publicação de Artefatos.

---

# 46. Publicação

A publicação de documentos deverá considerar:

* classificação;
* segurança;
* LGPD;
* propriedade intelectual;
* contratos;
* informações de terceiros;
* riscos;
* necessidade de transparência.

O princípio geral será:

> **Aberto sempre que possível, restrito sempre que necessário.**

---

# 47. Repositório Documental

O repositório do SIGMUN deverá manter:

* documentos vigentes;
* versões históricas relevantes;
* modelos;
* registros;
* decisões;
* artefatos;
* referências;
* documentação técnica;
* conhecimento corporativo.

---

# 48. Estrutura Física e Estrutura Lógica

A estrutura de diretórios representa a organização física.

A hierarquia documental representa a organização lógica.

As duas deverão ser coerentes, mas não necessariamente idênticas.

Exemplo:

```text
Diretório:
02-Modelo-de-Negocio/

Documento:
Cadeia-de-Valor-v1.1.md

Domínio lógico:
Modelo de Negócio

Categoria:
Mapa / Arquitetura de Negócio
```

---

# 49. Proibição de Duplicidade

Não deverão existir duas fontes oficiais diferentes para o mesmo conceito.

Exemplo inadequado:

```text
Mapa-de-Processos-v1.0.md
Processos-Municipais-v1.0.md
```

ambos sendo utilizados como fontes oficiais para o mesmo mapa.

Deverá existir uma fonte oficial e, quando necessário, documentos derivados.

---

# 50. Referências Cruzadas

Quando um documento depender de outro, deverá haver referência explícita.

Exemplo:

```markdown
Consulte também:

- Mapa-de-Processos-v1.0.md
- Mapa-de-Servicos-v1.0.md
- Casos-de-Uso-v1.0.md
```

---

# 51. Ciclo de Vida Documental

O ciclo de vida padrão será:

```text
Identificação
     ↓
Criação
     ↓
Revisão
     ↓
Aprovação
     ↓
Publicação
     ↓
Vigência
     ↓
Revisão
     ↓
Nova Versão
     ↓
Superação
     ↓
Arquivamento
```

---

# 52. Gestão de Mudanças

Mudanças que afetem documentos corporativos deverão ser avaliadas quanto ao impacto em:

* arquitetura;
* processos;
* requisitos;
* dados;
* aplicações;
* integrações;
* segurança;
* legislação;
* treinamento;
* operação.

---

# 53. Controle de Dependências

Antes de alterar um documento estrutural, deverá ser verificado:

* quem o referencia;
* quais documentos dele derivam;
* quais requisitos dependem dele;
* quais sistemas dependem dele;
* quais processos dependem dele;
* quais decisões estão relacionadas.

---

# 54. Documentos Obsoletos

Documentos obsoletos não deverão ser utilizados como fonte operacional.

Quando mantidos, deverão possuir indicação clara:

```markdown
**Status:** Obsoleto
```

ou:

```markdown
**Status:** Superado
```

---

# 55. Arquivamento

O arquivamento deverá preservar:

* conteúdo;
* versão;
* data;
* responsável;
* motivo da substituição;
* relação com a versão posterior.

---

# 56. Auditoria Documental

A governança deverá poder responder:

* qual é o documento vigente?
* qual foi sua versão anterior?
* quem aprovou?
* quando foi alterado?
* por que foi alterado?
* quais documentos foram afetados?
* qual decisão justificou a alteração?

---

# 57. Convenção para o SIGMUN

A convenção oficial será:

```text
<ID>-<NOME>-v<MAJOR>.<MINOR>.md
```

Exemplos:

```text
000C-HIERARQUIA-DOCUMENTAL-v1.0.md
Cadeia-de-Valor-v1.1.md
Mapa-de-Processos-v1.0.md
Casos-de-Uso-v1.0.md
```

---

# 58. Regra para Novos Documentos

Antes de criar um novo documento, o colaborador deverá verificar:

1. se já existe documento equivalente;
2. se o conteúdo pode ser incorporado a documento existente;
3. qual domínio deverá receber o documento;
4. qual categoria documental se aplica;
5. qual identificador deverá ser utilizado;
6. quais documentos deverão ser relacionados;
7. qual classificação da informação será aplicada;
8. qual responsável deverá ser definido.

---

# 59. Regra para Nova Versão

Antes de criar uma nova versão, deverá ser verificado:

1. qual é a versão vigente;
2. qual mudança será realizada;
3. se a mudança é editorial ou conceitual;
4. se há impacto em documentos dependentes;
5. se há necessidade de ADR;
6. se há necessidade de aprovação;
7. se a versão anterior deverá ser preservada;
8. quais documentos deverão ser atualizados.

---

# 60. Regra para Substituição

Quando uma nova versão entrar em vigor:

```text
Versão anterior → Superado
Nova versão → Vigente
```

Exemplo:

```text
Cadeia-de-Valor-v1.0.md
Status: Superado

Cadeia-de-Valor-v1.1.md
Status: Vigente
```

---

# 61. Exemplo Prático

Supondo a criação inicial:

```text
Mapa-de-Processos-v1.0.md
```

Após uma revisão estrutural compatível:

```text
Mapa-de-Processos-v1.1.md
```

Após nova alteração estrutural significativa:

```text
Mapa-de-Processos-v2.0.md
```

O diretório poderá conter:

```text
Mapa-de-Processos-v1.0.md
Mapa-de-Processos-v1.1.md
Mapa-de-Processos-v2.0.md
```

Apenas:

```text
Mapa-de-Processos-v2.0.md
```

será vigente.

---

# 62. Benefícios da Hierarquia Documental

A adoção desta hierarquia proporciona:

* organização;
* rastreabilidade;
* governança;
* continuidade;
* auditabilidade;
* redução de duplicidade;
* preservação do conhecimento;
* facilidade de manutenção;
* melhor onboarding;
* maior qualidade arquitetural;
* maior transparência;
* maior segurança documental.

---

# 63. Responsabilidades

## Governança Corporativa

Responsável por definir e manter as regras documentais.

## Arquitetura Corporativa

Responsável pela coerência arquitetural.

## Responsáveis pelos Domínios

Responsáveis pelo conteúdo dos documentos de seus respectivos domínios.

## Colaboradores

Responsáveis por respeitar os padrões definidos.

## Revisores

Responsáveis por verificar qualidade, coerência e conformidade.

---

# 64. Conformidade

Todo novo documento corporativo deverá observar:

* esta Hierarquia Documental;
* o Padrão Corporativo de Documentação;
* o Modelo de Documento;
* o Guia de Contribuição;
* as políticas corporativas aplicáveis;
* as regras de classificação da informação;
* as regras de versionamento;
* as regras de rastreabilidade.

---

# 65. Evolução da Hierarquia

A própria Hierarquia Documental poderá evoluir.

Alterações significativas deverão:

* ser justificadas;
* ser registradas;
* avaliar impacto;
* preservar a versão anterior;
* atualizar os documentos dependentes;
* possuir aprovação adequada.

---

# 66. Regra Fundamental

A documentação do SIGMUN deverá seguir o princípio:

> **Um conceito, uma fonte oficial, uma responsabilidade, uma rastreabilidade.**

E:

> **Toda versão relevante deve ser identificável, rastreável e preservável.**

---

# 67. Disposições Finais

A Hierarquia Documental constitui um dos mecanismos fundamentais de governança do SIGMUN.

Nenhum documento isolado deverá ser considerado suficiente para representar uma decisão corporativa quando houver necessidade de relacionamento com:

* estratégia;
* negócio;
* processos;
* requisitos;
* arquitetura;
* dados;
* tecnologia;
* segurança;
* indicadores;
* operação.

O conjunto documental deverá ser tratado como um **sistema integrado de conhecimento institucional**.

A documentação não é apenas registro do projeto.

Ela constitui parte da própria arquitetura corporativa do SIGMUN.

---

**Documento:** 000C-HIERARQUIA-DOCUMENTAL-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
