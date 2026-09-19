import { useEffect } from 'react';
import { listarPessoas } from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

export default function CumPage() {
  const [lista, recarregar] = useApiData(() => listarPessoas());

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section>
      <div className="page-head">
        <h2 className="section-title">Cadastro Único Municipal (CUM)</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>
      <p className="muted">
        Consulta de pessoas físicas/jurídicas via GET /api/v1/cadastro/pessoas. Cadastro completo
        e organograma de unidades evoluem na próxima iteração.
      </p>
      <TabelaEstado loading={lista.loading} erro={lista.erro} vazio={!lista.data || lista.data.items.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Identificação</th>
                <th>Tipo</th>
                <th>Unidade</th>
              </tr>
            </thead>
            <tbody>
              {(lista.data?.items ?? []).map((p) => (
                <tr key={p.id}>
                  <td>{p.nome_identificacao ?? p.id}</td>
                  <td>
                    <span className="badge">{p.tipo}</span>
                  </td>
                  <td className="mono">{p.unidade_id ?? '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </section>
  );
}
