export const API_BASE_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined) ?? '';

export class ApiError extends Error {
  status: number;
  detail: string;
  constructor(status: number, detail: string) {
    super(detail);
    this.name = 'ApiError';
    this.status = status;
    this.detail = detail;
  }
}

async function getJson<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, { headers: { Accept: 'application/json' } });
  let payload: unknown = null;
  try {
    payload = await res.json();
  } catch {
    payload = null;
  }
  if (!res.ok) {
    const detail =
      typeof payload === 'object' && payload !== null && 'detail' in payload
        ? String((payload as { detail: unknown }).detail)
        : `Falha ao acessar ${path} (HTTP ${res.status})`;
    throw new ApiError(res.status, detail);
  }
  return payload as T;
}

export interface PageEnvelope<T> {
  total: number;
  page: number;
  page_size: number;
  items: T[];
}

export interface LicitacaoPublica {
  id: string;
  numero: string;
  situacao: string;
  data?: string;
  valor_total?: string | number | null;
}

export interface ContratoPublico {
  id: string;
  numero?: string;
  [key: string]: unknown;
}

export async function listarLicitacoes(): Promise<PageEnvelope<LicitacaoPublica>> {
  return getJson<PageEnvelope<LicitacaoPublica>>('/api/v1/compras?page=0&page_size=50');
}

export async function listarContratos(): Promise<PageEnvelope<ContratoPublico>> {
  return getJson<PageEnvelope<ContratoPublico>>('/api/v1/contratos?page=0&page_size=50');
}
