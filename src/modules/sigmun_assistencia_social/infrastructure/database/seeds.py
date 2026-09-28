"""Seeds de dados DEMO do DOM-ASS — Assistência Social.

Cria dados demonstrativos para validação técnica e visual das telas
administrativas do DOM-ASS (CadÚnico local, benefícios eventuais,
CRAS/CREAS e atendimentos sociais).

IMPORTANTE:
- Os dados aqui definidos são DEMONSTRATIVOS e fictícios.
- Não representam cadastro real de famílias do Município.
- Nomes, NIS e CPFs foram gerados para teste e não correspondem a
  pessoas reais nem a famílias reais.
- O seed é executado sob demanda (não no startup da API).
- A criação respeita as regras de negócio do domínio: os registros são
  gravados pelos use cases reais, e não por INSERT direto.

Classificação da Informação: Pública
Responsável: Gildazio
Status da revisão: Vigente
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from sqlalchemy.orm import Session

from ...application.use_cases import (
    AprovarBeneficioUseCase,
    CadastrarFamiliaInput,
    CadastrarFamiliaUseCase,
    CadastrarPessoaInput,
    CadastrarPessoaUseCase,
    CadastrarUnidadeInput,
    CadastrarUnidadeUseCase,
    CancelarBeneficioUseCase,
    EntregarBeneficioUseCase,
    NegarBeneficioUseCase,
    RegistrarAtendimentoInput,
    RegistrarAtendimentoUseCase,
    SolicitarBeneficioInput,
    SolicitarBeneficioUseCase,
)
from ..repositories import (
    SQLAlchemyAtendimentoRepository,
    SQLAlchemyBeneficioRepository,
    SQLAlchemyFamiliaRepository,
    SQLAlchemyPessoaRepository,
    SQLAlchemyUnidadeRepository,
)

AUTOR_SEED = "seed-ass"


# ============================================================================
# DADOS DEMONSTRATIVOS
# ============================================================================


@dataclass(frozen=True)
class UnidadeSeed:
    """Unidade de assistencia social a ser criada."""

    codigo: str
    nome: str
    tipo: str
    endereco: str
    telefone: str
    email: str
    responsavel: str


UNIDADES_DEMO: tuple[UnidadeSeed, ...] = (
    UnidadeSeed(
        codigo="CRAS-01",
        nome="CRAS Centro",
        tipo="cras",
        endereco="Praca da Matriz, s/n - Centro",
        telefone="(73) 3212-1001",
        email="cras.centro@camacan.ba.gov.br",
        responsavel="Maria Aparecida Souza",
    ),
    UnidadeSeed(
        codigo="CRAS-02",
        nome="CRAS Nossa Senhora dos Anjos",
        tipo="cras",
        endereco="Rua das Flores, 120 - Nova Esperanca",
        telefone="(73) 3212-1002",
        email="cras.anjos@camacan.ba.gov.br",
        responsavel="Jose Carlos Lima",
    ),
    UnidadeSeed(
        codigo="CREAS-01",
        nome="CREAS Centro",
        tipo="creas",
        endereco="Av. Principal, 450 - Centro",
        telefone="(73) 3212-2001",
        email="creas.centro@camacan.ba.gov.br",
        responsavel="Ana Paula Ferreira",
    ),
    UnidadeSeed(
        codigo="POP-01",
        nome="Centro Popular",
        tipo="centro_pop",
        endereco="Rua do Mercado, 88 - Comercio",
        telefone="(73) 3212-3001",
        email="centropopular@camacan.ba.gov.br",
        responsavel="Carlos Eduardo Reis",
    ),
    UnidadeSeed(
        codigo="ABR-01",
        nome="Abrigo Municipal",
        tipo="abrigo",
        endereco="Estrada do Abrigo, km 2 - Zona Rural",
        telefone="(73) 3212-4001",
        email="abrigo@camacan.ba.gov.br",
        responsavel="Beatriz Oliveira Rocha",
    ),
)


@dataclass(frozen=True)
class PessoaSeed:
    """Pessoa membro de uma familia do CadUnico."""

    nome: str
    cpf: str
    data_nascimento: str
    sexo: str
    nome_mae: str
    parentesco: str
    escolaridade: str
    ocupacao: str
    renda: float


@dataclass(frozen=True)
class FamiliaSeed:
    """Familia do CadUnico e seus membros."""

    nis: str
    responsavel_nome: str
    responsavel_cpf: str
    endereco: str
    telefone: str
    renda_per_capita: float
    pessoas: tuple[PessoaSeed, ...]


FAMILIAS_DEMO: tuple[FamiliaSeed, ...] = (
    FamiliaSeed(
        nis="12345678901",
        responsavel_nome="Maria Aparecida Souza",
        responsavel_cpf="12345678909",
        endereco="Rua das Flores, 120 - Nova Esperanca",
        telefone="(73) 99999-1201",
        renda_per_capita=180.00,
        pessoas=(
            PessoaSeed("Maria Aparecida Souza", "12345678909", "1978-04-12", "feminino", "Rosa Souza Lima", "responsavel", "ensino fundamental", "domestica", 180.00),
            PessoaSeed("Joao Pedro Souza", "12345678917", "2012-09-30", "masculino", "Maria Aparecida Souza", "filho", "ensino fundamental", "estudante", 0.0),
            PessoaSeed("Ana Clara Souza", "12345678925", "2016-02-21", "feminino", "Maria Aparecida Souza", "filha", "ensino fundamental", "estudante", 0.0),
        ),
    ),
    FamiliaSeed(
        nis="12345678902",
        responsavel_nome="Jose Carlos Lima",
        responsavel_cpf="23456789008",
        endereco="Av. Principal, 450 - Centro",
        telefone="(73) 99999-1202",
        renda_per_capita=220.50,
        pessoas=(
            PessoaSeed("Jose Carlos Lima", "23456789008", "1972-11-05", "masculino", "Pedro Lima", "responsavel", "ensino medio", "pedreiro", 220.50),
            PessoaSeed("Rita de Cassia Lima", "23456789016", "1976-07-18", "feminino", "Ana Costa", "conjuge", "ensino fundamental", "costureira", 150.00),
            PessoaSeed("Lucas Lima", "23456789024", "2004-03-14", "masculino", "Rita de Cassia Lima", "filho", "ensino medio", "estudante", 0.0),
        ),
    ),
    FamiliaSeed(
        nis="12345678903",
        responsavel_nome="Ana Paula Ferreira",
        responsavel_cpf="34567890007",
        endereco="Rua do Mercado, 88 - Comercio",
        telefone="(73) 99999-1203",
        renda_per_capita=120.00,
        pessoas=(
            PessoaSeed("Ana Paula Ferreira", "34567890007", "1988-06-23", "feminino", "Marta Ferreira", "responsavel", "ensino medio", "comerciante", 120.00),
            PessoaSeed("Bento Ferreira", "34567890015", "1938-01-09", "masculino", "Joana Ferreira", "pai", "ensino fundamental", "aposentado", 0.0),
        ),
    ),
    FamiliaSeed(
        nis="12345678904",
        responsavel_nome="Carlos Eduardo Reis",
        responsavel_cpf="45678900006",
        endereco="Estrada do Abrigo, km 2 - Zona Rural",
        telefone="(73) 99999-1204",
        renda_per_capita=90.00,
        pessoas=(
            PessoaSeed("Carlos Eduardo Reis", "45678900006", "1990-09-02", "masculino", "Sandra Reis", "responsavel", "ensino fundamental", "trabalhador rural", 90.00),
            PessoaSeed("Marina Reis", "45678900014", "1994-12-11", "feminino", "Sandra Reis", "conjuge", "ensino fundamental", "trabalhadora rural", 0.0),
        ),
    ),
    FamiliaSeed(
        nis="12345678905",
        responsavel_nome="Beatriz Oliveira Rocha",
        responsavel_cpf="56789000005",
        endereco="Rua das Acacias, 33 - Jardim Novo",
        telefone="(73) 99999-1205",
        renda_per_capita=260.00,
        pessoas=(
            PessoaSeed("Beatriz Oliveira Rocha", "56789000005", "1984-08-17", "feminino", "Helena Rocha", "responsavel", "ensino superior", "professora", 260.00),
            PessoaSeed("Felipe Rocha", "56789000013", "2014-05-26", "masculino", "Beatriz Oliveira Rocha", "filho", "ensino fundamental", "estudante", 0.0),
        ),
    ),
    FamiliaSeed(
        nis="12345678906",
        responsavel_nome="Carlos Alberto Nunes",
        responsavel_cpf="67890000004",
        endereco="Travessa do Sol, 7 - Vila Nova",
        telefone="(73) 99999-1206",
        renda_per_capita=150.00,
        pessoas=(
            PessoaSeed("Carlos Alberto Nunes", "67890000004", "1969-10-08", "masculino", "Jose Nunes", "responsavel", "ensino fundamental", "servidor publico", 150.00),
            PessoaSeed("Elaine Nunes", "67890000012", "1971-02-19", "feminino", "Marcia Souza", "conjuge", "ensino fundamental", "aposentada", 0.0),
        ),
    ),
)



@dataclass(frozen=True)
class BeneficioSeed:
    """Beneficio eventual solicitado para uma familia do seed."""

    nis: str
    codigo_unidade: str
    tipo: str
    descricao: str
    valor: float
    quantidade: int
    observacao: str
    estado: str


# O campo `estado` define a situacao final desejada do beneficio, permitindo
# gerar a visao geral com filtros de status representativos.
BENEFICIOS_DEMO: tuple[BeneficioSeed, ...] = (
    BeneficioSeed("12345678901", "CRAS-01", "alimentacao", "Cesta basica mensal", 150.00, 1, "Familia com 3 pessoas de baixa renda.", "entregue"),
    BeneficioSeed("12345678901", "CRAS-01", "medicamento", "Medicamento de uso continuo", 85.00, 1, "Idoso com acompanhamento pela unidade de saude.", "aprovado"),
    BeneficioSeed("12345678902", "CRAS-01", "aluguel", "Auxilio aluguel", 200.00, 1, "Desemprego do responsavel.", "solicitado"),
    BeneficioSeed("12345678902", "CREAS-01", "alimentacao", "Cesta basica", 150.00, 1, "Adolescente em acompanhamento no CREAS.", "entregue"),
    BeneficioSeed("12345678903", "CREAS-01", "natalidade", "Kit bebe", 300.00, 1, "Nascimento de bebe ha tres meses.", "negado"),
    BeneficioSeed("12345678904", "POP-01", "alimentacao", "Cesta basica", 150.00, 1, "Trabalhadores rurais em situacao vulneravel.", "entregue"),
    BeneficioSeed("12345678905", "CRAS-02", "funeral", "Auxilio funeral", 600.00, 1, "Familia com renda acima do teto e sem BPC.", "negado"),
    BeneficioSeed("12345678905", "CRAS-02", "medicamento", "Medicamento controlado", 120.00, 1, "Uso continuo conforme laudo medico.", "aprovado"),
    BeneficioSeed("12345678906", "ABR-01", "alimentacao", "Cesta basica", 150.00, 1, "Familia atendida em abrigo temporario.", "solicitado"),
    BeneficioSeed("12345678906", "POP-01", "aluguel", "Auxilio aluguel", 200.00, 1, "Desocupacao do responsavel.", "cancelado"),
    BeneficioSeed("12345678903", "CRAS-01", "calamidade", "Auxilio calamidade", 250.00, 1, "Danos causados por chuva forte na regiao.", "solicitado"),
    BeneficioSeed("12345678904", "CRAS-02", "outro", "Material de higiene", 80.00, 1, "Requerimento avulso aprovado na escuta inicial.", "aprovado"),
)


@dataclass(frozen=True)
class AtendimentoSeed:
    """Atendimento social registrado para uma pessoa do seed."""

    cpf: str
    codigo_unidade: str
    tipo: str
    profissional: str
    descricao: str
    encaminhamento: str
    dias_atras: int


ATENDIMENTOS_DEMO: tuple[AtendimentoSeed, ...] = (
    AtendimentoSeed("12345678909", "CRAS-01", "acolhimento", "Maria Aparecida Souza - Assistente Social", "Escuta inicial e atualizacao do cadastro.", "", 45),
    AtendimentoSeed("12345678917", "CRAS-01", "visita_domiciliar", "Maria Aparecida Souza - Assistente Social", "Visita domiciliar para composicao familiar.", "Escola municipal", 30),
    AtendimentoSeed("23456789008", "CRAS-01", "orientacao", "Jose Carlos Lima - Assistente Social", "Orientacao sobre beneficios eventuais e CadUnico.", "", 25),
    AtendimentoSeed("23456789024", "CREAS-01", "acolhimento", "Ana Paula Ferreira - Assistente Social", "Acolhimento inicial do adolescente no CREAS.", "Conselho tutelar", 22),
    AtendimentoSeed("34567890007", "CREAS-01", "encaminhamento", "Ana Paula Ferreira - Assistente Social", "Encaminhamento para acompanhamento do idoso.", "Unidade basica de saude", 18),
    AtendimentoSeed("45678900006", "POP-01", "acolhimento", "Carlos Eduardo Reis - Assistente Social", "Atendimento no centro popular para inclusao no cadastro.", "", 15),
    AtendimentoSeed("56789000005", "CRAS-02", "orientacao", "Beatriz Oliveira Rocha - Assistente Social", "Orientacao sobre beneficios eventuais e uso do Cartao Unico.", "", 12),
    AtendimentoSeed("67890000004", "ABR-01", "acolhimento", "Carlos Alberto Nunes - Assistente Social", "Acolhimento no abrigo municipal.", "CRAS-02", 10),
    AtendimentoSeed("12345678925", "CRAS-01", "grupo_convivencia", "Maria Aparecida Souza - Assistente Social", "Participacao em grupo de convivencia infantil.", "", 8),
    AtendimentoSeed("23456789016", "CREAS-01", "orientacao", "Ana Paula Ferreira - Assistente Social", "Orientacao sobre qualificacao profissional.", "SENAC", 6),
)




# EXECUCAO DO SEED
# ============================================================================


def _criar_unidades(session: Session) -> tuple[dict[str, str], int]:
    """Cria as unidades de referencia. Retorna (codigo -> id, criadas)."""
    repo = SQLAlchemyUnidadeRepository(session)
    use_case = CadastrarUnidadeUseCase(repo)

    ids: dict[str, str] = {}
    criadas = 0

    for seed in UNIDADES_DEMO:
        existente = repo.get_by_codigo(seed.codigo)
        if existente is not None:
            ids[seed.codigo] = existente.id
            continue

        unidade = use_case.execute(
            CadastrarUnidadeInput(
                codigo=seed.codigo,
                nome=seed.nome,
                tipo=seed.tipo,
                endereco=seed.endereco,
                telefone=seed.telefone,
                email=seed.email,
                responsavel=seed.responsavel,
                autor_id=AUTOR_SEED,
            )
        )
        ids[seed.codigo] = unidade.id
        criadas += 1

    return ids, criadas


def _criar_familias_e_pessoas(
    session: Session,
) -> tuple[dict[str, str], dict[str, str], int, int]:
    """Cria familias e pessoas. Retorna (nis->id, cpf->id, familias, pessoas)."""
    familias_repo = SQLAlchemyFamiliaRepository(session)
    pessoas_repo = SQLAlchemyPessoaRepository(session)
    use_case_familia = CadastrarFamiliaUseCase(familias_repo)
    use_case_pessoa = CadastrarPessoaUseCase(pessoas_repo, familias_repo)

    familia_ids: dict[str, str] = {}
    pessoa_ids: dict[str, str] = {}
    familias_criadas = 0
    pessoas_criadas = 0

    for seed in FAMILIAS_DEMO:
        familia_existente = familias_repo.get_by_nis(seed.nis)
        if familia_existente is None:
            familia = use_case_familia.execute(
                CadastrarFamiliaInput(
                    nis=seed.nis,
                    responsavel_nome=seed.responsavel_nome,
                    responsavel_cpf=seed.responsavel_cpf,
                    endereco=seed.endereco,
                    telefone=seed.telefone,
                    renda_per_capita=seed.renda_per_capita,
                    quantidade_pessoas=len(seed.pessoas),
                    autor_id=AUTOR_SEED,
                )
            )
            familia_ids[seed.nis] = familia.id
            familias_criadas += 1
        else:
            familia_ids[seed.nis] = familia_existente.id

        for pessoa_seed in seed.pessoas:
            pessoa_existente = pessoas_repo.get_by_cpf(pessoa_seed.cpf)
            if pessoa_existente is not None:
                pessoa_ids[pessoa_seed.cpf] = pessoa_existente.id
                continue

            pessoa = use_case_pessoa.execute(
                CadastrarPessoaInput(
                    familia_id=familia_ids[seed.nis],
                    nome=pessoa_seed.nome,
                    cpf=pessoa_seed.cpf,
                    data_nascimento=pessoa_seed.data_nascimento,
                    sexo=pessoa_seed.sexo,
                    nome_mae=pessoa_seed.nome_mae,
                    parentesco=pessoa_seed.parentesco,
                    escolaridade=pessoa_seed.escolaridade,
                    ocupacao=pessoa_seed.ocupacao,
                    renda=pessoa_seed.renda,
                    autor_id=AUTOR_SEED,
                )
            )
            pessoa_ids[pessoa_seed.cpf] = pessoa.id
            pessoas_criadas += 1

    return familia_ids, pessoa_ids, familias_criadas, pessoas_criadas



def _criar_beneficios(
    session: Session,
    familia_ids: dict[str, str],
    unidades_ids: dict[str, str],
) -> int:
    """Cria beneficios eventuais e aplica o estado final desejado."""
    familias_repo = SQLAlchemyFamiliaRepository(session)
    unidades_repo = SQLAlchemyUnidadeRepository(session)
    beneficios_repo = SQLAlchemyBeneficioRepository(session)

    use_case_solicitar = SolicitarBeneficioUseCase(
        beneficios_repo, familias_repo, unidades_repo
    )
    use_case_aprovar = AprovarBeneficioUseCase(beneficios_repo)
    use_case_negar = NegarBeneficioUseCase(beneficios_repo)
    use_case_entregar = EntregarBeneficioUseCase(beneficios_repo)
    use_case_cancelar = CancelarBeneficioUseCase(beneficios_repo)

    criados = 0

    for seed in BENEFICIOS_DEMO:
        familia_id = familia_ids.get(seed.nis)
        unidade_id = unidades_ids.get(seed.codigo_unidade)
        if familia_id is None or unidade_id is None:
            continue

        # Idempotencia: nao duplica beneficios da mesma familia/tipo.
        ja_existe = any(
            b.familia_id == familia_id
            and b.descricao == seed.descricao
            for b in beneficios_repo.list_by_familia(familia_id)
        )
        if ja_existe:
            continue

        beneficio = use_case_solicitar.execute(
            SolicitarBeneficioInput(
                familia_id=familia_id,
                tipo=seed.tipo,
                descricao=seed.descricao,
                valor=seed.valor,
                quantidade=seed.quantidade,
                unidade_id=unidade_id,
                observacao=seed.observacao,
                autor_id=AUTOR_SEED,
            )
        )
        beneficio_id = beneficio.id

        # Aplica as transicoes ate o estado desejado, usando os use cases.
        if seed.estado in ("aprovado", "entregue"):
            use_case_aprovar.execute(beneficio_id)
        if seed.estado == "entregue":
            use_case_entregar.execute(beneficio_id)
        elif seed.estado == "negado":
            use_case_negar.execute(
                beneficio_id, "Renda acima do teto previsto na norma municipal"
            )
        elif seed.estado == "cancelado":
            use_case_cancelar.execute(beneficio_id)

        criados += 1

    return criados


def _criar_atendimentos(
    session: Session,
    pessoa_ids: dict[str, str],
    unidades_ids: dict[str, str],
) -> int:
    """Cria atendimentos sociais datados no passado recente."""
    pessoas_repo = SQLAlchemyPessoaRepository(session)
    unidades_repo = SQLAlchemyUnidadeRepository(session)
    atendimentos_repo = SQLAlchemyAtendimentoRepository(session)

    use_case = RegistrarAtendimentoUseCase(
        atendimentos_repo, pessoas_repo, unidades_repo
    )

    criados = 0
    hoje = date.today()

    for seed in ATENDIMENTOS_DEMO:
        pessoa_id = pessoa_ids.get(seed.cpf)
        unidade_id = unidades_ids.get(seed.codigo_unidade)
        if pessoa_id is None or unidade_id is None:
            continue

        data_atendimento = hoje - timedelta(days=seed.dias_atras)

        # Idempotencia: atendimentos sao append-only (o repositorio faz
        # `session.add` incondicional e nao possui chave natural), entao a
        # duplicidade e evitada por (pessoa, unidade, data, descricao).
        ja_existe = any(
            a.pessoa_id == pessoa_id
            and a.unidade_id == unidade_id
            and a.data == data_atendimento
            and a.descricao == seed.descricao
            for a in atendimentos_repo.list_by_pessoa(pessoa_id)
        )
        if ja_existe:
            continue

        # O atendimento ja e persistido pelo use case (com a data histórica
        # no campo `data`). Nao deve ser salvo novamente: o repositorio de
        # atendimentos faz `session.add` incondicional, e um segundo save
        # violaria a chave primaria.
        use_case.execute(
            RegistrarAtendimentoInput(
                pessoa_id=pessoa_id,
                unidade_id=unidade_id,
                tipo=seed.tipo,
                data=data_atendimento,
                descricao=seed.descricao,
                encaminhamento=seed.encaminhamento,
                profissional=seed.profissional,
                autor_id=AUTOR_SEED,
            )
        )
        criados += 1

    return criados


def popular_seed_ass(session: Session) -> dict[str, int]:
    """Popula os dados demonstrativos do DOM-ASS.

    A funcao nao realiza commit: o controle transacional pertence ao
    chamador. E idempotente: reexecutar nao duplica registros.

    Retorna um resumo com as quantidades criadas nesta execucao:
        unidades_criadas
        familias_criadas
        pessoas_criadas
        beneficios_criados
        atendimentos_criados
    """
    unidades_ids, unidades_criadas = _criar_unidades(session)
    (
        familia_ids,
        pessoa_ids,
        familias_criadas,
        pessoas_criadas,
    ) = _criar_familias_e_pessoas(session)

    beneficios_criados = _criar_beneficios(session, familia_ids, unidades_ids)
    atendimentos_criados = _criar_atendimentos(session, pessoa_ids, unidades_ids)

    session.flush()

    return {
        "unidades_criadas": unidades_criadas,
        "familias_criadas": familias_criadas,
        "pessoas_criadas": pessoas_criadas,
        "beneficios_criados": beneficios_criados,
        "atendimentos_criados": atendimentos_criados,
    }



# ============================================================================


def limpar_seed_ass(session: Session) -> dict[str, int]:
    """Remove os registros criados pelo seed do DOM-ASS.

    A ordem respeita as dependencias logicas: atendimentos e beneficios
    primeiro, depois pessoas, familias e unidades.

    Retorna as quantidades removidas por tabela.
    """
    from .models import (
        AtendimentoSocialModel,
        BeneficioEventualModel,
        FamiliaCadUnicoModel,
        PessoaCadUnicoModel,
        UnidadeAssistenciaModel,
    )

    nis_demo = {f.nis for f in FAMILIAS_DEMO}
    codigos_demo = {u.codigo for u in UNIDADES_DEMO}
    cpfs_demo = {p.cpf for f in FAMILIAS_DEMO for p in f.pessoas}

    familia_ids = [
        str(m.id)
        for m in session.query(FamiliaCadUnicoModel)
        .filter(FamiliaCadUnicoModel.nis.in_(nis_demo))
        .all()
    ]
    pessoa_ids = [
        str(m.id)
        for m in session.query(PessoaCadUnicoModel)
        .filter(PessoaCadUnicoModel.cpf.in_(cpfs_demo))
        .all()
    ]

    def _apagar(model, filtro) -> int:
        q = session.query(model)
        if filtro is not None:
            q = q.filter(filtro)
        return int(q.delete(synchronize_session=False) or 0)

    removidos: dict[str, int] = {
        "atendimentos": _apagar(
            AtendimentoSocialModel,
            AtendimentoSocialModel.pessoa_id.in_(pessoa_ids) if pessoa_ids else None,
        ),
        "beneficios": _apagar(
            BeneficioEventualModel,
            BeneficioEventualModel.familia_id.in_(familia_ids) if familia_ids else None,
        ),
        "pessoas": _apagar(
            PessoaCadUnicoModel,
            PessoaCadUnicoModel.cpf.in_(cpfs_demo) if cpfs_demo else None,
        ),
        "familias": _apagar(
            FamiliaCadUnicoModel,
            FamiliaCadUnicoModel.nis.in_(nis_demo) if nis_demo else None,
        ),
        "unidades": _apagar(
            UnidadeAssistenciaModel,
            UnidadeAssistenciaModel.codigo.in_(codigos_demo) if codigos_demo else None,
        ),
    }

    session.flush()
    return removidos
