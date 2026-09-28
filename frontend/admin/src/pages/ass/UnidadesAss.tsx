import { useState } from 'react';
import type { AssResources, UnidadeAss, UnidadeAssCreate } from './AssShared';
import type { ExecutarAss } from './AssShared';
import { atualizarUnidadeAss, criarUnidadeAss, excluirUnidadeAss } from '../../lib/api';
import { StatusBadge, Field } from './AssShared';

interface Props {
  resources: AssResources;
  executar: ExecutarAss;
  salvando: boolean;
}

const FORM_VAZIO: UnidadeAssCreate = {
  codigo: '',
  nome: '',
  tipo: 'cras',
  endereco: '',
  telefone: '',
  email: '',
  responsavel: '',
};

export function UnidadesAss({ resources, executar, salvando }: Props) {
  const [novaUnidade, setNovaUnidade] = useState<UnidadeAssCreate>({ ...FORM_VAZIO });
  const [editando, setEditando] = useState<UnidadeAss | null>(null);
  const [pesquisa, setPesquisa] = useState('');

  const unidades = resources.unidades.data ?? [];
  const filtradas = unidades.filter(
    (u) =>
      u.codigo.includes(pesquisa) ||
      u.nome.toLowerCase().includes(pesquisa.toLowerCase()),
  );

  function iniciarEdicao(unidade: UnidadeAss) {
    setEditando(unidade);
    setNovaUnidade({
      codigo: unidade.codigo,
      nome: unidade.nome,
      tipo: unidade.tipo,
      endereco: unidade.endereco ?? '',
      telefone: unidade.telefone ?? '',
      email: unidade.email ?? '',
      responsavel: unidade.responsavel ?? '',
    });
  }

  function cancelarEdicao() {
    setEditando(null);
    setNovaUnidade({ ...FORM_VAZIO });
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      const ok = await executar(
        () => atualizarUnidadeAss(editando.id, novaUnidade),
        'Unidade atualizada com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(() => criarUnidadeAss(novaUnidade), 'Unidade cadastrada com sucesso!');
    if (ok) setNovaUnidade({ ...FORM_VAZIO });
  }

  async function handleExcluir(unidade: UnidadeAss) {
    const confirmado = window.confirm(`Excluir a unidade ${unidade.codigo} - ${unidade.nome}?`);
    if (!confirmado) return;
    await executar(() => excluirUnidadeAss(unidade.id), 'Unidade excluída com sucesso!');
  }

  return (
    <section className="stack ass-unidades">
      <form className="card ass-form" onSubmit={handleSubmit}>
        <h3>{editando ? 'Editar unidade' : 'Cadastrar nova unidade'}</h3>
        <div className="form-grid">
          <Field label="Código" value={novaUnidade.codigo} onChange={(v) => setNovaUnidade({ ...novaUnidade, codigo: v })} required />
          <Field label="Nome" value={novaUnidade.nome} onChange={(v) => setNovaUnidade({ ...novaUnidade, nome: v })} required />
          <Field label="Tipo" value={novaUnidade.tipo ?? ''} onChange={(v) => setNovaUnidade({ ...novaUnidade, tipo: v })}>
            <select value={novaUnidade.tipo ?? ''} onChange={(e) => setNovaUnidade({ ...novaUnidade, tipo: e.target.value })}>
              <option value="cras">CRAS</option>
              <option value="creas">CREAS</option>
              <option value="centro_pop">Centro Pop</option>
              <option value="abrigo">Abrigo</option>
              <option value="outro">Outro</option>
            </select>
          </Field>
          <Field label="Endereço" value={novaUnidade.endereco ?? ''} onChange={(v) => setNovaUnidade({ ...novaUnidade, endereco: v })} />
          <Field label="Telefone" value={novaUnidade.telefone ?? ''} onChange={(v) => setNovaUnidade({ ...novaUnidade, telefone: v })} />
          <Field label="E-mail" value={novaUnidade.email ?? ''} onChange={(v) => setNovaUnidade({ ...novaUnidade, email: v })} type="email" />
          <Field label="Responsável" value={novaUnidade.responsavel ?? ''} onChange={(v) => setNovaUnidade({ ...novaUnidade, responsavel: v })} />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>{editando ? 'Atualizar' : 'Cadastrar unidade'}</button>
          {editando && <button type="button" className="button button--ghost" onClick={cancelarEdicao}>Cancelar edição</button>}
        </div>
      </form>

      <section className="card ass-lista">
        <div className="ass-lista-header">
          <h3>Unidades cadastradas ({unidades.length})</h3>
          <input type="text" placeholder="Filtrar por código ou nome..." value={pesquisa} onChange={(e) => setPesquisa(e.target.value)} className="ass-search" />
        </div>
        {filtradas.length === 0 ? (
          <p className="muted">Nenhuma unidade cadastrada.</p>
        ) : (
          <table className="ass-table">
            <thead>
              <tr><th>Código</th><th>Nome</th><th>Tipo</th><th>Endereço</th><th>Telefone</th><th>E-mail</th><th>Status</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {filtradas.map((u) => (
                <tr key={u.id}>
                  <td>{u.codigo}</td>
                  <td>{u.nome}</td>
                  <td>{u.tipo.toUpperCase()}</td>
                  <td>{u.endereco}</td>
                  <td>{u.telefone}</td>
                  <td>{u.email}</td>
                  <td><StatusBadge value={u.status} /></td>
                  <td><button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(u)}>Editar</button> <button type="button" className="button button--danger button--sm" onClick={() => handleExcluir(u)} disabled={salvando}>Excluir</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}