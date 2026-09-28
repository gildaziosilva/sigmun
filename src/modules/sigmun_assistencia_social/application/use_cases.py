"""Use cases do DOM-ASS - Assistência Social."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from . import interfaces as ports
from ..domain.entities import (
    AtendimentoSocial,
    BeneficioEventual,
    FamiliaCadUnico,
    PessoaCadUnico,
    Sexo,
    StatusFamilia,
    StatusUnidade,
    TipoAtendimento,
    TipoBeneficio,
    TipoUnidade,
    UnidadeAssistencia,
)


@dataclass
class CadastrarFamiliaInput:
    """DTO de cadastro de família no CadÚnico."""

    nis: str
    responsavel_nome: str
    responsavel_cpf: str
    endereco: str
    telefone: str
    renda_per_capita: float = 0.0
    quantidade_pessoas: int = 0
    autor_id: str = ""


class CadastrarFamiliaUseCase:
    """Cadastra uma família no CadÚnico (RN-ASS-001)."""

    def __init__(self, repo: ports.RepositorioFamilia) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarFamiliaInput) -> FamiliaCadUnico:
        """Executa o cadastro."""
        from ..domain.exceptions import FamiliaJaExistenteError, RegraNegocioError

        if not dto.nis or not dto.responsavel_nome:
            raise RegraNegocioError("NIS e nome do responsável são obrigatórios (RN-ASS-001)")
        if self._repo.get_by_nis(dto.nis) is not None:
            raise FamiliaJaExistenteError("NIS já cadastrado (RN-ASS-001)")
        familia = FamiliaCadUnico(
            nis=dto.nis,
            responsavel_nome=dto.responsavel_nome,
            responsavel_cpf=dto.responsavel_cpf,
            endereco=dto.endereco,
            telefone=dto.telefone,
            renda_per_capita=dto.renda_per_capita,
            quantidade_pessoas=dto.quantidade_pessoas,
            created_by=dto.autor_id,
        )
        familia.validar()
        return self._repo.save(familia)


@dataclass
class CadastrarPessoaInput:
    """DTO de cadastro de pessoa no CadÚnico."""

    familia_id: str
    nome: str
    cpf: str
    data_nascimento: str = ""
    sexo: str = "ignorado"
    nome_mae: str = ""
    parentesco: str = ""
    escolaridade: str = ""
    ocupacao: str = ""
    renda: float = 0.0
    autor_id: str = ""


class CadastrarPessoaUseCase:
    """Cadastra uma pessoa no CadÚnico (RN-ASS-002)."""

    def __init__(self, repo: ports.RepositorioPessoa, familias: ports.RepositorioFamilia) -> None:
        self._repo = repo
        self._familias = familias

    def execute(self, dto: CadastrarPessoaInput) -> PessoaCadUnico:
        """Executa o cadastro."""
        from ..domain.exceptions import PessoaJaExistenteError, RegraNegocioError, FamiliaNaoEncontradaError

        if not dto.nome or not dto.cpf:
            raise RegraNegocioError("Nome e CPF são obrigatórios (RN-ASS-002)")
        if self._repo.get_by_cpf(dto.cpf) is not None:
            raise PessoaJaExistenteError("CPF já cadastrado (RN-ASS-002)")
        if self._familias.get_by_id(dto.familia_id) is None:
            raise FamiliaNaoEncontradaError("Família não encontrada para cadastro da pessoa")
        pessoa = PessoaCadUnico(
            familia_id=dto.familia_id,
            nome=dto.nome,
            cpf=dto.cpf,
            data_nascimento=dto.data_nascimento,
            sexo=Sexo(dto.sexo),
            nome_mae=dto.nome_mae,
            parentesco=dto.parentesco,
            escolaridade=dto.escolaridade,
            ocupacao=dto.ocupacao,
            renda=dto.renda,
            created_by=dto.autor_id,
        )
        pessoa.validar()
        return self._repo.save(pessoa)


@dataclass
class CadastrarUnidadeInput:
    """DTO de cadastro de unidade CRAS/CREAS."""

    codigo: str
    nome: str
    tipo: str = "cras"
    endereco: str = ""
    telefone: str = ""
    email: str = ""
    responsavel: str = ""
    autor_id: str = ""


class CadastrarUnidadeUseCase:
    """Cadastra uma unidade de assistência social."""

    def __init__(self, repo: ports.RepositorioUnidade) -> None:
        self._repo = repo

    def execute(self, dto: CadastrarUnidadeInput) -> UnidadeAssistencia:
        """Executa o cadastro."""
        from ..domain.exceptions import RegraNegocioError

        if not dto.codigo or not dto.nome:
            raise RegraNegocioError("Código e nome da unidade são obrigatórios")
        unidade = UnidadeAssistencia(
            codigo=dto.codigo,
            nome=dto.nome,
            tipo=TipoUnidade(dto.tipo),
            endereco=dto.endereco,
            telefone=dto.telefone,
            email=dto.email,
            responsavel=dto.responsavel,
            created_by=dto.autor_id,
        )
        unidade.validar()
        return self._repo.save(unidade)


@dataclass
class SolicitarBeneficioInput:
    """DTO de solicitação de benefício eventual."""

    familia_id: str
    tipo: str = "alimentacao"
    descricao: str = ""
    valor: float = 0.0
    quantidade: int = 1
    unidade_id: str = ""
    observacao: str = ""
    autor_id: str = ""


class SolicitarBeneficioUseCase:
    """Solicita um benefício eventual (RN-ASS-003)."""

    def __init__(
        self,
        beneficios: ports.RepositorioBeneficio,
        familias: ports.RepositorioFamilia,
        unidades: ports.RepositorioUnidade,
    ) -> None:
        self._beneficios = beneficios
        self._familias = familias
        self._unidades = unidades

    def execute(self, dto: SolicitarBeneficioInput) -> BeneficioEventual:
        """Executa a solicitação."""
        from ..domain.exceptions import FamiliaNaoEncontradaError, UnidadeNaoEncontradaError

        if self._familias.get_by_id(dto.familia_id) is None:
            raise FamiliaNaoEncontradaError("Família não encontrada para benefício")
        if dto.unidade_id and self._unidades.get_by_id(dto.unidade_id) is None:
            raise UnidadeNaoEncontradaError("Unidade não encontrada")
        beneficio = BeneficioEventual(
            familia_id=dto.familia_id,
            tipo=TipoBeneficio(dto.tipo),
            descricao=dto.descricao,
            valor=dto.valor,
            quantidade=dto.quantidade,
            unidade_id=dto.unidade_id,
            observacao=dto.observacao,
            created_by=dto.autor_id,
        )
        beneficio.validar()
        return self._beneficios.save(beneficio)


class AprovarBeneficioUseCase:
    """Aprova um benefício eventual."""

    def __init__(self, repo: ports.RepositorioBeneficio) -> None:
        self._repo = repo

    def execute(self, beneficio_id: str) -> BeneficioEventual:
        """Executa a aprovação."""
        from ..domain.exceptions import BeneficioNaoEncontradoError

        beneficio = self._repo.get_by_id(beneficio_id)
        if beneficio is None:
            raise BeneficioNaoEncontradoError("Benefício não encontrado")
        beneficio.aprovar("")
        return self._repo.save(beneficio)


class NegarBeneficioUseCase:
    """Nega um benefício eventual."""

    def __init__(self, repo: ports.RepositorioBeneficio) -> None:
        self._repo = repo

    def execute(self, beneficio_id: str, justificativa: str) -> BeneficioEventual:
        """Executa a negativa."""
        from ..domain.exceptions import BeneficioNaoEncontradoError

        beneficio = self._repo.get_by_id(beneficio_id)
        if beneficio is None:
            raise BeneficioNaoEncontradoError("Benefício não encontrado")
        beneficio.negar("", justificativa)
        return self._repo.save(beneficio)


class EntregarBeneficioUseCase:
    """Registra entrega de benefício eventual."""

    def __init__(self, repo: ports.RepositorioBeneficio) -> None:
        self._repo = repo

    def execute(self, beneficio_id: str) -> BeneficioEventual:
        """Executa a entrega."""
        from ..domain.exceptions import BeneficioNaoEncontradoError

        beneficio = self._repo.get_by_id(beneficio_id)
        if beneficio is None:
            raise BeneficioNaoEncontradoError("Benefício não encontrado")
        beneficio.entregar("")
        return self._repo.save(beneficio)


class CancelarBeneficioUseCase:
    """Cancela um benefício eventual."""

    def __init__(self, repo: ports.RepositorioBeneficio) -> None:
        self._repo = repo

    def execute(self, beneficio_id: str) -> BeneficioEventual:
        """Executa o cancelamento."""
        from ..domain.exceptions import BeneficioNaoEncontradoError

        beneficio = self._repo.get_by_id(beneficio_id)
        if beneficio is None:
            raise BeneficioNaoEncontradoError("Benefício não encontrado")
        beneficio.cancelar("")
        return self._repo.save(beneficio)


@dataclass
class RegistrarAtendimentoInput:
    """DTO de registro de atendimento social."""

    pessoa_id: str
    unidade_id: str
    tipo: str = "acolhimento"
    data: date | None = None
    descricao: str = ""
    encaminhamento: str = ""
    profissional: str = ""
    autor_id: str = ""


class RegistrarAtendimentoUseCase:
    """Registra atendimento social (RN-ASS-004)."""

    def __init__(
        self,
        atendimentos: ports.RepositorioAtendimento,
        pessoas: ports.RepositorioPessoa,
        unidades: ports.RepositorioUnidade,
    ) -> None:
        self._atendimentos = atendimentos
        self._pessoas = pessoas
        self._unidades = unidades

    def execute(self, dto: RegistrarAtendimentoInput) -> AtendimentoSocial:
        """Executa o registro."""
        from ..domain.exceptions import PessoaNaoEncontradaError, UnidadeNaoEncontradaError

        if self._pessoas.get_by_id(dto.pessoa_id) is None:
            raise PessoaNaoEncontradaError("Pessoa não encontrada para atendimento")
        if self._unidades.get_by_id(dto.unidade_id) is None:
            raise UnidadeNaoEncontradaError("Unidade não encontrada para atendimento")
        atendimento = AtendimentoSocial(
            pessoa_id=dto.pessoa_id,
            unidade_id=dto.unidade_id,
            tipo=TipoAtendimento(dto.tipo),
            data=dto.data or datetime.utcnow(),
            descricao=dto.descricao,
            encaminhamento=dto.encaminhamento,
            profissional=dto.profissional,
            created_by=dto.autor_id,
        )
        atendimento.validar()
        return self._atendimentos.save(atendimento)



@dataclass
class AtualizarFamiliaInput:
    """DTO de atualização cadastral da família (campos opcionais)."""

    familia_id: str
    nis: str | None = None
    responsavel_nome: str | None = None
    responsavel_cpf: str | None = None
    endereco: str | None = None
    telefone: str | None = None
    renda_per_capita: float | None = None
    quantidade_pessoas: int | None = None
    status: str | None = None
    autor_id: str = ""


class AtualizarFamiliaUseCase:
    """Atualiza o cadastro de uma família do CadÚnico.

    Regras aplicadas (RN-ASS-001):
    - o NIS permanece único no cadastro municipal;
    - a família precisa existir e estar ativa para ser atualizada.
    """

    def __init__(self, repo: ports.RepositorioFamilia) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarFamiliaInput) -> FamiliaCadUnico:
        """Executa a atualização."""
        from ..domain.exceptions import FamiliaJaExistenteError, FamiliaNaoEncontradaError, RegraNegocioError

        familia = self._repo.get_by_id(dto.familia_id)
        if familia is None:
            raise FamiliaNaoEncontradaError("Família não encontrada para atualização")

        if dto.nis is not None and dto.nis != familia.nis:
            outra = self._repo.get_by_nis(dto.nis)
            if outra is not None and outra.id != familia.id:
                raise FamiliaJaExistenteError("NIS já cadastrado (RN-ASS-001)")
            familia.nis = dto.nis

        if dto.responsavel_nome is not None:
            familia.responsavel_nome = dto.responsavel_nome
        if dto.responsavel_cpf is not None:
            familia.responsavel_cpf = dto.responsavel_cpf
        if dto.endereco is not None:
            familia.endereco = dto.endereco
        if dto.telefone is not None:
            familia.telefone = dto.telefone
        if dto.renda_per_capita is not None:
            if dto.renda_per_capita < 0:
                raise RegraNegocioError("Renda per capita não pode ser negativa")
            familia.atualizar_renda(dto.renda_per_capita)
        if dto.quantidade_pessoas is not None:
            if dto.quantidade_pessoas < 0:
                raise RegraNegocioError("Quantidade de pessoas não pode ser negativa")
            familia.quantidade_pessoas = dto.quantidade_pessoas
        if dto.status is not None:
            if dto.status == StatusFamilia.ATIVA.value:
                familia.status = StatusFamilia.ATIVA
            elif dto.status == StatusFamilia.INATIVA.value:
                familia.inativar()
            else:
                raise RegraNegocioError(
                    f"Status inválido para família: {dto.status}"
                )

        familia.validar()
        familia.updated_at = datetime.utcnow()
        return self._repo.save(familia)


class ExcluirFamiliaUseCase:
    """Exclui (soft-delete) uma família do CadÚnico."""

    def __init__(self, repo: ports.RepositorioFamilia) -> None:
        self._repo = repo

    def execute(self, familia_id: str) -> FamiliaCadUnico:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import FamiliaNaoEncontradaError

        familia = self._repo.get_by_id(familia_id)
        if familia is None:
            raise FamiliaNaoEncontradaError("Família não encontrada para exclusão")
        familia.excluir()
        return self._repo.save(familia)



@dataclass
class AtualizarPessoaInput:
    """DTO de atualização cadastral da pessoa (campos opcionais)."""

    pessoa_id: str
    familia_id: str | None = None
    nome: str | None = None
    cpf: str | None = None
    data_nascimento: str | None = None
    sexo: str | None = None
    nome_mae: str | None = None
    parentesco: str | None = None
    escolaridade: str | None = None
    ocupacao: str | None = None
    renda: float | None = None
    autor_id: str = ""


class AtualizarPessoaUseCase:
    """Atualiza o cadastro de uma pessoa do CadÚnico.

    Regras aplicadas (RN-ASS-002):
    - o CPF permanece único no cadastro municipal;
    - a pessoa precisa existir e estar vinculada a uma família válida.
    """

    def __init__(
        self, repo: ports.RepositorioPessoa, familias: ports.RepositorioFamilia
    ) -> None:
        self._repo = repo
        self._familias = familias

    def execute(self, dto: AtualizarPessoaInput) -> PessoaCadUnico:
        """Executa a atualização."""
        from ..domain.exceptions import (
            FamiliaNaoEncontradaError,
            PessoaJaExistenteError,
            PessoaNaoEncontradaError,
            RegraNegocioError,
        )

        pessoa = self._repo.get_by_id(dto.pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradaError("Pessoa não encontrada para atualização")

        if dto.cpf is not None and dto.cpf != pessoa.cpf:
            outra = self._repo.get_by_cpf(dto.cpf)
            if outra is not None and outra.id != pessoa.id:
                raise PessoaJaExistenteError("CPF já cadastrado (RN-ASS-002)")
            pessoa.cpf = dto.cpf

        if dto.familia_id is not None and dto.familia_id != pessoa.familia_id:
            if self._familias.get_by_id(dto.familia_id) is None:
                raise FamiliaNaoEncontradaError(
                    "Família não encontrada para vínculo da pessoa"
                )
            pessoa.familia_id = dto.familia_id

        if dto.nome is not None:
            pessoa.nome = dto.nome
        if dto.data_nascimento is not None:
            pessoa.data_nascimento = dto.data_nascimento
        if dto.sexo is not None:
            try:
                pessoa.sexo = Sexo(dto.sexo)
            except ValueError as exc:
                raise RegraNegocioError(f"Sexo inválido: {dto.sexo}") from exc
        if dto.nome_mae is not None:
            pessoa.nome_mae = dto.nome_mae
        if dto.parentesco is not None:
            pessoa.parentesco = dto.parentesco
        if dto.escolaridade is not None:
            pessoa.escolaridade = dto.escolaridade
        if dto.ocupacao is not None:
            pessoa.ocupacao = dto.ocupacao
        if dto.renda is not None:
            if dto.renda < 0:
                raise RegraNegocioError("Renda não pode ser negativa")
            pessoa.renda = dto.renda

        pessoa.validar()
        pessoa.updated_at = datetime.utcnow()
        return self._repo.save(pessoa)


class ExcluirPessoaUseCase:
    """Exclui (soft-delete) uma pessoa do CadÚnico."""

    def __init__(self, repo: ports.RepositorioPessoa) -> None:
        self._repo = repo

    def execute(self, pessoa_id: str) -> PessoaCadUnico:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import PessoaNaoEncontradaError

        pessoa = self._repo.get_by_id(pessoa_id)
        if pessoa is None:
            raise PessoaNaoEncontradaError("Pessoa não encontrada para exclusão")
        pessoa.excluir()
        return self._repo.save(pessoa)



@dataclass
class AtualizarUnidadeInput:
    """DTO de atualização cadastral da unidade (campos opcionais)."""

    unidade_id: str
    codigo: str | None = None
    nome: str | None = None
    tipo: str | None = None
    endereco: str | None = None
    telefone: str | None = None
    email: str | None = None
    responsavel: str | None = None
    status: str | None = None
    autor_id: str = ""


class AtualizarUnidadeUseCase:
    """Atualiza o cadastro de uma unidade de assistência social."""

    def __init__(self, repo: ports.RepositorioUnidade) -> None:
        self._repo = repo

    def execute(self, dto: AtualizarUnidadeInput) -> UnidadeAssistencia:
        """Executa a atualização."""
        from ..domain.exceptions import RegraNegocioError, UnidadeNaoEncontradaError

        unidade = self._repo.get_by_id(dto.unidade_id)
        if unidade is None:
            raise UnidadeNaoEncontradaError("Unidade não encontrada para atualização")

        if dto.codigo is not None and dto.codigo != unidade.codigo:
            outra = self._repo.get_by_codigo(dto.codigo)
            if outra is not None and outra.id != unidade.id:
                raise RegraNegocioError("Código de unidade já cadastrado")
            unidade.codigo = dto.codigo
        if dto.nome is not None:
            unidade.nome = dto.nome
        if dto.tipo is not None:
            try:
                unidade.tipo = TipoUnidade(dto.tipo)
            except ValueError as exc:
                raise RegraNegocioError(f"Tipo de unidade inválido: {dto.tipo}") from exc
        if dto.endereco is not None:
            unidade.endereco = dto.endereco
        if dto.telefone is not None:
            unidade.telefone = dto.telefone
        if dto.email is not None:
            unidade.email = dto.email
        if dto.responsavel is not None:
            unidade.responsavel = dto.responsavel
        if dto.status is not None:
            if dto.status == StatusUnidade.ATIVA.value:
                unidade.status = StatusUnidade.ATIVA
            elif dto.status == StatusUnidade.INATIVA.value:
                unidade.inativar()
            else:
                raise RegraNegocioError(
                    f"Status inválido para unidade: {dto.status}"
                )

        unidade.validar()
        unidade.updated_at = datetime.utcnow()
        return self._repo.save(unidade)


class ExcluirUnidadeUseCase:
    """Exclui (soft-delete) uma unidade de assistência social."""

    def __init__(self, repo: ports.RepositorioUnidade) -> None:
        self._repo = repo

    def execute(self, unidade_id: str) -> UnidadeAssistencia:
        """Executa a exclusão lógica."""
        from ..domain.exceptions import UnidadeNaoEncontradaError

        unidade = self._repo.get_by_id(unidade_id)
        if unidade is None:
            raise UnidadeNaoEncontradaError("Unidade não encontrada para exclusão")
        unidade.excluir()
        return self._repo.save(unidade)


__all__ = [
    "CadastrarFamiliaInput",
    "CadastrarFamiliaUseCase",
    "CadastrarPessoaInput",
    "CadastrarPessoaUseCase",
    "CadastrarUnidadeInput",
    "CadastrarUnidadeUseCase",
    "AtualizarFamiliaInput",
    "AtualizarFamiliaUseCase",
    "ExcluirFamiliaUseCase",
    "AtualizarPessoaInput",
    "AtualizarPessoaUseCase",
    "ExcluirPessoaUseCase",
    "AtualizarUnidadeInput",
    "AtualizarUnidadeUseCase",
    "ExcluirUnidadeUseCase",
    "SolicitarBeneficioInput",
    "SolicitarBeneficioUseCase",
    "AprovarBeneficioUseCase",
    "NegarBeneficioUseCase",
    "EntregarBeneficioUseCase",
    "CancelarBeneficioUseCase",
    "RegistrarAtendimentoInput",
    "RegistrarAtendimentoUseCase",
]
