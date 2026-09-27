import { TabelaEstado } from '../../components/DataState';
import { type AssinaturaGDO, assinarDocumento, listarAssinaturas, type AssinaturaCreateRequest } from '../../lib/api';
import { type GdoResources, type ExecutarGdo, formatarData, documentoTitulo } from './GdoShared';
import { useState, useEffect } from 'react';

export interface AssinaturasGdoProps {
  resources: GdoResources;
  executar: ExecutarGdo;
  salvando: boolean;
}

export function AssinaturasGdo({ resources, executar, salvando }: AssinaturasGdoProps) {
  const [docId, setDocId] = useState('');
  const [assinaturas, setAssinaturas] = useState<AssinaturaGDO[]>([]);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  const [form, setForm] = useState<AssinaturaCreateRequest>({
    signatario_id: '',
    conteudo: '',
    autor_id: '',
    certificado_id: '',
  });

  useEffect(() => {
    if (docId) {
      carregarAssinaturas();
    }
  }, [docId]);

  async function carregarAssinaturas() {
    setLoading(true);
    setErro('');
    try {
      const data = await listarAssinaturas(docId);
      setAssinaturas(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar assinaturas');
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await assinarDocumento(docId, form);
        await carregarAssinaturas();
        setForm({ signatario_id: '', conteudo: '', autor_id: '', certificado_id: '' });
      },
      'Documento assinado com sucesso',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Assinar Documento</h3>
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
                <span>Signatário ID *</span>
                <input
                  type="text"
                  value={form.signatario_id}
                  onChange={(e) => setForm({ ...form, signatario_id: e.target.value })}
                  required
                />
              </label>
              <label>
                <span>Autor ID *</span>
                <input
                  type="text"
                  value={form.autor_id}
                  onChange={(e) => setForm({ ...form, autor_id: e.target.value })}
                  required
                />
              </label>
            </div>
            <label>
              <span>Conteúdo (hash) *</span>
              <input
                type="text"
                value={form.conteudo}
                onChange={(e) => setForm({ ...form, conteudo: e.target.value })}
                required
              />
            </label>
            <label>
              <span>Certificado ID</span>
              <input
                type="text"
                value={form.certificado_id}
                onChange={(e) => setForm({ ...form, certificado_id: e.target.value })}
              />
            </label>
            <div className="form-actions">
              <button type="submit" className="button" disabled={salvando}>
                {salvando ? 'Salvando...' : 'Assinar'}
              </button>
            </div>
          </form>
        )}
      </div>

      <TabelaEstado loading={loading} erro={erro} vazio={assinaturas.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Documento</th>
                <th>Signatário</th>
                <th>Data</th>
                <th>Hash</th>
                <th>Certificado</th>
                <th>Válida</th>
                <th>Revogada</th>
              </tr>
            </thead>
            <tbody>
              {assinaturas.map((a) => (
                <tr key={a.id}>
                  <td className="mono">{documentoTitulo(resources, a.documento_id)}</td>
                  <td>{a.signatario_id}</td>
                  <td>{formatarData(a.data_assinatura)}</td>
                  <td className="mono">{a.hash_assinatura}</td>
                  <td>{a.certificado_id || '—'}</td>
                  <td>{a.is_valida ? 'Sim' : 'Não'}</td>
                  <td>{a.is_revogada ? 'Sim' : 'Não'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </div>
  );
}