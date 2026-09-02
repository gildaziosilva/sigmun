import { useEffect, useState } from 'react'
import { fetchHealth, type HealthStatus } from '../lib/api'

interface Session {
  nome: string
  email: string
  loginAt: string
}

interface DashboardProps {
  session: Session
  onSair: () => void
}

const NAV_ITEMS = ['Painel', 'Módulos', 'Administração'] as const

/** Módulos de negócio do SIGMUN (placeholders até serem implementados). */
const MODULOS = [
  'Compras e Contratações',
  'Tributos',
  'Orçamento',
  'Patrimônio',
  'Saúde',
  'Educação',
]

function Dashboard({ session, onSair }: DashboardProps) {
  const [aba, setAba] = useState<(typeof NAV_ITEMS)[number]>('Painel')
  const [saude, setSaude] = useState<HealthStatus | null>(null)
  const [saudeErro, setSaudeErro] = useState('')

  useEffect(() => {
    fetchHealth()
      .then(setSaude)
      .catch((err: unknown) => {
        setSaudeErro(err instanceof Error ? err.message : 'API indisponível')
      })
  }, [])

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
          {NAV_ITEMS.map((item) => (
            <button
              key={item}
              type="button"
              className={item === aba ? 'active' : ''}
              aria-current={item === aba ? 'page' : undefined}
              onClick={() => setAba(item)}
            >
              {item}
            </button>
          ))}
        </nav>

        <button
          type="button"
          className="button button--ghost button--sair"
          onClick={onSair}
        >
          Sair
        </button>
      </aside>

      <div className="content">
        <header className="topbar">
          <div>
            <h1 className="topbar-title">{aba}</h1>
            <p className="topbar-subtitle">Bem-vindo(a), {session.nome}</p>
          </div>
          <span className="topbar-user" title={session.email}>
            {session.nome
              .split(' ')
              .slice(0, 2)
              .map((p) => p.charAt(0))
              .join('')
              .toUpperCase()}
          </span>
        </header>

        <main className="main">
          {aba === 'Painel' && (
            <section>
              <h2 className="section-title">Status do sistema</h2>
              <div
                className={`card status-card ${
                  saude ? 'status-card--ok' : 'status-card--error'
                }`}
              >
                <span className="status-dot" aria-hidden="true" />
                {saude ? (
                  <p>
                    Backend <strong>{saude.service}</strong> está{' '}
                    <strong>{saude.status}</strong> (versão {saude.version}).
                  </p>
                ) : (
                  <p>{saudeErro || 'Verificando API…'}</p>
                )}
              </div>
            </section>
          )}

          {aba === 'Módulos' && (
            <section>
              <h2 className="section-title">Módulos</h2>
              <div className="card-grid">
                {MODULOS.map((modulo) => (
                  <article key={modulo} className="card card--modulo">
                    <h3>{modulo}</h3>
                    <p>Em construção — em breve.</p>
                  </article>
                ))}
              </div>
            </section>
          )}

          {aba === 'Administração' && (
            <section>
              <h2 className="section-title">Administração</h2>
              <div className="card">
                <p>
                  Gestão de usuários, perfis e permissões sera implementada em
                  breve.
                </p>
              </div>
            </section>
          )}
        </main>
      </div>
    </div>
  )
}

export default Dashboard