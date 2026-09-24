"""Exceções de domínio do DOM-EDU — Educação Pública."""


class DomEduDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-EDU."""

    pass


class RegraNegocioError(DomEduDomainError):
    """Erro de regra de negócio."""

    pass


class AlunoNaoEncontradoError(DomEduDomainError):
    """Aluno não encontrado."""

    pass


class AlunoJaCadastradoError(DomEduDomainError):
    """Aluno já cadastrado (CPF duplicado)."""

    pass


class MatriculaNaoEncontradaError(DomEduDomainError):
    """Matrícula não encontrada."""

    pass


class MatriculaJaAtivaError(DomEduDomainError):
    """Aluno já possui matrícula ativa (RN-EDU-010)."""

    pass


class EstadoMatriculaInvalidoError(DomEduDomainError):
    """Transição de estado inválida para a matrícula."""

    pass


class RotaNaoEncontradaError(DomEduDomainError):
    """Rota de transporte escolar não encontrada."""

    pass


class EstadoRotaInvalidoError(DomEduDomainError):
    """Transição de estado inválida para a rota."""

    pass


class VagaIndisponivelError(DomEduDomainError):
    """Sem vaga disponível na rota (RN-EDU-030)."""

    pass


class ItemMerendaNaoEncontradoError(DomEduDomainError):
    """Item de merenda não encontrado."""

    pass


class EstoqueInsuficienteError(DomEduDomainError):
    """Estoque insuficiente para distribuição de merenda (RN-EDU-040)."""

    pass


DomainException = DomEduDomainError

__all__ = [
    "DomEduDomainError",
    "DomainException",
    "RegraNegocioError",
    "AlunoNaoEncontradoError",
    "AlunoJaCadastradoError",
    "MatriculaNaoEncontradaError",
    "MatriculaJaAtivaError",
    "EstadoMatriculaInvalidoError",
    "RotaNaoEncontradaError",
    "EstadoRotaInvalidoError",
    "VagaIndisponivelError",
    "ItemMerendaNaoEncontradoError",
    "EstoqueInsuficienteError",
]
