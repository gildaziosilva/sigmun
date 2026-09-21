"""Use cases do DOM-TRI — Administração Tributária."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from uuid import uuid4

from . import interfaces as ports
from ..domain.entities.certidao import Certidao, TipoCertidao
from ..domain.entities.contribuinte import (
    Contribuinte,
    TipoContribuinte,
)
from ..domain.entities.divida_ativa import (
    InscricaoDividaAtiva,
)
from ..domain.entities.imovel import Imovel
from ..domain.entities.lancamento import (
    Lancamento,
    TipoTributo,
)


def _gerar_numero(prefixo: str, exercicio: int) -> str:
    """Gera um número de lançamento/praças padrão com sufixo aleatório."""
    return f"{exercicio}{prefixo}{uuid4().hex[:6].upper()}"


@dataclass
class CadastrarContribuinteInput:
    """DTO de cadastro de contribuinte."""

    tipo: str
    nome: str
    cpf_cnpj: str
    inscricao_municipal: str = ""
    email: str = ""
    telefone: str = ""
    endereco: str = ""
    autor_id: str = ""


class CadastrarContribuinteUseCase:
    """Cadastra um contribuinte (RN-TRI-001/002)."""

    def __init__(self, repo: ports.RepositorioContribuinte) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarContribuinteInput) -> Contribuinte:
        """Executa o cadastro."""
        from ..domain.exceptions import (
            ContribuinteJaExistenteError,
            RegraNegocioError,
        )

        if not dto.nome or not dto.cpf_cnpj:
            raise RegraNegocioError(
                "Nome e CPF/CNPJ são obrigatórios no cadastro (RN-TRI-001)"
            )
        if self._repo.get_by_cpf_cnpj(dto.cpf_cnpj) is not None:
            raise ContribuinteJaExistenteError(
                "CPF/CNPJ já cadastrado como contribuinte (RN-TRI-001)"
            )
        contribuinte = Contribuinte(
            tipo=TipoContribuinte(dto.tipo),
            nome=dto.nome,
            cpf_cnpj=dto.cpf_cnpj,
            inscricao_municipal=dto.inscricao_municipal,
            email=dto.email,
            telefone=dto.telefone,
            endereco=dto.endereco,
            created_by=dto.autor_id,
        )
        contribuinte.validar()
        return self._repo.save(contribuinte)


@dataclass
class CadastrarImovelInput:
    """DTO de cadastro de imóvel (IPTU)."""

    contribuinte_id: str
    inscricao_imobiliaria: str
    logradouro: str = ""
    numero: str = ""
    bairro: str = ""
    cidade: str = ""
    uf: str = ""
    cep: str = ""
    area_terreno: float = 0.0
    area_construida: float = 0.0
    valor_venal: float = 0.0
    aliquota: float = 0.0
    autor_id: str = ""


class CadastrarImovelUseCase:
    """Cadastra um imóvel para IPTU (RN-TRI-010/011)."""

    def __init__(
        self,
        repo: ports.RepositorioImovel,
        contribuintes: ports.RepositorioContribuinte,
    ) -> None:
        self._repo = repo
        self._contribuintes = contribuintes

    def execute(self, dto: CadastrarImovelInput) -> Imovel:
        """Executa o cadastro."""
        from ..domain.exceptions import (
            ContribuinteNaoEncontradoError,
            ImovelJaExistenteError,
            RegraNegocioError,
        )

        if self._contribuintes.get_by_id(dto.contribuinte_id) is None:
            raise ContribuinteNaoEncontradoError(
                "Contribuinte não encontrado para vinculação do imóvel"
            )
        if self._repo.get_by_inscricao(dto.inscricao_imobiliaria) is not None:
            raise ImovelJaExistenteError(
                "Inscrição imobiliária já cadastrada (RN-TRI-010)"
            )
        if dto.valor_venal <= 0:
            raise RegraNegocioError("Valor venal deve ser maior que zero (RN-TRI-011)")
        imovel = Imovel(
            contribuinte_id=dto.contribuinte_id,
            inscricao_imobiliaria=dto.inscricao_imobiliaria,
            logradouro=dto.logradouro,
            numero=dto.numero,
            bairro=dto.bairro,
            cidade=dto.cidade,
            uf=dto.uf,
            cep=dto.cep,
            area_terreno=dto.area_terreno,
            area_construida=dto.area_construida,
            valor_venal=dto.valor_venal,
            aliquota=dto.aliquota,
            created_by=dto.autor_id,
        )
        imovel.validar()
        return self._repo.save(imovel)


@dataclass
class LancarTributoInput:
    """DTO de lançamento de crédito tributário."""

    contribuinte_id: str
    tipo_tributo: str
    exercicio: int
    base_calculo: float
    aliquota: float = 0.0
    imovel_id: str = ""
    descricao: str = ""
    juros: float = 0.0
    multa: float = 0.0
    data_vencimento: date | None = None
    autor_id: str = ""


class LancarTributoUseCase:
    """Constitui um crédito tributário (RN-TRI-020/021).

    Para IPTU o valor é derivado do imóvel (valor_venal × alíquota); para os
    demais tributos a base de cálculo e a alíquota são informadas.
    """

    def __init__(
        self,
        repo: ports.RepositorioLancamento,
        contribuintes: ports.RepositorioContribuinte,
        imoveis: ports.RepositorioImovel,
    ) -> None:
        self._repo = repo
        self._contribuintes = contribuintes
        self._imoveis = imoveis

    def execute(self, dto: LancarTributoInput) -> Lancamento:
        """Executa o lançamento."""
        from ..domain.exceptions import (
            ContribuinteNaoEncontradoError,
            ImovelNaoEncontradoError,
            RegraNegocioError,
        )

        cont = self._contribuintes.get_by_id(dto.contribuinte_id)
        if cont is None:
            raise ContribuinteNaoEncontradoError(
                "Contribuinte não encontrado para lançamento"
            )
        tipo = TipoTributo(dto.tipo_tributo)
        base = dto.base_calculo
        aliquota = dto.aliquota

        if tipo == TipoTributo.IPTU:
            if not dto.imovel_id:
                raise RegraNegocioError("Lançamento de IPTU exige imóvel")
            imovel = self._imoveis.get_by_id(dto.imovel_id)
            if imovel is None:
                raise ImovelNaoEncontradoError(
                    "Imóvel não encontrado para lançamento de IPTU"
                )
            if imovel.contribuinte_id != dto.contribuinte_id:
                raise RegraNegocioError(
                    "Imóvel não pertence ao contribuinte do lançamento"
                )
            base = imovel.valor_venal
            aliquota = imovel.aliquota

        if base is None or base <= 0:
            raise RegraNegocioError("Base de cálculo deve ser maior que zero")
        valor_tributo = round(float(base) * float(aliquota), 2)
        lance = Lancamento(
            contribuinte_id=dto.contribuinte_id,
            imovel_id=dto.imovel_id,
            tipo_tributo=tipo,
            exercicio=dto.exercicio,
            numero_lancamento=_gerar_numero(tipo.value.upper(), dto.exercicio),
            descricao=dto.descricao,
            base_calculo=float(base),
            aliquota=aliquota,
            valor_tributo=valor_tributo,
            juros=round(dto.juros, 2),
            multa=round(dto.multa, 2),
            data_vencimento=dto.data_vencimento,
            created_by=dto.autor_id,
        )
        lance.validar()
        lance.recalcular_total()
        return self._repo.save(lance)
class PagarLancamentoUseCase:
    """Quita integralmente um lançamento (RN-TRI-022)."""

    def __init__(self, repo: ports.RepositorioLancamento) -> None:
        self._repo = repo

    def execute(self, lancamento_id: str, data_pagamento: date | None = None) -> Lancamento:
        """Executa o pagamento."""
        from ..domain.exceptions import LancamentoNaoEncontradoError

        lance = self._repo.get_by_id(lancamento_id)
        if lance is None:
            raise LancamentoNaoEncontradoError("Lançamento não encontrado")
        lance.registrar_pagamento(data_pagamento)
        return self._repo.save(lance)


class InscreverDividaAtivaUseCase:
    """Inscreve crédito vencido em dívida ativa (RN-TRI-030/031)."""

    def __init__(
        self,
        repo: ports.RepositorioDividaAtiva,
        lancamentos: ports.RepositorioLancamento,
    ) -> None:
        self._repo = repo
        self._lancamentos = lancamentos

    def execute(self, lancamento_id: str, autor_id: str = "") -> InscricaoDividaAtiva:
        """Executa a inscrição."""
        from ..domain.exceptions import (
            LancamentoNaoEncontradoError,
            RegraNegocioError,
        )

        lance = self._lancamentos.get_by_id(lancamento_id)
        if lance is None:
            raise LancamentoNaoEncontradoError(
                "Lançamento não encontrado para inscrição"
            )
        if not lance.data_vencimento or lance.data_vencimento > date.today():
            raise RegraNegocioError(
                "Somente créditos vencidos podem ser inscritos em dívida ativa"
            )
        lance.inscrever_em_divida_ativa()
        self._lancamentos.save(lance)
        inscricao = InscricaoDividaAtiva(
            lancamento_id=lance.id,
            numero_inscricao=f"DA-{lance.exercicio}{uuid4().hex[:6].upper()}",
            data_inscricao=date.today(),
            valor_original=lance.valor_total,
            valor_atualizado=lance.valor_total,
            created_by=autor_id,
        )
        inscricao.validar()
        return self._repo.save(inscricao)
class BaixarDividaAtivaUseCase:
    """Baixa uma inscrição de dívida ativa."""

    def __init__(self, repo: ports.RepositorioDividaAtiva) -> None:
        self._repo = repo

    def execute(self, inscricao_id: str) -> InscricaoDividaAtiva:
        """Executa a baixa."""
        from ..domain.exceptions import DividaAtivaNaoEncontradaError

        inscricao = self._repo.get_by_id(inscricao_id)
        if inscricao is None:
            raise DividaAtivaNaoEncontradaError(
                "Inscrição de dívida ativa não encontrada"
            )
        inscricao.baixar()
        return self._repo.save(inscricao)


class EmitirCertidaoUseCase:
    """Emite certidão de regularidade fiscal (RN-TRI-040/041)."""

    def __init__(
        self,
        repo: ports.RepositorioCertidao,
        lancamentos: ports.RepositorioLancamento,
        contribuintes: ports.RepositorioContribuinte,
    ) -> None:
        self._repo = repo
        self._lancamentos = lancamentos
        self._contribuintes = contribuintes

    def execute(self, contribuinte_id: str, autor_id: str = "") -> Certidao:
        """Executa a emissão."""
        from ..domain.exceptions import ContribuinteNaoEncontradoError

        if self._contribuintes.get_by_id(contribuinte_id) is None:
            raise ContribuinteNaoEncontradoError(
                "Contribuinte não encontrado para emissão de certidão"
            )
        devedor = self._lancamentos.list_abertos_por_contribuinte(contribuinte_id)
        tipo = TipoCertidao.POSITIVA if devedor else TipoCertidao.NEGATIVA
        hoje = date.today()
        certidao = Certidao(
            contribuinte_id=contribuinte_id,
            tipo=tipo,
            numero=f"CERT{uuid4().hex[:10].upper()}",
            data_emissao=hoje,
            valido_ate=hoje + timedelta(days=90),
            observacao=(
                "Contribuinte sem débitos vencidos (RN-TRI-040)"
                if tipo == TipoCertidao.NEGATIVA
                else "Contribuinte com débitos vencidos (RN-TRI-041)"
            ),
            created_by=autor_id,
        )
        certidao.validar()
        return self._repo.save(certidao)


__all__ = [
    "CadastrarContribuinteInput",
    "CadastrarContribuinteUseCase",
    "CadastrarImovelInput",
    "CadastrarImovelUseCase",
    "LancarTributoInput",
    "LancarTributoUseCase",
    "PagarLancamentoUseCase",
    "InscreverDividaAtivaUseCase",
    "BaixarDividaAtivaUseCase",
    "EmitirCertidaoUseCase",
]