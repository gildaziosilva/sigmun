import { useState } from 'react';
import type { ReactNode } from 'react';
import { ApiError } from '../lib/api';

interface DataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export function useApiData<T>(loader: () => Promise<T>): [DataState<T>, () => void] {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState('');

  function carregar() {
    setLoading(true);
    setErro('');
    loader()
      .then(setData)
      .catch((err: unknown) => {
        if (err instanceof ApiError && err.status === 401) {
          setErro('Sessão expirada. Entre novamente.');
        } else {
          setErro(err instanceof Error ? err.message : 'Falha ao carregar dados.');
        }
      })
      .finally(() => setLoading(false));
  }

  return [{ data, loading, erro }, carregar];
}

export function TabelaEstado(props: { loading: boolean; erro: string; vazio: boolean; children: ReactNode }) {
  if (props.loading) return <p className="muted">Carregando…</p>;
  if (props.erro)
    return (
      <p className="alert alert--error" role="alert">
        {props.erro}
      </p>
    );
  if (props.vazio) return <p className="muted">Nenhum registro encontrado.</p>;
  return <>{props.children}</>;
}
