import { useEffect, useState } from 'react';
import { listarDocumentos, obterDocumento, type DocumentoGDO } from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

export default function GdoPage() {
  const [lista, recarregar] = useApiData(() => listarDocumentos());
  const [detalhe, setDetalhe] = useState<DocumentoGDO | null>(null);
  const [detalheErro, setDetalheErro] = useState('');

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function verDetalhe(id: string) {
    setDetalheErro('');
    try {
      setDetalhe(await obterDocumento(id));
    } catch (err) {
      setDetalheErro(err instanceof Error ? err.message : 'Falha ao carregar documento.');
    }
  }

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Gestão Documental (GDO)</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>
      <p className="muted">
        Listagem e detalhe via GET /api/v1/gdo/documentos. Upload de binários, versionamento,
        tramitação e assinatura digital evoluem em iterações seguintes (escopo VI.2 parcial).
      </p>
      <TabelaEstado loading={lista.loading} erro={lista.erro} vazio={!lista.data || lista.data.items.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Título</th>
                <th>Ano</th>
                <th>Status</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {(lista.data?.items ?? []).map((d) => (
                <tr key={d.id}>
                  <td className="mono">{d.codigo}</td>
                  <td>{d.titulo}</td>
                  <td>{d.ano}</td>
                  <td>
                    <span className="badge">{d.status}</span>
                    {d.is_sigiloso && <span className="badge badge--warn">sigiloso</span>}
                  </td>
                  <td>
                    <button type="button" className="link" onClick={() => verDetalhe(d.id)}>
                      Detalhe
                    </button>
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
            {detalhe.codigo} — {detalhe.titulo}
          </h3>
          <dl className="detail-list">
            <div>
              <dt>Número/Ano</dt>
              <dd>
                {detalhe.numero}/{detalhe.ano}
              </dd>
            </div>
            <div>
              <dt>Tipo documental</dt>
              <dd className="mono">{detalhe.tipo_documental_id}</dd>
            </div>
            <div>
              <dt>Unidade autora</dt>
              <dd className="mono">{detalhe.unidade_autor_id}</dd>
            </div>
            <div>
              <dt>Status</dt>
              <dd>{detalhe.status}</dd>
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
