import { TabelaEstado } from '../../components/DataState';
import { type TipoDocumentalGDO, listarTiposDocumentais, criarTipoDocumental, ativarTipoDocumental, inativarTipoDocumental, type TipoDocumentalCreateRequest } from '../../lib/api';
import { type ExecutarGdo, StatusBadge, formatarData } from './GdoShared';
import { useState, useEffect } from 'react';

export interface TiposDocumentaisGdoProps {
  executar: ExecutarGdo;
  salvando: boolean;
}

export function TiposDocumentaisGdo({ executar, salvando }: TiposDocumentaisGdoProps) {
  const [tipos, setTipos] = useState<TipoDocumentalGDO[]>([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState('');
  const [mostrarForm, setMostrarForm] = useState(false);

  const [form, setForm] = useState<TipoDocumentalCreateRequest>({
    codigo: '',
    nome: '',
    descricao: '',
  });

  useEffect(() => {
    carregarTipos();
  }, []);

  async function carregarTipos() {
    setLoading(true);
    setErro('');
    try {
      const data = await listarTiposDocumentais();
      setTipos(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar tipos documentais');
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await criarTipoDocumental(form);
        setMostrarForm(false);
        setForm({ codigo: '', nome: '', descricao: '' });
      },
      'Tipo documental criado com sucesso',
    );
  }

  async function handleAtivar(id: string) {
    await executar(
      async () => {
        await ativarTipoDocumental(id);
      },
      'Tipo documental ativado',
    );
  }

  async function handleInativar(id: string) {
    await executar(
      async () => {
        await inativarTipoDocumental(id);
      },
      'Tipo documental inativado',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="gdo-toolbar">
        <button type="button" className="button" onClick={() => setMostrarForm(!mostrarForm)}>
          {mostrarForm ? 'Cancelar' : 'Novo Tipo Documental'}
        </button>
      </div>

      {mostrarForm && (
        <form onSubmit={handleSubmit} className="card card--form gdo-form">
          <h3>Novo Tipo Documental</h3>
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

      <TabelaEstado loading={loading} erro={erro} vazio={tipos.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Nome</th>
                <th>Descrição</th>
                <th>Status</th>
                <th>Criado em</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {tipos.map((t) => (
                <tr key={t.id}>
                  <td className="mono">{t.codigo}</td>
                  <td>{t.nome}</td>
                  <td>{t.descricao || '—'}</td>
                  <td><StatusBadge value={t.is_ativo ? 'ativo' : 'inativo'} /></td>
                  <td>{formatarData(t.created_at)}</td>
                  <td>
                    {t.is_ativo ? (
                      <button type="button" className="link link--danger" onClick={() => handleInativar(t.id)} disabled={salvando}>
                        Inativar
                      </button>
                    ) : (
                      <button type="button" className="link" onClick={() => handleAtivar(t.id)} disabled={salvando}>
                        Ativar
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </div>
  );
}