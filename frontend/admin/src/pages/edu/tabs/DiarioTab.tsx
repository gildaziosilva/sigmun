import { useState } from 'react';
import { listarLancamentosPorMatricula } from '../../../lib/api';
import type { EduResources, ExecutarEdu } from '../EduShared';
import { formatarData, Field } from '../EduShared';

interface Props {
  resources: EduResources;
  executar: ExecutarEdu;
  salvando: boolean;
}

export function DiarioTab({ resources, executar, salvando }: Props) {
  const { lancamentos } = resources;
  const [matriculaId, setMatriculaId] = useState('');

  async function carregar() {
    if (!matriculaId.trim()) return;
    await executar(async () => {
      await listarLancamentosPorMatricula(matriculaId.trim());
    }, 'Lançamentos carregados');
  }

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Diário de Classe</h3>
        <p className="muted">Lançamentos de frequência e notas por matrícula.</p>
      </header>

      <div className="sau-form-row">
        <Field
          label="Matrícula ID"
          value={matriculaId}
          onChange={setMatriculaId}
          placeholder="UUID da matrícula"
        />
        <button type="button" className="button" onClick={carregar} disabled={!matriculaId.trim() || salvando}>
          Consultar
        </button>
      </div>

      {lancamentos.loading && <p className="muted">Carregando lançamentos…</p>}
      {lancamentos.erro && <p className="sau-feedback sau-feedback--error" role="alert">{lancamentos.erro}</p>}
      {lancamentos.data?.length === 0 && !lancamentos.loading && !lancamentos.erro && <p className="muted">Nenhum lançamento encontrado.</p>}

      {lancamentos.data && lancamentos.data.length > 0 && (
        <div className="sau-table-wrap">
          <table className="sau-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Matrícula</th>
                <th>Data</th>
                <th>Presente</th>
                <th>Nota</th>
                <th>Observação</th>
              </tr>
            </thead>
            <tbody>
              {lancamentos.data.map((l) => (
                <tr key={l.id}>
                  <td className="mono">{l.id.slice(0, 8)}…</td>
                  <td className="mono">{l.matricula_id.slice(0, 8)}…</td>
                  <td>{formatarData(l.data)}</td>
                  <td>{l.presente ? 'Sim' : 'Não'}</td>
                  <td>{l.nota !== null ? l.nota : '—'}</td>
                  <td>{l.observacao || '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
