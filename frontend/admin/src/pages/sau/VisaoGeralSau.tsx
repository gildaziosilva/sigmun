import { StatusBadge, formatarData, pacienteNome, type SauResources } from './SauShared';

export function VisaoGeralSau({ resources }: { resources: SauResources }) {
  const agendamentos = resources.agendamentos.data ?? [];
  const regulacoes = resources.regulacoes.data ?? [];
  const medicamentos = resources.medicamentos.data ?? [];
  const estoqueBaixo = medicamentos.filter((m) => m.estoque < m.estoque_minimo);
  const proximos = agendamentos.filter((a) => a.status === 'agendado' || a.status === 'confirmado').slice(0, 6);
  const pendentes = regulacoes.filter((r) => r.status === 'solicitada').slice(0, 6);
  const carregando = resources.pacientes.loading || resources.agendamentos.loading || resources.regulacoes.loading || resources.medicamentos.loading;

  return <div className="stack">
    <div className="sau-metrics">
      <article className="sau-metric"><span>Pacientes</span><strong>{carregando ? '…' : resources.pacientes.data?.length ?? 0}</strong><small>cadastros registrados</small></article>
      <article className="sau-metric"><span>Agenda</span><strong>{carregando ? '…' : proximos.length}</strong><small>consultas pendentes</small></article>
      <article className="sau-metric"><span>Regulação</span><strong>{carregando ? '…' : pendentes.length}</strong><small>solicitações aguardando decisão</small></article>
      <article className={`sau-metric ${estoqueBaixo.length ? 'sau-metric--alerta' : ''}`}><span>Farmácia</span><strong>{carregando ? '…' : estoqueBaixo.length}</strong><small>itens abaixo do mínimo</small></article>
    </div>
    <div className="sau-overview-grid">
      <article className="card">
        <h3>Próximos atendimentos</h3>
        {proximos.length ? <ul className="sau-list">
          {proximos.map((a) => <li key={a.id}><div><strong>{pacienteNome(resources, a.paciente_id)}</strong><small>{a.especialidade} · {formatarData(a.data)} {a.hora || ''}</small></div><StatusBadge value={a.status} /></li>)}
        </ul> : <p className="muted">Nenhuma consulta pendente.</p>}
      </article>
      <article className="card">
        <h3>Regulação pendente</h3>
        {pendentes.length ? <ul className="sau-list">
          {pendentes.map((r) => <li key={r.id}><div><strong>{pacienteNome(resources, r.paciente_id)}</strong><small>{r.procedimento} · {formatarData(r.data_solicitacao)}</small></div><StatusBadge value={r.prioridade} /></li>)}
        </ul> : <p className="muted">Nenhuma solicitação pendente.</p>}
      </article>
      <article className="card sau-card--full">
        <h3>Alertas da farmácia</h3>
        {estoqueBaixo.length ? <ul className="sau-list">
          {estoqueBaixo.map((m) => <li key={m.id}><div><strong>{m.nome}</strong><small>{m.apresentacao || 'Sem apresentação informada'}</small></div><StatusBadge value="repor" /></li>)}
        </ul> : <p className="muted">Nenhum item abaixo do estoque mínimo.</p>}
      </article>
    </div>
  </div>;
}
