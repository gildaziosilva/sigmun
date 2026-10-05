import { useEffect, useState } from 'react';
import { listarManifestacoesOuv, listarDenunciasOuv, listarPedidosLaiOuv, obterEstatisticasOuv, type EstatisticasOuv as EstatisticasOuvType } from '../../lib/api';
import { OUV_TABS, type OuvTab, type OuvResources, type ExecutarOuv } from './OuvShared';
import { VisaoGeralOuv } from './VisaoGeralOuv';
import { ManifestacoesOuv } from './ManifestacoesOuv';
import { DenunciasOuv } from './DenunciasOuv';
import { PedidosLaiOuv } from './PedidosLaiOuv';
import { EstatisticasOuv } from './EstatisticasOuv';

// ==================== Tipos ====================

interface OuvPageState {
  resources: OuvResources;
  estatisticas: EstatisticasOuvType | null;
  carregando: boolean;
  abaAtiva: OuvTab;
}

const initialResources: OuvResources = {
  manifestacoes: { data: null, loading: true, erro: '' },
  denuncias: { data: null, loading: true, erro: '' },
  pedidosLai: { data: null, loading: true, erro: '' },
  recarregar: () => {},
};

// ==================== Componente Principal ====================

export function OuvPage() {
  const [state, setState] = useState<OuvPageState>({
    resources: initialResources,
    estatisticas: null,
    carregando: true,
    abaAtiva: 'visao-geral',
  });

  // Recarregar todos os dados
  const recarregar = async () => {
    setState((s) => ({
      ...s,
      resources: {
        ...s.resources,
        manifestacoes: { ...s.resources.manifestacoes, loading: true },
        denuncias: { ...s.resources.denuncias, loading: true },
        pedidosLai: { ...s.resources.pedidosLai, loading: true },
      },
    }));

    try {
      const [m, d, p, e] = await Promise.all([
        listarManifestacoesOuv({ page_size: 100 }),
        listarDenunciasOuv({ page_size: 100 }),
        listarPedidosLaiOuv({ page_size: 100 }),
        obterEstatisticasOuv(),
      ]);

      setState((s) => ({
        ...s,
        resources: {
          manifestacoes: { data: m.items, loading: false, erro: '' },
          denuncias: { data: d.items, loading: false, erro: '' },
          pedidosLai: { data: p.items, loading: false, erro: '' },
          recarregar,
        },
        estatisticas: e,
        carregando: false,
      }));
    } catch (err) {
      console.error('Erro ao carregar dados da ouvidoria:', err);
      setState((s) => ({
        ...s,
        resources: {
          manifestacoes: { data: null, loading: false, erro: 'Falha ao carregar manifestações' },
          denuncias: { data: null, loading: false, erro: 'Falha ao carregar denúncias' },
          pedidosLai: { data: null, loading: false, erro: 'Falha ao carregar pedidos LAI' },
          recarregar,
        },
        carregando: false,
      }));
    }
  };

  // Carregar dados iniciais
  useEffect(() => {
    recarregar();
  }, []);

  // Executar ação com feedback
  const executar: ExecutarOuv = async (acao, msgSucesso) => {
    try {
      await acao();
      await recarregar();
      alert(msgSucesso);
      return true;
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Erro desconhecido';
      alert(`Erro: ${msg}`);
      return false;
    }
  };

  const salvando = false; // TODO: implementar estado global de salvando

  if (state.carregando) {
    return <div className="ouv-loading">Carregando ouvidoria…</div>;
  }

  return (
    <div className="ouv-page">
      <header className="ouv-header">
        <div className="ouv-header-title">
          <h1>Ouvidoria FalaBR / e-OUV</h1>
          <p className="muted">Manifestações, denúncias e Lei de Acesso à Informação</p>
        </div>
        <div className="ouv-header-actions">
          <button className="button button--primary" onClick={recarregar} disabled={state.carregando}>
            Atualizar
          </button>
        </div>
      </header>

      <nav className="ouv-tabs" aria-label="Abas da ouvidoria">
        {OUV_TABS.map((tab) => (
          <button
            key={tab.id}
            type="button"
            className={state.abaAtiva === tab.id ? 'active' : ''}
            aria-current={state.abaAtiva === tab.id ? 'page' : undefined}
            onClick={() => setState((s) => ({ ...s, abaAtiva: tab.id }))}
          >
            {tab.rotulo}
          </button>
        ))}
      </nav>

      <main className="ouv-main">
        {state.abaAtiva === 'visao-geral' && (
          <VisaoGeralOuv
            resources={state.resources}
            estatisticas={state.estatisticas}
          />
        )}

        {state.abaAtiva === 'manifestacoes' && (
          <ManifestacoesOuv
            resources={state.resources}
            executar={executar}
            salvando={salvando}
          />
        )}

        {state.abaAtiva === 'denuncias' && (
          <DenunciasOuv
            resources={state.resources}
            executar={executar}
            salvando={salvando}
          />
        )}

        {state.abaAtiva === 'pedidos-lai' && (
          <PedidosLaiOuv
            resources={state.resources}
            executar={executar}
            salvando={salvando}
          />
        )}

        {state.abaAtiva === 'estatisticas' && (
          <EstatisticasOuv
            resources={state.resources}
            estatisticas={state.estatisticas}
          />
        )}
      </main>
    </div>
  );
}

// ==================== Export ====================

export default OuvPage;
