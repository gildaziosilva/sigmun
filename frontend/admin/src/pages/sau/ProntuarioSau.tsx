import { useState, type FormEvent } from 'react';
import { criarPacienteSau, obterProntuarioSau, registrarAtendimentoSau, type AtendimentoSau } from '../../lib/api';
import { TabelaEstado } from '../../components/DataState';
import { Field, formatarData, StatusBadge, type ExecutarSau, type SauResources } from './SauShared';

export function ProntuarioSau({ resources, executar, salvando }: { resources: SauResources; executar: ExecutarSau; salvando: boolean }) {
  const [nome, setNome] = useState('');
  const [cns, setCns] = useState('');
  const [cpf, setCpf] = useState('');
  const [nascimento, setNascimento] = useState('');
  const [sexo, setSexo] = useState('ignorado');
  const [telefone, setTelefone] = useState('');
  const [endereco, setEndereco] = useState('');
  const [ubs, setUbs] = useState('');
  const [pacienteId, setPacienteId] = useState('');
  const [tipo, setTipo] = useState('consulta');
  const [profissional, setProfissional] = useState('');
  const [estabelecimento, setEstabelecimento] = useState('');
  const [queixa, setQueixa] = useState('');
  const [conduta, setConduta] = useState('');
  const [cid10, setCid10] = useState('');
  const [historico, setHistorico] = useState<AtendimentoSau[] | null>(null);
  const [historicoErro, setHistoricoErro] = useState('');
  const pacientes = resources.pacientes.data ?? [];

  async function cadastrar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => criarPacienteSau({
      nome: nome.trim(), cns: cns.trim(), cpf: cpf.trim(), data_nascimento: nascimento,
      sexo, telefone: telefone.trim(), endereco: endereco.trim(), ubs_referencia: ubs.trim(),
    }), 'Paciente cadastrado com sucesso.');
    if (ok) { setNome(''); setCns(''); setCpf(''); setNascimento(''); setTelefone(''); setEndereco(''); setUbs(''); }
  }

  async function registrar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => registrarAtendimentoSau({
      paciente_id: pacienteId, tipo, profissional: profissional.trim(), estabelecimento: estabelecimento.trim(),
      queixa: queixa.trim(), conduta: conduta.trim(), cid10: cid10.trim(),
    }), 'Atendimento registrado no prontuário.');
    if (ok) { setQueixa(''); setConduta(''); setCid10(''); setHistorico(null); }
  }

  async function consultar() {
    setHistoricoErro('');
    try { setHistorico(await obterProntuarioSau(pacienteId)); }
    catch (erro) { setHistorico(null); setHistoricoErro(erro instanceof Error ? erro.message : 'Falha ao consultar prontuário.'); }
  }


  return <div className="sau-grid">
    <article className="card sau-card">
      <h3>Cadastro do cidadão</h3><p className="muted">CNS obrigatório e único.</p>
      <form className="sau-form" onSubmit={cadastrar}>
        <Field label="Nome" value={nome} onChange={setNome} required />
        <Field label="CNS" value={cns} onChange={setCns} required hint="15 dígitos numéricos." />
        <Field label="CPF" value={cpf} onChange={setCpf} />
        <Field label="Nascimento" value={nascimento} onChange={setNascimento} type="date" />
        <Field label="Sexo" value={sexo} onChange={setSexo}><select value={sexo} onChange={(e) => setSexo(e.target.value)}><option value="ignorado">Ignorado</option><option value="feminino">Feminino</option><option value="masculino">Masculino</option></select></Field>
        <Field label="Telefone" value={telefone} onChange={setTelefone} />
        <Field label="Endereço" value={endereco} onChange={setEndereco} />
        <Field label="UBS de referência" value={ubs} onChange={setUbs} />
        <button className="button" type="submit" disabled={salvando}>Cadastrar paciente</button>
      </form>
    </article>
    <article className="card sau-card">
      <h3>Registro assistencial</h3>
      <form className="sau-form" onSubmit={registrar}>
        <Field label="Paciente" value={pacienteId} onChange={setPacienteId} required><select value={pacienteId} onChange={(e) => setPacienteId(e.target.value)} required><option value="">Selecione…</option>{pacientes.map((p) => <option key={p.id} value={p.id}>{p.nome} · {p.cns}</option>)}</select></Field>
        <Field label="Tipo" value={tipo} onChange={setTipo}><select value={tipo} onChange={(e) => setTipo(e.target.value)}><option value="consulta">Consulta</option><option value="retorno">Retorno</option><option value="urgencia">Urgência</option><option value="visita_domiciliar">Visita domiciliar</option><option value="teleatendimento">Teleatendimento</option></select></Field>
        <Field label="Profissional" value={profissional} onChange={setProfissional} required />
        <Field label="Estabelecimento" value={estabelecimento} onChange={setEstabelecimento} required />
        <Field label="CID-10" value={cid10} onChange={setCid10} />
        <label className="sau-field sau-field--wide"><span>Queixa</span><textarea rows={2} value={queixa} onChange={(e) => setQueixa(e.target.value)} /></label>
        <label className="sau-field sau-field--wide"><span>Conduta</span><textarea rows={2} value={conduta} onChange={(e) => setConduta(e.target.value)} /></label>
        <div className="actions"><button className="button" type="submit" disabled={salvando}>Registrar atendimento</button><button className="button button--ghost" type="button" onClick={consultar} disabled={!pacienteId}>Consultar histórico</button></div>
      </form>
      {historicoErro && <p className="alert alert--error" role="alert">{historicoErro}</p>}
      {historico && <TabelaEstado loading={false} erro="" vazio={historico.length === 0}><div className="table-wrap"><table className="table"><thead><tr><th>Data</th><th>Tipo</th><th>Profissional</th><th>CID-10</th><th>Queixa</th></tr></thead><tbody>{historico.map((a) => <tr key={a.id}><td>{formatarData(a.data)}</td><td><StatusBadge value={a.tipo} /></td><td>{a.profissional}<br /><small>{a.estabelecimento}</small></td><td>{a.cid10 || '—'}</td><td>{a.queixa || '—'}</td></tr>)}</tbody></table></div></TabelaEstado>}
    </article>
    <article className="card sau-card sau-card--full">
      <h3>Pacientes cadastrados</h3>
      <TabelaEstado loading={resources.pacientes.loading} erro={resources.pacientes.erro} vazio={pacientes.length === 0}><div className="table-wrap"><table className="table"><thead><tr><th>Nome</th><th>CNS</th><th>Nascimento</th><th>Sexo</th><th>UBS</th><th>Status</th></tr></thead><tbody>{pacientes.map((p) => <tr key={p.id}><td>{p.nome}</td><td className="mono">{p.cns}</td><td>{formatarData(p.data_nascimento)}</td><td>{p.sexo}</td><td>{p.ubs_referencia || '—'}</td><td><StatusBadge value={p.status} /></td></tr>)}</tbody></table></div></TabelaEstado>
    </article>
  </div>;
}
