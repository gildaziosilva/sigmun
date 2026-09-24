"""Use cases do DOM-EDU - Educacao Publica."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.aluno import Aluno, Sexo
from ..domain.entities.diario import LancamentoDiario
from ..domain.entities.matricula import Matricula
from ..domain.entities.merenda import DistribuicaoMerenda, ItemMerenda
from ..domain.entities.transporte import PassagemTransporte, RotaTransporte


@dataclass
class CadastrarAlunoInput:
    """DTO de cadastro de aluno."""

    nome: str
    cpf: str = ""
    data_nascimento: str = ""
    sexo: str = "ignorado"
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    autor_id: str = ""


class CadastrarAlunoUseCase:
    """Cadastra um aluno (RN-EDU-001)."""

    def __init__(self, repo: ports.RepositorioAluno) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarAlunoInput) -> Aluno:
        """Executa o cadastro."""
        from ..domain.exceptions import AlunoJaCadastradoError, RegraNegocioError

        if not dto.nome:
            raise RegraNegocioError("Nome do aluno e obrigatorio (RN-EDU-001)")
        if dto.cpf and self._repo.get_by_cpf(dto.cpf) is not None:
            raise AlunoJaCadastradoError("CPF ja cadastrado (RN-EDU-001)")
        aluno = Aluno(
            nome=dto.nome,
            cpf=dto.cpf,
            data_nascimento=dto.data_nascimento,
            sexo=Sexo(dto.sexo),
            nome_mae=dto.nome_mae,
            telefone=dto.telefone,
            endereco=dto.endereco,
            created_by=dto.autor_id,
        )
        aluno.validar()
        return self._repo.save(aluno)


@dataclass
class RealizarMatriculaInput:
    """DTO de matricula escolar."""

    aluno_id: str
    escola: str
    serie: str
    turno: str = "manha"
    ano_letivo: int = 0
    autor_id: str = ""


class RealizarMatriculaUseCase:
    """Realiza a matricula do aluno (RN-EDU-010)."""

    def __init__(
        self,
        repo: ports.RepositorioMatricula,
        alunos: ports.RepositorioAluno,
    ) -> None:
        self._repo = repo
        self._alunos = alunos

    def execute(self, dto: RealizarMatriculaInput) -> Matricula:
        """Executa a matricula."""
        from ..domain.exceptions import (
            AlunoNaoEncontradoError,
            MatriculaJaAtivaError,
        )

        aluno = self._alunos.get_by_id(dto.aluno_id)
        if aluno is None:
            raise AlunoNaoEncontradoError("Aluno nao encontrado para matricula")
        if self._repo.get_ativa_by_aluno(dto.aluno_id) is not None:
            raise MatriculaJaAtivaError(
                "Aluno ja possui matricula ativa (RN-EDU-010)"
            )
        matricula = Matricula(
            aluno_id=dto.aluno_id,
            escola=dto.escola,
            serie=dto.serie,
            turno=dto.turno,
            ano_letivo=dto.ano_letivo or date.today().year,
            data_matricula=date.today(),
            created_by=dto.autor_id,
        )
        matricula.validar()
        return self._repo.save(matricula)


class TransferirMatriculaUseCase:
    """Transfere a matricula para outra escola (RN-EDU-010)."""

    def __init__(self, repo: ports.RepositorioMatricula) -> None:
        self._repo = repo

    def execute(
        self, matricula_id: str, escola_destino: str, motivo: str = ""
    ) -> Matricula:
        """Executa a transferencia."""
        from ..domain.exceptions import MatriculaNaoEncontradaError

        matricula = self._repo.get_by_id(matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError("Matricula nao encontrada")
        matricula.transferir(escola_destino, motivo)
        return self._repo.save(matricula)


class CancelarMatriculaUseCase:
    """Cancela a matricula vigente (RN-EDU-010)."""

    def __init__(self, repo: ports.RepositorioMatricula) -> None:
        self._repo = repo

    def execute(self, matricula_id: str, motivo: str = "") -> Matricula:
        """Executa o cancelamento."""
        from ..domain.exceptions import MatriculaNaoEncontradaError

        matricula = self._repo.get_by_id(matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError("Matricula nao encontrada")
        matricula.cancelar(motivo)
        return self._repo.save(matricula)


class ConcluirMatriculaUseCase:
    """Conclui a matricula (fim do ano letivo) (RN-EDU-010)."""

    def __init__(self, repo: ports.RepositorioMatricula) -> None:
        self._repo = repo

    def execute(self, matricula_id: str) -> Matricula:
        """Executa a conclusao."""
        from ..domain.exceptions import MatriculaNaoEncontradaError

        matricula = self._repo.get_by_id(matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError("Matricula nao encontrada")
        matricula.concluir()
        return self._repo.save(matricula)


@dataclass
class RegistrarLancamentoDiarioInput:
    """DTO de lancamento no diario de classe digital."""

    matricula_id: str
    data: date | None = None
    presente: bool = True
    nota: float | None = None
    observacao: str = ""
    autor_id: str = ""


class RegistrarLancamentoDiarioUseCase:
    """Registra frequencia/nota no diario digital (RN-EDU-020)."""

    def __init__(
        self,
        repo: ports.RepositorioLancamentoDiario,
        matriculas: ports.RepositorioMatricula,
    ) -> None:
        self._repo = repo
        self._matriculas = matriculas

    def execute(self, dto: RegistrarLancamentoDiarioInput) -> LancamentoDiario:
        """Executa o lancamento."""
        from ..domain.exceptions import (
            EstadoMatriculaInvalidoError,
            MatriculaNaoEncontradaError,
        )

        matricula = self._matriculas.get_by_id(dto.matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError(
                "Matricula nao encontrada para lancamento"
            )
        if not matricula.esta_ativa:
            raise EstadoMatriculaInvalidoError(
                "Lancamento no diario exige matricula ativa (RN-EDU-020)"
            )
        lancamento = LancamentoDiario(
            matricula_id=dto.matricula_id,
            data=dto.data or date.today(),
            presente=dto.presente,
            nota=dto.nota,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        lancamento.validar()
        return self._repo.save(lancamento)


@dataclass
class CadastrarRotaTransporteInput:
    """DTO de rota de transporte escolar."""

    identificacao: str
    motorista: str
    veiculo: str = ""
    vagas: int = 0
    turno: str = "manha"
    autor_id: str = ""


class CadastrarRotaTransporteUseCase:
    """Cadastra uma rota de transporte escolar (RN-EDU-030)."""

    def __init__(self, repo: ports.RepositorioRotaTransporte) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarRotaTransporteInput) -> RotaTransporte:
        """Executa o cadastro."""
        rota = RotaTransporte(
            identificacao=dto.identificacao,
            motorista=dto.motorista,
            veiculo=dto.veiculo,
            vagas=dto.vagas,
            turno=dto.turno,
            created_by=dto.autor_id,
        )
        rota.validar()
        return self._repo.save(rota)


class InativarRotaTransporteUseCase:
    """Inativa rota (encerra novas passagens)."""

    def __init__(self, repo: ports.RepositorioRotaTransporte) -> None:
        self._repo = repo

    def execute(self, rota_id: str) -> RotaTransporte:
        """Executa a inativacao."""
        from ..domain.exceptions import RotaNaoEncontradaError

        rota = self._repo.get_by_id(rota_id)
        if rota is None:
            raise RotaNaoEncontradaError("Rota nao encontrada")
        rota.inativar()
        return self._repo.save(rota)


class AtivarRotaTransporteUseCase:
    """Reativa rota de transporte escolar."""

    def __init__(self, repo: ports.RepositorioRotaTransporte) -> None:
        self._repo = repo

    def execute(self, rota_id: str) -> RotaTransporte:
        """Executa a ativacao."""
        from ..domain.exceptions import RotaNaoEncontradaError

        rota = self._repo.get_by_id(rota_id)
        if rota is None:
            raise RotaNaoEncontradaError("Rota nao encontrada")
        rota.ativar()
        return self._repo.save(rota)



@dataclass
class RegistrarPassagemInput:
    """DTO de passagem no transporte escolar."""

    rota_id: str
    matricula_id: str
    data: date | None = None
    autor_id: str = ""


class RegistrarPassagemUseCase:
    """Registra passagem com cheque de vagas (RN-EDU-030)."""

    def __init__(
        self,
        repo: ports.RepositorioPassagemTransporte,
        rotas: ports.RepositorioRotaTransporte,
        matriculas: ports.RepositorioMatricula,
    ) -> None:
        self._repo = repo
        self._rotas = rotas
        self._matriculas = matriculas

    def execute(self, dto: RegistrarPassagemInput) -> PassagemTransporte:
        """Executa o registro de passagem."""
        from ..domain.exceptions import (
            EstadoMatriculaInvalidoError,
            EstadoRotaInvalidoError,
            MatriculaNaoEncontradaError,
            RotaNaoEncontradaError,
            VagaIndisponivelError,
        )

        rota = self._rotas.get_by_id(dto.rota_id)
        if rota is None:
            raise RotaNaoEncontradaError("Rota nao encontrada para passagem")
        if not rota.esta_ativa:
            raise EstadoRotaInvalidoError("Passagem exige rota ativa (RN-EDU-030)")
        matricula = self._matriculas.get_by_id(dto.matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError("Matricula nao encontrada para passagem")
        if not matricula.esta_ativa:
            raise EstadoMatriculaInvalidoError(
                "Passagem exige matricula ativa (RN-EDU-030)"
            )
        data = dto.data or date.today()
        if self._repo.count_by_rota_data(rota.id, data) >= rota.vagas:
            raise VagaIndisponivelError(
                f"Sem vagas na rota {rota.identificacao} em {data} "
                f"(vagas: {rota.vagas}) (RN-EDU-030)"
            )
        passagem = PassagemTransporte(
            rota_id=rota.id,
            matricula_id=matricula.id,
            data=data,
            created_by=dto.autor_id,
        )
        passagem.validar()
        return self._repo.save(passagem)


@dataclass
class CadastrarItemMerendaInput:
    """DTO de item de merenda."""

    nome: str
    tipo: str = "refeicao"
    estoque: float = 0.0
    estoque_minimo: float = 0.0
    autor_id: str = ""


class CadastrarItemMerendaUseCase:
    """Cadastra item do estoque de merenda."""

    def __init__(self, repo: ports.RepositorioItemMerenda) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarItemMerendaInput) -> ItemMerenda:
        """Executa o cadastro."""
        item = ItemMerenda(
            nome=dto.nome,
            tipo=dto.tipo,
            estoque=dto.estoque,
            estoque_minimo=dto.estoque_minimo,
            created_by=dto.autor_id,
        )
        item.validar()
        return self._repo.save(item)



class ReporEstoqueMerendaUseCase:
    """Registra entrada de estoque de merenda."""

    def __init__(self, repo: ports.RepositorioItemMerenda) -> None:
        self._repo = repo

    def execute(self, item_id: str, quantidade: float) -> ItemMerenda:
        """Executa a reposicao."""
        from ..domain.exceptions import ItemMerendaNaoEncontradoError

        item = self._repo.get_by_id(item_id)
        if item is None:
            raise ItemMerendaNaoEncontradoError("Item de merenda nao encontrado")
        item.repor(quantidade)
        return self._repo.save(item)


@dataclass
class DistribuirMerendaInput:
    """DTO de distribuicao de merenda."""

    matricula_id: str
    item_id: str
    quantidade: float
    refeicao: str = "almoco"
    data: date | None = None
    autor_id: str = ""


class DistribuirMerendaUseCase:
    """Distribui merenda com baixa atomica de estoque (RN-EDU-040)."""

    def __init__(
        self,
        distribuicoes: ports.RepositorioDistribuicaoMerenda,
        itens: ports.RepositorioItemMerenda,
        matriculas: ports.RepositorioMatricula,
    ) -> None:
        self._distribuicoes = distribuicoes
        self._itens = itens
        self._matriculas = matriculas

    def execute(self, dto: DistribuirMerendaInput) -> DistribuicaoMerenda:
        """Executa a distribuicao."""
        from ..domain.exceptions import (
            EstadoMatriculaInvalidoError,
            ItemMerendaNaoEncontradoError,
            MatriculaNaoEncontradaError,
        )

        matricula = self._matriculas.get_by_id(dto.matricula_id)
        if matricula is None:
            raise MatriculaNaoEncontradaError(
                "Matricula nao encontrada para distribuicao"
            )
        if not matricula.esta_ativa:
            raise EstadoMatriculaInvalidoError(
                "Distribuicao exige matricula ativa (RN-EDU-040)"
            )
        item = self._itens.get_by_id(dto.item_id)
        if item is None:
            raise ItemMerendaNaoEncontradoError("Item de merenda nao encontrado")
        item.distribuir(dto.quantidade)
        self._itens.save(item)
        distribuicao = DistribuicaoMerenda(
            matricula_id=matricula.id,
            item_id=item.id,
            quantidade=dto.quantidade,
            data=dto.data or date.today(),
            refeicao=dto.refeicao,
            created_by=dto.autor_id,
        )
        distribuicao.validar()
        return self._distribuicoes.save(distribuicao)


__all__ = [
    "CadastrarAlunoInput",
    "CadastrarAlunoUseCase",
    "RealizarMatriculaInput",
    "RealizarMatriculaUseCase",
    "TransferirMatriculaUseCase",
    "CancelarMatriculaUseCase",
    "ConcluirMatriculaUseCase",
    "RegistrarLancamentoDiarioInput",
    "RegistrarLancamentoDiarioUseCase",
    "CadastrarRotaTransporteInput",
    "CadastrarRotaTransporteUseCase",
    "InativarRotaTransporteUseCase",
    "AtivarRotaTransporteUseCase",
    "RegistrarPassagemInput",
    "RegistrarPassagemUseCase",
    "CadastrarItemMerendaInput",
    "CadastrarItemMerendaUseCase",
    "ReporEstoqueMerendaUseCase",
    "DistribuirMerendaInput",
    "DistribuirMerendaUseCase",
]

