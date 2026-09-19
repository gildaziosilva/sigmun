import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import type { ReactNode } from 'react';
import {
  clearToken,
  fetchUsuarioPorLogin,
  getToken,
  login as apiLogin,
  logoutApi,
  setToken,
  type Usuario,
} from '../lib/api';

export interface Session {
  token: string;
  login: string;
  usuario: Usuario | null;
  loginAt: string;
}

/** Perfis conhecidos (derivados de roles_ids; heurística client-side). */
export type Perfil = 'admin' | 'servidor';

interface AuthContextValue {
  session: Session | null;
  perfil: Perfil | null;
  loading: boolean;
  entrar: (login: string, senha: string) => Promise<void>;
  sair: () => void;
  erro: string;
  limparErro: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

const SESSION_KEY = 'sigmun_admin_session';

function readStoredSession(): Session | null {
  try {
    const raw = window.sessionStorage.getItem(SESSION_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as Session;
    if (!parsed.token || !parsed.login) return null;
    return parsed;
  } catch {
    return null;
  }
}

function isAdmin(usuario: Usuario | null): boolean {
  if (!usuario) return false;
  return usuario.roles_ids.some((r) => /admin|gestor|gdo|compras/i.test(r));
}

/** Compatibilidade: sessões legadas (mock localStorage nome/email). */
function migrateLegacySession(): void {
  try {
    const raw = window.localStorage.getItem('sigmun_admin_session');
    if (raw) window.localStorage.removeItem('sigmun_admin_session');
  } catch {
    /* ignora */
  }
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [session, setSession] = useState<Session | null>(null);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState('');

  useEffect(() => {
    migrateLegacySession();
    const stored = readStoredSession();
    if (stored && getToken()) {
      setSession(stored);
    } else {
      clearToken();
      window.sessionStorage.removeItem(SESSION_KEY);
    }
    setLoading(false);
  }, []);

  const entrar = useCallback(async (login: string, senha: string) => {
    setErro('');
    try {
      const resp = await apiLogin(login.trim(), senha);
      setToken(resp.token);
      let usuario: Usuario | null = null;
      try {
        usuario = await fetchUsuarioPorLogin(login.trim());
      } catch {
        usuario = null;
      }
      const nova: Session = {
        token: resp.token,
        login: login.trim(),
        usuario,
        loginAt: new Date().toISOString(),
      };
      window.sessionStorage.setItem(SESSION_KEY, JSON.stringify(nova));
      setSession(nova);
    } catch (err) {
      clearToken();
      if (err instanceof Error) {
        setErro(err.message || 'Falha na autenticação.');
      } else {
        setErro('Falha na autenticação.');
      }
      throw err;
    }
  }, []);

  const sair = useCallback(() => {
    const token = session?.token ?? getToken();
    if (token) {
      logoutApi(token).catch(() => undefined);
    }
    clearToken();
    window.sessionStorage.removeItem(SESSION_KEY);
    setSession(null);
  }, [session]);

  const value = useMemo<AuthContextValue>(
    () => ({
      session,
      perfil: session ? (isAdmin(session.usuario) ? 'admin' : 'servidor') : null,
      loading,
      entrar,
      sair,
      erro,
      limparErro: () => setErro(''),
    }),
    [session, loading, entrar, sair, erro],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth deve ser usado dentro de <AuthProvider>');
  return ctx;
}

/** Guarda de rota por perfil (RBAC client-side; server-side pendente). */
export function temAcesso(perfil: Perfil | null, rota: string): boolean {
  if (!perfil) return false;
  if (perfil === 'admin') return true;
  // Servidor: sem acesso à gestão de usuários.
  if (rota === 'usuarios') return false;
  return true;
}
