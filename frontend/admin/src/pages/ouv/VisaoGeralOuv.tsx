import type { OuvResources } from './OuvShared';
import type { EstatisticasOuv } from '../../lib/api';
import { StatusBadge, getProtocolo, getCidadaoNome, PrioridadeBadge, TipoManifestacaoBadge, PrazoBadge, CanalBadge } from './OuvShared';

export function VisaoGeralOuv({ resources, estatisticas }: { resources: OuvResources; estatisticas: EstatisticasOuv | null }) {
  const manifestacoes = resources.manifestacoes.data ?? [];
  const denuncias = resources.denuncias.data ?? [];
  const pedidosLai = resources.pedidosLai.data ?? [];

  const todas = [...manifestacoes, ...denuncias, ...pedidosLai];
  const proximas = todas.filter((m: any) => m.status === 'registrada' || m.status === 'em_analise' || m.status === 'encaminhada' || m.status === 'em_tratamento' || m.status === 'aguardando_complementacao').slice(0, 6);
  const vencendo = todas.filter((m: any) => m.prazo && !m.prazo.vencido && m.prazo.dias_restantes <= 7).slice(0, 6);
  const carregando = resources.manifestacoes.loading || resources.denuncias.loading || resources.pedidosLai.loading;

  const gerais = estatisticas?.gerais ?? { total: 0, respondidas: 0, concluidas: 0, vencidas: 0, taxa_resposta: 0, taxa_conclusao: 0 };

  return (
    <div className="stack">
      <div className="ouv-metrics">
        <article className="ouv-metric">
          <span>Total</span>
          <strong>{carregando ? '…' : gerais.total}</strong>
          <small>manifestações no ano</small>
        </article>
        <article className="ouv-metric">
          <span>Respondidas</span>
          <strong>{carregando ? '…' : gerais.respondidas}</strong>
          <small>taxa {gerais.taxa_resposta}%</small>
        </article>
        <article className="ouv-metric">
          <span>Concluídas</span>
          <strong>{carregando ? '…' : gerais.concluidas}</strong>
          <small>taxa {gerais.taxa_conclusao}%</small>
        </article>
        <article className={"ouv-metric " + (gerais.vencidas ? 'ouv-metric--alerta' : '')}>
          <span>Vencidas</span>
          <strong>{carregando ? '…' : gerais.vencidas}</strong>
          <small>prazo expirado</small>
        </article>
        <article className="ouv-metric">
          <span>Denúncias</span>
          <strong>{carregando ? '…' : denuncias.length}</strong>
          <small>recebidas no ano</small>
        </article>
        <article className="ouv-metric">
          <span>Pedidos LAI</span>
          <strong>{carregando ? '…' : pedidosLai.length}</strong>
          <small>recebidos no ano</small>
        </article>
      </div>

      <div className="ouv-overview-grid">
        <article className="card">
          <h3>Próximas a tratar</h3>
          {proximas.length ? (
            <ul className="ouv-list">
              {proximas.map((m: any) => (
                <li key={m.id}>
                  <div>
                    <strong>{getProtocolo(m)}</strong>
                    <small>{m.assunto}</small>
                  </div>
                  <div className="ouv-item-badges">
                    <StatusBadge value={m.status} />
                    <PrioridadeBadge value={m.prioridade} />
                  </div>
                </li>
              ))}
            </ul>
          ) : (
            <p className="muted">Nenhuma manifestação pendente.</p>
          )}
        </article>

        <article className="card">
          <h3>Prazos vencendo (≤ 7 dias)</h3>
          {vencendo.length ? (
            <ul className="ouv-list">
              {vencendo.map((m: any) => (
                <li key={m.id}>
                  <div>
                    <strong>{getProtocolo(m)}</strong>
                    <small>{m.assunto}</small>
                  </div>
                  <PrazoBadge prazo={m.prazo} />
                </li>
              ))}
            </ul>
          ) : (
            <p className="muted">Nenhum prazo vencendo.</p>
          )}
        </article>

        <article className="card ouv-card--full">
          <h3>Últimas registradas</h3>
          {todas.slice(0, 10).length ? (
            <ul className="ouv-list">
              {todas.slice(0, 10).map((m: any) => (
                <li key={m.id}>
                  <div>
                    <strong>{getProtocolo(m)}</strong>
                    <small>{m.assunto} · {getCidadaoNome(m)}</small>
                  </div>
                  <div className="ouv-item-badges">
                    <TipoManifestacaoBadge value={m.tipo} />
                    <StatusBadge value={m.status} />
                    <CanalBadge value={m.canal} />
                  </div>
                </li>
              ))}
            </ul>
          ) : (
            <p className="muted">Nenhuma manifestação registrada.</p>
          )}
        </article>
      </div>
    </div>
  );
}
