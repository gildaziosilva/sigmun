import { TabelaEstado } from '../../components/DataState';
import { type ClassificacaoDocumentalGDO, listarClassificacoes, obterClassificacao, type ClassificacaoCreateRequest } from '../../lib/api';
import { type ExecutarGdo, StatusBadge, formatarData } from './GdoShared';
import { useState, useEffect } from 'react';

export interface ClassificacoesGdoProps {
  executar: ExecutarGdo;
  salvando: boolean;
}

export function ClassificacoesGdo({ executar, salvando }: ClassificacoesGdoProps) {
  const [classificacoes, setClassificacoes] = useState<ClassificacaoDocumentalGDO[]>([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState('');
  const [mostrarForm, setMostrarForm] = useState(false);
  const [detalhe, setDetalhe] = useState<ClassificacaoDocumentalGDO | null>(null);

  const [form, setForm] = useState<ClassificacaoCreateRequest>({
    codigo: '',
    nome: '',
    descricao: '',
    nivel: 0,
    classificacao_pai_id: '',
    prazo_retencao: 0,
    unidade_destino_id: '',
  });

  useEffect(() => {
    carregarClassificacoes();
  }, []);

  async function carregarClassificacoes() {
    setLoading(true);
    setErro('');
    try {
      const data = await listarClassificacoes();
      setClassificacoes(data.items);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar classificações');
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        alert('Endpoint de criação não implementado no backend');
      },
      'Classificação criada com sucesso',
    );
  }

  async function verDetalhe(id: string) {
    try {
      const data = await obterClassificacao(id);
      setDetalhe(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar detalhe');
    }
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="gdo-toolbar">
        <button type="button" className="button" onClick={() => setMostrarForm(!mostrarForm)}>
          {mostrarForm ? 'Cancelar' : 'Nova Classificação'}
        </button>
      </div>

      {mostrarForm && (
        <form onSubmit={handleSubmit} className="card card--form gdo-form">
          <h3>Nova Classificação</h3>
          <div className="grid grid--2">
            <label>
              <span>Código *</span>
              <input
                type="text"
                value={form.codigo}
                onChange={(e) => setForm({ ...form, codigo: e.target.value })}
                required
              />
            </label>
            <label>
              <span>Nome *</span>
              <input
                type="text"
                value={form.nome}
                onChange={(e) => setForm({ ...form, nome: e.target.value })}
                required
              />
            </label>
            <label>
              <span>Nível</span>
              <input
                type="number"
                value={String(form.nivel)}
                onChange={(e) => setForm({ ...form, nivel: Number(e.target.value) })}
                min="0"
              />
            </label>
            <label>
              <span>Prazo Retenção (anos)</span>
              <input
                type="number"
                value={String(form.prazo_retencao)}
                onChange={(e) => setForm({ ...form, prazo_retencao: Number(e.target.value) })}
                min="0"
              />
            </label>
          </div>
          <div className="grid grid--2">
            <label>
              <span>Classificação Pai ID</span>
              <input
                type="text"
                value={form.classificacao_pai_id}
                onChange={(e) => setForm({ ...form, classificacao_pai_id: e.target.value })}
              />
            </label>
            <label>
              <span>Unidade Destino ID</span>
              <input
                type="text"
                value={form.unidade_destino_id}
                onChange={(e) => setForm({ ...form, unidade_destino_id: e.target.value })}
              />
            </label>
          </div>
          <label>
            <span>Descrição</span>
            <input
              type="text"
              value={form.descricao}
              onChange={(e) => setForm({ ...form, descricao: e.target.value })}
            />
          </label>
          <div className="form-actions">
            <button type="button" className="button button--ghost" onClick={() => setMostrarForm(false)}>Cancelar</button>
            <button type="submit" className="button" disabled={salvando}>{salvando ? 'Salvando...' : 'Criar'}</button>
          </div>
        </form>
      )}

      <TabelaEstado loading={loading} erro={erro} vazio={classificacoes.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Nome</th>
                <th>Nível</th>
                <th>Prazo Retenção</th>
                <th>Pai</th>
                <th>Status</th>
                <th>Criado em</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {classificacoes.map((c) => (
                <tr key={c.id}>
                  <td className="mono">{c.codigo}</td>
                  <td>{c.nome}</td>
                  <td>{c.nivel}</td>
                  <td>{c.prazo_retencao} anos</td>
                  <td className="mono">{c.classificacao_pai_id || '—'}</td>
                  <td><StatusBadge value={c.is_active ? 'ativo' : 'inativo'} /></td>
                  <td>{formatarData(c.created_at)}</td>
                  <td>
                    <button type="button" className="link" onClick={() => verDetalhe(c.id)}>Detalhe</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>

      {detalhe && (
        <article className="card card--detail">
          <h3>
            {detalhe.codigo} — {detalhe.nome}
            <button type="button" className="link link--close" onClick={() => setDetalhe(null)}>Fechar</button>
          </h3>
          <dl className="detail-list">
            <div><dt>Nível</dt><dd>{detalhe.nivel}</dd></div>
            <div><dt>Prazo Retenção</dt><dd>{detalhe.prazo_retencao} anos</dd></div>
            <div><dt>Classificação Pai</dt><dd className="mono">{detalhe.classificacao_pai_id || '—'}</dd></div>
            <div><dt>Unidade Destino</dt><dd className="mono">{detalhe.unidade_destino_id || '—'}</dd></div>
            <div><dt>Descrição</dt><dd>{detalhe.descricao || '—'}</dd></div>
            <div><dt>Criado em</dt><dd>{formatarData(detalhe.created_at)}</dd></div>
          </dl>
        </article>
      )}
    </div>
  );
}
