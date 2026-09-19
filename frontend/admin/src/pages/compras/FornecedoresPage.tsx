import { useEffect } from 'react';
import { listarContratos, listarFornecedores } from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

export default function FornecedoresPage() {
  const [fornecedores, recarregarForn] = useApiData(() => listarFornecedores());
  const [contratos, recarregarCont] = useApiData(() => listarContratos());

  useEffect(() => {
    recarregarForn();
    recarregarCont();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function recarregar() {
    recarregarForn();
    recarregarCont();
  }

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Fornecedores e Contratos</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>

      <h3 className="subsection-title">Fornecedores · GET /api/v1/fornecedores</h3>
      <TabelaEstado
        loading={fornecedores.loading}
        erro={fornecedores.erro}
        vazio={!fornecedores.data || fornecedores.data.items.length === 0}
      >
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Pessoa jurídica</th>
                <th>Situação</th>
                <th>Categoria</th>
              </tr>
            </thead>
            <tbody>
              {(fornecedores.data?.items ?? []).map((f) => (
                <tr key={f.id}>
                  <td className="mono">{f.pessoa_juridica_id}</td>
                  <td>
                    <span className="badge">{f.situacao_cadastro}</span>
                  </td>
                  <td>{f.macro_categoria ?? '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>

      <h3 className="subsection-title">Contratos · GET /api/v1/contratos</h3>
      <TabelaEstado
        loading={contratos.loading}
        erro={contratos.erro}
        vazio={!contratos.data || contratos.data.items.length === 0}
      >
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Número</th>
                <th>Detalhe</th>
              </tr>
            </thead>
            <tbody>
              {(contratos.data?.items ?? []).map((c) => (
                <tr key={c.id}>
                  <td className="mono">{String(c.id).slice(0, 8)}…</td>
                  <td>{c.numero ?? '—'}</td>
                  <td className="mono">{JSON.stringify(c).slice(0, 80)}…</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </section>
  );
}
