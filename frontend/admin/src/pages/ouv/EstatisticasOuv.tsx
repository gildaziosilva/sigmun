import type { OuvResources } from './OuvShared';
import type { EstatisticasOuv } from '../../lib/api';
import { StatusBadge, PrioridadeBadge, TipoManifestacaoBadge, TipoDenunciaBadge, NivelSigiloBadge, formatarNumero, formatarData, getProtocolo, getCidadaoNome } from './OuvShared';

export function EstatisticasOuv({ resources, estatisticas }: { resources: OuvResources; estatisticas: EstatisticasOuv | null }) {
  const manifestacoes = resources.manifestacoes.data ?? [];
  const denuncias = resources.denuncias.data ?? [];
  const pedidosLai = resources.pedidosLai.data ?? [];

  const gerais = estatisticas?.gerais ?? { total: 0, respondidas: 0, concluidas: 0, vencidas: 0, taxa_resposta: 0, taxa_conclusao: 0 };
  
  // Estatísticas por tipo de manifestação
  const statsManifestacoes = {
    sugestao: manifestacoes.filter(m => m.tipo === 'sugestao').length,
    elogio: manifestacoes.filter(m => m.tipo === 'elogio').length,
    reclamacao: manifestacoes.filter(m => m.tipo === 'reclamacao').length,
    solicitacao: manifestacoes.filter(m => m.tipo === 'solicitacao').length,
  };

  const statsDenuncias = {
    corrupcao: denuncias.filter(d => d.tipo_denuncia === 'corrupcao').length,
    improbidade: denuncias.filter(d => d.tipo_denuncia === 'improbidade').length,
    assedio: denuncias.filter(d => d.tipo_denuncia === 'assedio').length,
    desvio_verba: denuncias.filter(d => d.tipo_denuncia === 'desvio_verba').length,
    nepotismo: denuncias.filter(d => d.tipo_denuncia === 'nepotismo').length,
    fraude_licitacao: denuncias.filter(d => d.tipo_denuncia === 'fraude_licitacao').length,
    outro: denuncias.filter(d => d.tipo_denuncia === 'outro').length,
  };

  const statsLai = {
    publico: pedidosLai.filter(p => p.nivel_sigilo === 'publico').length,
    restrito: pedidosLai.filter(p => p.nivel_sigilo === 'restrito').length,
    sigiloso: pedidosLai.filter(p => p.nivel_sigilo === 'sigiloso').length,
    ultra_sigiloso: pedidosLai.filter(p => p.nivel_sigilo === 'ultra_sigiloso').length,
    recursos: pedidosLai.filter(p => p.is_recurso).length,
  };

  // Status breakdown
  const statusCounts = {
    registrada: 0,
    em_analise: 0,
    encaminhada: 0,
    em_tratamento: 0,
    aguardando_complementacao: 0,
    respondida: 0,
    concluida: 0,
    arquivada: 0,
    cancelada: 0,
  };
  [...manifestacoes, ...denuncias, ...pedidosLai].forEach(m => {
    if (statusCounts[m.status as keyof typeof statusCounts] !== undefined) {
      statusCounts[m.status as keyof typeof statusCounts]++;
    }
  });

  // Prazos
  const comPrazo = [...manifestacoes, ...denuncias, ...pedidosLai].filter(m => m.prazo);
  const vencidas = comPrazo.filter(m => m.prazo!.vencido).length;
  const vencendo3 = comPrazo.filter(m => m.prazo && !m.prazo.vencido && m.prazo.dias_restantes <= 3).length;
  const vencendo7 = comPrazo.filter(m => m.prazo && !m.prazo.vencido && m.prazo.dias_restantes <= 7).length;

  return (
    <div className="stack">
      <h2>Estatísticas da Ouvidoria</h2>

      <section className="card">
        <h3>Indicadores Gerais (Ano Atual)</h3>
        <div className="ouv-metrics-grid">
          <article className="ouv-metric-card"><span>Total</span><strong>{formatarNumero(gerais.total)}</strong></article>
          <article className="ouv-metric-card"><span>Respondidas</span><strong>{formatarNumero(gerais.respondidas)}</strong><small>{gerais.taxa_resposta}%</small></article>
          <article className="ouv-metric-card"><span>Concluídas</span><strong>{formatarNumero(gerais.concluidas)}</strong><small>{gerais.taxa_conclusao}%</small></article>
          <article className="ouv-metric-card ouv-metric-card--alerta"><span>Vencidas</span><strong>{formatarNumero(gerais.vencidas)}</strong></article>
          <article className="ouv-metric-card"><span>Vencendo ≤ 3 dias</span><strong>{formatarNumero(vencendo3)}</strong></article>
          <article className="ouv-metric-card"><span>Vencendo ≤ 7 dias</span><strong>{formatarNumero(vencendo7)}</strong></article>
        </div>
      </section>

      <section className="card">
        <h3>Distribuição por Status</h3>
        <div className="ouv-status-grid">
          {Object.entries(statusCounts).map(([status, count]) => (
            <article key={status} className="ouv-status-stat">
              <StatusBadge value={status} />
              <span className="ouv-status-label">{status.replace('_', ' ')}</span>
              <strong>{formatarNumero(count)}</strong>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <h3>Manifestações por Tipo</h3>
        <div className="ouv-tipo-grid">
          {Object.entries(statsManifestacoes).map(([tipo, count]) => (
            <article key={tipo} className="ouv-tipo-stat">
              <TipoManifestacaoBadge value={tipo} />
              <span className="ouv-tipo-label">{tipo}</span>
              <strong>{formatarNumero(count)}</strong>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <h3>Denúncias por Tipo</h3>
        <div className="ouv-tipo-grid">
          {Object.entries(statsDenuncias).map(([tipo, count]) => (
            <article key={tipo} className="ouv-tipo-stat">
              <TipoDenunciaBadge value={tipo} />
              <span className="ouv-tipo-label">{tipo.replace('_', ' ')}</span>
              <strong>{formatarNumero(count)}</strong>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <h3>Pedidos LAI por Nível de Sigilo</h3>
        <div className="ouv-tipo-grid">
          {Object.entries(statsLai).map(([nivel, count]) => (
            <article key={nivel} className="ouv-tipo-stat">
              <NivelSigiloBadge value={nivel} />
              <span className="ouv-tipo-label">{nivel.replace('_', ' ')}</span>
              <strong>{formatarNumero(count)}</strong>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <h3>Prazos de Resposta</h3>
        <div className="ouv-prazo-grid">
          <article className="ouv-prazo-stat"><span>Com prazo definido</span><strong>{formatarNumero(comPrazo.length)}</strong></article>
          <article className="ouv-prazo-stat ouv-prazo-stat--ok"><span>No prazo</span><strong>{formatarNumero(comPrazo.length - vencidas - vencendo3 - vencendo7)}</strong></article>
          <article className="ouv-prazo-stat ouv-prazo-stat--warning"><span>Vencendo ≤ 7 dias</span><strong>{formatarNumero(vencendo7)}</strong></article>
          <article className="ouv-prazo-stat ouv-prazo-stat--danger"><span>Vencendo ≤ 3 dias</span><strong>{formatarNumero(vencendo3)}</strong></article>
          <article className="ouv-prazo-stat ouv-prazo-stat--danger"><span>Vencidas</span><strong>{formatarNumero(vencidas)}</strong></article>
        </div>
      </section>

      <section className="card">
        <h3>Últimas 20 Manifestações</h3>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Protocolo</th>
                <th>Tipo</th>
                <th>Assunto</th>
                <th>Cidadão</th>
                <th>Status</th>
                <th>Prioridade</th>
                <th>Prazo</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>
              {[...manifestacoes, ...denuncias, ...pedidosLai]
                .sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
                .slice(0, 20)
                .map((m: any) => (
                  <tr key={m.id}>
                    <td><code>{getProtocolo(m)}</code></td>
                    <td>{m.tipo_denuncia ? <TipoDenunciaBadge value={m.tipo_denuncia} /> : m.nivel_sigilo ? <NivelSigiloBadge value={m.nivel_sigilo} /> : <TipoManifestacaoBadge value={m.tipo} />}</td>
                    <td>{m.assunto}</td>
                    <td>{getCidadaoNome(m)}</td>
                    <td><StatusBadge value={m.status} /></td>
                    <td><PrioridadeBadge value={m.prioridade} /></td>
                    <td>{m.prazo ? <span className={m.prazo.vencido ? 'ouv-prazo-vencido' : ''}>{formatarData(m.prazo.data_limite)}</span> : '—'}</td>
                    <td>{formatarData(m.created_at)}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
