"""Use Cases para Tipo Documental."""

from dataclasses import dataclass

from ...domain.entities import TipoDocumental
from ...domain.exceptions import (
    CodigoDocumentalDuplicadoError,
    TipoDocumentalInvalidoError,
)
from ..interfaces import RepositorioTipoDocumental


@dataclass
class CriarTipoDocumentoInputDTO:
    codigo: str
    nome: str
    descricao: str = ""


@dataclass
class TipoDocumentoOutputDTO:
    id: str
    codigo: str
    nome: str
    descricao: str
    is_ativo: bool


class CriarTipoDocumentoUseCase:
    """Caso de uso para criar um tipo documental."""

    def __init__(self, repositorio: RepositorioTipoDocumental):
        self._repo = repositorio

    def execute(self, dto: CriarTipoDocumentoInputDTO) -> TipoDocumentoOutputDTO:
        # Verificar unicidade do código (busca incluindo inativos)
        existente = self._repo.find_all()
        if any(t.codigo == dto.codigo for t in existente):
            raise CodigoDocumentalDuplicadoError(
                f"Código '{dto.codigo}' já utilizado por outro tipo documental"
            )

        tipo = TipoDocumental(
            codigo=dto.codigo,
            nome=dto.nome,
            descricao=dto.descricao,
            is_ativo=True,
        )
        salvo = self._repo.save(tipo)
        return _to_output(salvo)


class AtivarTipoDocumentoUseCase:
    """Caso de uso para ativar um tipo documental."""

    def __init__(self, repositorio: RepositorioTipoDocumental):
        self._repo = repositorio

    def execute(self, codigo: str) -> TipoDocumentoOutputDTO:
        tipos = self._repo.find_all()
        tipo = next((t for t in tipos if t.codigo == codigo), None)
        if not tipo:
            raise TipoDocumentalInvalidoError(f"Tipo documental '{codigo}' não encontrado")
        tipo.is_ativo = True
        salvo = self._repo.save(tipo)
        return _to_output(salvo)


class InativarTipoDocumentoUseCase:
    """Caso de uso para inativar um tipo documental."""

    def __init__(self, repositorio: RepositorioTipoDocumental):
        self._repo = repositorio

    def execute(self, codigo: str) -> TipoDocumentoOutputDTO:
        tipos = self._repo.find_all()
        tipo = next((t for t in tipos if t.codigo == codigo), None)
        if not tipo:
            raise TipoDocumentalInvalidoError(f"Tipo documental '{codigo}' não encontrado")
        tipo.is_ativo = False
        salvo = self._repo.save(tipo)
        return _to_output(salvo)


class BuscarTipoDocumentoUseCase:
    """Caso de uso para buscar tipo documental por código."""

    def __init__(self, repositorio: RepositorioTipoDocumental):
        self._repo = repositorio

    def execute(self, codigo: str) -> TipoDocumentoOutputDTO:
        tipos = self._repo.find_all()
        tipo = next((t for t in tipos if t.codigo == codigo), None)
        if not tipo:
            raise TipoDocumentalInvalidoError(f"Tipo documental '{codigo}' não encontrado")
        return _to_output(tipo)


class ListarTiposDocumentoUseCase:
    """Caso de uso para listar tipos documentais ativos."""

    def __init__(self, repositorio: RepositorioTipoDocumental):
        self._repo = repositorio

    def execute(self) -> list[TipoDocumentoOutputDTO]:
        return [_to_output(t) for t in self._repo.find_ativos()]


def _to_output(tipo: TipoDocumental) -> TipoDocumentoOutputDTO:
    return TipoDocumentoOutputDTO(
        id=tipo.id,
        codigo=tipo.codigo,
        nome=tipo.nome,
        descricao=tipo.descricao,
        is_ativo=tipo.is_ativo,
    )


# ---------------------------------------------------------------------------
# Aliases PT-BR espelhados no DOM-COMPRAS-001 (Registrar/Consultar).
# ---------------------------------------------------------------------------
RegistrarTipoDocumentoUseCase = CriarTipoDocumentoUseCase
ConsultarTipoDocumentoUseCase = BuscarTipoDocumentoUseCase
