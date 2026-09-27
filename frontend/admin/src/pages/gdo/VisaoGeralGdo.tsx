import { type GdoResources } from './GdoShared';
import { formatarNumero } from './GdoShared';

export interface VisaoGeralGdoProps {
  resources: GdoResources;
}

export function VisaoGeralGdo({ resources }: VisaoGeralGdoProps) {
  const totalDocumentos = resources.documentos.data?.total ?? 0;
  const totalTramitacoes = resources.tramitacoes.data?.length ?? 0;
  const totalVersoes = resources.versoes.data?.length ?? 0;
  const totalAssinaturas = resources.assinaturas.data?.length ?? 0;
  const totalTiposDocumentais = resources.tiposDocumentais.data?.length ?? 0;
  const totalClassificacoes = resources.classificacoes.data?.total ?? 0;

  return (
    <div className="stack gdo-tab-content">
      <h3>Visão Geral da Gestão Documental</h3>
      <p className="muted">Resumo dos principais indicadores do DOM-GDO.</p>

      <div className="grid grid--3 gdo-kpis">
        <article className="kpi-card">
          <dt>Documentos</dt>
          <dd>{formatarNumero(totalDocumentos)}</dd>
        </article>
        <article className="kpi-card">
          <dt>Tramitações</dt>
          <dd>{formatarNumero(totalTramitacoes)}</dd>
        </article>
        <article className="kpi-card">
          <dt>Versões</dt>
          <dd>{formatarNumero(totalVersoes)}</dd>
        </article>
        <article className="kpi-card">
          <dt>Assinaturas</dt>
          <dd>{formatarNumero(totalAssinaturas)}</dd>
        </article>
        <article className="kpi-card">
          <dt>Tipos Documentais</dt>
          <dd>{formatarNumero(totalTiposDocumentais)}</dd>
        </article>
        <article className="kpi-card">
          <dt>Classificações</dt>
          <dd>{formatarNumero(totalClassificacoes)}</dd>
        </article>
      </div>

      <section className="card">
        <h4>Últimos Documentos</h4>
        {resources.documentos.loading && <p className="muted">Carregando...</p>}
        {resources.documentos.erro && <p className="alert alert--error">{resources.documentos.erro}</p>}
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Título</th>
                <th>Ano</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {(resources.documentos.data?.items ?? []).slice(0, 5).map((d) => (
                <tr key={d.id}>
                  <td className="mono">{d.codigo}</td>
                  <td>{d.titulo}</td>
                  <td>{d.ano}</td>
                  <td><span className="badge">{d.status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="card">
        <h4>Ações Rápidas</h4>
        <div className="stack" style={{ gap: 'var(--space-3)' }}>
          <p className="muted">Use as abas acima para gerenciar documentos, tramitações, versões, arquivamentos, assinaturas, tipos documentais, classificações, processos e temporalidades.</p>
        </div>
      </section>
    </div>
  );
}
