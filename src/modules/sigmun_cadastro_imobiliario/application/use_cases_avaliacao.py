"""Use cases do DOM-IMO — avaliação, características e geometria do lote."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from ..domain.entities import (
    AvaliacaoImovel,
    CaracteristicaImovel,
    GeometriaImovel,
    TipoObra,
)
from . import interfaces as ports

# Ocupação territorial usada na planta genérica de valores conforme a natureza
# do imóvel (contrato de integração com o DOM-TEL).
_OCUPACAO_POR_TIPO_IMOVEL = {
    "lote": "terreno",
    "casa": "residencial",
    "apartamento": "residencial",
    "loja": "comercial",
    "galpao": "industrial",
    "terreno": "terreno",
    "outro": "misto",
}

# Ocupação declarada pela característica construtiva tem precedência.
_OCUPACAO_POR_OBRA = {
    "residencial": "residencial",
    "comercial": "comercial",
    "industrial": "industrial",
    "institucional": "institucional",
    "mista": "misto",
    "nao_aplicavel": "terreno",
}


def ocupacao_do_imovel(
    tipo_imovel: str, obra: str | None = None
) -> str:
    """Resolve a ocupação territorial usada para localizar a planta de valores."""
    if obra and obra in _OCUPACAO_POR_OBRA and obra != "nao_aplicavel":
        return _OCUPACAO_POR_OBRA[obra]
    return _OCUPACAO_POR_TIPO_IMOVEL.get(tipo_imovel, "misto")


@dataclass
class AvaliarImovelInput:
    """DTO de avaliação do valor venal (RN-IMO-005).

    Os valores unitários são resolvidos pelo consumidor a partir do contrato de
    integração com o DOM-TEL (`GET /api/v1/tel/plantas-valores/vigente`).
    """

    imovel_id: str
    ano: int
    valor_terreno_m2_unitario: float
    valor_construcao_m2_unitario: float
    aliquota_percent: float = 0.0
    data_avaliacao: date | None = None
    concluir: bool = True
    autor_id: str = ""


class AvaliarImovelUseCase:
    """Avalia o imóvel aplicando os valores unitários vigentes (RN-IMO-005)."""

    def __init__(
        self,
        repo: ports.RepositorioAvaliacao,
        imoveis: ports.RepositorioImovel,
    ) -> None:
        self._repo = repo
        self._imoveis = imoveis

    def execute(self, dto: AvaliarImovelInput) -> AvaliacaoImovel:
        """Executa a avaliação, opcionalmente já concluída."""
        from ..domain.exceptions import (
            AvaliacaoNaoEncontradaError,
            ImovelNaoEncontradoError,
            RegraNegocioError,
        )

        imovel = self._imoveis.get_by_id(dto.imovel_id)
        if imovel is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para avaliação")

        existente = self._repo.get_by_imovel_e_ano(dto.imovel_id, dto.ano)
        if existente is not None and existente.situacao.value == "concluida":
            raise AvaliacaoNaoEncontradaError(
                f"Já existe avaliação concluída para o imóvel no exercício {dto.ano} "
                "(RN-IMO-005)"
            )

        avaliacao = AvaliacaoImovel(
            id=existente.id if existente is not None else AvaliacaoImovel().id,
            imovel_id=imovel.id,
            ano=dto.ano,
            valor_terreno_m2_unitario=dto.valor_terreno_m2_unitario,
            valor_construcao_m2_unitario=dto.valor_construcao_m2_unitario,
            aliquota_percent=dto.aliquota_percent,
            area_terreno_m2=imovel.area_terreno_m2,
            area_construida_m2=imovel.area_construida_m2,
            data_avaliacao=dto.data_avaliacao or date.today(),
            created_by=dto.autor_id,
        )
        if imovel.area_terreno_m2 <= 0 and imovel.area_construida_m2 <= 0:
            raise RegraNegocioError(
                "Imóvel sem áreas de terreno ou construção não pode ser avaliado (RN-IMO-005)"
            )
        avaliacao.validar()
        if dto.concluir:
            avaliacao.concluir()
        return self._repo.save(avaliacao)


class ConcluirAvaliacaoUseCase:
    """Conclui uma avaliação em rascunho (RN-IMO-005)."""

    def __init__(self, repo: ports.RepositorioAvaliacao) -> None:
        self._repo = repo

    def execute(self, avaliacao_id: str) -> AvaliacaoImovel:
        """Executa a conclusão."""
        from ..domain.exceptions import AvaliacaoNaoEncontradaError

        avaliacao = self._repo.get_by_id(avaliacao_id)
        if avaliacao is None:
            raise AvaliacaoNaoEncontradaError("Avaliação não encontrada")
        avaliacao.concluir()
        return self._repo.save(avaliacao)


class CancelarAvaliacaoUseCase:
    """Cancela uma avaliação ainda não concluída (RN-IMO-005)."""

    def __init__(self, repo: ports.RepositorioAvaliacao) -> None:
        self._repo = repo

    def execute(self, avaliacao_id: str, motivo: str) -> AvaliacaoImovel:
        """Executa o cancelamento."""
        from ..domain.exceptions import AvaliacaoNaoEncontradaError

        avaliacao = self._repo.get_by_id(avaliacao_id)
        if avaliacao is None:
            raise AvaliacaoNaoEncontradaError("Avaliação não encontrada")
        avaliacao.cancelar(motivo)
        return self._repo.save(avaliacao)


@dataclass
class RegistrarCaracteristicaInput:
    """DTO da característica construtiva do imóvel."""

    imovel_id: str
    obra: str = "residencial"
    numero_pavimentos: int = 1
    ano_renovacao: int | None = None
    observacao: str = ""
    autor_id: str = ""


class RegistrarCaracteristicaUseCase:
    """Registra a característica construtiva vigente do imóvel."""

    def __init__(
        self,
        repo: ports.RepositorioCaracteristica,
        imoveis: ports.RepositorioImovel,
    ) -> None:
        self._repo = repo
        self._imoveis = imoveis

    def execute(self, dto: RegistrarCaracteristicaInput) -> CaracteristicaImovel:
        """Executa o registro, substituindo a característica anterior."""
        from ..domain.exceptions import ImovelNaoEncontradoError, RegraNegocioError

        if self._imoveis.get_by_id(dto.imovel_id) is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para característica")
        try:
            obra = TipoObra(dto.obra)
        except ValueError as exc:
            raise RegraNegocioError(f"Natureza da obra inválida: {dto.obra}") from exc

        anterior = self._repo.get_by_imovel(dto.imovel_id)
        caracteristica = CaracteristicaImovel(
            id=anterior.id if anterior is not None else CaracteristicaImovel().id,
            imovel_id=dto.imovel_id,
            obra=obra,
            numero_pavimentos=dto.numero_pavimentos,
            ano_renovacao=dto.ano_renovacao,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        caracteristica.validar()
        return self._repo.save(caracteristica)


@dataclass
class RegistrarGeometriaInput:
    """DTO da geometria georreferenciada do lote (RN-IMO-007)."""

    imovel_id: str
    geometria: str = "ponto"
    latitude: float = 0.0
    longitude: float = 0.0
    vertices: list[dict[str, float]] | None = None
    datum: str = "sirgas2000"
    precisao_m: float = 0.0
    data_levantamento: date | None = None
    autor_id: str = ""


class RegistrarGeometriaUseCase:
    """Registra a geometria georreferenciada do lote (RN-IMO-007)."""

    def __init__(
        self, repo: ports.RepositorioGeometria, imoveis: ports.RepositorioImovel
    ) -> None:
        self._repo = repo
        self._imoveis = imoveis

    def execute(self, dto: RegistrarGeometriaInput) -> GeometriaImovel:
        """Executa o registro da geometria, substituindo a anterior.

        O índice único `uq_imo_geometria_lote` admite uma geometria vigente por
        lote: a regeorreferência reutiliza o identificador do registro anterior.
        """
        from ..domain.exceptions import ImovelNaoEncontradoError

        if self._imoveis.get_by_id(dto.imovel_id) is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para geometria")

        vertices = list(dto.vertices) if dto.vertices else []
        primeiro = vertices[0] if dto.geometria == "ponto" and vertices else None
        anterior = self._repo.get_by_imovel(dto.imovel_id)
        geometria = GeometriaImovel(
            id=anterior.id if anterior is not None else GeometriaImovel().id,
            imovel_id=dto.imovel_id,
            geometria=dto.geometria,
            latitude=float(primeiro["latitude"]) if primeiro else dto.latitude,
            longitude=float(primeiro["longitude"]) if primeiro else dto.longitude,
            vertices=vertices,
            datum=dto.datum,
            precisao_m=dto.precisao_m,
            data_levantamento=dto.data_levantamento or date.today(),
            created_by=dto.autor_id,
        )
        geometria.validar()
        return self._repo.save(geometria)

