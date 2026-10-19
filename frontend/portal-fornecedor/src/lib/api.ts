/** Cliente HTTP público do Portal do Fornecedor (T-5.4: erro global + correlation_id). */

export const API_BASE_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined) ?? '';

export const CORRELATION_ID_HEADER = 'X-Correlation-ID';

let unauthorizedHandler: ((status: number) => void) | null = null;

export function onUnauthorized(handler: ((status: number) => void) | null): void {
  unauthorizedHandler = handler;
}

export class ApiError extends Error {
  status: number;
  detail: string;
  correlationId: string | null;
  constructor(status: number, detail: string, correlationId: string | null = null) {
    super(detail);
    this.name = 'ApiError';
    this.status = status;
    this.detail = detail;
    this.correlationId = correlationId;
  }

  get friendlyMessage(): string {
    if (this.status >= 500 && this.correlationId) {
      return `${this.detail} (protocolo de erro: ${this.correlationId})`;
    }
    return this.detail;
  }
}

/**
 * Extrai a mensagem de erro do envelope padronizado da API (T-3.2:
 * `{"error": {"message": ...}}`) com fallback para o `detail` do FastAPI e,
 * por fim, para uma mensagem genérica.
 */
export function extractErrorMessage(payload: unknown, path: string, status: number): string {
  if (typeof payload === 'object' && payload !== null) {
    const env = payload as { error?: { message?: unknown }; detail?: unknown };
    if (typeof env.error?.message === 'string' && env.error.message !== '') {
      return env.error.message;
    }
    if (env.detail !== undefined) {
      return String(env.detail);
    }
  }
  return `Falha ao acessar ${path} (HTTP ${status})`;
}

async function requestJson<T>(path: string, init?: RequestInit): Promise<{ data: T; correlationId: string | null }> {
  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: { Accept: 'application/json', ...(init?.headers ?? {}) },
  });
  const correlationId = res.headers.get(CORRELATION_ID_HEADER);
  let payload: unknown = null;
  try {
    payload = await res.json();
  } catch {
    payload = null;
  }
  if (res.status === 401 || res.status === 403) {
    unauthorizedHandler?.(res.status);
  }
  if (!res.ok) {
    throw new ApiError(
      res.status,
      extractErrorMessage(payload, path, res.status),
      correlationId,
    );
  }
  return { data: payload as T, correlationId };
}

async function getJson<T>(path: string): Promise<T> {
  const { data } = await requestJson<T>(path);
  return data;
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
  objeto?: string;
  valor_total?: string | number | null;
}

export interface ContratoPublico {
  id: string;
  numero?: string;
  objeto?: string;
  situacao?: string;
  valor?: string | number | null;
  [key: string]: unknown;
}

/** T-5.1: listagem paginada com filtro por situação (GET /api/v1/compras). */
export async function listarLicitacoes(
  page = 0,
  pageSize = 20,
  situacao?: string,
): Promise<PageEnvelope<LicitacaoPublica>> {
  const qs = new URLSearchParams({ page: String(page), page_size: String(pageSize) });
  if (situacao) qs.set('situacao', situacao);
  return getJson<PageEnvelope<LicitacaoPublica>>(`/api/v1/compras?${qs.toString()}`);
}

export async function obterLicitacao(id: string): Promise<LicitacaoPublica> {
  return getJson<LicitacaoPublica>(`/api/v1/compras/${encodeURIComponent(id)}`);
}

/** T-5.1: listagem paginada com filtro por situação (GET /api/v1/contratos). */
export async function listarContratos(
  page = 0,
  pageSize = 20,
  situacao?: string,
): Promise<PageEnvelope<ContratoPublico>> {
  const qs = new URLSearchParams({ page: String(page), page_size: String(pageSize) });
  if (situacao) qs.set('situacao', situacao);
  return getJson<PageEnvelope<ContratoPublico>>(`/api/v1/contratos?${qs.toString()}`);
}

export async function obterContrato(id: string): Promise<ContratoPublico> {
  return getJson<ContratoPublico>(`/api/v1/contratos/${encodeURIComponent(id)}`);
}
