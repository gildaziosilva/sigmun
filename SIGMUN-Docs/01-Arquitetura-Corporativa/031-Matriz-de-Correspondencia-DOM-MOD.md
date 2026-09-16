# 031 — Matriz de Correspondência DOM ↔ MOD

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Classificação da Informação:** Pública
**Documento:** Matriz de Correspondência entre Domínios e Módulos
**Código:** 031
**Versão:** 1.0
**Status:** Vigente
**Última atualização:** 2026-09-16
**Responsável:** Equipe SIGMUN

---

## 1. Objetivo

Este documento estabelece a correspondência formal entre os **Domínios Corporativos (`DOM-*`)** e os **Módulos de Aplicação (`sigmun_*`)** do SIGMUN, estabelecendo também a identidade modular proposta no padrão **`MOD-*`**.

A matriz tem como objetivo:

- registrar a relação entre domínio de negócio e módulo de aplicação;
- distinguir módulos efetivamente implementados de estruturas apenas preparadas;
- registrar evidências técnicas utilizadas para estabelecer a correspondência;
- separar ownership de dependências e referências documentais;
- fornecer uma base confiável para a futura organização documental `DOM → MOD → Capacidades → Artefatos técnicos`;
- apoiar a indexação documental e a recuperação de conhecimento pelo SIGMUN-AI/RAG;
- evitar a criação de módulos documentais sem correspondência técnica verificável.

---

## 2. Princípios

A matriz observa os seguintes princípios arquiteturais:

> **Um domínio representa uma unidade de negócio/documentação corporativa.**

> **Um módulo representa uma unidade modular implementável da aplicação, alinhada ao conceito de Bounded Context.**

> **Uma referência a outro domínio não caracteriza, por si só, ownership.**

> **Uma dependência técnica não altera a propriedade funcional do módulo.**

> **A existência de um diretório de módulo não significa que o módulo esteja implementado.**

Consequentemente, a correspondência DOM ↔ MOD deve ser estabelecida por evidências técnicas e não apenas por similaridade nominal.

---

## 3. Definições

### 3.1 DOM — Domínio Corporativo

`DOM-*` identifica uma unidade de negócio, conhecimento ou responsabilidade corporativa documentada pelo SIGMUN.

O domínio organiza:

- processos de negócio;
- conceitos;
- regras;
- requisitos;
- capacidades;
- documentos;
- responsabilidades;
- integrações;
- conhecimento corporativo.

---

### 3.2 MOD — Módulo de Aplicação

`MOD-*` representa a identidade arquitetural do módulo de aplicação correspondente a um domínio.

No código-fonte, o módulo é representado atualmente por um diretório:

```text
src/modules/sigmun_<modulo>

A documentação MOD-* representa a unidade modular correspondente, mas sua existência documental não implica que o módulo esteja implementado.

---

### 3.3 Ownership

Ownership significa que o módulo é responsável pela implementação funcional principal das capacidades pertencentes ao domínio.

A evidência de ownership pode incluir:

casos de uso;
entidades;
value objects;
serviços de domínio;
repositórios;
modelos de persistência;
routers;
schemas;
migrations;
registro no src/main.py;
APIs próprias;
documentação técnica explicitamente associada ao domínio.
3.4 Dependência

Dependência ocorre quando um módulo utiliza conceitos, serviços, mecanismos ou infraestrutura associados a outro domínio.

Exemplo:

sigmun_int
    ↓
utiliza mecanismos associados à segurança
    ↓
DOM-SEG

Isso não transforma sigmun_int em módulo proprietário de DOM-SEG.

3.5 Referência documental

Uma referência documental ou histórica ocorre quando um módulo, documento ou artefato menciona outro domínio por razões de:

histórico;
migração;
documentação;
compatibilidade;
contexto;
relacionamento funcional;
evolução arquitetural.

A referência não deve ser interpretada automaticamente como ownership.

4. Evidências utilizadas

A matriz foi estabelecida a partir da inspeção do repositório SIGMUN, considerando principalmente:

src/main.py
src/README.md
src/modules/*
src/sigmun.egg-info/PKG-INFO
alembic/versions/*

Também foram considerados:

routers registrados;
APIs;
casos de uso;
entidades;
value objects;
eventos;
repositórios;
modelos de banco;
tabelas SQLAlchemy;
migrations;
referências explícitas a DOM-*.
5. Matriz principal DOM ↔ MOD
5.1 Módulos implementados
DOM	Módulo de aplicação	MOD proposto	Status técnico	Evidências principais
DOM-COMPRAS-001	sigmun_compras	MOD-COMPRAS	Implementado	Casos de uso, entidades, repositórios, APIs, modelos de persistência, migrations e integração em src/main.py
DOM-CUM	sigmun_cadastro	MOD-CUM	Implementado	Casos de uso, entidades, VOs, repositórios, modelos de persistência, APIs, migration e integração em src/main.py
DOM-DAD	sigmun_dad	MOD-DAD	Implementado	Casos de uso, modelos de dados, APIs, persistência, migration e integração em src/main.py
DOM-GDO	sigmun_gdo	MOD-GDO	Implementado	Casos de uso, entidades, persistência, APIs, migrations e integração em src/main.py
DOM-IDN	sigmun_idn	MOD-IDN	Implementado	Casos de uso, entidade usuário, VOs, persistência, APIs, migration e integração em src/main.py
DOM-INT	sigmun_int	MOD-INT	Implementado	Casos de uso de integração, APIs, modelos, persistência, migration e integração em src/main.py
DOM-MET	sigmun_met	MOD-MET	Implementado	Casos de uso, modelos, APIs, persistência, migration e integração em src/main.py
DOM-SEG	sigmun_seg	MOD-SEG	Implementado	Casos de uso, modelos de segurança, APIs, persistência, migrations e integração em src/main.py
5.2 Módulos estruturalmente preparados

Os módulos abaixo possuem estrutura arquitetural em src/modules/, mas a inspeção realizada não encontrou implementação funcional correspondente.

DOM	Módulo de aplicação	MOD proposto	Status técnico	Evidência
DOM-ASS	sigmun_assistencia_social	MOD-ASS	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-EDU	sigmun_educacao	MOD-EDU	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-FRO	sigmun_frotas	MOD-FRO	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-OBR	sigmun_obras	MOD-OBR	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-OUV	sigmun_ouvidoria	MOD-OUV	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-PLA	sigmun_planejamento	MOD-PLA	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-SAU	sigmun_saude	MOD-SAU	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
DOM-TRI	sigmun_tributos	MOD-TRI	Preparado	Estrutura Clean Architecture presente; sem casos de uso, entidades, APIs, modelos ou migrations funcionais
5.3 Módulos ainda não determinados

Os módulos abaixo existem estruturalmente no código-fonte, porém a investigação realizada ainda não fornece evidências suficientes para estabelecer uma correspondência técnica definitiva com um DOM-*.

Módulo de aplicação	MOD potencial	Status da correspondência
sigmun_administracao	MOD-ADMINISTRAÇÃO	Não determinado
sigmun_agricultura	MOD-AGRICULTURA	Não determinado
sigmun_almoxarifado	MOD-ALMOXARIFADO	Não determinado
sigmun_contabilidade	MOD-CONTABILIDADE	Não determinado
sigmun_controladoria	MOD-CONTROLADORIA	Não determinado
sigmun_financas	MOD-FINANÇAS	Não determinado
sigmun_gabinete	MOD-GABINETE	Não determinado
sigmun_licitacoes	MOD-LICITAÇÕES	Não determinado
sigmun_patrimonio	MOD-PATRIMÔNIO	Não determinado
sigmun_procuradoria	MOD-PROCURADORIA	Não determinado
sigmun_rh	MOD-RH	Não determinado
sigmun_transparencia	MOD-TRANSPARÊNCIA	Não determinado

A ausência de correspondência determinada não significa que o módulo não tenha futuro correspondente. Significa apenas que a evidência técnica atualmente levantada não é suficiente para formalizar essa relação.

6. Resumo da situação atual

A situação identificada no repositório é:

Categoria	Quantidade
Módulos tecnicamente implementados	8
Módulos estruturalmente preparados	8
Módulos ainda não determinados	12
Total de módulos analisados	28

Dos 28 módulos existentes em src/modules/:

8  → implementação confirmada
8  → estrutura preparada
12 → correspondência ainda não determinada
7. Correspondência confirmada

A relação atualmente confirmada é:

DOM-COMPRAS-001
└── MOD-COMPRAS
    └── src/modules/sigmun_compras

DOM-CUM
└── MOD-CUM
    └── src/modules/sigmun_cadastro

DOM-DAD
└── MOD-DAD
    └── src/modules/sigmun_dad

DOM-GDO
└── MOD-GDO
    └── src/modules/sigmun_gdo

DOM-IDN
└── MOD-IDN
    └── src/modules/sigmun_idn

DOM-INT
└── MOD-INT
    └── src/modules/sigmun_int

DOM-MET
└── MOD-MET
    └── src/modules/sigmun_met

DOM-SEG
└── MOD-SEG
    └── src/modules/sigmun_seg
8. Dependências e referências que não representam ownership

A investigação identificou referências entre módulos e domínios que devem ser preservadas sem alterar a correspondência principal.

8.1 Integração e segurança

sigmun_int possui referências relacionadas a DOM-SEG.

A relação deve ser interpretada como:

MOD-INT
   │
   └── depende de mecanismos associados a
       MOD-SEG

e não como:

DOM-SEG
└── MOD-INT
8.2 Cadastro e identidade

sigmun_cadastro possui referências relacionadas a DOM-IDN.

A relação deve ser interpretada como dependência ou integração com identidade e acesso:

MOD-CUM
   │
   └── utiliza/referencia capacidades de
       MOD-IDN

A propriedade principal permanece:

DOM-CUM → MOD-CUM
DOM-IDN → MOD-IDN
8.3 Referências a DOM-COMPRAS-001

Foram encontradas referências a DOM-COMPRAS-001 em artefatos de outros módulos, incluindo:

sigmun_cadastro
sigmun_dad
sigmun_gdo
sigmun_idn
sigmun_met

Essas ocorrências não devem ser automaticamente classificadas como ownership.

A correspondência principal permanece:

DOM-COMPRAS-001 → MOD-COMPRAS

As demais ocorrências devem ser tratadas conforme seu contexto individual como:

dependência;
integração;
referência documental;
contexto histórico;
ou relacionamento funcional.
9. Critérios para criação futura de um MOD

A existência de um diretório src/modules/sigmun_* não é suficiente para declarar um módulo como implementado.

Um módulo poderá ser classificado como Implementado quando houver evidências técnicas suficientes, incluindo, conforme aplicável:

casos de uso;
entidades;
regras de domínio;
repositórios;
persistência;
APIs;
schemas;
migrations;
testes;
registro na aplicação;
documentação técnica;
correspondência inequívoca com o domínio corporativo.

A classificação não exige que todos os itens estejam completos para sempre. Ela exige evidência suficiente de que existe uma implementação funcional e integrada.

10. Estados de maturidade modular

A matriz adota os seguintes estados:

10.1 Não determinado

Existe um módulo ou referência potencial, mas não há evidência suficiente para estabelecer a correspondência DOM ↔ MOD.

10.2 Preparado

A estrutura modular foi criada, mas não há implementação funcional suficiente.

10.3 Em implementação

Existe implementação funcional parcial, porém o módulo ainda não atingiu o nível necessário para ser considerado consolidado.

10.4 Implementado

Existe implementação funcional identificável, persistência e/ou APIs quando aplicáveis, integração arquitetural e evidências suficientes de ownership.

10.5 Consolidado

Estado futuro destinado a módulos que, além de implementados, possuam documentação, testes, integração, observabilidade, segurança e demais critérios de maturidade estabelecidos pelo SIGMUN.

11. Relação com a documentação dos DOM

A partir desta matriz, a estrutura documental poderá evoluir para:

DOM
│
├── identidade e responsabilidade do domínio
├── processos
├── capacidades
├── requisitos
├── regras de negócio
│
└── MOD
    │
    ├── arquitetura
    ├── casos de uso
    ├── entidades
    ├── APIs
    ├── persistência
    ├── integrações
    ├── segurança
    ├── testes
    └── evidências

A matriz deste documento é a referência para estabelecer essa relação.

12. Relação com o SIGMUN-AI e RAG

A matriz também funciona como camada semântica para recuperação de conhecimento.

Uma consulta relacionada a um domínio poderá ser resolvida pela cadeia:

DOM
 ↓
MOD
 ↓
Capacidade
 ↓
Caso de uso
 ↓
Artefato técnico
 ↓
Evidência

Exemplo:

DOM-SEG
   ↓
MOD-SEG
   ↓
capacidades de segurança
   ↓
casos de uso
   ↓
API / persistência / testes

Isso permite que o SIGMUN-AI diferencie:

domínio corporativo;
módulo de aplicação;
capacidade;
dependência;
referência documental;
implementação real.

Essa distinção reduz o risco de o sistema inferir ownership apenas pela ocorrência textual de um código DOM-*.

13. Governança da matriz

A matriz deve ser atualizada quando ocorrer qualquer mudança relevante na relação entre domínio e módulo, incluindo:

criação de módulo;
implementação de módulo;
mudança de ownership;
criação de nova API;
criação de nova migration;
reorganização arquitetural;
decomposição ou consolidação de módulos;
alteração da fronteira de um Bounded Context;
mudança relevante na documentação corporativa.

Alterações devem ser acompanhadas de evidência técnica ou documental correspondente.

14. Regra para criação de índices DOM/MOD

Nenhum index.md de módulo deve ser criado com base apenas no nome de um diretório.

A geração dos índices deverá utilizar esta matriz como uma das fontes de verdade.

O processo deverá distinguir:

DOM existente
MOD confirmado
MOD preparado
MOD não determinado
dependências
referências

A geração de documentação não deve transformar automaticamente uma estrutura de código vazia em módulo implementado.

15. Estado da decisão arquitetural

A investigação realizada até 2026-09-16 permite estabelecer formalmente:

Os oito módulos atualmente integrados à aplicação constituem as correspondências DOM ↔ MOD tecnicamente confirmadas do SIGMUN.

Os oito módulos candidatos adicionais possuem estrutura arquitetural preparada, mas não possuem implementação funcional suficiente para serem classificados como módulos implementados.

Os doze módulos restantes permanecem sem correspondência técnica determinada até que novas evidências sejam levantadas.

Referências entre domínios e módulos não devem ser interpretadas como alteração de ownership sem evidência específica.

16. Próximos passos

Após a aprovação desta matriz, os próximos passos arquiteturais são:

validar este documento;
registrar a matriz no roadmap;
criar a estrutura documental MOD-* apenas para os módulos confirmados, quando apropriado;
definir o padrão documental de um MOD-*;
relacionar capacidades e casos de uso aos módulos;
projetar os index.md dos DOM;
projetar os index.md dos MOD;
validar a hierarquia para uso pelo SIGMUN-AI/RAG.
17. Histórico de alterações
Versão	Data	Alteração	Responsável
1.0	2026-09-16	Criação da matriz formal DOM ↔ MOD com base na análise do repositório	Equipe SIGMUN
