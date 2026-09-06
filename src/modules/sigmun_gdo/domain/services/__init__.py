"""Serviços de domínio do módulo de Gestão Documental."""

from datetime import datetime, timedelta


class ServicoTemporalidade:
    """Serviço de domínio para cálculo de temporalidade e destinação."""

    @staticmethod
    def calcular_data_destinacao(
        data_criacao: datetime,
        prazo_meses: int,
        evento_fim: str
    ) -> datetime:
        """Calcula a data de destinação baseada na temporalidade."""
        if prazo_meses <= 0:
            raise ValueError("Prazo deve ser positivo")

        if evento_fim == "encerramento":
            # Usa data de encerramento se disponível
            return data_criacao + timedelta(days=prazo_meses * 30)
        else:
            # Usa data de criação
            return data_criacao + timedelta(days=prazo_meses * 30)

    @staticmethod
    def is_documento_vencido(
        data_calculo: datetime,
        data_base: datetime | None = None
    ) -> bool:
        """Verifica se um documento atingiu a data de destinação."""
        base = data_base or datetime.utcnow()
        return base >= data_calculo


class ServicoHashIntegridade:
    """Serviço de domínio para cálculo de hash de integridade."""

    @staticmethod
    def calcular_hash(conteudo: bytes) -> str:
        """Calcula SHA-256 do conteúdo."""
        import hashlib
        return hashlib.sha256(conteudo).hexdigest()

    @staticmethod
    def validar_hash(conteudo: bytes, hash_esperado: str) -> bool:
        """Valida se o conteúdo bate com o hash esperado."""
        hash_calculado = ServicoHashIntegridade.calcular_hash(conteudo)
        return hash_calculado == hash_esperado.lower()


__all__ = [
    "ServicoTemporalidade",
    "ServicoHashIntegridade",
]
