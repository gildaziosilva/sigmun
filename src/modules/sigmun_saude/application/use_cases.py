"""Use cases do DOM-SAU - Saude Municipal."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from . import interfaces as ports
from ..domain.entities.atendimento import (
    Agendamento,
    Atendimento,
    TipoAtendimento,
)
from ..domain.entities.farmacia_regulacao import (
    Dispensacao,
    Medicamento,
    PrioridadeRegulacao,
    Regulacao,
)
from ..domain.entities.paciente import Paciente, Sexo


@dataclass
class CadastrarPacienteInput:
    """DTO de cadastro de paciente."""

    nome: str
    cns: str
    cpf: str = ""
    data_nascimento: str = ""
    sexo: str = "ignorado"
    nome_mae: str = ""
    telefone: str = ""
    endereco: str = ""
    ubs_referencia: str = ""
    autor_id: str = ""


class CadastrarPacienteUseCase:
    """Cadastra um paciente (RN-SAU-001)."""

    def __init__(self, repo: ports.RepositorioPaciente) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarPacienteInput) -> Paciente:
        """Executa o cadastro."""
        from ..domain.exceptions import PacienteJaExistenteError, RegraNegocioError

        if not dto.nome or not dto.cns:
            raise RegraNegocioError("Nome e CNS sao obrigatorios (RN-SAU-001)")
        if self._repo.get_by_cns(dto.cns) is not None:
            raise PacienteJaExistenteError("CNS ja cadastrado (RN-SAU-001)")
        paciente = Paciente(
            nome=dto.nome, cns=dto.cns, cpf=dto.cpf,
            data_nascimento=dto.data_nascimento, sexo=Sexo(dto.sexo),
            nome_mae=dto.nome_mae, telefone=dto.telefone,
            endereco=dto.endereco, ubs_referencia=dto.ubs_referencia,
            created_by=dto.autor_id,
        )
        paciente.validar()
        return self._repo.save(paciente)


@dataclass
class RegistrarAtendimentoInput:
    """DTO de atendimento do prontuario."""

    paciente_id: str
    profissional: str
    estabelecimento: str
    tipo: str = "consulta"
    data: date | None = None
    queixa: str = ""
    conduta: str = ""
    cid10: str = ""
    autor_id: str = ""


class RegistrarAtendimentoUseCase:
    """Registra atendimento no prontuario (RN-SAU-010)."""

    def __init__(self, repo: ports.RepositorioAtendimento, pacientes: ports.RepositorioPaciente) -> None:
        self._repo = repo
        self._pacientes = pacientes

    def execute(self, dto: RegistrarAtendimentoInput) -> Atendimento:
        """Executa o registro."""
        from ..domain.exceptions import PacienteNaoEncontradoError

        if self._pacientes.get_by_id(dto.paciente_id) is None:
            raise PacienteNaoEncontradoError("Paciente nao encontrado para atendimento")
        atendimento = Atendimento(
            paciente_id=dto.paciente_id, data=dto.data or date.today(),
            tipo=TipoAtendimento(dto.tipo), profissional=dto.profissional,
            estabelecimento=dto.estabelecimento, queixa=dto.queixa,
            conduta=dto.conduta, cid10=dto.cid10, created_by=dto.autor_id,
        )
        atendimento.validar()
        return self._repo.save(atendimento)


@dataclass
class AgendarConsultaInput:
    """DTO de agendamento SUS."""

    paciente_id: str
    especialidade: str
    data: date | None = None
    hora: str = ""
    estabelecimento: str = ""
    autor_id: str = ""


class AgendarConsultaUseCase:
    """Agenda consulta/exame SUS (RN-SAU-020)."""

    def __init__(self, repo: ports.RepositorioAgendamento, pacientes: ports.RepositorioPaciente) -> None:
        self._repo = repo
        self._pacientes = pacientes

    def execute(self, dto: AgendarConsultaInput) -> Agendamento:
        """Executa o agendamento."""
        from ..domain.exceptions import PacienteNaoEncontradoError

        if self._pacientes.get_by_id(dto.paciente_id) is None:
            raise PacienteNaoEncontradoError("Paciente nao encontrado para agendamento")
        agendamento = Agendamento(
            paciente_id=dto.paciente_id, especialidade=dto.especialidade,
            data=dto.data or date.today(), hora=dto.hora,
            estabelecimento=dto.estabelecimento, created_by=dto.autor_id,
        )
        agendamento.validar()
        return self._repo.save(agendamento)


class ConfirmarAgendamentoUseCase:
    """Confirma agendamento."""

    def __init__(self, repo: ports.RepositorioAgendamento) -> None:
        self._repo = repo

    def execute(self, agendamento_id: str) -> Agendamento:
        """Executa a confirmacao."""
        from ..domain.exceptions import AgendamentoNaoEncontradoError

        agendamento = self._repo.get_by_id(agendamento_id)
        if agendamento is None:
            raise AgendamentoNaoEncontradoError("Agendamento nao encontrado")
        agendamento.confirmar()
        return self._repo.save(agendamento)


class CancelarAgendamentoUseCase:
    """Cancela agendamento."""

    def __init__(self, repo: ports.RepositorioAgendamento) -> None:
        self._repo = repo

    def execute(self, agendamento_id: str, motivo: str = "") -> Agendamento:
        """Executa o cancelamento."""
        from ..domain.exceptions import AgendamentoNaoEncontradoError

        agendamento = self._repo.get_by_id(agendamento_id)
        if agendamento is None:
            raise AgendamentoNaoEncontradoError("Agendamento nao encontrado")
        agendamento.cancelar(motivo)
        return self._repo.save(agendamento)


class RealizarAgendamentoUseCase:
    """Marca comparecimento."""

    def __init__(self, repo: ports.RepositorioAgendamento) -> None:
        self._repo = repo

    def execute(self, agendamento_id: str) -> Agendamento:
        """Executa o registro de presenca."""
        from ..domain.exceptions import AgendamentoNaoEncontradoError

        agendamento = self._repo.get_by_id(agendamento_id)
        if agendamento is None:
            raise AgendamentoNaoEncontradoError("Agendamento nao encontrado")
        agendamento.registrar_realizado()
        return self._repo.save(agendamento)


@dataclass
class SolicitarRegulacaoInput:
    """DTO de solicitacao de regulacao."""

    paciente_id: str
    procedimento: str
    prioridade: str = "rotina"
    solicitante: str = ""
    autor_id: str = ""


class SolicitarRegulacaoUseCase:
    """Abre solicitacao na central (RN-SAU-030)."""

    def __init__(self, repo: ports.RepositorioRegulacao, pacientes: ports.RepositorioPaciente) -> None:
        self._repo = repo
        self._pacientes = pacientes

    def execute(self, dto: SolicitarRegulacaoInput) -> Regulacao:
        """Executa a solicitacao."""
        from ..domain.exceptions import PacienteNaoEncontradoError

        if self._pacientes.get_by_id(dto.paciente_id) is None:
            raise PacienteNaoEncontradoError("Paciente nao encontrado para regulacao")
        regulacao = Regulacao(
            paciente_id=dto.paciente_id, procedimento=dto.procedimento,
            prioridade=PrioridadeRegulacao(dto.prioridade), solicitante=dto.solicitante,
            data_solicitacao=date.today(), created_by=dto.autor_id,
        )
        regulacao.validar()
        return self._repo.save(regulacao)


class AutorizarRegulacaoUseCase:
    """Autoriza solicitacao."""

    def __init__(self, repo: ports.RepositorioRegulacao) -> None:
        self._repo = repo

    def execute(self, regulacao_id: str) -> Regulacao:
        """Executa a autorizacao."""
        from ..domain.exceptions import RegulacaoNaoEncontradaError

        regulacao = self._repo.get_by_id(regulacao_id)
        if regulacao is None:
            raise RegulacaoNaoEncontradaError("Regulacao nao encontrada")
        regulacao.autorizar()
        return self._repo.save(regulacao)


class NegarRegulacaoUseCase:
    """Nega solicitacao."""

    def __init__(self, repo: ports.RepositorioRegulacao) -> None:
        self._repo = repo

    def execute(self, regulacao_id: str, justificativa: str = "") -> Regulacao:
        """Executa a negativa."""
        from ..domain.exceptions import RegulacaoNaoEncontradaError

        regulacao = self._repo.get_by_id(regulacao_id)
        if regulacao is None:
            raise RegulacaoNaoEncontradaError("Regulacao nao encontrada")
        regulacao.negar(justificativa)
        return self._repo.save(regulacao)


@dataclass
class CadastrarMedicamentoInput:
    """DTO de medicamento da farmacia basica."""

    nome: str
    apresentacao: str = ""
    estoque: float = 0.0
    estoque_minimo: float = 0.0
    autor_id: str = ""


class CadastrarMedicamentoUseCase:
    """Cadastra medicamento."""

    def __init__(self, repo: ports.RepositorioMedicamento) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarMedicamentoInput) -> Medicamento:
        """Executa o cadastro."""
        medicamento = Medicamento(
            nome=dto.nome, apresentacao=dto.apresentacao,
            estoque=dto.estoque, estoque_minimo=dto.estoque_minimo,
            created_by=dto.autor_id,
        )
        medicamento.validar()
        return self._repo.save(medicamento)


class ReporEstoqueUseCase:
    """Registra entrada de estoque."""

    def __init__(self, repo: ports.RepositorioMedicamento) -> None:
        self._repo = repo

    def execute(self, medicamento_id: str, quantidade: float) -> Medicamento:
        """Executa a reposicao."""
        from ..domain.exceptions import MedicamentoNaoEncontradoError

        medicamento = self._repo.get_by_id(medicamento_id)
        if medicamento is None:
            raise MedicamentoNaoEncontradoError("Medicamento nao encontrado")
        medicamento.repor(quantidade)
        return self._repo.save(medicamento)


@dataclass
class DispensarMedicamentoInput:
    """DTO de dispensacao."""

    paciente_id: str
    medicamento_id: str
    quantidade: float
    receita: str = ""
    autor_id: str = ""


class DispensarMedicamentoUseCase:
    """Dispensa medicamento com baixa atomica (RN-SAU-040)."""

    def __init__(self, dispensacoes: ports.RepositorioDispensacao, medicamentos: ports.RepositorioMedicamento, pacientes: ports.RepositorioPaciente) -> None:
        self._dispensacoes = dispensacoes
        self._medicamentos = medicamentos
        self._pacientes = pacientes

    def execute(self, dto: DispensarMedicamentoInput) -> Dispensacao:
        """Executa a dispensacao."""
        from ..domain.exceptions import MedicamentoNaoEncontradoError, PacienteNaoEncontradoError

        if self._pacientes.get_by_id(dto.paciente_id) is None:
            raise PacienteNaoEncontradoError("Paciente nao encontrado para dispensacao")
        medicamento = self._medicamentos.get_by_id(dto.medicamento_id)
        if medicamento is None:
            raise MedicamentoNaoEncontradoError("Medicamento nao encontrado")
        medicamento.dispensar(dto.quantidade)
        self._medicamentos.save(medicamento)
        dispensacao = Dispensacao(
            paciente_id=dto.paciente_id, medicamento_id=dto.medicamento_id,
            quantidade=dto.quantidade, data=date.today(),
            receita=dto.receita, created_by=dto.autor_id,
        )
        dispensacao.validar()
        return self._dispensacoes.save(dispensacao)


__all__ = [
    "CadastrarPacienteInput",
    "CadastrarPacienteUseCase",
    "RegistrarAtendimentoInput",
    "RegistrarAtendimentoUseCase",
    "AgendarConsultaInput",
    "AgendarConsultaUseCase",
    "ConfirmarAgendamentoUseCase",
    "CancelarAgendamentoUseCase",
    "RealizarAgendamentoUseCase",
    "SolicitarRegulacaoInput",
    "SolicitarRegulacaoUseCase",
    "AutorizarRegulacaoUseCase",
    "NegarRegulacaoUseCase",
    "CadastrarMedicamentoInput",
    "CadastrarMedicamentoUseCase",
    "ReporEstoqueUseCase",
    "DispensarMedicamentoInput",
    "DispensarMedicamentoUseCase",
]
