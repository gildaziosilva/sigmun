import type { GeoPageResources } from './GeoPage';
import { StatusGeo } from './GeoShared';

export function VisaoGeralGeo({ resources }: { resources: GeoPageResources }) {
  const camadas = resources.camadas.data ?? [];
  const mapas = resources.mapas.data ?? [];
  const features = resources.features.data ?? [];
  const servicos = resources.servicos.data ?? [];

  const ativas = camadas.filter((c) => c.situacao === 'ativa').length;
  const publicados = mapas.filter((m) => m.situacao === 'publicado').length;
  const servicosAtivos = servicos.filter((s) => s.situacao === 'ativo').length;

  return (
    <section className="stack">
      <div className="geo-kpis">
        <article className="card">
          <h3>Camadas</h3>
          <p className="geo-kpi-valor">{camadas.length}</p>
          <p className="muted">{ativas} ativas para composicao</p>
        </article>
        <article className="card">
          <h3>Mapas SIG</h3>
          <p className="geo-kpi-valor">{mapas.length}</p>
          <p className="muted">{publicados} publicados no geoportal</p>
        </article>
        <article className="card">
          <h3>Elementos</h3>
          <p className="geo-kpi-valor">{features.length}</p>
          <p className="muted">pontos de interesse georreferenciados</p>
        </article>
        <article className="card">
          <h3>Servicos</h3>
          <p className="geo-kpi-valor">{servicos.length}</p>
          <p className="muted">{servicosAtivos} ativos para consulta</p>
        </article>
      </div>

      <section className="card geo-lista">
        <div className="geo-lista-header">
          <h3>Situacao dos mapas</h3>
        </div>
        {mapas.length === 0 ? (
          <p className="muted">Nenhum mapa cadastrado.</p>
        ) : (
          <ul className="geo-lista-situacao">
            {mapas.map((m) => (
              <li key={m.id}>
                <span>
                  <strong>{m.codigo}</strong> — {m.nome}
                </span>
                <StatusGeo value={m.situacao} />
              </li>
            ))}
          </ul>
        )}
      </section>
    </section>
  );
}
