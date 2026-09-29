"""Use cases do DOM-IMO — Cadastro Imobiliário (imóveis)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..domain.entities import (
    Imovel,
    ProprietarioImovel,
    SituacaoImovel,
    TipoImovel,
    TipoPropriedade,
    TipoVinculo,
)
from . import interfaces as ports


def _tipo_vinculo(valor: str) -> TipoVinculo:
    """Converte o tipo de vínculo textual, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoVinculo(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de vínculo inválido: {valor}") from exc


def _tipo_imovel(valor: str) -> TipoImovel:
    """Converte o tipo textual do imóvel, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoImovel(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de imóvel inválido: {valor}") from exc


def _tipo_propriedade(valor: str) -> TipoPropriedade:
    """Converte o tipo de propriedade textual, rejeitando valores desconhecidos."""
    from ..domain.exceptions import RegraNegocioError

    try:
        return TipoPropriedade(valor)
    except ValueError as exc:
        raise RegraNegocioError(f"Tipo de propriedade inválido: {valor}") from exc


@dataclass
class CadastrarImovelInput:
    """DTO de cadastro de unidade imobiliária (RN-IMO-001/002)."""

    inscricao_imobiliaria: str
    logradouro_id: str
    bairro_id: str
    numero: str = ""
    complemento: str = ""
    tipo: str = "lote"
    tipo_propriedade: str = "proprio"
    area_terreno_m2: float = 0.0
    area_construida_m2: float = 0.0
    ano_construcao: int | None = None
    autor_id: str = ""


class CadastrarImovelUseCase:
    """Cadastra uma unidade imobiliária (RN-IMO-001/002)."""

    def __init__(self, repo: ports.RepositorioImovel) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarImovelInput) -> Imovel:
        """Executa o cadastro."""
        from ..domain.exceptions import ImovelJaExistenteError, RegraNegocioError

        if not dto.inscricao_imobiliaria:
            raise RegraNegocioError("Inscrição imobiliária é obrigatória (RN-IMO-001)")
        if self._repo.get_by_inscricao(dto.inscricao_imobiliaria) is not None:
            raise ImovelJaExistenteError(
                "Já existe imóvel com esta inscrição imobiliária (RN-IMO-001)"
            )

        imovel = Imovel(
            inscricao_imobiliaria=dto.inscricao_imobiliaria,
            logradouro_id=dto.logradouro_id,
            bairro_id=dto.bairro_id,
            numero=dto.numero,
            complemento=dto.complemento,
            tipo=_tipo_imovel(dto.tipo),
            tipo_propriedade=_tipo_propriedade(dto.tipo_propriedade),
            area_terreno_m2=dto.area_terreno_m2,
            area_construida_m2=dto.area_construida_m2,
            ano_construcao=dto.ano_construcao,
            created_by=dto.autor_id,
        )
        imovel.validar()
        return self._repo.save(imovel)


@dataclass
class AtualizarImovelInput:
    """DTO de atualização cadastral do imóvel (campos opcionais)."""

    imovel_id: str
    numero: str | None = None
    complemento: str | None = None
    tipo: str | None = None
    tipo_propriedade: str | None = None
    area_terreno_m2: float | None = None
    area_construida_m2: float | None = None
    ano_construcao: int | None = None
    autor_id: str = ""


class AtualizarImovelUseCase:
    """Atualiza o cadastro de uma unidade imobiliária (RN-IMO-003)."""

    def __init__(self, repo: ports.RepositorioImovel) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarImovelInput) -> Imovel:
        """Executa a atualização."""
        from ..domain.exceptions import ImovelNaoEncontradoError

        imovel = self._repo.get_by_id(dto.imovel_id)
        if imovel is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para atualização")

        if dto.numero is not None:
            imovel.numero = dto.numero
        if dto.complemento is not None:
            imovel.complemento = dto.complemento
        if dto.tipo is not None:
            imovel.tipo = _tipo_imovel(dto.tipo)
        if dto.tipo_propriedade is not None:
            imovel.tipo_propriedade = _tipo_propriedade(dto.tipo_propriedade)
        if dto.area_terreno_m2 is not None:
            imovel.area_terreno_m2 = dto.area_terreno_m2
        if dto.area_construida_m2 is not None:
            imovel.area_construida_m2 = dto.area_construida_m2
        if dto.ano_construcao is not None:
            imovel.ano_construcao = dto.ano_construcao

        imovel.validar()
        imovel.updated_at = datetime.utcnow()
        return self._repo.save(imovel)


class AlterarSituacaoImovelUseCase:
    """Altera a situação do imóvel respeitando a máquina de estados (RN-IMO-004)."""

    def __init__(self, repo: ports.RepositorioImovel) -> None:
        self._repo = repo

    def execute(self, imovel_id: str, situacao: str) -> Imovel:
        """Executa a mudança de situação."""
        from ..domain.exceptions import ImovelNaoEncontradoError, RegraNegocioError

        imovel = self._repo.get_by_id(imovel_id)
        if imovel is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para alteração de situação")
        try:
            destino = SituacaoImovel(situacao)
        except ValueError as exc:
            raise RegraNegocioError(f"Situação inválida para imóvel: {situacao}") from exc
        imovel.mudar_situacao(destino)
        return self._repo.save(imovel)


class ExcluirImovelUseCase:
    """Exclui (soft-delete) uma unidade imobiliária (RN-IMO-003)."""

    def __init__(self, repo: ports.RepositorioImovel) -> None:
        self._repo = repo

    def execute(self, imovel_id: str) -> Imovel:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import ImovelNaoEncontradoError

        imovel = self._repo.get_by_id(imovel_id)
        if imovel is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para exclusão")
        imovel.excluir()
        return self._repo.save(imovel)


@dataclass
class VincularProprietarioInput:
    """DTO de vínculo de pessoa com a unidade imobiliária (RN-IMO-006)."""

    imovel_id: str
    nome: str
    cpf: str
    pessoa_id: str = ""
    vinculo: str = "titular"
    principal: bool = False
    autor_id: str = ""


class VincularProprietarioUseCase:
    """Vincula um proprietário à unidade imobiliária (RN-IMO-006).

    Ao vincular um novo titular principal, os demais titulares principais
    anteriores são rebaixados, preservando o histórico do cadastro.
    """

    def __init__(
        self, repo: ports.RepositorioProprietario, imoveis: ports.RepositorioImovel
    ) -> None:
        self._repo = repo
        self._imoveis = imoveis

    def execute(self, dto: VincularProprietarioInput) -> ProprietarioImovel:
        """Executa o vínculo."""
        from ..domain.exceptions import (
            ImovelNaoEncontradoError,
            ProprietarioJaExistenteError,
            ProprietarioPrincipalDuplicadoError,
        )

        if self._imoveis.get_by_id(dto.imovel_id) is None:
            raise ImovelNaoEncontradoError("Imóvel não encontrado para vínculo")
        if self._repo.get_by_imovel_e_cpf(dto.imovel_id, dto.cpf) is not None:
            raise ProprietarioJaExistenteError(
                "Esta pessoa já está vinculada ao imóvel (RN-IMO-006)"
            )

        vinculo = _tipo_vinculo(dto.vinculo)
        principal = dto.principal and vinculo == TipoVinculo.TITULAR
        if principal and self._repo.get_principal(dto.imovel_id) is not None:
            raise ProprietarioPrincipalDuplicadoError(
                "Imóvel já possui proprietário titular principal (RN-IMO-006)"
            )

        proprietario = ProprietarioImovel(
            imovel_id=dto.imovel_id,
            pessoa_id=dto.pessoa_id,
            nome=dto.nome,
            cpf=dto.cpf,
            vinculo=vinculo,
            principal=principal,
            created_by=dto.autor_id,
        )
        proprietario.validar()
        return self._repo.save(proprietario)


class RemoverProprietarioUseCase:
    """Remove o vínculo de propriedade de uma unidade imobiliária (RN-IMO-006)."""

    def __init__(self, repo: ports.RepositorioProprietario) -> None:
        self._repo = repo

    def execute(self, vinculo_id: str) -> ProprietarioImovel:
        """Executa a remoção lógica."""
        from ..domain.exceptions import ProprietarioNaoEncontradoError

        vinculo = self._repo.get_by_id(vinculo_id)
        if vinculo is None:
            raise ProprietarioNaoEncontradoError("Vínculo de propriedade não encontrado")
        vinculo.remover()
        return self._repo.save(vinculo)

