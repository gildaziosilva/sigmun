# 017 Arquitetura de Governanca de Dados



**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Arquitetura Corporativa

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



---



- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md



---



017-Governanca-de-Dados-e-Gestao-da-Informacao.md

# 1. Objetivo



Este documento estabelece a Arquitetura de Governança de Dados do SIGMUN, definindo princípios, papéis, processos, políticas e padrões para assegurar que os dados municipais sejam tratados como ativos estratégicos da Administração Pública.



A governança de dados visa garantir que as informações produzidas, armazenadas, compartilhadas e utilizadas pelo SIGMUN sejam confiáveis, íntegras, seguras, interoperáveis, rastreáveis e alinhadas às legislações vigentes, promovendo uma gestão pública orientada por dados (Data-Driven Government).



# 2. Princípios da Governança de Dados



A Governança de Dados do SIGMUN será baseada nos seguintes princípios:



dado como patrimônio público;

informação como ativo estratégico;

responsabilidade compartilhada;

transparência administrativa;

segurança da informação;

privacidade por padrão (Privacy by Design);

qualidade dos dados;

interoperabilidade;

padronização;

rastreabilidade;

reutilização da informação;

conformidade legal;

melhoria contínua.

# 3. Objetivos Estratégicos



A governança de dados busca:



eliminar duplicidade de informações;

aumentar a confiabilidade dos dados;

facilitar integração entre secretarias;

reduzir retrabalho;

apoiar decisões estratégicas;

fortalecer a transparência pública;

apoiar auditorias;

facilitar análises estatísticas;

preparar o município para Inteligência Artificial;

possibilitar políticas públicas baseadas em evidências.

# 4. Arquitetura Corporativa de Dados

                Fontes de Dados

                        │

                        ▼

             Coleta e Integração

                        │

                        ▼

          Validação e Qualidade dos Dados

                        │

                        ▼

      Catálogo Corporativo de Dados (Metadata)

                        │

                        ▼

      Dados Mestres (Master Data Management)

                        │

                        ▼

      Data Warehouse / Data Lake / Analytics

                        │

                        ▼

 BI • IA • Dashboards • Indicadores • Open Data

# 5. Ciclo de Vida dos Dados



Todo dado deverá possuir um ciclo de vida claramente definido.



Etapas:



criação;

captura;

validação;

armazenamento;

utilização;

compartilhamento;

atualização;

arquivamento;

retenção;

descarte seguro.

# 6. Classificação da Informação



Todos os dados do SIGMUN deverão possuir classificação.



Exemplo:



Classificação	Descrição

Pública	Informações de livre acesso

Uso Interno	Restrita aos servidores

Restrita	Informações administrativas sensíveis

Confidencial	Dados protegidos por legislação

Sigilosa	Informações protegidas por norma específica

# 7. Domínios de Dados



Os dados serão organizados por domínios de negócio.



Exemplos:



Cadastro Municipal

Pessoas

Empresas

Tributação

Saúde

Educação

Assistência Social

Agricultura

Meio Ambiente

Obras

Patrimônio

Compras

Licitações

Contratos

Financeiro

Recursos Humanos

Frotas

Protocolo

Ouvidoria

Defesa Civil

Turismo

Cultura

Esporte



Cada domínio possuirá responsáveis definidos.



# 8. Master Data Management (MDM)



O SIGMUN adotará um modelo corporativo de Dados Mestres.



Exemplos de entidades mestres:



Pessoa Física

Pessoa Jurídica

Servidor Público

Imóvel

Logradouro

Bairro

Unidade Administrativa

Escola

Unidade de Saúde

Veículo

Fornecedor

Produto

Processo Administrativo



Cada entidade possuirá um identificador único e permanente.



# 9. Catálogo Corporativo de Dados



Será mantido um catálogo central contendo:



descrição do dado;

significado de negócio;

origem;

sistema responsável;

formato;

periodicidade de atualização;

proprietário do dado;

responsável técnico;

classificação;

regras de qualidade;

legislação relacionada.

# 10. Metadados



Cada conjunto de dados possuirá metadados padronizados.



Incluindo:



nome;

descrição;

domínio;

tipo;

tamanho;

formato;

responsável;

data de criação;

última atualização;

política de retenção;

classificação de segurança.

# 11. Data Lineage (Linhagem dos Dados)



Toda transformação deverá ser rastreável.



A linhagem permitirá identificar:



Origem



↓



Sistema de origem



↓



Transformações



↓



Integrações



↓



Banco de Dados



↓



Data Warehouse



↓



Painéis



↓



Relatórios



↓



Indicadores



# 12. Qualidade dos Dados



Serão monitoradas dimensões de qualidade como:



completude;

consistência;

precisão;

unicidade;

atualidade;

integridade;

validade;

conformidade.



Indicadores deverão ser medidos continuamente.



# 13. Regras de Qualidade



Exemplos:



CPF válido;

CNPJ válido;

CEP válido;

datas consistentes;

endereço padronizado;

duplicidades identificadas;

campos obrigatórios preenchidos;

referências íntegras.

# 14. Padronização de Dados



Os dados seguirão padrões corporativos.



Exemplos:



nomes próprios;

endereços;

municípios;

códigos IBGE;

CNAE;

CID;

CBO;

unidades de medida;

moeda;

data e hora ISO-8601;

UTF-8.

# 15. Dados de Referência



Serão utilizados cadastros oficiais sempre que possível.



Exemplos:



IBGE;

Receita Federal;

Correios;

CNES;

TSE;

INEP;

SIAFI;

Tabelas SUS.

# 16. Papéis e Responsabilidades

Conselho de Governança de Dados



Responsável pelas diretrizes estratégicas.



Data Owner



Responsável pelo domínio de negócio.



Define:



regras;

políticas;

qualidade;

autorização de uso.

Data Steward



Responsável pela gestão operacional da qualidade.



Executa:



monitoramento;

saneamento;

catalogação;

documentação.

Data Custodian



Responsável técnico.



Executa:



armazenamento;

backup;

segurança;

infraestrutura;

disponibilidade.

Usuários de Dados



Utilizam os dados conforme suas permissões.



# 17. Compartilhamento de Dados



O compartilhamento observará:



necessidade de acesso;

finalidade;

menor privilégio;

LGPD;

segurança;

auditoria;

rastreabilidade.

# 18. Interoperabilidade Semântica



Os sistemas deverão utilizar definições comuns.



Exemplo:



"Pessoa"



Sempre significará a mesma entidade em todos os módulos.



Evita divergências conceituais.



# 19. Integração de Dados



Integrações utilizarão preferencialmente:



APIs REST;

Eventos;

Mensageria;

ETL;

ELT;

Arquivos padronizados;

OpenAPI;

JSON;

XML.

# 20. Open Data



Os dados públicos poderão ser disponibilizados em Portal de Dados Abertos.



Critérios:



anonimização;

atualização periódica;

formatos abertos;

documentação;

APIs públicas quando aplicável.

# 21. Retenção e Descarte



Cada categoria possuirá política específica.



Definições:



tempo mínimo;

prazo legal;

arquivamento;

descarte seguro;

registro do descarte.

# 22. Conformidade com a LGPD



A governança deverá assegurar:



finalidade;

adequação;

necessidade;

transparência;

segurança;

prevenção;

responsabilização;

prestação de contas.

# 23. Auditoria de Dados



Serão registradas:



alterações;

exclusões;

importações;

exportações;

integrações;

correções;

acessos.

# 24. Indicadores da Governança



Exemplos:



percentual de cadastros completos;

registros duplicados;

tempo médio de atualização;

qualidade por domínio;

dados catalogados;

integrações padronizadas;

incidentes de qualidade;

conformidade com LGPD;

percentual de metadados preenchidos.

# 25. Gestão de Dados Analíticos



Os ambientes analíticos deverão utilizar:



Data Warehouse;

Data Lake;

Cubos Analíticos;

Modelos Dimensionais;

Indicadores Corporativos.



Os dados analíticos deverão ser derivados dos dados transacionais governados.



# 26. Inteligência Artificial e Dados



Os modelos de IA deverão utilizar apenas dados:



catalogados;

autorizados;

auditáveis;

íntegros;

atualizados;

anonimizados quando necessário.



As decisões automatizadas deverão ser explicáveis e passíveis de auditoria.



# 27. Capacitação e Cultura de Dados



A governança de dados depende de pessoas. O SIGMUN promoverá programas permanentes de capacitação para servidores, gestores e equipes técnicas, incentivando a cultura orientada a dados, o uso responsável das informações e a compreensão dos papéis definidos nesta arquitetura.



As ações poderão incluir:



treinamentos periódicos;

campanhas de conscientização;

guias de boas práticas;

trilhas de aprendizagem por perfil;

avaliação contínua da maturidade em governança de dados.

# 28. Maturidade da Governança



A evolução da governança será acompanhada por níveis de maturidade.



Nível	Descrição

1	Inicial (processos informais)

2	Repetível (práticas padronizadas)

3	Definido (governança institucionalizada)

4	Gerenciado (indicadores e monitoramento)

5	Otimizado (melhoria contínua e automação)



A evolução deverá ser revisada periodicamente pelo Comitê de Governança de Dados.



# 29. Benefícios Esperados



A implantação da Governança de Dados proporcionará:



informações mais confiáveis e consistentes;

integração efetiva entre secretarias e órgãos municipais;

redução de inconsistências e retrabalho;

maior conformidade com a LGPD e demais normas;

suporte à tomada de decisão baseada em evidências;

fortalecimento da transparência e do controle social;

preparação para iniciativas de Business Intelligence, Analytics e Inteligência Artificial;

aumento da eficiência administrativa e da qualidade dos serviços públicos.

Conclusão



A Arquitetura de Governança de Dados e Gestão da Informação estabelece os fundamentos para que o SIGMUN trate os dados municipais como um ativo estratégico, promovendo qualidade, interoperabilidade, segurança, transparência e conformidade legal. Ao institucionalizar papéis, processos e padrões de governança, o município cria uma base sólida para a transformação digital, o governo orientado por dados e a evolução contínua de seus serviços públicos.



---



**Documento:**017-Arquitetura-de-Governanca-de-Governaca-de-Dados.md

**Última atualização:** 2026-08-03

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

