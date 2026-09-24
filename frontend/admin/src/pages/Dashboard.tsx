import { useEffect, useState } from 'react';
import { temAcesso, useAuth } from '../auth/AuthContext';
import { fetchHealth, type HealthStatus } from '../lib/api';
import ComprasPage from './compras/ComprasPage';
import FornecedoresPage from './compras/FornecedoresPage';
import CumPage from './cum/CumPage';
import GdoPage from './gdo/GdoPage';
import IdnPage from './idn/IdnPage';
import TriPage from './tri/TriPage';
import PatPage from './pat/PatPage';
import FroPage from './fro/FroPage';
import SauPage from './sau/SauPage';

const NAV_ITEMS = [
  { id: 'painel', rotulo: 'Painel' },
  { id: 'compras', rotulo: 'Compras' },
  { id: 'fornecedores', rotulo: 'Fornecedores' },
  { id: 'gdo', rotulo: 'Documentos' },
  { id: 'cum', rotulo: 'Cadastro Único' },
  { id: 'tri', rotulo: 'Tributos' },
  { id: 'pat', rotulo: 'Patrimônio' },
  { id: 'fro', rotulo: 'Frota' },
  { id: 'sau', rotulo: 'Saúde' },
  { id: 'usuarios', rotulo: 'Usuários' },
] as const;

type Rota = (typeof NAV_ITEMS)[number]['id'];

function Dashboard() {
  const { session, perfil, sair } = useAuth();
  const [aba, setAba] = useState<Rota>('painel');
  const [saude, setSaude] = useState<HealthStatus | null>(null);
  const [saudeErro, setSaudeErro] = useState('');

  useEffect(() => {
    fetchHealth()
      .then(setSaude)
      .catch((err: unknown) => {
        setSaudeErro(err instanceof Error ? err.message : 'API indisponível');
      });
  }, []);

  const nome = session?.usuario?.nome ?? session?.login ?? 'Servidor(a)';
  const email = session?.usuario?.email ?? '';
  const iniciais = nome
    .split(' ')
    .slice(0, 2)
    .map((p) => p.charAt(0))
    .join('')
    .toUpperCase();

  const rotaPermitida: Rota = temAcesso(perfil, aba) ? aba : 'painel';

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <span className="brand-mark" aria-hidden="true">
            S
          </span>
          <div>
            <strong>SIGMUN</strong>
            <small>Gestão Municipal</small>
          </div>
        </div>

        <nav className="sidebar-nav" aria-label="Navegação principal">
          {NAV_ITEMS.map((item) => {
            if (!temAcesso(perfil, item.id)) return null;
            return (
              <button
                key={item.id}
                type="button"
                className={item.id === rotaPermitida ? 'active' : ''}
                aria-current={item.id === rotaPermitida ? 'page' : undefined}
                onClick={() => setAba(item.id)}
              >
                {item.rotulo}
              </button>
            );
          })}
        </nav>

        <div className="sidebar-user">
          <small>{perfil === 'admin' ? 'Administrador' : 'Servidor'}</small>
        </div>

        <button type="button" className="button button--ghost button--sair" onClick={sair}>
          Sair
        </button>
      </aside>

      <div className="content">
        <header className="topbar">
          <div>
            <h1 className="topbar-title">{NAV_ITEMS.find((n) => n.id === rotaPermitida)?.rotulo}</h1>
            <p className="topbar-subtitle">Bem-vindo(a), {nome}</p>
          </div>
          <span className="topbar-user" title={email || nome}>
            {iniciais}
          </span>
        </header>

        <main className="main">
          {rotaPermitida === 'painel' && (
            <section>
              <h2 className="section-title">Status do sistema</h2>
              <div className={`card status-card ${saude ? 'status-card--ok' : 'status-card--error'}`}>
                <span className="status-dot" aria-hidden="true" />
                {saude ? (
                  <p>
                    Backend <strong>{saude.service}</strong> está <strong>{saude.status}</strong>{' '}
                    (versão {saude.version}
                    {saude.database ? `, banco ${saude.database}` : ''}).
                  </p>
                ) : (
                  <p>{saudeErro || 'Verificando API…'}</p>
                )}
              </div>
              <div className="card-grid">
                <article className="card card--modulo">
                  <h3>Compras</h3>
                  <p>Processos, fornecedores e contratos.</p>
                  <button type="button" className="link" onClick={() => setAba('compras')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Documentos</h3>
                  <p>Gestão documental (GDO).</p>
                  <button type="button" className="link" onClick={() => setAba('gdo')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Cadastro Único</h3>
                  <p>Pessoas físicas e jurídicas.</p>
                  <button type="button" className="link" onClick={() => setAba('cum')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Tributos</h3>
                  <p>Lançamentos tributários e dívida ativa.</p>
                  <button type="button" className="link" onClick={() => setAba('tri')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Patrimônio</h3>
                  <p>Bens, tombamento e depreciação.</p>
                  <button type="button" className="link" onClick={() => setAba('pat')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Frota</h3>
                  <p>Veículos, abastecimentos e manutenções.</p>
                  <button type="button" className="link" onClick={() => setAba('fro')}>
                    Abrir módulo
                  </button>
                </article>
                <article className="card card--modulo">
                  <h3>Saúde</h3>
                  <p>Prontuário, agenda SUS, regulação e farmácia.</p>
                  <button type="button" className="link" onClick={() => setAba('sau')}>
                    Abrir módulo
                  </button>
                </article>
              </div>
            </section>
          )}

          {rotaPermitida === 'compras' && <ComprasPage />}
          {rotaPermitida === 'fornecedores' && <FornecedoresPage />}
          {rotaPermitida === 'gdo' && <GdoPage />}
          {rotaPermitida === 'cum' && <CumPage />}
          {rotaPermitida === 'tri' && <TriPage />}
          {rotaPermitida === 'pat' && <PatPage />}
          {rotaPermitida === 'fro' && <FroPage />}
          {rotaPermitida === 'sau' && <SauPage />}
          {rotaPermitida === 'usuarios' && <IdnPage />}
        </main>
      </div>
    </div>
  );
}

export default Dashboard;
