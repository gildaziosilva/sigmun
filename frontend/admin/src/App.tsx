import { AuthProvider, useAuth } from './auth/AuthContext';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';

function Shell() {
  const { session, loading } = useAuth();
  if (loading) {
    return (
      <div className="login-page">
        <p className="muted">Carregando sessão…</p>
      </div>
    );
  }
  return session ? <Dashboard /> : <Login />;
}

function App() {
  return (
    <AuthProvider>
      <Shell />
    </AuthProvider>
  );
}

export default App;
