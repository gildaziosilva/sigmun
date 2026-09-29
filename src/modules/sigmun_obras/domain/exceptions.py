"""Exceções de domínio do DOM-OBR — Obras e Infraestrutura."""


class DomObrDomainError(Exception):
    """Base das exceções de negócio do domínio DOM-OBR."""

    pass


class RegraNegocioError(DomObrDomainError):
    """Erro de regra de negócio."""

    pass


class ObraNaoEncontradaError(DomObrDomainError):
    """Obra não encontrada no cadastro de obras públicas."""

    pass


class ObraJaExistenteError(DomObrDomainError):
    """Obra já cadastrada (número/identificador duplicado)."""

    pass


class ObraComDependenciasError(DomObrDomainError):
    """Obra possui medições ou despesas vinculadas e não pode ser excluída."""

    pass


class MedicaoNaoEncontradaError(DomObrDomainError):
    """Medição de obra não encontrada."""

    pass


class MedicaoJaRegistradaError(DomObrDomainError):
    """Já existe medição com o mesmo número na obra."""

    pass


class EtapaNaoEncontradaError(DomObrDomainError):
    """Etapa de obra não encontrada."""

    pass


class DespesaNaoEncontradaError(DomObrDomainError):
    """Despesa de obra não encontrada."""

    pass


class VistoriaNaoEncontradaError(DomObrDomainError):
    """Vistoria de obra não encontrada."""

    pass


DomainException = DomObrDomainError

__all__ = [
    "DomObrDomainError",
    "DomainException",
    "RegraNegocioError",
    "ObraNaoEncontradaError",
    "ObraJaExistenteError",
    "ObraComDependenciasError",
    "MedicaoNaoEncontradaError",
    "MedicaoJaRegistradaError",
    "EtapaNaoEncontradaError",
    "DespesaNaoEncontradaError",
    "VistoriaNaoEncontradaError",
]
