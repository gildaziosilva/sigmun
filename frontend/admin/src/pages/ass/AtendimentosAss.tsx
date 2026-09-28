import { useState, type FormEvent } from 'react';
import { criarPessoaAss, listarAtendimentosPorPessoaAss, registrarAtendimentoAss, type AtendimentoAss } from '../../lib/api';
import { TabelaEstado } from '../../components/DataState';
import { Field, formatarData, StatusBadge, type ExecutarAss, type AssResources } from './AssShared';

export function AtendimentosAss({ resources, executar, salvando }: { resources: AssResources; executar: ExecutarAss; salvando: boolean }) {
  const [nome, setNome] = useState('');
  const [cpf, setCpf] = useState('');
  const [nascimento, setNascimento] = useState('');
  const [sexo, setSexo] = useState('ignorado');
  const [nome_mae, setNomeMae] = useState('');
  const [parentesco, setParentesco] = useState('');
  const [escolaridade, setEscolaridade] = useState('');
  const [ocupacao, setOcupacao] = useState('');
  const [renda, setRenda] = useState(0);
  const [familiaId, setFamiliaId] = useState('');
  const [pessoaId, setPessoaId] = useState('');
  const [tipo, setTipo] = useState('acolhimento');
  const [profissional, setProfissional] = useState('');
  const [unidadeId, setUnidadeId] = useState('');
  const [data, setData] = useState('');
  const [descricao, setDescricao] = useState('');
  const [encaminhamento, setEncaminhamento] = useState('');
  const [historico, setHistorico] = useState<AtendimentoAss[] | null>(null);
  const [historicoErro, setHistoricoErro] = useState('');
  const pessoas = resources.pessoas.data ?? [];
  const unidades = resources.unidades.data ?? [];
  const familias = resources.familias.data ?? [];

  async function cadastrar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => criarPessoaAss({
      familia_id: familiaId, nome: nome.trim(), cpf: cpf.trim(), data_nascimento: nascimento,
      sexo, nome_mae: nome_mae.trim(), parentesco: parentesco.trim(),
      escolaridade: escolaridade.trim(), ocupacao: ocupacao.trim(), renda,
    }), 'Pessoa cadastrado com sucesso.');
    if (ok) { setNome(''); setCpf(''); setNascimento(''); setNomeMae(''); setParentesco(''); setEscolaridade(''); setOcupacao(''); setRenda(0); setFamiliaId(''); }
  }

  async function registrar(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => registrarAtendimentoAss({
      pessoa_id: pessoaId, unidade_id: unidadeId, tipo, data: data || undefined,
      descricao: descricao.trim(), encaminhamento: encaminhamento.trim(),
      profissional: profissional.trim(),
    }), 'Atendimento registrado.');
    if (ok) { setDescricao(''); setEncaminhamento(''); setProfissional(''); setUnidadeId(''); setData(''); setHistorico(null); }
  }

  async function consultar() {
    setHistoricoErro('');
    try { setHistorico(await listarAtendimentosPorPessoaAss(pessoaId)); }
    catch (erro) { setHistorico(null); setHistoricoErro(erro instanceof Error ? erro.message : 'Falha ao consultar atendimentos.'); }
  }

  return <div className="ass-grid">
    <article className="card ass-card">
      <h3>Cadastro da pessoa</h3><p className="muted">CPF obrigatório e único.</p>
      <form className="ass-form" onSubmit={cadastrar}>
        <Field label="Família" value={familiaId} onChange={setFamiliaId} required><select value={familiaId} onChange={(e) => setFamiliaId(e.target.value)} required><option value="">Selecione…</option>{familias.map((f) => <option key={f.id} value={f.id}>{f.nis} - {f.responsavel_nome}</option>)}</select></Field>
        <Field label="Nome" value={nome} onChange={setNome} required />
        <Field label="CPF" value={cpf} onChange={setCpf} required hint="11 dígitos numéricos." />
        <Field label="Nascimento" value={nascimento} onChange={setNascimento} type="date" />
        <Field label="Sexo" value={sexo} onChange={setSexo}><select value={sexo} onChange={(e) => setSexo(e.target.value)}><option value="ignorado">Ignorado</option><option value="feminino">Feminino</option><option value="masculino">Masculino</option></select></Field>
        <Field label="Nome da mãe" value={nome_mae} onChange={setNomeMae} />
        <Field label="Parentesco" value={parentesco} onChange={setParentesco} />
        <Field label="Escolaridade" value={escolaridade} onChange={setEscolaridade} />
        <Field label="Ocupação" value={ocupacao} onChange={setOcupacao} />
        <Field label="Renda" value={String(renda)} onChange={(v) => setRenda(Number(v) || 0)} type="number" step="0.01" min="0" />
        <button className="button" type="submit" disabled={salvando}>Cadastrar pessoa</button>
      </form>
    </article>
    <article className="card ass-card">
      <h3>Registro de atendimento</h3>
      <form className="ass-form" onSubmit={registrar}>
        <Field label="Pessoa" value={pessoaId} onChange={setPessoaId} required><select value={pessoaId} onChange={(e) => setPessoaId(e.target.value)} required><option value="">Selecione…</option>{pessoas.map((p) => <option key={p.id} value={p.id}>{p.nome} · {p.cpf}</option>)}</select></Field>
        <Field label="Unidade" value={unidadeId} onChange={setUnidadeId} required><select value={unidadeId} onChange={(e) => setUnidadeId(e.target.value)} required><option value="">Selecione…</option>{unidades.map((u) => <option key={u.id} value={u.id}>{u.codigo} - {u.nome}</option>)}</select></Field>
        <Field label="Tipo" value={tipo} onChange={setTipo}><select value={tipo} onChange={(e) => setTipo(e.target.value)}><option value="acolhimento">Acolhimento</option><option value="orientacao">Orientação</option><option value="encaminhamento">Encaminhamento</option><option value="visita_domiciliar">Visita domiciliar</option><option value="grupo_convivencia">Grupo de convivência</option><option value="beneficio_eventual">Benefício eventual</option><option value="outro">Outro</option></select></Field>
        <Field label="Data" value={data} onChange={setData} type="date" />
        <Field label="Profissional" value={profissional} onChange={setProfissional} required />
        <Field label="Descrição" value={descricao} onChange={setDescricao} />
        <Field label="Encaminhamento" value={encaminhamento} onChange={setEncaminhamento} />
        <div className="actions"><button className="button" type="submit" disabled={salvando}>Registrar atendimento</button><button className="button button--ghost" type="button" onClick={consultar} disabled={!pessoaId}>Consultar histórico</button></div>
      </form>
      {historicoErro && <p className="alert alert--error" role="alert">{historicoErro}</p>}
      {historico && <TabelaEstado loading={false} erro="" vazio={historico.length === 0}><div className="table-wrap"><table className="table"><thead><tr><th>Data</th><th>Tipo</th><th>Profissional</th><th>Encaminhamento</th><th>Descrição</th></tr></thead><tbody>{historico.map((a) => <tr key={a.id}><td>{formatarData(a.data)}</td><td><StatusBadge value={a.tipo} /></td><td>{a.profissional}</td><td>{a.encaminhamento || '—'}</td><td>{a.descricao || '—'}</td></tr>)}</tbody></table></div></TabelaEstado>}
    </article>
    <article className="card ass-card ass-card--full">
      <h3>Pessoas cadastradas</h3>
      <TabelaEstado loading={resources.pessoas.loading} erro={resources.pessoas.erro} vazio={pessoas.length === 0}><div className="table-wrap"><table className="table"><thead><tr><th>Nome</th><th>CPF</th><th>Nascimento</th><th>Sexo</th><th>Renda</th><th>Cadastrada em</th></tr></thead><tbody>{pessoas.map((p) => <tr key={p.id}><td>{p.nome}</td><td className="mono">{p.cpf}</td><td>{formatarData(p.data_nascimento)}</td><td>{p.sexo}</td><td>R$ {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(p.renda)}</td><td>{formatarData(p.created_at)}</td></tr>)}</tbody></table></div></TabelaEstado>
    </article>
  </div>;
}
