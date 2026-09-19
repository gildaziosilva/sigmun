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

export interface DocumentoPublico {
  id: string;
  codigo: string;
  numero: string;
  ano: number;
  titulo: string;
  status: string;
  is_sigiloso?: boolean;
}

/** Consulta pública de protocolo/documento por código. */
export async function consultarProtocolo(codigo: string): Promise<DocumentoPublico[]> {
  const page = await getJson<PageEnvelope<DocumentoPublico>>(
    '/api/v1/gdo/documentos?page=0&page_size=200',
  );
  const alvo = codigo.trim().toLowerCase();
  return page.items.filter(
    (d) => d.is_sigiloso !== true && d.codigo.toLowerCase().includes(alvo),
  );
}

export interface HealthStatus {
  status: string;
  service: string;
  version: string;
}

export async function fetchHealth(): Promise<HealthStatus> {
  return getJson<HealthStatus>('/health');
}
