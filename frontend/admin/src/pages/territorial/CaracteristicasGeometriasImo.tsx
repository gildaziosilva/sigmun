import { useState } from 'react';
import type {
  CaracteristicaImoCreate,
  GeometriaImoCreate,
  VerticeTel,
} from '../../lib/api';
import { registrarCaracteristicaImo, registrarGeometriaImo } from '../../lib/api';
import type { ImoResources } from './ImoPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  formatarDataTerr,
  imovelInscricao,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: ImoResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const OBRAS = [
  { valor: 'residencial', rotulo: 'Residencial' },
  { valor: 'comercial', rotulo: 'Comercial' },
  { valor: 'industrial', rotulo: 'Industrial' },
  { valor: 'institucional', rotulo: 'Institucional' },
  { valor: 'mista', rotulo: 'Mista' },
  { valor: 'nao_aplicavel', rotulo: 'Não aplicável' },
];

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

const VERTICE_VAZIO: VerticeTel = { latitude: 0, longitude: 0 };

export function CaracteristicasGeometriasImo({ resources, executar, salvando }: Props) {
  const imoveis = resources.imoveis.data ?? [];
  const caracteristicas = resources.caracteristicas.data ?? [];
  const geometrias = resources.geometrias.data ?? [];
  const opcoesImovel = imoveis.map((i) => ({
    valor: i.id,
    rotulo: i.inscricao_imobiliaria,
  }));

  // Característica construtiva
  const [imovelCar, setImovelCar] = useState('');
  const [obra, setObra] = useState('residencial');
  const [pavimentos, setPavimentos] = useState('1');
  const [anoRenovacao, setAnoRenovacao] = useState('');
  const [observacao, setObservacao] = useState('');

  // Geometria do lote
  const [imovelGeo, setImovelGeo] = useState('');
  const [geometria, setGeometria] = useState('ponto');
  const [datum, setDatum] = useState('sirgas2000');
  const [precisao, setPrecisao] = useState('0');
  const [vertices, setVertices] = useState<VerticeTel[]>([{ ...VERTICE_VAZIO }]);

  const minimo = GEOMETRIAS.find((g) => g.valor === geometria)?.minimo ?? 1;

  function ajustarGeometria(valor: string) {
    setGeometria(valor);
    const exigido = GEOMETRIAS.find((g) => g.valor === valor)?.minimo ?? 1;
    setVertices((atual) =>
      atual.length >= exigido
        ? atual
        : [...atual, ...Array.from({ length: exigido - atual.length }, () => ({ ...VERTICE_VAZIO }))],
    );
  }

  function alterarVertice(indice: number, campo: 'latitude' | 'longitude', valor: string) {
    setVertices((atual) =>
      atual.map((v, i) => (i === indice ? { ...v, [campo]: paraNumero(valor) } : v)),
    );
  }

  async function handleCaracteristica(event: React.FormEvent) {
    event.preventDefault();
    const payload: CaracteristicaImoCreate = {
      imovel_id: imovelCar,
      obra,
      numero_pavimentos: paraNumero(pavimentos, 1),
      ano_renovacao: anoRenovacao.trim() ? paraNumero(anoRenovacao) : null,
      observacao,
    };
    const ok = await executar(
      () => registrarCaracteristicaImo(payload),
      'Característica construtiva registrada com sucesso!',
    );
    if (ok) {
      setImovelCar('');
      setObservacao('');
      setAnoRenovacao('');
      setPavimentos('1');
    }
  }

  async function handleGeometria(event: React.FormEvent) {
    event.preventDefault();
    const payload: GeometriaImoCreate = {
      imovel_id: imovelGeo,
      geometria,
      vertices,
      datum,
      precisao_m: paraNumero(precisao),
      latitude: vertices[0]?.latitude ?? 0,
      longitude: vertices[0]?.longitude ?? 0,
    };
    const ok = await executar(
      () => registrarGeometriaImo(payload),
      'Geometria do lote registrada com sucesso!',
    );
    if (ok) {
      setImovelGeo('');
      setVertices([{ ...VERTICE_VAZIO }]);
      setPrecisao('0');
    }
  }

  return (
    <section className="stack terr-caracteristicas">
      <div className="terr-grid">
        <form className="card terr-form" onSubmit={handleCaracteristica}>
          <h3>Característica construtiva</h3>
          <p className="muted">
            Descreve a construção existente e alimenta a resolução da ocupação usada na
            avaliação do valor venal.
          </p>
          <div className="form-grid">
            <SelectTerr
              label="Imóvel"
              value={imovelCar}
              opcoes={opcoesImovel}
              onChange={setImovelCar}
              required
              vazio="Selecione..."
            />
            <SelectTerr label="Natureza da obra" value={obra} opcoes={OBRAS} onChange={setObra} required />
            <FieldTerr label="Número de pavimentos" value={pavimentos} onChange={setPavimentos} type="number" min="1" step="1" required />
            <FieldTerr label="Ano de renovação" value={anoRenovacao} onChange={setAnoRenovacao} type="number" min="1800" max="2200" step="1" />
            <FieldTerr label="Observação" value={observacao} onChange={setObservacao} />
          </div>
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando}>
              Registrar característica
            </button>
          </div>
        </form>

        <form className="card terr-form" onSubmit={handleGeometria}>
          <h3>Geometria do lote</h3>
          <p className="muted">
            Georreferência do lote, com datum e vértices validados pelo sistema (RN-IMO-007).
            Cada lote admite uma geometria vigente.
          </p>
          <div className="form-grid">
            <SelectTerr
              label="Imóvel"
              value={imovelGeo}
              opcoes={opcoesImovel}
              onChange={setImovelGeo}
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
            <legend>Vértices</legend>
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
                    onClick={() => setVertices((atual) => atual.filter((_, i) => i !== indice))}
                    disabled={vertices.length <= minimo}
                  >
                    Remover
                  </button>
                </div>
              ))}
            </div>
            <button
              type="button"
              className="button button--ghost button--sm"
              onClick={() => setVertices((atual) => [...atual, { ...VERTICE_VAZIO }])}
            >
              Adicionar vértice
            </button>
          </fieldset>
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando}>
              Registrar geometria
            </button>
          </div>
        </form>
      </div>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Características construtivas ({caracteristicas.length})</h3>
        </div>
        {caracteristicas.length === 0 ? (
          <p className="muted">Nenhuma característica registrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Imóvel</th>
                <th>Obra</th>
                <th className="num">Pavimentos</th>
                <th className="num">Ano de renovação</th>
                <th>Observação</th>
              </tr>
            </thead>
            <tbody>
              {caracteristicas.map((c) => (
                <tr key={c.id}>
                  <td>{imovelInscricao(imoveis, c.imovel_id)}</td>
                  <td>{c.obra.replaceAll('_', ' ')}</td>
                  <td className="num">{c.numero_pavimentos}</td>
                  <td className="num">{c.ano_renovacao ?? '—'}</td>
                  <td>{c.observacao || '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Geometrias dos lotes ({geometrias.length})</h3>
        </div>
        {geometrias.length === 0 ? (
          <p className="muted">Nenhuma geometria registrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Imóvel</th>
                <th>Geometria</th>
                <th className="num">Vértices</th>
                <th className="num">Latitude</th>
                <th className="num">Longitude</th>
                <th>Datum</th>
                <th className="num">Precisão</th>
                <th>Levantamento</th>
              </tr>
            </thead>
            <tbody>
              {geometrias.map((g) => (
                <tr key={g.id}>
                  <td>{imovelInscricao(imoveis, g.imovel_id)}</td>
                  <td>{g.geometria}</td>
                  <td className="num">{g.vertices.length}</td>
                  <td className="num">{g.latitude}</td>
                  <td className="num">{g.longitude}</td>
                  <td>{g.datum.toUpperCase()}</td>
                  <td className="num">{g.precisao_m} m</td>
                  <td>{formatarDataTerr(g.data_levantamento)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}

