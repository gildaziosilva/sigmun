import type { ObrasPageResources } from './ObrasPage';
import { StatusObras, formatarMoedaObras } from './ObrasShared';

export function VisaoGeralObras({ resources }: { resources: ObrasPageResources }) {
  const obras = resources.obras.data ?? [];

  const emExecucao = obras.filter((o) => o.situacao === 'em_execucao');
  const concluidas = obras.filter((o) => o.situacao === 'concluida');
  const orcado = obras.reduce((total, o) => total + o.valor_orcado, 0);
  const medido = obras.reduce((total, o) => total + o.valor_mediado, 0);
  const pago = obras.reduce((total, o) => total + o.valor_pago, 0);
  const avancoMedio =
    obras.length > 0
      ? obras.reduce((total, o) => total + o.percentual_fisico, 0) / obras.length
      : 0;

  return (
    <section className="stack">
      <div className="obras-kpis">
        <article className="card">
          <h3>Obras</h3>
          <p className="obras-kpi-valor">{obras.length}</p>
          <p className="muted">
            {emExecucao.length} em execucao &middot; {concluidas.length} concluidas
          </p>
        </article>
        <article className="card">
          <h3>Investimento orcado</h3>
          <p className="obras-kpi-valor">{formatarMoedaObras(orcado)}</p>
          <p className="muted">somatorio das obras cadastradas</p>
        </article>
        <article className="card">
          <h3>Medido / Pago</h3>
          <p className="obras-kpi-valor">{formatarMoedaObras(pago)}</p>
          <p className="muted">medido: {formatarMoedaObras(medido)}</p>
        </article>
        <article className="card">
          <h3>Avanco fisico medio</h3>
          <p className="obras-kpi-valor">{avancoMedio.toFixed(1)}%</p>
          <p className="muted">media das obras cadastradas</p>
        </article>
      </div>

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Situacao das obras</h3>
        </div>
        {obras.length === 0 ? (
          <p className="muted">Nenhuma obra cadastrada.</p>
        ) : (
          <ul className="obras-lista-situacao">
            {obras.map((o) => (
              <li key={o.id}>
                <span>
                  <strong>{o.numero}</strong> — {o.nome}
                </span>
                <span className="obras-avanco">
                  {o.percentual_fisico.toFixed(0)}% fisico &middot;{' '}
                  {o.percentual_financeiro.toFixed(0)}% financeiro
                </span>
                <StatusObras value={o.situacao} />
              </li>
            ))}
          </ul>
        )}
      </section>
    </section>
  );
}
