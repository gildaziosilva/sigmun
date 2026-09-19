import { useEffect } from 'react';
import { listarUsuarios } from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

export default function IdnPage() {
  const [lista, recarregar] = useApiData(() => listarUsuarios());

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section>
      <div className="page-head">
        <h2 className="section-title">Identidade e Acesso (IDN)</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>
      <p className="muted">
        Gestão de usuários via GET /api/v1/idn/usuarios. Atribuição de perfis e trilha de
        acessos evoluem na próxima iteração.
      </p>
      <TabelaEstado loading={lista.loading} erro={lista.erro} vazio={!lista.data || lista.data.items.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Login</th>
                <th>E-mail</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {(lista.data?.items ?? []).map((u) => (
                <tr key={u.id}>
                  <td>{u.nome}</td>
                  <td className="mono">{u.login}</td>
                  <td>{u.email}</td>
                  <td>
                    <span className="badge">{u.status}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>
    </section>
  );
}
