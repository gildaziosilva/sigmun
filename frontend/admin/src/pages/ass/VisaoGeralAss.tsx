import type { AssResources } from './AssShared';
import { StatusBadge, formatarData, formatarNumero } from './AssShared';

interface Props { resources: AssResources; }

export function VisaoGeralAss({ resources }: Props) {
  const { familias, pessoas, unidades, beneficios, atendimentos } = resources;

  const totalFamilias = familias.data?.length ?? 0;
  const totalPessoas = pessoas.data?.length ?? 0;
  const totalUnidades = unidades.data?.filter(u => u.status === 'ativa').length ?? 0;
  const beneficiosSolicitados = beneficios.data?.filter(b => b.status === 'solicitado').length ?? 0;
  const beneficiosAprovados = beneficios.data?.filter(b => b.status === 'aprovado').length ?? 0;
  const beneficiosEntregues = beneficios.data?.filter(b => b.status === 'entregue').length ?? 0;
  const totalAtendimentos = atendimentos.data?.length ?? 0;

  const ultimasFamilias = familias.data?.slice(-5).reverse() ?? [];
  const ultimosBeneficios = beneficios.data?.slice(-5).reverse() ?? [];
  const ultimosAtendimentos = atendimentos.data?.slice(-5).reverse() ?? [];

  return (
    <section className="stack ass-visao-geral">
      <div className="card-grid ass-kpis">
        <article className="card kpi"><h3>Famílias cadastradas</h3><p className="kpi-value">{formatarNumero(totalFamilias)}</p></article>
        <article className="card kpi"><h3>Pessoas cadastradas</h3><p className="kpi-value">{formatarNumero(totalPessoas)}</p></article>
        <article className="card kpi"><h3>Unidades ativas (CRAS/CREAS)</h3><p className="kpi-value">{formatarNumero(totalUnidades)}</p></article>
        <article className="card kpi"><h3>Benefícios solicitados</h3><p className="kpi-value">{formatarNumero(beneficiosSolicitados)}</p></article>
        <article className="card kpi"><h3>Benefícios aprovados</h3><p className="kpi-value">{formatarNumero(beneficiosAprovados)}</p></article>
        <article className="card kpi"><h3>Benefícios entregues</h3><p className="kpi-value">{formatarNumero(beneficiosEntregues)}</p></article>
        <article className="card kpi"><h3>Atendimentos registrados</h3><p className="kpi-value">{formatarNumero(totalAtendimentos)}</p></article>
      </div>

      <div className="ass-recentes">
        <section className="card ass-recentes-card">
          <h3>Últimas famílias cadastradas</h3>
          {ultimasFamilias.length === 0 ? (
            <p className="muted">Nenhuma família cadastrada.</p>
          ) : (
            <table className="ass-table">
              <thead>
                <tr><th>NIS</th><th>Responsável</th><th>Renda per capita</th><th>Pessoas</th><th>Status</th><th>Cadastrada em</th></tr>
              </thead>
              <tbody>
                {ultimasFamilias.map((f) => (
                  <tr key={f.id}>
                    <td>{f.nis}</td>
                    <td>{f.responsavel_nome}</td>
                    <td>R$ {new Intl.NumberFormat('pt-BR', { minimumFractionDigits: 2 }).format(f.renda_per_capita)}</td>
                    <td>{f.quantidade_pessoas}</td>
                    <td><StatusBadge value={f.status} /></td>
                    <td>{formatarData(f.created_at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>

        <section className="card ass-recentes-card">
          <h3>Últimos benefícios solicitados</h3>
          {ultimosBeneficios.length === 0 ? (
            <p className="muted">Nenhum benefício solicitado.</p>
          ) : (
            <table className="ass-table">
              <thead>
                <tr><th>Família</th><th>Tipo</th><th>Valor</th><th>Qtd</th><th>Status</th><th>Solicitado em</th></tr>
              </thead>
              <tbody>
                {ultimosBeneficios.map((b) => (
                  <tr key={b.id}>
                    <td>{b.familia_id}</td>
                    <td>{b.tipo}</td>
                    <td>R$ {new Intl.NumberFormat('pt-BR', { minimumFractionDigits: 2 }).format(b.valor)}</td>
                    <td>{b.quantidade}</td>
                    <td><StatusBadge value={b.status} /></td>
                    <td>{formatarData(b.data_solicitacao)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>

        <section className="card ass-recentes-card">
          <h3>Últimos atendimentos</h3>
          {ultimosAtendimentos.length === 0 ? (
            <p className="muted">Nenhum atendimento registrado.</p>
          ) : (
            <table className="ass-table">
              <thead>
                <tr><th>Pessoa</th><th>Unidade</th><th>Tipo</th><th>Profissional</th><th>Data</th></tr>
              </thead>
              <tbody>
                {ultimosAtendimentos.map((a) => (
                  <tr key={a.id}>
                    <td>{a.pessoa_id}</td>
                    <td>{a.unidade_id}</td>
                    <td>{a.tipo}</td>
                    <td>{a.profissional}</td>
                    <td>{formatarData(a.data)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>
      </div>
    </section>
  );
}