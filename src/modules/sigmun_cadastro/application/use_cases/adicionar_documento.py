"""Caso de uso: Adicionar Documento a uma Pessoa (DOM-CUM RN-CUM-002/003/004)."""

from __future__ import annotations

import logging

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    AdicionarDocumentoCommand,
)
from src.modules.sigmun_cadastro.application.use_cases.registrar_pessoa import (
    _normalizar_documento,
)
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.exceptions import (
    DocumentoDuplicadoError,
    DocumentoInvalidoError,
    PessoaNaoEncontradoError,
)
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)

logger = logging.getLogger(__name__)


class AdicionarDocumentoUseCase:
    """Adiciona um documento ao agregado da pessoa.

    Normaliza e valida CPF/CNPJ (RN-CUM-002/003) e verifica unicidade
    entre pessoas vivas (RN-CUM-004).
    """

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: AdicionarDocumentoCommand) -> Pessoa:
        pessoa = self._repository.get_by_id(command.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradoError(f"Pessoa {command.pessoa_id} não encontrada")

        numero = _normalizar_documento(command.tipo, command.numero)
        if self._repository.exists_documento(command.tipo, numero):
            raise DocumentoDuplicadoError(
                f"Documento {command.tipo.value} {numero} já registrado para outra "
                "pessoa (RN-CUM-004)"
            )

        try:
            pessoa.adicionar_documento(
                tipo=command.tipo,
                numero=numero,
                usuario_id=command.usuario_id,
                orgao_emissor=command.orgao_emissor,
                data_emissao=command.data_emissao,
                data_validade=command.data_validade,
                principal=command.principal,
            )
        except ValueError as exc:
            raise DocumentoInvalidoError(str(exc)) from exc

        salvo = self._repository.save(pessoa)
        logger.info("Documento %s/%s adicionado à pessoa %s", command.tipo.value, numero, command.pessoa_id)
        return salvo


__all__ = ["AdicionarDocumentoUseCase"]
