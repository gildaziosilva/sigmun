# Mapa de Secretarias

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
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`
* `005-Arquitetura-de-Negocio.md`

---

# 1. Finalidade

Este documento estabelece o **Mapa Corporativo de Secretarias e Órgãos da Prefeitura Municipal**, representando a estrutura organizacional responsável pela execução das políticas públicas, processos, serviços e atividades administrativas do município.

O Mapa de Secretarias tem como finalidade:

* representar a estrutura organizacional;
* identificar responsabilidades institucionais;
* relacionar órgãos a domínios;
* relacionar órgãos a capacidades;
* relacionar órgãos a processos;
* identificar responsáveis por serviços;
* apoiar a gestão de acessos;
* apoiar a gestão de competências;
* apoiar a governança;
* apoiar a arquitetura de negócio;
* apoiar a implantação do SIGMUN.

---

# 2. Princípio Fundamental

A estrutura organizacional é necessária para a administração municipal, porém não deverá ser utilizada como único eixo de organização da arquitetura corporativa.

O SIGMUN deverá distinguir claramente:

```text
Organização
     ↓
Secretarias e Órgãos
     ↓
Unidades Organizacionais
     ↓
Papéis e Responsabilidades
```

de:

```text
Conhecimento
     ↓
Domínios
     ↓
Capacidades
     ↓
Processos
     ↓
Serviços
```

Portanto:

> **Secretaria representa estrutura organizacional; domínio representa conhecimento; capacidade representa o que a organização é capaz de fazer; processo representa como o trabalho é realizado.**

---

# 3. Objetivos

O Mapa de Secretarias deverá permitir:

1. identificar os órgãos municipais;
2. identificar suas responsabilidades;
3. identificar unidades subordinadas;
4. relacionar secretarias aos domínios;
5. relacionar secretarias às capacidades;
6. relacionar secretarias aos processos;
7. identificar serviços sob sua responsabilidade;
8. identificar atores institucionais;
9. apoiar a definição de papéis;
10. apoiar a gestão de acessos;
11. apoiar a gestão de indicadores;
12. apoiar a governança corporativa.

---

# 4. Estrutura Organizacional

A estrutura organizacional municipal deverá ser representada hierarquicamente.

Modelo:

```text
Prefeitura Municipal
│
├── Gabinete do Prefeito
│
├── Procuradoria
│
├── Controladoria
│
├── Secretarias
│   │
│   ├── Secretaria
│   │   ├── Departamento
│   │   │   ├── Coordenação
│   │   │   │   └── Unidade
│   │   │   └── Coordenação
│   │   └── Departamento
│   │
│   └── Secretaria
│
└── Órgãos e Entidades Vinculadas
```

A estrutura real deverá ser parametrizada conforme a legislação municipal vigente.

---

# 5. Níveis Organizacionais

O SIGMUN deverá suportar, no mínimo, os seguintes níveis:

### Nível 0 — Município

Representa a Prefeitura como organização.

### Nível 1 — Órgão

Representa:

* Gabinete;
* Secretaria;
* Procuradoria;
* Controladoria;
* Autarquia;
* Fundação;
* demais órgãos.

### Nível 2 — Unidade Organizacional

Representa:

* departamentos;
* diretorias;
* coordenações;
* gerências;
* assessorias.

### Nível 3 — Unidade Operacional

Representa unidades que executam atividades diretamente.

Exemplos:

* escolas;
* unidades de saúde;
* CRAS;
* almoxarifados;
* oficinas;
* unidades administrativas.

---

# 6. Classificação dos Órgãos

Os órgãos poderão ser classificados em:

* Administração Direta;
* Administração Indireta;
* Órgãos de Assessoramento;
* Órgãos de Controle;
* Órgãos Finalísticos;
* Órgãos Administrativos;
* Órgãos Executivos;
* Órgãos Consultivos.

---

# 7. Administração Direta

A Administração Direta compreende as unidades integrantes da estrutura da Prefeitura.

Exemplos:

* Gabinete;
* Secretarias;
* Procuradoria;
* Controladoria;
* demais unidades administrativas.

---

# 8. Administração Indireta

Quando existentes, deverão ser representadas separadamente entidades como:

* autarquias;
* fundações;
* empresas públicas;
* sociedades de economia mista.

Cada entidade deverá possuir seu próprio registro organizacional.

---

# 9. Estrutura Organizacional de Referência

A estrutura deverá ser cadastrada no SIGMUN de forma parametrizada.

Modelo inicial:

```text
Prefeitura Municipal de Camacan
│
├── Gabinete do Prefeito
│
├── Procuradoria Geral
│
├── Controladoria Geral
│
├── Secretaria de Administração
│
├── Secretaria de Finanças
│
├── Secretaria de Educação
│
├── Secretaria de Saúde
│
├── Secretaria de Assistência Social
│
├── Secretaria de Obras
│
├── Secretaria de Agricultura
│
├── Secretaria de Meio Ambiente
│
├── Secretaria de Cultura
│
├── Secretaria de Esporte
│
├── Secretaria de Turismo
│
└── Demais órgãos e unidades
```

**Observação:** esta estrutura é apenas uma referência arquitetural inicial. A estrutura oficial deverá ser obtida da legislação municipal vigente e mantida sob governança institucional.

---

# 10. Cadastro Corporativo de Secretarias

Cada secretaria ou órgão deverá possuir um registro corporativo.

Modelo:

```markdown
## ORG-XXX – Nome da Secretaria

**Código:** ORG-XXX

**Nome oficial:** Nome oficial do órgão

**Sigla:** SIGLA

**Tipo:** Secretaria / Órgão / Controladoria / Procuradoria / etc.

**Nível organizacional:** 1

**Órgão superior:** Prefeitura Municipal

**Finalidade institucional:** Descrição.

**Competências:** Competências legais.

**Responsável:** Cargo responsável.

**Domínios:** Domínios relacionados.

**Capacidades:** Capacidades relacionadas.

**Processos:** Processos executados.

**Serviços:** Serviços prestados.

**Indicadores:** Indicadores relacionados.

**Unidades subordinadas:** Unidades.

**Ativos de informação:** Principais ativos.

**Sistemas utilizados:** Aplicações relacionadas.

**Status:** Ativo / Inativo / Extinto.

**Base legal:** Legislação aplicável.
```

---

# 11. Código Organizacional

Cada órgão deverá possuir um identificador único.

Padrão:

```text
ORG-001
ORG-002
ORG-003
```

Unidades subordinadas poderão utilizar:

```text
ORG-001-001
ORG-001-002
ORG-001-003
```

O código deverá ser estável e não deverá depender exclusivamente do nome da secretaria.

---

# 12. Siglas

As siglas deverão ser controladas pelo **Vocabulário Corporativo do SIGMUN**.

Exemplo:

```text
SEADM – Secretaria de Administração
SEFIN – Secretaria de Finanças
SEDUC – Secretaria de Educação
SESAU – Secretaria de Saúde
```

As siglas oficiais deverão ser confirmadas com base nos atos administrativos vigentes.

---

# 13. Secretaria não é Domínio

Uma secretaria poderá atuar em diversos domínios.

Exemplo:

```text
Secretaria de Administração
        │
        ├── Gestão de Pessoas
        ├── Gestão Documental
        ├── Compras
        ├── Contratos
        └── Patrimônio
```

Da mesma forma, um domínio poderá envolver diversas secretarias.

---

# 14. Secretaria não é Processo

Uma secretaria poderá executar diversos processos.

Exemplo:

```text
Secretaria de Finanças
        │
        ├── Planejamento Orçamentário
        ├── Gestão da Receita
        ├── Gestão da Despesa
        ├── Tesouraria
        └── Contabilidade
```

Um processo poderá envolver diversas secretarias.

---

# 15. Secretaria não é Sistema

Uma secretaria poderá utilizar diversos sistemas.

Da mesma forma, um sistema poderá atender diversas secretarias.

O SIGMUN deverá evitar o modelo:

```text
Secretaria
   ↓
Sistema isolado
```

e priorizar:

```text
Organização
   ↓
Domínios
   ↓
Capacidades
   ↓
Processos
   ↓
Serviços
   ↓
Sistemas
```

---

# 16. Relacionamento com Domínios

Cada secretaria deverá possuir relacionamentos com um ou mais domínios.

Exemplo:

| Secretaria    | Domínio                |
| ------------- | ---------------------- |
| Administração | Gestão de Pessoas      |
| Administração | Gestão Documental      |
| Administração | Compras                |
| Finanças      | Orçamento              |
| Finanças      | Receita                |
| Finanças      | Contabilidade          |
| Saúde         | Saúde Pública          |
| Educação      | Educação               |
| Obras         | Obras e Infraestrutura |

---

# 17. Relacionamento com Capacidades

A secretaria deverá ser relacionada às capacidades que possui ou compartilha.

Exemplo:

```text
Secretaria de Saúde
       │
       ├── Planejar Saúde
       ├── Gerenciar Unidades
       ├── Gerenciar Profissionais
       ├── Gerenciar Atendimento
       └── Monitorar Saúde
```

---

# 18. Relacionamento com Processos

Cada secretaria deverá possuir participação definida nos processos.

O papel poderá ser:

* proprietária;
* executora;
* participante;
* aprovadora;
* fiscalizadora;
* consultada;
* informada.

---

# 19. Matriz Secretaria × Processo

O SIGMUN deverá manter uma matriz de responsabilidades.

| Processo             | Secretaria Principal | Participação |
| -------------------- | -------------------- | ------------ |
| Gestão de Pessoas    | Administração        | Proprietária |
| Folha                | Administração        | Executora    |
| Orçamento            | Finanças             | Proprietária |
| Compras              | Administração        | Executora    |
| Atendimento em Saúde | Saúde                | Proprietária |
| Matrícula            | Educação             | Proprietária |
| Obras Públicas       | Obras                | Proprietária |

A matriz deverá ser detalhada conforme a estrutura oficial do município.

---

# 20. Matriz RACI

Quando necessário, processos críticos deverão utilizar RACI.

| Processo    | R       | A             | C        | I                     |
| ----------- | ------- | ------------- | -------- | --------------------- |
| Contratação | Compras | Administração | Jurídico | Secretaria demandante |
| Obra        | Obras   | Administração | Jurídico | Finanças              |
| Folha       | RH      | Administração | Finanças | Gestores              |

Onde:

* **R — Responsible:** responsável pela execução;
* **A — Accountable:** responsável final;
* **C — Consulted:** consultado;
* **I — Informed:** informado.

---

# 21. Responsabilidade Institucional

Cada secretaria deverá possuir competências formalmente definidas.

A fonte de autoridade deverá ser:

* lei;
* decreto;
* regimento;
* portaria;
* ato administrativo;
* outro instrumento normativo válido.

O SIGMUN não deverá inferir competências institucionais exclusivamente a partir do nome da secretaria.

---

# 22. Unidades Organizacionais

As secretarias poderão possuir:

* departamentos;
* diretorias;
* coordenações;
* gerências;
* assessorias;
* setores;
* unidades operacionais.

Cada unidade deverá possuir relacionamento hierárquico.

---

# 23. Unidades Finalísticas

As unidades finalísticas são aquelas que executam diretamente serviços públicos.

Exemplos:

### Saúde

* UBS;
* unidades especializadas;
* farmácias;
* centros de atendimento.

### Educação

* escolas;
* creches;
* unidades de apoio.

### Assistência Social

* CRAS;
* CREAS;
* centros especializados.

---

# 24. Unidade Organizacional e Local Físico

O SIGMUN deverá diferenciar:

**Unidade Organizacional**

de:

**Localização Física.**

Uma unidade organizacional poderá:

* possuir mais de um endereço;
* mudar de endereço;
* possuir atendimento remoto.

Um local físico poderá:

* abrigar várias unidades;
* possuir diversas funções.

---

# 25. Secretarias e Serviços

Cada serviço público deverá possuir relacionamento com:

* órgão responsável;
* unidade executora;
* processo;
* domínio;
* capacidade;
* indicadores.

Modelo:

```text
Serviço
   ↓
Processo
   ↓
Capacidade
   ↓
Domínio
   ↓
Secretaria
```

---

# 26. Secretarias e Cidadãos

A relação com o cidadão deverá ocorrer preferencialmente por meio dos serviços.

Exemplo:

```text
Cidadão
   ↓
Serviço Público
   ↓
Processo
   ↓
Unidade Executora
   ↓
Secretaria Responsável
```

Isso permite que o cidadão não precise conhecer a estrutura interna da Prefeitura para acessar um serviço.

---

# 27. Secretarias e Cadastro Único Municipal

O **Cadastro Único Municipal** deverá representar as relações entre:

* cidadãos;
* organizações;
* unidades;
* endereços;
* serviços;
* órgãos.

Exemplo:

```text
Pessoa
  │
  ├── solicita serviço
  ├── possui endereço
  ├── possui vínculos
  └── interage com órgãos
```

---

# 28. Secretarias e Identidade

As unidades organizacionais deverão integrar-se ao domínio de Identidade e Acesso.

Um usuário poderá possuir:

* vínculo;
* unidade;
* cargo;
* função;
* papel;
* permissões.

---

# 29. Secretaria e Papel

O acesso ao SIGMUN não deverá ser definido exclusivamente pela secretaria.

Deverá considerar:

```text
Usuário
   ↓
Vínculo
   ↓
Unidade
   ↓
Papel
   ↓
Responsabilidade
   ↓
Permissão
```

---

# 30. Segregação de Funções

A estrutura organizacional deverá permitir implementação de segregação de funções.

Exemplo:

```text
Solicitar
   ≠
Aprovar
   ≠
Executar
   ≠
Fiscalizar
   ≠
Pagar
```

Quando aplicável, o SIGMUN deverá impedir conflitos de responsabilidade.

---

# 31. Secretarias e Dados

Cada secretaria deverá possuir responsabilidades sobre os dados sob sua gestão.

Poderá existir:

* proprietário do dado;
* custodiante;
* usuário;
* produtor;
* consumidor.

---

# 32. Secretaria como Data Owner

Quando aplicável, a secretaria poderá atuar como **Data Owner** de determinados conjuntos de informações.

Exemplo:

```text
Secretaria de Educação
       ↓
Dados educacionais
```

Isso não significa necessariamente que os dados estejam fisicamente armazenados na secretaria.

---

# 33. Secretarias e Governança de Dados

A governança deverá estabelecer:

* responsabilidade;
* qualidade;
* acesso;
* classificação;
* compartilhamento;
* retenção;
* publicação.

---

# 34. Secretarias e Classificação da Informação

A existência de uma secretaria não determina automaticamente a classificação da informação.

A classificação deverá ocorrer conforme a política corporativa.

Aplicando:

> **Classificação da Informação por política.**

---

# 35. Secretarias e Transparência

Informações produzidas pelas secretarias deverão ser avaliadas quanto à possibilidade de publicação.

Aplicando:

> **Transparência por padrão.**

---

# 36. Secretarias e Segurança

A estrutura organizacional deverá ser considerada nos controles de acesso.

Entretanto:

> **Segurança por princípio.**

A secretaria não deverá ser utilizada como único mecanismo de autorização.

---

# 37. Secretarias e LGPD

Secretarias que tratem dados pessoais deverão observar:

* finalidade;
* necessidade;
* adequação;
* base legal;
* segurança;
* direitos dos titulares;
* controle de acesso;
* retenção.

---

# 38. Secretarias e Indicadores

Cada secretaria deverá possuir indicadores relacionados a:

* resultados;
* processos;
* serviços;
* eficiência;
* qualidade;
* custos;
* metas.

Os indicadores deverão ser integrados ao domínio corporativo de indicadores.

---

# 39. Secretarias e Orçamento

Quando aplicável, a estrutura organizacional deverá relacionar:

```text
Secretaria
   ↓
Programa
   ↓
Ação
   ↓
Dotação
   ↓
Despesa
   ↓
Resultado
```

Isso permitirá relacionar recursos públicos a resultados.

---

# 40. Secretarias e Projetos

Projetos poderão possuir:

* secretaria patrocinadora;
* secretaria responsável;
* unidades participantes;
* equipes;
* fornecedores.

A estrutura organizacional deverá ser integrada ao gerenciamento de portfólio.

---

# 41. Secretarias e Contratos

Os contratos poderão possuir:

* órgão contratante;
* unidade demandante;
* gestor;
* fiscal;
* fornecedor.

O relacionamento deverá ser rastreável.

---

# 42. Secretarias e Patrimônio

Bens públicos poderão possuir:

* órgão responsável;
* unidade responsável;
* localização;
* responsável pelo uso;
* situação patrimonial.

---

# 43. Secretarias e Gestão de Pessoas

O vínculo do servidor deverá considerar:

```text
Pessoa
   ↓
Vínculo
   ↓
Cargo
   ↓
Função
   ↓
Órgão
   ↓
Unidade
```

Isso permitirá relacionar pessoas às responsabilidades organizacionais.

---

# 44. Estrutura Dinâmica

A estrutura organizacional municipal poderá sofrer alterações.

Podem ocorrer:

* criação de secretaria;
* extinção;
* fusão;
* desmembramento;
* mudança de nome;
* mudança de competências;
* mudança de hierarquia.

O SIGMUN deverá tratar essas alterações como **dados de configuração e governança**, não como mudanças estruturais no código da aplicação.

---

# 45. Histórico Organizacional

Toda alteração relevante deverá preservar histórico.

Exemplo:

```text
Secretaria A
    ↓
alteração legal
    ↓
Secretaria B
```

O sistema deverá preservar:

* identificação anterior;
* nova identificação;
* vigência;
* ato legal;
* data;
* responsáveis.

---

# 46. Vigência

Cada órgão e unidade deverá possuir:

* data de início;
* data de término, quando aplicável;
* situação atual.

Isso permitirá reconstruir a estrutura organizacional em determinado período.

---

# 47. Modelo Temporal

A estrutura poderá ser representada:

```text
ORG-001
Vigência:
01/01/2025 → 31/12/2026
```

e posteriormente:

```text
ORG-010
Vigência:
01/01/2027 → atual
```

A identificação histórica deverá permanecer preservada.

---

# 48. Modelo de Dados Organizacional

Entidades mínimas:

```text
Órgão
 ├── Unidade Organizacional
 │      ├── Unidade Operacional
 │      └── Localização
 │
 ├── Competência
 ├── Domínio
 ├── Capacidade
 ├── Processo
 ├── Serviço
 └── Responsabilidade
```

---

# 49. Cadastro de Unidade Organizacional

Modelo:

```markdown
## UND-XXX – Nome da Unidade

**Código:** UND-XXX

**Nome oficial:** Nome

**Sigla:** SIGLA

**Órgão superior:** ORG-XXX

**Tipo:** Departamento / Coordenação / Unidade / etc.

**Nível:** 2 / 3

**Finalidade:** Descrição.

**Competências:** Competências.

**Domínios:** Domínios relacionados.

**Capacidades:** Capacidades relacionadas.

**Processos:** Processos executados.

**Serviços:** Serviços prestados.

**Responsável:** Cargo ou função.

**Localização:** Endereço ou referência.

**Vigência:** Período.

**Status:** Ativo / Inativo.
```

---

# 50. Catálogo Corporativo de Organizações

O SIGMUN deverá manter um catálogo corporativo contendo:

* código;
* nome;
* sigla;
* tipo;
* hierarquia;
* competências;
* responsável;
* domínios;
* capacidades;
* processos;
* serviços;
* localização;
* vigência;
* base legal;
* status.

---

# 51. Matriz Organização × Domínio

Exemplo:

| Organização   | Domínio    | Relação      |
| ------------- | ---------- | ------------ |
| Administração | Pessoas    | Proprietária |
| Administração | Documentos | Responsável  |
| Finanças      | Orçamento  | Proprietária |
| Saúde         | Saúde      | Proprietária |
| Educação      | Educação   | Proprietária |
| Obras         | Obras      | Proprietária |

A matriz deverá ser mantida de forma dinâmica.

---

# 52. Matriz Organização × Capacidade

Exemplo:

| Organização   | Capacidade          | Papel       |
| ------------- | ------------------- | ----------- |
| Administração | Gerir Pessoas       | Responsável |
| Finanças      | Gerir Orçamento     | Responsável |
| Saúde         | Prestar Atendimento | Responsável |
| Educação      | Gerir Ensino        | Responsável |

---

# 53. Matriz Organização × Serviço

Exemplo:

| Serviço              | Órgão responsável | Unidade executora   |
| -------------------- | ----------------- | ------------------- |
| Atendimento em Saúde | Saúde             | Unidade de Saúde    |
| Matrícula Escolar    | Educação          | Escola              |
| Licenciamento        | Meio Ambiente     | Unidade responsável |
| Atendimento Social   | Assistência       | CRAS                |

---

# 54. Mapa Organizacional

A representação gráfica poderá seguir:

```text
                    PREFEITURA
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
    Governança     Administração     Finalísticos
        │               │                │
        ↓               ↓                ↓
    Controle         Finanças        Saúde/Educação
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                   Serviços Públicos
                        ↓
                     Cidadão
```

---

# 55. Relação com o Mapa de Atores

O Mapa de Secretarias deverá alimentar o **Mapa de Atores**.

Exemplo:

```text
Secretaria
   ↓
Unidade
   ↓
Papel
   ↓
Ator
   ↓
Responsabilidade
```

---

# 56. Relação com o Mapa de Capacidades

A estrutura organizacional deverá indicar quem possui ou compartilha determinada capacidade.

```text
Secretaria
      ↓
Capacidade
      ↓
Processo
```

---

# 57. Relação com o Mapa de Processos

O processo deverá identificar as organizações participantes.

```text
Processo
   ↓
RACI
   ↓
Secretarias
   ↓
Unidades
```

---

# 58. Relação com o Mapa de Domínios

A secretaria deverá ser associada aos domínios nos quais possui responsabilidades.

```text
Secretaria
   ↓
Domínio
   ↓
Capacidade
   ↓
Processo
```

---

# 59. Relação com a Cadeia de Valor

A estrutura organizacional deverá contribuir para a entrega de valor público.

```text
Secretarias
      ↓
Capacidades
      ↓
Processos
      ↓
Serviços
      ↓
Valor Público
```

---

# 60. Relação com Arquitetura de Aplicações

As aplicações deverão suportar processos e serviços independentemente da estrutura organizacional.

A organização deverá ser um **atributo configurável**, e não uma dependência rígida da aplicação.

---

# 61. Arquitetura Orientada à Organização

O SIGMUN deverá evitar:

```text
Código da aplicação
      ↓
Secretaria fixa
```

e adotar:

```text
Configuração
      ↓
Organização
      ↓
Unidade
      ↓
Papel
      ↓
Processo
      ↓
Serviço
```

---

# 62. Multiunidade

O SIGMUN deverá permitir que um mesmo serviço ou processo seja executado por várias unidades.

Exemplo:

```text
Serviço: Atendimento Social

        ┌─────────────┐
        ↓             ↓
      CRAS 1        CRAS 2
        │             │
        └──────┬──────┘
               ↓
          Assistência
```

---

# 63. Multi-Secretaria

O SIGMUN deverá permitir processos intersecretariais.

Exemplo:

```text
Programa Social
      │
      ├── Assistência
      ├── Saúde
      ├── Educação
      └── Finanças
```

---

# 64. Governança do Mapa de Secretarias

A manutenção deverá envolver:

* Administração;
* Gestão de Pessoas;
* Planejamento;
* Arquitetura Corporativa;
* Governança de Dados;
* áreas responsáveis.

A estrutura oficial deverá possuir uma fonte institucional.

---

# 65. Fonte Oficial

O SIGMUN deverá identificar a fonte oficial da estrutura organizacional.

Poderá ser:

* legislação municipal;
* lei de estrutura administrativa;
* decreto;
* regimento interno;
* organograma oficial.

A fonte deverá ser registrada.

---

# 66. Atualização

Alterações na estrutura deverão ser incorporadas mediante:

1. identificação do ato legal;
2. validação;
3. atualização do cadastro;
4. atualização da hierarquia;
5. atualização dos relacionamentos;
6. preservação do histórico;
7. comunicação aos sistemas afetados.

---

# 67. Impacto de Mudanças Organizacionais

Uma mudança de secretaria deverá permitir identificar impactos sobre:

* processos;
* capacidades;
* serviços;
* usuários;
* permissões;
* dados;
* documentos;
* indicadores;
* aplicações;
* integrações.

---

# 68. Indicadores Organizacionais

Poderão ser acompanhados:

* quantidade de órgãos;
* quantidade de unidades;
* unidades ativas;
* unidades extintas;
* quantidade de processos por órgão;
* quantidade de serviços por órgão;
* quantidade de servidores por unidade;
* quantidade de sistemas utilizados;
* quantidade de domínios relacionados.

---

# 69. Critérios de Qualidade

O cadastro organizacional deverá garantir:

* unicidade;
* consistência;
* atualidade;
* rastreabilidade;
* validade;
* integridade;
* histórico.

---

# 70. Princípio da Configurabilidade

A estrutura organizacional deverá ser configurável.

Mudanças administrativas ordinárias não deverão exigir alterações estruturais no software.

---

# 71. Princípio da Independência Arquitetural

A arquitetura deverá permanecer estável mesmo quando a organização mudar.

Exemplo:

```text
Secretaria A
     ↓
Processo X
```

poderá tornar-se:

```text
Secretaria B
     ↓
Processo X
```

sem que o processo precise ser recriado.

---

# 72. Princípio da Continuidade

A estrutura organizacional poderá mudar, mas os registros históricos deverão permanecer íntegros.

Isso é essencial para:

* auditoria;
* prestação de contas;
* histórico administrativo;
* indicadores;
* transparência;
* análise de políticas públicas.

---

# 73. Princípio da Transparência

Sempre que possível, a estrutura organizacional deverá ser publicada de forma acessível.

Aplicando:

> **Transparência por padrão.**

---

# 74. Princípio da Segurança

Informações organizacionais sensíveis deverão possuir controles adequados.

Aplicando:

> **Segurança por princípio.**

---

# 75. Princípio da Classificação da Informação

As informações relacionadas à estrutura organizacional deverão ser classificadas conforme a política corporativa.

Aplicando:

> **Classificação da Informação por política.**

---

# 76. Princípio de Abertura

O SIGMUN deverá adotar:

> **Aberto sempre que possível, restrito sempre que necessário.**

---

# 77. Evolução Futura

O Mapa de Secretarias deverá evoluir para um **Catálogo Corporativo de Organizações**, contendo:

* órgãos;
* unidades;
* cargos;
* funções;
* papéis;
* competências;
* responsabilidades;
* domínios;
* capacidades;
* processos;
* serviços;
* localização;
* vigência;
* atos legais.

Esse catálogo deverá integrar-se ao **Cadastro Único Municipal** e ao **Catálogo Corporativo do Conhecimento**.

---

# 78. Disposições Finais

O **Mapa de Secretarias** constitui uma referência corporativa para representação da estrutura organizacional do município.

Sua função não é substituir os documentos legais nem estabelecer competências administrativas. Sua função é **estruturar essas informações de maneira interoperável e integrada ao modelo corporativo do SIGMUN**.

A arquitetura deverá preservar a separação conceitual:

```text
Organização
    ↓
Domínio
    ↓
Capacidade
    ↓
Processo
    ↓
Serviço
    ↓
Aplicação
    ↓
Dados
```

Dessa forma, mudanças administrativas poderão ser absorvidas pelo SIGMUN sem comprometer a arquitetura corporativa.

---

# 79. Princípios Arquiteturais Relacionados

O Mapa de Secretarias deverá observar os princípios fundamentais do SIGMUN:

> **Transparência por padrão.**

> **Segurança por princípio.**

> **Classificação da Informação por política.**

> **Aberto sempre que possível, restrito sempre que necessário.**

> **Tecnologia como meio. Pessoas, organizações, processos, conhecimento, capacidades e valor público como finalidade.**

---

**Documento:** `Mapa-de-Secretarias.md`

**Última atualização:** `2026-08-11`

**Responsável:** `Equipe SIGMUN`

**Status da revisão:** `Vigente`
