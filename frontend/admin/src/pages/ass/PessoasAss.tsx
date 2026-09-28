import { useState, type FormEvent } from 'react';
import { atualizarPessoaAss, criarPessoaAss, excluirPessoaAss, obterPessoaAssPorCpf, type PessoaAss } from '../../lib/api';
import { Field, formatarData, formatarNumero, type ExecutarAss, type AssResources, type FamiliaAss } from './AssShared';

const FORM_VAZIO = {
  familia_id: '',
  nome: '',
  cpf: '',
  data_nascimento: '',
  sexo: 'ignorado',
  nome_mae: '',
  parentesco: '',
  escolaridade: '',
  ocupacao: '',
  renda: 0,
};

export function PessoasAss({ resources, executar, salvando }: { resources: AssResources; executar: ExecutarAss; salvando: boolean }) {
  const [novaPessoa, setNovaPessoa] = useState({ ...FORM_VAZIO });
  const [editando, setEditando] = useState<PessoaAss | null>(null);
  const [pesquisa, setPesquisa] = useState('');

  const pessoas = resources.pessoas.data ?? [];

  function iniciarEdicao(pessoa: PessoaAss) {
    setEditando(pessoa);
    setNovaPessoa({
      familia_id: pessoa.familia_id,
      nome: pessoa.nome,
      cpf: pessoa.cpf,
      data_nascimento: pessoa.data_nascimento ?? '',
      sexo: pessoa.sexo,
      nome_mae: pessoa.nome_mae ?? '',
      parentesco: pessoa.parentesco ?? '',
      escolaridade: pessoa.escolaridade ?? '',
      ocupacao: pessoa.ocupacao ?? '',
      renda: pessoa.renda,
    });
  }

  function cancelarEdicao() {
    setEditando(null);
    setNovaPessoa({ ...FORM_VAZIO });
  }

  async function handleSubmit(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    if (editando) {
      const ok = await executar(
        () => atualizarPessoaAss(editando.id, novaPessoa),
        'Pessoa atualizada com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(() => criarPessoaAss(novaPessoa), 'Pessoa cadastrada com sucesso!');
    if (ok) setNovaPessoa({ ...FORM_VAZIO });
  }

  async function handleExcluir(pessoa: PessoaAss) {
    const confirmado = window.confirm(`Excluir ${pessoa.nome} (CPF ${pessoa.cpf})?`);
    if (!confirmado) return;
    await executar(() => excluirPessoaAss(pessoa.id), 'Pessoa excluída com sucesso!');
  }

  async function buscarPorCpf(cpf: string) {
    if (!cpf.trim()) return;
    try {
      const pessoa = await obterPessoaAssPorCpf(cpf);
      iniciarEdicao(pessoa);
    } catch {
      // Ignore - CPF não encontrado
    }
  }

  const filtradas = pessoas.filter(
    (p) =>
      p.nome.toLowerCase().includes(pesquisa.toLowerCase()) ||
      p.cpf.includes(pesquisa),
  );

  return (
    <section className="stack ass-pessoas">
      <form className="card ass-form" onSubmit={handleSubmit}>


  <h3>{editando ? 'Editar pessoa' : 'Cadastrar nova pessoa'}</h3>
        <div className="form-grid">
          <Field label="Família (NIS/Responsável)" value={novaPessoa.familia_id} onChange={(v) => setNovaPessoa({ ...novaPessoa, familia_id: v })} required>
            <select value={novaPessoa.familia_id} onChange={(e) => setNovaPessoa({ ...novaPessoa, familia_id: e.target.value })} required>
              <option value="">Selecione a família</option>
              {resources.familias.data?.map((f) => (
                <option key={f.id} value={f.id}>{f.nis} - {f.responsavel_nome}</option>
              ))}
            </select>
          </Field>
          <Field label="Nome" value={novaPessoa.nome} onChange={(v) => setNovaPessoa({ ...novaPessoa, nome: v })} required />
          <Field label="CPF (11 dígitos)" value={novaPessoa.cpf} onChange={(v) => setNovaPessoa({ ...novaPessoa, cpf: v })} required pattern="\d{11}" hint="11 dígitos numéricos" />
          <Field label="Data de nascimento" value={novaPessoa.data_nascimento} onChange={(v) => setNovaPessoa({ ...novaPessoa, data_nascimento: v })} type="date" />
          <Field label="Sexo" value={novaPessoa.sexo} onChange={(v) => setNovaPessoa({ ...novaPessoa, sexo: v })}>
            <select value={novaPessoa.sexo} onChange={(e) => setNovaPessoa({ ...novaPessoa, sexo: e.target.value })}>
              <option value="masculino">Masculino</option>
              <option value="feminino">Feminino</option>
              <option value="ignorado">Ignorado</option>
            </select>
          </Field>
          <Field label="Nome da mãe" value={novaPessoa.nome_mae} onChange={(v) => setNovaPessoa({ ...novaPessoa, nome_mae: v })} />
          <Field label="Parentesco" value={novaPessoa.parentesco} onChange={(v) => setNovaPessoa({ ...novaPessoa, parentesco: v })} />
          <Field label="Escolaridade" value={novaPessoa.escolaridade} onChange={(v) => setNovaPessoa({ ...novaPessoa, escolaridade: v })} />
          <Field label="Ocupação" value={novaPessoa.ocupacao} onChange={(v) => setNovaPessoa({ ...novaPessoa, ocupacao: v })} />
          <Field label="Renda" value={String(novaPessoa.renda)} onChange={(v) => setNovaPessoa({ ...novaPessoa, renda: Number(v) || 0 })} type="number" step="0.01" min="0" />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>{editando ? 'Atualizar' : 'Cadastrar pessoa'}</button>
          {editando && <button type="button" className="button button--ghost" onClick={cancelarEdicao}>Cancelar edição</button>}
        </div>
        <div className="form-search">
          <Field label="Buscar pessoa por CPF" value={pesquisa} onChange={setPesquisa} placeholder="Digite o CPF para buscar e editar" />
          <button type="button" className="button button--secondary" onClick={() => buscarPorCpf(pesquisa)}>Buscar</button>
        </div>
      </form>

      <section className="card ass-lista">
        <div className="ass-lista-header">
          <h3>Pessoas cadastradas ({pessoas.length})</h3>
          <input type="text" placeholder="Filtrar por nome ou CPF..." value={pesquisa} onChange={(e) => setPesquisa(e.target.value)} className="ass-search" />
        </div>
        {pessoas.length === 0 ? (
          <p className="muted">Nenhuma pessoa cadastrada.</p>
        ) : (
          <table className="ass-table">
            <thead>
              <tr><th>Nome</th><th>CPF</th><th>Família</th><th>Sexo</th><th>Data nasc.</th><th>Renda</th><th>Cadastrada em</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {filtradas.map((p) => (
                <tr key={p.id}>
                  <td>{p.nome}</td>
                  <td>{p.cpf}</td>
                  <td>{pessoaNome(resources, p.familia_id)}</td>
                  <td>{p.sexo}</td>
                  <td>{formatarData(p.data_nascimento)}</td>
                  <td>R$ {formatarNumero(p.renda)}</td>
                  <td>{formatarData(p.created_at)}</td>
                  <td><button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(p)}>Editar</button> <button type="button" className="button button--danger button--sm" onClick={() => handleExcluir(p)} disabled={salvando}>Excluir</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}

function pessoaNome(resources: AssResources, id: string): string {
  return resources.familias.data?.find((f: FamiliaAss) => f.id === id)?.responsavel_nome ?? id;
}
