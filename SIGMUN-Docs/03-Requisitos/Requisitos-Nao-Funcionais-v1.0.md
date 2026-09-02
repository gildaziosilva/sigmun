# Requisitos Não Funcionais

#### Requisitos Não Funcionais

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* 000A-PADRAO-CORPORATIVO-DE-DOCUMENTACAO-DO-SIGMUN.md
* 000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000C-HIERARQUIA-DOCUMENTAL-v1.0.md
* 000D-MODELO-DE-DOCUMENTO.md
* 000E-GUIA-DE-CONTRIBUICAO.md
* 000F-REGISTRO-DE-DECISOES-ARQUITETURAIS.md
* 000G-FRAMEWORK-CORPORATIVO-DE-GESTAO-DE-REQUISITOS-E-RRASTREABILIDADE.md
* Regras-de-Negocio-v1.0.md
* Requisitos-Funcionais-v1.0.md
* Especificacoes-v1.0.md
* Criterios-de-Aceitacao-v1.0.md
* Matriz-de-Rastreabilidade-v1.0.md
* 011-Arquitetura-de-Segurança.md
* 012-Arquitetura-de-Implantacao.md
* 013-Experiencia-do-Usuario.md
* 019-Arquitetura-de-Dispositivos-Móveis-e-Servicos-de-Campo.md
* 021-Governanca-de-Dados.md
* 022-Arquitetura-de-BI-Analytics-e-IA.md

---

# 1. Finalidade

Este documento estabelece o padrão corporativo para identificação, documentação, validação, rastreabilidade, versionamento e governança dos **Requisitos Não Funcionais (RNF) do SIGMUN**.

Os Requisitos Não Funcionais definem características de qualidade, restrições, propriedades, condições operacionais e atributos que a solução deverá atender.

Eles complementam os Requisitos Funcionais e são fundamentais para garantir que o SIGMUN não apenas execute suas funções, mas as execute com níveis adequados de segurança, desempenho, disponibilidade, confiabilidade, acessibilidade, usabilidade, interoperabilidade e sustentabilidade.

---

# 2. Objetivos

Os Requisitos Não Funcionais deverão:

* estabelecer atributos mensuráveis de qualidade;
* definir restrições relevantes da solução;
* orientar decisões arquiteturais;
* orientar desenvolvimento;
* orientar infraestrutura;
* orientar segurança;
* orientar testes;
* estabelecer critérios objetivos de qualidade;
* apoiar homologação;
* reduzir riscos técnicos;
* preservar requisitos institucionais;
* permitir análise de impacto;
* permitir rastreabilidade.

---

# 3. Definição

Um Requisito Não Funcional especifica uma característica, restrição ou condição que a solução deverá atender, mas que não representa diretamente uma função de negócio.

Exemplo:

> O sistema deverá manter disponibilidade mínima de 99,5% ao mês, excetuando-se janelas de manutenção previamente comunicadas.

O requisito não define uma funcionalidade específica, mas uma condição de qualidade da solução.

---

# 4. Requisito Não Funcional x Requisito Funcional

### Requisito Funcional

Define:

> **O que o sistema deverá fazer.**

### Requisito Não Funcional

Define:

> **Com quais características, restrições ou níveis de qualidade o sistema deverá fazer.**

Exemplo:

```text
RF-COMPRAS-001

O sistema deverá permitir consultar contratos.

RNF-PERF-001

A consulta deverá apresentar os resultados em até
2 segundos nas condições de carga estabelecidas.
```

---

# 5. Requisito Não Funcional x Arquitetura

O Requisito Não Funcional estabelece a necessidade.

A arquitetura define a solução técnica capaz de atendê-la.

Exemplo:

```text
RNF-SEG-001
Os dados deverão ser protegidos durante transmissão.

        ↓

Arquitetura de Segurança

        ↓

Solução técnica de proteção de comunicação.
```

O requisito não deverá prescrever uma tecnologia específica sem justificativa arquitetural.

---

# 6. Princípios

Os Requisitos Não Funcionais deverão ser:

* claros;
* mensuráveis quando possível;
* verificáveis;
* rastreáveis;
* consistentes;
* necessários;
* proporcionais ao risco;
* independentes de tecnologia quando possível;
* versionados;
* governados.

---

# 7. Identificação

Cada requisito deverá possuir identificador único.

Formato recomendado:

```text
RNF-<CATEGORIA>-<NÚMERO>
```

Exemplos:

```text
RNF-SEG-001
RNF-PERF-001
RNF-DISP-001
RNF-USA-001
RNF-INT-001
RNF-ESC-001
```

---

# 8. Categorias

Os Requisitos Não Funcionais poderão ser classificados em:

* segurança;
* privacidade;
* desempenho;
* disponibilidade;
* confiabilidade;
* escalabilidade;
* capacidade;
* usabilidade;
* acessibilidade;
* interoperabilidade;
* portabilidade;
* manutenibilidade;
* observabilidade;
* auditabilidade;
* continuidade;
* recuperação de desastres;
* compatibilidade;
* sustentabilidade;
* operação;
* infraestrutura;
* qualidade de dados;
* arquitetura;
* conformidade;
* governança;
* experiência do usuário.

---

# 9. Requisitos de Segurança

Os requisitos de segurança deverão estabelecer condições relacionadas à proteção da solução e das informações.

Exemplos:

* autenticação;
* autorização;
* controle de acesso;
* segregação de funções;
* criptografia;
* gestão de sessões;
* proteção contra ataques;
* auditoria;
* gestão de vulnerabilidades;
* segurança de APIs.

Exemplo:

```text
RNF-SEG-001

O sistema deverá proteger os dados sensíveis durante
a transmissão por mecanismos de segurança adequados.
```

---

# 10. Requisitos de Privacidade

Deverão ser considerados quando houver tratamento de dados pessoais.

Poderão abranger:

* minimização;
* finalidade;
* controle de acesso;
* rastreabilidade;
* retenção;
* descarte;
* anonimização quando aplicável;
* atendimento a direitos;
* segregação;
* proteção.

Exemplo:

```text
RNF-PRI-001

O sistema deverá restringir o acesso a dados pessoais
conforme as autorizações e finalidades definidas.
```

---

# 11. Requisitos de Desempenho

Deverão estabelecer métricas objetivas sempre que possível.

Poderão considerar:

* tempo de resposta;
* throughput;
* latência;
* processamento;
* consultas;
* geração de relatórios;
* APIs;
* sincronização.

Exemplo:

```text
RNF-PERF-001

O sistema deverá responder às consultas classificadas
como padrão em até 2 segundos para o volume de dados
e carga definidos no cenário de referência.
```

---

# 12. Requisitos de Capacidade

Deverão definir limites ou volumes suportados.

Exemplos:

* número de usuários;
* quantidade de registros;
* requisições;
* documentos;
* armazenamento;
* transações.

---

# 13. Requisitos de Disponibilidade

Deverão definir o nível esperado de disponibilidade.

Exemplo:

```text
RNF-DISP-001

O serviço deverá possuir disponibilidade mínima de 99,5%
mensal, excetuando-se as janelas de manutenção previamente
planejadas e comunicadas.
```

Os níveis definitivos deverão ser definidos conforme criticidade do serviço.

---

# 14. Requisitos de Confiabilidade

Deverão estabelecer condições para operação consistente.

Poderão abranger:

* integridade;
* consistência;
* tolerância a falhas;
* recuperação;
* idempotência;
* prevenção de perda de dados.

---

# 15. Requisitos de Escalabilidade

Deverão estabelecer a capacidade de crescimento da solução.

O SIGMUN deverá ser projetado considerando expansão:

* de municípios;
* de usuários;
* de secretarias;
* de módulos;
* de dados;
* de integrações;
* de serviços.

Exemplo:

```text
RNF-ESC-001

A arquitetura deverá permitir expansão da capacidade
de processamento sem necessidade de alteração estrutural
do modelo funcional da solução.
```

---

# 16. Requisitos de Multi-Município

Considerando a abrangência nacional do SIGMUN, quando aplicável deverão ser considerados:

* isolamento de dados;
* configuração por município;
* parametrização;
* identidade institucional;
* políticas locais;
* escalabilidade;
* governança.

---

# 17. Requisitos de Usabilidade

Deverão estabelecer condições para facilitar a utilização do sistema.

Poderão considerar:

* consistência;
* simplicidade;
* feedback;
* prevenção de erros;
* navegação;
* aprendizagem;
* clareza das mensagens.

---

# 18. Requisitos de Acessibilidade

O SIGMUN deverá considerar requisitos de acessibilidade aplicáveis à solução.

Poderão abranger:

* navegação por teclado;
* leitores de tela;
* contraste;
* tamanho de elementos;
* alternativas textuais;
* foco;
* linguagem clara;
* acessibilidade em dispositivos móveis.

---

# 19. Requisitos de Experiência do Usuário

Deverão considerar:

* consistência;
* previsibilidade;
* redução de esforço;
* clareza;
* eficiência;
* prevenção de erros;
* orientação ao usuário.

Os requisitos deverão manter alinhamento com a arquitetura de experiência do usuário.

---

# 20. Requisitos de Interoperabilidade

O SIGMUN deverá ser capaz de interoperar com sistemas e serviços externos quando necessário.

Poderão abranger:

* APIs;
* padrões de dados;
* formatos;
* protocolos;
* autenticação;
* versionamento;
* compatibilidade.

---

# 21. Requisitos de Integração

Deverão definir condições de qualidade das integrações.

Exemplos:

```text
RNF-INT-001

As integrações deverão possuir mecanismo de tratamento
de falhas e registro das ocorrências relevantes.
```

---

# 22. Requisitos de Portabilidade

Quando aplicável, a solução deverá permitir execução em ambientes compatíveis com a arquitetura definida.

Deverão ser evitadas dependências tecnológicas desnecessárias.

---

# 23. Requisitos de Compatibilidade

Poderão definir:

* navegadores;
* dispositivos;
* sistemas operacionais;
* versões suportadas;
* padrões de comunicação;
* formatos de arquivo.

---

# 24. Requisitos de Manutenibilidade

Deverão considerar:

* modularidade;
* documentação;
* testabilidade;
* observabilidade;
* baixo acoplamento;
* facilidade de evolução;
* padrões de código.

Exemplo:

```text
RNF-MAN-001

Os componentes da solução deverão possuir documentação
suficiente para permitir sua manutenção por equipe técnica
qualificada sem dependência exclusiva de um indivíduo.
```

---

# 25. Requisitos de Evolutividade

A solução deverá permitir evolução sem necessidade de alterações desproporcionais na arquitetura.

Deverão ser consideradas:

* novos módulos;
* novos municípios;
* novas integrações;
* alterações normativas;
* novos dispositivos;
* novas tecnologias.

---

# 26. Requisitos de Observabilidade

A solução deverá fornecer informações suficientes para operação, monitoramento e diagnóstico.

Poderão abranger:

* logs;
* métricas;
* eventos;
* rastreamento;
* alertas;
* indicadores técnicos.

---

# 27. Requisitos de Auditabilidade

Operações relevantes deverão possuir evidências suficientes para auditoria.

Poderão incluir:

* usuário;
* data;
* hora;
* operação;
* entidade;
* resultado;
* origem;
* alterações.

---

# 28. Requisitos de Rastreabilidade

Deverá ser possível rastrear eventos e operações relevantes desde sua origem até seu resultado.

---

# 29. Requisitos de Continuidade

Serviços críticos deverão possuir requisitos relacionados à continuidade.

Poderão incluir:

* RTO;
* RPO;
* contingência;
* recuperação;
* redundância;
* procedimentos operacionais.

---

# 30. Requisitos de Recuperação de Desastres

Deverão definir, quando aplicável:

* tempo máximo para recuperação;
* perda máxima aceitável de dados;
* procedimentos de restauração;
* testes de recuperação;
* responsabilidades.

---

# 31. Requisitos de Backup

Deverão definir:

* periodicidade;
* retenção;
* proteção;
* localização;
* criptografia quando aplicável;
* testes de restauração.

---

# 32. Requisitos de Integridade dos Dados

Deverão garantir que os dados permaneçam:

* completos;
* consistentes;
* íntegros;
* rastreáveis;
* protegidos contra alterações indevidas.

---

# 33. Requisitos de Qualidade de Dados

Poderão considerar:

* completude;
* precisão;
* consistência;
* atualidade;
* unicidade;
* validade.

---

# 34. Requisitos de Retenção

Deverão estar alinhados à Política de Retenção e Descarte de Documentos e às regras de governança de dados.

---

# 35. Requisitos de Disponibilidade Offline

Para atividades de campo, quando aplicável, a solução deverá considerar operação **Offline First**.

Deverão ser definidos:

* funcionalidades disponíveis offline;
* dados armazenados localmente;
* período máximo offline;
* sincronização;
* conflitos;
* recuperação;
* segurança local.

---

# 36. Requisitos de Sincronização

Quando houver operação distribuída ou offline:

```text
Operação local
      ↓
Armazenamento local
      ↓
Fila de sincronização
      ↓
Servidor
      ↓
Validação
      ↓
Confirmação
```

Deverão ser definidos requisitos para:

* consistência;
* segurança;
* reprocessamento;
* conflitos;
* integridade.

---

# 37. Requisitos de Segurança em Dispositivos Móveis

Quando aplicável:

* proteção de dados locais;
* autenticação;
* bloqueio;
* expiração;
* armazenamento seguro;
* sincronização protegida;
* limpeza remota quando aplicável.

---

# 38. Requisitos de Infraestrutura

Poderão definir:

* capacidade computacional;
* armazenamento;
* rede;
* redundância;
* disponibilidade;
* monitoramento;
* recuperação.

Os requisitos não deverão substituir os documentos de arquitetura e implantação.

---

# 39. Requisitos de Operação

Deverão considerar:

* monitoramento;
* suporte;
* manutenção;
* atualização;
* incidentes;
* mudanças;
* procedimentos operacionais.

---

# 40. Requisitos de Implantação

Poderão abranger:

* instalação;
* configuração;
* migração;
* atualização;
* rollback;
* validação;
* documentação.

---

# 41. Requisitos de Atualização

Deverão definir condições para atualização segura da solução.

Exemplo:

```text
RNF-OPS-001

Atualizações deverão possuir mecanismo de rollback
compatível com a criticidade do serviço.
```

---

# 42. Requisitos de Migração

Quando aplicável, deverão considerar:

* integridade;
* completude;
* validação;
* rastreabilidade;
* reconciliação;
* rollback.

---

# 43. Requisitos de Escalabilidade Nacional

Considerando a finalidade nacional do projeto, a arquitetura deverá ser capaz de suportar crescimento progressivo da base de municípios.

A capacidade deverá ser avaliada por cenários, e não por um número arbitrário de municípios.

Deverão ser considerados:

* municípios pequenos;
* municípios médios;
* municípios grandes;
* diferentes volumes de usuários;
* diferentes volumes de dados;
* diferentes níveis de integração.

---

# 44. Requisitos de Configurabilidade

Quando diferentes municípios possuírem necessidades legítimas distintas, a solução deverá permitir parametrização sem criação desnecessária de versões independentes do software.

---

# 45. Requisitos de Localização

Poderão abranger:

* idioma;
* formatos;
* calendário;
* timezone;
* moeda;
* regras locais.

---

# 46. Requisitos de Documentação

Componentes relevantes deverão possuir documentação adequada à manutenção e operação.

---

# 47. Requisitos de Código

Quando estabelecidos como requisito corporativo, poderão considerar:

* padrões;
* análise estática;
* cobertura de testes;
* revisão;
* documentação;
* segurança.

Detalhes deverão ser definidos nos padrões de desenvolvimento.

---

# 48. Requisitos de Testabilidade

Os componentes deverão permitir testes adequados ao nível de risco e criticidade.

---

# 49. Requisitos de Monitoramento

Serviços críticos deverão possuir mecanismos de monitoramento capazes de identificar indisponibilidade ou degradação relevante.

---

# 50. Requisitos de Alertas

Deverão definir:

* condição;
* severidade;
* destinatário;
* canal;
* escalonamento;
* registro.

---

# 51. Requisitos de Logs

Os registros deverão conter informações suficientes para diagnóstico e auditoria, respeitando as políticas de segurança e proteção de dados.

Deverão ser evitados dados pessoais ou sensíveis desnecessários em logs.

---

# 52. Requisitos de Métricas

Poderão incluir:

* disponibilidade;
* latência;
* erros;
* volume;
* utilização;
* filas;
* sincronização;
* integrações.

---

# 53. Requisitos de Segurança da Informação

Os requisitos deverão estar alinhados à Arquitetura de Segurança e às políticas corporativas do SIGMUN.

---

# 54. Requisitos de Conformidade

Quando aplicável, deverão considerar:

* legislação;
* regulamentação;
* políticas;
* normas;
* contratos;
* padrões institucionais.

---

# 55. Requisitos de Licenciamento

Quando houver dependências de software ou componentes de terceiros, deverão ser consideradas suas condições de licenciamento.

---

# 56. Requisitos de Código Aberto

Quando o SIGMUN utilizar componentes de código aberto, deverão ser avaliados:

* licença;
* obrigações;
* segurança;
* manutenção;
* compatibilidade;
* sustentabilidade.

---

# 57. Requisitos de Sustentabilidade

A solução deverá considerar sustentabilidade técnica e econômica.

Poderão ser considerados:

* custo operacional;
* dependências;
* capacidade de manutenção;
* reutilização;
* eficiência;
* redução de retrabalho.

---

# 58. Requisitos de Neutralidade Tecnológica

Os Requisitos Não Funcionais deverão evitar a imposição de tecnologias específicas quando o objetivo puder ser descrito por uma característica mensurável.

Exemplo inadequado:

```text
O sistema deverá utilizar tecnologia X.
```

Preferir:

```text
A solução deverá suportar o nível de desempenho definido
para o serviço.
```

A tecnologia deverá ser definida pela arquitetura, quando aplicável.

---

# 59. Requisitos Mensuráveis

Sempre que possível, o requisito deverá utilizar métricas.

Exemplo:

```text
RNF-PERF-001

Percentil 95 do tempo de resposta ≤ 2 segundos.
```

Evitar:

```text
O sistema deverá ser rápido.
```

---

# 60. Cenários de Referência

Métricas deverão possuir cenário de referência.

Exemplo:

```text
Usuários simultâneos: <quantidade>
Volume de dados: <quantidade>
Operação: <operação>
Infraestrutura: <referência>
Percentil: P95
Meta: ≤ 2 segundos
```

Sem cenário de referência, a métrica poderá ser ambígua.

---

# 61. Critérios de Aceitação

Todo Requisito Não Funcional deverá possuir critério de aceitação mensurável ou verificável.

Exemplo:

```text
RNF-PERF-001

Critério:

Em cenário de referência definido,
95% das consultas deverão responder em até 2 segundos.
```

---

# 62. Testes

Os RNFs deverão possuir métodos de verificação adequados.

Exemplos:

* teste de carga;
* teste de segurança;
* teste de disponibilidade;
* teste de recuperação;
* teste de acessibilidade;
* inspeção;
* análise documental;
* teste de interoperabilidade.

---

# 63. Prioridade

Poderão ser classificados como:

```text
Crítica
Alta
Média
Baixa
```

---

# 64. Criticidade

A criticidade poderá considerar:

* impacto ao cidadão;
* impacto financeiro;
* impacto legal;
* impacto operacional;
* impacto à segurança;
* impacto à continuidade;
* impacto à reputação institucional.

---

# 65. Dependências

Deverão ser registradas dependências com:

* arquitetura;
* infraestrutura;
* segurança;
* dados;
* integrações;
* fornecedores;
* componentes;
* outros requisitos.

---

# 66. Conflitos entre RNFs

Quando dois Requisitos Não Funcionais entrarem em conflito, deverá ser realizada análise de trade-off.

Exemplo:

```text
Segurança
    ↕
Desempenho

Disponibilidade
    ↕
Custo

Flexibilidade
    ↕
Simplicidade
```

A decisão deverá ser registrada quando possuir impacto arquitetural relevante.

---

# 67. Rastreabilidade

Os RNFs deverão possuir rastreabilidade bidirecional.

Fluxo:

```text
Objetivo / Necessidade
        ↓
RNF
        ↓
Arquitetura
        ↓
Especificação
        ↓
Critério de Aceitação
        ↓
Teste
        ↓
Evidência
```

---

# 68. Relação com Arquitetura

Cada RNF relevante deverá possuir vínculo com os elementos arquiteturais responsáveis pelo seu atendimento.

---

# 69. Relação com Requisitos Funcionais

Um RNF poderá se aplicar a:

* um requisito funcional;
* vários requisitos funcionais;
* um módulo;
* um serviço;
* todo o sistema.

---

# 70. Relação com Serviços

A criticidade de um serviço poderá determinar diferentes níveis de requisitos não funcionais.

Exemplo:

```text
Serviço Crítico
     ↓
Alta disponibilidade
Alta segurança
Alta observabilidade
Alta capacidade de recuperação
```

---

# 71. Relação com Critérios de Aceitação

Os critérios deverão demonstrar objetivamente o atendimento.

---

# 72. Relação com Testes

Os testes deverão fornecer evidências.

Exemplo:

```text
RNF-PERF-001
      ↓
CA-PERF-001
      ↓
TEST-PERF-001
      ↓
Evidência
```

---

# 73. Versionamento

Cada RNF deverá possuir versão.

Exemplo:

```text
RNF-PERF-001 – Versão 1.0
RNF-PERF-001 – Versão 1.1
```

Alterações deverão possuir histórico.

---

# 74. Estado

Os estados poderão ser:

```text
Proposto
Em Análise
Em Validação
Aprovado
Em Implementação
Em Teste
Homologado
Vigente
Suspenso
Superado
Cancelado
```

---

# 75. Modelo Corporativo

```markdown
# RNF-XXXX-001 – Nome do Requisito

#### Requisito Não Funcional

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RNF-XXXX-001

**Categoria:** <Categoria>

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- <Documento>

---

# 1. Descrição

<Descrição>

# 2. Objetivo

<Objetivo>

# 3. Justificativa

<Justificativa>

# 4. Escopo

<Escopo>

# 5. Métrica

<Métrica>

# 6. Meta

<Meta>

# 7. Cenário de Referência

<Cenário>

# 8. Condições

<Condições>

# 9. Dependências

<Dependências>

# 10. Requisitos Funcionais Relacionados

<Requisitos>

# 11. Serviços Relacionados

<Serviços>

# 12. Elementos Arquiteturais Relacionados

<Arquitetura>

# 13. Critérios de Aceitação

<Critérios>

# 14. Método de Verificação

<Método>

# 15. Testes

<Testes>

# 16. Evidências

<Evidências>

# 17. Segurança

<Segurança>

# 18. Privacidade

<Privacidade>

# 19. Continuidade

<Continuidade>

# 20. Prioridade

<Prioridade>

# 21. Criticidade

<Criticidade>

# 22. Rastreabilidade

<Rastreabilidade>

# 23. Impactos

<Impactos>

# 24. Observações

<Observações>

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | AAAA-MM-DD | Criação |
```

---

# 76. Exemplo Completo

````markdown
# RNF-PERF-001 – Tempo de Resposta das Consultas

#### Requisito Não Funcional

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Requisitos e Especificações

**ID:** RNF-PERF-001

**Categoria:** Desempenho

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

---

# 1. Descrição

As consultas classificadas como padrão deverão apresentar
tempo de resposta compatível com o nível de desempenho definido
para o serviço.

# 2. Métrica

Percentil 95 do tempo de resposta.

# 3. Meta

Até 2 segundos.

# 4. Cenário de Referência

O cenário de referência deverá especificar:

- número de usuários simultâneos;
- volume de dados;
- operação;
- infraestrutura;
- condições de rede.

# 5. Critério de Aceitação

Em cenário de referência aprovado, pelo menos 95% das consultas
deverão apresentar tempo de resposta igual ou inferior a 2 segundos.

# 6. Método de Verificação

Teste de desempenho.

# 7. Teste

TEST-PERF-001.

# 8. Rastreabilidade

```text
Serviço
   ↓
RNF-PERF-001
   ↓
CA-PERF-001
   ↓
TEST-PERF-001
   ↓
Evidência
````

```

---

# 77. Exemplo de Categorias Corporativas

| Código | Categoria |
|---|---|
| `RNF-SEG` | Segurança |
| `RNF-PRI` | Privacidade |
| `RNF-PERF` | Desempenho |
| `RNF-DISP` | Disponibilidade |
| `RNF-CONF` | Confiabilidade |
| `RNF-CAP` | Capacidade |
| `RNF-ESC` | Escalabilidade |
| `RNF-USA` | Usabilidade |
| `RNF-ACE` | Acessibilidade |
| `RNF-INT` | Interoperabilidade |
| `RNF-POR` | Portabilidade |
| `RNF-MAN` | Manutenibilidade |
| `RNF-OBS` | Observabilidade |
| `RNF-AUD` | Auditabilidade |
| `RNF-CON` | Continuidade |
| `RNF-OPS` | Operação |
| `RNF-DAD` | Qualidade de Dados |
| `RNF-COMP` | Compatibilidade |
| `RNF-SUS` | Sustentabilidade |
| `RNF-COMPL` | Conformidade |

---

# 78. Checklist

Antes de considerar um RNF aprovado:

- [ ] Possui identificador único?
- [ ] Possui categoria?
- [ ] Possui descrição objetiva?
- [ ] Possui justificativa?
- [ ] Possui escopo?
- [ ] É mensurável quando aplicável?
- [ ] Possui métrica?
- [ ] Possui meta?
- [ ] Possui cenário de referência quando necessário?
- [ ] Possui condições?
- [ ] Possui dependências?
- [ ] Está relacionado aos requisitos funcionais?
- [ ] Está relacionado aos serviços?
- [ ] Está relacionado à arquitetura?
- [ ] Possui critério de aceitação?
- [ ] Possui método de verificação?
- [ ] Possui teste?
- [ ] Possui evidência?
- [ ] Possui prioridade?
- [ ] Possui criticidade?
- [ ] Possui rastreabilidade?
- [ ] Está versionado?
- [ ] Está validado?

---

# 79. Governança

Os Requisitos Não Funcionais são parte integrante da definição de qualidade da solução SIGMUN.

Nenhum requisito não funcional crítico deverá ser tratado apenas como recomendação técnica.

Quando aprovado, deverá ser considerado requisito formal da solução e deverá possuir mecanismo de verificação.

Alterações relevantes deverão seguir o processo corporativo de gestão de requisitos e mudanças.

---

# 80. Regra Fundamental

Todo Requisito Não Funcional deverá permitir responder:

> **Qual característica ou restrição deverá ser atendida?**

> **Por que ela é necessária?**

> **Como será medida?**

> **Qual é a meta?**

> **Em qual cenário será avaliada?**

> **Como será verificada?**

> **Qual parte da arquitetura será responsável por atendê-la?**

> **Qual evidência demonstrará seu atendimento?**

---

# 81. Disposições Finais

Os Requisitos Não Funcionais representam os atributos de qualidade e as restrições que condicionam a solução SIGMUN.

Eles deverão ser considerados desde a arquitetura e não apenas durante os testes finais.

Requisitos críticos de segurança, disponibilidade, desempenho, continuidade, privacidade e integridade deverão possuir critérios de aceitação e evidências objetivas.

O conjunto de Requisitos Funcionais e Não Funcionais deverá constituir a referência formal para especificação, desenvolvimento, testes, homologação e evolução do SIGMUN.

---

# Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 2026-08-11 | Criação do padrão corporativo de Requisitos Não Funcionais |

---

**Documento:** Requisitos-Nao-Funcionais-v1.0.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
```
