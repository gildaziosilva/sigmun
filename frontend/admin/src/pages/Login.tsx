import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import { fetchHealth, type HealthStatus } from '../lib/api'

interface LoginProps {
  onEntrar: (nome: string, email: string) => void
}

function Login({ onEntrar }: LoginProps) {
  const [nome, setNome] = useState('')
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [erro, setErro] = useState('')

  const [saude, setSaude] = useState<HealthStatus | null>(null)
  const [saudeErro, setSaudeErro] = useState('')

  useEffect(() => {
    fetchHealth()
      .then(setSaude)
      .catch((err: unknown) => {
        setSaudeErro(err instanceof Error ? err.message : 'API indisponível')
      })
  }, [])

  function handleSubmit(event: FormEvent) {
    event.preventDefault()
    if (!nome.trim() || !email.trim() || !senha.trim()) {
      setErro('Preencha todos os campos para entrar.')
      return
    }
    setErro('')
    // TODO: integrar com POST /api/v1/auth/login quando o endpoint existir.
    onEntrar(nome.trim(), email.trim())
  }

  return (
    <div className="login-page">
      <main className="login-card">
        <header className="login-header">
          <div className="brand brand--center">
            <span className="brand-mark" aria-hidden="true">
              S
            </span>
            <div>
              <h1>SIGMUN</h1>
              <p>Sistema Integrado de Gestão Municipal</p>
            </div>
          </div>
        </header>

        <form className="form" onSubmit={handleSubmit} noValidate>
          <h2>Painel administrativo</h2>

          <label htmlFor="nome">
            Nome
            <input
              id="nome"
              type="text"
              autoComplete="name"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              placeholder="Nome do servidor"
            />
          </label>

          <label htmlFor="email">
            E-mail
            <input
              id="email"
              type="email"
              autoComplete="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="servidor@camacan.ba.gov.br"
            />
          </label>

          <label htmlFor="senha">
            Senha
            <input
              id="senha"
              type="password"
              autoComplete="current-password"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              placeholder="••••••••"
            />
          </label>

          {erro && (
            <p className="alert alert--error" role="alert">
              {erro}
            </p>
          )}

          <button type="submit" className="button button--primary">
            Entrar
          </button>
        </form>

        <footer className="login-status">
          <span className="status-dot" aria-hidden="true" />
          {saude ? (
            <p>
              API conectada — <strong>{saude.service}</strong> (v
              {saude.version})
            </p>
          ) : (
            <p>{saudeErro || 'Verificando conexão com a API…'}</p>
          )}
        </footer>
      </main>
    </div>
  )
}

export default Login