"""Casos de uso da aplicação de Gestão Documental."""

from .criar_documento_use_case import (
    CriarDocumentoUseCase,
    CriarDocumentoInputDTO,
    CriarDocumentoOutputDTO,
)
from .classificar_documento_use_case import ClassificarDocumentoUseCase
from .tramitar_documento_use_case import TramitarDocumentoUseCase
from .arquivar_documento_use_case import (
    ArquivarDocumentoUseCase,
    ArquivarDocumentoInputDTO,
)
from .assinar_documento_use_case import (
    AssinarDocumentoUseCase,
    AssinarDocumentoInputDTO,
)
from .criar_versao_documento_use_case import (
    CriarVersaoDocumentoUseCase,
    CriarVersaoInputDTO,
)
from .avaliar_destinacao_use_case import (
    AvaliarDestinacaoUseCase,
    AvaliarDestinacaoInputDTO,
    TipoDestinacaoAplicada,
)
from .tipo_documento_use_cases import (
    CriarTipoDocumentoUseCase,
    CriarTipoDocumentoInputDTO,
    AtivarTipoDocumentoUseCase,
    InativarTipoDocumentoUseCase,
    BuscarTipoDocumentoUseCase,
    ListarTiposDocumentoUseCase,
    TipoDocumentoOutputDTO,
)

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
