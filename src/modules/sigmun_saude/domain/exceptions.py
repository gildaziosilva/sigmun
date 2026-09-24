"""Exceções de domínio do DOM-SAU — Saúde Municipal."""


class DomSauDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-SAU."""

    pass


class RegraNegocioError(DomSauDomainError):
    """Erro de regra de negócio."""

    pass


class PacienteNaoEncontradoError(DomSauDomainError):
    """Paciente não encontrado."""

    pass


class PacienteJaExistenteError(DomSauDomainError):
    """Paciente já cadastrado (CNS duplicado)."""

    pass


class AtendimentoNaoEncontradoError(DomSauDomainError):
    """Atendimento do prontuário não encontrado."""

    pass


class AgendamentoNaoEncontradoError(DomSauDomainError):
    """Agendamento não encontrado."""

    pass


class EstadoAgendamentoInvalidoError(DomSauDomainError):
    """Transição de estado inválida para o agendamento."""

    pass


class RegulacaoNaoEncontradaError(DomSauDomainError):
    """Solicitação de regulação não encontrada."""

    pass


class EstadoRegulacaoInvalidoError(DomSauDomainError):
    """Transição de estado inválida para a regulação."""

    pass


class MedicamentoNaoEncontradoError(DomSauDomainError):
    """Medicamento da farmácia básica não encontrado."""

    pass


class EstoqueInsuficienteError(DomSauDomainError):
    """Estoque insuficiente para dispensação."""

    pass


DomainException = DomSauDomainError

__all__ = [
    "DomSauDomainError",
    "DomainException",
    "RegraNegocioError",
    "PacienteNaoEncontradoError",
    "PacienteJaExistenteError",
    "AtendimentoNaoEncontradoError",
    "AgendamentoNaoEncontradoError",
    "EstadoAgendamentoInvalidoError",
    "RegulacaoNaoEncontradaError",
    "EstadoRegulacaoInvalidoError",
    "MedicamentoNaoEncontradoError",
    "EstoqueInsuficienteError",
]
