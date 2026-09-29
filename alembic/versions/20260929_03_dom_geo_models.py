"""Migração DOM-GEO: geoinformação municipal (schema geo).

Cria o schema `geo` e as tabelas de camadas cartográficas, mapas SIG,
composição mapa↔camada, elementos geoespaciais e serviços publicados.

Regras: RN-GEO-001 (código único de camada), RN-GEO-002 (código único de mapa),
RN-GEO-003 (geometria com vértices mínimos por tipo), RN-GEO-004 (mapa publicado
não é removível da composição), RN-GEO-006 (camada de serviço exige URL),
RN-GEO-007 (serviço ativo exige URL e, em WMS/WFS, nome de camada).
"""

from __future__ import annotations

import uuid

import sqlalchemy as sa
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

revision = "20260929_03_dom_geo_models"
down_revision = "20260929_02_dom_imo_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS geo")
    op.create_table(
        "camadas_mapa",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("tipo", Text, nullable=False, server_default="outro"),
        Column("formato", Text, nullable=False, server_default="geojson"),
        Column("fonte", Text),
        Column("data_atualizacao", Date, nullable=False),
        Column("datum", Text, nullable=False, server_default="sirgas2000"),
        Column("srid", Integer, nullable=False, server_default="4326"),
        Column("url_servico", Text),
        Column("zoom_minimo", Integer, nullable=False, server_default="0"),
        Column("zoom_maximo", Integer, nullable=False, server_default="24"),
        Column("visivel", Boolean, nullable=False, server_default="true"),
        Column("situacao", Text, nullable=False, server_default="rascunho"),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="geo",
    )
    op.create_index("ix_geo_camadas_codigo", "camadas_mapa", ["codigo"], schema="geo")
    op.create_index("ix_geo_camadas_tipo", "camadas_mapa", ["tipo"], schema="geo")
    # RN-GEO-006: camada de serviço published exige URL de acesso.
    op.create_check_constraint(
        "ck_geo_camada_zoom",
        "camadas_mapa",
        "zoom_minimo <= zoom_maximo",
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_camada_servico_url",
        "camadas_mapa",
        "formato NOT IN ('wms', 'wfs', 'wmts', 'xyz') OR situacao <> 'ativa' "
        "OR (url_servico IS NOT NULL AND btrim(url_servico) <> '')",
        schema="geo",
    )

    op.create_table(
        "mapas_sig",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("tipo", Text, nullable=False, server_default="tematico"),
        Column("situacao", Text, nullable=False, server_default="rascunho"),
        Column("datum", Text, nullable=False, server_default="sirgas2000"),
        Column("srid", Integer, nullable=False, server_default="4326"),
        Column("escala_denominador", Integer, nullable=False, server_default="0"),
        Column("zoom_inicial", Integer, nullable=False, server_default="13"),
        Column("zoom_minimo", Integer, nullable=False, server_default="0"),
        Column("zoom_maximo", Integer, nullable=False, server_default="24"),
        Column("lat_min", Float),
        Column("lon_min", Float),
        Column("lat_max", Float),
        Column("lon_max", Float),
        Column("publicado_em", DateTime(timezone=True)),
        Column("criado_por", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="geo",
    )
    op.create_index("ix_geo_mapas_codigo", "mapas_sig", ["codigo"], schema="geo")
    op.create_index("ix_geo_mapas_situacao", "mapas_sig", ["situacao"], schema="geo")
    # RN-GEO-005: coerência dos níveis de zoom e da extensão (bbox).
    op.create_check_constraint(
        "ck_geo_mapa_zoom",
        "mapas_sig",
        "zoom_minimo <= zoom_inicial AND zoom_inicial <= zoom_maximo",
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_mapa_extensao",
        "mapas_sig",
        "lat_min IS NULL OR lat_max IS NULL OR lat_min <= lat_max",
        schema="geo",
    )

    op.create_table(
        "mapas_camadas",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("mapa_id", Text, nullable=False),
        Column("camada_id", Text, nullable=False),
        Column("ordem", Integer, nullable=False, server_default="0"),
        Column("opacidade", Float, nullable=False, server_default="100"),
        Column("visivel", Boolean, nullable=False, server_default="true"),
        Column("rotulo", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="geo",
    )
    # RN-GEO-004: a mesma camada não entra duas vezes na composição do mapa.
    op.create_index(
        "uq_geo_mapa_camada",
        "mapas_camadas",
        ["mapa_id", "camada_id"],
        unique=True,
        postgresql_where=sa.text("is_deleted = false"),
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_composicao_opacidade",
        "mapas_camadas",
        "opacidade >= 0 AND opacidade <= 100",
        schema="geo",
    )

    op.create_table(
        "features_geo",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("camada_id", Text, nullable=False),
        Column("geometria", Text, nullable=False, server_default="ponto"),
        Column("latitude", Float, nullable=False, server_default="0"),
        Column("longitude", Float, nullable=False, server_default="0"),
        Column("vertices", JSON),
        Column("datum", Text, nullable=False, server_default="sirgas2000"),
        Column("atributos", JSON),
        Column("criado_por", Text),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="geo",
    )
    op.create_index("ix_geo_features_camada", "features_geo", ["camada_id"], schema="geo")
    op.create_index("ix_geo_features_codigo", "features_geo", ["codigo"], schema="geo")
    # RN-GEO-003: vértices mínimos por tipo de geometria e coordenadas em faixa.
    op.create_check_constraint(
        "ck_geo_feature_coordenadas",
        "features_geo",
        "latitude >= -90 AND latitude <= 90 AND longitude >= -180 AND longitude <= 180",
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_feature_vertices",
        "features_geo",
        "CASE geometria "
        "WHEN 'ponto' THEN coalesce(jsonb_array_length(vertices::jsonb), 0) >= 1 "
        "WHEN 'linha' THEN coalesce(jsonb_array_length(vertices::jsonb), 0) >= 2 "
        "WHEN 'poligono' THEN coalesce(jsonb_array_length(vertices::jsonb), 0) >= 3 "
        "ELSE true END",
        schema="geo",
    )

    op.create_table(
        "servicos_geo",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        Column("codigo", Text, nullable=False, unique=True),
        Column("nome", Text, nullable=False),
        Column("descricao", Text),
        Column("tipo", Text, nullable=False, server_default="wms"),
        Column("situacao", Text, nullable=False, server_default="ativo"),
        Column("url", Text),
        Column("camada", Text),
        Column("datum", Text, nullable=False, server_default="sirgas2000"),
        Column("srid", Integer, nullable=False, server_default="4326"),
        Column("zoom_minimo", Integer, nullable=False, server_default="0"),
        Column("zoom_maximo", Integer, nullable=False, server_default="24"),
        Column("publico", Boolean, nullable=False, server_default="false"),
        Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
        Column("updated_at", DateTime(timezone=True)),
        Column("created_by", Text),
        Column("is_deleted", Boolean, nullable=False, server_default="false"),
        schema="geo",
    )
    op.create_index("ix_geo_servicos_tipo", "servicos_geo", ["tipo"], schema="geo")
    # RN-GEO-007: serviço ativo exige URL; WMS/WFS exigem nome de camada.
    op.create_check_constraint(
        "ck_geo_servico_url",
        "servicos_geo",
        "situacao <> 'ativo' OR (url IS NOT NULL AND btrim(url) <> '')",
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_servico_camada",
        "servicos_geo",
        "situacao <> 'ativo' OR tipo NOT IN ('wms', 'wfs') "
        "OR (camada IS NOT NULL AND btrim(camada) <> '')",
        schema="geo",
    )
    op.create_check_constraint(
        "ck_geo_servico_zoom",
        "servicos_geo",
        "zoom_minimo <= zoom_maximo",
        schema="geo",
    )


def downgrade() -> None:
    op.drop_index("ix_geo_servicos_tipo", table_name="servicos_geo", schema="geo")
    op.drop_table("servicos_geo", schema="geo")
    op.drop_index("ix_geo_features_codigo", table_name="features_geo", schema="geo")
    op.drop_index("ix_geo_features_camada", table_name="features_geo", schema="geo")
    op.drop_table("features_geo", schema="geo")
    op.drop_index("uq_geo_mapa_camada", table_name="mapas_camadas", schema="geo")
    op.drop_table("mapas_camadas", schema="geo")
    op.drop_index("ix_geo_mapas_situacao", table_name="mapas_sig", schema="geo")
    op.drop_index("ix_geo_mapas_codigo", table_name="mapas_sig", schema="geo")
    op.drop_table("mapas_sig", schema="geo")
    op.drop_index("ix_geo_camadas_tipo", table_name="camadas_mapa", schema="geo")
    op.drop_index("ix_geo_camadas_codigo", table_name="camadas_mapa", schema="geo")
    op.drop_table("camadas_mapa", schema="geo")
    op.execute("DROP SCHEMA IF EXISTS geo")
