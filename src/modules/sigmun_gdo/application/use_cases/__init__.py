"""Casos de uso da aplicação de Gestão Documental."""

from .arquivar_documento_use_case import (
    ArquivarDocumentoInputDTO,
    ArquivarDocumentoUseCase,
)
from .assinar_documento_use_case import (
    AssinarDocumentoInputDTO,
    AssinarDocumentoUseCase,
)
from .avaliar_destinacao_use_case import (
    AvaliarDestinacaoInputDTO,
    AvaliarDestinacaoUseCase,
    TipoDestinacaoAplicada,
)
from .classificar_documento_use_case import ClassificarDocumentoUseCase
from .criar_documento_use_case import (
    CriarDocumentoInputDTO,
    CriarDocumentoOutputDTO,
    CriarDocumentoUseCase,
)
from .criar_versao_documento_use_case import (
    CriarVersaoDocumentoUseCase,
    CriarVersaoInputDTO,
)
from .tipo_documento_use_cases import (
    AtivarTipoDocumentoUseCase,
    BuscarTipoDocumentoUseCase,
    CriarTipoDocumentoInputDTO,
    CriarTipoDocumentoUseCase,
    InativarTipoDocumentoUseCase,
    ListarTiposDocumentoUseCase,
    TipoDocumentoOutputDTO,
)
from .tramitar_documento_use_case import TramitarDocumentoUseCase

__all__ = [
    "CriarDocumentoUseCase",
    "CriarDocumentoInputDTO",
    "CriarDocumentoOutputDTO",
    "ClassificarDocumentoUseCase",
    "TramitarDocumentoUseCase",
    "ArquivarDocumentoUseCase",
    "ArquivarDocumentoInputDTO",
    "AssinarDocumentoUseCase",
    "AssinarDocumentoInputDTO",
    "CriarVersaoDocumentoUseCase",
    "CriarVersaoInputDTO",
    "AvaliarDestinacaoUseCase",
    "AvaliarDestinacaoInputDTO",
    "TipoDestinacaoAplicada",
    "CriarTipoDocumentoUseCase",
    "CriarTipoDocumentoInputDTO",
    "AtivarTipoDocumentoUseCase",
    "InativarTipoDocumentoUseCase",
    "BuscarTipoDocumentoUseCase",
    "ListarTiposDocumentoUseCase",
    "TipoDocumentoOutputDTO",
]
