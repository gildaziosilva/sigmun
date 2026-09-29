import { useState } from 'react';
import type { LogradouroTel, LogradouroTelCreate } from '../../lib/api';
import { atualizarLogradouroTel, criarLogradouroTel, excluirLogradouroTel } from '../../lib/api';
import type { TelResources } from './TelPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  StatusTerr,
  TIPOS_LOGRADOURO,
  bairroNome,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: TelResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const FORM_VAZIO: LogradouroTelCreate = {
  codigo: '',
  nome: '',
  bairro_id: '',
  tipo: 'rua',
  cep: '',
  numero_inicial: 0,
  numero_final: 0,
};

export function LogradourosTel({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<LogradouroTelCreate>({ ...FORM_VAZIO });
  const [inicial, setInicial] = useState('0');
  const [final, setFinal] = useState('0');
  const [situacao, setSituacao] = useState('');
  const [editando, setEditando] = useState<LogradouroTel | null>(null);
  const [pesquisa, setPesquisa] = useState('');
  const [filtroBairro, setFiltroBairro] = useState('');

  const bairros = resources.bairros.data ?? [];
  const logradouros = resources.logradouros.data ?? [];
  const opcoesBairro = bairros.map((b) => ({ valor: b.id, rotulo: `${b.codigo} — ${b.nome}` }));

  const filtrados = logradouros.filter(
    (l) =>
      (filtroBairro === '' || l.bairro_id === filtroBairro) &&
      (l.codigo.toLowerCase().includes(pesquisa.toLowerCase()) ||
        l.nome.toLowerCase().includes(pesquisa.toLowerCase())),
  );

  function iniciarEdicao(logradouro: LogradouroTel) {
    setEditando(logradouro);
    setForm({
      codigo: logradouro.codigo,
      nome: logradouro.nome,
      bairro_id: logradouro.bairro_id,
      tipo: logradouro.tipo,
      cep: logradouro.cep ?? '',
      numero_inicial: logradouro.numero_inicial,
      numero_final: logradouro.numero_final,
    });
    setInicial(String(logradouro.numero_inicial));
    setFinal(String(logradouro.numero_final));
  }

  function cancelarEdicao() {
    setEditando(null);
    setForm({ ...FORM_VAZIO });
    setInicial('0');
    setFinal('0');
    setSituacao('');
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: LogradouroTelCreate = {
      ...form,
      numero_inicial: paraNumero(inicial),
      numero_final: paraNumero(final),
    };
    if (editando) {
      const ok = await executar(
        () => atualizarLogradouroTel(editando.id, { ...payload, situacao: situacao || undefined }),
        'Logradouro atualizado com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(() => criarLogradouroTel(payload), 'Logradouro cadastrado com sucesso!');
    if (ok) cancelarEdicao();
  }

  async function handleExcluir(logradouro: LogradouroTel) {
    if (!window.confirm(`Excluir o logradouro ${logradouro.codigo} - ${logradouro.nome}?`)) return;
    await executar(() => excluirLogradouroTel(logradouro.id), 'Logradouro excluído com sucesso!');
  }

  return (
    <section className="stack terr-logradouros">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>{editando ? 'Editar logradouro' : 'Cadastrar novo logradouro'}</h3>
        <div className="form-grid">
          <FieldTerr
            label="Código"
            value={form.codigo}
            onChange={(v) => setForm({ ...form, codigo: v })}
            required
            hint="Único no município (RN-TEL-002)"
          />
          <FieldTerr label="Nome" value={form.nome} onChange={(v) => setForm({ ...form, nome: v })} required />
          <SelectTerr
            label="Bairro"
            value={form.bairro_id}
            opcoes={opcoesBairro}
            onChange={(v) => setForm({ ...form, bairro_id: v })}
            required
            vazio="Selecione..."
            hint="Obrigatório: todo logradouro pertence a um bairro (RN-TEL-002)"
          />
          <SelectTerr
            label="Tipo"
            value={form.tipo ?? 'rua'}
            opcoes={TIPOS_LOGRADOURO}
            onChange={(v) => setForm({ ...form, tipo: v })}
            required
          />
          <FieldTerr label="CEP" value={form.cep ?? ''} onChange={(v) => setForm({ ...form, cep: v })} />
          <FieldTerr label="Número inicial" value={inicial} onChange={setInicial} type="number" min="0" step="1" />
          <FieldTerr label="Número final" value={final} onChange={setFinal} type="number" min="0" step="1" />
          {editando && (
            <SelectTerr
              label="Situação"
              value={situacao}
              opcoes={[
                { valor: 'ativo', rotulo: 'Ativo' },
                { valor: 'em_obra', rotulo: 'Em obra' },
                { valor: 'inativo', rotulo: 'Inativo' },
              ]}
              onChange={setSituacao}
              vazio="(sem alteração)"
            />
          )}
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Atualizar' : 'Cadastrar logradouro'}
          </button>
          {editando && (
            <button type="button" className="button button--ghost" onClick={cancelarEdicao}>
              Cancelar edição
            </button>
          )}
        </div>
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Logradouros cadastrados ({filtrados.length} de {logradouros.length})</h3>
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            <select value={filtroBairro} onChange={(e) => setFiltroBairro(e.target.value)} className="terr-search">
              <option value="">Todos os bairros</option>
              {bairros.map((b) => (
                <option key={b.id} value={b.id}>{b.nome}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Filtrar por código ou nome..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
              className="terr-search"
            />
          </div>
        </div>
        {filtrados.length === 0 ? (
          <p className="muted">Nenhum logradouro cadastrado.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Nome</th>
                <th>Tipo</th>
                <th>Bairro</th>
                <th>CEP</th>
                <th className="num">Numeração</th>
                <th>Situação</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {filtrados.map((l) => (
                <tr key={l.id}>
                  <td>{l.codigo}</td>
                  <td>{l.nome}</td>
                  <td>{l.tipo}</td>
                  <td>{bairroNome(bairros, l.bairro_id)}</td>
                  <td>{l.cep || '—'}</td>
                  <td className="num">
                    {l.numero_final ? `${l.numero_inicial}–${l.numero_final}` : (l.numero_inicial || 's/n')}
                  </td>
                  <td><StatusTerr value={l.situacao} /></td>
                  <td>
                    <button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(l)}>
                      Editar
                    </button>{' '}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => handleExcluir(l)}
                      disabled={salvando}
                    >
                      Excluir
                    </button>
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

