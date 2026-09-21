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


/* ------------------------------------------------------------------ */
/* DOM-DIA — Gestão de Diárias, Viagens e Deslocamentos                */
/* ------------------------------------------------------------------ */

export interface ViagemDia {
  id: string;
  servidor_id: string;
  dota_id: string;
  motivo: string;
  cargo_ocupado?: string | null;
  unidade_origem_id: string;
  unidade_destino_id: string;
  data_inicio?: string | null;
  data_fim?: string | null;
  destino: string;
  is_antecipacao: boolean;
  created_at: string;
  updated_at?: string | null;
  created_by?: string | null;
}

export interface DiariaDia {
  id: string;
  viagem_id: string;
  servidor_id: string;
  dota_id: string;
  categoria: string;
  descricao: string;
  data_inicio?: string | null;
  data_fim?: string | null;
  valor_diaria: number;
  valor_total: number;
  status: string;
  data_solicitacao?: string | null;
  data_autorizacao?: string | null;
  data_calculo?: string | null;
  data_concessao?: string | null;
  data_inicio_prestacao?: string | null;
  data_fim_prestacao?: string | null;
  data_pagamento?: string | null;
  data_aprovacao?: string | null;
  data_glosa?: string | null;
  data_restituicao?: string | null;
  data_cancelamento?: string | null;
  motivo_cancelamento?: string | null;
  motivo_glosa?: string | null;
  valor_glosado: number;
  documento_prestacao_id?: string | null;
  created_at: string;
  updated_at?: string | null;
  created_by?: string | null;
  updated_by?: string | null;
}

export interface PrestacaoContasDia {
  id: string;
  diaria_id: string;
  servidor_id: string;
  dota_id: string;
  data_emissao: string;
  data_vencimento?: string | null;
  documento_id: string;
  valor_previsto: number;
  valor_apresentado: number;
  valor_glosado: number;
  valor_liquido: number;
  status: string;
  motivo_glosa?: string | null;
  created_at: string;
  updated_at?: string | null;
  created_by?: string | null;
}

/* ------------------------------------------------------------------ */
/* DOM-TRI — Administração Tributária (GET /api/v1/tri/*)              */
/* ------------------------------------------------------------------ */

export interface ContribuinteTri {
  id: string;
  tipo: string;
  nome: string;
  cpf_cnpj: string;
  inscricao_municipal?: string | null;
  email?: string | null;
  telefone?: string | null;
  endereco?: string | null;
  status: string;
  created_at: string;
  updated_at?: string | null;
}

export interface ImovelTri {
  id: string;
  contribuinte_id: string;
  inscricao_imobiliaria: string;
  logradouro?: string | null;
  numero?: string | null;
  bairro?: string | null;
  cidade?: string | null;
  uf?: string | null;
  cep?: string | null;
  area_terreno: number;
  area_construida: number;
  valor_venal: number;
  aliquota: number;
  status: string;
  created_at: string;
}

export interface LancamentoTri {
  id: string;
  contribuinte_id: string;
  imovel_id?: string | null;
  tipo_tributo: string;
  exercicio: number;
  numero_lancamento: string;
  descricao?: string | null;
  base_calculo: number;
  aliquota: number;
  valor_tributo: number;
  juros: number;
  multa: number;
  valor_total: number;
  data_vencimento?: string | null;
  status: string;
  data_pagamento?: string | null;
  created_at: string;
}

export interface DividaAtivaTri {
  id: string;
  lancamento_id: string;
  numero_inscricao: string;
  data_inscricao?: string | null;
  valor_original: number;
  juros: number;
  multa: number;
  valor_atualizado: number;
  status: string;
  created_at: string;
}

export interface CertidaoTri {
  id: string;
  contribuinte_id: string;
  tipo: string;
  numero: string;
  data_emissao?: string | null;
  valido_ate?: string | null;
  observacao?: string | null;
  status: string;
  created_at: string;
}

/* ------------------------------------------------------------------ */
/* DOM-PAT — Gestão Patrimonial (GET /api/v1/pat/*)                    */
/* ------------------------------------------------------------------ */

export interface BemPat {
  id: string;
  codigo: string;
  tipo: string;
  descricao: string;
  categoria?: string | null;
  valor_aquisicao: number;
  data_aquisicao?: string | null;
  valor_residual: number;
  vida_util_anos: number;
  valor_contabil: number;
  status: string;
  localizacao?: string | null;
  responsavel_id?: string | null;
  created_at: string;
}

export interface DepreciacaoPat {
  id: string;
  bem_id: string;
  data?: string | null;
  valor_depreciado: number;
  valor_acumulado: number;
  valor_liquido: number;
  created_at: string;
}

/* ------------------------------------------------------------------ */
/* DOM-FRO — Gestão de Frota (GET /api/v1/fro/*)                       */
/* ------------------------------------------------------------------ */

export interface VeiculoFro {
  id: string;
  placa: string;
  chassi?: string | null;
  renavam?: string | null;
  marca: string;
  modelo: string;
  ano_fabricacao: number;
  ano_modelo: number;
  tipo: string;
  combustivel: string;
  capacidade: number;
  odometro_atual: number;
  status: string;
  unidade_id?: string | null;
  created_at: string;
}

export interface AbastecimentoFro {
  id: string;
  veiculo_id: string;
  data?: string | null;
  quantidade_litros: number;
  valor_unitario: number;
  valor_total: number;
  odometro: number;
  posto?: string | null;
  tipo_combustivel: string;
  created_at: string;
}

export interface ManutencaoFro {
  id: string;
  veiculo_id: string;
  data_entrada?: string | null;
  data_saida?: string | null;
  tipo: string;
  descricao: string;
  oficina?: string | null;
  valor: number;
  status: string;
  created_at: string;
}

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


/* ------------------------------------------------------------------ */
/* DOM-DIA — Consultas                                                 */
/* ------------------------------------------------------------------ */

export async function listarViagensPorServidor(
  servidorId: string,
): Promise<ViagemDia[]> {
  return apiGet<ViagemDia[]>(
    `/api/v1/dia/viagens/servidor/${encodeURIComponent(servidorId)}`,
  );
}

export async function listarDiariasPorServidor(
  servidorId: string,
): Promise<DiariaDia[]> {
  return apiGet<DiariaDia[]>(
    `/api/v1/dia/diarias/servidor/${encodeURIComponent(servidorId)}`,
  );
}

export async function listarDiariasPorStatus(
  status: string,
): Promise<DiariaDia[]> {
  return apiGet<DiariaDia[]>(
    `/api/v1/dia/diarias/status/${encodeURIComponent(status)}`,
  );
}

export async function listarPrestacoesAbertas(): Promise<PrestacaoContasDia[]> {
  return apiGet<PrestacaoContasDia[]>('/api/v1/dia/prestacoes/abertas');
}

/* ------------------------------------------------------------------ */
/* DOM-TRI — Administração Tributária                                  */
/* ------------------------------------------------------------------ */

export async function listarContribuintes(): Promise<ContribuinteTri[]> {
  return apiGet<ContribuinteTri[]>('/api/v1/tri/contribuintes');
}

export async function obterContribuinte(id: string): Promise<ContribuinteTri> {
  return apiGet<ContribuinteTri>(`/api/v1/tri/contribuintes/${encodeURIComponent(id)}`);
}

export async function listarImoveis(): Promise<ImovelTri[]> {
  return apiGet<ImovelTri[]>('/api/v1/tri/imoveis');
}

export async function obterImovel(id: string): Promise<ImovelTri> {
  return apiGet<ImovelTri>(`/api/v1/tri/imoveis/${encodeURIComponent(id)}`);
}

export async function listarLancamentos(): Promise<LancamentoTri[]> {
  return apiGet<LancamentoTri[]>('/api/v1/tri/lancamentos');
}

export async function obterLancamento(id: string): Promise<LancamentoTri> {
  return apiGet<LancamentoTri>(`/api/v1/tri/lancamentos/${encodeURIComponent(id)}`);
}

export async function pagarLancamento(id: string, dataPagamento?: string): Promise<LancamentoTri> {
  return apiPost<LancamentoTri>(
    `/api/v1/tri/lancamentos/${encodeURIComponent(id)}/pagar`,
    dataPagamento ? { data_pagamento: dataPagamento } : {},
  );
}

export async function listarDividaAtiva(): Promise<DividaAtivaTri[]> {
  return apiGet<DividaAtivaTri[]>('/api/v1/tri/divida-ativa');
}

export async function obterCertidao(id: string): Promise<CertidaoTri> {
  return apiGet<CertidaoTri>(`/api/v1/tri/certidoes/${encodeURIComponent(id)}`);
}

/* ------------------------------------------------------------------ */
/* DOM-PAT — Gestão Patrimonial                                        */
/* ------------------------------------------------------------------ */

export async function listarBens(): Promise<BemPat[]> {
  return apiGet<BemPat[]>('/api/v1/pat/bens');
}

export async function obterBem(id: string): Promise<BemPat> {
  return apiGet<BemPat>(`/api/v1/pat/bens/${encodeURIComponent(id)}`);
}

export async function listarDepreciacoes(bemId: string): Promise<DepreciacaoPat[]> {
  return apiGet<DepreciacaoPat[]>(
    `/api/v1/pat/bens/${encodeURIComponent(bemId)}/depreciacoes`,
  );
}

/* ------------------------------------------------------------------ */
/* DOM-FRO — Gestão de Frota                                           */
/* ------------------------------------------------------------------ */

export async function listarVeiculos(): Promise<VeiculoFro[]> {
  return apiGet<VeiculoFro[]>('/api/v1/fro/veiculos');
}

export async function obterVeiculo(id: string): Promise<VeiculoFro> {
  return apiGet<VeiculoFro>(`/api/v1/fro/veiculos/${encodeURIComponent(id)}`);
}

export async function listarAbastecimentos(): Promise<AbastecimentoFro[]> {
  return apiGet<AbastecimentoFro[]>('/api/v1/fro/abastecimentos');
}

export async function listarManutencoes(): Promise<ManutencaoFro[]> {
  return apiGet<ManutencaoFro[]>('/api/v1/fro/manutencoes');
}


