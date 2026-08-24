"""Casos de uso do domínio Gestão de Compras e Contratações."""

from src.modules.sigmun_compras.application.use_cases.alterar_situacao_compra import (
    AlterarSituacaoCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_compra import (
    AtualizarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_fornecedor import (
    AtualizarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_item_compra import (
    AtualizarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.atualizar_processo_documental import (
    AtualizarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_compra import (
    ConsultarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_fornecedor import (
    ConsultarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_item_compra import (
    ConsultarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.consultar_processo_documental import (
    ConsultarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_compra import (
    ExcluirCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.excluir_processo_documental import (
    ExcluirProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.inativar_fornecedor import (
    InativarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_compras import (
    ListarComprasUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_fornecedores import (
    ListarFornecedoresUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_itens_compra import (
    ListarItensCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.listar_processos_documentais import (
    ListarProcessosDocumentaisUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_compra import (
    RegistrarCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_fornecedor import (
    RegistrarFornecedorUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_item_compra import (
    RegistrarItemCompraUseCase,
)
from src.modules.sigmun_compras.application.use_cases.registrar_processo_documental import (
    RegistrarProcessoDocumentalUseCase,
)
from src.modules.sigmun_compras.application.use_cases.remover_item_compra import (
    RemoverItemCompraUseCase,
)

__all__ = [
    "RegistrarFornecedorUseCase",
    "ConsultarFornecedorUseCase",
    "ListarFornecedoresUseCase",
    "AtualizarFornecedorUseCase",
    "InativarFornecedorUseCase",
    "RegistrarItemCompraUseCase",
    "ConsultarItemCompraUseCase",
    "ListarItensCompraUseCase",
    "AtualizarItemCompraUseCase",
    "RemoverItemCompraUseCase",
    "RegistrarCompraUseCase",
    "ConsultarCompraUseCase",
    "ListarComprasUseCase",
    "AtualizarCompraUseCase",
    "AlterarSituacaoCompraUseCase",
    "ExcluirCompraUseCase",
    "RegistrarProcessoDocumentalUseCase",
    "ConsultarProcessoDocumentalUseCase",
    "ListarProcessosDocumentaisUseCase",
    "AtualizarProcessoDocumentalUseCase",
    "ExcluirProcessoDocumentalUseCase",
]


