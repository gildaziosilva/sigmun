"""Testes unitários da integração Formalização da Contratação.

Valida o caso de uso FormalizarContratacaoUseCase que integra os
repositórios de Compra (processo) e de Contrato, exercitando as regras
RN-COMPRAS-026/036/038 sem depender de banco.
"""

from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from src.modules.sigmun_compras.application.commands.formalizar_contratacao_command import (
    FormalizarContratacaoCommand,
)
from src.modules.sigmun_compras.application.use_cases.formalizar_contratacao import (
    FormalizarContratacaoUseCase,
)
from src.modules.sigmun_compras.domain.entities.compra import Compra, SituacaoCompra
from src.modules.sigmun_compras.domain.entities.contrato import SituacaoContrato
from src.modules.sigmun_compras.domain.exceptions import (
    CompraNaoEncontradaError,
    ContratoDuplicadoError,
)
from tests.unit.test_compra_use_cases import InMemoryCompraRepository
from tests.unit.test_contrato_use_cases import InMemoryContratoRepository


def _montar_repositorios(criar_homologada: bool = True):
    """Configura repositórios com uma compra e os vínculos válidos."""
    processo = uuid4()
    fornecedor = uuid4()
    unidade = uuid4()

    compras = InMemoryCompraRepository()
    contratos = InMemoryContratoRepository()

    compras.add_processo(processo)
    compras.add_fornecedor_ativo(fornecedor)
    compras.add_unidade(unidade)

    contratos.add_processo_documental(processo)
    contratos.add_fornecedor_ativo(fornecedor)
    contratos.add_unidade(unidade)

    situacao = (
        SituacaoCompra.HOMOLOGADO if criar_homologada else SituacaoCompra.RASCUNHO
    )
    compra = Compra(
        processo_documental_id=processo,
        fornecedor_id=fornecedor,
        unidade_id=unidade,
        numero="001/2026",
        data=date(2026, 1, 1),
        valor_total=Decimal("10000.00"),
        situacao=situacao,
    )
    compras.save(compra)

    return compras, contratos, compra


def _command(**overrides) -> FormalizarContratacaoCommand:
    dados = {
        "compra_id": uuid4(),
        "numero": "CT-001/2026",
        "data_inicio": date(2026, 2, 1),
        "data_fim": date(2026, 12, 31),
        "valor": Decimal("10000.00"),
        "objeto": "Serviços de limpeza",
        "usuario_id": uuid4(),
    }
    dados.update(overrides)
    return FormalizarContratacaoCommand(**dados)


def test_formalizar_contratacao_sucesso_avanca_compra() -> None:
    compras, contratos, compra = _montar_repositorios()
    use_case = FormalizarContratacaoUseCase(contratos, compras)

    contrato = use_case.execute(_command(compra_id=compra.id))

    assert contrato.compra_id == compra.id
    assert contrato.processo_documental_id == compra.processo_documental_id
    assert contrato.situacao == SituacaoContrato.EM_ELABORACAO

    compra_salva = compras.get_by_id(compra.id)
    assert compra_salva is not None
    assert compra_salva.situacao == SituacaoCompra.CONTRATADO


def test_formalizar_contratacao_compra_inexistente_lanca_erro() -> None:
    compras = InMemoryCompraRepository()
    contratos = InMemoryContratoRepository()

    use_case = FormalizarContratacaoUseCase(contratos, compras)
    with pytest.raises(CompraNaoEncontradaError):
        use_case.execute(_command())


def test_formalizar_contratacao_compra_nao_homologada_lanca_erro() -> None:
    compras, contratos, compra = _montar_repositorios(criar_homologada=False)

    use_case = FormalizarContratacaoUseCase(contratos, compras)
    with pytest.raises(ValueError, match="HOMOLOGADA"):
        use_case.execute(_command(compra_id=compra.id))


def test_formalizar_contratacao_numero_duplicado_lanca_erro() -> None:
    compras, contratos, compra = _montar_repositorios()

    use_case = FormalizarContratacaoUseCase(contratos, compras)
    use_case.execute(_command(compra_id=compra.id, numero="CT-001/2026"))

    with pytest.raises(ContratoDuplicadoError):
        use_case.execute(_command(compra_id=compra.id, numero="CT-001/2026"))


def test_formalizar_contratacao_com_assinatura_avanca_para_assinado() -> None:
    compras, contratos, compra = _montar_repositorios()
    use_case = FormalizarContratacaoUseCase(contratos, compras)

    contrato = use_case.execute(
        _command(compra_id=compra.id, numero="CT-002/2026", data_assinatura=date(2026, 2, 1))
    )

    assert contrato.situacao == SituacaoContrato.ASSINADO


def test_formalizar_contratacao_assinatura_sem_usuario_lanca_erro() -> None:
    compras, contratos, compra = _montar_repositorios()
    use_case = FormalizarContratacaoUseCase(contratos, compras)

    with pytest.raises(ValueError, match="usuário autenticado"):
        use_case.execute(
            _command(
                compra_id=compra.id,
                numero="CT-003/2026",
                data_assinatura=date(2026, 2, 1),
                usuario_id=None,
            )
        )
