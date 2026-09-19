import { useEffect, useState } from 'react';
import type { FormEvent } from 'react';
import { useAuth } from '../auth/AuthContext';
import { fetchHealth, type HealthStatus } from '../lib/api';

function Login() {
  const { entrar, erro } = useAuth();
  const [login, setLogin] = useState('');
  const [senha, setSenha] = useState('');
  const [localErro, setLocalErro] = useState('');
  const [carregando, setCarregando] = useState(false);
  const [saude, setSaude] = useState<HealthStatus | null>(null);
  const [saudeErro, setSaudeErro] = useState('');

  useEffect(() => {
    fetchHealth()
      .then(setSaude)
      .catch((err: unknown) => {
        setSaudeErro(err instanceof Error ? err.message : 'API indisponível');
      });
  }, []);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!login.trim() || !senha.trim()) {
      setLocalErro('Preencha login e senha para entrar.');
      return;
    }
    setLocalErro('');
    setCarregando(true);
    try {
      await entrar(login, senha);
    } catch {
      /* erro já exposto via contexto */
    } finally {
      setCarregando(false);
    }
  }

  const mensagem = localErro || erro;

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

          <label htmlFor="login">
            Login
            <input
              id="login"
              type="text"
              autoComplete="username"
              value={login}
              onChange={(e) => setLogin(e.target.value)}
              placeholder="matricula ou usuário"
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

          {mensagem && (
            <p className="alert alert--error" role="alert">
              {mensagem}
            </p>
          )}

          <button type="submit" className="button button--primary" disabled={carregando}>
            {carregando ? 'Entrando…' : 'Entrar'}
          </button>
          <p className="form-hint">Autenticação via POST /api/v1/idn/auth/login.</p>
        </form>

        <footer className="login-status">
          <span className="status-dot" aria-hidden="true" />
          {saude ? (
            <p>
              API conectada — <strong>{saude.service}</strong> (v{saude.version})
              {saude.database ? ` · banco ${saude.database}` : ''}
            </p>
          ) : (
            <p>{saudeErro || 'Verificando conexão com a API…'}</p>
          )}
        </footer>
      </main>
    </div>
  );
}

export default Login;
