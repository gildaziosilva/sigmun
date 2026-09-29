import { useState } from 'react';
import type { GeorreferenciaTel, GeorreferenciaTelCreate, VerticeTel } from '../../lib/api';
import { excluirGeorreferenciaTel, registrarGeorreferenciaTel } from '../../lib/api';
import type { TelResources } from './TelPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  formatarDataTerr,
  bairroNome,
  logradouroNome,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: TelResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const GEOMETRIAS = [
  { valor: 'ponto', rotulo: 'Ponto', minimo: 1 },
  { valor: 'linha', rotulo: 'Linha', minimo: 2 },
  { valor: 'poligono', rotulo: 'Polígono', minimo: 3 },
];

const DATUMS = [
  { valor: 'sirgas2000', rotulo: 'SIRGAS 2000' },
  { valor: 'sad69', rotulo: 'SAD 69' },
  { valor: 'wgs84', rotulo: 'WGS 84' },
];

/** Vértice vazio para acréscimo na grade de coordenadas. */
const VERTICE_VAZIO: VerticeTel = { latitude: 0, longitude: 0 };

export function GeorreferenciasTel({ resources, executar, salvando }: Props) {
  const [referencia, setReferencia] = useState<'bairro' | 'logradouro'>('bairro');
  const [referenciaId, setReferenciaId] = useState('');
  const [geometria, setGeometria] = useState('ponto');
  const [datum, setDatum] = useState('sirgas2000');
  const [precisao, setPrecisao] = useState('0');
  const [vertices, setVertices] = useState<VerticeTel[]>([{ ...VERTICE_VAZIO }]);

  const bairros = resources.bairros.data ?? [];
  const logradouros = resources.logradouros.data ?? [];
  const georreferencias = resources.georreferencias.data ?? [];

  const minimo = GEOMETRIAS.find((g) => g.valor === geometria)?.minimo ?? 1;
  const opcoesReferencia =
    referencia === 'bairro'
      ? bairros.map((b) => ({ valor: b.id, rotulo: `${b.codigo} — ${b.nome}` }))
      : logradouros.map((l) => ({ valor: l.id, rotulo: `${l.codigo} — ${l.nome}` }));

  function ajustarGeometria(valor: string) {
    setGeometria(valor);
    const exigido = GEOMETRIAS.find((g) => g.valor === valor)?.minimo ?? 1;
    setVertices((atual) => {
      if (atual.length >= exigido) return atual;
      return [...atual, ...Array.from({ length: exigido - atual.length }, () => ({ ...VERTICE_VAZIO }))];
    });
  }

  function alterarVertice(indice: number, campo: 'latitude' | 'longitude', valor: string) {
    setVertices((atual) =>
      atual.map((v, i) => (i === indice ? { ...v, [campo]: paraNumero(valor) } : v)),
    );
  }

  function adicionarVertice() {
    setVertices((atual) => [...atual, { ...VERTICE_VAZIO }]);
  }

  function removerVertice(indice: number) {
    setVertices((atual) => atual.filter((_, i) => i !== indice));
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: GeorreferenciaTelCreate = {
      [referencia === 'bairro' ? 'bairro_id' : 'logradouro_id']: referenciaId,
      geometria,
      vertices,
      datum,
      precisao_m: paraNumero(precisao),
      latitude: vertices[0]?.latitude ?? 0,
      longitude: vertices[0]?.longitude ?? 0,
    };
    const ok = await executar(
      () => registrarGeorreferenciaTel(payload),
      'Georreferência registrada com sucesso!',
    );
    if (ok) {
      setReferenciaId('');
      setVertices([{ ...VERTICE_VAZIO }]);
      setPrecisao('0');
    }
  }

  async function handleExcluir(geo: GeorreferenciaTel) {
    if (!window.confirm('Excluir esta georreferência?')) return;
    await executar(() => excluirGeorreferenciaTel(geo.id), 'Georreferência excluída com sucesso!');
  }

  return (
    <section className="stack terr-georreferencias">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>Registrar georreferência territorial</h3>
        <p className="muted">
          A georreferência é vinculada a um bairro <strong>ou</strong> a um logradouro, nunca a
          ambos (RN-TEL-005). Coordenadas e vértices são validados pelo sistema.
        </p>
        <div className="form-grid">
          <SelectTerr
            label="Tipo de referência"
            value={referencia}
            opcoes={[
              { valor: 'bairro', rotulo: 'Bairro' },
              { valor: 'logradouro', rotulo: 'Logradouro' },
            ]}
            onChange={(v) => {
              setReferencia(v as 'bairro' | 'logradouro');
              setReferenciaId('');
            }}
            required
          />
          <SelectTerr
            label={referencia === 'bairro' ? 'Bairro' : 'Logradouro'}
            value={referenciaId}
            opcoes={opcoesReferencia}
            onChange={setReferenciaId}
            required
            vazio="Selecione..."
          />
          <SelectTerr
            label="Tipo de geometria"
            value={geometria}
            opcoes={GEOMETRIAS}
            onChange={ajustarGeometria}
            required
            hint={`Exige ao menos ${minimo} vértice(s)`}
          />
          <SelectTerr label="Datum" value={datum} opcoes={DATUMS} onChange={setDatum} required />
          <FieldTerr label="Precisão (m)" value={precisao} onChange={setPrecisao} type="number" min="0" step="0.01" />
        </div>

        <fieldset style={{ border: '1px solid var(--cor-borda)', borderRadius: '0.5rem', padding: '0.75rem' }}>
          <legend>Vértices da geometria</legend>
          <div className="terr-vertices">
            {vertices.map((v, indice) => (
              <div key={indice} className="terr-vertex-row">
                <FieldTerr
                  label={`Latitude ${indice + 1}`}
                  value={String(v.latitude)}
                  onChange={(valor) => alterarVertice(indice, 'latitude', valor)}
                  type="number"
                  step="0.000001"
                />
                <FieldTerr
                  label={`Longitude ${indice + 1}`}
                  value={String(v.longitude)}
                  onChange={(valor) => alterarVertice(indice, 'longitude', valor)}
                  type="number"
                  step="0.000001"
                />
                <button
                  type="button"
                  className="button button--danger button--sm"
                  onClick={() => removerVertice(indice)}
                  disabled={vertices.length <= minimo}
                >
                  Remover
                </button>
              </div>
            ))}
          </div>
          <button type="button" className="button button--ghost button--sm" onClick={adicionarVertice}>
            Adicionar vértice
          </button>
        </fieldset>

        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Registrar georreferência
          </button>
        </div>
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Georreferências registradas ({georreferencias.length})</h3>
        </div>
        {georreferencias.length === 0 ? (
          <p className="muted">Nenhuma georreferência registrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Referência</th>
                <th>Tipo</th>
                <th>Geometria</th>
                <th className="num">Vértices</th>
                <th className="num">Latitude</th>
                <th className="num">Longitude</th>
                <th>Datum</th>
                <th>Levantamento</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {georreferencias.map((g) => (
                <tr key={g.id}>
                  <td>
                    {g.bairro_id
                      ? bairroNome(bairros, g.bairro_id)
                      : logradouroNome(logradouros, g.logradouro_id)}
                  </td>
                  <td>{g.bairro_id ? 'Bairro' : 'Logradouro'}</td>
                  <td>{g.geometria}</td>
                  <td className="num">{g.vertices.length}</td>
                  <td className="num">{g.latitude}</td>
                  <td className="num">{g.longitude}</td>
                  <td>{g.datum.toUpperCase()}</td>
                  <td>{formatarDataTerr(g.data_levantamento)}</td>
                  <td>
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => handleExcluir(g)}
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

