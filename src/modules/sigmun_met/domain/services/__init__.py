"""Serviços de domínio do módulo de Metadados Corporativos."""

import logging

from src.modules.sigmun_met.domain.entities import (
    Metadado,
    Taxonomia,
    TermoTaxonomia,
    TipoDadoMetadado,
)
from src.modules.sigmun_met.domain.exceptions import (
    HierarquiaCiclicaError,
    TermoJaExisteError,
    ValorMetadadoInvalidoError,
)

logger = logging.getLogger(__name__)


class MetadadoService:
    """Serviço de metadados: validação de valores conforme tipo de dado."""

    @staticmethod
    def validar_valor(metadado: Metadado, valor: str) -> bool:
        """Valida se o valor é compatível com o tipo de dado do metadado."""
        if metadado.tipo_dado == TipoDadoMetadado.NUMERO:
            try:
                float(valor.replace(",", "."))
                return True
            except (ValueError, AttributeError):
                return False
        if metadado.tipo_dado == TipoDadoMetadado.DATA:
            from datetime import datetime
            for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S"):
                try:
                    datetime.strptime(valor, fmt)
                    return True
                except (ValueError, TypeError):
                    continue
            return False
        if metadado.tipo_dado == TipoDadoMetadado.BOOLEANO:
            return str(valor).strip().lower() in ("true", "false", "sim", "nao", "não", "1", "0")
        if metadado.tipo_dado == TipoDadoMetadado.LISTA:
            return "," in valor or bool(valor)
        if metadado.tipo_dado == TipoDadoMetadado.JSON:
            import json
            try:
                json.loads(valor)
                return True
            except (ValueError, TypeError):
                return False
        # TEXTO e demais tipos: apenas não vazio
        return bool(valor and valor.strip())

    @staticmethod
    def validar_e_levantar(metadado: Metadado, valor: str) -> None:
        """Valida valor e levanta exceção de domínio se inválido."""
        if not MetadadoService.validar_valor(metadado, valor):
            raise ValorMetadadoInvalidoError(
                f"Valor '{valor}' inválido para o metadado '{metadado.codigo}' "
                f"do tipo '{metadado.tipo_dado.value}'"
            )

    @staticmethod
    def validar_entidade_aplicavel(metadado: Metadado, entidade_tipo: str) -> bool:
        """Verifica se o metadado é aplicável ao tipo de entidade."""
        if not metadado.aplicavel_a:
            return True
        return entidade_tipo in metadado.aplicavel_a

    @staticmethod
    def validar_codigo_unico(metadados: list[Metadado], codigo: str, exclude_id: str = "") -> bool:
        """Valida se código do metadado é único."""
        for metadado in metadados:
            if metadado.codigo.lower() == codigo.lower() and metadado.id != exclude_id:
                return False
        return True


class TaxonomiaService:
    """Serviço de taxonomias: gestão da hierarquia de termos."""

    @staticmethod
    def validar_hierarquia(termos: list[TermoTaxonomia], termo_pai_id: str, termo_id: str) -> None:
        """Valida que associar termo_id sob termo_pai_id não cria ciclo."""
        if termo_pai_id == termo_id:
            raise HierarquiaCiclicaError("Um termo não pode ser pai de si mesmo")
        # Sobe a hierarquia a partir do pai procurando o termo filho
        atual_id = termo_pai_id
        visitados: set[str] = set()
        mapa = {t.id: t for t in termos}
        while atual_id:
            if atual_id in visitados:
                raise HierarquiaCiclicaError("Ciclo detectado na hierarquia existente")
            visitados.add(atual_id)
            if atual_id == termo_id:
                raise HierarquiaCiclicaError(
                    "Associação criaria ciclo na hierarquia da taxonomia"
                )
            pai = mapa.get(atual_id)
            atual_id = pai.termo_pai_id if pai else ""

    @staticmethod
    def rastrear_ancestrais(termos: list[TermoTaxonomia], termo_id: str) -> list[str]:
        """Retorna a cadeia de ancestrais do termo (do pai até a raiz)."""
        mapa = {t.id: t for t in termos}
        ancestrais: list[str] = []
        atual = mapa.get(termo_id)
        while atual and atual.termo_pai_id:
            ancestrais.append(atual.termo_pai_id)
            atual = mapa.get(atual.termo_pai_id)
        return ancestrais

    @staticmethod
    def rastrear_descendentes(termos: list[TermoTaxonomia], termo_id: str) -> list[str]:
        """Retorna todos os descendentes do termo (busca em profundidade)."""
        filhos_map: dict[str, list[str]] = {}
        for t in termos:
            filhos_map.setdefault(t.termo_pai_id, []).append(t.id)
        descendentes: list[str] = []
        pilha = list(filhos_map.get(termo_id, []))
        while pilha:
            atual = pilha.pop()
            descendentes.append(atual)
            pilha.extend(filhos_map.get(atual, []))
        return descendentes

    @staticmethod
    def calcular_profundidade(termos: list[TermoTaxonomia], termo_id: str) -> int:
        """Calcula a profundidade do termo na hierarquia (raiz = 0)."""
        mapa = {t.id: t for t in termos}
        profundidade = 0
        atual = mapa.get(termo_id)
        while atual and atual.termo_pai_id:
            profundidade += 1
            atual = mapa.get(atual.termo_pai_id)
        return profundidade

    @staticmethod
    def validar_codigo_unico_na_taxonomia(
        termos: list[TermoTaxonomia], taxonomia_id: str, codigo: str, exclude_id: str = ""
    ) -> None:
        """Valida que o código do termo é único dentro da taxonomia."""
        for termo in termos:
            if (
                termo.taxonomia_id == taxonomia_id
                and termo.codigo.lower() == codigo.lower()
                and termo.id != exclude_id
            ):
                raise TermoJaExisteError(
                    f"Termo com código '{codigo}' já existe na taxonomia"
                )

    @staticmethod
    def adicionar_termo_raiz(taxonomia: Taxonomia, termo: TermoTaxonomia) -> Taxonomia:
        """Adiciona termo raiz à taxonomia."""
        if termo.termo_pai_id:
            raise ValueError("Apenas termos raiz podem ser adicionados à taxonomia")
        if termo.id in taxonomia.termos_ids:
            raise TermoJaExisteError(f"Termo '{termo.nome}' já está na taxonomia")
        taxonomia.add_termo(termo.id)
        logger.info("Termo raiz '%s' adicionado à taxonomia '%s'", termo.codigo, taxonomia.codigo)
        return taxonomia


class ClassificacaoService:
    """Serviço de classificações corporativas."""

    @staticmethod
    def ordenar_por_nivel(classificacoes: list) -> list:
        """Retorna classificações ordenadas por nível (crescente)."""
        return sorted(classificacoes, key=lambda c: c.nivel)

    @staticmethod
    def nivel_maximo(classificacoes: list) -> int:
        """Retorna o nível máximo entre as classificações."""
        if not classificacoes:
            return 0
        return max(c.nivel for c in classificacoes)

    @staticmethod
    def e_mais_restritiva(classificacao, outras: list) -> bool:
        """Verifica se a classificação é mais restritiva (nível maior) que as outras."""
        return all(classificacao.nivel > c.nivel for c in outras)


__all__ = [
    "MetadadoService",
    "TaxonomiaService",
    "ClassificacaoService",
]
