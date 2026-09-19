"""Use cases de Frequencia (DOM-PES)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time

from . import interfaces as ports
from ..domain.entities.frequencia import Frequencia, TipoFrequencia


@dataclass
class RegistrarFrequenciaInput:
    """DTO de apontamento de frequencia."""

    servidor_id: str
    data: date | None = None
    tipo: str = "presenca"
    hora_entrada: time | None = None
    hora_saida: time | None = None
    minutos_atraso: int = 0
    autor_id: str = ""


class RegistrarFrequenciaUseCase:
    """Registra frequencia diaria (RN-PES-050/051/052)."""

    def __init__(
        self, repo: ports.RepositorioFrequencia, servidores: ports.RepositorioServidor
    ) -> None:
        self._repo = repo
        self._servidores = servidores

    def execute(self, dto: RegistrarFrequenciaInput) -> Frequencia:
        """Executa o registro."""
        from ..domain.exceptions import RegraNegocioError

        if self._servidores.get_by_id(dto.servidor_id) is None:
            raise RegraNegocioError("Servidor nao encontrado")
        if dto.data is None:
            raise RegraNegocioError("Data da frequencia obrigatoria")
        existente = self._repo.get_por_servidor_data(dto.servidor_id, dto.data)
        if existente is not None:
            raise RegraNegocioError("Frequencia ja registrada (RN-PES-050)")
        frequencia = Frequencia(
            servidor_id=dto.servidor_id,
            data=dto.data,
            tipo=TipoFrequencia(dto.tipo),
            hora_entrada=dto.hora_entrada,
            hora_saida=dto.hora_saida,
            minutos_atraso=dto.minutos_atraso,
            created_by=dto.autor_id,
        )
        if frequencia.tipo == TipoFrequencia.FALTA:
            frequencia.marcar_desconto()
        return self._repo.save(frequencia)


@dataclass
class JustificarFaltaInput:
    """DTO de justificativa de falta."""

    frequencia_id: str
    justificativa: str


class JustificarFaltaUseCase:
    """Justifica falta registrada."""

    def __init__(self, repo: ports.RepositorioFrequencia) -> None:
        self._repo = repo

    def execute(self, dto: JustificarFaltaInput) -> Frequencia:
        """Executa a justificativa."""
        from ..domain.exceptions import FrequenciaNaoEncontradaError

        frequencia = self._repo.get_by_id(dto.frequencia_id)
        if frequencia is None:
            raise FrequenciaNaoEncontradaError("Frequencia nao encontrada")
        frequencia.justificar(dto.justificativa)
        return self._repo.save(frequencia)


__all__ = [
    "RegistrarFrequenciaInput",
    "RegistrarFrequenciaUseCase",
    "JustificarFaltaInput",
    "JustificarFaltaUseCase",
]
