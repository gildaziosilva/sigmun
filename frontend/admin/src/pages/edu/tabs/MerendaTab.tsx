import { useState } from 'react';
import type { EduResources } from '../EduShared';
import { formatarData, StatusBadge, Field } from '../EduShared';

interface Props {
  resources: EduResources;
}

export function MerendaTab({ resources }: Props) {
  const { itensMerenda, distribuicoes } = resources;
  const [filtroMatriculaId, setFiltroMatriculaId] = useState('');

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Merenda Escolar</h3>
        <p className="muted">Estoque de itens e distribuições da merenda escolar.</p>
      </header>

      <article className="sau-card">
        <h4>Itens de Merenda (Estoque)</h4>
        {itensMerenda.loading && <p className="muted">Carregando itens…</p>}
        {itensMerenda.erro && <p className="sau-feedback sau-feedback--error" role="alert">{itensMerenda.erro}</p>}
        {itensMerenda.data?.length === 0 && !itensMerenda.loading && !itensMerenda.erro && <p className="muted">Nenhum item cadastrado.</p>}

        {itensMerenda.data && itensMerenda.data.length > 0 && (
          <div className="sau-table-wrap">
            <table className="sau-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>Tipo</th>
                  <th>Estoque</th>
                  <th>Mínimo</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {itensMerenda.data.map((i) => (
                  <tr key={i.id}>
                    <td className="mono">{i.id.slice(0, 8)}…</td>
                    <td>{i.nome}</td>
                    <td>{i.tipo}</td>
                    <td>{i.estoque}</td>
                    <td>{i.estoque_minimo}</td>
                    <td><StatusBadge value={i.estoque < i.estoque_minimo ? 'abaixo_mínimo' : 'ok'} /></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>

      <article className="sau-card">
        <h4>Distribuições de Merenda</h4>
        <Field
          label="Filtrar por Matrícula (opcional)"
          value={filtroMatriculaId}
          onChange={setFiltroMatriculaId}
          placeholder="UUID da matrícula"
        />
        {distribuicoes.loading && <p className="muted">Carregando distribuições…</p>}
        {distribuicoes.erro && <p className="sau-feedback sau-feedback--error" role="alert">{distribuicoes.erro}</p>}
        {distribuicoes.data?.length === 0 && !distribuicoes.loading && !distribuicoes.erro && <p className="muted">Nenhuma distribuição encontrada.</p>}

        {distribuicoes.data && distribuicoes.data.length > 0 && (
          <div className="sau-table-wrap">
            <table className="sau-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Matrícula</th>
                  <th>Item</th>
                  <th>Quantidade</th>
                  <th>Refeição</th>
                  <th>Data</th>
                </tr>
              </thead>
              <tbody>
                {distribuicoes.data.map((d) => (
                  <tr key={d.id}>
                    <td className="mono">{d.id.slice(0, 8)}…</td>
                    <td className="mono">{d.matricula_id.slice(0, 8)}…</td>
                    <td className="mono">{d.item_id.slice(0, 8)}…</td>
                    <td>{d.quantidade}</td>
                    <td>{d.refeicao}</td>
                    <td>{formatarData(d.data)}</td>
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
