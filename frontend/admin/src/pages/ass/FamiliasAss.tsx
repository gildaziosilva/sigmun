import { useState } from 'react';
import type { AssResources, FamiliaAss, FamiliaAssCreate } from './AssShared';
import type { ExecutarAss } from './AssShared';
import { atualizarFamiliaAss, criarFamiliaAss, excluirFamiliaAss, obterFamiliaAssPorNis } from '../../lib/api';
import { StatusBadge, Field, formatarData } from './AssShared';

interface Props {
  resources: AssResources;
  executar: ExecutarAss;
  salvando: boolean;
}

const FORM_VAZIO: FamiliaAssCreate = {
  nis: '',
  responsavel_nome: '',
  responsavel_cpf: '',
  endereco: '',
  telefone: '',
  renda_per_capita: 0,
  quantidade_pessoas: 0,
};

export function FamiliasAss({ resources, executar, salvando }: Props) {
  const [novaFamilia, setNovaFamilia] = useState<FamiliaAssCreate>({ ...FORM_VAZIO });
  const [editando, setEditando] = useState<FamiliaAss | null>(null);
  const [pesquisa, setPesquisa] = useState('');

  const familias = resources.familias.data ?? [];
  const filtradas = familias.filter(
    (f) =>
      f.nis.includes(pesquisa) ||
      f.responsavel_nome.toLowerCase().includes(pesquisa.toLowerCase()),
  );

  function iniciarEdicao(familia: FamiliaAss) {
    setEditando(familia);
    setNovaFamilia({
      nis: familia.nis,
      responsavel_nome: familia.responsavel_nome,
      responsavel_cpf: familia.responsavel_cpf ?? '',
      endereco: familia.endereco ?? '',
      telefone: familia.telefone ?? '',
      renda_per_capita: familia.renda_per_capita,
      quantidade_pessoas: familia.quantidade_pessoas,
    });
  }

  function cancelarEdicao() {
    setEditando(null);
    setNovaFamilia({ ...FORM_VAZIO });
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      const ok = await executar(
        () => atualizarFamiliaAss(editando.id, novaFamilia),
        'Família atualizada com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(() => criarFamiliaAss(novaFamilia), 'Família cadastrada com sucesso!');
    if (ok) setNovaFamilia({ ...FORM_VAZIO });
  }

  async function handleExcluir(familia: FamiliaAss) {
    const confirmado = window.confirm(
      `Excluir a família de ${familia.responsavel_nome} (NIS ${familia.nis})?`,
    );
    if (!confirmado) return;
    await executar(() => excluirFamiliaAss(familia.id), 'Família excluída com sucesso!');
  }

  async function buscarPorNis(nis: string) {
    if (!nis.trim()) return;
    try {
      const familia = await obterFamiliaAssPorNis(nis);
      iniciarEdicao(familia);
    } catch {
      // Ignore - NIS não encontrado
    }
  }

  return (
    <section className="stack ass-familias">
      <form className="card ass-form" onSubmit={handleSubmit}>
        <h3>{editando ? 'Editar família' : 'Cadastrar nova família'}</h3>
        <div className="form-grid">
          <Field label="NIS (11 dígitos)" value={novaFamilia.nis} onChange={(v) => setNovaFamilia({ ...novaFamilia, nis: v })} required pattern="\d{11}" hint="11 dígitos numéricos" />
          <Field label="Nome do responsável" value={novaFamilia.responsavel_nome} onChange={(v) => setNovaFamilia({ ...novaFamilia, responsavel_nome: v })} required />
          <Field label="CPF do responsável" value={novaFamilia.responsavel_cpf ?? ''} onChange={(v) => setNovaFamilia({ ...novaFamilia, responsavel_cpf: v })} pattern="\d{11}" hint="11 dígitos numéricos" />
          <Field label="Endereço" value={novaFamilia.endereco ?? ''} onChange={(v) => setNovaFamilia({ ...novaFamilia, endereco: v })} />
          <Field label="Telefone" value={novaFamilia.telefone ?? ''} onChange={(v) => setNovaFamilia({ ...novaFamilia, telefone: v })} />
          <Field label="Renda per capita" value={String(novaFamilia.renda_per_capita)} onChange={(v) => setNovaFamilia({ ...novaFamilia, renda_per_capita: Number(v) || 0 })} type="number" step="0.01" min="0" />
          <Field label="Quantidade de pessoas" value={String(novaFamilia.quantidade_pessoas)} onChange={(v) => setNovaFamilia({ ...novaFamilia, quantidade_pessoas: Number(v) || 0 })} type="number" min="0" />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>{editando ? 'Atualizar' : 'Cadastrar família'}</button>
          {editando && <button type="button" className="button button--ghost" onClick={cancelarEdicao}>Cancelar edição</button>}
        </div>
        <div className="form-search">
          <Field label="Buscar família por NIS" value={pesquisa} onChange={setPesquisa} placeholder="Digite o NIS para buscar e editar" />
          <button type="button" className="button button--secondary" onClick={() => buscarPorNis(pesquisa)}>Buscar</button>
        </div>
      </form>

      <section className="card ass-lista">
        <div className="ass-lista-header">
          <h3>Famílias cadastradas ({familias.length})</h3>
          <input type="text" placeholder="Filtrar por NIS ou nome..." value={pesquisa} onChange={(e) => setPesquisa(e.target.value)} className="ass-search" />
        </div>
        {filtradas.length === 0 ? (
          <p className="muted">Nenhuma família encontrada.</p>
        ) : (
          <table className="ass-table">
            <thead>
              <tr><th>NIS</th><th>Responsável</th><th>Renda per capita</th><th>Qtd. pessoas</th><th>Status</th><th>Cadastrada em</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {filtradas.map((f) => (
                <tr key={f.id}>
                  <td>{f.nis}</td>
                  <td>{f.responsavel_nome}</td>
                  <td>R$ {new Intl.NumberFormat('pt-BR', { minimumFractionDigits: 2 }).format(f.renda_per_capita)}</td>
                  <td>{f.quantidade_pessoas}</td>
                  <td><StatusBadge value={f.status} /></td>
                  <td>{formatarData(f.created_at)}</td>
                  <td>
                    <button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(f)}>Editar</button>
                    <button type="button" className="button button--danger button--sm" onClick={() => handleExcluir(f)} disabled={salvando}>Excluir</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}