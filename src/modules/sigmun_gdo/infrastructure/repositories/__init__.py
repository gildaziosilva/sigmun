"""Repositórios do módulo de Gestão Documental."""

from .sqlalchemy_arquivamento_repository import SQLAlchemyArquivamentoRepository
from .sqlalchemy_assinatura_repository import SQLAlchemyAssinaturaRepository
from .sqlalchemy_classificacao_documental_repository import (
    SQLAlchemyClassificacaoDocumentalRepository,
)
from .sqlalchemy_documento_repository import SQLAlchemyDocumentoRepository
from .sqlalchemy_processo_documento_repository import SQLAlchemyProcessoDocumentoRepository
from .sqlalchemy_tabela_temporalidade_repository import SQLAlchemyTabelaTemporalidadeRepository
from .sqlalchemy_tipo_documental_repository import SQLAlchemyTipoDocumentalRepository
from .sqlalchemy_tramitacao_repository import SQLAlchemyTramitacaoRepository
from .sqlalchemy_versao_documento_repository import SQLAlchemyVersaoDocumentoRepository

__all__ = [
    "SQLAlchemyDocumentoRepository",
    "SQLAlchemyVersaoDocumentoRepository",
    "SQLAlchemyTramitacaoRepository",
    "SQLAlchemyProcessoDocumentoRepository",
    "SQLAlchemyClassificacaoDocumentalRepository",
    "SQLAlchemyTabelaTemporalidadeRepository",
    "SQLAlchemyArquivamentoRepository",
    "SQLAlchemyAssinaturaRepository",
    "SQLAlchemyTipoDocumentalRepository",
]
