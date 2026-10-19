/** Cliente HTTP público do Portal do Cidadão (T-5.4: erro global + correlation_id). */

export const API_BASE_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined) ?? '';

export const CORRELATION_ID_HEADER = 'X-Correlation-ID';

/** Callback global para 401/403 (portais públicos apenas exibem aviso; sem redirect). */
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

  /** Mensagem amigável com correlation_id para erros 500 (T-5.4). */
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

async function postJson<T>(path: string, body: unknown): Promise<T> {
  const { data } = await requestJson<T>(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return data;
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

/* ------------------------------------------------------------------ */
/* T-5.1 — Ouvidoria pública (DOM-OUV, prefixo /api/v1/ouv).           */
/* Criação é anônima (ADR-0008 §2.2); acompanhamento usa o protocolo   */
/* devolvido no 201.                                                   */
/* ------------------------------------------------------------------ */

export type TipoManifestacao = 'sugestao' | 'elogio' | 'reclamacao' | 'solicitacao';
export type TipoDenuncia =
  | 'corrupcao'
  | 'improbidade'
  | 'assedio'
  | 'desvio_verba'
  | 'nepotismo'
  | 'fraude_licitacao'
  | 'outro';

export interface ProtocoloOuv {
  numero: string;
  ano: number;
}

export interface ManifestacaoOuv {
  id: string;
  protocolo: ProtocoloOuv | null;
  tipo: string;
  status: string;
  assunto: string;
  descricao: string;
  orgao_destino: string;
}

export interface ManifestacaoCreate {
  tipo: TipoManifestacao;
  assunto: string;
  descricao: string;
  cidadao_nome?: string;
  cidadao_email?: string;
  cidadao_telefone?: string;
  cidadao_anonimo?: boolean;
  orgao_destino: string;
}

export async function abrirManifestacao(payload: ManifestacaoCreate): Promise<ManifestacaoOuv> {
  return postJson<ManifestacaoOuv>('/api/v1/ouv/manifestacoes', {
    ...payload,
    canal: 'portal_cidadao',
  });
}

export interface DenunciaCreate {
  assunto: string;
  descricao: string;
  tipo_denuncia?: TipoDenuncia;
  local_fato: string;
  data_fato: string;
  cidadao_anonimo?: boolean;
  orgao_destino: string;
}

export interface DenunciaOuv {
  id: string;
  protocolo: ProtocoloOuv | null;
  status: string;
  assunto: string;
}

export async function abrirDenuncia(payload: DenunciaCreate): Promise<DenunciaOuv> {
  return postJson<DenunciaOuv>('/api/v1/ouv/denuncias', {
    ...payload,
    canal: 'portal_cidadao',
  });
}

export interface PedidoLaiCreate {
  assunto: string;
  descricao: string;
  informacao_solicitada: string;
  fundamentacao: string;
  formato_resposta?: 'digital' | 'fisico' | 'presencial';
  cidadao_nome: string;
  cidadao_email?: string;
  orgao_destino: string;
}

export interface PedidoLaiOuv {
  id: string;
  protocolo: ProtocoloOuv | null;
  status: string;
  assunto: string;
}

export async function abrirPedidoLai(payload: PedidoLaiCreate): Promise<PedidoLaiOuv> {
  return postJson<PedidoLaiOuv>('/api/v1/ouv/pedidos-lai', {
    ...payload,
    canal: 'portal_cidadao',
  });
}

export function formatProtocolo(p: ProtocoloOuv | null): string {
  if (!p) return 'protocolo pendente';
  return `${p.numero}/${p.ano}`;
}
