/**
 * Cliente HTTP mínimo para a API do SIGMUN.
 *
 * Em desenvolvimento a base fica vazia (same-origin) e o Vite faz proxy
 * de `/api` e `/health` para o backend (ver `vite.config.ts`). Em produção,
 * o `nginx.conf` faz o mesmo repasse, ou pode-se definir `VITE_API_URL`.
 */

export const API_BASE_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined) ?? ''

export interface HealthStatus {
  status: string
  service: string
  version: string
}

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: { Accept: 'application/json' },
  })
  if (!response.ok) {
    throw new Error(`Falha ao acessar ${path} (HTTP ${response.status})`)
  }
  return (await response.json()) as T
}

/** Consulta o endpoint /health do backend. */
export async function fetchHealth(): Promise<HealthStatus> {
  return getJson<HealthStatus>('/health')
}