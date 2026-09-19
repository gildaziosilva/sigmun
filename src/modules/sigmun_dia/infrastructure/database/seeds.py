"""Seeds de referência para DOM-DIA - Categorias e Tipos de diária."""

from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Session

from .models import CategoriaDiariaModel, TipoDeslocamentoModel


def seed_categorias(session: Session) -> None:
    """Cria categorias de diária de referência se não existirem."""

    categorias_existentes = {c.codigo for c in session.query(CategoriaDiariaModel).all()}

    categorias_para_criar = [
        {"codigo": "evento", "nome": "Evento", "descricao": "Diária por participação em evento"},
        {"codigo": "reuniao", "nome": "Reunião", "descricao": "Diária por participação em reunião"},
        {"codigo": "treinamento", "nome": "Treinamento", "descricao": "Diária por participação em treinamento"},
        {"codigo": "viagem_oficial", "nome": "Viagem Oficial", "descricao": "Diária por viagem oficial"},
        {"codigo": "servico_consultivo", "nome": "Serviço Consultivo", "descricao": "Diária por serviço consultivo"},
    ]

    for cat in categorias_para_criar:
        if cat["codigo"] not in categorias_existentes:
            model = CategoriaDiariaModel(
                id=uuid4(),
                codigo=cat["codigo"],
                nome=cat["nome"],
                descricao=cat["descricao"],
                is_ativo=True,
                created_at=datetime.utcnow(),
                created_by="seed",
            )
            session.add(model)

    session.flush()


def seed_tipos_deslocamento(session: Session) -> None:
    """Cria tipos de deslocamento de referência se não existirem."""

    tipos_existentes = {t.codigo for t in session.query(TipoDeslocamentoModel).all()}

    tipos_para_criar = [
        {"codigo": "terrestre", "nome": "Terrestre", "descricao": "Deslocamento terrestre"},
        {"codigo": "aereo", "nome": "Aéreo", "descricao": "Deslocamento aéreo"},
        {"codigo": "fluvial", "nome": "Fluvial", "descricao": "Deslocamento fluvial"},
        {"codigo": "maritimo", "nome": "Marítimo", "descricao": "Deslocamento marítimo"},
    ]

    for tipo in tipos_para_criar:
        if tipo["codigo"] not in tipos_existentes:
            model = TipoDeslocamentoModel(
                id=uuid4(),
                codigo=tipo["codigo"],
                nome=tipo["nome"],
                descricao=tipo["descricao"],
                is_ativo=True,
                created_at=datetime.utcnow(),
                created_by="seed",
            )
            session.add(model)

    session.flush()


def run_seeds(session: Session) -> None:
    """Executa todos os seeds do DOM-DIA."""
    seed_categorias(session)
    seed_tipos_deslocamento(session)
