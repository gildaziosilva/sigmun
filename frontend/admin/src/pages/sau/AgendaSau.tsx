import { useState, type FormEvent } from 'react';
import { agendarConsultaSau, cancelarAgendamentoSau, confirmarAgendamentoSau, realizarAgendamentoSau, type AgendamentoSau } from '../../lib/api';
import { TabelaEstado } from '../../components/DataState';
import { Field, formatarData, pacienteNome, StatusBadge, type ExecutarSau, type SauResources } from './SauShared';

export function AgendaSau({ resources, executar, salvando }: { resources: SauResources; executar: ExecutarSau; salvando: boolean }) {
  const [pacienteId, setPacienteId] = useState('');
  const [especialidade, setEspecialidade] = useState('');
  const [data, setData] = useState('');
  const [hora, setHora] = useState('');
  const [estabelecimento, setEstabelecimento] = useState('');
  const [filtro, setFiltro] = useState('todos');
  const agendamentos = resources.agendamentos.data ?? [];
  const pacientes = resources.pacientes.data ?? [];
  const visiveis = filtro === 'todos' ? agendamentos : agendamentos.filter((a) => a.status === filtro);

  async function agendar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => agendarConsultaSau({ paciente_id: pacienteId, especialidade: especialidade.trim(), data, hora, estabelecimento: estabelecimento.trim() }), 'Consulta agendada na fila SUS.');
    if (ok) { setEspecialidade(''); setData(''); setHora(''); setEstabelecimento(''); }
  }

  async function acao(agendamento: AgendamentoSau, tipo: 'confirmar' | 'realizar' | 'cancelar') {
    const acao = tipo === 'confirmar' ? () => confirmarAgendamentoSau(agendamento.id)
      : tipo === 'realizar' ? () => realizarAgendamentoSau(agendamento.id)
        : () => cancelarAgendamentoSau(agendamento.id, 'Cancelado pelo painel administrativo');
    await executar(acao, `Agendamento atualizado: ${tipo}.`);
  }

  return <div className="sau-grid">
    <article className="card sau-card">
      <h3>Nova consulta</h3><p className="muted">Agendamento de especialidade para a rede municipal.</p>
      <form className="sau-form" onSubmit={agendar}>
        <Field label="Cidadão" value={pacienteId} onChange={setPacienteId} required><select value={pacienteId} onChange={(e) => setPacienteId(e.target.value)} required><option value="">Selecione…</option>{pacientes.map((p) => <option key={p.id} value={p.id}>{p.nome} · {p.cns}</option>)}</select></Field>
        <Field label="Especialidade" value={especialidade} onChange={setEspecialidade} required placeholder="Clínica médica" />
        <Field label="Data" value={data} onChange={setData} type="date" required />
        <Field label="Hora" value={hora} onChange={setHora} type="time" required />
        <Field label="Estabelecimento" value={estabelecimento} onChange={setEstabelecimento} placeholder="UBS / unidade de saúde" />
        <button className="button" type="submit" disabled={salvando}>Agendar consulta</button>
      </form>
    </article>
    <article className="card sau-card sau-card--full">
      <div className="sau-card-title"><div><h3>Agenda SUS</h3><p className="muted">Confirmação, comparecimento e cancelamento.</p></div><select className="sau-filter" value={filtro} onChange={(e) => setFiltro(e.target.value)} aria-label="Filtrar agendamentos"><option value="todos">Todos</option><option value="agendado">Agendados</option><option value="confirmado">Confirmados</option><option value="realizado">Realizados</option><option value="cancelado">Cancelados</option></select></div>
      <TabelaEstado loading={resources.agendamentos.loading} erro={resources.agendamentos.erro} vazio={visiveis.length === 0}>
        <div className="table-wrap"><table className="table"><thead><tr><th>Cidadão</th><th>Especialidade</th><th>Data</th><th>Unidade</th><th>Status</th><th>Ações</th></tr></thead><tbody>
          {visiveis.map((a) => <tr key={a.id}><td>{pacienteNome(resources, a.paciente_id)}</td><td>{a.especialidade}</td><td>{formatarData(a.data)} {a.hora || ''}</td><td>{a.estabelecimento || '—'}</td><td><StatusBadge value={a.status} /></td><td><div className="actions">{a.status === 'agendado' && <button className="link" type="button" onClick={() => acao(a, 'confirmar')} disabled={salvando}>Confirmar</button>}{['agendado', 'confirmado'].includes(a.status) && <button className="link" type="button" onClick={() => acao(a, 'realizar')} disabled={salvando}>Realizar</button>}{['agendado', 'confirmado'].includes(a.status) && <button className="link sau-danger-link" type="button" onClick={() => acao(a, 'cancelar')} disabled={salvando}>Cancelar</button>}</div></td></tr>)}
        </tbody></table></div>
      </TabelaEstado>
    </article>
  </div>;
}
