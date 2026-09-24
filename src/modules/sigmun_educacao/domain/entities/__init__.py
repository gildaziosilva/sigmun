"""Agregador de entidades do DOM-EDU."""

from .aluno import Aluno, Sexo, StatusAluno
from .diario import LancamentoDiario
from .matricula import Matricula, StatusMatricula
from .merenda import DistribuicaoMerenda, ItemMerenda
from .transporte import PassagemTransporte, RotaTransporte, StatusRota

__all__ = [
    "Aluno",
    "Sexo",
    "StatusAluno",
    "Matricula",
    "StatusMatricula",
    "LancamentoDiario",
    "RotaTransporte",
    "StatusRota",
    "PassagemTransporte",
    "ItemMerenda",
    "DistribuicaoMerenda",
]
