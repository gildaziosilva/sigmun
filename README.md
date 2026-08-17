# SIGMUN — Sistema Integrado de Gestão Municipal

Projeto SIGMUN: plataforma para integração de processos, dados e serviços na administração pública municipal.

Sumário rápido

- **Documentação completa:** SIGMUN-Docs/
- **Guia de contribuição:** SIGMUN-Docs/00-Governanca/000E-GUIA-DE-CONTRIBUICAO.md
- **Status do projeto:** consulte `SIGMUN-Docs/Plano-de-Trabalho.md` e `SIGMUN-Docs/ROADMAP.md`

Como começar

1. Leia a documentação em `SIGMUN-Docs/`.
2. Configure seu ambiente Python (recomenda-se usar um virtualenv `.venv`).
3. Antes de abrir PRs, siga o guia de contribuição.

Arquivos sugeridos para o commit inicial

- `README.md` (este arquivo)
- `LICENSE` (adicionar licença do projeto)
- `.gitignore` (já presente)

Se quiser, posso criar também um `LICENSE` padrão e fazer o commit inicial.
# SIGMUN

## Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA

> Plataforma ERP Público para integração, gestão, governança e transformação digital da administração municipal.

---

## 1. Sobre o Projeto

O **SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA** é um projeto de ERP Público concebido para apoiar a gestão integrada das secretarias, órgãos, unidades administrativas e processos do município.

O projeto busca substituir a fragmentação causada por sistemas isolados, planilhas, controles paralelos e duplicidade de informações por uma arquitetura integrada, orientada a processos, dados, serviços e governança.

O SIGMUN é concebido para oferecer uma base tecnológica comum para:

- gestão administrativa;
- gestão financeira;
- contabilidade;
- compras e contratações;
- patrimônio;
- almoxarifado;
- recursos humanos;
- educação;
- saúde;
- assistência social;
- agricultura;
- obras;
- frota;
- tributos;
- planejamento;
- controladoria;
- procuradoria;
- transparência;
- ouvidoria;
- portal do cidadão;
- integrações governamentais;
- inteligência de dados e indicadores.

---

## 2. Objetivos

O projeto tem como objetivos principais:

1. integrar os processos da administração municipal;
2. eliminar ou reduzir retrabalho;
3. evitar duplicidade de informações;
4. estabelecer uma fonte confiável de dados institucionais;
5. promover interoperabilidade entre módulos e sistemas;
6. fortalecer governança, segurança e auditoria;
7. apoiar transparência e prestação de contas;
8. proporcionar rastreabilidade dos processos administrativos;
9. permitir evolução tecnológica contínua;
10. estabelecer uma arquitetura reutilizável para outros municípios.

---

## 3. Princípios

O SIGMUN adota como princípios estruturantes:

- **Transparência por padrão**
- **Segurança por princípio**
- **Classificação da Informação por política**
- **Aberto sempre que possível, restrito sempre que necessário**
- integração;
- interoperabilidade;
- rastreabilidade;
- auditabilidade;
- reutilização;
- modularidade;
- escalabilidade;
- qualidade;
- acessibilidade;
- sustentabilidade;
- evolução contínua.

---

## 4. Situação Atual

O projeto encontra-se em fase de **estruturação arquitetural, modelagem, especificação e preparação do ambiente de desenvolvimento**.

A documentação corporativa está sendo organizada antes da implementação progressiva dos módulos.

O primeiro domínio utilizado como referência para implementação é:

### Gestão de Compras e Contratações

Identificador do domínio:

```text
DOM-COMPRAS-001