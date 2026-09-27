import { useState } from 'react';
import type { EduResources } from '../EduShared';
import { formatarData, StatusBadge, Field } from '../EduShared';

interface Props {
  resources: EduResources;
}

export function TransporteTab({ resources }: Props) {
  const { rotas, passagens } = resources;
  const [filtroRotaId, setFiltroRotaId] = useState('');

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Transporte Escolar</h3>
        <p className="muted">Rotas e embarques (passagens) do transporte escolar.</p>
      </header>

      <article className="sau-card">
        <h4>Rotas</h4>
        {rotas.loading && <p className="muted">Carregando rotas…</p>}
        {rotas.erro && <p className="sau-feedback sau-feedback--error" role="alert">{rotas.erro}</p>}
        {rotas.data?.length === 0 && !rotas.loading && !rotas.erro && <p className="muted">Nenhuma rota cadastrada.</p>}

        {rotas.data && rotas.data.length > 0 && (
          <div className="sau-table-wrap">
            <table className="sau-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Identificação</th>
                  <th>Veículo</th>
                  <th>Motorista</th>
                  <th>Vagas</th>
                  <th>Turno</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {rotas.data.map((r) => (
                  <tr key={r.id}>
                    <td className="mono">{r.id.slice(0, 8)}…</td>
                    <td>{r.identificacao}</td>
                    <td>{r.veiculo || '—'}</td>
                    <td>{r.motorista}</td>
                    <td>{r.vagas}</td>
                    <td>{r.turno}</td>
                    <td><StatusBadge value={r.status} /></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>

      <article className="sau-card">
        <h4>Passagens (Embarques)</h4>
        <Field
          label="Filtrar por Rota (opcional)"
          value={filtroRotaId}
          onChange={setFiltroRotaId}
          placeholder="UUID da rota"
        />
        {passagens.loading && <p className="muted">Carregando passagens…</p>}
        {passagens.erro && <p className="sau-feedback sau-feedback--error" role="alert">{passagens.erro}</p>}
        {passagens.data?.length === 0 && !passagens.loading && !passagens.erro && <p className="muted">Nenhuma passagem encontrada.</p>}

        {passagens.data && passagens.data.length > 0 && (
          <div className="sau-table-wrap">
            <table className="sau-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Rota</th>
                  <th>Matrícula</th>
                  <th>Data</th>
                </tr>
              </thead>
              <tbody>
                {passagens.data.map((p) => (
                  <tr key={p.id}>
                    <td className="mono">{p.id.slice(0, 8)}…</td>
                    <td className="mono">{p.rota_id.slice(0, 8)}…</td>
                    <td className="mono">{p.matricula_id.slice(0, 8)}…</td>
                    <td>{formatarData(p.data)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>
    </section>
  );
}
