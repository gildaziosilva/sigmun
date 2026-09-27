import type { EduResources } from './EduShared';
import { formatarNumero } from './EduShared';

interface Props {
  resources: EduResources;
}

export function VisaoGeralEdu({ resources }: Props) {
  const { alunos, matriculas, rotas, itensMerenda } = resources;

  const totalAlunos = alunos.data?.length ?? 0;
  const totalMatriculas = matriculas.data?.length ?? 0;
  const totalRotas = rotas.data?.length ?? 0;
  const itensBaixoEstoque = itensMerenda.data?.filter((i) => i.estoque < i.estoque_minimo).length ?? 0;

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Visão Geral</h3>
        <p className="muted">Resumo dos principais indicadores da rede municipal de ensino.</p>
      </header>

      <div className="sau-cards-grid">
        <article className="sau-card sau-card--kpi">
          <div className="sau-kpi-icon">👨‍🎓</div>
          <div className="sau-kpi-value">{formatarNumero(totalAlunos)}</div>
          <div className="sau-kpi-label">Alunos Cadastrados</div>
        </article>

        <article className="sau-card sau-card--kpi">
          <div className="sau-kpi-icon">📝</div>
          <div className="sau-kpi-value">{formatarNumero(totalMatriculas)}</div>
          <div className="sau-kpi-label">Matrículas Ativas</div>
        </article>

        <article className="sau-card sau-card--kpi">
          <div className="sau-kpi-icon">🚌</div>
          <div className="sau-kpi-value">{formatarNumero(totalRotas)}</div>
          <div className="sau-kpi-label">Rotas de Transporte</div>
        </article>

        <article className="sau-card sau-card--kpi">
          <div className="sau-kpi-icon">🍎</div>
          <div className="sau-kpi-value">{formatarNumero(itensBaixoEstoque)}</div>
          <div className="sau-kpi-label">Itens com Estoque Baixo</div>
        </article>
      </div>

      <div className="sau-section-divider" />

      <h4>Ações Rápidas</h4>
      <div className="sau-quick-actions">
        <button type="button" className="button button--ghost">Consultar Aluno</button>
        <button type="button" className="button button--ghost">Nova Matrícula</button>
        <button type="button" className="button button--ghost">Registrar Frequência</button>
        <button type="button" className="button button--ghost">Nova Rota de Transporte</button>
        <button type="button" className="button button--ghost">Entrada de Merenda</button>
      </div>
    </section>
  );
}
