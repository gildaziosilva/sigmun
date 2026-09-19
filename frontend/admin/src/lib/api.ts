/**
 * Cliente HTTP da API SIGMUN (frontend/admin).
 *
 * - Em dev, `VITE_API_URL` vazio => same-origin e o Vite faz proxy de
 *   `/api` e `/health` para o backend (ver `vite.config.ts`).
 * - Em produção, o `nginx.conf` repassa `/api` e `/health` ao backend,
 *   ou define-se `VITE_API_URL`.
 * - Auth real (VI.1): `POST /api/v1/idn/auth/login` retorna token opaco;
 *   guardado em `sessionStorage` e injetado como `Bearer` nas chamadas.
 */

export const API_BASE_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined) ?? '';

const TOKEN_KEY = 'sigmun_admin_token';

export function getToken(): string | null {
  return window.sessionStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string): void {
  window.sessionStorage.setItem(TOKEN_KEY, token);
}

export function clearToken(): void {
  window.sessionStorage.removeItem(TOKEN_KEY);
}

/** Erro HTTP tipado para exibição amigável nas telas. */
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

interface RequestOptions {
  method?: 'GET' | 'POST' | 'PATCH' | 'DELETE';
  body?: unknown;
  /** Não injeta Authorization (usado no login). */
  anonymous?: boolean;
}

async function request<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const headers: Record<string, string> = { Accept: 'application/json' };
  if (options.body !== undefined) headers['Content-Type'] = 'application/json';
  if (!options.anonymous) {
    const token = getToken();
    if (token) headers.Authorization = `Bearer ${token}`;
  }
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: options.method ?? 'GET',
    headers,
    body: options.body !== undefined ? JSON.stringify(options.body) : undefined,
  });
  if (response.status === 204) return undefined as T;
  let payload: unknown = null;
  try {
    payload = await response.json();
  } catch {
    payload = null;
  }
  if (!response.ok) {
    const detail =
      typeof payload === 'object' && payload !== null && 'detail' in payload
        ? String((payload as { detail: unknown }).detail)
        : `Falha ao acessar ${path} (HTTP ${response.status})`;
    throw new ApiError(response.status, detail);
  }
  return payload as T;
}

export const apiGet = <T>(path: string): Promise<T> => request<T>(path);
export const apiPost = <T>(path: string, body?: unknown, anonymous = false): Promise<T> =>
  request<T>(path, { method: 'POST', body, anonymous });

export interface HealthStatus {
  status: string;
  service: string;
  version: string;
  database?: string;
}

export interface LoginResponse {
  token: string;
  mensagem: string;
}

export interface Usuario {
  id: string;
  login: string;
  email: string;
  nome: string;
  status: string;
  unidades_ids: string[];
  roles_ids: string[];
  last_login?: string | null;
  created_at?: string;
}

export interface PageEnvelope<T> {
  total: number;
  page: number;
  page_size: number;
  items: T[];
}

export interface Compra {
  id: string;
  processo_documental_id: string;
  fornecedor_id: string;
  unidade_id: string;
  numero: string;
  data: string;
  valor_total?: string | number | null;
  situacao: string;
}

export interface Fornecedor {
  id: string;
  pessoa_juridica_id: string;
  situacao_cadastro: string;
  macro_categoria?: string | null;
}

export interface Contrato {
  id: string;
  numero?: string;
  [key: string]: unknown;
}

export interface DocumentoGDO {
  id: string;
  codigo: string;
  numero: string;
  ano: number;
  tipo_documental_id: string;
  titulo: string;
  unidade_autor_id: string;
  status: string;
  is_sigiloso: boolean;
}

export interface Pessoa {
  id: string;
  tipo: string;
  nome_identificacao?: string;
  unidade_id?: string | null;
}

/** Autentica (POST /api/v1/idn/auth/login). Chamada anônima. */
export async function login(login: string, senha: string): Promise<LoginResponse> {
  return apiPost<LoginResponse>('/api/v1/idn/auth/login', { login, senha }, true);
}

/** Encerra a sessão no backend (token via query, conforme contrato IDN). */
export async function logoutApi(token: string): Promise<void> {
  await request<{ mensagem: string }>(
    `/api/v1/idn/auth/logout?token=${encodeURIComponent(token)}`,
    { method: 'POST' },
  );
}

/** Localiza o usuário pelo login (enriquecimento p/ RBAC client-side). */
export async function fetchUsuarioPorLogin(login: string): Promise<Usuario | null> {
  const page = await apiGet<PageEnvelope<Usuario>>('/api/v1/idn/usuarios?page=0&page_size=200');
  return page.items.find((u) => u.login === login) ?? null;
}

export async function listarUsuarios(): Promise<PageEnvelope<Usuario>> {
  return apiGet<PageEnvelope<Usuario>>('/api/v1/idn/usuarios?page=0&page_size=50');
}

export async function listarCompras(): Promise<PageEnvelope<Compra>> {
  return apiGet<PageEnvelope<Compra>>('/api/v1/compras?page=0&page_size=50');
}

export async function obterCompra(id: string): Promise<Compra> {
  return apiGet<Compra>(`/api/v1/compras/${encodeURIComponent(id)}`);
}

export async function listarFornecedores(): Promise<PageEnvelope<Fornecedor>> {
  return apiGet<PageEnvelope<Fornecedor>>('/api/v1/fornecedores?page=0&page_size=50');
}

export async function listarContratos(): Promise<PageEnvelope<Contrato>> {
  return apiGet<PageEnvelope<Contrato>>('/api/v1/contratos?page=0&page_size=50');
}

export async function listarDocumentos(): Promise<PageEnvelope<DocumentoGDO>> {
  return apiGet<PageEnvelope<DocumentoGDO>>('/api/v1/gdo/documentos?page=0&page_size=50');
}

export async function obterDocumento(id: string): Promise<DocumentoGDO> {
  return apiGet<DocumentoGDO>(`/api/v1/gdo/documentos/${encodeURIComponent(id)}`);
}

export async function listarPessoas(): Promise<PageEnvelope<Pessoa>> {
  return apiGet<PageEnvelope<Pessoa>>('/api/v1/cadastro/pessoas?page=1&page_size=50');
}

/** Consulta o endpoint /health do backend. */
export async function fetchHealth(): Promise<HealthStatus> {
  return apiGet<HealthStatus>('/health');
}


