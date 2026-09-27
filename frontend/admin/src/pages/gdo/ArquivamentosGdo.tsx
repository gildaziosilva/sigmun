import { type ArquivamentoCreateRequest, arquivarDocumento } from '../../lib/api';
import { type ExecutarGdo } from './GdoShared';
import { useState } from 'react';

export interface ArquivamentosGdoProps {
  executar: ExecutarGdo;
  salvando: boolean;
}

export function ArquivamentosGdo({ executar, salvando }: ArquivamentosGdoProps) {
  const [docId, setDocId] = useState('');
  const [form, setForm] = useState<ArquivamentoCreateRequest>({
    unidade_arquivo_id: '',
    autor_id: '',
    observacao: '',
  });

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await arquivarDocumento(docId, form);
        setForm({ unidade_arquivo_id: '', autor_id: '', observacao: '' });
      },
      'Documento arquivado com sucesso',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Arquivar Documento</h3>
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
                <span>Unidade Arquivo *</span>
                <input
                  type="text"
                  value={form.unidade_arquivo_id}
                  onChange={(e) => setForm({ ...form, unidade_arquivo_id: e.target.value })}
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
              <span>Observação</span>
              <input
                type="text"
                value={form.observacao}
                onChange={(e) => setForm({ ...form, observacao: e.target.value })}
              />
            </label>
            <div className="form-actions">
              <button type="submit" className="button" disabled={salvando}>
                {salvando ? 'Salvando...' : 'Arquivar'}
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}