"""Caso de uso: Registrar Pessoa (DOM-CUM).

Baseado em:
  - 005-Casos-de-Uso-Cadastro-Unico-Municipal.md (registrar pessoa)
  - RN-CUM-001 a 006
"""

from __future__ import annotations

import logging
from uuid import uuid4

from src.modules.sigmun_cadastro.application.commands.pessoa_commands import (
    CriarPessoaCommand,
)
from src.modules.sigmun_cadastro.domain.entities.documento import TipoDocumento
from src.modules.sigmun_cadastro.domain.entities.pessoa import Pessoa
from src.modules.sigmun_cadastro.domain.events.pessoa_events import PessoaRegistradaEvent
from src.modules.sigmun_cadastro.domain.exceptions import DocumentoDuplicadoError
from src.modules.sigmun_cadastro.domain.repositories.pessoa_repository import (
    PessoaRepository,
)
from src.modules.sigmun_cadastro.domain.value_objects.cnpj import CNPJ
from src.modules.sigmun_cadastro.domain.value_objects.cpf import CPF

logger = logging.getLogger(__name__)


def _normalizar_documento(tipo: TipoDocumento, numero: str) -> str:
    """Valida CPF/CNPJ (RN-CUM-002/003) e devolve apenas dígitos."""
    if tipo is TipoDocumento.CPF:
        return CPF(numero).valor
    if tipo is TipoDocumento.CNPJ:
        return CNPJ(numero).valor
    if not numero or not numero.strip():
        raise ValueError("Número do documento é obrigatório")
    return numero.strip()


class RegistrarPessoaUseCase:
    """Orquestra o registro de uma nova pessoa com seus dados de contato."""

    def __init__(self, repository: PessoaRepository) -> None:
        self._repository = repository

    def execute(self, command: CriarPessoaCommand) -> Pessoa:
        logger.info("Registrando pessoa – tipo=%s categoria=%s", command.tipo, command.categoria)

        # RN-CUM-002/003/004: valida e verifica unicidade dos documentos
        documentos_normalizados: list[tuple[TipoDocumento, str, dict]] = []
        for doc in command.documentos:
            tipo = TipoDocumento(doc["tipo"])
            numero = _normalizar_documento(tipo, doc["numero"])
            if self._repository.exists_documento(tipo, numero):
                raise DocumentoDuplicadoError(
                    f"Documento {tipo.value} {numero} já registrado para outra pessoa "
                    "(RN-CUM-004)"
                )
            documentos_normalizados.append((tipo, numero, doc))

        pessoa = Pessoa(
            tipo=command.tipo,
            categoria=command.categoria,
            unidade_id=command.unidade_id,
            dados_fisicos=command.dados_fisicos(),
            dados_juridicos=command.dados_juridicos(),
            created_by=command.usuario_id,
        )

        for tipo, numero, doc in documentos_normalizados:
            pessoa.adicionar_documento(
                tipo,
                numero,
                usuario_id=command.usuario_id,
                orgao_emissor=doc.get("orgao_emissor"),
                data_emissao=doc.get("data_emissao"),
                data_validade=doc.get("data_validade"),
                principal=doc.get("principal", False),
            )
        for end in command.enderecos:
            extras = {
                k: v for k, v in end.items() if k not in ("tipo", "logradouro", "numero")
            }
            pessoa.adicionar_endereco(
                tipo=end["tipo"],
                logradouro=end["logradouro"],
                numero=end["numero"],
                usuario_id=command.usuario_id,
                **extras,
            )
        for contato in command.contatos:
            pessoa.adicionar_contato(
                tipo=contato["tipo"],
                valor=contato["valor"],
                usuario_id=command.usuario_id,
                principal=contato.get("principal", False),
            )

        salvo = self._repository.save(pessoa)

        evento = PessoaRegistradaEvent(
            event_id=uuid4(),
            pessoa_id=salvo.id,
            tipo=salvo.tipo.value,
            categoria=salvo.categoria.value,
            occurred_at=salvo.created_at,
        )
        logger.info("Pessoa registrada: %s", evento)
        return salvo


__all__ = ["RegistrarPessoaUseCase", "_normalizar_documento"]
