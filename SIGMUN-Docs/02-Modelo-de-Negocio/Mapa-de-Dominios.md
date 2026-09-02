# Mapa de Domínios

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
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`
* `009-Arquitetura-de-Dados.md`
* `008-Arquitetura-de-Software.md`
* `010-Arquitetura-de-Integracao.md`

---

## 1. Finalidade

Este documento estabelece o **Mapa Corporativo de Domínios do SIGMUN**, identificando e organizando os principais domínios de conhecimento, responsabilidade, informação e atuação necessários à gestão municipal.

O Mapa de Domínios tem como finalidade estabelecer uma visão corporativa e integrada do município, servindo como referência para:

* arquitetura de negócio;
* arquitetura de dados;
* arquitetura de aplicações;
* arquitetura de integração;
* definição de módulos;
* definição de serviços;
* gestão de processos;
* gestão de requisitos;
* governança de dados;
* gestão do conhecimento;
* segurança da informação;
* organização do catálogo corporativo.

---

# 2. Conceito de Domínio

Para fins do SIGMUN, um **Domínio** representa uma área de conhecimento, responsabilidade ou atuação institucional que possui:

* conceitos próprios;
* informações próprias;
* regras de negócio;
* processos;
* atores;
* responsabilidades;
* indicadores;
* serviços;
* relacionamentos com outros domínios.

Um domínio representa **um conjunto coerente de conhecimentos e responsabilidades**, independentemente da secretaria, departamento, sistema ou tecnologia utilizada.

---

# 3. Domínio não é Secretaria

O SIGMUN não deverá utilizar a estrutura administrativa atual como única forma de organização do conhecimento.

Uma secretaria pode:

* possuir vários domínios;
* compartilhar um domínio com outras secretarias;
* consumir informações de outros domínios;
* produzir informações utilizadas por outros domínios.

Da mesma forma, um domínio poderá ser utilizado por diversas secretarias.

Portanto:

> **Domínio representa conhecimento e responsabilidade; secretaria representa estrutura organizacional.**

---

# 4. Princípio Fundamental

A arquitetura corporativa do SIGMUN deverá adotar o princípio:

> **Organizar o conhecimento por domínios, as capacidades por responsabilidades, os processos por fluxos de trabalho e os sistemas por serviços que suportam essas necessidades.**

---

# 5. Relação entre Domínios e Arquitetura

A relação conceitual é:

```text
Estratégia
    ↓
Domínios
    ↓
Capacidades
    ↓
Processos
    ↓
Serviços
    ↓
Requisitos
    ↓
Aplicações
    ↓
Dados
    ↓
Tecnologia
```

---

# 6. Categorias de Domínios

Os domínios do SIGMUN serão classificados em:

1. **Domínios Corporativos;**
2. **Domínios Administrativos;**
3. **Domínios Econômico-Financeiros;**
4. **Domínios de Pessoas;**
5. **Domínios Patrimoniais;**
6. **Domínios Territoriais;**
7. **Domínios Finalísticos;**
8. **Domínios de Atendimento e Relacionamento;**
9. **Domínios de Dados e Conhecimento;**
10. **Domínios Tecnológicos;**
11. **Domínios de Governança e Controle.**

---

# 7. Domínios Corporativos

Os domínios corporativos suportam o funcionamento transversal da administração municipal.

Incluem:

* Governança;
* Planejamento;
* Gestão Estratégica;
* Gestão de Processos;
* Gestão de Riscos;
* Gestão Documental;
* Gestão de Contratos;
* Gestão de Projetos;
* Gestão de Portfólio;
* Comunicação Institucional.

---

# 8. Domínio de Governança

### 8.1 Identificação

**Código:** `DOM-GOV`

**Nome:** Governança Municipal

**Tipo:** Corporativo

### 8.2 Finalidade

Abrange os mecanismos utilizados para:

* tomar decisões;
* estabelecer responsabilidades;
* definir políticas;
* supervisionar resultados;
* controlar riscos;
* garantir conformidade.

### 8.3 Principais capacidades

* Governança Corporativa;
* Governança Digital;
* Gestão de Riscos;
* Compliance;
* Gestão de Políticas.

---

# 9. Domínio de Planejamento

### 9.1 Identificação

**Código:** `DOM-PLA`

**Nome:** Planejamento Governamental

**Tipo:** Estratégico

### 9.2 Abrangência

Inclui:

* planejamento estratégico;
* planejamento governamental;
* programas;
* projetos;
* metas;
* indicadores;
* orçamento;
* acompanhamento de resultados.

---

# 10. Domínios Administrativos

Incluem:

* Protocolo;
* Processos Administrativos;
* Gestão Documental;
* Gestão de Contratos;
* Gestão de Compras;
* Licitações;
* Patrimônio;
* Almoxarifado;
* Serviços Administrativos.

---

# 11. Domínio de Gestão Documental

**Código:** `DOM-GDO`

**Nome:** Gestão Documental

Abrange:

* documentos;
* processos documentais;
* classificação;
* versionamento;
* tramitação;
* assinatura;
* arquivamento;
* preservação;
* descarte.

Relaciona-se diretamente com:

* Gestão de Processos;
* Protocolo;
* Segurança;
* Governança de Dados.

---

# 12. Domínio de Compras e Contratações

**Código:** `DOM-COM`

**Nome:** Compras e Contratações

Abrange:

* planejamento de compras;
* demandas;
* licitações;
* dispensas;
* inexigibilidades;
* fornecedores;
* contratos;
* fiscalização contratual.

---

# 13. Domínios Econômico-Financeiros

Incluem:

* Orçamento;
* Receita;
* Despesa;
* Contabilidade;
* Tesouraria;
* Dívida;
* Tributação;
* Arrecadação;
* Prestação de Contas.

---

# 14. Domínio Tributário

**Código:** `DOM-TRI`

**Nome:** Administração Tributária

Abrange:

* cadastro tributário;
* contribuintes;
* tributos;
* lançamentos;
* arrecadação;
* fiscalização;
* dívida ativa;
* cobrança;
* benefícios fiscais.

---

# 15. Domínio Orçamentário

**Código:** `DOM-ORC`

**Nome:** Orçamento Público

Abrange:

* planejamento orçamentário;
* receitas;
* despesas;
* créditos;
* execução;
* acompanhamento;
* metas fiscais.

---

# 16. Domínio Contábil

**Código:** `DOM-CON`

**Nome:** Contabilidade Pública

Abrange:

* registros contábeis;
* demonstrações;
* patrimônio;
* obrigações;
* informações fiscais;
* prestação de contas.

---

# 17. Domínios de Pessoas

Incluem:

* Gestão de Pessoas;
* Recursos Humanos;
* Folha;
* Benefícios;
* Saúde Ocupacional;
* Competências;
* Capacitação;
* Conhecimento Organizacional.

---

# 18. Domínio de Pessoas e Servidores

**Código:** `DOM-PES`

**Nome:** Gestão de Pessoas

Abrange:

* servidores;
* vínculos;
* cargos;
* funções;
* lotações;
* movimentações;
* férias;
* afastamentos;
* benefícios;
* avaliações.

---

# 19. Domínio de Competências

**Código:** `DOM-CPT`

**Nome:** Gestão de Competências

Abrange:

* competências;
* habilidades;
* qualificações;
* capacitações;
* lacunas;
* desenvolvimento profissional.

---

# 20. Domínios Patrimoniais

Incluem:

* Patrimônio;
* Bens;
* Imóveis;
* Veículos;
* Almoxarifado;
* Estoques;
* Manutenção de Ativos.

---

# 21. Domínio Patrimonial

**Código:** `DOM-PAT`

**Nome:** Gestão Patrimonial

Abrange:

* bens móveis;
* bens imóveis;
* equipamentos;
* ativos;
* movimentações;
* inventários;
* depreciação;
* baixa patrimonial.

---

# 22. Domínio de Frota

**Código:** `DOM-FRO`

**Nome:** Gestão de Frota

Abrange:

* veículos;
* condutores;
* utilização;
* abastecimento;
* manutenção;
* custos;
* documentação.

---

# 23. Domínios Territoriais

Incluem:

* Território;
* Cadastro Imobiliário;
* Endereçamento;
* Geoprocessamento;
* Obras;
* Infraestrutura;
* Meio Ambiente;
* Serviços Urbanos.

---

# 24. Domínio Territorial

**Código:** `DOM-TEL`

**Nome:** Gestão Territorial

Abrange:

* território municipal;
* bairros;
* distritos;
* logradouros;
* localidades;
* áreas públicas;
* zonas;
* referências geográficas.

---

# 25. Domínio Imobiliário

**Código:** `DOM-IMO`

**Nome:** Cadastro Imobiliário

Abrange:

* imóveis;
* proprietários;
* possuidores;
* terrenos;
* edificações;
* características físicas;
* valores;
* situação cadastral.

---

# 26. Domínio Geoespacial

**Código:** `DOM-GEO`

**Nome:** Geoinformação Municipal

Abrange:

* mapas;
* camadas;
* coordenadas;
* dados geográficos;
* análises espaciais;
* georreferenciamento.

---

# 27. Domínio de Obras e Infraestrutura

**Código:** `DOM-OBR`

**Nome:** Obras e Infraestrutura

Abrange:

* obras públicas;
* projetos;
* contratos;
* fiscalização;
* medições;
* cronogramas;
* custos;
* manutenção.

---

# 28. Domínios Finalísticos

Os domínios finalísticos representam áreas de políticas públicas e serviços diretamente relacionados à população.

Incluem:

* Saúde;
* Educação;
* Assistência Social;
* Cultura;
* Esporte;
* Turismo;
* Meio Ambiente;
* Agricultura;
* Desenvolvimento Econômico;
* Habitação;
* Mobilidade;
* Defesa Civil.

Cada domínio finalístico deverá possuir seu próprio modelo detalhado.

---

# 29. Domínio de Saúde

**Código:** `DOM-SAU`

**Nome:** Saúde Pública

Abrange:

* cidadãos;
* pacientes;
* unidades;
* profissionais;
* atendimentos;
* procedimentos;
* medicamentos;
* vacinação;
* vigilância;
* regulação.

---

# 30. Domínio de Educação

**Código:** `DOM-EDU`

**Nome:** Educação Pública

Abrange:

* alunos;
* escolas;
* professores;
* matrículas;
* turmas;
* frequência;
* transporte;
* alimentação;
* avaliações.

---

# 31. Domínio de Assistência Social

**Código:** `DOM-ASS`

**Nome:** Assistência Social

Abrange:

* famílias;
* indivíduos;
* benefícios;
* vulnerabilidades;
* serviços;
* programas;
* acompanhamento social.

---

# 32. Domínio de Meio Ambiente

**Código:** `DOM-MAM`

**Nome:** Meio Ambiente

Abrange:

* licenciamento;
* fiscalização;
* resíduos;
* recursos naturais;
* áreas protegidas;
* monitoramento ambiental.

---

# 33. Domínio de Desenvolvimento Econômico

**Código:** `DOM-DEC`

**Nome:** Desenvolvimento Econômico

Abrange:

* empresas;
* empreendedores;
* atividades econômicas;
* emprego;
* investimentos;
* programas de desenvolvimento;
* economia local.

---

# 34. Domínios de Atendimento e Relacionamento

Incluem:

* Cadastro Único Municipal;
* Atendimento ao Cidadão;
* Serviços Digitais;
* Ouvidoria;
* Participação Social;
* Comunicação.

---

# 35. Domínio do Cadastro Único Municipal

**Código:** `DOM-CUM`

**Nome:** Cadastro Único Municipal

É um dos principais domínios corporativos do SIGMUN.

Deverá permitir uma visão integrada dos principais sujeitos e organizações relacionados ao município, respeitando:

* finalidade;
* necessidade;
* classificação da informação;
* proteção de dados;
* controles de acesso.

---

# 36. Domínio de Atendimento

**Código:** `DOM-ATE`

**Nome:** Atendimento ao Cidadão

Abrange:

* solicitações;
* requerimentos;
* serviços;
* protocolos;
* agendamentos;
* manifestações;
* acompanhamento.

---

# 37. Domínio de Ouvidoria

**Código:** `DOM-OUV`

**Nome:** Ouvidoria

Abrange:

* manifestações;
* reclamações;
* denúncias;
* sugestões;
* elogios;
* respostas;
* indicadores.

---

# 38. Domínios de Dados e Conhecimento

Incluem:

* Dados;
* Metadados;
* Informação;
* Conhecimento;
* Indicadores;
* Business Intelligence;
* Analytics;
* Inteligência Artificial.

---

# 39. Domínio de Dados

**Código:** `DOM-DAD`

**Nome:** Dados Corporativos

Abrange:

* dados mestres;
* dados transacionais;
* dados de referência;
* dados analíticos;
* dados históricos.

---

# 40. Domínio de Metadados

**Código:** `DOM-MET`

**Nome:** Metadados Corporativos

Abrange:

* definições;
* conceitos;
* atributos;
* classificações;
* proprietários;
* origem;
* qualidade;
* linhagem.

Este domínio deverá estar integrado ao:

`000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`

---

# 41. Domínio de Indicadores

**Código:** `DOM-IND`

**Nome:** Indicadores e Desempenho

Abrange:

* indicadores estratégicos;
* indicadores operacionais;
* indicadores de políticas públicas;
* metas;
* resultados;
* painéis.

---

# 42. Domínio de Inteligência e Analytics

**Código:** `DOM-ANA`

**Nome:** Analytics e Inteligência

Abrange:

* análise de dados;
* estatística;
* modelos preditivos;
* ciência de dados;
* inteligência artificial;
* apoio à decisão.

---

# 43. Domínios Tecnológicos

Incluem:

* Identidade;
* Segurança;
* Aplicações;
* Integração;
* Infraestrutura;
* Mobilidade;
* Comunicação;
* Observabilidade.

---

# 44. Domínio de Identidade

**Código:** `DOM-IDN`

**Nome:** Identidade e Acesso

Abrange:

* identidades;
* autenticação;
* autorização;
* perfis;
* papéis;
* permissões;
* credenciais.

---

# 45. Domínio de Segurança

**Código:** `DOM-SEG`

**Nome:** Segurança da Informação

Abrange:

* proteção;
* ameaças;
* vulnerabilidades;
* incidentes;
* controles;
* auditoria;
* monitoramento.

---

# 46. Domínio de Integração

**Código:** `DOM-INT`

**Nome:** Integração e Interoperabilidade

Abrange:

* APIs;
* eventos;
* mensagens;
* integrações;
* interoperabilidade;
* sistemas externos.

---

# 47. Domínio de Mobilidade

**Código:** `DOM-MOB`

**Nome:** Mobilidade e Serviços de Campo

Abrange:

* dispositivos móveis;
* aplicações móveis;
* operações de campo;
* captura de evidências;
* geolocalização;
* sincronização;
* operação offline.

---

# 48. Domínio de Infraestrutura

**Código:** `DOM-INF`

**Nome:** Infraestrutura Tecnológica

Abrange:

* computação;
* armazenamento;
* redes;
* bancos de dados;
* nuvem;
* dispositivos;
* ambientes.

---

# 49. Domínios de Governança e Controle

Incluem:

* Auditoria;
* Controle Interno;
* Compliance;
* Transparência;
* Prestação de Contas;
* Gestão de Riscos.

---

# 50. Mapa Consolidado de Domínios

| Código    | Domínio                                     | Categoria            |
| --------- | ------------------------------------------- | -------------------- |
| `DOM-GOV` | Governança Municipal                        | Corporativo          |
| `DOM-PLA` | Planejamento Governamental                  | Estratégico          |
| `DOM-GDO` | Gestão Documental                           | Administrativo       |
| `DOM-COM` | Compras e Contratações                      | Administrativo       |
| `DOM-TRI` | Administração Tributária                    | Econômico-Financeiro |
| `DOM-ORC` | Orçamento Público                           | Econômico-Financeiro |
| `DOM-CON` | Contabilidade Pública                       | Econômico-Financeiro |
| `DOM-PES` | Gestão de Pessoas                           | Pessoas              |
| `DOM-CPT` | Gestão de Competências                      | Pessoas              |
| `DOM-PAT` | Gestão Patrimonial                          | Patrimonial          |
| `DOM-FRO` | Gestão de Frota                             | Patrimonial          |
| `DOM-TEL` | Gestão Territorial                          | Territorial          |
| `DOM-IMO` | Cadastro Imobiliário                        | Territorial          |
| `DOM-GEO` | Geoinformação Municipal                     | Territorial          |
| `DOM-OBR` | Obras e Infraestrutura                      | Territorial          |
| `DOM-SAU` | Saúde Pública                               | Finalístico          |
| `DOM-EDU` | Educação Pública                            | Finalístico          |
| `DOM-ASS` | Assistência Social                          | Finalístico          |
| `DOM-MAM` | Meio Ambiente                               | Finalístico          |
| `DOM-DEC` | Desenvolvimento Econômico                   | Finalístico          |
| `DOM-CUM` | Cadastro Único Municipal                    | Atendimento          |
| `DOM-ATE` | Atendimento ao Cidadão                      | Atendimento          |
| `DOM-OUV` | Ouvidoria                                   | Atendimento          |
| `DOM-DAD` | Dados Corporativos                          | Dados                |
| `DOM-MET` | Metadados Corporativos                      | Dados                |
| `DOM-IND` | Indicadores e Desempenho                    | Dados                |
| `DOM-ANA` | Analytics e Inteligência                    | Dados                |
| `DOM-IDN` | Identidade e Acesso                         | Tecnológico          |
| `DOM-SEG` | Segurança da Informação                     | Tecnológico          |
| `DOM-INT` | Integração e Interoperabilidade             | Tecnológico          |
| `DOM-MOB` | Mobilidade e Serviços de Campo              | Tecnológico          |
| `DOM-INF` | Infraestrutura Tecnológica                  | Tecnológico          |
| `DOM-DIA` | Gestão de Diárias, Viagens e Deslocamentos  | Administrativo       |
| --------- | ------------------------------------------- | -------------------- |

---

# 51. Relacionamento entre Domínios

Os domínios não deverão ser considerados isoladamente.

O SIGMUN deverá representar seus relacionamentos.

Exemplo:

```text
                   ┌──────────────────┐
                   │ Cadastro Único   │
                   │ Municipal        │
                   └────────┬─────────┘
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │  Saúde   │  │ Educação │  │Assistência│
        └──────────┘  └──────────┘  └──────────┘
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                    ┌───────────────┐
                    │   Indicadores │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │    Gestão     │
                    │  Estratégica  │
                    └───────────────┘
```

---

# 52. Domínios Mestres

Alguns domínios possuem caráter transversal e deverão funcionar como referências corporativas.

São considerados inicialmente domínios mestres:

* `DOM-CUM` – Cadastro Único Municipal;
* `DOM-DAD` – Dados Corporativos;
* `DOM-MET` – Metadados Corporativos;
* `DOM-IDN` – Identidade e Acesso;
* `DOM-GEO` – Geoinformação Municipal;
* `DOM-IND` – Indicadores e Desempenho.

Esses domínios deverão possuir governança específica.

---

# 53. Domínios Compartilhados

Um domínio poderá ser compartilhado por diversas unidades organizacionais.

Exemplo:

```text
Gestão de Pessoas
       ↑
       │
┌──────┼──────┬────────┐
│      │      │        │
Saúde Educação Obras Administração
```

A existência de um domínio compartilhado não implica necessariamente centralização operacional.

---

# 54. Domínios de Referência

São domínios utilizados como fonte oficial de determinadas informações corporativas.

Exemplos:

* pessoas;
* organizações;
* endereços;
* imóveis;
* unidades administrativas;
* fornecedores;
* servidores;
* territórios.

A definição de uma fonte de referência deverá ser estabelecida pela **Governança de Dados**.

---

# 55. Domínios e Dados Mestres

Cada domínio poderá possuir entidades consideradas dados mestres.

Exemplo:

| Domínio                  | Dado Mestre            |
| ------------------------ | ---------------------- |
| Cadastro Único           | Pessoa                 |
| Administração Tributária | Contribuinte           |
| Pessoas                  | Servidor               |
| Patrimônio               | Bem                    |
| Território               | Imóvel                 |
| Compras                  | Fornecedor             |
| Educação                 | Aluno                  |
| Saúde                    | Paciente               |
| Organização              | Unidade Organizacional |

---

# 56. Domínios e Segurança

Cada domínio deverá possuir classificação de segurança compatível com:

* sensibilidade;
* criticidade;
* impacto;
* legislação;
* riscos;
* finalidade.

A classificação do domínio não substitui a classificação individual das informações.

Deverá prevalecer:

> **Classificação da Informação por política.**

---

# 57. Domínios e LGPD

Domínios que tratem dados pessoais deverão possuir:

* finalidade definida;
* base legal aplicável;
* responsáveis;
* controles de acesso;
* rastreabilidade;
* políticas de retenção;
* mecanismos de proteção;
* avaliação de riscos quando aplicável.

---

# 58. Domínios e Requisitos

Todo requisito relevante deverá, quando aplicável, possuir vínculo com:

```text
Domínio
   ↓
Capacidade
   ↓
Processo
   ↓
Necessidade
   ↓
Requisito
```

Isso permite rastrear a origem e o propósito do requisito.

---

# 59. Domínios e Aplicações

Uma aplicação poderá suportar:

* um domínio;
* vários domínios;
* capacidades de um domínio;
* processos de vários domínios.

Portanto:

> **Domínio não é sinônimo de aplicação.**

---

# 60. Domínios e Módulos

Os módulos do SIGMUN deverão ser definidos após a análise de:

* domínios;
* capacidades;
* processos;
* serviços;
* requisitos;
* dados;
* integrações.

A estrutura de módulos deverá evitar:

* duplicidade;
* silos de informação;
* cadastros paralelos;
* funcionalidades redundantes.

---

# 61. Domínios e Arquitetura de Dados

O Mapa de Domínios servirá como uma das entradas para a definição de:

* domínios de dados;
* entidades;
* agregados;
* proprietários;
* custodiante;
* fontes oficiais;
* integrações;
* linhagem.

---

# 62. Domínios e Arquitetura de Aplicações

O Mapa de Domínios servirá como referência para:

* definição de módulos;
* definição de serviços;
* limites de aplicações;
* APIs;
* integrações;
* responsabilidades sistêmicas.

---

# 63. Domínios e Arquitetura de Integração

Integrações deverão identificar:

* domínio de origem;
* domínio de destino;
* dados compartilhados;
* finalidade;
* frequência;
* mecanismo;
* responsabilidade;
* nível de segurança.

---

# 64. Governança dos Domínios

Cada domínio deverá possuir:

* proprietário institucional;
* responsável pelo negócio;
* responsável pelos dados;
* definição formal;
* documentação;
* indicadores;
* regras de negócio;
* processos relacionados.

A governança deverá evitar que diferentes unidades utilizem conceitos conflitantes para o mesmo domínio.

---

# 65. Registro de um Domínio

Cada domínio deverá possuir uma ficha padronizada.

```markdown
## DOM-XXX – Nome do Domínio

**Código:** DOM-XXX

**Nome:** Nome do domínio

**Categoria:** Corporativo / Administrativo / Finalístico / Tecnológico

**Descrição:** Descrição objetiva.

**Finalidade:** Finalidade institucional.

**Proprietário:** Unidade ou papel responsável.

**Responsável pelo negócio:** Papel responsável.

**Responsável pelos dados:** Papel responsável.

**Atores:** Principais atores.

**Capacidades:** Capacidades relacionadas.

**Processos:** Processos relacionados.

**Serviços:** Serviços relacionados.

**Dados:** Principais dados.

**Aplicações:** Sistemas ou módulos relacionados.

**Integrações:** Integrações existentes.

**Indicadores:** Indicadores relacionados.

**Criticidade:** Baixa / Média / Alta / Crítica.

**Classificação:** Conforme política de classificação da informação.

**Dependências:** Domínios relacionados.

**Observações:** Informações adicionais.
```

---

# 66. Governança do Mapa de Domínios

O Mapa de Domínios deverá ser mantido sob responsabilidade da **Arquitetura Corporativa**, com participação da:

* Governança de Dados;
* Arquitetura de Negócio;
* Arquitetura de Software;
* Arquitetura de Integração;
* Segurança da Informação;
* áreas responsáveis pelos processos.

Alterações estruturais deverão ser:

* documentadas;
* justificadas;
* avaliadas;
* aprovadas;
* versionadas.

---

# 67. Critérios para Criação de Novo Domínio

Um novo domínio deverá ser criado somente quando houver justificativa clara, considerando:

* conjunto coerente de conhecimentos;
* regras de negócio próprias;
* informações próprias;
* processos relevantes;
* responsabilidades distintas;
* necessidade de governança específica;
* necessidade de integração;
* relevância institucional.

Não deverá ser criado um domínio exclusivamente porque:

* existe uma nova secretaria;
* existe um novo módulo;
* existe uma nova tela;
* existe uma nova tecnologia.

---

# 68. Critérios para Consolidação de Domínios

Domínios poderão ser consolidados quando:

* possuírem conceitos fortemente relacionados;
* compartilharem responsabilidades;
* possuírem processos semelhantes;
* houver baixa necessidade de governança independente;
* a separação provocar duplicidade.

---

# 69. Ciclo de Vida dos Domínios

Os domínios poderão passar pelos estados:

```text
Proposto
   ↓
Em Avaliação
   ↓
Aprovado
   ↓
Ativo
   ↓
Em Evolução
   ↓
Consolidado
   ↓
Descontinuado
```

A descontinuação deverá preservar a rastreabilidade histórica.

---

# 70. Indicadores do Mapa de Domínios

Poderão ser acompanhados:

* número de domínios;
* domínios ativos;
* domínios compartilhados;
* domínios mestres;
* domínios com proprietário definido;
* domínios com responsável por dados;
* domínios documentados;
* domínios relacionados a processos;
* domínios relacionados a aplicações;
* domínios com governança estabelecida.

---

# 71. Princípio da Não Duplicidade

O SIGMUN deverá evitar a criação de múltiplos domínios para representar o mesmo conhecimento.

Quando diferentes áreas utilizarem conceitos equivalentes, deverá ser avaliada a possibilidade de criação de um domínio corporativo comum.

---

# 72. Princípio da Fonte Oficial

Quando um domínio possuir uma informação considerada corporativa ou mestre, deverá existir uma fonte oficial definida.

Exemplo:

```text
Pessoa
   ↓
Fonte Corporativa
   ↓
Saúde
Educação
Assistência
Tributação
RH
```

Isso reduz:

* duplicidade;
* inconsistência;
* retrabalho;
* divergência cadastral.

---

# 73. Princípio da Interoperabilidade

Os domínios deverão ser projetados para permitir compartilhamento controlado de informações.

A integração deverá ocorrer por mecanismos padronizados e seguros.

---

# 74. Princípio da Transparência

Sempre que possível, informações públicas deverão ser disponibilizadas de forma:

* acessível;
* compreensível;
* reutilizável;
* estruturada;
* auditável.

Aplicando o princípio:

> **Transparência por padrão.**

---

# 75. Princípio da Segurança

A proteção das informações deverá ser incorporada desde a definição do domínio.

Aplicando o princípio:

> **Segurança por princípio.**

---

# 76. Princípio da Classificação da Informação

A abertura ou restrição das informações deverá observar a política corporativa de classificação.

Aplicando o princípio:

> **Classificação da Informação por política.**

---

# 77. Princípio de Abertura

O SIGMUN deverá adotar:

> **Aberto sempre que possível, restrito sempre que necessário.**

Isso significa que a restrição deverá possuir justificativa baseada em:

* legislação;
* privacidade;
* segurança;
* interesse público;
* risco;
* obrigação institucional.

---

# 78. Disposições Finais

O **Mapa de Domínios do SIGMUN** constitui referência corporativa para organizar o conhecimento, as responsabilidades, as informações e as relações institucionais do município.

Seu objetivo é garantir que a arquitetura do SIGMUN seja construída de forma integrada e coerente, evitando:

* silos organizacionais;
* silos de dados;
* sistemas isolados;
* duplicidade cadastral;
* conceitos conflitantes;
* funcionalidades redundantes.

A relação fundamental da arquitetura deverá permanecer:

```text
Estratégia
   ↓
Valor Público
   ↓
Domínios
   ↓
Capacidades
   ↓
Processos
   ↓
Serviços
   ↓
Requisitos
   ↓
Aplicações
   ↓
Dados
   ↓
Tecnologia
   ↓
Resultados
```

O documento deverá ser utilizado conjuntamente com:

* `Cadeia-de-Valor.md`;
* `Mapa-de-Atores.md`;
* `Mapa-de-Capacidades.md`;
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`;
* `000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md`;
* `009-Arquitetura-de-Dados.md`;
* `008-Arquitetura-de-Software.md`;
* `010-Arquitetura-de-Integracao.md`;
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade.md`.

---

# 79. Princípios Arquiteturais Relacionados

O Mapa de Domínios deverá observar os princípios fundamentais do SIGMUN:

> **Transparência por padrão.**

> **Segurança por princípio.**

> **Classificação da Informação por política.**

> **Aberto sempre que possível, restrito sempre que necessário.**

> **Tecnologia como meio. Pessoas, conhecimento, capacidades e valor público como finalidade.**

---

**Documento:** `Mapa-de-Dominios.md`

**Última atualização:** `2026-08-11`

**Responsável:** `Equipe SIGMUN`

**Status da revisão:** `Vigente`
