import { TabelaEstado } from '../../components/DataState';
import { type VersaoDocumentoGDO, listarVersoes, criarVersao, type VersaoCreateRequest } from '../../lib/api';
import { type GdoResources, type ExecutarGdo, formatarData, documentoTitulo } from './GdoShared';
import { useState, useEffect } from 'react';

export interface VersoesGdoProps {
  resources: GdoResources;
  executar: ExecutarGdo;
  salvando: boolean;
}

export function VersoesGdo({ resources, executar, salvando }: VersoesGdoProps) {
  const [docId, setDocId] = useState('');
  const [versoes, setVersoes] = useState<VersaoDocumentoGDO[]>([]);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  const [form, setForm] = useState<VersaoCreateRequest>({
    documento_id: '',
    numero_versao: 1,
    conteudo_ref: '',
    hash_integridade: '',
  });

  useEffect(() => {
    if (docId) {
      carregarVersoes();
    }
  }, [docId]);

  async function carregarVersoes() {
    setLoading(true);
    setErro('');
    try {
      const data = await listarVersoes(docId);
      setVersoes(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar versões');
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await criarVersao({ ...form, documento_id: docId });
        await carregarVersoes();
        setForm({ documento_id: docId, numero_versao: versoes.length + 1, conteudo_ref: '', hash_integridade: '' });
      },
      'Versão criada com sucesso',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Criar Nova Versão</h3>
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
                <span>Número da Versão *</span>
                <input
                  type="number"
                  value={form.numero_versao}
                  onChange={(e) => setForm({ ...form, numero_versao: Number(e.target.value) })}
                  required
                  min="1"
                />
              </label>
            </div>
            <label>
              <span>Referência do Conteúdo</span>
              <input
                type="text"
                value={form.conteudo_ref}
                onChange={(e) => setForm({ ...form, conteudo_ref: e.target.value })}
              />
            </label>
            <label>
              <span>Hash de Integridade</span>
              <input
                type="text"
                value={form.hash_integridade}
                onChange={(e) => setForm({ ...form, hash_integridade: e.target.value })}
              />
            </label>
            <div className="form-actions">
              <button type="submit" className="button" disabled={salvando}>
                {salvando ? 'Salvando...' : 'Criar Versão'}
              </button>
            </div>
          </form>
        )}
      </div>

      <TabelaEstado loading={loading} erro={erro} vazio={versoes.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Documento</th>
                <th>Versão</th>
                <th>Data</th>
                <th>Conteúdo Ref</th>
                <th>Hash</th>
                <th>Criado por</th>
              </tr>
            </thead>
            <tbody>
              {versoes.map((v) => (
                <tr key={v.id}>
                  <td className="mono">{documentoTitulo(resources, v.documento_id)}</td>
                  <td>{v.numero_versao}</td>
                  <td>{formatarData(v.data_versao)}</td>
                  <td className="mono">{v.conteudo_ref || '—'}</td>
                  <td className="mono">{v.hash_integridade || '—'}</td>
                  <td>{v.created_by || '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </div>
  );
}