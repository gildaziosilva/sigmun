import { useState, type FormEvent } from 'react';
import { criarMedicamentoSau, dispensarMedicamentoSau, reporEstoqueSau, type MedicamentoSau } from '../../lib/api';
import { TabelaEstado } from '../../components/DataState';
import { Field, formatarNumero, StatusBadge, type ExecutarSau, type SauResources } from './SauShared';

export function FarmaciaSau({ resources, executar, salvando }: { resources: SauResources; executar: ExecutarSau; salvando: boolean }) {
  const [nome, setNome] = useState('');
  const [apresentacao, setApresentacao] = useState('');
  const [estoque, setEstoque] = useState('');
  const [minimo, setMinimo] = useState('');
  const [medicamentoId, setMedicamentoId] = useState('');
  const [reposicao, setReposicao] = useState('');
  const [pacienteId, setPacienteId] = useState('');
  const [quantidade, setQuantidade] = useState('');
  const [receita, setReceita] = useState('');
  const medicamentos = resources.medicamentos.data ?? [];
  const pacientes = resources.pacientes.data ?? [];

  async function cadastrar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => criarMedicamentoSau({ nome: nome.trim(), apresentacao: apresentacao.trim(), estoque: Number(estoque), estoque_minimo: Number(minimo) }), 'Medicamento cadastrado.');
    if (ok) { setNome(''); setApresentacao(''); setEstoque(''); setMinimo(''); }
  }

  async function repor(medicamento: MedicamentoSau) {
    const alvo = medicamento.id === medicamentoId ? medicamento : medicamentos.find((item) => item.id === medicamentoId);
    if (!alvo) return;
    await executar(() => reporEstoqueSau(alvo.id, Number(reposicao)), `Estoque de ${alvo.nome} atualizado.`);
    if (reposicao) setReposicao('');
  }

  async function dispensar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => dispensarMedicamentoSau({ paciente_id: pacienteId, medicamento_id: medicamentoId, quantidade: Number(quantidade), receita: receita.trim() }), 'Dispensação registrada.');
    if (ok) { setQuantidade(''); setReceita(''); }
  }

  return <div className="sau-grid">
    <article className="card sau-card">
      <h3>Elenco da farmácia</h3><p className="muted">Cadastre medicamentos e defina o estoque mínimo.</p>
      <form className="sau-form" onSubmit={cadastrar}>
        <Field label="Medicamento" value={nome} onChange={setNome} required placeholder="Nome genérico" />
        <Field label="Apresentação" value={apresentacao} onChange={setApresentacao} placeholder="Comprimido, frasco…" />
        <Field label="Estoque inicial" value={estoque} onChange={setEstoque} type="number" min="0" step="0.01" required />
        <Field label="Estoque mínimo" value={minimo} onChange={setMinimo} type="number" min="0" step="0.01" required />
        <button className="button" type="submit" disabled={salvando}>Cadastrar medicamento</button>
      </form>
    </article>
    <article className="card sau-card">
      <h3>Dispensação</h3><p className="muted">Entrega registrada e baixa automática de estoque.</p>
      <form className="sau-form" onSubmit={dispensar}>
        <Field label="Cidadão" value={pacienteId} onChange={setPacienteId} required><select value={pacienteId} onChange={(e) => setPacienteId(e.target.value)} required><option value="">Selecione…</option>{pacientes.map((p) => <option key={p.id} value={p.id}>{p.nome} · {p.cns}</option>)}</select></Field>
        <Field label="Medicamento" value={medicamentoId} onChange={setMedicamentoId} required><select value={medicamentoId} onChange={(e) => setMedicamentoId(e.target.value)} required><option value="">Selecione…</option>{medicamentos.map((m) => <option key={m.id} value={m.id}>{m.nome} · {formatarNumero(m.estoque)} em estoque</option>)}</select></Field>
        <Field label="Quantidade" value={quantidade} onChange={setQuantidade} type="number" min="0.01" step="0.01" required />
        <Field label="Receita / observação" value={receita} onChange={setReceita} />
        <button className="button" type="submit" disabled={salvando}>Dispensar medicamento</button>
      </form>
    </article>
    <article className="card sau-card sau-card--full">
      <div className="sau-card-title"><div><h3>Posição de estoque</h3><p className="muted">Selecione um item para repor.</p></div><Field label="Medicamento" value={medicamentoId} onChange={setMedicamentoId}><select value={medicamentoId} onChange={(e) => setMedicamentoId(e.target.value)}><option value="">Selecione…</option>{medicamentos.map((m) => <option key={m.id} value={m.id}>{m.nome}</option>)}</select></Field><Field label="Quantidade" value={reposicao} onChange={setReposicao} type="number" min="0.01" step="0.01" /><button className="button" type="button" disabled={!medicamentoId || !reposicao || salvando} onClick={() => { const alvo = medicamentos.find((m) => m.id === medicamentoId); if (alvo) void repor(alvo); }}>Repor estoque</button></div>
      <TabelaEstado loading={resources.medicamentos.loading} erro={resources.medicamentos.erro} vazio={medicamentos.length === 0}>
        <div className="table-wrap"><table className="table"><thead><tr><th>Medicamento</th><th>Apresentação</th><th>Estoque</th><th>Mínimo</th><th>Situação</th></tr></thead><tbody>{medicamentos.map((m) => <tr key={m.id}><td>{m.nome}</td><td>{m.apresentacao || '—'}</td><td>{formatarNumero(m.estoque)}</td><td>{formatarNumero(m.estoque_minimo)}</td><td><StatusBadge value={m.estoque < m.estoque_minimo ? 'repor' : 'disponivel'} /></td></tr>)}</tbody></table></div>
      </TabelaEstado>
    </article>
  </div>;
}
