"""Use cases de PPA/LDO/LOA (DOM-ORC)."""

from __future__ import annotations

from dataclasses import dataclass

from ..domain.entities.ldo import LDO, StatusLDO
from ..domain.entities.loa import LOA
from ..domain.entities.ppa import PPA, StatusPPA
from . import interfaces as ports


@dataclass
class CriarPPAInput:
    """DTO de criação de PPA."""

    ano_inicial: int
    ano_final: int
    descricao: str = ""
    autor_id: str = ""


class CriarPPAUseCase:
    """Cria PPA do quadriênio (RN-ORC-001)."""

    def __init__(self, repo: ports.RepositorioPPA) -> None:
        self._repo = repo

    def execute(self, dto: CriarPPAInput) -> PPA:
        """Executa a criação."""
        from ..domain.exceptions import RegraNegocioError

        if dto.ano_final - dto.ano_inicial != 3:
            raise RegraNegocioError("PPA deve cobrir um quadriênio (RN-ORC-001)")
        if self._repo.get_by_quadrienio(dto.ano_inicial, dto.ano_final) is not None:
            raise RegraNegocioError("PPA já existe para este quadriênio (RN-ORC-001)")
        ppa = PPA(ano_inicial=dto.ano_inicial, ano_final=dto.ano_final,
                  descricao=dto.descricao, created_by=dto.autor_id)
        return self._repo.save(ppa)


class PublicarPPAUseCase:
    """Publica PPA em elaboração."""

    def __init__(self, repo: ports.RepositorioPPA) -> None:
        self._repo = repo

    def execute(self, ppa_id: str) -> PPA:
        """Executa a publicação."""
        from ..domain.exceptions import PPANaoEncontradoError

        ppa = self._repo.get_by_id(ppa_id)
        if ppa is None:
            raise PPANaoEncontradoError("PPA não encontrado")
        ppa.publicar()
        return self._repo.save(ppa)


@dataclass
class CriarLDOInput:
    """DTO de criação de LDO."""

    exercicio: int
    ppa_id: str
    descricao: str = ""
    meta_receita: float = 0.0
    meta_despesa: float = 0.0
    autor_id: str = ""


class CriarLDOUseCase:
    """Cria LDO vinculada a PPA vigente (RN-ORC-011)."""

    def __init__(self, ldos: ports.RepositorioLDO, ppas: ports.RepositorioPPA) -> None:
        self._ldos = ldos
        self._ppas = ppas

    def execute(self, dto: CriarLDOInput) -> LDO:
        """Executa a criação."""
        from ..domain.exceptions import RegraNegocioError

        if dto.exercicio < 2000:
            raise RegraNegocioError("Exercício inválido")
        if self._ldos.get_by_exercicio(dto.exercicio) is not None:
            raise RegraNegocioError(f"LDO {dto.exercicio} já existe (RN-ORC-010)")
        ppa = self._ppas.get_by_id(dto.ppa_id)
        if ppa is None:
            raise RegraNegocioError("PPA inválido (RN-ORC-011)")
        if ppa.status != StatusPPA.VIGENTE:
            raise RegraNegocioError("LDO exige PPA vigente (RN-ORC-011)")
        if not (ppa.ano_inicial <= dto.exercicio <= ppa.ano_final):
            raise RegraNegocioError("Exercício fora do quadriênio do PPA")
        ldo = LDO(exercicio=dto.exercicio, ppa_id=dto.ppa_id,
                  descricao=dto.descricao, meta_fiscal_receita=dto.meta_receita,
                  meta_fiscal_despesa=dto.meta_despesa, created_by=dto.autor_id)
        return self._ldos.save(ldo)


class SancionarLDOUseCase:
    """Aprova e sanciona LDO."""

    def __init__(self, repo: ports.RepositorioLDO) -> None:
        self._repo = repo

    def execute(self, ldo_id: str, sancionar: bool = False) -> LDO:
        """Aprova; se sancionar=True, aprova e sanciona."""
        from ..domain.exceptions import LDONaoEncontradaError

        ldo = self._repo.get_by_id(ldo_id)
        if ldo is None:
            raise LDONaoEncontradaError("LDO não encontrada")
        ldo.aprovar()
        if sancionar:
            ldo.sancionar()
        return self._repo.save(ldo)


@dataclass
class CriarLOAInput:
    """DTO de criação de LOA."""

    exercicio: int
    ldo_id: str
    descricao: str = ""
    receita: float = 0.0
    despesa: float = 0.0
    autor_id: str = ""


class CriarLOAUseCase:
    """Cria LOA vinculada a LDO sancionada (RN-ORC-021)."""

    def __init__(self, loas: ports.RepositorioLOA, ldos: ports.RepositorioLDO) -> None:
        self._loas = loas
        self._ldos = ldos

    def execute(self, dto: CriarLOAInput) -> LOA:
        """Executa a criação."""
        from ..domain.exceptions import RegraNegocioError

        if dto.exercicio < 2000:
            raise RegraNegocioError("Exercício inválido")
        if self._loas.get_by_exercicio(dto.exercicio) is not None:
            raise RegraNegocioError(f"LOA {dto.exercicio} já existe (RN-ORC-020)")
        ldo = self._ldos.get_by_id(dto.ldo_id)
        if ldo is None:
            raise RegraNegocioError("LDO inválida (RN-ORC-021)")
        if ldo.status != StatusLDO.SANCIONADA:
            raise RegraNegocioError("LOA exige LDO sancionada (RN-ORC-021)")
        if ldo.exercicio != dto.exercicio:
            raise RegraNegocioError("LOA e LDO devem ter mesmo exercício")
        loa = LOA(exercicio=dto.exercicio, ldo_id=dto.ldo_id,
                  descricao=dto.descricao, valor_receita_prevista=dto.receita,
                  valor_despesa_fixada=dto.despesa, created_by=dto.autor_id)
        return self._loas.save(loa)


class PublicarLOAUseCase:
    """Aprova e publica LOA."""

    def __init__(self, repo: ports.RepositorioLOA) -> None:
        self._repo = repo

    def execute(self, loa_id: str, publicar: bool = False) -> LOA:
        """Aprova; se publicar=True, aprova e publica."""
        from ..domain.exceptions import LOANaoEncontradaError

        loa = self._repo.get_by_id(loa_id)
        if loa is None:
            raise LOANaoEncontradaError("LOA não encontrada")
        loa.aprovar()
        if publicar:
            loa.publicar()
        return self._repo.save(loa)


__all__ = [
    "CriarPPAInput", "CriarPPAUseCase", "PublicarPPAUseCase",
    "CriarLDOInput", "CriarLDOUseCase", "SancionarLDOUseCase",
    "CriarLOAInput", "CriarLOAUseCase", "PublicarLOAUseCase",
]
