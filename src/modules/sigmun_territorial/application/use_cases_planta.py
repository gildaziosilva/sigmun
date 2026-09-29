"""Use cases do DOM-TEL — Gestão Territorial (parte 3: planta genérica de valores)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..domain.entities import PlantaGenericaValores, TipoOcupacaoImovel
from . import interfaces as ports


def _ocupacao(valor: str) -> TipoOcupacaoImovel:
    """Converte a ocupação textual, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoOcupacaoImovel(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Ocupação inválida: {valor}") from exc


@dataclass
class CadastrarPlantaValoresInput:
    """DTO de cadastro da planta genérica de valores (RN-TEL-003)."""

    ano: int
    bairro_id: str
    ocupacao: str = "residencial"
    valor_terreno_m2: float = 0.0
    valor_construcao_m2: float = 0.0
    aliquota_percent: float = 0.0
    legislacao: str = ""
    ativar: bool = False
    autor_id: str = ""


class CadastrarPlantaValoresUseCase:
    """Cadastra uma planta genérica de valores (RN-TEL-003)."""

    def __init__(
        self, repo: ports.RepositorioPlantaValores, bairros: ports.RepositorioBairro
    ) -> None:
        self._repo = repo
        self._bairros = bairros

    def execute(self, dto: CadastrarPlantaValoresInput) -> PlantaGenericaValores:
        """Executa o cadastro, opcionalmente já ativando a planta."""
        from ..domain.exceptions import (
            BairroNaoEncontradoError,
            PlantaValoresJaExistenteError,
            RegraNegocioError,
        )

        if not dto.bairro_id:
            raise RegraNegocioError("Planta genérica de valores exige bairro (RN-TEL-003)")
        if self._bairros.get_by_id(dto.bairro_id) is None:
            raise BairroNaoEncontradoError("Bairro não encontrado para a planta de valores")

        ocupacao = _ocupacao(dto.ocupacao)
        if dto.ativar:
            vigente = self._repo.get_vigente(dto.ano, dto.bairro_id, ocupacao.value)
            if vigente is not None:
                raise PlantaValoresJaExistenteError(
                    "Já existe planta vigente para o ano, bairro e ocupação informados "
                    "(RN-TEL-003)"
                )

        planta = PlantaGenericaValores(
            ano=dto.ano,
            bairro_id=dto.bairro_id,
            ocupacao=ocupacao,
            valor_terreno_m2=dto.valor_terreno_m2,
            valor_construcao_m2=dto.valor_construcao_m2,
            aliquota_percent=dto.aliquota_percent,
            legislacao=dto.legislacao,
            created_by=dto.autor_id,
        )
        planta.validar()
        if dto.ativar:
            planta.ativar()
        return self._repo.save(planta)


class AtivarPlantaValoresUseCase:
    """Ativa uma planta genérica de valores em rascunho (RN-TEL-003/004)."""

    def __init__(self, repo: ports.RepositorioPlantaValores) -> None:
        self._repo = repo

    def execute(self, planta_id: str) -> PlantaGenericaValores:
        """Executa a ativação."""
        from ..domain.exceptions import (
            PlantaValoresJaExistenteError,
            PlantaValoresNaoEncontradaError,
        )

        planta = self._repo.get_by_id(planta_id)
        if planta is None:
            raise PlantaValoresNaoEncontradaError("Planta genérica de valores não encontrada")

        vigente = self._repo.get_vigente(planta.ano, planta.bairro_id, planta.ocupacao.value)
        if vigente is not None and vigente.id != planta.id:
            raise PlantaValoresJaExistenteError(
                "Já existe planta vigente para o mesmo ano, bairro e ocupação (RN-TEL-003)"
            )
        planta.ativar()
        return self._repo.save(planta)


class RevogarPlantaValoresUseCase:
    """Revoga uma planta genérica de valores vigente (RN-TEL-004)."""

    def __init__(self, repo: ports.RepositorioPlantaValores) -> None:
        self._repo = repo

    def execute(self, planta_id: str, motivo: str) -> PlantaGenericaValores:
        """Executa a revogação."""
        from ..domain.exceptions import PlantaValoresNaoEncontradaError

        planta = self._repo.get_by_id(planta_id)
        if planta is None:
            raise PlantaValoresNaoEncontradaError("Planta genérica de valores não encontrada")
        planta.revogar(motivo)
        return self._repo.save(planta)


@dataclass
class AtualizarPlantaValoresInput:
    """DTO de atualização da planta genérica de valores (campos opcionais)."""

    planta_id: str
    ano: int | None = None
    valor_terreno_m2: float | None = None
    valor_construcao_m2: float | None = None
    aliquota_percent: float | None = None
    legislacao: str | None = None
    autor_id: str = ""


class AtualizarPlantaValoresUseCase:
    """Atualiza os valores de uma planta genérica de valores.

    RN-TEL-004: somente plantas em rascunho podem ser editadas; planta vigente
    ou revogada é preservada como evidência histórica.
    """

    def __init__(self, repo: ports.RepositorioPlantaValores) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarPlantaValoresInput) -> PlantaGenericaValores:
        """Executa a atualização."""
        from ..domain.exceptions import PlantaValoresNaoEncontradaError, RegraNegocioError

        planta = self._repo.get_by_id(dto.planta_id)
        if planta is None:
            raise PlantaValoresNaoEncontradaError("Planta genérica de valores não encontrada")
        if planta.situacao.value != "rascunho":
            raise RegraNegocioError(
                "Somente planta em rascunho pode ser editada; revogue a vigente para "
                "substituir (RN-TEL-004)"
            )

        if dto.ano is not None:
            planta.ano = dto.ano
        if dto.valor_terreno_m2 is not None:
            if dto.valor_terreno_m2 < 0:
                raise RegraNegocioError("Valor unitário do terreno não pode ser negativo")
            planta.valor_terreno_m2 = dto.valor_terreno_m2
        if dto.valor_construcao_m2 is not None:
            if dto.valor_construcao_m2 < 0:
                raise RegraNegocioError("Valor unitário da construção não pode ser negativo")
            planta.valor_construcao_m2 = dto.valor_construcao_m2
        if dto.aliquota_percent is not None:
            if not 0 <= dto.aliquota_percent <= 100:
                raise RegraNegocioError("Alíquota deve estar entre 0 e 100")
            planta.aliquota_percent = dto.aliquota_percent
        if dto.legislacao is not None:
            planta.legislacao = dto.legislacao

        planta.validar()
        planta.updated_at = datetime.utcnow()
        return self._repo.save(planta)

