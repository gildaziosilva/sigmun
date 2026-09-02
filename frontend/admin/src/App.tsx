import { useState } from 'react'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'

export interface Session {
  nome: string
  email: string
  loginAt: string
}

const SESSION_KEY = 'sigmun_admin_session'

function readSession(): Session | null {
  const raw = window.localStorage.getItem(SESSION_KEY)
  if (!raw) return null
  try {
    return JSON.parse(raw) as Session
  } catch {
    return null
  }
}

function App() {
  const [session, setSession] = useState<Session | null>(() => readSession())

  function entrar(nome: string, email: string) {
    const nova: Session = { nome, email, loginAt: new Date().toISOString() }
    window.localStorage.setItem(SESSION_KEY, JSON.stringify(nova))
    setSession(nova)
  }

  function sair() {
    window.localStorage.removeItem(SESSION_KEY)
    setSession(null)
  }

  return session ? (
    <Dashboard session={session} onSair={sair} />
  ) : (
    <Login onEntrar={entrar} />
  )
}

export default App