# DICIONÁRIO DE DADOS DA PESQUISA

## Estudo Nacional da Transformação Digital dos Municípios Brasileiros

**Documento:** 003-Dicionario-de-Dados-da-Pesquisa.md

**Domínio:** 98 – Estudos e Pesquisas

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

---

# Controle de Versões

| Versão | Data | Descrição |
|---------|------|-----------|
| 1.0 | AAAA-MM-DD | Emissão inicial |

---

# Documentos Relacionados

- 001-Estudo-Nacional-da-Transformacao-Digital-dos-Municipios-Brasileiros.md
- 002-Metodologia-de-Coleta-de-Dados.md
- Catálogo Corporativo do Conhecimento
- Vocabulário Corporativo do SIGMUN
- Política de Governança de Dados

---

# 1. Finalidade

Este documento estabelece o Dicionário Oficial de Dados utilizado no Estudo Nacional da Transformação Digital dos Municípios Brasileiros.

Seu objetivo é padronizar as variáveis da pesquisa, garantindo uniformidade na coleta, armazenamento, integração, análise e publicação dos dados.

---

# 2. Estrutura das Variáveis

Cada variável deverá possuir, no mínimo, os seguintes metadados:

- Identificador da variável
- Nome técnico
- Nome de apresentação
- Descrição
- Categoria
- Domínio
- Tipo de dado
- Formato
- Unidade de medida (quando aplicável)
- Obrigatoriedade
- Permite valor nulo
- Valor padrão
- Fonte de dados
- Periodicidade de atualização
- Responsável pela informação
- Critérios de validação
- Exemplo de preenchimento
- Observações

---

# 3. Convenções de Nomenclatura

Os nomes técnicos deverão utilizar:

- letras minúsculas;
- palavras separadas por "_";
- nomes descritivos;
- sem acentuação;
- sem caracteres especiais.

Exemplos:

codigo_ibge

nome_municipio

populacao

despesa_anual_ti

despesa_locacao_software

quantidade_profissionais_ti

indice_maturidade_digital

---

# 4. Categorias de Dados

As variáveis serão agrupadas nas seguintes categorias:

- Identificação;
- Caracterização do Município;
- Estrutura Organizacional;
- Recursos Humanos;
- Custos de Pessoal;
- Custos de Software;
- Infraestrutura;
- Governança;
- Integração;
- Segurança;
- Serviços Digitais;
- Indicadores;
- Observações.

---

# 5. Variáveis de Identificação

## VAR-000001

Nome Técnico

codigo_ibge

Descrição

Código oficial do Município.

Tipo

Inteiro

Obrigatório

Sim

Fonte

IBGE

Exemplo

2905606

---

## VAR-000002

Nome Técnico

nome_municipio

Descrição

Nome oficial do Município.

Tipo

Texto

Obrigatório

Sim

Exemplo

Camacan

---

## VAR-000003

Nome Técnico

uf

Descrição

Unidade da Federação.

Tipo

Texto

Formato

UF

Exemplo

BA

---

## VAR-000004

Nome Técnico

regiao

Descrição

Região geográfica.

Valores

Norte

Nordeste

Centro-Oeste

Sudeste

Sul

---

# 6. Variáveis Demográficas

## VAR-000010

populacao

Descrição

População residente.

Tipo

Inteiro

Fonte

IBGE

---

## VAR-000011

area_km2

Descrição

Área territorial.

Tipo

Decimal

Unidade

km²

---

## VAR-000012

idhm

Descrição

Índice de Desenvolvimento Humano Municipal.

Tipo

Decimal

---

# 7. Recursos Humanos de TI

## VAR-000100

quantidade_profissionais_ti

Descrição

Quantidade total de profissionais de TI.

Tipo

Inteiro

---

## VAR-000101

quantidade_servidores_efetivos_ti

Tipo

Inteiro

---

## VAR-000102

quantidade_terceirizados_ti

Tipo

Inteiro

---

## VAR-000103

quantidade_estagiarios_ti

Tipo

Inteiro

---

# 8. Custos de Pessoal

## VAR-000200

despesa_anual_equipe_ti

Descrição

Despesa anual com equipe de TI.

Tipo

Moeda

---

## VAR-000201

despesa_capacitacao_ti

Tipo

Moeda

---

## VAR-000202

despesa_consultoria_ti

Tipo

Moeda

---

# 9. Custos com Software

## VAR-000300

despesa_locacao_software

Descrição

Despesa anual com locação/licenciamento/SaaS.

Tipo

Moeda

---

## VAR-000301

quantidade_softwares_contratados

Tipo

Inteiro

---

## VAR-000302

quantidade_modulos

Tipo

Inteiro

---

## VAR-000303

principal_fornecedor

Tipo

Texto

---

# 10. Infraestrutura

## VAR-000400

possui_datacenter

Tipo

Booleano

---

## VAR-000401

possui_nuvem

Tipo

Booleano

---

## VAR-000402

possui_backup

Tipo

Booleano

---

## VAR-000403

possui_firewall

Tipo

Booleano

---

# 11. Governança

## VAR-000500

possui_plano_diretor_ti

Tipo

Booleano

---

## VAR-000501

possui_governanca_digital

Tipo

Booleano

---

## VAR-000502

possui_politica_seguranca

Tipo

Booleano

---

# 12. Indicadores Calculados

As seguintes variáveis serão derivadas dos dados coletados:

- custo_ti_por_habitante;
- custo_software_por_habitante;
- percentual_receita_ti;
- percentual_receita_software;
- profissionais_ti_por_mil_servidores;
- indice_maturidade_digital;
- indice_integracao;
- indice_governanca.

Cada indicador terá fórmula documentada em documento específico.

---

# 13. Regras Gerais de Validação

As variáveis deverão observar regras como:

- tipo correto;
- faixa válida;
- domínio permitido;
- consistência lógica;
- ausência de duplicidade;
- integridade referencial.

---

# 14. Versionamento

Nenhuma variável poderá ser removida sem preservação do histórico.

Alterações deverão manter compatibilidade sempre que possível.

Variáveis obsoletas deverão ser marcadas como depreciadas.

---

# 15. Integração com o Catálogo Corporativo

Cada variável deverá possuir referência ao Catálogo Corporativo do Conhecimento.

Sempre que possível, deverá ser estabelecida ligação entre:

- conceito corporativo;
- entidade;
- API;
- indicador;
- requisito;
- módulo;
- documento.

---

# 16. Evolução

Novas variáveis poderão ser incorporadas mediante aprovação da Governança da Pesquisa.

Todas deverão seguir os padrões estabelecidos neste documento.

---

# 17. Disposições Finais

Este Dicionário de Dados constitui a referência oficial para definição das variáveis utilizadas no Estudo Nacional da Transformação Digital dos Municípios Brasileiros.

Sua utilização é obrigatória em todos os processos de coleta, armazenamento, integração, análise e publicação dos dados da pesquisa.