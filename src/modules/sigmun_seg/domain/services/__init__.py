"""Serviços do domínio de Segurança da Informação."""

from src.modules.sigmun_seg.domain.entities import (
    ControleSeguranca,
    StatusControle,
    StatusIncidente,
    IncidenteSeguranca,
)


class ControleRiscoService:
    """Serviço de cálculo e classificação de risco de controles."""

    NIVEIS = ("baixo", "medio", "alto", "critico")

    def calcular_risco_residual(self, controle: ControleSeguranca) -> str:
        """Calcula o risco residual de um controle."""
        if controle.status == StatusControle.IMPLEMENTADO:
            return "baixo"
        elif controle.status == StatusControle.PARCIAL:
            return "medio"
        return controle.nivel_risco

    def prioritizar_controles(
        self, controles: list[ControleSeguranca]
    ) -> list[ControleSeguranca]:
        """Ordena controles por risco decresente."""
        ordem = {"critico": 4, "alto": 3, "medio": 2, "baixo": 1}
        return sorted(
            controles,
            key=lambda c: ordem.get(c.nivel_risco, 0),
            reverse=True,
        )


class IncidenteService:
    """Serviço auxiliar para análise de incidentes."""

    def tempo_resolucao_horas(self, incidente: IncidenteSeguranca) -> float | None:
        """Calcula tempo de resolução em horas."""
        if incidente.data_resolucao and incidente.data_ocorrencia:
            delta = incidente.data_resolucao - incidente.data_ocorrencia
            return round(delta.total_seconds() / 3600, 2)
        return None

    def incidente_critico_aberto(
        self, incidentes: list[IncidenteSeguranca]
    ) -> bool:
        """Verifica se existe incidente crítico aberto."""
        return any(
            i.severidade.value == "critica" and i.status == StatusIncidente.ABERTO
            for i in incidentes
        )


__all__ = ["ControleRiscoService", "IncidenteService"]
