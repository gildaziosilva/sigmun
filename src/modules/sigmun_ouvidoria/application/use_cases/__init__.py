"""Use cases do DOM-OUV (Ouvidoria FalaBR / e-OUV municipal)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID, uuid4

from ...domain.entities import Denuncia, Manifestacao, PedidoLai, Prioridade
from ...domain.exceptions import (
    DenunciaNaoEncontradaError,
    ManifestacaoNaoEncontradaError,
    PedidoLaiNaoEncontradoError,
    RegraNegocioError,
)
from ...domain.services import (
    CalculadoraPrazo,
    GeradorProtocolo,
    ServicoEncaminhamento,
    ServicoEstatisticas,
    ValidadorManifestacao,
)
from ...domain.value_objects import (
    Anexo,
    CanalRecebimento,
    DadosCidadao,
    FormaResposta,
    NivelSigilo,
    StatusManifestacao,
    TipoDenuncia,
    TipoManifestacao,
)
from ..interfaces import (
    RepositorioAnexo,
    RepositorioDenuncia,
    RepositorioManifestacao,
    RepositorioPedidoLai,
    RepositorioProtocolo,
    RepositorioTramitacao,
)

# ==================== DTOs ====================


@dataclass
class RegistrarManifestacaoInput:
    """DTO para registro de manifestação genérica."""

    tipo: str = "solicitacao"
    assunto: str = ""
    descricao: str = ""
    cidadao_nome: str = ""
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    cidadao_anonimo: bool = False
    canal: str = "portal_cidadao"
    orgao_destino: str = ""
    setor_responsavel: str = ""
    prioridade: str = "normal"
    anexos: list[dict] = None
    autor_id: str = ""


@dataclass
class RegistrarDenunciaInput:
    """DTO para registro de denúncia."""

    assunto: str = ""
    descricao: str = ""
    tipo_denuncia: str = "outro"
    envolve_servidor_publico: bool = False
    servidor_envolvido: str = ""
    valor_envolvido: float | None = None
    local_fato: str = ""
    data_fato: date | None = None
    cidadao_nome: str = ""
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    cidadao_anonimo: bool = True
    canal: str = "portal_cidadao"
    orgao_destino: str = ""
    setor_responsavel: str = ""
    prioridade: str = "alta"
    anexos: list[dict] = None
    autor_id: str = ""


@dataclass
class RegistrarPedidoLaiInput:
    """DTO para registro de pedido LAI."""

    assunto: str = ""
    descricao: str = ""
    informacao_solicitada: str = ""
    fundamentacao: str = ""
    nivel_sigilo: str = "publico"
    fundamentacao_sigilo: str = ""
    dados_pessoais_terceiros: bool = False
    formato_resposta: str = "digital"
    cidadao_nome: str = ""
    cidadao_cpf: str = ""
    cidadao_email: str = ""
    cidadao_telefone: str = ""
    cidadao_endereco: str = ""
    canal: str = "portal_cidadao"
    orgao_destino: str = ""
    setor_responsavel: str = ""
    prioridade: str = "normal"
    anexos: list[dict] = None
    autor_id: str = ""


@dataclass
class ResponderManifestacaoInput:
    """DTO para resposta de manifestação."""

    manifestacao_id: str
    resposta: str
    forma_resposta: str = "portal"
    respondido_por: str = ""


@dataclass
class AlterarStatusInput:
    """DTO para alteração de status."""

    manifestacao_id: str
    novo_status: str
    observacao: str = ""
    usuario_id: str = ""


@dataclass
class ProrrogarPrazoInput:
    """DTO para prorrogação de prazo."""

    manifestacao_id: str
    justificativa: str
    usuario_id: str = ""


@dataclass
class AvaliarManifestacaoInput:
    """DTO para avaliação do cidadão."""

    manifestacao_id: str
    nota: int
    comentario: str = ""


@dataclass
class EncaminharDenunciaInput:
    """DTO para encaminhamento de denúncia a órgão externo."""

    denuncia_id: str
    orgao: str
    numero_processo: str
    usuario_id: str = ""


@dataclass
class InterporRecursoLaiInput:
    """DTO para interposição de recurso LAI."""

    pedido_original_id: str
    autor_id: str = ""


@dataclass
class DecidirRecursoLaiInput:
    """DTO para decisão de recurso LAI."""

    recurso_id: str
    deferido: bool
    fundamentacao: str
    usuario_id: str = ""


@dataclass
class ListarManifestacoesInput:
    """DTO para listagem paginada."""

    page: int = 1
    page_size: int = 20
    filtros: dict | None = None


# ==================== Use Cases ====================


class RegistrarManifestacaoUseCase:
    """Registra nova manifestação genérica (RN-OUV-001, RN-OUV-002)."""

    def __init__(
        self,
        repo: RepositorioManifestacao,
        protocolo_repo: RepositorioProtocolo,
        anexo_repo: RepositorioAnexo,
        tramitacao_repo: RepositorioTramitacao,
    ) -> None:
        self._repo = repo
        self._protocolo_repo = protocolo_repo
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo
        self._gerador = GeradorProtocolo(protocolo_repo)
        self._validador = ValidadorManifestacao()

    def execute(self, dto: RegistrarManifestacaoInput) -> Manifestacao:
        tipo = TipoManifestacao(dto.tipo)
        if tipo == TipoManifestacao.DENUNCIA:
            raise RegraNegocioError("Use RegistrarDenunciaUseCase para denúncias")
        if tipo == TipoManifestacao.PEDIDO_ACESSO_INFORMACAO:
            raise RegraNegocioError("Use RegistrarPedidoLaiUseCase para pedidos LAI")

        ano = date.today().year
        protocolo = self._gerador.gerar(ano)
        self._gerador.registrar(protocolo)

        cidadao = DadosCidadao(
            nome=dto.cidadao_nome,
            cpf=dto.cidadao_cpf or None,
            email=dto.cidadao_email or None,
            telefone=dto.cidadao_telefone or None,
            endereco=dto.cidadao_endereco or None,
            anonimo=dto.cidadao_anonimo,
        )

        prazo = CalculadoraPrazo.calcular(tipo, date.today())

        anexos = []
        if dto.anexos:
            for a in dto.anexos:
                anexos.append(
                    Anexo(
                        id=str(uuid4()),
                        nome_arquivo=a["nome_arquivo"],
                        tipo_mime=a["tipo_mime"],
                        tamanho_bytes=a["tamanho_bytes"],
                        url=a["url"],
                        descricao=a.get("descricao", ""),
                    )
                )

        manifestacao = Manifestacao(
            protocolo=protocolo,
            tipo=tipo,
            status=StatusManifestacao.REGISTRADA,
            prioridade=Prioridade(dto.prioridade),
            assunto=dto.assunto,
            descricao=dto.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(dto.canal),
            orgao_destino=dto.orgao_destino,
            setor_responsavel=dto.setor_responsavel,
            prazo=prazo,
            anexos=anexos,
            created_by=dto.autor_id,
        )

        manifestacao.validar()
        self._validador.validar_criacao(manifestacao)  # noqa: F841 — validacao executada

        return self._repo.save(manifestacao)


class RegistrarDenunciaUseCase:
    """Registra nova denúncia (RN-OUV-002, RN-OUV-030)."""

    def __init__(
        self,
        repo: RepositorioDenuncia,
        protocolo_repo: RepositorioProtocolo,
        anexo_repo: RepositorioAnexo,
        tramitacao_repo: RepositorioTramitacao,
    ) -> None:
        self._repo = repo
        self._protocolo_repo = protocolo_repo
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo
        self._gerador = GeradorProtocolo(protocolo_repo)
        self._validador = ValidadorManifestacao()

    def execute(self, dto: RegistrarDenunciaInput) -> Denuncia:
        ano = date.today().year
        protocolo = self._gerador.gerar(ano)
        self._gerador.registrar(protocolo)

        cidadao = DadosCidadao(
            nome=dto.cidadao_nome,
            cpf=dto.cidadao_cpf or None,
            email=dto.cidadao_email or None,
            telefone=dto.cidadao_telefone or None,
            endereco=dto.cidadao_endereco or None,
            anonimo=dto.cidadao_anonimo,
        )

        prazo = CalculadoraPrazo.calcular(TipoManifestacao.DENUNCIA, date.today())

        anexos = []
        if dto.anexos:
            for a in dto.anexos:
                anexos.append(
                    Anexo(
                        id=str(uuid4()),
                        nome_arquivo=a["nome_arquivo"],
                        tipo_mime=a["tipo_mime"],
                        tamanho_bytes=a["tamanho_bytes"],
                        url=a["url"],
                        descricao=a.get("descricao", ""),
                    )
                )

        denuncia = Denuncia(
            protocolo=protocolo,
            tipo=TipoManifestacao.DENUNCIA,
            status=StatusManifestacao.REGISTRADA,
            prioridade=Prioridade(dto.prioridade),
            assunto=dto.assunto,
            descricao=dto.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(dto.canal),
            orgao_destino=dto.orgao_destino,
            setor_responsavel=dto.setor_responsavel,
            prazo=prazo,
            anexos=anexos,
            tipo_denuncia=TipoDenuncia(dto.tipo_denuncia),
            envolve_servidor_publico=dto.envolve_servidor_publico,
            servidor_envolvido=dto.servidor_envolvido,
            valor_envolvido=dto.valor_envolvido,
            local_fato=dto.local_fato,
            data_fato=dto.data_fato,
            created_by=dto.autor_id,
        )

        denuncia.validar()
        self._validador.validar_criacao(denuncia)  # noqa: F841 — validacao executada

        return self._repo.save(denuncia)


class RegistrarPedidoLaiUseCase:
    """Registra novo pedido de acesso à informação (RN-OUV-003, LAI Art. 11)."""

    def __init__(
        self,
        repo: RepositorioPedidoLai,
        protocolo_repo: RepositorioProtocolo,
        anexo_repo: RepositorioAnexo,
        tramitacao_repo: RepositorioTramitacao,
    ) -> None:
        self._repo = repo
        self._protocolo_repo = protocolo_repo
        self._anexo_repo = anexo_repo
        self._tramitacao_repo = tramitacao_repo
        self._gerador = GeradorProtocolo(protocolo_repo)
        self._validador = ValidadorManifestacao()

    def execute(self, dto: RegistrarPedidoLaiInput) -> PedidoLai:
        ano = date.today().year
        protocolo = self._gerador.gerar(ano)
        self._gerador.registrar(protocolo)

        cidadao = DadosCidadao(
            nome=dto.cidadao_nome,
            cpf=dto.cidadao_cpf or None,
            email=dto.cidadao_email or None,
            telefone=dto.cidadao_telefone or None,
            endereco=dto.cidadao_endereco or None,
            anonimo=False,
        )

        prazo = CalculadoraPrazo.calcular(TipoManifestacao.PEDIDO_ACESSO_INFORMACAO, date.today())

        anexos = []
        if dto.anexos:
            for a in dto.anexos:
                anexos.append(
                    Anexo(
                        id=str(uuid4()),
                        nome_arquivo=a["nome_arquivo"],
                        tipo_mime=a["tipo_mime"],
                        tamanho_bytes=a["tamanho_bytes"],
                        url=a["url"],
                        descricao=a.get("descricao", ""),
                    )
                )

        pedido = PedidoLai(
            protocolo=protocolo,
            tipo=TipoManifestacao.PEDIDO_ACESSO_INFORMACAO,
            status=StatusManifestacao.REGISTRADA,
            prioridade=Prioridade(dto.prioridade),
            assunto=dto.assunto,
            descricao=dto.descricao,
            cidadao=cidadao,
            canal=CanalRecebimento(dto.canal),
            orgao_destino=dto.orgao_destino,
            setor_responsavel=dto.setor_responsavel,
            prazo=prazo,
            anexos=anexos,
            informacao_solicitada=dto.informacao_solicitada,
            fundamentacao=dto.fundamentacao,
            nivel_sigilo=NivelSigilo(dto.nivel_sigilo),
            fundamentacao_sigilo=dto.fundamentacao_sigilo,
            dados_pessoais_terceiros=dto.dados_pessoais_terceiros,
            formato_resposta=dto.formato_resposta,
            created_by=dto.autor_id,
        )

        pedido.validar()
        self._validador.validar_criacao(pedido)  # noqa: F841 — validacao executada

        return self._repo.save(pedido)


class ResponderManifestacaoUseCase:
    """Registra resposta à manifestação/denúncia/pedido LAI."""

    def __init__(
        self,
        repo_m: RepositorioManifestacao,
        repo_d: RepositorioDenuncia,
        repo_l: RepositorioPedidoLai,
    ) -> None:
        self._repo_m = repo_m
        self._repo_d = repo_d
        self._repo_l = repo_l
        self._validador = ValidadorManifestacao()

    def execute(self, dto: ResponderManifestacaoInput):
        manifestacao = self._repo_m.get_by_id(dto.manifestacao_id)
        if manifestacao:
            self._validador.validar_resposta(manifestacao)
            manifestacao.registrar_resposta(
                dto.resposta, FormaResposta(dto.forma_resposta), dto.respondido_por
            )
            return self._repo_m.save(manifestacao)

        denuncia = self._repo_d.get_by_id(dto.manifestacao_id)
        if denuncia:
            self._validador.validar_resposta(denuncia)
            denuncia.registrar_resposta(
                dto.resposta, FormaResposta(dto.forma_resposta), dto.respondido_por
            )
            return self._repo_d.save(denuncia)

        pedido = self._repo_l.get_by_id(dto.manifestacao_id)
        if pedido:
            self._validador.validar_resposta(pedido)
            pedido.registrar_resposta(
                dto.resposta, FormaResposta(dto.forma_resposta), dto.respondido_por
            )
            return self._repo_l.save(pedido)

        raise ManifestacaoNaoEncontradaError(f"Manifestação {dto.manifestacao_id} não encontrada")


class AlterarStatusUseCase:
    """Altera status de manifestação/denúncia/pedido LAI (RN-OUV-010)."""

    def __init__(
        self,
        repo_m: RepositorioManifestacao,
        repo_d: RepositorioDenuncia,
        repo_l: RepositorioPedidoLai,
    ) -> None:
        self._repo_m = repo_m
        self._repo_d = repo_d
        self._repo_l = repo_l
        self._validador = ValidadorManifestacao()

    def execute(self, dto: AlterarStatusInput):
        novo_status = StatusManifestacao(dto.novo_status)

        manifestacao = self._repo_m.get_by_id(dto.manifestacao_id)
        if manifestacao:
            self._validador.validar_transicao_status(manifestacao.status, novo_status)
            manifestacao.alterar_status(novo_status, dto.usuario_id)
            return self._repo_m.save(manifestacao)

        denuncia = self._repo_d.get_by_id(dto.manifestacao_id)
        if denuncia:
            self._validador.validar_transicao_status(denuncia.status, novo_status)
            denuncia.alterar_status(novo_status, dto.usuario_id)
            return self._repo_d.save(denuncia)

        pedido = self._repo_l.get_by_id(dto.manifestacao_id)
        if pedido:
            self._validador.validar_transicao_status(pedido.status, novo_status)
            pedido.alterar_status(novo_status, dto.usuario_id)
            return self._repo_l.save(pedido)

        raise ManifestacaoNaoEncontradaError(f"Manifestação {dto.manifestacao_id} não encontrada")


class ProrrogarPrazoUseCase:
    """Prorroga prazo de resposta (LAI Art. 11 §1º, RN-OUV-020)."""

    def __init__(
        self,
        repo_m: RepositorioManifestacao,
        repo_d: RepositorioDenuncia,
        repo_l: RepositorioPedidoLai,
    ) -> None:
        self._repo_m = repo_m
        self._repo_d = repo_d
        self._repo_l = repo_l

    def execute(self, dto: ProrrogarPrazoInput):
        manifestacao = self._repo_m.get_by_id(dto.manifestacao_id)
        if manifestacao:
            manifestacao.prorrogar_prazo(dto.justificativa, dto.usuario_id)
            return self._repo_m.save(manifestacao)

        denuncia = self._repo_d.get_by_id(dto.manifestacao_id)
        if denuncia:
            denuncia.prorrogar_prazo(dto.justificativa, dto.usuario_id)
            return self._repo_d.save(denuncia)

        pedido = self._repo_l.get_by_id(dto.manifestacao_id)
        if pedido:
            pedido.prorrogar_prazo(dto.justificativa, dto.usuario_id)
            return self._repo_l.save(pedido)

        raise ManifestacaoNaoEncontradaError(f"Manifestação {dto.manifestacao_id} não encontrada")


class AvaliarManifestacaoUseCase:
    """Registra avaliação do cidadão (1-5)."""

    def __init__(self, repo: RepositorioManifestacao) -> None:
        self._repo = repo

    def execute(self, dto: AvaliarManifestacaoInput) -> Manifestacao:
        manifestacao = self._repo.get_by_id(dto.manifestacao_id)
        if not manifestacao:
            raise ManifestacaoNaoEncontradaError(
                f"Manifestação {dto.manifestacao_id} não encontrada"
            )
        manifestacao.avaliar(dto.nota, dto.comentario)
        return self._repo.save(manifestacao)


class EncaminharDenunciaUseCase:
    """Encaminha denúncia a órgão externo (MP, PF, TCE)."""

    def __init__(self, repo: RepositorioDenuncia) -> None:
        self._repo = repo

    def execute(self, dto: EncaminharDenunciaInput) -> Denuncia:
        denuncia = self._repo.get_by_id(dto.denuncia_id)
        if not denuncia:
            raise DenunciaNaoEncontradaError(f"Denúncia {dto.denuncia_id} não encontrada")
        ServicoEncaminhamento.encaminhar_denuncia(
            denuncia, dto.orgao, dto.numero_processo, dto.usuario_id
        )
        return self._repo.save(denuncia)


class InterporRecursoLaiUseCase:
    """Interpõe recurso de pedido LAI negado (LAI Art. 15)."""

    def __init__(self, repo: RepositorioPedidoLai) -> None:
        self._repo = repo

    def execute(self, dto: InterporRecursoLaiInput) -> PedidoLai:
        pedido_original = self._repo.get_by_id(dto.pedido_original_id)
        if not pedido_original:
            raise PedidoLaiNaoEncontradoError(
                f"Pedido original {dto.pedido_original_id} não encontrado"
            )
        if pedido_original.status != StatusManifestacao.ARQUIVADA:
            raise RegraNegocioError("Só é possível recorrer de pedidos arquivados/indeferidos")
        recurso = pedido_original.interpor_recurso(dto.pedido_original_id)
        return self._repo.save(recurso)


class DecidirRecursoLaiUseCase:
    """Decide sobre recurso LAI interposto."""

    def __init__(self, repo: RepositorioPedidoLai) -> None:
        self._repo = repo

    def execute(self, dto: DecidirRecursoLaiInput) -> PedidoLai:
        recurso = self._repo.get_by_id(dto.recurso_id)
        if not recurso:
            raise PedidoLaiNaoEncontradoError(f"Recurso {dto.recurso_id} não encontrado")
        if not recurso.is_recurso:
            raise RegraNegocioError("Este pedido não é um recurso")
        recurso.decidir_recurso(dto.deferido, dto.fundamentacao, dto.usuario_id)
        return self._repo.save(recurso)


class ListarManifestacoesUseCase:
    """Lista manifestações com paginação e filtros."""

    def __init__(self, repo: RepositorioManifestacao) -> None:
        self._repo = repo

    def execute(self, dto: ListarManifestacoesInput):
        items = self._repo.list_all(dto.page, dto.page_size, dto.filtros)
        total = self._repo.count_all(dto.filtros)
        return {
            "items": items,
            "total": total,
            "page": dto.page,
            "page_size": dto.page_size,
            "pages": (total + dto.page_size - 1) // dto.page_size,
        }


class ListarDenunciasUseCase:
    """Lista denúncias com paginação e filtros."""

    def __init__(self, repo: RepositorioDenuncia) -> None:
        self._repo = repo

    def execute(self, dto: ListarManifestacoesInput):
        items = self._repo.list_all(dto.page, dto.page_size, dto.filtros)
        total = self._repo.count_all(dto.filtros)
        return {
            "items": items,
            "total": total,
            "page": dto.page,
            "page_size": dto.page_size,
            "pages": (total + dto.page_size - 1) // dto.page_size,
        }


class ListarPedidosLaiUseCase:
    """Lista pedidos LAI com paginação e filtros."""

    def __init__(self, repo: RepositorioPedidoLai) -> None:
        self._repo = repo

    def execute(self, dto: ListarManifestacoesInput):
        items = self._repo.list_all(dto.page, dto.page_size, dto.filtros)
        total = self._repo.count_all(dto.filtros)
        return {
            "items": items,
            "total": total,
            "page": dto.page,
            "page_size": dto.page_size,
            "pages": (total + dto.page_size - 1) // dto.page_size,
        }


class ObterManifestacaoUseCase:
    """Obtém detalhes de uma manifestação/denúncia/pedido LAI por ID ou protocolo."""

    def __init__(
        self,
        repo_m: RepositorioManifestacao,
        repo_d: RepositorioDenuncia,
        repo_l: RepositorioPedidoLai,
    ) -> None:
        self._repo_m = repo_m
        self._repo_d = repo_d
        self._repo_l = repo_l

    def execute(
        self, identificador: str, usuario_perfil: str = "", usuario_autorizado: bool = False
    ):
        for repo in [self._repo_m, self._repo_d, self._repo_l]:
            resultado = repo.get_by_protocolo(identificador)
            if resultado:
                return resultado
        # Só consultar por id quando o identificador for um UUID válido (C1b):
        # os repositórios convertem direto via UUID() e lançariam ValueError
        # para um protocolo inexistente, gerando HTTP 500 em vez de 404.
        try:
            uuid_identificador = UUID(str(identificador))
        except (ValueError, AttributeError, TypeError):
            uuid_identificador = None
        if uuid_identificador is not None:
            identificador_uuid = str(uuid_identificador)
            for repo in [self._repo_m, self._repo_d, self._repo_l]:
                resultado = repo.get_by_id(identificador_uuid)
                if resultado:
                    return resultado
        raise ManifestacaoNaoEncontradaError(f"Manifestação {identificador} não encontrada")


class ObterEstatisticasUseCase:
    """Obtém estatísticas e indicadores da ouvidoria."""

    def __init__(self, servico: ServicoEstatisticas) -> None:
        self._servico = servico

    def execute(self, ano: int = None) -> dict:
        if ano is None:
            ano = date.today().year
        return {
            "gerais": self._servico.indicadores_gerais(ano),
            "por_tipo": self._servico.indicadores_por_tipo(ano),
            "vencendo_5_dias": len(self._servico.manifestacoes_vencendo_prazo(5)),
            "vencendo_10_dias": len(self._servico.manifestacoes_vencendo_prazo(10)),
        }


__all__ = [
    "RegistrarManifestacaoInput",
    "RegistrarDenunciaInput",
    "RegistrarPedidoLaiInput",
    "ResponderManifestacaoInput",
    "AlterarStatusInput",
    "ProrrogarPrazoInput",
    "AvaliarManifestacaoInput",
    "EncaminharDenunciaInput",
    "InterporRecursoLaiInput",
    "DecidirRecursoLaiInput",
    "ListarManifestacoesInput",
    "RegistrarManifestacaoUseCase",
    "RegistrarDenunciaUseCase",
    "RegistrarPedidoLaiUseCase",
    "ResponderManifestacaoUseCase",
    "AlterarStatusUseCase",
    "ProrrogarPrazoUseCase",
    "AvaliarManifestacaoUseCase",
    "EncaminharDenunciaUseCase",
    "InterporRecursoLaiUseCase",
    "DecidirRecursoLaiUseCase",
    "ListarManifestacoesUseCase",
    "ListarDenunciasUseCase",
    "ListarPedidosLaiUseCase",
    "ObterManifestacaoUseCase",
    "ObterEstatisticasUseCase",
]
