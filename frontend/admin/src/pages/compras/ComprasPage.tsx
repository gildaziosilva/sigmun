import { useEffect } from 'react';
import { listarCompras, obterCompra, type Compra } from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';
import { useState } from 'react';

export default function ComprasPage() {
  const [lista, recarregar] = useApiData(() => listarCompras());
  const [detalheId, setDetalheId] = useState('');
  const [detalhe, setDetalhe] = useState<Compra | null>(null);
  const [detalheErro, setDetalheErro] = useState('');

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function verDetalhe(id: string) {
    setDetalheId(id);
    setDetalheErro('');
    try {
      setDetalhe(await obterCompra(id));
    } catch (err) {
      setDetalheErro(err instanceof Error ? err.message : 'Falha ao carregar compra.');
    }
  }

  return (
    <section>
      <div className="page-head">
        <h2 className="section-title">Compras e Contratos — Processos</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>
      <TabelaEstado loading={lista.loading} erro={lista.erro} vazio={!lista.data || lista.data.items.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Número</th>
                <th>Situação</th>
                <th>Valor</th>
                <th>Data</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {(lista.data?.items ?? []).map((c) => (
                <tr key={c.id} className={detalheId === c.id ? 'row--active' : undefined}>
                  <td>{c.numero}</td>
                  <td>
                    <span className="badge">{c.situacao}</span>
                  </td>
                  <td>{c.valor_total ?? '—'}</td>
                  <td>{c.data}</td>
                  <td>
                    <button type="button" className="link" onClick={() => verDetalhe(c.id)}>
                      Detalhe
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="muted">Total: {lista.data?.total ?? 0} processo(s) · GET /api/v1/compras</p>
      </TabelaEstado>

      {detalhe && (
        <article className="card card--detail">
          <h3>Processo {detalhe.numero}</h3>
          <dl className="detail-list">
            <div>
              <dt>Situação</dt>
              <dd>{detalhe.situacao}</dd>
            </div>
            <div>
              <dt>Fornecedor</dt>
              <dd className="mono">{detalhe.fornecedor_id}</dd>
            </div>
            <div>
              <dt>Processo documental</dt>
              <dd className="mono">{detalhe.processo_documental_id}</dd>
            </div>
            <div>
              <dt>Unidade</dt>
              <dd className="mono">{detalhe.unidade_id}</dd>
            </div>
          </dl>
          <button type="button" className="link" onClick={() => setDetalhe(null)}>
            Fechar detalhe
          </button>
        </article>
      )}
      {detalheErro && (
        <p className="alert alert--error" role="alert">
          {detalheErro}
        </p>
      )}
    </section>
  );
}
