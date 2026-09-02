# Mapa de Serviços

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Negócio

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `Cadeia-de-Valor.md`
* `Mapa-de-Atores.md`
* `Mapa-de-Capacidades.md`
* `Mapa-de-Dominios.md`
* `Mapa-de-Processos.md`
* `Mapa-de-Secretarias.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`
* `013-Experiencia-do-Usuario.md`
* `014-Processos.md`
* `015-Relatorios-Indicadores-e-BI.md`

---

# 1. Finalidade

Este documento estabelece o **Mapa Corporativo de Serviços do SIGMUN**, organizando os serviços disponibilizados pelo Município e suportados pela administração municipal.

O Mapa de Serviços tem como finalidade:

* identificar os serviços municipais;
* organizar serviços por domínio;
* relacionar serviços às capacidades;
* relacionar serviços aos processos;
* identificar órgãos responsáveis;
* identificar unidades executoras;
* identificar usuários;
* identificar canais de atendimento;
* apoiar a transformação digital;
* apoiar o catálogo de serviços;
* apoiar requisitos;
* apoiar indicadores;
* apoiar a experiência do usuário.

---

# 2. Conceito de Serviço

Para fins do SIGMUN, um **serviço** é uma forma organizada de disponibilizar uma capacidade ou resultado a um usuário, cidadão, empresa, servidor, órgão público ou outra parte interessada.

O serviço representa aquilo que o usuário **recebe ou acessa**.

Portanto:

> **Processo representa como a organização trabalha. Serviço representa aquilo que é disponibilizado ao usuário.**

---

# 3. Princípio Fundamental

O SIGMUN deverá ser orientado a serviços.

A arquitetura deverá partir da seguinte lógica:

```text
Necessidade
    ↓
Serviço
    ↓
Processo
    ↓
Capacidade
    ↓
Domínio
    ↓
Organização
    ↓
Aplicações
    ↓
Dados
```

---

# 4. Serviço não é Processo

Um serviço e um processo possuem funções diferentes.

Exemplo:

```text
Serviço:
Solicitar Alvará

Processo:
Licenciamento

Subprocessos:
- Receber solicitação
- Analisar documentação
- Avaliar requisitos
- Realizar fiscalização
- Emitir decisão
```

O cidadão acessa o **serviço**.

A administração executa o **processo**.

---

# 5. Serviço não é Sistema

O usuário não deveria precisar conhecer qual sistema interno executa o serviço.

O SIGMUN deverá buscar:

```text
Cidadão
   ↓
Serviço
   ↓
SIGMUN
   ↓
Processos
   ↓
Sistemas e serviços internos
```

e não:

```text
Cidadão
   ↓
Sistema A
   ↓
Sistema B
   ↓
Sistema C
```

---

# 6. Serviço como Unidade de Valor

O serviço deverá ser analisado sob a perspectiva do valor entregue.

Exemplo:

```text
Entrada:
Necessidade do cidadão

        ↓

Serviço:
Solicitação de manutenção urbana

        ↓

Resultado:
Problema resolvido

        ↓

Valor:
Melhoria do espaço público
```

---

# 7. Categorias de Serviços

Os serviços poderão ser classificados em:

1. Serviços ao Cidadão;
2. Serviços às Empresas;
3. Serviços aos Servidores;
4. Serviços às Secretarias;
5. Serviços aos Gestores;
6. Serviços aos Órgãos de Controle;
7. Serviços Institucionais;
8. Serviços Digitais;
9. Serviços Internos;
10. Serviços de Informação.

---

# 8. Serviços ao Cidadão

Incluem serviços como:

* atendimento em saúde;
* matrícula escolar;
* emissão de documentos;
* solicitação de serviços urbanos;
* assistência social;
* licenciamento;
* emissão de certidões;
* protocolos;
* agendamentos;
* consultas;
* solicitações;
* reclamações;
* denúncias;
* ouvidoria.

---

# 9. Serviços às Empresas

Incluem:

* abertura e regularização;
* licenciamento;
* alvarás;
* consulta tributária;
* emissão de documentos;
* contratação pública;
* fornecedores;
* programas de incentivo;
* atendimento empresarial.

---

# 10. Serviços aos Servidores

Incluem:

* consulta funcional;
* solicitação de férias;
* afastamentos;
* benefícios;
* contracheques;
* atualização cadastral;
* capacitação;
* solicitações internas.

---

# 11. Serviços aos Gestores

Incluem:

* acompanhamento de indicadores;
* consultas gerenciais;
* relatórios;
* acompanhamento orçamentário;
* acompanhamento de contratos;
* gestão de riscos;
* gestão de processos;
* gestão de projetos.

---

# 12. Serviços Institucionais

Incluem serviços destinados à própria administração.

Exemplos:

* protocolo;
* compras;
* licitações;
* contratos;
* patrimônio;
* gestão de pessoas;
* orçamento;
* contabilidade;
* gestão documental.

---

# 13. Serviços de Informação

São serviços que disponibilizam informações.

Exemplos:

* consulta de indicadores;
* consulta de processos;
* consulta de despesas;
* consulta de contratos;
* consulta de serviços;
* dados abertos;
* informações institucionais.

---

# 14. Serviços Digitais

São serviços que podem ser acessados por meios digitais.

Exemplos:

* portal web;
* aplicativo móvel;
* atendimento online;
* protocolo digital;
* assinatura eletrônica;
* notificações;
* consultas;
* agendamentos.

---

# 15. Serviços Presenciais

Serviços que exigem ou podem ser realizados presencialmente.

Exemplos:

* atendimento em unidade;
* entrega de documentos;
* atendimento social;
* atendimento de saúde;
* atendimento educacional.

---

# 16. Serviços Omnichannel

Sempre que possível, um mesmo serviço deverá ser disponibilizado por múltiplos canais.

Exemplo:

```text
                    Serviço
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Portal         App          Presencial
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                    SIGMUN
```

O cidadão deverá perceber o serviço como único, independentemente do canal utilizado.

---

# 17. Canais de Serviço

Os serviços poderão utilizar:

* Portal Web;
* Aplicativo;
* Atendimento presencial;
* Telefone;
* E-mail;
* Mensageria;
* Totens;
* Integrações;
* APIs;
* dispositivos móveis de campo.

---

# 18. Serviços de Campo

O SIGMUN deverá suportar serviços executados diretamente no território.

Exemplos:

* fiscalização;
* manutenção urbana;
* visitas sociais;
* inspeções;
* coleta de evidências;
* atendimento domiciliar;
* vistorias.

Quando necessário, deverá ser utilizada arquitetura **Offline First**.

---

# 19. Catálogo de Serviços

O SIGMUN deverá manter um **Catálogo Corporativo de Serviços**.

Cada serviço deverá possuir:

* código;
* nome;
* descrição;
* objetivo;
* categoria;
* público-alvo;
* órgão responsável;
* unidade executora;
* domínio;
* capacidade;
* processo;
* canais;
* requisitos;
* documentos;
* prazo;
* custo;
* legislação;
* indicadores;
* status.

---

# 20. Código do Serviço

Cada serviço deverá possuir um identificador único.

Padrão:

```text
SRV-001
SRV-002
SRV-003
```

Os códigos deverão permanecer estáveis durante o ciclo de vida do serviço.

A alteração do nome do serviço não deverá necessariamente alterar seu identificador.

---

# 21. Modelo de Registro de Serviço

Modelo corporativo:

```markdown
## SRV-XXX – Nome do Serviço

**Código:** SRV-XXX

**Nome:** Nome oficial.

**Descrição:** Descrição do serviço.

**Objetivo:** Resultado esperado.

**Categoria:** Cidadão / Empresa / Servidor / Interno / Informação.

**Público-alvo:** Usuários.

**Órgão responsável:** Organização.

**Unidade executora:** Unidade.

**Domínio:** Domínio.

**Capacidade:** Capacidade.

**Processo:** Processo.

**Subprocesso:** Subprocesso, quando aplicável.

**Canais:** Canais disponíveis.

**Requisitos:** Requisitos para utilização.

**Documentos necessários:** Documentos.

**Prazo:** Prazo estimado ou legal.

**Custo:** Gratuito / Taxa / Valor.

**Legislação:** Base legal.

**Dados utilizados:** Dados.

**Dados produzidos:** Dados.

**Integrações:** Sistemas externos.

**Indicadores:** Indicadores.

**Criticidade:** Baixa / Média / Alta / Crítica.

**Maturidade digital:** Nível.

**Status:** Planejado / Ativo / Suspenso / Encerrado.

**Observações:** Informações adicionais.
```

---

# 22. Serviço e Usuário

Todo serviço deverá identificar seu público.

Possíveis públicos:

* cidadão;
* empresa;
* servidor;
* fornecedor;
* gestor;
* órgão público;
* organização social;
* visitante;
* outro usuário autorizado.

---

# 23. Serviço e Jornada do Usuário

O serviço deverá ser analisado a partir da jornada do usuário.

Modelo:

```text
Necessidade
    ↓
Descoberta
    ↓
Solicitação
    ↓
Identificação
    ↓
Execução
    ↓
Acompanhamento
    ↓
Resultado
    ↓
Avaliação
```

---

# 24. Serviço e Experiência do Usuário

Os serviços deverão observar:

* simplicidade;
* clareza;
* acessibilidade;
* transparência;
* previsibilidade;
* baixo esforço;
* segurança;
* comunicação adequada.

---

# 25. Serviço e Processo

Cada serviço deverá possuir um processo responsável por sua execução.

Exemplo:

```text
SRV-001 – Solicitação de Iluminação Pública
        ↓
PRC-ATE-001 – Solicitação de Serviço
        ↓
PRC-TER-XXX – Manutenção Urbana
```

---

# 26. Serviço e Capacidade

O serviço deverá utilizar uma ou mais capacidades.

Exemplo:

```text
Serviço:
Licenciamento Ambiental

Capacidades:
- Analisar Licenciamento
- Fiscalizar
- Emitir Autorização
- Gerenciar Documentos
```

---

# 27. Serviço e Domínio

Cada serviço deverá possuir relacionamento com um domínio corporativo.

Exemplo:

| Serviço            | Domínio                   |
| ------------------ | ------------------------- |
| Matrícula Escolar  | Educação                  |
| Atendimento Médico | Saúde                     |
| Licenciamento      | Meio Ambiente             |
| Alvará             | Desenvolvimento Econômico |
| IPTU               | Tributação                |

---

# 28. Serviço e Organização

Cada serviço deverá possuir:

* órgão responsável;
* unidade executora;
* responsáveis;
* participantes.

Exemplo:

```text
Serviço
   ↓
Secretaria
   ↓
Unidade
   ↓
Servidor/Papel
```

---

# 29. Serviço Intersecretarial

Um serviço poderá envolver diversas secretarias.

Exemplo:

```text
Serviço:
Programa de Atendimento Social Integrado

       ┌───────────────┐
       ↓               ↓
 Assistência        Saúde
       │               │
       └───────┬───────┘
               ↓
            Educação
```

O serviço deverá possuir um responsável institucional principal, quando necessário.

---

# 30. Serviço Compartilhado

Serviços corporativos poderão ser utilizados por várias secretarias.

Exemplos:

* protocolo;
* gestão documental;
* gestão de pessoas;
* compras;
* patrimônio;
* identidade;
* notificações.

---

# 31. Serviço Público Digital

Um serviço digital deverá possuir:

* identificação digital;
* autenticação;
* formulário;
* validações;
* acompanhamento;
* notificações;
* resultado;
* histórico.

---

# 32. Serviço Digital Nível 1

**Informação digital**

O cidadão pode consultar informações.

Exemplos:

* endereço;
* requisitos;
* horário;
* legislação;
* custos.

---

# 33. Serviço Digital Nível 2

**Interação digital**

O cidadão inicia uma solicitação.

Exemplos:

* formulário;
* protocolo;
* agendamento;
* consulta.

---

# 34. Serviço Digital Nível 3

**Transação digital**

O serviço é executado integralmente ou predominantemente de forma digital.

Exemplos:

* emissão de certidão;
* pagamento;
* autorização digital;
* documento eletrônico.

---

# 35. Serviço Digital Nível 4

**Serviço proativo**

O município antecipa uma necessidade ou oferece automaticamente um serviço.

Exemplos:

* alertas;
* renovação;
* notificações;
* benefícios identificados automaticamente.

---

# 36. Serviço Inteligente

Um serviço poderá utilizar dados e IA para melhorar:

* classificação;
* encaminhamento;
* previsão;
* personalização;
* detecção de inconsistências;
* priorização.

A utilização de IA deverá observar governança, segurança, proteção de dados e supervisão humana quando necessária.

---

# 37. Serviço Proativo

O SIGMUN deverá evoluir progressivamente de:

```text
Cidadão solicita
      ↓
Prefeitura responde
```

para:

```text
Sistema identifica necessidade
      ↓
Prefeitura antecipa
      ↓
Cidadão recebe
```

sempre respeitando a legislação e os direitos dos usuários.

---

# 38. Requisitos do Serviço

Cada serviço deverá identificar:

* requisitos legais;
* requisitos administrativos;
* documentos;
* condições;
* critérios de elegibilidade;
* autenticação necessária.

---

# 39. Documentos Necessários

Os documentos deverão ser identificados de forma estruturada.

Exemplo:

```text
Serviço:
Alvará

Documentos:
- Documento de identificação
- Comprovante
- Cadastro
- Projeto
```

Quando possível, o SIGMUN deverá evitar exigir documentos que já estejam disponíveis em bases públicas integradas.

---

# 40. Princípio do Dado Único

O usuário não deverá fornecer novamente uma informação que o município já possua e possa utilizar legitimamente.

Aplicando:

> **Informar uma vez, utilizar de forma governada sempre que possível.**

---

# 41. Serviço e Cadastro Único Municipal

Os serviços deverão utilizar o **Cadastro Único Municipal** como referência quando aplicável.

Relacionamentos:

```text
Pessoa
   ↓
Cadastro
   ↓
Serviço
   ↓
Processo
```

---

# 42. Serviço e Notificações

Os serviços poderão utilizar:

* notificações;
* alertas;
* mensagens;
* e-mail;
* SMS;
* aplicativo;
* outros canais autorizados.

---

# 43. Serviço e Protocolo

Serviços que demandem tramitação deverão gerar protocolo ou identificador rastreável.

O usuário deverá poder acompanhar:

* número;
* situação;
* etapas;
* responsável, quando apropriado;
* prazo;
* resultado.

---

# 44. Serviço e SLA

Quando aplicável, cada serviço deverá possuir prazo de atendimento.

Exemplo:

```text
Prazo legal: 15 dias
Prazo operacional: 10 dias
```

O SIGMUN deverá permitir acompanhamento do cumprimento.

---

# 45. Indicadores de Serviço

Os serviços deverão possuir indicadores adequados.

Exemplos:

* quantidade de solicitações;
* tempo médio;
* tempo mediano;
* taxa de conclusão;
* taxa de abandono;
* taxa de retrabalho;
* taxa de erro;
* satisfação;
* custo;
* atendimento dentro do prazo.

---

# 46. Indicadores de Experiência

Poderão ser utilizados:

* satisfação;
* facilidade;
* esforço do usuário;
* taxa de resolução;
* reclamações;
* reincidência;
* tempo percebido.

---

# 47. Custo do Serviço

Quando possível, o SIGMUN deverá permitir estimar:

* custo por atendimento;
* custo por solicitação;
* custo por usuário;
* custo operacional;
* custo tecnológico.

Isso permitirá relacionar:

```text
Custo
   ↓
Serviço
   ↓
Resultado
   ↓
Valor Público
```

---

# 48. Serviços Gratuitos e Remunerados

O catálogo deverá informar se o serviço é:

* gratuito;
* sujeito a taxa;
* sujeito a tarifa;
* sujeito a preço público;
* outro modelo legalmente aplicável.

---

# 49. Serviço e Transparência

As informações públicas sobre serviços deverão ser disponibilizadas de maneira acessível.

Deverão ser divulgados, quando aplicável:

* descrição;
* requisitos;
* prazo;
* custo;
* canais;
* legislação;
* situação.

Aplicando:

> **Transparência por padrão.**

---

# 50. Serviço e Classificação da Informação

Informações utilizadas pelo serviço deverão ser classificadas conforme a política corporativa.

A classificação não deverá ser determinada simplesmente pelo fato de o serviço ser público ou privado.

Aplicando:

> **Classificação da Informação por política.**

---

# 51. Serviço e Segurança

Todo serviço deverá considerar:

* autenticação;
* autorização;
* integridade;
* confidencialidade;
* disponibilidade;
* rastreabilidade.

Aplicando:

> **Segurança por princípio.**

---

# 52. Serviço e Proteção de Dados

Serviços que tratem dados pessoais deverão observar:

* finalidade;
* necessidade;
* adequação;
* base legal;
* segurança;
* direitos dos titulares;
* retenção.

---

# 53. Serviço e Acessibilidade

Os serviços digitais deverão buscar conformidade com padrões de acessibilidade.

Deverão considerar:

* pessoas com deficiência;
* linguagem clara;
* dispositivos móveis;
* diferentes níveis de letramento digital;
* limitações de conectividade.

---

# 54. Serviço e Inclusão Digital

O município deverá evitar que a digitalização crie uma barreira de acesso.

Sempre que necessário, deverão existir canais alternativos:

```text
Digital
   +
Presencial
   +
Assistido
```

---

# 55. Serviço Offline

Quando o serviço for executado em campo ou em locais com conectividade limitada, poderá utilizar:

* armazenamento local;
* captura offline;
* sincronização posterior;
* controle de conflitos;
* evidências digitais.

---

# 56. Serviço e Integrações

Serviços poderão depender de:

* sistemas municipais;
* sistemas estaduais;
* sistemas federais;
* serviços externos;
* APIs;
* bases de dados.

As integrações deverão possuir governança.

---

# 57. Serviço e APIs

Serviços digitais poderão disponibilizar APIs para:

* integração;
* automação;
* consulta;
* interoperabilidade.

APIs públicas deverão observar a política de publicação e segurança.

---

# 58. Serviço e Aplicações

Um serviço poderá ser suportado por:

* módulo SIGMUN;
* aplicação externa;
* aplicativo móvel;
* portal;
* API;
* workflow.

O serviço deverá permanecer conceitualmente independente da aplicação.

---

# 59. Serviço e Arquitetura de Software

A arquitetura deverá preferir:

```text
Serviço
   ↓
API / Serviço de Aplicação
   ↓
Domínio
   ↓
Dados
```

sempre que tecnicamente adequado.

---

# 60. Serviço e Dados

Cada serviço deverá identificar:

### Dados de entrada

Informações necessárias para iniciar ou executar o serviço.

### Dados produzidos

Informações geradas pelo serviço.

### Dados derivados

Informações calculadas.

### Dados compartilhados

Informações disponibilizadas a outros processos ou órgãos.

---

# 61. Serviço e Documentos

Cada serviço deverá identificar:

* documentos recebidos;
* documentos produzidos;
* evidências;
* registros;
* documentos assinados;
* retenção;
* descarte.

---

# 62. Serviço e Auditoria

Serviços críticos deverão possuir trilha de auditoria.

Deverão ser rastreáveis, quando aplicável:

* solicitação;
* usuário;
* data;
* alterações;
* decisões;
* aprovações;
* resultado.

---

# 63. Serviço e Riscos

Cada serviço crítico deverá possuir avaliação de riscos.

Modelo:

```text
Serviço
   ↓
Risco
   ↓
Controle
   ↓
Indicador
   ↓
Monitoramento
```

---

# 64. Serviço e Continuidade

Serviços críticos deverão possuir requisitos de continuidade.

Deverão ser avaliados:

* disponibilidade;
* dependências;
* tempo máximo de interrupção;
* recuperação;
* contingência.

---

# 65. Criticidade do Serviço

Os serviços poderão ser classificados como:

| Nível | Classificação |
| ----- | ------------- |
| 1     | Baixa         |
| 2     | Moderada      |
| 3     | Alta          |
| 4     | Muito Alta    |
| 5     | Crítica       |

A criticidade deverá considerar o impacto da interrupção.

---

# 66. Maturidade Digital do Serviço

Os serviços poderão ser classificados:

| Nível | Maturidade           |
| ----- | -------------------- |
| 1     | Manual               |
| 2     | Informatizado        |
| 3     | Digital              |
| 4     | Integrado            |
| 5     | Inteligente/Proativo |

---

# 67. Priorização da Digitalização

A digitalização deverá considerar:

* volume;
* impacto público;
* criticidade;
* frequência;
* custo;
* tempo;
* satisfação;
* potencial de automação;
* potencial de integração;
* viabilidade técnica.

---

# 68. Matriz de Priorização

| Critério                | Peso sugerido |
| ----------------------- | ------------: |
| Impacto ao cidadão      |           25% |
| Volume                  |           15% |
| Criticidade             |           15% |
| Redução de custo        |           10% |
| Redução de tempo        |           10% |
| Potencial de automação  |           10% |
| Potencial de integração |           10% |
| Viabilidade             |            5% |

Os pesos poderão ser ajustados pela governança.

---

# 69. Jornada de Serviço

Cada serviço relevante poderá possuir uma jornada documentada.

Modelo:

```text
1. Descobrir
      ↓
2. Entender
      ↓
3. Solicitar
      ↓
4. Autenticar
      ↓
5. Fornecer informações
      ↓
6. Acompanhar
      ↓
7. Receber resultado
      ↓
8. Avaliar
```

---

# 70. Catálogo de Serviços por Domínio

Os serviços poderão ser agrupados por domínio.

### Saúde

* Atendimento;
* Vacinação;
* Farmácia;
* Regulação.

### Educação

* Matrícula;
* Transporte;
* Alimentação;
* Atendimento escolar.

### Assistência Social

* Cadastro;
* Benefícios;
* Atendimento;
* Acompanhamento.

### Finanças

* Tributos;
* Certidões;
* Parcelamentos;
* Consulta fiscal.

### Obras

* Solicitação de manutenção;
* Licenciamento;
* Vistorias.

---

# 71. Catálogo de Serviços por Público

Outra visão poderá organizar serviços por público.

### Cidadão

Serviços de acesso direto à população.

### Empresa

Serviços relacionados à atividade econômica.

### Servidor

Serviços funcionais.

### Gestor

Serviços gerenciais.

### Órgãos Públicos

Serviços institucionais e de integração.

---

# 72. Catálogo de Serviços por Canal

Poderá existir uma visão:

```text
Serviços
 ├── Portal
 ├── Aplicativo
 ├── Presencial
 ├── Telefone
 ├── API
 └── Campo
```

---

# 73. Catálogo de Serviços por Maturidade

Poderá existir uma visão:

```text
Manual
   ↓
Informatizado
   ↓
Digital
   ↓
Integrado
   ↓
Inteligente
```

Isso permitirá construir um plano de transformação digital.

---

# 74. Relação com o Mapa de Capacidades

O serviço deverá ser sustentado por capacidades.

```text
Serviço
   ↓
Capacidade
   ↓
Processo
```

Essa relação permitirá identificar capacidades insuficientes para determinado serviço.

---

# 75. Relação com o Mapa de Processos

Cada serviço deverá possuir pelo menos um processo relacionado.

```text
Serviço
   ↓
Processo
   ↓
Atividades
   ↓
Resultado
```

---

# 76. Relação com o Mapa de Secretarias

Cada serviço deverá identificar o órgão responsável e as unidades envolvidas.

```text
Serviço
   ↓
Órgão
   ↓
Unidade
   ↓
Responsável
```

---

# 77. Relação com o Mapa de Atores

Os serviços deverão identificar os atores envolvidos:

* usuário;
* cidadão;
* servidor;
* gestor;
* fornecedor;
* órgão externo.

---

# 78. Relação com a Cadeia de Valor

A relação deverá ser:

```text
Cadeia de Valor
      ↓
Valor Público
      ↓
Serviços
      ↓
Resultados
```

---

# 79. Relação com o Catálogo Corporativo do Conhecimento

Cada serviço deverá estar relacionado ao conhecimento corporativo correspondente.

```text
Serviço
   ↓
Conceitos
   ↓
Termos
   ↓
Regras
   ↓
Documentos
   ↓
Dados
```

---

# 80. Relação com Requisitos

Todo requisito funcional relevante deverá possuir rastreabilidade até o serviço que suporta.

Modelo:

```text
Serviço
   ↓
Necessidade
   ↓
Requisito
   ↓
Implementação
   ↓
Teste
```

---

# 81. Relação com Indicadores

Cada serviço deverá possuir indicadores adequados ao seu objetivo.

```text
Serviço
   ↓
Indicador
   ↓
Meta
   ↓
Resultado
   ↓
Avaliação
```

---

# 82. Serviço e Observatório Municipal Inteligente

Os serviços deverão fornecer dados para o futuro **Observatório Municipal Inteligente**, permitindo acompanhar:

* demanda;
* atendimento;
* desempenho;
* distribuição territorial;
* custos;
* satisfação;
* resultados.

O Observatório deverá funcionar como camada de análise e transparência sobre os serviços municipais.

---

# 83. Serviços e Dados Abertos

Quando possível e legalmente permitido, dados agregados sobre os serviços poderão ser disponibilizados como dados abertos.

Exemplos:

* quantidade de atendimentos;
* tempo médio;
* distribuição territorial;
* taxa de conclusão;
* indicadores de desempenho.

---

# 84. Princípio de Reutilização

Um mesmo serviço deverá ser reutilizável por diferentes canais e aplicações.

Exemplo:

```text
             Serviço
                │
      ┌─────────┼─────────┐
      ↓         ↓         ↓
    Portal     App       API
```

A lógica de negócio não deverá ser duplicada desnecessariamente.

---

# 85. Princípio de Composição

Serviços poderão ser compostos a partir de outros serviços.

Exemplo:

```text
Serviço:
Abertura de Empresa

      ↓

Consulta Cadastral
      +
Consulta Tributária
      +
Licenciamento
      +
Emissão de Alvará
```

---

# 86. Princípio de Interoperabilidade

Os serviços deverão ser projetados para integração sempre que necessário.

Deverão ser consideradas:

* APIs;
* eventos;
* padrões de dados;
* identificadores;
* autenticação;
* interoperabilidade governamental.

---

# 87. Governança do Catálogo de Serviços

O catálogo deverá possuir:

* proprietário;
* responsável pela manutenção;
* fonte oficial;
* versão;
* status;
* data de atualização.

---

# 88. Ciclo de Vida do Serviço

Os serviços poderão seguir:

```text
Identificado
    ↓
Analisado
    ↓
Projetado
    ↓
Aprovado
    ↓
Implementado
    ↓
Disponibilizado
    ↓
Monitorado
    ↓
Melhorado
    ↓
Descontinuado
```

---

# 89. Mudança de Serviço

Alterações relevantes deverão avaliar impacto sobre:

* usuários;
* processos;
* requisitos;
* dados;
* aplicações;
* integrações;
* legislação;
* indicadores;
* comunicação.

---

# 90. Descontinuação

Um serviço poderá ser descontinuado quando:

* deixar de possuir fundamento legal;
* for substituído;
* for incorporado a outro;
* deixar de ser necessário;
* houver decisão institucional.

O histórico deverá ser preservado.

---

# 91. Histórico do Serviço

O SIGMUN deverá preservar:

* versões;
* mudanças;
* responsáveis;
* atos legais;
* alterações de processo;
* alterações de canal;
* alterações de requisitos.

---

# 92. Qualidade dos Serviços

A qualidade deverá considerar:

* eficácia;
* eficiência;
* acessibilidade;
* disponibilidade;
* confiabilidade;
* segurança;
* satisfação;
* tempo de resposta.

---

# 93. Indicadores de Qualidade

Exemplos:

* SLA cumprido;
* taxa de resolução;
* taxa de erro;
* satisfação;
* reclamações;
* tempo médio;
* custo;
* disponibilidade.

---

# 94. Serviços Críticos

Serviços críticos deverão possuir:

* classificação;
* responsável;
* riscos;
* controles;
* indicadores;
* plano de continuidade;
* plano de recuperação.

---

# 95. Serviços e Gestão de Mudanças

Mudanças relevantes em serviços deverão ser comunicadas aos usuários.

Poderão incluir:

* alteração de requisitos;
* alteração de prazo;
* alteração de canal;
* alteração de custo;
* alteração de legislação.

---

# 96. Publicação do Catálogo

O catálogo público deverá apresentar, quando aplicável:

* nome;
* descrição;
* público;
* requisitos;
* documentos;
* prazo;
* custo;
* canal;
* legislação;
* acompanhamento.

Informações internas não deverão ser publicadas automaticamente.

---

# 97. Segurança da Publicação

A publicação deverá obedecer:

> **Aberto sempre que possível, restrito sempre que necessário.**

A informação pública deverá ser separada de informações internas, operacionais ou protegidas.

---

# 98. Modelo de Arquitetura de Serviço

A arquitetura deverá buscar:

```text
              USUÁRIO
                 │
                 ↓
             SERVIÇO
                 │
        ┌────────┴────────┐
        ↓                 ↓
      CANAL            IDENTIDADE
        │                 │
        └────────┬────────┘
                 ↓
              PROCESSO
                 ↓
             CAPACIDADE
                 ↓
              DOMÍNIO
                 ↓
          DADOS / REGRAS
                 ↓
             SISTEMAS
                 ↓
             RESULTADO
```

---

# 99. Modelo de Governança

Cada serviço relevante deverá possuir:

* **Dono do Serviço;**
* **Responsável pelo Processo;**
* **Responsável pela Capacidade;**
* **Responsável pelos Dados;**
* **Responsável pela Aplicação**, quando aplicável.

Esses papéis poderão ser exercidos por diferentes pessoas ou unidades.

---

# 100. Princípios Arquiteturais Relacionados

O Mapa de Serviços deverá observar os princípios fundamentais do SIGMUN:

> **Serviço antes da aplicação.**

> **Processo antes da automação.**

> **Valor público antes da tecnologia.**

> **Transparência por padrão.**

> **Segurança por princípio.**

> **Classificação da Informação por política.**

> **Aberto sempre que possível, restrito sempre que necessário.**

> **Informar uma vez, utilizar de forma governada sempre que possível.**

> **Digitalizar para simplificar, não para burocratizar.**

---

# 101. Disposições Finais

O **Mapa de Serviços** constitui uma visão corporativa dos serviços disponibilizados pelo Município e representa uma das principais interfaces entre a administração pública e seus usuários.

Sua função é estabelecer uma ligação clara entre:

```text
Necessidade do Usuário
        ↓
Serviço
        ↓
Processo
        ↓
Capacidade
        ↓
Domínio
        ↓
Organização
        ↓
Aplicação
        ↓
Dados
        ↓
Resultado
        ↓
Valor Público
```

O Mapa de Serviços deverá ser utilizado como referência para:

* arquitetura de negócio;
* experiência do usuário;
* transformação digital;
* catálogo de serviços;
* requisitos;
* desenvolvimento;
* indicadores;
* dados;
* integrações;
* gestão de processos;
* governança.

O catálogo deverá evoluir continuamente à medida que o SIGMUN avance na identificação, padronização, digitalização e integração dos serviços municipais.

---

**Documento:** `Mapa-de-Servicos.md`

**Última atualização:** `2026-08-11`

**Responsável:** `Equipe SIGMUN`

**Status da revisão:** `Vigente`
