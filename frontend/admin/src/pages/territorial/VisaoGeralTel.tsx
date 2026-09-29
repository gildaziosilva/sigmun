import type { TelResources } from './TelPage';
import {
  StatusTerr,
  bairroNome,
  formatarDataTerr,
  formatarMoedaTerr,
  formatarNumeroTerr,
  logradouroNome,
} from './TerrShared';

interface Props {
  resources: TelResources;
}

export function VisaoGeralTel({ resources }: Props) {
  const { bairros, logradouros, plantas, georreferencias } = resources;

  const totalBairros = bairros.data?.length ?? 0;
  const bairrosAtivos = bairros.data?.filter((b) => b.situacao === 'ativo').length ?? 0;
  const populacao = bairros.data?.reduce((t, b) => t + b.populacao_estimada, 0) ?? 0;
  const totalLogradouros = logradouros.data?.length ?? 0;
  const logradourosAtivos = logradouros.data?.filter((l) => l.situacao === 'ativo').length ?? 0;
  const plantasVigentes = plantas.data?.filter((p) => p.situacao === 'vigente').length ?? 0;
  const plantasRascunho = plantas.data?.filter((p) => p.situacao === 'rascunho').length ?? 0;
  const totalGeo = georreferencias.data?.length ?? 0;

  const maisCaros = [...(plantas.data ?? [])]
    .filter((p) => p.situacao === 'vigente')
    .sort((a, b) => b.valor_terreno_m2 - a.valor_terreno_m2)
    .slice(0, 5);

  return (
    <section className="stack terr-visao-geral">
      <div className="card-grid terr-kpis">
        <article className="card kpi">
          <h3>Bairros / divisões</h3>
          <p className="kpi-value">{formatarNumeroTerr(totalBairros)}</p>
        </article>
        <article className="card kpi">
          <h3>Bairros ativos</h3>
          <p className="kpi-value">{formatarNumeroTerr(bairrosAtivos)}</p>
        </article>
        <article className="card kpi">
          <h3>População estimada</h3>
          <p className="kpi-value">{formatarNumeroTerr(populacao)}</p>
        </article>
        <article className="card kpi">
          <h3>Logradouros cadastrados</h3>
          <p className="kpi-value">{formatarNumeroTerr(totalLogradouros)}</p>
        </article>
        <article className="card kpi">
          <h3>Logradouros ativos</h3>
          <p className="kpi-value">{formatarNumeroTerr(logradourosAtivos)}</p>
        </article>
        <article className="card kpi">
          <h3>Plantas vigentes</h3>
          <p className="kpi-value">{formatarNumeroTerr(plantasVigentes)}</p>
        </article>
        <article className="card kpi">
          <h3>Plantas em rascunho</h3>
          <p className="kpi-value">{formatarNumeroTerr(plantasRascunho)}</p>
        </article>
        <article className="card kpi">
          <h3>Georreferências</h3>
          <p className="kpi-value">{formatarNumeroTerr(totalGeo)}</p>
        </article>
      </div>

      <div className="terr-recentes">
        <section className="card terr-recentes-card">
          <h3>Maiores valores de terreno vigentes (R$/m²)</h3>
          {maisCaros.length === 0 ? (
            <p className="muted">Nenhuma planta vigente cadastrada.</p>
          ) : (
            <table className="terr-table">
              <thead>
                <tr>
                  <th>Ano</th>
                  <th>Bairro</th>
                  <th>Ocupação</th>
                  <th className="num">Terreno</th>
                  <th className="num">Construção</th>
                  <th className="num">Alíquota</th>
                </tr>
              </thead>
              <tbody>
                {maisCaros.map((p) => (
                  <tr key={p.id}>
                    <td>{p.ano}</td>
                    <td>{bairroNome(bairros.data ?? [], p.bairro_id)}</td>
                    <td>{p.ocupacao}</td>
                    <td className="num">{formatarMoedaTerr(p.valor_terreno_m2)}</td>
                    <td className="num">{formatarMoedaTerr(p.valor_construcao_m2)}</td>
                    <td className="num">{formatarNumeroTerr(p.aliquota_percent, 2)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>

        <section className="card terr-recentes-card">
          <h3>Cobertura territorial</h3>
          <table className="terr-table">
            <thead>
              <tr>
                <th>Bairro</th>
                <th>Tipo</th>
                <th className="num">Área (km²)</th>
                <th className="num">População</th>
                <th className="num">Logradouros</th>
                <th>Situação</th>
              </tr>
            </thead>
            <tbody>
              {(bairros.data ?? []).map((b) => (
                <tr key={b.id}>
                  <td>{b.nome}</td>
                  <td>{b.tipo.replaceAll('_', ' ')}</td>
                  <td className="num">{formatarNumeroTerr(b.area_km2, 2)}</td>
                  <td className="num">{formatarNumeroTerr(b.populacao_estimada)}</td>
                  <td className="num">
                    {formatarNumeroTerr(
                      (logradouros.data ?? []).filter((l) => l.bairro_id === b.id).length,
                    )}
                  </td>
                  <td><StatusTerr value={b.situacao} /></td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <section className="card terr-recentes-card">
          <h3>Georreferências territoriais</h3>
          {(georreferencias.data ?? []).length === 0 ? (
            <p className="muted">Nenhuma georreferência registrada.</p>
          ) : (
            <table className="terr-table">
              <thead>
                <tr>
                  <th>Referência</th>
                  <th>Geometria</th>
                  <th className="num">Latitude</th>
                  <th className="num">Longitude</th>
                  <th>Datum</th>
                  <th className="num">Precisão</th>
                  <th>Levantamento</th>
                </tr>
              </thead>
              <tbody>
                {(georreferencias.data ?? []).map((g) => (
                  <tr key={g.id}>
                    <td>
                      {g.bairro_id
                        ? bairroNome(bairros.data ?? [], g.bairro_id)
                        : logradouroNome(logradouros.data ?? [], g.logradouro_id)}
                    </td>
                    <td>{g.geometria}</td>
                    <td className="num">{formatarNumeroTerr(g.latitude, 6)}</td>
                    <td className="num">{formatarNumeroTerr(g.longitude, 6)}</td>
                    <td>{g.datum.toUpperCase()}</td>
                    <td className="num">{formatarNumeroTerr(g.precisao_m, 2)} m</td>
                    <td>{formatarDataTerr(g.data_levantamento)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>
      </div>
    </section>
  );
}

