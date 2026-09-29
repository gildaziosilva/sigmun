"""Conteúdo de negócio dos domínios DOM-TEL e DOM-IMO para a geração
dos artefatos `001`-`026`.

Reúne o conhecimento que **não** deriva do código-fonte (atores, processos,
capacidades, requisitos e critérios). O gerador
`gerar_artefatos_territoriais.py` combina estes dados com a extração técnica do
código (modelos, endpoints, casos de uso e testes) para produzir os artefatos.

As regras aqui declaradas são as mesmas implementadas em
`src/modules/*/domain/entities/*`; divergências são defeitos a corrigir na
origem, não neste arquivo.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations


def __getitem__(nome: str) -> object:
    """Permite acessar os conjuntos de dados por índice: `dados["TEL_REGRAS"]`.

    O gerador referencia os conjuntos pelo nome montado em tempo de execução
    (ex.: `f"{prefixo}_REGRAS"`); este accessor evita repetir o prefixo em cada
    chamada e mantém a listagem de atributos acessível para ferramentas.
    """
    return globals()[nome]


DOMINIOS = {
    "TEL": {
        "codigo": "DOM-TEL",
        "dominio": "Gestão Territorial",
        "modulo": "sigmun_territorial",
        "schema": "tel",
        "prefixo": "/api/v1/tel",
        "migracao": "alembic/versions/20260929_01_dom_tel_models.py",
        "migracao_id": "20260929_01_dom_tel_models",
        "rotulo": "Gestão Territorial",
        "prefixo_regra": "TEL",
        "entidades": [
            ("Bairro", "Divisão territorial (bairro, distrito, setor ou zona rural)."),
            ("Logradouro", "Logradouro público vinculado a uma divisão territorial."),
            ("PlantaGenericaValores", "Valores unitários por ano, divisão e ocupação."),
            ("Georreferencia", "Georreferência de bairro ou logradouro."),
        ],
        "variaveis": (
            ("Tipos de divisão", "bairro, distrito, setor, zona_rural"),
            ("Tipos de logradouro", "rua, avenida, travessa, praca, rodovia, estrada, alameda, parque, outro"),
            ("Situações de divisão", "ativo, inativo"),
            ("Situações de logradouro", "ativo, em_obra, inativo"),
            ("Ocupações", "residencial, comercial, industrial, institucional, misto, terreno"),
            ("Situações da planta", "rascunho, vigente, revogada"),
            ("Datuns", "sirgas2000, sad69, wgs84"),
            ("Geometrias", "ponto, linha, poligono"),
        ),
    },
    "IMO": {
        "codigo": "DOM-IMO",
        "dominio": "Cadastro Imobiliário",
        "modulo": "sigmun_cadastro_imobiliario",
        "schema": "imo",
        "prefixo": "/api/v1/imo",
        "migracao": "alembic/versions/20260929_02_dom_imo_models.py",
        "migracao_id": "20260929_02_dom_imo_models",
        "rotulo": "Cadastro Imobiliário",
        "prefixo_regra": "IMO",
        "entidades": [
            ("Imovel", "Unidade imobiliária (lote) com inscrição definitiva."),
            ("ProprietarioImovel", "Vínculo de titularidade entre pessoa e imóvel."),
            ("AvaliacaoImovel", "Avaliação do valor venal para um exercício."),
            ("CaracteristicaImovel", "Característica construtiva do imóvel."),
            ("GeometriaImovel", "Geometria georreferenciada do lote."),
        ],
        "variaveis": (
            ("Tipos de imóvel", "lote, casa, apartamento, loja, galpao, terreno, outro"),
            ("Situações do imóvel", "ativo, inativo, em_obra, desocupado, demolido"),
            ("Tipos de propriedade", "proprio, alugado, cedido, invencionado"),
            ("Vínculos", "titular, comodato, arrendamento, usufruto, parceiro"),
            ("Naturezas da obra", "residencial, comercial, industrial, institucional, mista, nao_aplicavel"),
            ("Situações da avaliação", "rascunho, concluida, cancelada"),
            ("Datuns", "sirgas2000, sad69, wgs84"),
            ("Geometrias", "ponto, linha, poligono"),
        ),
    },
    "GEO": {
        "codigo": "DOM-GEO",
        "dominio": "Geoinformação Municipal",
        "modulo": "sigmun_geoinformacao",
        "schema": "geo",
        "prefixo": "/api/v1/geo",
        "migracao": "alembic/versions/20260929_03_dom_geo_models.py",
        "migracao_id": "20260929_03_dom_geo_models",
        "rotulo": "Geoinformação Municipal",
        "prefixo_regra": "GEO",
        "entidades": [
            ("CamadaMapa", "Camada cartográfica disponibilizada no geoportal."),
            ("MapaSig", "Mapa publicado no geoportal municipal."),
            ("MapaCamada", "Vínculo de composição entre mapa e camada."),
            ("FeatureGeo", "Elemento geoespacial (ponto de interesse) de uma camada."),
            ("ServicoGeo", "Serviço geoespacial publicado (WMS, WFS, WMTS, XYZ ou REST)."),
        ],
        "variaveis": (
            ("Tipos de camada", "ortofoto, hipsometria, hipsografia, topografia, hidrografia, uso_solo, vegetacao, malha_urbana, infraestrutura, cadastro_territorial, outro"),
            ("Formatos de camada", "geotiff, shapefile, geojson, kml, postgis, wms, wfs, wmts, xyz, vetorial"),
            ("Situações da camada", "rascunho, ativa, desativada"),
            ("Tipos de mapa", "tematico, cadastral, basemap, infraestrutura, ambiental, outro"),
            ("Situações do mapa", "rascunho, publicado, arquivado"),
            ("Protocolos de serviço", "wms, wfs, wmts, xyz, rest"),
            ("Situações do serviço", "ativo, inativo, manutencao"),
            ("Datuns", "sirgas2000, sad69, wgs84"),
            ("Geometrias", "ponto, linha, poligono"),
        ),
    },
    "OBR": {
        "codigo": "DOM-OBR",
        "dominio": "Obras e Infraestrutura",
        "modulo": "sigmun_obras",
        "schema": "obr",
        "prefixo": "/api/v1/obr",
        "migracao": "alembic/versions/20260929_04_dom_obr_models.py",
        "migracao_id": "20260929_04_dom_obr_models",
        "rotulo": "Obras e Infraestrutura",
        "prefixo_regra": "OBR",
        "entidades": [
            ("Obra", "Obra pública acompanhada quanto ao avanço físico e financeiro."),
            ("MedicaoObra", "Medição físico-financeira de avanço da obra."),
            ("EtapaObra", "Etapa de execução fisicamente verificável da obra."),
            ("DespesaObra", "Desembolso financeiro vinculado à obra."),
            ("VistoriaObra", "Vistoria fiscalizadora com parecer sobre o avanço verificado."),
        ],
        "variaveis": (
            ("Tipos de obra", "pavimentacao, drenagem, construcao, reforma, iluminacao, saneamento, ponte, praca, quadra, outro"),
            ("Situações da obra", "planejada, em_licitacao, contratada, em_execucao, suspensa, concluida, cancelada"),
            ("Tipos de contratação", "licitacao, dispensa, inexigibilidade, convenio, contrato_direto"),
            ("Fontes de recurso", "orcamento_proprio, convenio, convenio_estadual, convenio_federal, transferencia, operacao_credito, outro"),
            ("Tipos de medição", "avanco, etapa, final, revisional"),
            ("Situações da medição", "registrada, conferida, aprovada, glosada, cancelada"),
            ("Tipos de despesa", "medicao, repasse, material, mao_de_obra, tributos, custos, outro"),
            ("Tipos de etapa", "projeto, terraplanagem, fundacao, estrutura, acabamento, instalacao, pavimentacao, paisagismo, recepcao"),
            ("Situações da etapa", "pendente, em_execucao, concluida, atrasada, cancelada"),
            ("Tipos de vistoria", "periodica, parcial, final, recepcao"),
            ("Pareceres da vistoria", "aprovado, aprovado_com_ressalvas, reprovado"),
        ),
    },
}



# ============================================================================
# DOM-TEL — Atores e capacidades
# ============================================================================

TEL_ATORES = [
    {
        "id": "AT-TEL-001",
        "nome": "Técnico de cadastro imobiliário",
        "tipo": "Servidor municipal",
        "papel": "Mantém o cadastro territorial e responde pela consistência dos códigos cadastrais.",
        "decisoes": "Cadastra e altera divisões territoriais e logradouros; inativa logradouros que deixaram de existir.",
        "sistemas": "SIGMUN — Gestão Territorial",
        "capacidades": "CAP-TEL-001, CAP-TEL-002",
    },
    {
        "id": "AT-TEL-002",
        "nome": "Comissão de Valores da Planta",
        "tipo": "Colegiado municipal",
        "papel": "Define os valores unitários de terreno e construção por divisão, ocupação e exercício.",
        "decisoes": "Elabora a planta em rascunho, aprova sua vigência e revoga plantas superadas.",
        "sistemas": "SIGMUN — Gestão Territorial; legislação municipal",
        "capacidades": "CAP-TEL-003",
    },
    {
        "id": "AT-TEL-003",
        "nome": "Fiscal de tributos",
        "tipo": "Servidor municipal",
        "papel": "Consulta os valores vigentes para instruir lançamentos e contestações.",
        "decisoes": "Não altera a planta; apenas consulta e solicita correção.",
        "sistemas": "SIGMUN — Gestão Territorial; SIGMUN — Tributos",
        "capacidades": "CAP-TEL-004",
    },
    {
        "id": "AT-TEL-004",
        "nome": "Técnico de georreferenciamento",
        "tipo": "Servidor municipal",
        "papel": "Registra a georreferência obtida em levantamento de campo ou base cartográfica.",
        "decisoes": "Registra e revoga georreferências, definindo datum e vértices.",
        "sistemas": "SIGMUN — Gestão Territorial; SIGMUN — Geoinformação",
        "capacidades": "CAP-TEL-005",
    },
    {
        "id": "AT-TEL-005",
        "nome": "Cartório de registro de imóveis",
        "tipo": "Entidade externa",
        "papel": "Fornece matrículas e dados de lote para conferência do cadastro municipal.",
        "decisoes": "Não altera o sistema; participa da conferência cadastral.",
        "sistemas": "Cartório",
        "capacidades": "CAP-TEL-002",
    },
]

TEL_CAPACIDADES = [
    {
        "id": "CAP-TEL-001",
        "nome": "Cadastro de divisões territoriais",
        "descricao": "Manter bairros, distritos, setores e zonas rurais com código único, população estimada e área.",
        "processos": "PRO-TEL-001",
        "regras": "RN-TEL-001, RN-TEL-006",
        "atores": "AT-TEL-001",
    },
    {
        "id": "CAP-TEL-002",
        "nome": "Cadastro de logradouros públicos",
        "descricao": "Manter logradouros vinculados a uma divisão territorial, com tipo, CEP e numeração.",
        "processos": "PRO-TEL-002",
        "regras": "RN-TEL-002, RN-TEL-006",
        "atores": "AT-TEL-001, AT-TEL-005",
    },
    {
        "id": "CAP-TEL-003",
        "nome": "Gestão da planta genérica de valores",
        "descricao": "Elaborar, ativar e revogar os valores unitários por ano, divisão e ocupação.",
        "processos": "PRO-TEL-003",
        "regras": "RN-TEL-003, RN-TEL-004",
        "atores": "AT-TEL-002",
    },
    {
        "id": "CAP-TEL-004",
        "nome": "Consulta de valores vigentes",
        "descricao": "Disponibilizar a planta vigente por ano, divisão e ocupação, inclusive para o DOM-IMO.",
        "processos": "PRO-TEL-004",
        "regras": "RN-TEL-003",
        "atores": "AT-TEL-002, AT-TEL-003",
    },
    {
        "id": "CAP-TEL-005",
        "nome": "Georreferenciamento territorial",
        "descricao": "Registrar a posição geográfica de divisões e logradouros, com datum, vértices e precisão.",
        "processos": "PRO-TEL-005",
        "regras": "RN-TEL-005",
        "atores": "AT-TEL-004",
    },
]


TEL_PROCESSOS = [
    {
        "id": "PRO-TEL-001",
        "nome": "Manter divisão territorial",
        "gatilho": "Levantamento censitário, criação de nova área ou alteração de limites.",
        "objetivo": "Garantir divisões territoriais codificadas e consistentes.",
        "entradas": "Código; nome; tipo; população estimada; área em km²",
        "saidas": "Divisão territorial cadastrada ou atualizada",
        "passos": [
            "Verificar se o código já está cadastrado (RN-TEL-001).",
            "Preencher os dados da divisão territorial.",
            "Gravar a divisão e registrar autoria e data.",
        ],
        "regras": "RN-TEL-001, RN-TEL-006",
    },
    {
        "id": "PRO-TEL-002",
        "nome": "Manter logradouro",
        "gatilho": "Pavimentação nova, alteração de nome ou mudança de situação.",
        "objetivo": "Manter a malha viária codificada e vinculada ao bairro.",
        "entradas": "Código; nome; divisão territorial; tipo; CEP; numeração inicial e final",
        "saidas": "Logradouro cadastrado, atualizado ou excluído",
        "passos": [
            "Selecionar a divisão territorial de vinculação (RN-TEL-002).",
            "Verificar a unicidade do código do logradouro (RN-TEL-002).",
            "Informar tipo, CEP e faixa de numeração.",
            "Gravar o logradouro vinculado.",
        ],
        "regras": "RN-TEL-002, RN-TEL-006",
    },
    {
        "id": "PRO-TEL-003",
        "nome": "Elaborar e aprovar a planta de valores",
        "gatilho": "Início do exercício fiscal ou alteração da legislação de valores.",
        "objetivo": "Estabelecer os valores unitários que sustentam o valor venal.",
        "entradas": "Ano; divisão; ocupação; valor do terreno; valor da construção; alíquota; legislação",
        "saidas": "Planta genérica de valores vigente",
        "passos": [
            "Elaborar a planta em rascunho, conforme a legislação vigente.",
            "Verificar se já existe planta vigente para o mesmo ano, divisão e ocupação (RN-TEL-003).",
            "Ativar a planta, tornando-a referência do exercício (RN-TEL-004).",
            "Quando superada, revogar a planta anterior com justificativa (RN-TEL-004).",
        ],
        "regras": "RN-TEL-003, RN-TEL-004",
    },
    {
        "id": "PRO-TEL-004",
        "nome": "Consultar planta de valores vigente",
        "gatilho": "Necessidade de apurar o valor unitário de um imóvel.",
        "objetivo": "Recuperar de forma determinística a planta aplicável.",
        "entradas": "Ano; divisão territorial; ocupação",
        "saidas": "Valores unitários vigentes; alíquota; legislação",
        "passos": [
            "Informar ano, divisão e ocupação.",
            "Localizar a planta com situação vigente (RN-TEL-003).",
            "Retornar os valores; sem planta vigente, informar a ausência.",
        ],
        "regras": "RN-TEL-003",
    },
    {
        "id": "PRO-TEL-005",
        "nome": "Registrar georreferência",
        "gatilho": "Levantamento de campo, atualização cartográfica ou georreferenciamento legal.",
        "objetivo": "Associar a divisões e logradouros suas coordenadas.",
        "entradas": "Referência territorial; tipo de geometria; vértices; datum; precisão; data do levantamento",
        "saidas": "Georreferência registrada",
        "passos": [
            "Selecionar a divisão ou o logradouro de referência, nunca ambos (RN-TEL-005).",
            "Informar o tipo de geometria e os vértices correspondentes (RN-TEL-005).",
            "Definir o datum e a precisão do levantamento.",
            "Gravar a georreferência.",
        ],
        "regras": "RN-TEL-005",
    },
]

TEL_REGRAS = [
    {
        "id": "RN-TEL-001",
        "titulo": "Unicidade do Código da Divisão Territorial",
        "tipo": "Restrição",
        "processo": "PRO-TEL-001",
        "descricao": "O código da divisão territorial é único no cadastro municipal; código e nome são obrigatórios.",
        "justificativa": "O código é a chave natural usada pelo cadastro imobiliário e pelas bases cartográficas.",
        "garantia": "Restrição UNIQUE em `tel.bairros.codigo` e validação em `Bairro.validar()`.",
    },
    {
        "id": "RN-TEL-002",
        "titulo": "Unicidade do Logradouro e Vinculação Territorial",
        "tipo": "Restrição",
        "processo": "PRO-TEL-002",
        "descricao": "O código do logradouro é único e todo logradouro pertence a uma divisão territorial cadastrada.",
        "justificativa": "A malha viária é referenciada pelo cadastro imobiliário e pelo georreferenciamento.",
        "garantia": "Restrição UNIQUE em `tel.logradouros.codigo` e validação de `bairro_id`.",
    },
    {
        "id": "RN-TEL-003",
        "titulo": "Unicidade da Planta Vigente",
        "tipo": "Restrição",
        "processo": "PRO-TEL-003",
        "descricao": "Existe no máximo uma planta vigente para cada combinação de ano, divisão e ocupação.",
        "justificativa": "Garante que o cálculo do valor venal tenha referência única e determinística.",
        "garantia": "Índice único parcial `uq_tel_planta_vigente` e verificação na ativação.",
    },
    {
        "id": "RN-TEL-004",
        "titulo": "Ciclo de Vida da Planta Genérica de Valores",
        "tipo": "Máquina de estados",
        "processo": "PRO-TEL-003",
        "descricao": "A planta percorre `RASCUNHO -> VIGENTE -> REVOGADA`, sem retorno a partir de `REVOGADA`; a revogação exige justificativa e somente plantas em rascunho podem ser editadas.",
        "justificativa": "Preserva a memória histórica dos valores aplicados a cada exercício.",
        "garantia": "Transições em `PlantaGenericaValores.ativar()` e `.revogar()`.",
    },
    {
        "id": "RN-TEL-005",
        "titulo": "Integridade da Georreferência",
        "tipo": "Restrição",
        "processo": "PRO-TEL-005",
        "descricao": "A georreferência exige datum suportado, está vinculada a uma divisão **ou** a um logradouro (nunca a ambos), e seus vértices são validados quanto à faixa de coordenadas e à quantidade mínima do tipo de geometria.",
        "justificativa": "Coordenadas inválidas ou referências ambíguas corromperiam a base cartográfica.",
        "garantia": "Check `ck_tel_geo_referencia` e validação em `Georreferencia.validar()`.",
    },
    {
        "id": "RN-TEL-006",
        "titulo": "Proteção contra Exclusão com Dependências",
        "tipo": "Restrição",
        "processo": "PRO-TEL-001",
        "descricao": "Uma divisão territorial com logradouros ativos não pode ser excluída.",
        "justificativa": "A exclusão deixaria logradouros órfãos e quebraria o cadastro imobiliário.",
        "garantia": "Verificação de dependências em `ExcluirBairroUseCase`.",
    },
]


TEL_RF = [
    ("RF-TEL-001", "O sistema deve permitir cadastrar, alterar, listar, consultar e excluir divisões territoriais.", "Essencial", "CAP-TEL-001", "RN-TEL-001, RN-TEL-006",
     "POST /api/v1/tel/bairros; GET /api/v1/tel/bairros; GET /api/v1/tel/bairros/{bairro_id}; PATCH /api/v1/tel/bairros/{bairro_id}; DELETE /api/v1/tel/bairros/{bairro_id}"),
    ("RF-TEL-002", "O sistema deve permitir consultar uma divisão territorial pelo código cadastral.", "Essencial", "CAP-TEL-001", "RN-TEL-001",
     "GET /api/v1/tel/bairros/codigo/{codigo}"),
    ("RF-TEL-003", "O sistema deve permitir cadastrar, alterar, listar, consultar e excluir logradouros vinculados a uma divisão territorial.", "Essencial", "CAP-TEL-002", "RN-TEL-002, RN-TEL-006",
     "POST /api/v1/tel/logradouros; GET /api/v1/tel/logradouros; GET /api/v1/tel/logradouros/{logradouro_id}; PATCH /api/v1/tel/logradouros/{logradouro_id}; DELETE /api/v1/tel/logradouros/{logradouro_id}"),
    ("RF-TEL-004", "O sistema deve permitir listar os logradouros de uma divisão territorial.", "Essencial", "CAP-TEL-002", "RN-TEL-002",
     "GET /api/v1/tel/bairros/{bairro_id}/logradouros"),
    ("RF-TEL-005", "O sistema deve permitir cadastrar a planta genérica de valores em rascunho ou já vigente.", "Essencial", "CAP-TEL-003", "RN-TEL-003, RN-TEL-004",
     "POST /api/v1/tel/plantas-valores"),
    ("RF-TEL-006", "O sistema deve permitir ativar uma planta em rascunho e revogar uma planta vigente com justificativa.", "Essencial", "CAP-TEL-003", "RN-TEL-004",
     "POST /api/v1/tel/plantas-valores/{planta_id}/ativar; POST /api/v1/tel/plantas-valores/{planta_id}/revogar"),
    ("RF-TEL-007", "O sistema deve permitir editar os valores de uma planta somente enquanto ela estiver em rascunho.", "Essencial", "CAP-TEL-003", "RN-TEL-004",
     "PATCH /api/v1/tel/plantas-valores/{planta_id}"),
    ("RF-TEL-008", "O sistema deve permitir consultar a planta vigente por ano, divisão territorial e ocupação.", "Essencial", "CAP-TEL-004", "RN-TEL-003",
     "GET /api/v1/tel/plantas-valores/vigente"),
    ("RF-TEL-009", "O sistema deve permitir listar as plantas, opcionalmente filtradas por divisão territorial.", "Importante", "CAP-TEL-003", "",
     "GET /api/v1/tel/plantas-valores; GET /api/v1/tel/plantas-valores/{planta_id}"),
    ("RF-TEL-010", "O sistema deve permitir registrar, listar, consultar e excluir georreferências.", "Essencial", "CAP-TEL-005", "RN-TEL-005",
     "POST /api/v1/tel/georreferencias; GET /api/v1/tel/georreferencias; GET /api/v1/tel/georreferencias/{georreferencia_id}; DELETE /api/v1/tel/georreferencias/{georreferencia_id}"),
    ("RF-TEL-011", "O sistema deve permitir filtrar as georreferências por divisão territorial ou por logradouro.", "Importante", "CAP-TEL-005", "RN-TEL-005",
     "GET /api/v1/tel/georreferencias/referencia"),
]

TEL_CU = [
    ("CU-TEL-001", "Cadastrar divisão territorial", "AT-TEL-001", "CAP-TEL-001", "O servidor está autenticado e possui permissão de cadastro territorial.",
     "Informar código, nome, tipo, população estimada e área; verificar a unicidade do código (RN-TEL-001); gravar e registrar autoria e data.",
     "A divisão territorial está cadastrada e ativa.", "RN-TEL-001", "CadastrarBairroUseCase"),
    ("CU-TEL-002", "Alterar situação de divisão territorial", "AT-TEL-001", "CAP-TEL-001", "A divisão territorial existe.",
     "Informar a nova situação (ativo ou inativo); aplicar a alteração e registrar a data da modificação.",
     "A divisão territorial está na situação informada.", "RN-TEL-001", "AtualizarBairroUseCase"),
    ("CU-TEL-003", "Excluir divisão territorial", "AT-TEL-001", "CAP-TEL-001", "A divisão territorial existe.",
     "Solicitar a exclusão; verificar logradouros ativos vinculados (RN-TEL-006); havendo dependências, recusar com HTTP 409; caso contrário, excluir logicamente.",
     "A divisão está excluída logicamente e preserva o histórico.", "RN-TEL-006", "ExcluirBairroUseCase"),
    ("CU-TEL-004", "Cadastrar logradouro", "AT-TEL-001", "CAP-TEL-002", "A divisão territorial de vinculação existe.",
     "Selecionar a divisão e informar código, nome, tipo, CEP e numeração; verificar a unicidade do código (RN-TEL-002); gravar o logradouro vinculado.",
     "O logradouro está cadastrado e vinculado à divisão territorial.", "RN-TEL-002", "CadastrarLogradouroUseCase"),
    ("CU-TEL-005", "Elaborar planta genérica de valores", "AT-TEL-002", "CAP-TEL-003", "A divisão territorial de referência existe.",
     "Informar ano, divisão, ocupação, valores unitários, alíquota e legislação; gravar em rascunho; se solicitado, verificar a unicidade de planta vigente (RN-TEL-003) e ativar.",
     "A planta está cadastrada em rascunho ou vigente.", "RN-TEL-003, RN-TEL-004", "CadastrarPlantaValoresUseCase"),
    ("CU-TEL-006", "Ativar planta genérica de valores", "AT-TEL-002", "CAP-TEL-003", "A planta existe e está em rascunho.",
     "Solicitar a ativação; verificar se já existe planta vigente para a mesma combinação (RN-TEL-003); não havendo conflito, passar a vigente (RN-TEL-004).",
     "A planta está vigente e é a referência do exercício.", "RN-TEL-003, RN-TEL-004", "AtivarPlantaValoresUseCase"),
    ("CU-TEL-007", "Revogar planta genérica de valores", "AT-TEL-002", "CAP-TEL-003", "A planta existe e está vigente.",
     "Informar a justificativa; o sistema exige a justificativa e altera a situação para revogada (RN-TEL-004).",
     "A planta está revogada e preserva o histórico.", "RN-TEL-004", "RevogarPlantaValoresUseCase"),
    ("CU-TEL-008", "Consultar planta de valores vigente", "AT-TEL-003", "CAP-TEL-004", "Não há precondição.",
     "Informar ano, divisão e ocupação; retornar a planta vigente ou informar a ausência (RN-TEL-003).",
     "Os valores vigentes foram obtidos ou a ausência foi informada.", "RN-TEL-003", "— (consulta ao repositório)"),
    ("CU-TEL-009", "Registrar georreferência", "AT-TEL-004", "CAP-TEL-005", "A divisão ou o logradouro de referência existe.",
     "Selecionar a referência territorial (divisão ou logradouro, nunca ambas); informar geometria, vértices, datum e precisão; validar e gravar (RN-TEL-005).",
     "A georreferência está registrada e associada à referência.", "RN-TEL-005", "RegistrarGeorreferenciaUseCase"),
]


TEL_HU = [
    ("HU-TEL-001", "Manter o cadastro de divisões territoriais", "Como técnico de cadastro imobiliário",
     "cadastrar e manter bairros, distritos, setores e zonas rurais", "dispor da malha territorial codificada e consistente", "CAP-TEL-001",
     "RN-TEL-001, RN-TEL-006",
     "Dado um código inexistente, quando o técnico cadastra a divisão, então a divisão é criada e fica ativa.;"
     "Dado um código já cadastrado, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-TEL-001).;"
     "Dado uma divisão com logradouros ativos, quando o técnico tenta excluir, então o sistema recusa com HTTP 409 (RN-TEL-006)."),
    ("HU-TEL-002", "Manter a malha de logradouros", "Como técnico de cadastro imobiliário",
     "cadastrar logradouros vinculados à divisão territorial correspondente", "identificar univocamente cada endereço do município", "CAP-TEL-002",
     "RN-TEL-002",
     "Dado um bairro existente, quando o técnico cadastra o logradouro, então o logradouro fica vinculado ao bairro.;"
     "Dado um bairro inexistente, quando o técnico cadastra o logradouro, então o sistema recusa com HTTP 404 (RN-TEL-002).;"
     "Dado um código de logradouro já cadastrado, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-TEL-002)."),
    ("HU-TEL-003", "Elaborar e aprovar a planta de valores do exercício", "Como membro da Comissão de Valores da Planta",
     "elaborar, ativar e revogar plantas genéricas de valores", "estabelecer os valores unitários que sustentam o valor venal", "CAP-TEL-003",
     "RN-TEL-003, RN-TEL-004",
     "Dado uma planta em rascunho, quando a comissão ativa e não há conflito, então a planta passa a vigente.;"
     "Dado que já existe planta vigente para a mesma combinação, quando a comissão ativa outra, então o sistema recusa com HTTP 409 (RN-TEL-003).;"
     "Dado uma planta vigente, quando a comissão revoga com justificativa, então a planta passa a revogada (RN-TEL-004).;"
     "Dado uma planta sem justificativa, quando a comissão tenta revogar, então o sistema recusa (RN-TEL-004).;"
     "Dado uma planta vigente ou revogada, quando se tenta editar valores, então o sistema recusa (RN-TEL-004)."),
    ("HU-TEL-004", "Consultar a planta de valores vigente", "Como fiscal de tributos",
     "consultar os valores unitários vigentes por ano, divisão e ocupação", "instruir lançamentos e contestações com base na tabela oficial", "CAP-TEL-004",
     "RN-TEL-003",
     "Dado uma planta vigente para a combinação, quando o fiscal consulta, então os valores unitários e a alíquota são retornados.;"
     "Dado que não há planta vigente para a combinação, quando o fiscal consulta, então o sistema responde HTTP 404."),
    ("HU-TEL-005", "Registrar a georreferência do território", "Como técnico de georreferenciamento",
     "registrar a posição geográfica de divisões e logradouros", "apoiar o georreferenciamento legal e a produção cartográfica", "CAP-TEL-005",
     "RN-TEL-005",
     "Dado uma divisão existente, quando o técnico registra um polígono com ao menos 3 vértices válidos, então a georreferência é criada.;"
     "Dado que nenhum ou ambos os vínculos são informados, quando o técnico registra, então o sistema recusa (RN-TEL-005).;"
     "Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-TEL-005).;"
     "Dado uma coordenada fora da faixa do datum, quando o técnico registra, então o sistema recusa (RN-TEL-005)."),
]

TEL_RNF = [
    ("RNF-TEL-001", "Desempenho", "As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens.",
     "Teste de integração verificando o parâmetro `page_size` e a resposta paginada."),
    ("RNF-TEL-002", "Integridade", "As invariantes de unicidade e de vínculo devem ser garantidas no banco de dados, e não apenas na aplicação.",
     "Verificação dos índices únicos parciais e da constraint `ck_tel_geo_referencia` na migração."),
    ("RNF-TEL-003", "Robustez", "Identificadores malformados devem resultar em HTTP 404, e não em erro interno.",
     "Round-trip E2E consultando identificadores não-UUID."),
    ("RNF-TEL-004", "Usabilidade", "Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada.",
     "Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409."),
    ("RNF-TEL-005", "Rastreabilidade", "Toda alteração deve registrar autoria (`created_by`) e data (`created_at`, `updated_at`).",
     "Teste de integração verificando as colunas de auditoria após criação e alteração."),
    ("RNF-TEL-006", "Compatibilidade", "A API deve manter contrato estável, versionado sob o prefixo `/api/v1/tel`.",
     "Verificação do OpenAPI publicado e da contagem de paths e operações."),
    ("RNF-TEL-007", "Desacoplamento", "O domínio não deve manter chave estrangeira física para outros bancos de domínios.",
     "Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco."),
]



# ============================================================================
# DOM-IMO — Atores, capacidades, processos e regras
# ============================================================================

IMO_ATORES = [
    ("AT-IMO-001", "Técnico de cadastro imobiliário", "Servidor municipal",
     "Mantém o cadastro dos lotes, suas características e a titularidade.",
     "Cadastra imóveis, altera dados cadastrais e altera a situação conforme a máquina de estados.",
     "SIGMUN — Cadastro Imobiliário", "CAP-IMO-001, CAP-IMO-002, CAP-IMO-003"),
    ("AT-IMO-002", "Avaliador fiscal", "Servidor municipal",
     "Apura o valor venal dos imóveis a partir dos valores unitários vigentes.",
     "Registra e cancela avaliações; não altera a planta genérica de valores.",
     "SIGMUN — Cadastro Imobiliário; SIGMUN — Gestão Territorial; SIGMUN — Tributos", "CAP-IMO-004"),
    ("AT-IMO-003", "Cartório de registro de imóveis", "Entidade externa",
     "Fornece dados registrais para conferência da titularidade e da geometria do lote.",
     "Não altera o sistema.", "Cartório", "CAP-IMO-002"),
    ("AT-IMO-004", "Cidadão", "Externo",
     "Consulta a situação cadastral do imóvel e a avaliação aplicada.",
     "Não altera o sistema; pode contestar o valor venal.", "SIGMUN — Cadastro Imobiliário", "CAP-IMO-005"),
]

IMO_CAPACIDADES = [
    ("CAP-IMO-001", "Cadastro de lotes",
     "Manter unidades imobiliárias com inscrição única, logradouro, bairro, áreas e ano de construção.",
     "PRO-IMO-001", "RN-IMO-001, RN-IMO-002, RN-IMO-003", "AT-IMO-001"),
    ("CAP-IMO-002", "Titularidade do imóvel",
     "Vincular pessoas físicas e jurídicas ao imóvel, com um único titular principal.",
     "PRO-IMO-002", "RN-IMO-006", "AT-IMO-001, AT-IMO-003"),
    ("CAP-IMO-003", "Ciclo de vida do imóvel",
     "Controlar a situação cadastral do imóvel por meio de uma máquina de estados auditável.",
     "PRO-IMO-003", "RN-IMO-004", "AT-IMO-001"),
    ("CAP-IMO-004", "Avaliação do valor venal",
     "Apurar o valor venal a partir dos valores unitários vigentes da planta genérica de valores.",
     "PRO-IMO-004", "RN-IMO-005", "AT-IMO-002"),
    ("CAP-IMO-005", "Consulta e contestação cadastral",
     "Consultar a situação do imóvel, a titularidade e o valor venal aplicado.",
     "PRO-IMO-005", "RN-IMO-001, RN-IMO-005", "AT-IMO-002, AT-IMO-004"),
    ("CAP-IMO-006", "Georreferenciamento do lote",
     "Registrar a geometria georreferenciada de cada lote, com datum e vértices validados.",
     "PRO-IMO-006", "RN-IMO-007", "AT-IMO-001"),
]

IMO_PROCESSOS = [
    ("PRO-IMO-001", "Cadastrar lote", "Levantamento predial, loteamento novo ou regularização cadastral.",
     "Registrar a unidade imobiliária com sua inscrição definitiva.",
     "Inscrição imobiliária; logradouro; bairro; número; tipo; áreas; ano de construção",
     "Imóvel cadastrado",
     "Selecionar o logradouro e o bairro de vinculação (RN-IMO-002); verificar a unicidade da inscrição (RN-IMO-001); informar as áreas (RN-IMO-003); gravar com situação ativa.",
     "RN-IMO-001, RN-IMO-002, RN-IMO-003"),
    ("PRO-IMO-002", "Vincular titularidade", "Aquisição de título, escritura, contrato ou atualização de cadastro.",
     "Manter a titularidade do imóvel com um único titular principal.",
     "Imóvel; nome; CPF ou CNPJ; vínculo; indicador de principal", "Vínculo de propriedade registrado",
     "Selecionar o imóvel; informar os dados do proprietário; o sistema impede titular principal duplicado e vínculo repetido (RN-IMO-006); gravar o vínculo.",
     "RN-IMO-006"),
    ("PRO-IMO-003", "Alterar situação do imóvel", "Obra, ocupação, demolição ou regularização cadastral.",
     "Manter a situação cadastral coerente com a realidade do imóvel.",
     "Imóvel; nova situação", "Imóvel com situação alterada",
     "Solicitar a nova situação; o sistema valida a transição contra a máquina de estados (RN-IMO-004); transições inválidas são recusadas com HTTP 409.",
     "RN-IMO-004"),
    ("PRO-IMO-004", "Avaliar o valor venal", "Início do exercício fiscal ou revisão cadastral do imóvel.",
     "Apurar o valor venal e o lançamento estimado do imóvel.",
     "Imóvel; exercício; valor do terreno por m²; valor da construção por m²; alíquota", "Avaliação concluída com valor venal",
     "Consultar a planta vigente no DOM-TEL; calcular terreno, construção, valor venal e lançamento (RN-IMO-005); impedir reavaliação de exercício concluído; registrar e concluir.",
     "RN-IMO-005"),
    ("PRO-IMO-005", "Consultar cadastro e contestar valor", "Solicitação do cidadão ou de órgão de controle.",
     "Prestar esclarecimento sobre a inscrição, a titularidade e o valor venal.",
     "Inscrição imobiliária", "Dados cadastrais e avaliação do exercício",
     "Consultar o imóvel pela inscrição; exibir situação, áreas, titularidade e avaliações.",
     "RN-IMO-001, RN-IMO-005"),
    ("PRO-IMO-006", "Georreferenciar o lote", "Levantamento topográfico ou certificação pelo registro do imóvel.",
     "Vincular a geometria fundiária ao cadastro do lote.",
     "Imóvel; tipo de geometria; vértices; datum; precisão", "Geometria do lote registrada",
     "Selecionar o imóvel; informar geometria, vértices e datum (RN-IMO-007); o sistema valida e substitui a geometria vigente.",
     "RN-IMO-007"),
]



IMO_REGRAS = [
    ("RN-IMO-001", "Unicidade da Inscrição Imobiliária", "Restrição", "PRO-IMO-001",
     "A inscrição imobiliária é única no município e obrigatória; a alteração posterior mantém o mesmo identificador.",
     "A inscrição é a chave de endereçamento do imóvel e o meio de citação de lançamento junto ao cidadão.",
     "Restrição UNIQUE em `imo.imoveis.inscricao_imobiliaria` e validação em `Imovel.validar()`."),
    ("RN-IMO-002", "Vinculação Obrigatória ao Território", "Restrição", "PRO-IMO-001",
     "O imóvel exige logradouro e divisão territorial vinculados; o bairro é resolvido a partir do logradouro.",
     "Sem o vínculo territorial não há endereço válido nem aplicação possível da planta de valores.",
     "Validação de `logradouro_id` e `bairro_id` em `Imovel.validar()`."),
    ("RN-IMO-003", "Coerência das Áreas", "Restrição", "PRO-IMO-001",
     "As áreas do terreno e da construção não podem ser negativas e o ano de construção deve ser coerente.",
     "Áreas negativas produziriam valor venal incorreto e urbanismo inválido.",
     "Validação em `Imovel.validar()` e faixas restritivas nos schemas Pydantic."),
    ("RN-IMO-004", "Máquina de Estados da Situação do Imóvel", "Máquina de estados", "PRO-IMO-003",
     "As transições são `ATIVO -> INATIVO | EM_OBRA | DESOCUPADO | DEMOLIDO`, `INATIVO -> ATIVO`, `EM_OBRA -> ATIVO | DEMOLIDO` e `DESOCUPADO -> ATIVO | INATIVO`; `DEMOLIDO` é terminal.",
     "Impede situações incoerentes, como imóvel demolido reativado, e preserva o histórico fiscal.",
     "Tabela `_TRANSICOES_SITUACAO` e validação em `Imovel.mudar_situacao()`."),
    ("RN-IMO-005", "Apuração do Valor Venal", "Cálculo", "PRO-IMO-004",
     "`valor_terreno = área_terreno_m2 × Vt`, `valor_construção = área_construida_m2 × Vc`, `valor_venal = valor_terreno + valor_construcao` e `valor_lançamento = valor_venal × alíquota / 100`; um exercício já concluído não pode ser reavaliado.",
     "Garante a rastreabilidade do valor aplicado e impede índices contraditórios no mesmo exercício.",
     "Propriedades calculadas em `AvaliacaoImovel` e índice único `uq_imo_avaliacao_exercicio`."),
    ("RN-IMO-006", "Titularidade Principal Única", "Restrição", "PRO-IMO-002",
     "Cada imóvel admite no máximo um proprietário titular principal, a mesma pessoa não é vinculada duas vezes ao mesmo imóvel e o documento é CPF (11 dígitos) ou CNPJ (14 dígitos).",
     "A titularidade principal é a base da notificação de lançamento e da cobrança.",
     "Índice único parcial `uq_imo_titular_principal` e validação em `ProprietarioImovel.validar()`."),
    ("RN-IMO-007", "Integridade da Geometria do Lote", "Restrição", "PRO-IMO-006",
     "A geometria exige datum suportado, coordenadas no intervalo admissível e vértices compatíveis com o tipo de geometria; cada lote admite uma geometria vigente.",
     "Assegura a fidelidade do desenho fundiário e o georreferenciamento legal.",
     "Validação em `GeometriaImovel.validar()` e índice único `uq_imo_geometria_lote`."),
]

IMO_RF = [
    ("RF-IMO-001", "O sistema deve permitir cadastrar, alterar, listar, consultar e excluir lotes.", "Essencial", "CAP-IMO-001", "RN-IMO-001, RN-IMO-002, RN-IMO-003",
     "POST /api/v1/imo/imoveis; GET /api/v1/imo/imoveis; GET /api/v1/imo/imoveis/{imovel_id}; PATCH /api/v1/imo/imoveis/{imovel_id}; DELETE /api/v1/imo/imoveis/{imovel_id}"),
    ("RF-IMO-002", "O sistema deve permitir consultar o imóvel pela inscrição e listar os imóveis de um logradouro ou de um bairro.", "Essencial", "CAP-IMO-001", "RN-IMO-001",
     "GET /api/v1/imo/imoveis/inscricao/{inscricao}; GET /api/v1/imo/imoveis/logradouro/{logradouro_id}; GET /api/v1/imo/imoveis/bairro/{bairro_id}"),
    ("RF-IMO-003", "O sistema deve permitir alterar a situação do imóvel conforme a máquina de estados.", "Essencial", "CAP-IMO-003", "RN-IMO-004",
     "POST /api/v1/imo/imoveis/{imovel_id}/situacao"),
    ("RF-IMO-004", "O sistema deve permitir vincular proprietários ao imóvel, com um único titular principal.", "Essencial", "CAP-IMO-002", "RN-IMO-006",
     "POST /api/v1/imo/proprietarios; GET /api/v1/imo/proprietarios; GET /api/v1/imo/imoveis/{imovel_id}/proprietarios; DELETE /api/v1/imo/proprietarios/{vinculo_id}"),
    ("RF-IMO-005", "O sistema deve permitir registrar a avaliação do valor venal do imóvel para um exercício.", "Essencial", "CAP-IMO-004", "RN-IMO-005",
     "POST /api/v1/imo/avaliacoes; GET /api/v1/imo/avaliacoes"),
    ("RF-IMO-006", "O sistema deve permitir concluir e cancelar avaliações conforme o ciclo de vida da avaliação.", "Essencial", "CAP-IMO-004", "RN-IMO-005",
     "POST /api/v1/imo/avaliacoes/{avaliacao_id}/concluir; POST /api/v1/imo/avaliacoes/{avaliacao_id}/cancelar; GET /api/v1/imo/avaliacoes/{avaliacao_id}; GET /api/v1/imo/avaliacoes/imovel/{imovel_id}"),
    ("RF-IMO-007", "O sistema deve permitir registrar a característica construtiva do imóvel.", "Importante", "CAP-IMO-001", "RN-IMO-003",
     "POST /api/v1/imo/caracteristicas; GET /api/v1/imo/caracteristicas; GET /api/v1/imo/caracteristicas/imovel/{imovel_id}"),
    ("RF-IMO-008", "O sistema deve permitir registrar a geometria georreferenciada do lote.", "Essencial", "CAP-IMO-006", "RN-IMO-007",
     "POST /api/v1/imo/geometrias; GET /api/v1/imo/geometrias; GET /api/v1/imo/geometrias/imovel/{imovel_id}"),
]



IMO_CU = [
    ("CU-IMO-001", "Cadastrar lote", "AT-IMO-001", "CAP-IMO-001", "O logradouro e o bairro de vinculação existem no DOM-TEL.",
     "Selecionar o logradouro; o bairro é resolvido a partir dele (RN-IMO-002); informar inscrição, número, tipo, áreas e ano; verificar a unicidade da inscrição (RN-IMO-001) e a coerência das áreas (RN-IMO-003); gravar com situação ativa.",
     "O imóvel está cadastrado com inscrição definitiva.", "RN-IMO-001, RN-IMO-002, RN-IMO-003", "CadastrarImovelUseCase"),
    ("CU-IMO-002", "Vincular titular principal", "AT-IMO-001", "CAP-IMO-002", "O imóvel existe.",
     "Selecionar o imóvel e informar nome e CPF ou CNPJ; o sistema impede titular principal duplicado e vínculo repetido (RN-IMO-006); gravar o vínculo.",
     "O imóvel possui o titular principal vinculado.", "RN-IMO-006", "VincularProprietarioUseCase"),
    ("CU-IMO-003", "Alterar situação do imóvel", "AT-IMO-001", "CAP-IMO-003", "O imóvel existe.",
     "Selecionar a nova situação; o sistema valida a transição contra a máquina de estados (RN-IMO-004); transições inválidas são recusadas com HTTP 409.",
     "O imóvel está na situação informada, quando a transição é válida.", "RN-IMO-004", "AlterarSituacaoImovelUseCase"),
    ("CU-IMO-004", "Avaliar o valor venal", "AT-IMO-002", "CAP-IMO-004", "O imóvel existe e possui áreas cadastradas.",
     "Consultar a planta vigente no DOM-TEL; calcular terreno, construção, valor venal e lançamento (RN-IMO-005); o sistema recusa a reavaliação de exercício concluído; registrar e concluir.",
     "A avaliação do exercício está concluída e o valor venal apurado.", "RN-IMO-005", "AvaliarImovelUseCase"),
    ("CU-IMO-005", "Consultar cadastro do imóvel", "AT-IMO-004", "CAP-IMO-005", "Não há precondição.",
     "Informar a inscrição imobiliária; o sistema exibe situação, áreas, titularidade e avaliações.",
     "Os dados cadastrais foram apresentados ao cidadão.", "RN-IMO-001, RN-IMO-005", "— (consulta ao repositório)"),
    ("CU-IMO-006", "Georreferenciar o lote", "AT-IMO-001", "CAP-IMO-006", "O imóvel existe.",
     "Selecionar o imóvel e informar geometria, vértices, datum e precisão; o sistema valida e substitui a geometria vigente (RN-IMO-007).",
     "O lote possui geometria georreferenciada vigente.", "RN-IMO-007", "RegistrarGeometriaUseCase"),
]



IMO_HU = [
    ("HU-IMO-001", "Cadastrar e manter lotes", "Como técnico de cadastro imobiliário",
     "cadastrar lotes com inscrição definitiva e áreas consistentes", "manter a base do cadastro imobiliário municipal", "CAP-IMO-001",
     "RN-IMO-001, RN-IMO-002, RN-IMO-003",
     "Dado um logradouro existente no DOM-TEL, quando o técnico cadastra o lote, então o imóvel é criado com o bairro resolvido.;"
     "Dado uma inscrição já cadastrada, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-IMO-001).;"
     "Dado uma área negativa, quando o técnico cadastra, então o sistema recusa (RN-IMO-003)."),
    ("HU-IMO-002", "Controlar a titularidade do imóvel", "Como técnico de cadastro imobiliário",
     "vincular o titular principal e demais parceiros", "notificar corretamente o cidadão e orientar a cobrança", "CAP-IMO-002",
     "RN-IMO-006",
     "Dado um imóvel sem titular, quando o técnico vincula um titular principal, então o vínculo é criado.;"
     "Dado um imóvel que já possui titular principal, quando o técnico tenta vincular outro principal, então o sistema recusa com HTTP 409 (RN-IMO-006).;"
     "Dado um CPF ou CNPJ com comprimento inválido, quando o técnico vincula, então o sistema recusa (RN-IMO-006).;"
     "Dado a mesma pessoa já vinculada, quando o técnico vincula novamente, então o sistema recusa (RN-IMO-006)."),
    ("HU-IMO-003", "Controlar o ciclo de vida do imóvel", "Como técnico de cadastro imobiliário",
     "alterar a situação cadastral do imóvel", "refletir a realidade do imóvel e sustentar a avaliação", "CAP-IMO-003",
     "RN-IMO-004",
     "Dado um imóvel ativo, quando o técnico marca em obra, então a situação é alterada (RN-IMO-004).;"
     "Dado um imóvel demolido, quando o técnico tenta reativar, então o sistema recusa com HTTP 409 (RN-IMO-004).;"
     "Dado um imóvel inativo, quando o técnico marca desocupado sem reativar, então o sistema recusa (RN-IMO-004)."),
    ("HU-IMO-004", "Avaliar o valor venal do imóvel", "Como avaliador fiscal",
     "apurar o valor venal com base na planta genérica de valores vigente", "fundamentar o lançamento do tributo municipal", "CAP-IMO-004",
     "RN-IMO-005",
     "Dado um imóvel de 200 m² de terreno e 120 m² de construção, quando a avaliação usa R$ 180/m² e R$ 950/m², então o valor venal é de R$ 150.000,00 (RN-IMO-005).;"
     "Dado um exercício já avaliado e concluído, quando o avaliador tenta reavaliar, então o sistema recusa com HTTP 409 (RN-IMO-005).;"
     "Dado um imóvel sem áreas, quando o avaliador tenta avaliar, então o sistema recusa (RN-IMO-005)."),
    ("HU-IMO-005", "Georreferenciar o lote", "Como técnico de cadastro imobiliário",
     "registrar a geometria georreferenciada do lote", "apoiar o georreferenciamento legal e a produção cartográfica", "CAP-IMO-006",
     "RN-IMO-007",
     "Dado um imóvel existente, quando o técnico registra um polígono com vértices válidos, então a geometria é gravada.;"
     "Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa (RN-IMO-007).;"
     "Dado um datum não suportado, quando o técnico registra, então o sistema recusa (RN-IMO-007)."),
]




IMO_RNF = [
    ("RNF-IMO-001", "Desempenho", "As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens.",
     "Teste de integração verificando o parâmetro `page_size` e a resposta paginada."),
    ("RNF-IMO-002", "Integridade", "As invariantes de inscrição, titularidade principal, avaliação e geometria devem ser garantidas no banco de dados.",
     "Verificação dos índices `uq_imo_avaliacao_exercicio`, `uq_imo_titular_principal` e `uq_imo_geometria_lote`."),
    ("RNF-IMO-003", "Desacoplamento", "O domínio não deve manter chave estrangeira física para o banco do DOM-TEL; o contrato é resolvido por API.",
     "Inspeção da migração e do port `ConsultaPlantaValores`."),
    ("RNF-IMO-004", "Robustez", "Identificadores malformados devem resultar em HTTP 404, e não em erro interno.",
     "Round-trip E2E consultando identificadores não-UUID."),
    ("RNF-IMO-005", "Rastreabilidade", "Toda alteração deve registrar autoria e data; avaliações preservam a memória por exercício.",
     "Teste de integração verificando as colunas de auditoria e a coexistência de avaliações por ano."),
    ("RNF-IMO-006", "Precisão numérica", "Os valores monetários devem ser gravados e retornados com duas casas decimais.",
     "Round-trip E2E do cálculo do valor venal e do lançamento estimado."),
    ("RNF-IMO-007", "Compatibilidade", "A API deve manter contrato estável, versionado sob o prefixo `/api/v1/imo`.",
     "Verificação do OpenAPI publicado e da contagem de paths e operações."),
]


# ============================================================================
# DOM-GEO — Geoinformação Municipal: atores, capacidades, processos e regras
# ============================================================================

GEO_ATORES = [
    {
        "id": "AT-GEO-001",
        "nome": "Técnico de geoprocessamento",
        "tipo": "Servidor municipal",
        "papel": "Mantém as camadas cartográficas do geoportal e responde pela consistência técnica das base geoespaciais.",
        "decisoes": "Cadastra e altera camadas; ativa e desativa camadas; publica mapas no geoportal.",
        "sistemas": "SIGMUN — Geoinformação Municipal",
        "capacidades": "CAP-GEO-001, CAP-GEO-003",
    },
    {
        "id": "AT-GEO-002",
        "nome": "Gestor do geoportal",
        "tipo": "Servidor municipal",
        "papel": "Decide o conteúdo e a publicação dos mapas temáticos e cadastrais do município.",
        "decisoes": "Compõe mapas a partir das camadas ativas; publica, arquiva e exclui mapas.",
        "sistemas": "SIGMUN — Geoinformação Municipal",
        "capacidades": "CAP-GEO-002",
    },
    {
        "id": "AT-GEO-003",
        "nome": "Fiscal de urbanismo",
        "tipo": "Servidor municipal",
        "papel": "Consulta mapas e elementos geoespaciais para instruir processos de licenciamento e fiscalização.",
        "decisoes": "Não altera a cartografia; consulta e solicita correção.",
        "sistemas": "SIGMUN — Geoinformação Municipal",
        "capacidades": "CAP-GEO-004",
    },
    {
        "id": "AT-GEO-004",
        "nome": "Administrador de serviços geoespaciais",
        "tipo": "Servidor municipal",
        "papel": "Cadastra e mantém os serviços de publicação (WMS, WFS, WMTS, XYZ) consumidos por terceiros.",
        "decisoes": "Cadastra, altera e inativa serviços geoespaciais.",
        "sistemas": "SIGMUN — Geoinformação Municipal",
        "capacidades": "CAP-GEO-005",
    },
    {
        "id": "AT-GEO-005",
        "nome": "Cidadão",
        "tipo": "Público externo",
        "papel": "Consulta os mapas publicados e os serviços geoespaciais de acesso público.",
        "decisoes": "Não altera o sistema; apenas consulta.",
        "sistemas": "Geoportal municipal",
        "capacidades": "CAP-GEO-006",
    },
]

GEO_CAPACIDADES = [
    {
        "id": "CAP-GEO-001",
        "nome": "Cadastro de camadas cartográficas",
        "descricao": "Manter camadas com código único, tipo, formato, datum, faixa de zoom e URL de serviço quando aplicável.",
        "processos": "PRO-GEO-001",
        "regras": "RN-GEO-001, RN-GEO-006",
        "atores": "AT-GEO-001",
    },
    {
        "id": "CAP-GEO-002",
        "nome": "Gestão de mapas SIG",
        "descricao": "Elaborar, publicar e arquivar mapas temáticos e cadastrais do geoportal municipal.",
        "processos": "PRO-GEO-003",
        "regras": "RN-GEO-002, RN-GEO-004, RN-GEO-005",
        "atores": "AT-GEO-002",
    },
    {
        "id": "CAP-GEO-003",
        "nome": "Composição de camadas por mapa",
        "descricao": "Definir quais camadas compõem cada mapa, com ordem, opacidade, rótulo e visibilidade.",
        "processos": "PRO-GEO-002",
        "regras": "RN-GEO-004, RN-GEO-008",
        "atores": "AT-GEO-002, AT-GEO-001",
    },
    {
        "id": "CAP-GEO-004",
        "nome": "Cadastro de elementos geoespaciais",
        "descricao": "Registrar pontos de interesse e demais elementos com geometria georreferenciada em uma camada.",
        "processos": "PRO-GEO-004",
        "regras": "RN-GEO-003, RN-GEO-008",
        "atores": "AT-GEO-001, AT-GEO-003",
    },
    {
        "id": "CAP-GEO-005",
        "nome": "Publicação de serviços geoespaciais",
        "descricao": "Cadastrar e manter os serviços de publicação do geoportal, com protocolo, URL e camada publicada.",
        "processos": "PRO-GEO-005",
        "regras": "RN-GEO-007",
        "atores": "AT-GEO-004",
    },
    {
        "id": "CAP-GEO-006",
        "nome": "Consulta de mapas e serviços",
        "descricao": "Disponibilizar mapas publicados, elementos geoespaciais e serviços de acesso público.",
        "processos": "PRO-GEO-006",
        "regras": "RN-GEO-003, RN-GEO-004",
        "atores": "AT-GEO-003, AT-GEO-005",
    },
]

GEO_PROCESSOS = [
    {
        "id": "PRO-GEO-001",
        "nome": "Manter camada cartográfica",
        "gatilho": "Aquisição de nova base geoespacial, atualização de base existente ou correção de metadado.",
        "objetivo": "Manter camadas cartográficas identificáveis e tecnicamente consistentes.",
        "entradas": "Código; nome; tipo; formato; fonte; datum; SRID; faixa de zoom; URL de serviço",
        "saidas": "Camada cadastrada, atualizada, ativada ou desativada",
        "passos": [
            "Verificar se o código da camada já está cadastrado (RN-GEO-001).",
            "Preencher os dados da camada, incluindo datum, SRID e faixa de zoom.",
            "Informar a URL de serviço quando o formato exigir (RN-GEO-006).",
            "Gravar a camada e registrar autoria e data.",
        ],
        "regras": "RN-GEO-001, RN-GEO-005, RN-GEO-006",
    },
    {
        "id": "PRO-GEO-002",
        "nome": "Compor mapa com camadas ativas",
        "gatilho": "Elaboração de novo mapa temático ou atualização da composição de mapa em rascunho.",
        "objetivo": "Compor o mapa exclusivamente com camadas aptas a publicação.",
        "entradas": "Mapa em rascunho; camada ativa; ordem; opacidade; rótulo",
        "saidas": "Vínculo de composição criado ou removido",
        "passos": [
            "Selecionar o mapa, que deve estar em rascunho (RN-GEO-004).",
            "Selecionar a camada, que deve estar ativa (RN-GEO-006).",
            "Impedir a inclusão da mesma camada duas vezes no mesmo mapa (RN-GEO-004).",
            "Gravar o vínculo com ordem, opacidade e visibilidade.",
        ],
        "regras": "RN-GEO-004, RN-GEO-006, RN-GEO-008",
    },
    {
        "id": "PRO-GEO-003",
        "nome": "Publicar mapa no geoportal",
        "gatilho": "Mapa temático ou cadastral aprovado para disponibilização ao público.",
        "objetivo": "Publicar mapa com conteúdo cartográfico verificável.",
        "entradas": "Mapa em rascunho; composição de camadas",
        "saidas": "Mapa publicado com data de publicação",
        "passos": [
            "Verificar que o mapa possui ao menos uma camada na composição (RN-GEO-004).",
            "Verificar que todas as camadas da composição estão ativas (RN-GEO-004, RN-GEO-006).",
            "Publicar o mapa e registrar a data de publicação.",
        ],
        "regras": "RN-GEO-004, RN-GEO-005, RN-GEO-006",
    },
    {
        "id": "PRO-GEO-004",
        "nome": "Registrar elemento geoespacial",
        "gatilho": "Levantamento de campo, cadastro de ponto de interesse ou correção de geometria.",
        "objetivo": "Manter elementos georreferenciados consistentes com a camada de destino.",
        "entradas": "Código; nome; camada; geometria; vértices; datum; atributos",
        "saidas": "Elemento geoespacial registrado ou excluído",
        "passos": [
            "Selecionar a camada de destino, que deve existir e não estar desativada (RN-GEO-008).",
            "Verificar a unicidade do código dentro da camada.",
            "Informar a geometria e os vértices, respeitando o mínimo do tipo (RN-GEO-003).",
            "Gravar o elemento e registrar autoria e data.",
        ],
        "regras": "RN-GEO-003, RN-GEO-008",
    },
    {
        "id": "PRO-GEO-005",
        "nome": "Publicar serviço geoespacial",
        "gatilho": "Disponibilização de novo serviço de mapa ou ajuste de endpoint existente.",
        "objetivo": "Manter serviços de publicação válidos e coerentes com o protocolo declarado.",
        "entradas": "Código; nome; protocolo; URL; camada publicada; datum; faixa de zoom",
        "saidas": "Serviço cadastrado, atualizado ou inativado",
        "passos": [
            "Verificar se o código do serviço já está cadastrado (RN-GEO-007).",
            "Informar a URL; para WMS e WFS, também a camada publicada (RN-GEO-007).",
            "Gravar o serviço e registrar autoria e data.",
        ],
        "regras": "RN-GEO-005, RN-GEO-007",
    },
    {
        "id": "PRO-GEO-006",
        "nome": "Consultar mapa e serviço publicado",
        "gatilho": "Necessidade de informação espacial por parte do público ou de servidores.",
        "objetivo": "Disponibilizar a informação cartográfica publicada.",
        "entradas": "Filtro opcional por tipo ou situação; camada de interesse",
        "saidas": "Lista de mapas, elementos ou serviços",
        "passos": [
            "Informar o filtro de interesse, quando houver.",
            "Retornar os registros, com paginação entre 1 e 100 itens por página.",
        ],
        "regras": "RN-GEO-003, RN-GEO-004",
    },
]

GEO_REGRAS = [
    {
        "id": "RN-GEO-001",
        "titulo": "Unicidade do Código da Camada",
        "tipo": "Restrição",
        "processo": "PRO-GEO-001",
        "descricao": "O código da camada de mapa é único no geoportal municipal; código e nome são obrigatórios.",
        "justificativa": "O código é a chave natural usada na composição dos mapas e nos clientes que consomem o geoportal.",
        "garantia": "Restrição UNIQUE em `geo.camadas_mapa.codigo` e validação em `CamadaMapa.validar()`.",
    },
    {
        "id": "RN-GEO-002",
        "titulo": "Unicidade do Código do Mapa",
        "tipo": "Restrição",
        "processo": "PRO-GEO-003",
        "descricao": "O código do mapa SIG é único no geoportal municipal; código e nome são obrigatórios.",
        "justificativa": "O código identifica o mapa publicado e é referenciado por portais e aplicações que consomem o geoportal.",
        "garantia": "Restrição UNIQUE em `geo.mapas_sig.codigo` e validação em `MapaSig.validar()`.",
    },
    {
        "id": "RN-GEO-003",
        "titulo": "Integridade da Geometria do Elemento",
        "tipo": "Restrição",
        "processo": "PRO-GEO-004",
        "descricao": "O elemento geoespacial exige geometria suportada, coordenadas no intervalo do datum e quantidade de vértices compatível com o tipo de geometria (ponto 1, linha 2, polígono 3).",
        "justificativa": "Geometria inválida corromperia a camada e a visualização no visor cartográfico.",
        "garantia": "Checks `ck_geo_feature_vertices` e `ck_geo_feature_coordenadas`, e validação em `FeatureGeo.validar()`.",
    },
    {
        "id": "RN-GEO-004",
        "titulo": "Ciclo de Vida do Mapa e Congelamento da Composição",
        "tipo": "Máquina de estados",
        "processo": "PRO-GEO-003",
        "descricao": "O mapa percorre `RASCUNHO -> PUBLICADO -> ARQUIVADO`, sem retorno a partir de `ARQUIVADO`. Somente mapas em rascunho aceitam alteração de composição, a publicação exige ao menos uma camada ativa e mapa publicado não pode ser excluído diretamente.",
        "justificativa": "A composição publicada é o produto cartográfico entregue ao cidadão e deve permanecer estável para consulta e cache.",
        "garantia": "Transições em `MapaSig.publicar()` e `.arquivar()`, e verificações nos casos de uso de composição e exclusão.",
    },
    {
        "id": "RN-GEO-005",
        "titulo": "Coerência Cartográfica do Mapa e do Serviço",
        "tipo": "Restrição",
        "processo": "PRO-GEO-003",
        "descricao": "A extensão (bbox) do mapa deve ser coerente, o SRID deve estar em faixa válida e a faixa de zoom deve respeitar `zoom_minimo <= zoom_inicial <= zoom_maximo`.",
        "justificativa": "Parâmetros incoerentes impedem a exibição correta do mapa no visor.",
        "garantia": "Checks `ck_geo_mapa_zoom`, `ck_geo_mapa_extensao`, `ck_geo_camada_zoom` e `ck_geo_servico_zoom`, e validação nas entidades.",
    },
    {
        "id": "RN-GEO-006",
        "titulo": "Ciclo de Vida da Camada e Exigência de URL de Serviço",
        "tipo": "Máquina de estados",
        "processo": "PRO-GEO-001",
        "descricao": "A camada percorre `RASCUNHO -> ATIVA -> DESATIVADA`, sem retorno a partir de `DESATIVADA`. Camada ativa cujo formato seja de serviço (WMS, WFS, WMTS, XYZ) exige URL preenchida, e somente camada ativa compõe mapa.",
        "justificativa": "Camada publicada sem endpoint válido quebraria a exibição do mapa no geoportal.",
        "garantia": "Check `ck_geo_camada_servico_url`, transições em `CamadaMapa.ativar()`/`.desativar()` e validação na composição.",
    },
    {
        "id": "RN-GEO-007",
        "titulo": "Validação do Serviço Geoespacial",
        "tipo": "Restrição",
        "processo": "PRO-GEO-005",
        "descricao": "O serviço geoespacial exige código e nome únicos, URL válida iniciada por `http://` ou `https://` quando ativo e, nos protocolos WMS e WFS, o nome da camada publicada.",
        "justificativa": "Serviço sem endpoint ou sem camada identificável não é consumível por terceiros.",
        "garantia": "Checks `ck_geo_servico_url` e `ck_geo_servico_camada`, e validação em `ServicoGeo.validar()`.",
    },
    {
        "id": "RN-GEO-008",
        "titulo": "Vinculação do Elemento Geoespacial e da Composição",
        "tipo": "Restrição",
        "processo": "PRO-GEO-004",
        "descricao": "Todo elemento geoespacial pertence a uma camada cadastrada e não desativada; toda camada da composição de um mapa é uma camada cadastrada; a mesma camada não integra duas vezes o mesmo mapa.",
        "justificativa": "Referências órfãs impediriam a consulta e a consistência da base cartográfica.",
        "garantia": "Validações em `FeatureGeo.validar()` e nos casos de uso de registro e de composição; índice único parcial `uq_geo_mapa_camada`.",
    },
]


GEO_RF = [
    ("RF-GEO-001", "O sistema deve permitir cadastrar, alterar, listar, consultar, ativar, desativar e excluir camadas cartográficas.", "Essencial", "CAP-GEO-001", "RN-GEO-001, RN-GEO-006",
     "POST /api/v1/geo/camadas; GET /api/v1/geo/camadas; GET /api/v1/geo/camadas/{camada_id}; PATCH /api/v1/geo/camadas/{camada_id}; DELETE /api/v1/geo/camadas/{camada_id}; POST /api/v1/geo/camadas/{camada_id}/ativar; POST /api/v1/geo/camadas/{camada_id}/desativar"),
    ("RF-GEO-002", "O sistema deve permitir filtrar a listagem de camadas por tipo.", "Desejável", "CAP-GEO-001", "RN-GEO-001",
     "GET /api/v1/geo/camadas"),
    ("RF-GEO-003", "O sistema deve permitir cadastrar, alterar, listar, consultar, publicar, arquivar e excluir mapas SIG.", "Essencial", "CAP-GEO-002", "RN-GEO-002, RN-GEO-004",
     "POST /api/v1/geo/mapas; GET /api/v1/geo/mapas; GET /api/v1/geo/mapas/{mapa_id}; PATCH /api/v1/geo/mapas/{mapa_id}; DELETE /api/v1/geo/mapas/{mapa_id}; POST /api/v1/geo/mapas/{mapa_id}/publicar; POST /api/v1/geo/mapas/{mapa_id}/arquivar"),
    ("RF-GEO-004", "O sistema deve permitir compor e descompor mapas por camada, definindo ordem, opacidade, rótulo e visibilidade.", "Essencial", "CAP-GEO-003", "RN-GEO-004, RN-GEO-006, RN-GEO-008",
     "GET /api/v1/geo/mapas/{mapa_id}/composicao; POST /api/v1/geo/mapas/{mapa_id}/composicao; DELETE /api/v1/geo/mapas/{mapa_id}/composicao/{vinculo_id}"),
    ("RF-GEO-005", "O sistema deve permitir registrar, listar, consultar e excluir elementos geoespaciais vinculados a uma camada.", "Essencial", "CAP-GEO-004", "RN-GEO-003, RN-GEO-008",
     "POST /api/v1/geo/features; GET /api/v1/geo/features; GET /api/v1/geo/features/{feature_id}; DELETE /api/v1/geo/features/{feature_id}"),
    ("RF-GEO-006", "O sistema deve permitir listar os elementos geoespaciais de uma camada específica.", "Essencial", "CAP-GEO-004", "RN-GEO-008",
     "GET /api/v1/geo/features/camada/{camada_id}"),
    ("RF-GEO-007", "O sistema deve permitir cadastrar, alterar, listar, consultar, inativar e excluir serviços geoespaciais.", "Essencial", "CAP-GEO-005", "RN-GEO-007",
     "POST /api/v1/geo/servicos; GET /api/v1/geo/servicos; GET /api/v1/geo/servicos/{servico_id}; PATCH /api/v1/geo/servicos/{servico_id}; DELETE /api/v1/geo/servicos/{servico_id}; POST /api/v1/geo/servicos/{servico_id}/inativar"),
    ("RF-GEO-008", "O sistema deve permitir filtrar a listagem de serviços por protocolo.", "Desejável", "CAP-GEO-005", "RN-GEO-007",
     "GET /api/v1/geo/servicos"),
    ("RF-GEO-009", "O sistema deve permitir filtrar a listagem de mapas por situação.", "Desejável", "CAP-GEO-002", "RN-GEO-004",
     "GET /api/v1/geo/mapas"),
]

GEO_CU = [
    ("CU-GEO-001", "Cadastrar camada cartográfica", "AT-GEO-001", "CAP-GEO-001", "O servidor está autenticado e possui permissão de gestão cartográfica.",
     "Informar código, nome, tipo, formato, fonte, datum, SRID e faixa de zoom; verificar a unicidade do código (RN-GEO-001); informar URL quando o formato exigir; gravar e registrar autoria e data.",
     "A camada está cadastrada em rascunho, ativa ou desativada conforme solicitado.", "RN-GEO-001, RN-GEO-005, RN-GEO-006", "CadastrarCamadaUseCase"),
    ("CU-GEO-002", "Alterar camada cartográfica", "AT-GEO-001", "CAP-GEO-001", "A camada existe.",
     "Informar os campos a alterar; ao trocar o código, verificar a unicidade (RN-GEO-001); gravar a alteração e registrar a data.",
     "A camada está atualizada.", "RN-GEO-001, RN-GEO-005", "AtualizarCamadaUseCase"),
    ("CU-GEO-003", "Ativar camada cartográfica", "AT-GEO-001", "CAP-GEO-001", "A camada existe e não está desativada.",
     "Solicitar a ativação; exigir URL quando o formato for de serviço (RN-GEO-006); alterar a situação para ativa.",
     "A camada está ativa e apta a compor mapas.", "RN-GEO-006", "AtivarCamadaUseCase"),
    ("CU-GEO-004", "Desativar camada cartográfica", "AT-GEO-001", "CAP-GEO-001", "A camada existe e não está desativada.",
     "Solicitar a desativação; esconder a camada e alterar a situação para desativada (RN-GEO-006).",
     "A camada está desativada e indisponível para composição.", "RN-GEO-006", "DesativarCamadaUseCase"),
    ("CU-GEO-005", "Excluir camada cartográfica", "AT-GEO-001", "CAP-GEO-001", "A camada existe.",
     "Solicitar a exclusão; verificar se a camada compõe mapa publicado (RN-GEO-004); havendo dependência, recusar com HTTP 409; caso contrário, excluir logicamente.",
     "A camada está excluída logicamente e preserva o histórico.", "RN-GEO-004", "ExcluirCamadaUseCase"),
    ("CU-GEO-006", "Cadastrar mapa SIG", "AT-GEO-002", "CAP-GEO-002", "O servidor está autenticado e possui permissão de gestão de mapas.",
     "Informar código, nome, tipo, datum, SRID, escala, faixa de zoom e extensão; verificar a unicidade do código (RN-GEO-002); gravar o mapa em rascunho.",
     "O mapa está cadastrado em rascunho.", "RN-GEO-002, RN-GEO-005", "CadastrarMapaUseCase"),
    ("CU-GEO-007", "Alterar mapa SIG", "AT-GEO-002", "CAP-GEO-002", "O mapa existe.",
     "Informar os campos a alterar; em mapa publicado, o código é imutável (RN-GEO-004); gravar a alteração e registrar a data.",
     "O mapa está atualizado.", "RN-GEO-004, RN-GEO-005", "AtualizarMapaUseCase"),
    ("CU-GEO-008", "Compor mapa com camada", "AT-GEO-002", "CAP-GEO-003", "O mapa existe e está em rascunho; a camada existe e está ativa.",
     "Selecionar mapa e camada; impedir duplicidade da camada no mapa (RN-GEO-004); informar ordem, opacidade e visibilidade; gravar o vínculo.",
     "O mapa possui a camada em sua composição.", "RN-GEO-004, RN-GEO-006, RN-GEO-008", "ComporCamadaUseCase"),
    ("CU-GEO-009", "Remover camada da composição do mapa", "AT-GEO-002", "CAP-GEO-003", "O vínculo existe e o mapa está em rascunho.",
     "Selecionar o vínculo; remover a composição (RN-GEO-004).",
     "A camada foi removida da composição do mapa.", "RN-GEO-004", "RemoverComposicaoUseCase"),
    ("CU-GEO-010", "Publicar mapa no geoportal", "AT-GEO-002", "CAP-GEO-002", "O mapa existe e está em rascunho.",
     "Solicitar a publicação; exigir ao menos uma camada ativa na composição (RN-GEO-004); alterar a situação para publicado e registrar a data.",
     "O mapa está publicado e disponível ao público.", "RN-GEO-004", "PublicarMapaUseCase"),
    ("CU-GEO-011", "Arquivar mapa publicado", "AT-GEO-002", "CAP-GEO-002", "O mapa existe e está publicado.",
     "Solicitar o arquivamento; alterar a situação para arquivado (RN-GEO-004).",
     "O mapa está arquivado e saiu do geoportal, preservando o histórico.", "RN-GEO-004", "ArquivarMapaUseCase"),
    ("CU-GEO-012", "Excluir mapa SIG", "AT-GEO-002", "CAP-GEO-002", "O mapa existe e não está publicado.",
     "Solicitar a exclusão; remover os vínculos de composição; excluir logicamente o mapa (RN-GEO-004).",
     "O mapa está excluído logicamente e preserva o histórico.", "RN-GEO-004", "ExcluirMapaUseCase"),
    ("CU-GEO-013", "Registrar elemento geoespacial", "AT-GEO-001", "CAP-GEO-004", "A camada de destino existe e não está desativada.",
     "Selecionar a camada; informar geometria, vértices, datum e atributos; verificar o mínimo de vértices e a faixa de coordenadas (RN-GEO-003); gravar o elemento.",
     "O elemento está registrado e vinculado à camada.", "RN-GEO-003, RN-GEO-008", "RegistrarFeatureUseCase"),
    ("CU-GEO-014", "Excluir elemento geoespacial", "AT-GEO-001", "CAP-GEO-004", "O elemento existe.",
     "Solicitar a exclusão; excluir logicamente o elemento.",
     "O elemento está excluído logicamente.", "RN-GEO-003", "ExcluirFeatureUseCase"),
    ("CU-GEO-015", "Cadastrar serviço geoespacial", "AT-GEO-004", "CAP-GEO-005", "O servidor está autenticado e possui permissão de gestão de serviços.",
     "Informar código, nome, protocolo, URL e camada publicada; verificar a unicidade do código e a coerência do serviço (RN-GEO-007); gravar o serviço.",
     "O serviço geoespacial está cadastrado e ativo.", "RN-GEO-007", "CadastrarServicoUseCase"),
    ("CU-GEO-016", "Alterar serviço geoespacial", "AT-GEO-004", "CAP-GEO-005", "O serviço existe.",
     "Informar os campos a alterar; ao trocar o código, verificar a unicidade (RN-GEO-007); validar e gravar a alteração.",
     "O serviço está atualizado.", "RN-GEO-007", "AtualizarServicoUseCase"),
    ("CU-GEO-017", "Inativar serviço geoespacial", "AT-GEO-004", "CAP-GEO-005", "O serviço existe e está ativo.",
     "Solicitar a inativação; alterar a situação para inativo (RN-GEO-007).",
     "O serviço está inativo e indisponível para consumo.", "RN-GEO-007", "InativarServicoUseCase"),
    ("CU-GEO-018", "Excluir serviço geoespacial", "AT-GEO-004", "CAP-GEO-005", "O serviço existe.",
     "Solicitar a exclusão; excluir logicamente o serviço.",
     "O serviço está excluído logicamente.", "RN-GEO-007", "ExcluirServicoUseCase"),
    ("CU-GEO-019", "Consultar mapas, elementos e serviços", "AT-GEO-003", "CAP-GEO-006", "Não há precondição.",
     "Informar o filtro de interesse, quando houver; retornar os registros com paginação (RF-GEO-002, RF-GEO-008, RF-GEO-009).",
     "Os registros foram obtidos ou a lista vazia foi informada.", "RN-GEO-004", "— (consulta aos repositórios)"),
]

GEO_HU = [
    ("HU-GEO-001", "Manter as camadas do geoportal", "Como técnico de geoprocessamento",
     "cadastrar e manter camadas cartográficas com seus metadados técnicos", "dispor de bases geoespaciais identificáveis e consistentes", "CAP-GEO-001",
     "RN-GEO-001, RN-GEO-005, RN-GEO-006",
     "Dado que o código da camada é novo, quando o técnico cadastra, então a camada é criada.;"
     "Dado que o código já existe, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-GEO-001).;"
     "Dado uma camada WMS sem URL, quando o técnico tenta ativar, então o sistema recusa (RN-GEO-006).;"
     "Dado uma camada desativada, quando o técnico tenta reativar, então o sistema recusa (RN-GEO-006)."),
    ("HU-GEO-002", "Compor mapas temáticos com camadas", "Como gestor do geoportal",
     "definir as camadas que compõem cada mapa, com ordem e opacidade", "publicar mapas consistentes e controláveis", "CAP-GEO-003",
     "RN-GEO-004, RN-GEO-006, RN-GEO-008",
     "Dado um mapa em rascunho e uma camada ativa, quando o gestor compõe, então o vínculo é criado.;"
     "Dado que a camada já está na composição, quando o gestor tenta incluir de novo, então o sistema recusa (RN-GEO-004).;"
     "Dado um mapa publicado, quando o gestor tenta alterar a composição, então o sistema recusa (RN-GEO-004)."),
    ("HU-GEO-003", "Publicar mapas no geoportal", "Como gestor do geoportal",
     "publicar mapas temáticos e cadastrais para consulta pública", "disponibilizar a cartografia oficial do município", "CAP-GEO-002",
     "RN-GEO-004, RN-GEO-005, RN-GEO-006",
     "Dado um mapa com ao menos uma camada ativa, quando o gestor publica, então o mapa passa a publicado.;"
     "Dado um mapa sem camadas, quando o gestor tenta publicar, então o sistema recusa com HTTP 409 (RN-GEO-004).;"
     "Dado um mapa publicado, quando o gestor arquiva, então o mapa passa a arquivado (RN-GEO-004)."),
    ("HU-GEO-004", "Registrar pontos de interesse no mapa", "Como técnico de geoprocessamento",
     "registrar elementos geoespaciais com geometria validada", "enriquecer a cartografia com equipamentos e referenciais", "CAP-GEO-004",
     "RN-GEO-003, RN-GEO-008",
     "Dado uma camada existente, quando o técnico registra um ponto com vértice válido, então o elemento é criado.;"
     "Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-GEO-003).;"
     "Dado um elemento cuja camada foi desativada, quando o técnico registra, então o sistema recusa (RN-GEO-008)."),
    ("HU-GEO-005", "Publicar serviços de mapas para terceiros", "Como administrador de serviços geoespaciais",
     "cadastrar e manter serviços WMS, WFS, WMTS e XYZ", "permitir a integração do geoportal com sistemas próprios e de terceiros", "CAP-GEO-005",
     "RN-GEO-005, RN-GEO-007",
     "Dado protocolo WMS com URL e camada publicada, quando o administrador cadastra, então o serviço é criado.;"
     "Dado um serviço ativo sem URL, quando o administrador cadastra, então o sistema recusa (RN-GEO-007).;"
     "Dado um WFS sem nome de camada, quando o administrador cadastra, então o sistema recusa (RN-GEO-007)."),
    ("HU-GEO-006", "Consultar a cartografia municipal", "Como cidadão",
     "consultar mapas publicados e elementos geoespaciais", "acesso à informação espacial oficial do município", "CAP-GEO-006",
     "RN-GEO-003, RN-GEO-004",
     "Dado que existem mapas publicados, quando o cidadão consulta, então os mapas são retornados.;"
     "Dado que a camada é informada, quando o cidadão lista elementos, então somente os elementos da camada são retornados (RN-GEO-008).;"
     "Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404."),
]

GEO_RNF = [
    ("RNF-GEO-001", "Desempenho", "As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens.",
     "Teste de integração verificando o parâmetro `page_size` e a resposta paginada."),
    ("RNF-GEO-002", "Integridade", "As invariantes de geometria, ciclo de vida e unicidade devem ser garantidas no banco de dados, e não apenas na aplicação.",
     "Verificação dos 10 CHECK constraints e dos índices únicos parciais nas migrações do schema `geo`."),
    ("RNF-GEO-003", "Robustez", "Identificadores malformados devem resultar em HTTP 404, e não em erro interno.",
     "Round-trip E2E consultando identificadores não-UUID."),
    ("RNF-GEO-004", "Usabilidade", "Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada.",
     "Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409."),
    ("RNF-GEO-005", "Rastreabilidade", "Toda alteração deve registrar autoria (`created_by`) e data (`created_at`, `updated_at`).",
     "Teste de integração verificando as colunas de auditoria após criação e alteração."),
    ("RNF-GEO-006", "Compatibilidade", "A API deve manter contrato estável, versionado sob o prefixo `/api/v1/geo`.",
     "Verificação do OpenAPI publicado e da contagem de 16 paths e 28 operações."),
    ("RNF-GEO-007", "Desacoplamento", "O domínio não deve manter chave estrangeira física para outros bancos de domínios.",
     "Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco."),
    ("RNF-GEO-008", "Interoperabilidade", "O cadastro deve admitir os datuns e formatos de serviço usuais no geoportal municipal.",
     "Testes unitários cobrindo datuns (`sirgas2000`, `sad69`, `wgs84`) e formatos de serviço."),
]


# ============================================================================
# DOM-OBR — Obras e Infraestrutura: atores, capacidades, processos e regras
# ============================================================================

OBR_ATORES = [
    {
        "id": "AT-OBR-001",
        "nome": "Gestor de obras",
        "tipo": "Servidor municipal",
        "papel": "Planeja, contrata e acompanha as obras públicas, respondendo pela consistência do cadastro e do ciclo de vida.",
        "decisoes": "Cadastra obras, altera a contratação e conduz o ciclo de vida até a conclusão ou o cancelamento.",
        "sistemas": "SIGMUN — Obras e Infraestrutura",
        "capacidades": "CAP-OBR-001, CAP-OBR-005",
    },
    {
        "id": "AT-OBR-002",
        "nome": "Fiscal de obra",
        "tipo": "Servidor municipal",
        "papel": "Confere medições no campo e lavra as vistorias fiscalizadoras do avanço físico.",
        "decisoes": "Confere e aprova medições, glosa medições indevidas e registra vistorias com parecer.",
        "sistemas": "SIGMUN — Obras e Infraestrutura",
        "capacidades": "CAP-OBR-002, CAP-OBR-004",
    },
    {
        "id": "AT-OBR-003",
        "nome": "Responsável técnico da obra",
        "tipo": "Profissional contratado",
        "papel": "Executa a obra e registra o avanço físico por etapa e por medição.",
        "decisoes": "Registra etapas, informa o avanço e solicita a medição; não aprova a própria medição.",
        "sistemas": "SIGMUN — Obras e Infraestrutura",
        "capacidades": "CAP-OBR-003",
    },
    {
        "id": "AT-OBR-004",
        "nome": "Tesouraria municipal",
        "tipo": "Servidor municipal",
        "papel": "Registra os repasses e as despesas financeiras da obra, limitados ao valor já medido.",
        "decisoes": "Registra despesas e repasses; não altera medições nem avança o percentual físico.",
        "sistemas": "SIGMUN — Obras e Infraestrutura; SIGMUN — Finanças",
        "capacidades": "CAP-OBR-003",
    },
    {
        "id": "AT-OBR-005",
        "nome": "Controle interno do município",
        "tipo": "Órgão municipal de controle",
        "papel": "Acompanha a execução financeira e a regularidade das obras públicas.",
        "decisoes": "Consulta indicadores e não altera o cadastro da obra.",
        "sistemas": "SIGMUN — Obras e Infraestrutura",
        "capacidades": "CAP-OBR-005",
    },
    {
        "id": "AT-OBR-006",
        "nome": "Cidadão",
        "tipo": "Público externo",
        "papel": "Consulta o andamento físico e financeiro das obras do município.",
        "decisoes": "Não altera o sistema; apenas consulta.",
        "sistemas": "SIGMUN — Portal do cidadão",
        "capacidades": "CAP-OBR-005",
    },
]

OBR_CAPACIDADES = [
    {
        "id": "CAP-OBR-001",
        "nome": "Cadastro e ciclo de vida das obras",
        "descricao": "Cadastrar obras com número único e conduzi-las pelo ciclo até a conclusão ou o cancelamento.",
        "processos": "PRO-OBR-001",
        "regras": "RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004",
        "atores": "AT-OBR-001",
    },
    {
        "id": "CAP-OBR-002",
        "nome": "Medição físico-financeira",
        "descricao": "Registrar, conferir, aprovar e glosar medições, recompondo o avanço da obra.",
        "processos": "PRO-OBR-002",
        "regras": "RN-OBR-005",
        "atores": "AT-OBR-002, AT-OBR-003",
    },
    {
        "id": "CAP-OBR-003",
        "nome": "Execução financeira da obra",
        "descricao": "Registrar despesas e repasses, limitados ao valor medido e ainda não pago.",
        "processos": "PRO-OBR-003",
        "regras": "RN-OBR-004, RN-OBR-006",
        "atores": "AT-OBR-004, AT-OBR-003",
    },
    {
        "id": "CAP-OBR-004",
        "nome": "Acompanhamento de etapas e vistorias",
        "descricao": "Registrar etapas de execução e vistorias fiscalizadoras com parecer sobre o avanço verificado.",
        "processos": "PRO-OBR-004",
        "regras": "RN-OBR-007, RN-OBR-008",
        "atores": "AT-OBR-002, AT-OBR-003",
    },
    {
        "id": "CAP-OBR-005",
        "nome": "Consulta do andamento das obras",
        "descricao": "Consultar o avanço físico-financeiro consolidado, inclusive por terceiros.",
        "processos": "PRO-OBR-005",
        "regras": "RN-OBR-004, RN-OBR-005, RN-OBR-006",
        "atores": "AT-OBR-005, AT-OBR-006, AT-OBR-001",
    },
]

OBR_PROCESSOS = [
    {
        "id": "PRO-OBR-001",
        "nome": "Cadastrar e conduzir a obra",
        "gatilho": "Inclusão de obra no plano de metas, contratação, retomada, conclusão ou cancelamento.",
        "objetivo": "Manter a obra com cadastro e situação coerentes e com o contrato vigente.",
        "entradas": "Número; nome; tipo; contratação; recurso; valores orçado e contratado; prazos; empresa",
        "saidas": "Obra cadastrada e situada no ciclo de vida",
        "passos": [
            "Verificar se o número da obra já está cadastrado (RN-OBR-001).",
            "Informar valores, respeitando que o contratado não supera o orçado (RN-OBR-004).",
            "Para iniciar a execução, exigir empresa, contratação e data prevista (RN-OBR-003).",
            "Conduzir a obra pelo ciclo até a conclusão, que exige 100% do avanço físico (RN-OBR-005), ou o cancelamento.",
        ],
        "regras": "RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004",
    },
    {
        "id": "PRO-OBR-002",
        "nome": "Medir e conferir o avanço",
        "gatilho": "Periodicidade de medição definida em contrato ou solicitação do responsável técnico.",
        "objetivo": "Compor o avanço físico-financeiro da obra com base em medição conferida.",
        "entradas": "Obra; número da medição; percentual físico; valor medido; responsável técnico",
        "saidas": "Medição registrada, conferida, aprovada, glosada ou cancelada; obra recomposta",
        "passos": [
            "Verificar que a obra está em execução ou suspensa (RN-OBR-005).",
            "Verificar a unicidade do número da medição dentro da obra e o teto do valor contratado.",
            "Registrar a medição em situação registrada.",
            "Na conferência, aprovar ou glosar; a aprovação recompõe o avanço da obra (RN-OBR-005).",
        ],
        "regras": "RN-OBR-004, RN-OBR-005",
    },
    {
        "id": "PRO-OBR-003",
        "nome": "Registrar a despesa da obra",
        "gatilho": "Repasse, aquisição de material ou quitação de custo atribuível à obra.",
        "objetivo": "Registrar o desembolso sem permitir pagamento acima do medido.",
        "entradas": "Obra; medição vinculada; descrição; tipo; valor; credor; documento",
        "saidas": "Despesa registrada e avanço financeiro da obra recomposto",
        "passos": [
            "Verificar que a obra está contratada ou em execução (RN-OBR-006).",
            "Verificar que existe saldo medido e ainda não pago (RN-OBR-006).",
            "Registrar a despesa e recompor o avanço financeiro, limitado ao avanço físico (RN-OBR-004).",
        ],
        "regras": "RN-OBR-004, RN-OBR-006",
    },
    {
        "id": "PRO-OBR-004",
        "nome": "Registrar etapas e vistorias",
        "gatilho": "Planejamento de cronograma, avanço de frente de trabalho ou visita de fiscalização.",
        "objetivo": "Manter o detalhamento físico da obra e o registro de fiscalização.",
        "entradas": "Obra; etapa prevista e realizada; vistoria com parecer e percentual verificado",
        "saidas": "Etapa registrada ou concluída; vistoria registrada com parecer",
        "passos": [
            "Cadastrar a etapa com responsável e percentual previsto (RN-OBR-007).",
            "Atualizar o percentual realizado da etapa, na faixa de 0 a 100 (RN-OBR-007).",
            "Concluir a etapa, o que exige 100% do previsto (RN-OBR-007).",
            "Registrar a vistoria com fiscal, percentual verificado e parecer (RN-OBR-008).",
        ],
        "regras": "RN-OBR-007, RN-OBR-008",
    },
    {
        "id": "PRO-OBR-005",
        "nome": "Consultar o andamento físico-financeiro",
        "gatilho": "Necessidade de acompanhamento por parte da gestão, do controle ou do cidadão.",
        "objetivo": "Disponibilizar a situação consolidada do avanço da obra.",
        "entradas": "Obra ou filtro de situação",
        "saidas": "Obra com valores e percentuais, ou acompanhamento consolidado",
        "passos": [
            "Informar a obra ou o filtro de situação, quando houver.",
            "Retornar os indicadores de avanço físico e financeiro com paginação.",
            "Para o acompanhamento detalhado, retornar medições, despesas, etapas e vistorias.",
        ],
        "regras": "RN-OBR-004, RN-OBR-005, RN-OBR-006",
    },
]


OBR_REGRAS = [
    {
        "id": "RN-OBR-001",
        "titulo": "Unicidade do Número da Obra",
        "tipo": "Restrição",
        "processo": "PRO-OBR-001",
        "descricao": "O número da obra é único no cadastro municipal; número e nome são obrigatórios e o número não pode ser alterado após a identificação da obra.",
        "justificativa": "O número é a chave de rastreamento da obra nos convênios, nos processos e na transparência.",
        "garantia": "Restrição UNIQUE em `obr.obras.numero` e validação em `Obra.validar()`.",
    },
    {
        "id": "RN-OBR-002",
        "titulo": "Ciclo de Vida da Obra",
        "tipo": "Máquina de estados",
        "processo": "PRO-OBR-001",
        "descricao": "A obra percorre `PLANEJADA -> EM_LICITACAO -> CONTRATADA -> EM_EXECUCAO -> CONCLUIDA`, com `SUSPENSA` e `CANCELADA` disponíveis. A conclusão e o cancelamento são terminais e obra concluída não aceita alteração cadastral.",
        "justificativa": "O ciclo reflete a situação real do empreendimento e preserva a memória das decisões.",
        "garantia": "Transições em `Obra.iniciar_execucao()`, `.suspender()`, `.concluir()` e `.cancelar()`.",
    },
    {
        "id": "RN-OBR-003",
        "titulo": "Pré-condições para Iniciar a Execução",
        "tipo": "Restrição",
        "processo": "PRO-OBR-001",
        "descricao": "A execução só pode ser iniciada em obra contratada ou suspensa, e exige empresa contratada e data de início prevista informadas.",
        "justificativa": "Sem contratação formal e prazo definido não há como aferir o andamento nem a responsável pela obra.",
        "garantia": "Validações em `Obra.iniciar_execucao()`.",
    },
    {
        "id": "RN-OBR-004",
        "titulo": "Coerência Físico-Financeira da Obra",
        "tipo": "Restrição",
        "processo": "PRO-OBR-003",
        "descricao": "Os valores e percentuais são não negativos, o valor contratado não supera o valor orçado, o valor pago não supera o valor medido e **o avanço financeiro nunca ultrapassa o avanço físico**.",
        "justificativa": "O município não pode desembolhar mais do que executou; a coerência entre os dois avanços é a base do controle social da obra pública.",
        "garantia": "Checks `ck_obr_obra_valores`, `ck_obr_obra_avanco` e `ck_obr_obra_pago`, e validação em `Obra.validar()`.",
    },
    {
        "id": "RN-OBR-005",
        "titulo": "Ciclo de Vida da Medição e Composição do Avanço",
        "tipo": "Máquina de estados",
        "processo": "PRO-OBR-002",
        "descricao": "A medição percorre `REGISTRADA -> CONFERIDA -> APROVADA`, com `GLOSADA` e `CANCELADA` disponíveis. Apenas medição aprovada compõe o avanço da obra; a conclusão exige 100% do avanço físico; o valor medido não pode superar o contratado e o número da medição é único por obra.",
        "justificativa": "Somente medição conferida e aprovada deve compor o avanço, para que o físico e o financeiro reflitam a execução real.",
        "garantia": "Transições em `MedicaoObra.conferir()`, `.aprovar()`, `.glosar()` e `.cancelar()`; índice único parcial `uq_obr_medicao_numero`; check `ck_obr_medicao_percentual`.",
    },
    {
        "id": "RN-OBR-006",
        "titulo": "Limite da Despesa ao Valor Medido",
        "tipo": "Restrição",
        "processo": "PRO-OBR-003",
        "descricao": "A despesa exige valor positivo, pertence a obra contratada ou em execução e não pode superar o saldo medido e ainda não pago.",
        "justificativa": "Não se paga o que não foi medido; a regra protege o erário de desembolsos antecipados sem lastro de execução.",
        "garantia": "Check `ck_obr_despesa_valor` e validações em `RegistrarDespesaUseCase` e `DespesaObra.validar()`.",
    },
    {
        "id": "RN-OBR-007",
        "titulo": "Ciclo de Vida da Etapa e Escala de Percentuais",
        "tipo": "Máquina de estados",
        "processo": "PRO-OBR-004",
        "descricao": "A etapa pertence a uma obra, exige responsável e percorre `PENDENTE -> EM_EXECUCAO -> CONCLUIDA`, com `ATRASADA` e `CANCELADA` disponíveis; concluí-la exige 100% do percentual previsto. O percentual previsto é o peso da etapa na obra e o percentual realizado é a conclusão da etapa: são escalas distintas e ambos ficam na faixa de 0 a 100.",
        "justificativa": "O peso previsto dimensiona a etapa no cronograma; a distinção entre as escalas permite concluir uma etapa de peso parcial sem distorcer o cronograma.",
        "garantia": "Transições em `EtapaObra.iniciar()` e `.concluir()`, e check `ck_obr_etapa_percentual`.",
    },
    {
        "id": "RN-OBR-008",
        "titulo": "Registro de Vistoria Fiscalizadora",
        "tipo": "Restrição",
        "processo": "PRO-OBR-004",
        "descricao": "A vistoria pertence a uma obra existente, exige fiscal identificado e registra tipo, parecer e percentual físico verificado na faixa de 0 a 100.",
        "justificativa": "A vistoria é a evidência de campo que confronta o avanço declarado com o avanço executado.",
        "garantia": "Check `ck_obr_vistoria_percentual` e validação em `VistoriaObra.validar()`.",
    },
]


OBR_RF = [
    ("RF-OBR-001", "O sistema deve permitir cadastrar, alterar, listar, consultar e excluir obras públicas.", "Essencial", "CAP-OBR-001", "RN-OBR-001, RN-OBR-002, RN-OBR-004",
     "POST /api/v1/obr/obras; GET /api/v1/obr/obras; GET /api/v1/obr/obras/{obra_id}; PATCH /api/v1/obr/obras/{obra_id}; DELETE /api/v1/obr/obras/{obra_id}"),
    ("RF-OBR-002", "O sistema deve permitir iniciar, suspender, concluir e cancelar a obra, com justificativa quando aplicável.", "Essencial", "CAP-OBR-001", "RN-OBR-002, RN-OBR-003, RN-OBR-005",
     "POST /api/v1/obr/obras/{obra_id}/iniciar-execucao; POST /api/v1/obr/obras/{obra_id}/suspender; POST /api/v1/obr/obras/{obra_id}/concluir; POST /api/v1/obr/obras/{obra_id}/cancelar"),
    ("RF-OBR-003", "O sistema deve permitir filtrar a listagem de obras por situação.", "Desejável", "CAP-OBR-001", "RN-OBR-002",
     "GET /api/v1/obr/obras"),
    ("RF-OBR-004", "O sistema deve permitir registrar, aprovar, glosar e cancelar medições físico-financeiras, recompondo o avanço da obra.", "Essencial", "CAP-OBR-002", "RN-OBR-004, RN-OBR-005",
     "POST /api/v1/obr/medicoes; POST /api/v1/obr/medicoes/{medicao_id}/aprovar; POST /api/v1/obr/medicoes/{medicao_id}/glosar; POST /api/v1/obr/medicoes/{medicao_id}/cancelar"),
    ("RF-OBR-005", "O sistema deve permitir registrar e excluir despesas financeiras da obra.", "Essencial", "CAP-OBR-003", "RN-OBR-004, RN-OBR-006",
     "POST /api/v1/obr/despesas; DELETE /api/v1/obr/despesas/{despesa_id}"),
    ("RF-OBR-006", "O sistema deve permitir cadastrar etapas, atualizar o avanço realizado e concluir etapas da obra.", "Essencial", "CAP-OBR-004", "RN-OBR-007",
     "POST /api/v1/obr/etapas; PATCH /api/v1/obr/etapas/{etapa_id}; POST /api/v1/obr/etapas/{etapa_id}/concluir"),
    ("RF-OBR-007", "O sistema deve permitir registrar vistorias fiscalizadoras com parecer sobre o avanço verificado.", "Essencial", "CAP-OBR-004", "RN-OBR-008",
     "POST /api/v1/obr/vistorias"),
    ("RF-OBR-008", "O sistema deve permitir consultar o acompanhamento consolidado da obra, reunindo medições, despesas, etapas e vistorias.", "Essencial", "CAP-OBR-005", "RN-OBR-004, RN-OBR-005, RN-OBR-006",
     "GET /api/v1/obr/obras/{obra_id}/acompanhamento"),
    ("RF-OBR-009", "O sistema deve permitir consultar, separadamente, as medições, despesas, etapas e vistorias de uma obra.", "Essencial", "CAP-OBR-005", "RN-OBR-005, RN-OBR-006, RN-OBR-007, RN-OBR-008",
     "GET /api/v1/obr/obras/{obra_id}/medicoes; GET /api/v1/obr/obras/{obra_id}/despesas; GET /api/v1/obr/obras/{obra_id}/etapas; GET /api/v1/obr/obras/{obra_id}/vistorias"),
]

OBR_CU = [
    ("CU-OBR-001", "Cadastrar obra pública", "AT-OBR-001", "CAP-OBR-001", "O servidor está autenticado e possui permissão de gestão de obras.",
     "Informar número, nome, tipo, contratação, fonte de recurso e valores orçado e contratado; verificar a unicidade do número (RN-OBR-001) e a coerência dos valores (RN-OBR-004); gravar a obra em situação planejada.",
     "A obra está cadastrada e planejada.", "RN-OBR-001, RN-OBR-004", "CadastrarObraUseCase"),
    ("CU-OBR-002", "Alterar cadastro da obra", "AT-OBR-001", "CAP-OBR-001", "A obra existe e não está concluída.",
     "Informar os campos a alterar; gravar a alteração e registrar a data (RN-OBR-002).",
     "A obra está atualizada.", "RN-OBR-002, RN-OBR-004", "AtualizarObraUseCase"),
    ("CU-OBR-003", "Iniciar a execução da obra", "AT-OBR-001", "CAP-OBR-001", "A obra está contratada ou suspensa, com empresa e data prevista informadas.",
     "Solicitar o início; exigir empresa contratada e data de início prevista (RN-OBR-003); registrar a data de início real.",
     "A obra está em execução.", "RN-OBR-002, RN-OBR-003", "IniciarExecucaoObraUseCase"),
    ("CU-OBR-004", "Suspender a obra", "AT-OBR-001", "CAP-OBR-001", "A obra está em execução ou contratada.",
     "Informar a justificativa; alterar a situação para suspensa (RN-OBR-002).",
     "A obra está suspensa com a justificativa registrada.", "RN-OBR-002", "SuspenderObraUseCase"),
    ("CU-OBR-005", "Concluir a obra", "AT-OBR-001", "CAP-OBR-001", "A obra está em execução ou suspensa, com 100% do avanço físico.",
     "Solicitar a conclusão; exigir 100% do avanço físico (RN-OBR-005); registrar a data de conclusão real.",
     "A obra está concluída com data de conclusão registrada.", "RN-OBR-002, RN-OBR-005", "ConcluirObraUseCase"),
    ("CU-OBR-006", "Cancelar a obra", "AT-OBR-001", "CAP-OBR-001", "A obra não está concluída nem cancelada.",
     "Informar a justificativa; alterar a situação para cancelada (RN-OBR-002).",
     "A obra está cancelada com a justificativa registrada.", "RN-OBR-002", "CancelarObraUseCase"),
    ("CU-OBR-007", "Excluir obra", "AT-OBR-001", "CAP-OBR-001", "A obra existe e não possui medições nem despesas.",
     "Solicitar a exclusão; havendo medições ou despesas, recusar com HTTP 409 (RN-OBR-005, RN-OBR-006); caso contrário, excluir logicamente.",
     "A obra está excluída logicamente e preserva o histórico.", "RN-OBR-005, RN-OBR-006", "ExcluirObraUseCase"),
    ("CU-OBR-008", "Registrar medição da obra", "AT-OBR-003", "CAP-OBR-002", "A obra está em execução ou suspensa.",
     "Informar número, tipo, percentual físico, valor medido e responsável técnico; verificar a unicidade do número e o teto do valor contratado (RN-OBR-005); gravar a medição em situação registrada.",
     "A medição está registrada.", "RN-OBR-005", "RegistrarMedicaoUseCase"),
    ("CU-OBR-009", "Aprovar medição", "AT-OBR-002", "CAP-OBR-002", "A medição existe e está registrada.",
     "Conferir a medição e aprová-la (RN-OBR-005); recompor o valor medido e o avanço físico da obra a partir das medições aprovadas.",
     "A medição está aprovada e o avanço da obra foi recomposto.", "RN-OBR-004, RN-OBR-005", "AprovarMedicaoUseCase"),
    ("CU-OBR-010", "Glosar medição", "AT-OBR-002", "CAP-OBR-002", "A medição existe e está conferida.",
     "Informar a justificativa; alterar a situação para glosada (RN-OBR-005).",
     "A medição está glosada e não compõe o avanço.", "RN-OBR-005", "GlosarMedicaoUseCase"),
    ("CU-OBR-011", "Cancelar medição", "AT-OBR-002", "CAP-OBR-002", "A medição existe e não está aprovada.",
     "Solicitar o cancelamento; alterar a situação para cancelada (RN-OBR-005).",
     "A medição está cancelada e não compõe o avanço.", "RN-OBR-005", "CancelarMedicaoUseCase"),
    ("CU-OBR-012", "Registrar despesa da obra", "AT-OBR-004", "CAP-OBR-003", "A obra está contratada ou em execução e há saldo medido.",
     "Informar descrição, tipo, valor, credor e medição vinculada; exigir valor positivo e não superior ao saldo medido a pagar (RN-OBR-006); gravar a despesa e recompor o avanço financeiro.",
     "A despesa está registrada e o avanço financeiro da obra foi recomposto.", "RN-OBR-004, RN-OBR-006", "RegistrarDespesaUseCase"),
    ("CU-OBR-013", "Excluir despesa", "AT-OBR-004", "CAP-OBR-003", "A despesa existe.",
     "Solicitar a exclusão; excluir logicamente a despesa e recompor o avanço financeiro da obra.",
     "A despesa está excluída e o avanço financeiro foi recomposto.", "RN-OBR-006", "ExcluirDespesaUseCase"),
    ("CU-OBR-014", "Cadastrar etapa da obra", "AT-OBR-003", "CAP-OBR-004", "A obra existe.",
     "Informar número, descrição, tipo, percentual previsto e responsável; gravar a etapa em situação pendente (RN-OBR-007).",
     "A etapa está cadastrada.", "RN-OBR-007", "CadastrarEtapaUseCase"),
    ("CU-OBR-015", "Atualizar avanço da etapa", "AT-OBR-003", "CAP-OBR-004", "A etapa existe.",
     "Informar o percentual realizado e a situação; validar a faixa de 0 a 100 (RN-OBR-007); gravar a alteração.",
     "O avanço da etapa está atualizado.", "RN-OBR-007", "AtualizarEtapaUseCase"),
    ("CU-OBR-016", "Concluir etapa", "AT-OBR-003", "CAP-OBR-004", "A etapa existe e não está concluída nem cancelada.",
     "Solicitar a conclusão; exigir 100% do percentual previsto (RN-OBR-007); registrar a data de conclusão.",
     "A etapa está concluída com data registrada.", "RN-OBR-007", "ConcluirEtapaUseCase"),
    ("CU-OBR-017", "Registrar vistoria da obra", "AT-OBR-002", "CAP-OBR-004", "A obra existe.",
     "Informar tipo, parecer, percentual físico verificado e fiscal; validar a faixa de 0 a 100 (RN-OBR-008); gravar a vistoria.",
     "A vistoria está registrada com o parecer do fiscal.", "RN-OBR-008", "RegistrarVistoriaUseCase"),
    ("CU-OBR-018", "Consultar o andamento da obra", "AT-OBR-005", "CAP-OBR-005", "Não há precondição.",
     "Informar a obra ou o filtro de situação; retornar valores, percentuais e, quando solicitado, o acompanhamento consolidado.",
     "O andamento da obra foi obtido.", "RN-OBR-004, RN-OBR-005, RN-OBR-006", "— (consulta aos repositórios)"),
]


OBR_HU = [
    ("HU-OBR-001", "Manter o cadastro das obras públicas", "Como gestor de obras",
     "cadastrar obras, convenir a contratação e manter os dados da obra", "dispor de cadastro oficial para o acompanhamento e a transparência", "CAP-OBR-001",
     "RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004",
     "Dado que o número da obra é novo, quando o gestor cadastra, então a obra é criada.;"
     "Dado que o número já existe, quando o gestor cadastra, então o sistema recusa com HTTP 409 (RN-OBR-001).;"
     "Dado que o valor contratado supera o orçado, quando o gestor cadastra, então o sistema recusa (RN-OBR-004).;"
     "Dado uma obra já concluída, quando o gestor tenta alterar o cadastro, então o sistema recusa (RN-OBR-002)."),
    ("HU-OBR-002", "Conduzir o ciclo de vida da obra", "Como gestor de obras",
     "iniciar, suspender, concluir e cancelar obras", "refletir no sistema a situação real do empreendimento", "CAP-OBR-001",
     "RN-OBR-002, RN-OBR-003, RN-OBR-005",
     "Dado uma obra contratada com empresa e data prevista, quando o gestor inicia a execução, então a obra passa a em execução.;"
     "Dado que a empresa não foi informada, quando o gestor tenta iniciar, então o sistema recusa (RN-OBR-003).;"
     "Dado uma obra com avanço físico parcial, quando o gestor tenta concluir, então o sistema recusa com HTTP 409 (RN-OBR-005)."),
    ("HU-OBR-003", "Medir e conferir o avanço da obra", "Como fiscal de obra",
     "conferir medições e aprovar ou glosar o avanço físico-financeiro", "assegurar que o medido corresponde ao executado", "CAP-OBR-002",
     "RN-OBR-004, RN-OBR-005",
     "Dado uma medição registrada, quando o fiscal confere e aprova, então a medição passa a aprovada e o avanço da obra é recomposto.;"
     "Dado que a medição não foi conferida, quando se tenta aprová-la, então o sistema recusa (RN-OBR-005).;"
     "Dado que o valor medido supera o contratado, quando o responsável registra, então o sistema recusa (RN-OBR-005).;"
     "Dado uma medição aprovada, quando o fiscal tenta cancelá-la, então o sistema recusa (RN-OBR-005)."),
    ("HU-OBR-004", "Registrar etapas e vistorias da obra", "Como fiscal de obra",
     "registrar etapas de execução e lavrar vistorias com parecer", "documentar o avanço físico e a fiscalização de campo", "CAP-OBR-004",
     "RN-OBR-007, RN-OBR-008",
     "Dado uma etapa com responsável, quando o responsável cadastra, então a etapa é criada.;"
     "Dado uma etapa de peso parcial totalmente executada, quando o fiscal conclui, então a etapa passa a concluída (RN-OBR-007).;"
     "Dado uma etapa com realizado abaixo do previsto, quando se tenta concluir, então o sistema recusa (RN-OBR-007).;"
     "Dado uma obra existente, quando o fiscal registra vistoria, então o parecer e o percentual verificado são gravados (RN-OBR-008)."),
    ("HU-OBR-005", "Registrar repasses e despesas da obra", "Como tesoureiro municipal",
     "registrar repasses, materiais e custos atribuíveis à obra", "pagar apenas o que foi medido e acompanhar o avanço financeiro", "CAP-OBR-003",
     "RN-OBR-004, RN-OBR-006",
     "Dado que há saldo medido, quando a tesouraria registra a despesa, então o avanço financeiro é recomposto.;"
     "Dado que a despesa supera o saldo medido a pagar, quando a tesouraria registra, então o sistema recusa com HTTP 409 (RN-OBR-006).;"
     "Dado que a obra está planejada, quando a tesouraria registra despesa, então o sistema recusa (RN-OBR-006)."),
    ("HU-OBR-006", "Consultar o andamento das obras", "Como cidadão",
     "consultar o percentual físico e financeiro de cada obra", "acompanhar a aplicação de recursos públicos", "CAP-OBR-005",
     "RN-OBR-004, RN-OBR-005, RN-OBR-006",
     "Dado que existem obras cadastradas, quando o cidadão consulta, então a lista de obras com seus percentuais é retornada.;"
     "Dado uma obra específica, quando o cidadão consulta o acompanhamento, então medições, despesas, etapas e vistorias são retornadas (RF-OBR-008).;"
     "Dado um identificador inexistente, quando o cidadão consulta, então o sistema responde HTTP 404."),
    ("HU-OBR-007", "Fiscalizar a regularidade financeira", "Como auditor do controle interno",
     "consultar a coerência entre avanço físico, medido e pago", "detectar pagamento de valor não executado", "CAP-OBR-005",
     "RN-OBR-004, RN-OBR-006",
     "Dado o conjunto de obras cadastradas, quando o auditor consulta, então nenhum caso de avanço financeiro superior ao físico é apresentado (RN-OBR-004).;"
     "Dado que não há saldo medido, quando o auditor verifica, então não há despesa acima do medido (RN-OBR-006)."),
]

OBR_RNF = [
    ("RNF-OBR-001", "Desempenho", "As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens.",
     "Teste de integração verificando o parâmetro `page_size` e a resposta paginada."),
    ("RNF-OBR-002", "Integridade", "A coerência físico-financeira e a unicidade devem ser garantidas no banco de dados, e não apenas na aplicação.",
     "Verificação dos 7 CHECK constraints e do índice único parcial `uq_obr_medicao_numero` nas migrações do schema `obr`."),
    ("RNF-OBR-003", "Robustez", "Identificadores malformados devem resultar em HTTP 404, e não em erro interno.",
     "Round-trip E2E consultando identificadores não-UUID."),
    ("RNF-OBR-004", "Usabilidade", "Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada.",
     "Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409."),
    ("RNF-OBR-005", "Rastreabilidade", "Toda medição, despesa, etapa e vistoria deve estar vinculada a uma obra existente e registrar autoria e data.",
     "Testes unitários e de integração verificando as referências e as colunas de auditoria."),
    ("RNF-OBR-006", "Compatibilidade", "A API deve manter contrato estável, versionado sob o prefixo `/api/v1/obr`.",
     "Verificação do OpenAPI publicado e da contagem de 21 paths e 24 operações."),
    ("RNF-OBR-007", "Desacoplamento", "O domínio não deve manter chave estrangeira física para outros bancos de domínios.",
     "Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco."),
    ("RNF-OBR-008", "Consistência do recálculo", "O avanço físico e financeiro da obra deve ser sempre recomposto a partir das medições aprovadas e das despesas registradas.",
     "Round-trip E2E comparando os valores da obra com a soma das medições aprovadas e das despesas."),
]
