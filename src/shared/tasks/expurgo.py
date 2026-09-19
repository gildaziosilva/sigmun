"""Serviço de expurgo físico de arquivos do DOM-GDO (Fase VII).

Remove do `STORAGE_ROOT` apenas arquivos de documentos com descarte
autorizado (`data_eliminacao` + `status == encerrado`, RN-GDO-010/011)
e carência cumprida. Nunca apaga fora de STORAGE_ROOT.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class ResultadoExpurgo:
    """Resumo de uma execução do expurgo."""

    candidatos: int = 0
    removidos: int = 0
    ignorados_fora_da_raiz: int = 0
    ausentes: int = 0
    erros: int = 0
    arquivos_removidos: list[str] = field(default_factory=list)
    arquivos_ignorados: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "candidatos": self.candidatos,
            "removidos": self.removidos,
            "ignorados_fora_da_raiz": self.ignorados_fora_da_raiz,
            "ausentes": self.ausentes,
            "erros": self.erros,
            "arquivos_removidos": self.arquivos_removidos,
            "arquivos_ignorados": self.arquivos_ignorados,
        }


def resolver_caminho_seguro(storage_root: str | Path, conteudo_ref: str) -> Path | None:
    """Resolve `conteudo_ref` contra a raiz, ou None se inseguro."""
    if not conteudo_ref or not conteudo_ref.strip():
        return None
    raiz = Path(storage_root).resolve()
    candidato = Path(conteudo_ref.strip())
    if not candidato.is_absolute():
        candidato = raiz / candidato
    try:
        resolvido = candidato.resolve()
    except OSError:
        return None
    try:
        resolvido.relative_to(raiz)
    except ValueError:
        return None
    if resolvido == raiz:
        return None
    return resolvido


def coletar_candidatos_expurgo(
    session: Any, dias_retencao: int = 30, limite: int = 500
) -> list[Any]:
    """Documentos com descarte autorizado e carência cumprida."""
    from src.modules.sigmun_gdo.infrastructure.database.models import DocumentoModel

    base = datetime.now(timezone.utc)
    modelos = (
        session.query(DocumentoModel)
        .filter(
            DocumentoModel.data_eliminacao.is_not(None),
            DocumentoModel.status == "encerrado",
            DocumentoModel.deleted_at.is_(None),
        )
        .order_by(DocumentoModel.data_eliminacao)
        .limit(limite)
        .all()
    )
    elegiveis = []
    for modelo in modelos:
        data_elim = modelo.data_eliminacao
        if data_elim is None:
            continue
        if data_elim.tzinfo is None:
            data_elim = data_elim.replace(tzinfo=timezone.utc)
        try:
            dias = (base - data_elim).days
        except Exception:  # pragma: no cover - defensivo
            continue
        if dias >= dias_retencao:
            elegiveis.append(modelo)
    return elegiveis


def expurgar_arquivos(
    session: Any,
    storage_root: str | Path | None = None,
    dias_retencao: int = 30,
    dry_run: bool = False,
    limite: int = 500,
) -> ResultadoExpurgo:
    """Remove binários com descarte autorizado (registro permanece p/ auditoria)."""

    from src.shared.config.settings import settings as _settings

    raiz = Path(storage_root or _settings.STORAGE_ROOT)
    resultado = ResultadoExpurgo()
    candidatos = coletar_candidatos_expurgo(session, dias_retencao=dias_retencao, limite=limite)
    for modelo in candidatos:
        ref = getattr(modelo, "conteudo_ref", "") or ""
        if not ref.strip():
            continue
        resultado.candidatos += 1
        seguro = resolver_caminho_seguro(raiz, ref)
        if seguro is None:
            resultado.ignorados_fora_da_raiz += 1
            resultado.arquivos_ignorados.append(ref)
            logger.warning("expurgo: ref fora de STORAGE_ROOT ignorada")
            continue
        if seguro.is_symlink() or not seguro.is_file():
            if not seguro.exists():
                resultado.ausentes += 1
            else:
                resultado.ignorados_fora_da_raiz += 1
                resultado.arquivos_ignorados.append(str(seguro))
            continue
        if dry_run:
            resultado.arquivos_removidos.append(str(seguro))
            continue
        try:
            os.remove(seguro)
            resultado.removidos += 1
            resultado.arquivos_removidos.append(str(seguro))
            logger.info("expurgo: arquivo removido %s doc=%s", seguro, modelo.id)
        except OSError as exc:
            resultado.erros += 1
            logger.error("expurgo: falha ao remover %s: %s", seguro, exc)
    return resultado


__all__ = [
    "ResultadoExpurgo",
    "resolver_caminho_seguro",
    "coletar_candidatos_expurgo",
    "expurgar_arquivos",
]
