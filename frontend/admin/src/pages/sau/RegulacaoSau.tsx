import { useState, type FormEvent } from 'react';
import { autorizarRegulacaoSau, negarRegulacaoSau, solicitarRegulacaoSau, type RegulacaoSau } from '../../lib/api';
import { TabelaEstado } from '../../components/DataState';
import { Field, formatarData, pacienteNome, StatusBadge, type ExecutarSau, type SauResources } from './SauShared';

export function RegulacaoSau({ resources, executar, salvando }: { resources: SauResources; executar: ExecutarSau; salvando: boolean }) {
  const [pacienteId, setPacienteId] = useState('');
  const [procedimento, setProcedimento] = useState('');
  const [prioridade, setPrioridade] = useState('rotina');
  const [solicitante, setSolicitante] = useState('');
  const [justificativa, setJustificativa] = useState('');
  const pacientes = resources.pacientes.data ?? [];
  const regulacoes = resources.regulacoes.data ?? [];

  async function solicitar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => solicitarRegulacaoSau({ paciente_id: pacienteId, procedimento: procedimento.trim(), prioridade, solicitante: solicitante.trim() }), 'Solicitação enviada à central de regulação.');
    if (ok) { setProcedimento(''); setSolicitante(''); setJustificativa(''); }
  }

  async function decidir(regulacao: RegulacaoSau, autorizar: boolean) {
    await executar(autorizar ? () => autorizarRegulacaoSau(regulacao.id) : () => negarRegulacaoSau(regulacao.id, justificativa.trim() || 'Não informado'), `Solicitação ${autorizar ? 'autorizada' : 'negada'}.`);
  }

  return <div className="sau-grid">
    <article className="card sau-card">
      <h3>Nova solicitação</h3><p className="muted">Fila para procedimentos e consultas especializadas.</p>
      <form className="sau-form" onSubmit={solicitar}>
        <Field label="Cidadão" value={pacienteId} onChange={setPacienteId} required><select value={pacienteId} onChange={(e) => setPacienteId(e.target.value)} required><option value="">Selecione…</option>{pacientes.map((p) => <option key={p.id} value={p.id}>{p.nome} · {p.cns}</option>)}</select></Field>
        <Field label="Procedimento / exame" value={procedimento} onChange={setProcedimento} required placeholder="Especialidade solicitada" />
        <Field label="Prioridade" value={prioridade} onChange={setPrioridade}><select value={prioridade} onChange={(e) => setPrioridade(e.target.value)}><option value="rotina">Rotina</option><option value="prioritaria">Prioritária</option><option value="urgencia">Urgência</option></select></Field>
        <Field label="Profissional solicitante" value={solicitante} onChange={setSolicitante} />
        <Field label="Justificativa para negativa" value={justificativa} onChange={setJustificativa} hint="Usada somente na ação Negar." />
        <button className="button" type="submit" disabled={salvando}>Enviar solicitação</button>
      </form>
    </article>
    <article className="card sau-card sau-card--full">
      <h3>Central de regulação</h3>
      <TabelaEstado loading={resources.regulacoes.loading} erro={resources.regulacoes.erro} vazio={regulacoes.length === 0}>
        <div className="table-wrap"><table className="table"><thead><tr><th>Cidadão</th><th>Procedimento</th><th>Prioridade</th><th>Solicitante</th><th>Data</th><th>Status</th><th>Decisão</th></tr></thead><tbody>
          {regulacoes.map((r) => <tr key={r.id}><td>{pacienteNome(resources, r.paciente_id)}</td><td>{r.procedimento}</td><td><StatusBadge value={r.prioridade} /></td><td>{r.solicitante || '—'}</td><td>{formatarData(r.data_solicitacao)}</td><td><StatusBadge value={r.status} /></td><td>{r.status === 'solicitada' ? <div className="actions"><button className="link" type="button" disabled={salvando} onClick={() => decidir(r, true)}>Autorizar</button><button className="link sau-danger-link" type="button" disabled={salvando} onClick={() => decidir(r, false)}>Negar</button></div> : <span className="muted">{r.justificativa || '—'}</span>}</td></tr>)}
        </tbody></table></div>
      </TabelaEstado>
    </article>
  </div>;
}
