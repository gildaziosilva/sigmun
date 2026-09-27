import type { EduResources } from '../EduShared';
import { StatusBadge } from '../EduShared';

interface Props {
  resources: EduResources;
}

export function MatriculasTab({ resources }: Props) {
  const { matriculas } = resources;

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Matrículas</h3>
        <p className="muted">Matrículas escolares ativas e históricas.</p>
      </header>

      {matriculas.loading && <p className="muted">Carregando matrículas…</p>}
      {matriculas.erro && <p className="sau-feedback sau-feedback--error" role="alert">{matriculas.erro}</p>}
      {matriculas.data?.length === 0 && !matriculas.loading && !matriculas.erro && <p className="muted">Nenhuma matrícula encontrada.</p>}

      {matriculas.data && matriculas.data.length > 0 && (
        <div className="sau-table-wrap">
          <table className="sau-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Aluno</th>
                <th>Escola</th>
                <th>Série</th>
                <th>Turno</th>
                <th>Ano Letivo</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {matriculas.data.map((m) => (
                <tr key={m.id}>
                  <td className="mono">{m.id.slice(0, 8)}…</td>
                  <td className="mono">{m.aluno_id.slice(0, 8)}…</td>
                  <td>{m.escola}</td>
                  <td>{m.serie}</td>
                  <td>{m.turno}</td>
                  <td>{m.ano_letivo}</td>
                  <td><StatusBadge value={m.status} /></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
