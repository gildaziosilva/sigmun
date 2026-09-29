import { useState } from 'react';
import type { FeatureGeo, FeatureGeoCreate, VerticeGeo } from '../../lib/api';
import { excluirFeatureGeo, listarFeaturesGeo, registrarFeatureGeo } from '../../lib/api';
import type { GeoPageResources } from './GeoPage';
import type { ExecutarGeo } from './GeoShared';
import { DATUMS, FieldGeo, GEOMETRIAS, SelectGeo, paraNumeroGeo } from './GeoShared';

interface Props {
  resources: GeoPageResources;
  executar: ExecutarGeo;
  salvando: boolean;
}

const VAZIA: VerticeGeo = { latitude: 0, longitude: 0 };

export function FeaturesGeo({ resources, executar, salvando }: Props) {
  const [codigo, setCodigo] = useState('');
  const [nome, setNome] = useState('');
  const [camadaId, setCamadaId] = useState('');
  const [geometria, setGeometria] = useState('ponto');
  const [datum, setDatum] = useState('sirgas2000');
  const [vertices, setVertices] = useState<VerticeGeo[]>([{ ...VAZIA }]);

  // Filtro por camada: usa o endpoint dedicado; "Todas" volta a listagem geral.
  const [filtroCamada, setFiltroCamada] = useState('');
  const [filtrados, setFiltrados] = useState<FeatureGeo[] | null>(null);
  const [carregandoFiltro, setCarregandoFiltro] = useState(false);
  const [erro, setErro] = useState('');

  const camadas = resources.camadas.data ?? [];
  const features = filtrados ?? resources.features.data ?? [];
  const minimo = GEOMETRIAS.find((g) => g.valor === geometria)?.minimo ?? 1;

  function nomeCamada(id: string): string {
    return camadas.find((c) => c.id === id)?.nome ?? id;
  }

  function filtrar(camada: string) {
    setFiltroCamada(camada);
    setErro('');
    if (!camada) {
      setFiltrados(null);
      return;
    }
    setCarregandoFiltro(true);
    listarFeaturesGeo(camada)
      .then(setFiltrados)
      .catch((falha: unknown) => {
        setErro(falha instanceof Error ? falha.message : 'Falha ao filtrar elementos.');
        setFiltrados(null);
      })
      .finally(() => setCarregandoFiltro(false));
  }

  function ajustarGeometria(valor: string) {
    setGeometria(valor);
    const exigido = GEOMETRIAS.find((g) => g.valor === valor)?.minimo ?? 1;
    setVertices((atual) =>
      atual.length >= exigido
        ? atual
        : [...atual, ...Array.from({ length: exigido - atual.length }, () => ({ ...VAZIA }))],
    );
  }

  function alterarVertice(indice: number, campo: 'latitude' | 'longitude', valor: string) {
    setVertices((atual) =>
      atual.map((v, i) => (i === indice ? { ...v, [campo]: paraNumeroGeo(valor) } : v)),
    );
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: FeatureGeoCreate = {
      codigo,
      nome,
      camada_id: camadaId,
      geometria,
      datum,
      vertices,
      latitude: vertices[0]?.latitude ?? 0,
      longitude: vertices[0]?.longitude ?? 0,
    };
    const ok = await executar(
      () => registrarFeatureGeo(payload),
      'Elemento geoespacial registrado!',
    );
    if (ok) {
      setCodigo('');
      setNome('');
      setVertices([{ ...VAZIA }]);
    }
  }

  return (
    <section className="stack">
      <form className="card geo-form" onSubmit={handleSubmit}>
        <h3>Novo elemento geoespacial (RN-GEO-003, RN-GEO-008)</h3>
        <div className="form-grid">
          <FieldGeo label="Codigo" value={codigo} onChange={setCodigo} required />
          <FieldGeo label="Nome" value={nome} onChange={setNome} required />
          <SelectGeo
            label="Camada"
            value={camadaId}
            opcoes={camadas.map((c) => ({ valor: c.id, rotulo: `${c.codigo} — ${c.nome}` }))}
            onChange={setCamadaId}
            vazio="Selecione a camada"
            required
          />
          <SelectGeo
            label="Geometria"
            value={geometria}
            opcoes={GEOMETRIAS}
            onChange={ajustarGeometria}
          />
          <SelectGeo label="Datum" value={datum} opcoes={DATUMS} onChange={setDatum} />
        </div>

        <fieldset className="geo-vertices">
          <legend>Vertices ({geometria})</legend>
          {vertices.map((v, indice) => (
            <div key={indice} className="geo-vertex-row">
              <FieldGeo
                label={`Latitude ${indice + 1}`}
                value={String(v.latitude)}
                onChange={(valor) => alterarVertice(indice, 'latitude', valor)}
                type="number"
                step="0.000001"
              />
              <FieldGeo
                label={`Longitude ${indice + 1}`}
                value={String(v.longitude)}
                onChange={(valor) => alterarVertice(indice, 'longitude', valor)}
                type="number"
                step="0.000001"
              />
              <button
                type="button"
                className="button button--danger button--sm"
                onClick={() => setVertices((atual) => atual.filter((_, i) => i !== indice))}
                disabled={vertices.length <= minimo}
              >
                Remover
              </button>
            </div>
          ))}
          <button
            type="button"
            className="button button--ghost button--sm"
            onClick={() => setVertices((atual) => [...atual, { ...VAZIA }])}
          >
            Adicionar vertice
          </button>
        </fieldset>

        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Registrar elemento
          </button>
        </div>
      </form>

      {erro && <p className="alert alert--error">{erro}</p>}

      <section className="card geo-lista">
        <div className="geo-lista-header">
          <h3>
            Elementos registrados ({features.length})
            {filtroCamada ? ` — camada: ${nomeCamada(filtroCamada)}` : ''}
          </h3>
          <div className="geo-filtro">
            <SelectGeo
              label="Filtrar por camada"
              value={filtroCamada}
              opcoes={camadas.map((c) => ({ valor: c.id, rotulo: c.nome }))}
              onChange={filtrar}
              vazio="Todas as camadas"
            />
            {carregandoFiltro && <span className="muted">Carregando…</span>}
          </div>
        </div>
        {features.length === 0 ? (
          <p className="muted">Nenhum elemento geoespacial registrado.</p>
        ) : (
          <table className="geo-table">
            <thead>
              <tr>
                <th>Codigo</th>
                <th>Nome</th>
                <th>Camada</th>
                <th>Geometria</th>
                <th className="num">Latitude</th>
                <th className="num">Longitude</th>
                <th>Datum</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {features.map((f) => (
                <tr key={f.id}>
                  <td>{f.codigo}</td>
                  <td>{f.nome}</td>
                  <td>{nomeCamada(f.camada_id)}</td>
                  <td>{f.geometria}</td>
                  <td className="num">{f.latitude}</td>
                  <td className="num">{f.longitude}</td>
                  <td>{f.datum.toUpperCase()}</td>
                  <td className="geo-acoes">
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => executar(() => excluirFeatureGeo(f.id), 'Elemento excluido!')}
                      disabled={salvando}
                    >
                      Excluir
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}
