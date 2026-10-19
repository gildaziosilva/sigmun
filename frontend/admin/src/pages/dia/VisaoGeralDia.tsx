import { TabelaEstado } from '../../components/DataState';
import {
  DIA_STATUS_DIARIA,
  formatarMoeda,
  resumirDia,
  StatusDiariaBadge,
  StatusPrestacaoBadge,
  type DiaResources,
} from './DiaShared';

export function VisaoGeralDia({ resources }: { resources: DiaResources }) {
  const viagens = resources.viagens.data ?? [];
  const diarias = resources.diariasPorStatus.data ?? [];
  const prestacoes = resources.prestacoesAbertas.data ?? [];
  const resumo = resumirDia(viagens, diarias, prestacoes);
  const erro = resources.viagens.erro || resources.diariasPorStatus.erro || resources.prestacoesAbertas.erro;
  const loading = resources.viagens.loading || resources.diariasPorStatus.loading || resources.prestacoesAbertas.loading;

  return (
    <div>
      <div className="card-grid">
        <article className="card kpi">
          <h3>Viagens</h3>
          <p className="kpi-value">{resumo.totalViagens}</p>
          <p className="muted">Viagens registradas</p>
        </article>
        <article className="card kpi">
          <h3>Diárias</h3>
          <p className="kpi-value">{resumo.totalDiarias}</p>
          <p className="muted">Valor total: {formatarMoeda(resumo.valorTotal)}</p>
        </article>
        <article className="card kpi">
          <h3>Prestações abertas</h3>
          <p className="kpi-value">{resumo.prestacoesAbertas}</p>
          <p className="muted">Aguardando análise</p>
        </article>
        <article className="card kpi">
          <h3>Valor glosado</h3>
          <p className="kpi-value">{formatarMoeda(resumo.valorGlosado)}</p>
          <p className="muted">Total glosado em diárias</p>
        </article>
      </div>

      <article className="card">
        <div className="page-head">
          <div>
            <h3>Diárias por status</h3>
            <p className="muted">Distribuição das diárias consultadas por situação.</p>
          </div>
        </div>
        <TabelaEstado loading={loading} erro={erro} vazio={!loading && !erro && diarias.length === 0 && prestacoes.length === 0}>
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Status</th>
                  <th>Quantidade</th>
                </tr>
              </thead>
              <tbody>
                {DIA_STATUS_DIARIA.filter((s) => (resumo.porStatus[s.value] ?? 0) > 0).map((s) => (
                  <tr key={s.value}>
                    <td><StatusDiariaBadge value={s.value} /></td>
                    <td>{resumo.porStatus[s.value]}</td>
                  </tr>
                ))}
                {prestacoes.slice(0, 5).map((p) => (
                  <tr key={`prest-${p.id}`}>
                    <td>Prestação <StatusPrestacaoBadge value={p.status} /></td>
                    <td className="mono">{p.diaria_id.slice(0, 8)}…</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>
    </div>
  );
}
