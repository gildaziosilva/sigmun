# 030 — Roadmap de Implementação dos Domínios do SIGMUN

**Projeto:** SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA  
**Classificação da Informação:** Pública  
**Documento:** Roadmap de Implementação dos Domínios  
**Código:** 030  
**Versão:** 1.0  
**Status:** Vigente  
**Data:** 2026-08-20  
**Responsável:** Arquitetura Corporativa do SIGMUN

---

## 1. Objetivo

Estabelecer a ordem estratégica, arquitetural e incremental de implementação dos domínios do SIGMUN, definindo ondas de evolução que permitam:

- reduzir riscos técnicos e organizacionais;
- validar a arquitetura progressivamente;
- priorizar dependências estruturais;
- evitar desenvolvimento isolado de módulos;
- maximizar reutilização de componentes e serviços;
- estabelecer padrões corporativos antes da expansão;
- garantir rastreabilidade entre negócio, requisitos, arquitetura, dados, serviços, segurança, testes e operação;
- permitir evolução incremental do SIGMUN sem comprometer sua arquitetura corporativa.

Este documento não substitui o `Mapa-de-Dominios.md`. Ele transforma a visão arquitetural dos domínios em uma estratégia de implementação.

---

# 2. Princípios do Roadmap

A implementação dos domínios seguirá os seguintes princípios:

1. **Arquitetura antes do código.**
2. **Domínio antes de módulo.**
3. **Dependências antes de funcionalidades isoladas.**
4. **Reutilização antes de duplicação.**
5. **Dados como ativo corporativo.**
6. **Segurança desde a concepção.**
7. **Auditoria como requisito estrutural.**
8. **Integração como capacidade nativa.**
9. **Testabilidade desde o início.**
10. **Implementação incremental.**
11. **Automação sempre que possível.**
12. **Observabilidade desde os primeiros serviços.**
13. **Documentação como parte do produto.**
14. **Rastreabilidade ponta a ponta.**
15. **Evolução controlada por versionamento.**

---

# 3. Linha de Base Arquitetural

O SIGMUN possui atualmente **32 domínios consolidados**.

A implementação será organizada em ondas arquiteturais.

O domínio:

**DOM-COMPRAS-001 — Gestão de Compras e Contratações**

será utilizado como **primeiro domínio-piloto de implementação**, permitindo validar:

- arquitetura de domínio;
- arquitetura de serviços;
- modelo de dados;
- padrões de API;
- autenticação e autorização;
- auditoria;
- testes;
- observabilidade;
- CI/CD;
- documentação técnica;
- padrões de desenvolvimento;
- estrutura de aplicações;
- integração entre domínios.

O sucesso do primeiro domínio será utilizado como referência para a expansão dos demais.

---

# 4. Estratégia Geral

A implementação será realizada em ondas.

```
FUNDAÇÃO
    │
    ▼
DOM-COM
    │
    ▼
DOMÍNIOS MESTRES E TRANSVERSAIS
    │
    ▼
NÚCLEO ADMINISTRATIVO E ECONÔMICO-FINANCEIRO
    │
    ▼
DOMÍNIOS TERRITORIAIS E FINALÍSTICOS
    │
    ▼
ATENDIMENTO, INTELIGÊNCIA, MOBILIDADE E INFRAESTRUTURA

As ondas não significam que todos os domínios de uma determinada onda serão necessariamente desenvolvidos simultaneamente.

A ordem representa prioridade arquitetural e dependência.

---

# 5. Onda 0 — Fundação do SIGMUN

Objetivo

Estabelecer a infraestrutura arquitetural e técnica necessária para o desenvolvimento dos domínios.

Principais componentes
repositório Git;
estratégia de branches;
versionamento;
ambiente de desenvolvimento;
ambiente de testes;
configuração de banco de dados;
estrutura de aplicações;
configuração de containers;
CI/CD;
logging;
observabilidade;
autenticação;
autorização;
configuração;
gestão de segredos;
testes automatizados;
padrões de API;
documentação técnica.
Resultado esperado

Um framework corporativo executável capaz de receber o primeiro domínio.

---

# 6. Onda 1 — DOM-COMPRAS-001

Domínio

Gestão de Compras e Contratações

Objetivo

Implementar o primeiro domínio operacional do SIGMUN.

Artefatos já produzidos

O domínio possui atualmente os seguintes artefatos:

000-Dominio
001-Mapa-de-Atores
002-Mapa-de-Capacidades
003-Mapa-de-Processos
004-Mapa-de-Servicos
005-Casos-de-Uso
006-Historias-de-Usuario
007-Regras-de-Negocio
008-Requisitos-Funcionais
009-Requisitos-Nao-Funcionais
010-Especificacoes
011-Criterios-de-Aceitacao
012-Matriz-de-Rastreabilidade
013-Modelo-de-Dados
014-Modelo-de-Integracao
015-Arquitetura-de-Servicos
016-Modelo-de-Seguranca
017-Modelo-de-Auditoria
018-Plano-de-Testes
019-Casos-de-Teste
020-Plano-de-Implantacao
021-Checklist-de-Prontidao-para-Producao
022-Plano-de-Migracao-de-Dados
023-Plano-de-Treinamento
024-Plano-de-Suporte-e-Operacao
025-Estrutura-Tecnica
026-Modelo-de-Dominio
Objetivo técnico

Transformar os artefatos arquiteturais em implementação executável.

Primeiras capacidades técnicas
cadastro e gestão de processos de contratação;
fornecedores;
itens;
solicitações;
planejamento;
processos administrativos;
documentos;
contratos;
empenhos e integrações financeiras;
acompanhamento;
auditoria;
consultas;
indicadores.
Critério de conclusão

O domínio somente será considerado implementado quando possuir:

código;
banco de dados;
APIs;
regras de negócio;
testes;
segurança;
auditoria;
documentação;
observabilidade;
implantação automatizada;
homologação;
operação controlada.

---

# 7. Onda 2 — Domínios Mestres e Transversais

Após a validação do DOM-COM, serão priorizados os domínios que fornecem informações e serviços compartilhados.

# 7.1 DOM-CUM — Cadastro Único Municipal

Responsável por informações corporativas compartilhadas.

Prioridade:

Muito alta

Dependências:

praticamente todos os demais domínios.

# 7.2 DOM-IDN — Identidade e Acesso

Responsável por:

identidade;
autenticação;
autorização;
perfis;
papéis;
permissões;
identidade institucional.

Prioridade:

Muito alta

# 7.3 DOM-DAD — Governança de Dados

Responsável por:

governança;
qualidade;
catálogo;
metadados;
linhagem;
políticas;
domínio de dados;
compartilhamento.

Prioridade:

Muito alta

# 7.4 DOM-MET — Gestão de Metadados

Responsável por:

metadados;
classificações;
taxonomias;
padrões corporativos;
referências semânticas.

Prioridade:

Alta

# 7.5 DOM-SEG — Segurança da Informação

Responsável por:

políticas;
controles;
incidentes;
segurança;
proteção;
monitoramento.

Prioridade:

Alta

# 7.6 DOM-GDO — Gestão Documental

Responsável por:

documentos;
classificação;
versionamento;
retenção;
arquivamento;
temporalidade.

Prioridade:

Alta

# 7.7 DOM-INT — Integrações

Responsável pela arquitetura corporativa de integração.

Inclui:

APIs;
eventos;
mensageria;
integrações externas;
interoperabilidade.

Prioridade:

Alta

# 7.8 DOM-GOV — Governança

Responsável por:

governança;
decisões;
políticas;
conformidade;
gestão institucional.

Prioridade:

Alta

# 7.9 DOM-IND — Indicadores e Inteligência

Responsável por:

indicadores;
métricas;
painéis;
analytics;
inteligência municipal.

Prioridade:

Média/Alta

---

# 8. Onda 3 — Núcleo Administrativo e Econômico-Financeiro

Nesta onda serão implementados os domínios diretamente relacionados à administração municipal e ao ciclo econômico-financeiro.

Domínios
DOM-ORC — Orçamento
DOM-CON — Contabilidade
DOM-TRI — Tributos
DOM-PES — Pessoas
DOM-CPT — Patrimônio
DOM-PAT — Patrimônio
DOM-FRO — Frotas
DOM-PLA — Planejamento

A ordem interna será refinada após a consolidação das dependências entre dados, processos e serviços.

---

# 9. Onda 4 — Domínios Territoriais e Finalísticos

Após a consolidação do núcleo administrativo e econômico-financeiro, serão priorizados os domínios finalísticos.

Domínios
DOM-TEL — Território
DOM-IMO — Imobiliário
DOM-GEO — Geoprocessamento
DOM-OBR — Obras
DOM-SAU — Saúde
DOM-EDU — Educação
DOM-ASS — Assistência Social
DOM-MAM — Meio Ambiente
DOM-DEC — Defesa Civil

A implantação seguirá uma estratégia orientada por:

criticidade;
impacto social;
dependências;
maturidade;
disponibilidade de dados;
capacidade institucional;
capacidade técnica;
prioridade estratégica municipal.

---

# 10. Onda 5 — Atendimento, Inteligência, Mobilidade e Infraestrutura

Domínios
DOM-ATE — Atendimento
DOM-OUV — Ouvidoria
DOM-ANA — Analytics
DOM-MOB — Mobilidade e Serviços de Campo
DOM-INF — Infraestrutura Tecnológica

Esta onda consolida a interação do SIGMUN com:

cidadãos;
servidores;
gestores;
dispositivos móveis;
serviços externos;
infraestrutura tecnológica;
inteligência municipal.

---

# 11. Ordem Consolidada de Implementação

A sequência estratégica inicial será:

Ordem	Domínio	Prioridade
0	Fundação do SIGMUN	Crítica
1	DOM-COM	Crítica
2	DOM-CUM	Crítica
3	DOM-IDN	Crítica
4	DOM-DAD	Crítica
5	DOM-MET	Alta
6	DOM-SEG	Alta
7	DOM-GDO	Alta
8	DOM-INT	Alta
9	DOM-GOV	Alta
10	DOM-IND	Alta
11	DOM-ORC	Alta
12	DOM-CON	Alta
13	DOM-TRI	Alta
14	DOM-PES	Alta
15	DOM-PAT	Alta
16	DOM-FRO	Média/Alta
17	DOM-PLA	Média/Alta
18	DOM-TEL	Média/Alta
19	DOM-IMO	Média/Alta
20	DOM-GEO	Média/Alta
21	DOM-OBR	Média/Alta
22	DOM-SAU	Alta
23	DOM-EDU	Alta
24	DOM-ASS	Alta
25	DOM-MAM	Média
26	DOM-DEC	Média
27	DOM-ATE	Alta
28	DOM-OUV	Alta
29	DOM-ANA	Alta
30	DOM-MOB	Média/Alta
31	DOM-INF	Alta

A ordem acima é uma linha de base arquitetural. A sequência de execução poderá ser alterada por ADR, desde que as dependências e impactos sejam formalmente registrados.

---

# 12. Critérios para Avançar uma Onda

Uma onda somente deverá avançar quando os seguintes critérios forem atendidos:

arquitetura aprovada;
requisitos rastreáveis;
modelo de domínio definido;
modelo de dados definido;
integrações identificadas;
segurança definida;
auditoria definida;
testes planejados;
infraestrutura disponível;
documentação atualizada;
critérios de aceitação definidos;
riscos avaliados;
plano de implantação aprovado.

---

# 13. Critérios de Prontidão de um Domínio

Um domínio estará pronto para implementação quando possuir:

Mapa de Atores
       ↓
Mapa de Capacidades
       ↓
Mapa de Processos
       ↓
Mapa de Serviços
       ↓
Casos de Uso
       ↓
Histórias de Usuário
       ↓
Regras de Negócio
       ↓
Requisitos
       ↓
Especificações
       ↓
Critérios de Aceitação
       ↓
Rastreabilidade
       ↓
Modelo de Dados
       ↓
Integrações
       ↓
Serviços
       ↓
Segurança
       ↓
Auditoria
       ↓
Testes
       ↓
Estrutura Técnica
       ↓
Modelo de Domínio
       ↓
IMPLEMENTAÇÃO

---

# 14. Estratégia de Implementação Incremental

Cada domínio deverá ser desenvolvido em ciclos.

Ciclo 1 — Fundação

Infraestrutura e padrões.

Ciclo 2 — Núcleo do domínio

Entidades, agregados e regras essenciais.

Ciclo 3 — Aplicação

Casos de uso e serviços de aplicação.

Ciclo 4 — Interface

APIs e interfaces de usuário.

Ciclo 5 — Integrações

Comunicação com outros domínios e sistemas externos.

Ciclo 6 — Segurança e Auditoria

Controles, autorização, logs e rastreabilidade.

Ciclo 7 — Testes

Testes unitários, integração, aceitação e segurança.

Ciclo 8 — Homologação

Validação com usuários e responsáveis pelo negócio.

Ciclo 9 — Implantação

Publicação controlada.

Ciclo 10 — Operação

Monitoramento, suporte e evolução.

---

# 15. Estratégia de Dependências

Nenhum domínio deverá assumir diretamente estruturas internas de outro domínio.

A comunicação deverá ocorrer por meio de:

APIs;
serviços;
eventos;
contratos de integração;
modelos compartilhados formalmente definidos;
mecanismos de interoperabilidade.

Deve ser evitado:

acesso direto ao banco de outro domínio;
duplicação de cadastros mestres;
regras de negócio copiadas;
dependências ocultas;
integrações não documentadas.

---

# 16. Primeiro Marco Técnico

O primeiro grande marco do roadmap será:

M1 — Primeiro domínio executável do SIGMUN

Representado por:

DOM-COMPRAS-001
        │
        ├── Backend
        ├── Banco de Dados
        ├── API
        ├── Segurança
        ├── Auditoria
        ├── Testes
        ├── Documentação
        ├── Observabilidade
        └── Implantação

O objetivo não é simplesmente produzir uma aplicação de compras.

O objetivo é produzir o primeiro domínio que valide o padrão de construção do SIGMUN.

---

# 17. Marco M2 — Framework Corporativo Reutilizável

Após a implementação inicial do DOM-COM, os componentes reutilizáveis deverão ser extraídos e consolidados.

Exemplos:

autenticação;
autorização;
auditoria;
usuários;
organizações;
documentos;
notificações;
eventos;
configuração;
logs;
observabilidade;
tratamento de erros;
paginação;
filtros;
versionamento;
APIs.

---

# 18. Marco M3 — Expansão dos Domínios Mestres

Após a validação do padrão técnico:

DOM-CUM
DOM-IDN
DOM-DAD
DOM-MET
DOM-SEG
DOM-GDO
DOM-INT
DOM-GOV
DOM-IND

serão progressivamente implementados e disponibilizados como serviços corporativos.

---

# 19. Marco M4 — Integração Corporativa

O SIGMUN deverá evoluir de:

domínios isolados

para:

ecossistema integrado de domínios

com:

APIs;
eventos;
serviços compartilhados;
dados mestres;
governança;
observabilidade;
segurança centralizada.

---

# 20. Marco M5 — Plataforma Municipal Integrada

O estado-alvo será:

                 SIGMUN
                   │
        ┌──────────┼──────────┐
        │          │          │
     Negócio      Dados     Serviços
        │          │          │
        └──────────┼──────────┘
                   │
              Integrações
                   │
        ┌──────────┼──────────┐
        │          │          │
     Governo    Cidadão    Sistemas

---

# 21. Governança do Roadmap

Alterações significativas na ordem de implementação deverão ser registradas como decisão arquitetural.

Devem ser considerados:

impacto;
dependências;
riscos;
custo;
capacidade institucional;
maturidade;
urgência;
legislação;
disponibilidade de dados;
impacto social;
estratégia municipal.

---

# 22. Rastreabilidade

Este documento deverá manter rastreabilidade com:

Mapa-de-Dominios.md;
000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md;
Plano-de-Trabalho.md;
ROADMAP.md;
ADRs;
documentação de cada domínio;
arquitetura corporativa;
requisitos;
modelos de dados;
arquitetura de serviços;
planos de implantação.

---

# 23. Indicadores do Roadmap

Serão acompanhados, entre outros:

Indicador	Objetivo
Domínios implementados	Medir evolução
Domínios em desenvolvimento	Medir execução
Domínios planejados	Medir backlog
Percentual de reutilização	Medir maturidade arquitetural
Cobertura de testes	Medir qualidade
Cobertura de rastreabilidade	Medir governança
Incidentes por domínio	Medir estabilidade
Disponibilidade	Medir operação
Tempo médio de entrega	Medir eficiência
Débito técnico	Medir sustentabilidade
Integrações ativas	Medir interoperabilidade

---

# 24. Riscos do Roadmap

Principais riscos:

desenvolvimento prematuro;
ausência de governança;
duplicação de dados;
acoplamento entre domínios;
falta de padronização;
dependência de fornecedores;
ausência de testes automatizados;
ausência de documentação;
crescimento descontrolado da complexidade;
implantação sem maturidade operacional.

---

# 25. Diretriz Final

O roadmap deverá ser tratado como instrumento vivo de governança arquitetural.

A implementação do SIGMUN não será conduzida pela quantidade de telas produzidas, mas pela capacidade de construir progressivamente:

domínios coesos, serviços reutilizáveis, dados governados, processos integrados, segurança estruturada e arquitetura sustentável.

O DOM-COMPRAS-001 será o primeiro domínio executável e servirá como referência arquitetural para os demais domínios do SIGMUN