import { type ProcessoDocumentoGDO, obterProcesso } from '../../lib/api';
import { formatarData, StatusBadge } from './GdoShared';
import { useState, useEffect } from 'react';
import React from 'react';

export interface ProcessosGdoProps {}

export function ProcessosGdo(): React.JSX.Element {
  const [processoId, setProcessoId] = useState('');
  const [processo, setProcesso] = useState<ProcessoDocumentoGDO | null>(null);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  useEffect(() => {
    if (processoId) {
      carregarProcesso();
    }
  }, [processoId]);

  async function carregarProcesso() {
    setLoading(true);
    setErro('');
    try {
      const data = await obterProcesso(processoId);
      setProcesso(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar processo');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Buscar Processo Documental</h3>
        <div className="grid grid--2">
          <label>
            <span>Processo ID *</span>
            <input
              type="text"
              value={processoId}
              onChange={(e) => setProcessoId(e.target.value)}
              required
              placeholder="UUID do processo"
            />
          </label>
        </div>
      </div>

      {loading && <p className="muted">Carregando...</p>}
      {erro && <p className="alert alert--error" role="alert">{erro}</p>}

      {processo && (
        <article className="card card--detail">
          <h3>
            {processo.numero}/{processo.ano} — {processo.titulo}
            <button type="button" className="link link--close" onClick={() => setProcesso(null)}>Fechar</button>
          </h3>
          <dl className="detail-list">
            <div><dt>Número/Ano</dt><dd>{processo.numero}/{processo.ano}</dd></div>
            <div><dt>Tipo Processo</dt><dd className="mono">{processo.tipo_processo_id}</dd></div>
            <div><dt>Unidade Autora</dt><dd className="mono">{processo.unidade_autor_id}</dd></div>
            <div><dt>Data Abertura</dt><dd>{formatarData(processo.data_abertura)}</dd></div>
            <div><dt>Data Encerramento</dt><dd>{formatarData(processo.data_encerramento)}</dd></div>
            <div><dt>Status</dt><dd><StatusBadge value={processo.status} /></dd></div>
            <div><dt>Ativo</dt><dd>{processo.is_active ? 'Sim' : 'Não'}</dd></div>
            <div><dt>Criado em</dt><dd>{formatarData(processo.created_at)}</dd></div>
          </dl>
        </article>
      )}
    </div>
  );
}
