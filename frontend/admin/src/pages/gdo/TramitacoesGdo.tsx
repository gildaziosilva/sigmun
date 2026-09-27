import { TabelaEstado } from '../../components/DataState';
import { type TramitacaoGDO, listarTramitacoes, tramitarDocumento, type TramitacaoCreateRequest } from '../../lib/api';
import { type GdoResources, type ExecutarGdo, StatusBadge, formatarData, documentoTitulo } from './GdoShared';
import { useState, useEffect } from 'react';

export interface TramitacoesGdoProps {
  resources: GdoResources;
  executar: ExecutarGdo;
  salvando: boolean;
}

export function TramitacoesGdo({ resources, executar, salvando }: TramitacoesGdoProps) {
  const [docId, setDocId] = useState('');
  const [tramitacoes, setTramitacoes] = useState<TramitacaoGDO[]>([]);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  const [form, setForm] = useState<TramitacaoCreateRequest>({
    unidade_origem_id: '',
    unidade_destino_id: '',
    tipo: 'envio',
    motivo: '',
    observacao: '',
  });

  useEffect(() => {
    if (docId) {
      carregarTramitacoes();
    }
  }, [docId]);

  async function carregarTramitacoes() {
    setLoading(true);
    setErro('');
    try {
      const data = await listarTramitacoes(docId);
      setTramitacoes(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar tramitações');
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await tramitarDocumento(docId, form);
        await carregarTramitacoes();
        setForm({ unidade_origem_id: '', unidade_destino_id: '', tipo: 'envio', motivo: '', observacao: '' });
      },
      'Tramitação registrada com sucesso',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Registrar Tramitação</h3>
        <div className="grid grid--2">
          <label>
            <span>Documento ID *</span>
            <input
              type="text"
              value={docId}
              onChange={(e) => setDocId(e.target.value)}
              required
              placeholder="UUID do documento"
            />
          </label>
        </div>
        {docId && (
          <form onSubmit={handleSubmit} className="stack">
            <div className="grid grid--2">
              <label>
                <span>Unidade Origem *</span>
                <input
                  type="text"
                  value={form.unidade_origem_id}
                  onChange={(e) => setForm({ ...form, unidade_origem_id: e.target.value })}
                  required
                />
              </label>
              <label>
                <span>Unidade Destino *</span>
                <input
                  type="text"
                  value={form.unidade_destino_id}
                  onChange={(e) => setForm({ ...form, unidade_destino_id: e.target.value })}
                  required
                />
              </label>
              <label>
                <span>Tipo *</span>
                <select
                  value={form.tipo}
                  onChange={(e) => setForm({ ...form, tipo: e.target.value as 'envio' | 'recebimento' | 'devolucao' })}
                >
                  <option value="envio">Envio</option>
                  <option value="recebimento">Recebimento</option>
                  <option value="devolucao">Devolução</option>
                </select>
              </label>
            </div>
            <label>
              <span>Motivo</span>
              <input
                type="text"
                value={form.motivo}
                onChange={(e) => setForm({ ...form, motivo: e.target.value })}
              />
            </label>
            <label>
              <span>Observação</span>
              <input
                type="text"
                value={form.observacao}
                onChange={(e) => setForm({ ...form, observacao: e.target.value })}
              />
            </label>
            <div className="form-actions">
              <button type="submit" className="button" disabled={salvando}>
                {salvando ? 'Salvando...' : 'Tramitar'}
              </button>
            </div>
          </form>
        )}
      </div>

      <TabelaEstado loading={loading} erro={erro} vazio={tramitacoes.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Documento</th>
                <th>Origem</th>
                <th>Destino</th>
                <th>Tipo</th>
                <th>Data Envio</th>
                <th>Data Recebimento</th>
                <th>Motivo</th>
              </tr>
            </thead>
            <tbody>
              {tramitacoes.map((t) => (
                <tr key={t.id}>
                  <td className="mono">{documentoTitulo(resources, t.documento_id)}</td>
                  <td>{t.unidade_origem_id}</td>
                  <td>{t.unidade_destino_id}</td>
                  <td><StatusBadge value={t.tipo} /></td>
                  <td>{formatarData(t.data_envio)}</td>
                  <td>{formatarData(t.data_recebimento)}</td>
                  <td>{t.motivo || '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </div>
  );
}