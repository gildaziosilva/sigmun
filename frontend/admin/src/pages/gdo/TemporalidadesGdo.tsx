import { type TabelaTemporalidadeGDO, obterTemporalidade } from '../../lib/api';
import { formatarData, StatusBadge } from './GdoShared';
import { useState, useEffect } from 'react';
import React from 'react';

export interface TemporalidadesGdoProps {}

export function TemporalidadesGdo(): React.JSX.Element {
  const [codigo, setCodigo] = useState('');
  const [temporalidade, setTemporalidade] = useState<TabelaTemporalidadeGDO | null>(null);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  useEffect(() => {
    if (codigo) {
      carregarTemporalidade();
    }
  }, [codigo]);

  async function carregarTemporalidade() {
    setLoading(true);
    setErro('');
    try {
      const data = await obterTemporalidade(codigo);
      setTemporalidade(data);
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar temporalidade');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="card card--form">
        <h3>Buscar Tabela de Temporalidade</h3>
        <div className="grid grid--2">
          <label>
            <span>Código *</span>
            <input
              type="text"
              value={codigo}
              onChange={(e) => setCodigo(e.target.value)}
              required
              placeholder="Código da tabela"
            />
          </label>
        </div>
      </div>

      {loading && <p className="muted">Carregando...</p>}
      {erro && <p className="alert alert--error" role="alert">{erro}</p>}

      {temporalidade && (
        <article className="card card--detail">
          <h3>
            {temporalidade.codigo} — {temporalidade.nome}
            <button type="button" className="link link--close" onClick={() => setTemporalidade(null)}>Fechar</button>
          </h3>
          <dl className="detail-list">
            <div><dt>Prazo (tempo)</dt><dd>{temporalidade.prazo_tempo} {temporalidade.unidade_tempo}</dd></div>
            <div><dt>Evento Fim</dt><dd>{temporalidade.evento_fim}</dd></div>
            <div><dt>Tipo Destinação</dt><dd>{temporalidade.tipo_destinacao}</dd></div>
            <div><dt>Status</dt><dd><StatusBadge value={temporalidade.is_ativo ? 'ativo' : 'inativo'} /></dd></div>
            <div><dt>Criado em</dt><dd>{formatarData(temporalidade.created_at)}</dd></div>
          </dl>
        </article>
      )}
    </div>
  );
}
