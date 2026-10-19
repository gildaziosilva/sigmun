"""Exceções de domínio de Atendimento ao Cidadão (DOM-ATE)."""


class AteDominioError(Exception):
    """Exceção base do domínio ATE."""

    def __init__(self, message: str, codigo: str = "ATE_ERROR"):
        self.message = message
        self.codigo = codigo
        super().__init__(message)


class TriagemInvalidaError(AteDominioError):
    """Erro na triagem de atendimento."""

    def __init__(self, message: str = "Triagem inválida"):
        super().__init__(message, "TRIAGEM_INVALIDA")


class FilaInvalidaError(AteDominioError):
    """Erro na fila de atendimento."""

    def __init__(self, message: str = "Fila inválida"):
        super().__init__(message, "FILA_INVALIDA")


class FilaFechadaError(AteDominioError):
    """Tentativa de operar em fila fechada."""

    def __init__(self, message: str = "Fila fechada"):
        super().__init__(message, "FILA_FECHADA")


class SenhaInvalidaError(AteDominioError):
    """Erro na senha de atendimento."""

    def __init__(self, message: str = "Senha inválida"):
        super().__init__(message, "SENHA_INVALIDA")


class SenhaJaChamadaError(AteDominioError):
    """Senha já foi chamada."""

    def __init__(self, message: str = "Senha já foi chamada"):
        super().__init__(message, "SENHA_JA_CHAMADA")


class SenhaNaoChamadaError(AteDominioError):
    """Senha não foi chamada para atendimento."""

    def __init__(self, message: str = "Senha não foi chamada"):
        super().__init__(message, "SENHA_NAO_CHAMADA")


class SenhaAtendidaError(AteDominioError):
    """Senha já foi atendida."""

    def __init__(self, message: str = "Senha já foi atendida"):
        super().__init__(message, "SENHA_ATENDIDA")


class SenhaCanceladaError(AteDominioError):
    """Senha cancelada."""

    def __init__(self, message: str = "Senha cancelada"):
        super().__init__(message, "SENHA_CANCELADA")


class MaximoRechamadasError(AteDominioError):
    """Excedeu máximo de rechamadas."""

    def __init__(self, message: str = "Máximo de rechamadas atingido"):
        super().__init__(message, "MAXIMO_RECHAMADAS")


class AtendimentoInvalidoError(AteDominioError):
    """Erro no atendimento."""

    def __init__(self, message: str = "Atendimento inválido"):
        super().__init__(message, "ATENDIMENTO_INVALIDO")


class AtendimentoNaoIniciadoError(AteDominioError):
    """Atendimento não foi iniciado."""

    def __init__(self, message: str = "Atendimento não iniciado"):
        super().__init__(message, "ATENDIMENTO_NAO_INICIADO")


class AtendimentoJaConcluidoError(AteDominioError):
    """Atendimento já concluído."""

    def __init__(self, message: str = "Atendimento já concluído"):
        super().__init__(message, "ATENDIMENTO_JA_CONCLUIDO")


class AvaliacaoInvalidaError(AteDominioError):
    """Avaliação inválida."""

    def __init__(self, message: str = "Avaliação inválida"):
        super().__init__(message, "AVALIACAO_INVALIDA")


class NotaForaIntervaloError(AteDominioError):
    """Nota fora do intervalo permitido (1-5)."""

    def __init__(self, message: str = "Nota deve estar entre 1 e 5"):
        super().__init__(message, "NOTA_FORA_INTERVALO")


class AvaliacaoJaRegistradaError(AteDominioError):
    """Avaliação já registrada para este atendimento."""

    def __init__(self, message: str = "Avaliação já registrada"):
        super().__init__(message, "AVALIACAO_JA_REGISTRADA")


class EncaminhamentoInvalidoError(AteDominioError):
    """Encaminhamento inválido."""

    def __init__(self, message: str = "Encaminhamento inválido"):
        super().__init__(message, "ENCAMINHAMENTO_INVALIDO")


class EncaminhamentoJaConcluidoError(AteDominioError):
    """Encaminhamento já concluído."""

    def __init__(self, message: str = "Encaminhamento já concluído"):
        super().__init__(message, "ENCAMINHAMENTO_JA_CONCLUIDO")


class GuicheInvalidoError(AteDominioError):
    """Guichê inválido."""

    def __init__(self, message: str = "Guichê inválido"):
        super().__init__(message, "GUICHE_INVALIDO")


class GuicheInativoError(AteDominioError):
    """Guichê inativo."""

    def __init__(self, message: str = "Guichê inativo"):
        super().__init__(message, "GUICHE_INATIVO")


class UnidadeInvalidaError(AteDominioError):
    """Unidade de atendimento inválida."""

    def __init__(self, message: str = "Unidade inválida"):
        super().__init__(message, "UNIDADE_INVALIDA")


class ServicoInvalidoError(AteDominioError):
    """Serviço de atendimento inválido."""

    def __init__(self, message: str = "Serviço inválido"):
        super().__init__(message, "SERVICO_INVALIDO")


class CanalInvalidoError(AteDominioError):
    """Canal de atendimento inválido."""

    def __init__(self, message: str = "Canal inválido"):
        super().__init__(message, "CANAL_INVALIDO")


class OperadorInvalidoError(AteDominioError):
    """Operador inválido."""

    def __init__(self, message: str = "Operador inválido"):
        super().__init__(message, "OPERADOR_INVALIDO")


__all__ = [
    "AteDominioError",
    "TriagemInvalidaError",
    "FilaInvalidaError",
    "FilaFechadaError",
    "SenhaInvalidaError",
    "SenhaJaChamadaError",
    "SenhaNaoChamadaError",
    "SenhaAtendidaError",
    "SenhaCanceladaError",
    "MaximoRechamadasError",
    "AtendimentoInvalidoError",
    "AtendimentoNaoIniciadoError",
    "AtendimentoJaConcluidoError",
    "AvaliacaoInvalidaError",
    "NotaForaIntervaloError",
    "AvaliacaoJaRegistradaError",
    "EncaminhamentoInvalidoError",
    "EncaminhamentoJaConcluidoError",
    "GuicheInvalidoError",
    "GuicheInativoError",
    "UnidadeInvalidaError",
    "ServicoInvalidoError",
    "CanalInvalidoError",
    "OperadorInvalidoError",
]
