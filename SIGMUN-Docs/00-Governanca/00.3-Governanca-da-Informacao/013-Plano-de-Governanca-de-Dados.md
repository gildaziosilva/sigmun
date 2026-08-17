# 013-Plano-de-Governanca-de-Dados.md

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Governança
**Versão:** 1.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Documento(s) Relacionado(s):**
- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

---

# Plano de Governança de Dados do SIGMUN

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** 00 – Governança

**Versão:** 1.0

**Status:** Em elaboração

---

# 1. Objetivo

Este Plano estabelece a estrutura de Governança de Dados do SIGMUN, definindo princípios, políticas, papéis, responsabilidades, processos e mecanismos necessários para assegurar que os dados produzidos, compartilhados e utilizados pela plataforma sejam tratados como ativos estratégicos da Administração Pública.

O plano busca garantir que os dados possuam qualidade, integridade, segurança, disponibilidade, rastreabilidade e conformidade legal durante todo o seu ciclo de vida.

---

# 2. Escopo

Este plano aplica-se a:

- todos os módulos do SIGMUN;
- Cadastro Único Municipal;
- bases de dados corporativas;
- integrações internas;
- integrações externas;
- APIs;
- documentos digitais;
- indicadores;
- painéis gerenciais;
- inteligência artificial;
- analytics;
- arquivos eletrônicos;
- metadados;
- dados mestres;
- dados de referência;
- dados pessoais;
- dados sensíveis;
- dados públicos.

---

# 3. Objetivos Específicos

São objetivos deste plano:

- estabelecer responsabilidades sobre os dados;
- melhorar a qualidade da informação;
- garantir integridade dos dados;
- promover compartilhamento seguro;
- reduzir duplicidade;
- padronizar conceitos;
- fortalecer a tomada de decisão;
- assegurar conformidade com a LGPD;
- apoiar iniciativas de BI e Inteligência Artificial;
- aumentar a confiabilidade das informações institucionais.

---

# 4. Princípios

A Governança de Dados observará os seguintes princípios:

- dados como ativo estratégico;
- dado único;
- integridade;
- qualidade;
- rastreabilidade;
- transparência;
- responsabilidade;
- segurança;
- privacidade;
- interoperabilidade;
- reutilização;
- padronização;
- melhoria contínua.

---

# 5. Estrutura de Governança

A Governança de Dados será composta pelos seguintes níveis.

## Alta Administração

Responsável pelo patrocínio institucional.

---

## Comitê de Governança de Dados

Responsável pelas decisões estratégicas relacionadas aos dados corporativos.

---

## Gestores de Dados (Data Owners)

Responsáveis pelo conteúdo e pelas regras de negócio dos dados sob sua responsabilidade.

---

## Administradores de Dados (Data Stewards)

Responsáveis pela qualidade, padronização, catalogação e acompanhamento operacional dos dados.

---

## Equipe Técnica

Responsável pela implementação tecnológica.

---

## Usuários

Responsáveis pela correta utilização das informações conforme suas atribuições.

---

# 6. Papéis e Responsabilidades

## Comitê de Governança de Dados

Competências:

- definir políticas;
- aprovar padrões;
- deliberar sobre conflitos;
- acompanhar indicadores;
- priorizar melhorias.

---

## Data Owner

Responsável por:

- definir regras de negócio;
- aprovar alterações;
- validar qualidade;
- autorizar compartilhamentos;
- definir responsabilidades funcionais.

---

## Data Steward

Responsável por:

- monitorar qualidade;
- catalogar dados;
- manter metadados;
- apoiar usuários;
- acompanhar inconsistências.

---

## Equipe Técnica

Responsável por:

- implementar controles;
- garantir disponibilidade;
- executar integrações;
- administrar bancos de dados;
- implementar mecanismos de segurança.

---

# 7. Domínios de Dados

Os dados do SIGMUN serão organizados em domínios.

Exemplos:

- Pessoas;
- Empresas;
- Imóveis;
- Servidores;
- Processos;
- Saúde;
- Educação;
- Assistência Social;
- Tributação;
- Financeiro;
- Patrimônio;
- Compras;
- Licitações;
- Protocolo;
- Obras;
- Agricultura;
- Meio Ambiente;
- Transporte;
- Documentos;
- Georreferenciamento.

Cada domínio possuirá um Data Owner formalmente designado.

---

# 8. Classificação dos Dados

Os dados deverão ser classificados conforme sua natureza.

## Dados Públicos

Informações passíveis de divulgação.

---

## Dados de Uso Interno

Informações restritas aos servidores.

---

## Dados Confidenciais

Informações protegidas por normas institucionais.

---

## Dados Pessoais

Informações protegidas pela LGPD.

---

## Dados Pessoais Sensíveis

Informações sujeitas a controles adicionais de segurança.

---

# 9. Ciclo de Vida dos Dados

Todos os dados deverão possuir gestão durante todo o seu ciclo de vida.

Etapas:

1. Criação.
2. Coleta.
3. Validação.
4. Armazenamento.
5. Compartilhamento.
6. Utilização.
7. Atualização.
8. Arquivamento.
9. Retenção.
10. Descarte seguro.

---

# 10. Dados Mestres (Master Data)

O SIGMUN adotará o conceito de Master Data.

Exemplos:

- Cadastro Único Municipal;
- Pessoas;
- Empresas;
- Imóveis;
- Logradouros;
- Órgãos;
- Secretarias;
- Servidores;
- Unidades Administrativas.

Nenhum módulo poderá manter cadastros duplicados desses dados.

---

# 11. Metadados

Todo dado corporativo deverá possuir metadados padronizados.

Exemplos:

- nome;
- descrição;
- domínio;
- proprietário;
- steward;
- origem;
- sistema de origem;
- periodicidade;
- classificação;
- sensibilidade;
- qualidade;
- regras de validação;
- histórico de alterações.

---

---

# 12. Gestão da Qualidade dos Dados (Data Quality)

A qualidade dos dados deverá ser monitorada continuamente para garantir que as informações utilizadas pelos processos administrativos sejam confiáveis, consistentes e adequadas à tomada de decisão.

## Dimensões da Qualidade

Os dados deverão atender aos seguintes critérios:

- precisão;
- completude;
- consistência;
- unicidade;
- validade;
- atualidade;
- integridade;
- disponibilidade;
- confiabilidade;
- rastreabilidade.

Toda inconsistência identificada deverá gerar um processo de tratamento.

---

# 13. Catálogo Corporativo de Dados

O SIGMUN deverá manter um Catálogo Corporativo de Dados (Data Catalog) contendo todos os ativos de dados institucionais.

Cada item do catálogo deverá conter, no mínimo:

- nome do ativo;
- descrição;
- domínio;
- proprietário (Data Owner);
- administrador (Data Steward);
- classificação;
- origem;
- sistema responsável;
- periodicidade de atualização;
- regras de negócio;
- restrições legais;
- políticas de retenção;
- integrações relacionadas.

O catálogo deverá estar disponível para consulta pelos usuários autorizados.

---

# 14. Glossário Corporativo de Negócio

Será mantido um Glossário Corporativo para padronizar conceitos utilizados em todas as secretarias.

Cada termo deverá possuir:

- nome;
- definição;
- área responsável;
- domínio;
- sinônimos;
- legislação relacionada;
- regras de utilização.

Exemplos:

- Contribuinte;
- Servidor Público;
- Processo Administrativo;
- Unidade Gestora;
- Empenho;
- Liquidação;
- Beneficiário;
- Família;
- Imóvel;
- Atendimento.

---

# 15. Linhagem dos Dados (Data Lineage)

O SIGMUN deverá registrar a origem e o percurso dos dados ao longo de todo o seu ciclo de vida.

A linhagem deverá permitir identificar:

- origem da informação;
- sistemas envolvidos;
- transformações realizadas;
- integrações executadas;
- usuários responsáveis;
- data e hora das alterações;
- destino dos dados.

Esse mecanismo apoiará auditorias, rastreabilidade e conformidade.

---

# 16. Gestão de Dados Mestres (Master Data Management - MDM)

Os Dados Mestres deverão possuir administração centralizada.

Objetivos:

- eliminar duplicidades;
- padronizar cadastros;
- garantir unicidade;
- facilitar integrações;
- melhorar a qualidade das informações.

O Cadastro Único Municipal será o principal repositório de Dados Mestres.

---

# 17. Gestão de Dados de Referência

Os Dados de Referência deverão possuir controle centralizado.

Exemplos:

- bairros;
- logradouros;
- estados;
- municípios;
- CNAE;
- CBO;
- CEP;
- códigos IBGE;
- Naturezas Jurídicas;
- órgãos públicos;
- unidades administrativas.

Alterações nesses dados deverão seguir fluxo formal de aprovação.

---

# 18. Compartilhamento de Dados

O compartilhamento de dados entre secretarias deverá observar:

- necessidade de negócio;
- competência legal;
- princípio do menor privilégio;
- classificação da informação;
- LGPD;
- trilhas de auditoria;
- políticas de segurança.

Sempre que possível, o compartilhamento ocorrerá por meio de APIs corporativas.

---

# 19. Governança das Integrações

Toda integração deverá possuir:

- responsável funcional;
- responsável técnico;
- contrato de integração;
- documentação;
- versionamento;
- monitoramento;
- mecanismos de autenticação;
- registros de auditoria.

As integrações deverão seguir a Arquitetura de Integração do SIGMUN.

---

# 20. Indicadores de Governança de Dados

A Governança de Dados deverá ser monitorada por indicadores.

| Indicador | Objetivo |
|-----------|----------|
| Índice de qualidade dos dados | Qualidade |
| Cadastros duplicados | Unicidade |
| Dados incompletos | Completude |
| Inconsistências identificadas | Controle |
| Inconsistências corrigidas | Melhoria contínua |
| Dados catalogados | Cobertura |
| Domínios governados | Evolução |
| APIs documentadas | Governança |
| Compartilhamentos autorizados | Conformidade |
| Auditorias realizadas | Controle |

---

# 21. Tratamento de Inconsistências

Toda inconsistência deverá possuir registro formal contendo:

- identificador;
- data;
- origem;
- domínio de dados;
- impacto;
- responsável;
- causa provável;
- ação corretiva;
- prazo;
- situação.

Os registros deverão ser acompanhados até sua resolução.

---

# 22. Auditoria de Dados

A auditoria deverá verificar periodicamente:

- qualidade;
- integridade;
- conformidade;
- acessos;
- alterações;
- compartilhamentos;
- retenção;
- descarte;
- conformidade com a LGPD;
- aderência às políticas institucionais.

Os resultados deverão ser apresentados ao Comitê de Governança de Dados.

---

# 23. Matriz RACI

| Atividade | Comitê de Governança | Data Owner | Data Steward | Equipe Técnica | Usuário |
|------------|----------------------|------------|---------------|----------------|---------|
| Definir políticas | A | C | C | I | I |
| Aprovar padrões | A | R | C | C | I |
| Manter catálogo | I | C | R | C | I |
| Monitorar qualidade | C | C | R | C | I |
| Corrigir inconsistências | I | A | R | C | I |
| Implementar controles técnicos | I | C | C | R | I |
| Utilizar dados | I | I | I | I | R |

**Legenda:**

- **R** – Responsável pela execução.
- **A** – Responsável pela aprovação.
- **C** – Consultado.
- **I** – Informado.

---

# 24. Integração com Outros Documentos

Este plano integra-se diretamente com:

- Arquitetura de Dados;
- Cadastro Único Municipal;
- Arquitetura de Integração;
- Arquitetura de Segurança;
- Gestão de Identidade e Acessos;
- LGPD;
- Business Intelligence;
- Analytics e Inteligência Artificial;
- Plano de Comunicação;
- Plano de Gestão das Partes Interessadas;
- Gestão de Riscos;
- Gestão da Qualidade;
- Plano de Trabalho do SIGMUN.

---

# 25. Revisão do Plano

Este plano deverá ser revisado:

- anualmente;
- após alterações legislativas;
- quando novos domínios de dados forem incorporados;
- após auditorias;
- após incidentes relevantes;
- quando houver mudanças significativas na arquitetura de dados.

---

# 26. Controle de Versões

| Versão | Data | Alteração | Responsável |
|---------|------|-----------|-------------|
| 1.0 | ____/____/______ | Criação do documento | Equipe SIGMUN |

---

# 27. Referências

## Frameworks

- DAMA-DMBOK2 – Data Management Body of Knowledge.
- COBIT 2019.
- TOGAF Standard.
- BABOK Guide.

## Normas

- ISO/IEC 38505 – Governance of Data.
- ISO 8000 – Data Quality.
- ISO/IEC 25012 – Data Quality Model.
- ISO/IEC 27001 – Segurança da Informação.
- Lei nº 13.709/2018 – Lei Geral de Proteção de Dados (LGPD).

---

# 28. Considerações Finais

A Governança de Dados constitui um dos pilares estratégicos do SIGMUN, reconhecendo a informação como um ativo institucional essencial para a prestação de serviços públicos, a transparência, a conformidade legal e a tomada de decisões.

Ao estabelecer papéis claros, processos padronizados, mecanismos de controle e indicadores de desempenho, este plano promove a qualidade, a integridade, a interoperabilidade e o uso responsável dos dados em toda a Administração Municipal.

Este documento deverá orientar todas as iniciativas relacionadas à gestão de dados do SIGMUN, assegurando que a informação seja administrada de forma ética, segura, integrada e alinhada aos objetivos estratégicos do Município.

---

---

**Documento:**013-Plano-de-Governanca-de-Dados.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
