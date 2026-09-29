/**
 * Cliente HTTP da API SIGMUN (frontend/admin).
 *
 * - Em dev, `VITE_API_URL` vazio => same-origin e o Vite faz proxy de
 *   `/api` e `/health` para o backend (ver `vite.config.ts`).
 * - Em produção, o `nginx.conf` repassa `/api` e `/health` ao backend,
 *   ou define-se `VITE_API_URL`.
 * - Auth real (VI.1): `POST /api/v1/idn/auth/login` retorna token opaco;
 *   guardado em `sessionStorage` e injetado como `Bearer` nas chamadas.
 * - IDN (VI.2 — Esta iteração): operações de usuário,
 *   `POST /api/v1/idn/usuarios` (criar),
 *   `GET /api/v1/idn/usuarios` e `GET /api/v1/idn/usuarios/{id}` (listar e buscar),
 *   `POST .../usuarios/{id}/ativar|desativar|bloquear` (ciclo de vida).
 *   Não há endpoints HTTP de Role/Permissão, portanto o frontend não expõe
 *   criação/edição/attribuição de role/permissão.
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
export const apiPatch = <T>(path: string, body?: unknown): Promise<T> =>
  request<T>(path, { method: 'PATCH', body });
export const apiDelete = <T>(path: string): Promise<T> =>
  request<T>(path, { method: 'DELETE' });


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

/* ------------------------------------------------------------------ */
/* DOM-SAU — Saúde Municipal (GET/POST /api/v1/sau/*)                   */
/* ------------------------------------------------------------------ */

export interface PacienteSau {
  id: string;
  nome: string;
  cns: string;
  cpf?: string | null;
  data_nascimento?: string | null;
  sexo: string;
  nome_mae?: string | null;
  telefone?: string | null;
  endereco?: string | null;
  ubs_referencia?: string | null;
  status: string;
  created_at: string;
  updated_at?: string | null;
}

export interface PacienteSauCreate {
  nome: string;
  cns: string;
  cpf?: string;
  data_nascimento?: string;
  sexo?: string;
  nome_mae?: string;
  telefone?: string;
  endereco?: string;
  ubs_referencia?: string;
}

export interface AtendimentoSau {
  id: string;
  paciente_id: string;
  data?: string | null;
  tipo: string;
  profissional: string;
  estabelecimento: string;
  queixa?: string | null;
  conduta?: string | null;
  cid10?: string | null;
  created_at: string;
}

export interface AtendimentoSauCreate {
  paciente_id: string;
  profissional: string;
  estabelecimento: string;
  tipo?: string;
  data?: string;
  queixa?: string;
  conduta?: string;
  cid10?: string;
}

export interface AgendamentoSau {
  id: string;
  paciente_id: string;
  especialidade: string;
  data?: string | null;
  hora?: string | null;
  estabelecimento?: string | null;
  status: string;
  created_at: string;
}

export interface AgendamentoSauCreate {
  paciente_id: string;
  especialidade: string;
  data?: string;
  hora?: string;
  estabelecimento?: string;
}

export interface RegulacaoSau {
  id: string;
  paciente_id: string;
  procedimento: string;
  prioridade: string;
  solicitante?: string | null;
  data_solicitacao?: string | null;
  status: string;
  justificativa?: string | null;
  created_at: string;
}

export interface RegulacaoSauCreate {
  paciente_id: string;
  procedimento: string;
  prioridade?: string;
  solicitante?: string;
}

export interface MedicamentoSau {
  id: string;
  nome: string;
  apresentacao?: string | null;
  estoque: number;
  estoque_minimo: number;
  created_at: string;
}

export interface MedicamentoSauCreate {
  nome: string;
  apresentacao?: string;
  estoque?: number;
  estoque_minimo?: number;
}

export interface DispensacaoSau {
  id: string;
  paciente_id: string;
  medicamento_id: string;
  quantidade: number;
  data?: string | null;
  receita?: string | null;
  created_at: string;
}

export interface DispensacaoSauCreate {
  paciente_id: string;
  medicamento_id: string;
  quantidade: number;
  receita?: string;
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
  descricao?: string | null;
  data_criacao?: string | null;
  data_recebimento?: string | null;
  data_arquivamento?: string | null;
  data_encerramento?: string | null;
  data_eliminacao?: string | null;
  unidade_autor_id: string;
  unidade_arquivo_id?: string | null;
  processo_id?: string | null;
  status: string;
  is_sigiloso: boolean;
  conteudo_ref?: string | null;
  hash_integridade?: string | null;
  created_at: string;
  created_by?: string | null;
  updated_at?: string | null;
  updated_by?: string | null;
  deleted_at?: string | null;
  deleted_by?: string | null;
}

export interface DocumentoCreateRequest {
  codigo: string;
  numero: string;
  ano: number;
  tipo_documental_id: string;
  titulo: string;
  descricao?: string;
  unidade_autor_id: string;
  unidade_arquivo_id?: string;
  processo_id?: string;
  is_sigiloso?: boolean;
  conteudo_ref?: string;
  hash_integridade?: string;
}

export interface DocumentoUpdateRequest {
  titulo?: string;
  descricao?: string;
  unidade_arquivo_id?: string;
  processo_id?: string;
  status?: string;
  is_sigiloso?: boolean;
  conteudo_ref?: string;
  hash_integridade?: string;
}

export interface TramitacaoGDO {
  id: string;
  documento_id: string;
  unidade_origem_id: string;
  unidade_destino_id: string;
  tipo: string;
  data_envio?: string | null;
  data_recebimento?: string | null;
  data_devolucao?: string | null;
  motivo?: string | null;
  observacao?: string | null;
  created_at: string;
  created_by?: string | null;
}

export interface TramitacaoCreateRequest {
  unidade_origem_id: string;
  unidade_destino_id: string;
  tipo: 'envio' | 'recebimento' | 'devolucao';
  motivo?: string;
  observacao?: string;
}

export interface VersaoDocumentoGDO {
  id: string;
  documento_id: string;
  numero_versao: number;
  conteudo_ref?: string | null;
  hash_integridade?: string | null;
  data_versao: string;
  created_by?: string | null;
  deleted_at?: string | null;
  deleted_by?: string | null;
}

export interface VersaoCreateRequest {
  documento_id: string;
  numero_versao: number;
  conteudo_ref?: string;
  hash_integridade?: string;
}

export interface ArquivamentoGDO {
  id: string;
  documento_id: string;
  unidade_arquivo_id: string;
  autor_id: string;
  observacao?: string | null;
  data_arquivamento: string;
  created_at: string;
}

export interface ArquivamentoCreateRequest {
  unidade_arquivo_id: string;
  autor_id: string;
  observacao?: string;
}

export interface AssinaturaGDO {
  id: string;
  documento_id: string;
  signatario_id: string;
  data_assinatura: string;
  hash_assinatura: string;
  certificado_id?: string | null;
  is_valida: boolean;
  is_revogada: boolean;
  created_at: string;
}

export interface AssinaturaCreateRequest {
  signatario_id: string;
  conteudo: string;
  autor_id: string;
  certificado_id?: string;
}

export interface TipoDocumentalGDO {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  is_ativo: boolean;
  created_at: string;
  created_by?: string | null;
  updated_at?: string | null;
  updated_by?: string | null;
  deleted_at?: string | null;
  deleted_by?: string | null;
}

export interface TipoDocumentalCreateRequest {
  codigo: string;
  nome: string;
  descricao?: string;
}

export interface ClassificacaoDocumentalGDO {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  nivel: number;
  classificacao_pai_id?: string | null;
  prazo_retencao: number;
  unidade_destino_id?: string | null;
  created_at: string;
  created_by?: string | null;
  updated_at?: string | null;
  updated_by?: string | null;
  deleted_at?: string | null;
  deleted_by?: string | null;
  is_active: boolean;
}

export interface ClassificacaoCreateRequest {
  codigo: string;
  nome: string;
  descricao?: string;
  nivel?: number;
  classificacao_pai_id?: string;
  prazo_retencao?: number;
  unidade_destino_id?: string;
}

export interface ProcessoDocumentoGDO {
  id: string;
  numero: string;
  ano: number;
  tipo_processo_id: string;
  titulo: string;
  descricao?: string | null;
  unidade_autor_id: string;
  data_abertura: string;
  data_encerramento?: string | null;
  status: string;
  created_at: string;
  is_active: boolean;
}

export interface TabelaTemporalidadeGDO {
  id: string;
  codigo: string;
  nome: string;
  prazo_tempo: number;
  unidade_tempo: string;
  evento_fim: string;
  tipo_destinacao: string;
  is_ativo: boolean;
  created_at: string;
}

export interface DestinacaoRequest {
  tipo_destinacao: 'eliminacao' | 'guarda_permanente';
  autor_id: string;
  autoridade_homologadora_id?: string;
  justificativa?: string;
}

export interface Pessoa {
  id: string;
  tipo: string;
  nome_identificacao?: string;
  unidade_id?: string | null;
}

/* ------------------------------------------------------------------ */
/* DOM-IDN — Identidade e Acesso                                       */
/* ------------------------------------------------------------------ */

export interface UsuarioCreatePayload {
  login: string;
  email: string;
  nome: string;
  senha: string;
  unidades_ids?: string[];
  roles_ids?: string[];
}

export async function criarUsuario(payload: UsuarioCreatePayload): Promise<Usuario> {
  return apiPost<Usuario>('/api/v1/idn/usuarios', payload);
}

export async function obterUsuario(id: string): Promise<Usuario> {
  return apiGet<Usuario>(`/api/v1/idn/usuarios/${encodeURIComponent(id)}`);
}

export async function ativarUsuario(id: string): Promise<Usuario> {
  return apiPost<Usuario>(`/api/v1/idn/usuarios/${encodeURIComponent(id)}/ativar`);
}

export async function desativarUsuario(id: string): Promise<Usuario> {
  return apiPost<Usuario>(`/api/v1/idn/usuarios/${encodeURIComponent(id)}/desativar`);
}

export async function bloquearUsuario(id: string): Promise<Usuario> {
  return apiPost<Usuario>(`/api/v1/idn/usuarios/${encodeURIComponent(id)}/bloquear`);
}

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

export async function criarDocumento(payload: DocumentoCreateRequest): Promise<DocumentoGDO> {
  return apiPost<DocumentoGDO>('/api/v1/gdo/documentos', payload);
}

export async function listarDocumentosPorProcesso(processoId: string): Promise<DocumentoGDO[]> {
  return apiGet<DocumentoGDO[]>(`/api/v1/gdo/documentos/processo/${encodeURIComponent(processoId)}`);
}

export async function tramitarDocumento(documentoId: string, payload: TramitacaoCreateRequest): Promise<TramitacaoGDO> {
  return apiPost<TramitacaoGDO>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/tramitar`, payload);
}

export async function listarTramitacoes(documentoId: string): Promise<TramitacaoGDO[]> {
  return apiGet<TramitacaoGDO[]>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/tramitacoes`);
}

export async function listarVersoes(documentoId: string): Promise<VersaoDocumentoGDO[]> {
  return apiGet<VersaoDocumentoGDO[]>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/versoes`);
}

export async function criarVersao(payload: VersaoCreateRequest): Promise<VersaoDocumentoGDO> {
  return apiPost<VersaoDocumentoGDO>('/api/v1/gdo/versoes', payload);
}

export async function arquivarDocumento(documentoId: string, payload: ArquivamentoCreateRequest): Promise<ArquivamentoGDO> {
  return apiPost<ArquivamentoGDO>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/arquivar`, payload);
}

export async function assinarDocumento(documentoId: string, payload: AssinaturaCreateRequest): Promise<AssinaturaGDO> {
  return apiPost<AssinaturaGDO>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/assinar`, payload);
}

export async function listarAssinaturas(documentoId: string): Promise<AssinaturaGDO[]> {
  return apiGet<AssinaturaGDO[]>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/assinaturas`);
}

export async function aplicarDestinacao(documentoId: string, payload: DestinacaoRequest): Promise<DocumentoGDO> {
  return apiPost<DocumentoGDO>(`/api/v1/gdo/documentos/${encodeURIComponent(documentoId)}/destinacao`, payload);
}

export async function listarTiposDocumentais(): Promise<TipoDocumentalGDO[]> {
  return apiGet<TipoDocumentalGDO[]>('/api/v1/gdo/tipos-documentais');
}

export async function criarTipoDocumental(payload: TipoDocumentalCreateRequest): Promise<TipoDocumentalGDO> {
  return apiPost<TipoDocumentalGDO>('/api/v1/gdo/tipos-documentais', payload);
}

export async function ativarTipoDocumental(id: string): Promise<void> {
  return apiPost<void>(`/api/v1/gdo/tipos-documentais/${encodeURIComponent(id)}/ativar`, {});
}

export async function inativarTipoDocumental(id: string): Promise<void> {
  return apiPost<void>(`/api/v1/gdo/tipos-documentais/${encodeURIComponent(id)}/inativar`, {});
}

export async function listarClassificacoes(): Promise<PageEnvelope<ClassificacaoDocumentalGDO>> {
  return apiGet<PageEnvelope<ClassificacaoDocumentalGDO>>('/api/v1/gdo/classificacoes?page=0&page_size=50');
}

export async function obterClassificacao(id: string): Promise<ClassificacaoDocumentalGDO> {
  return apiGet<ClassificacaoDocumentalGDO>(`/api/v1/gdo/classificacoes/${encodeURIComponent(id)}`);
}

export async function obterProcesso(processoId: string): Promise<ProcessoDocumentoGDO> {
  return apiGet<ProcessoDocumentoGDO>(`/api/v1/gdo/processos/${encodeURIComponent(processoId)}`);
}

export async function obterTemporalidade(codigo: string): Promise<TabelaTemporalidadeGDO> {
  return apiGet<TabelaTemporalidadeGDO>(`/api/v1/gdo/temporalidades/${encodeURIComponent(codigo)}`);
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

/* ------------------------------------------------------------------ */
/* DOM-SAU — Saúde Municipal                                           */
/* ------------------------------------------------------------------ */

export async function listarPacientesSau(): Promise<PacienteSau[]> {
  return apiGet<PacienteSau[]>('/api/v1/sau/pacientes');
}

export async function obterPacienteSau(id: string): Promise<PacienteSau> {
  return apiGet<PacienteSau>(`/api/v1/sau/pacientes/${encodeURIComponent(id)}`);
}

export async function criarPacienteSau(payload: PacienteSauCreate): Promise<PacienteSau> {
  return apiPost<PacienteSau>('/api/v1/sau/pacientes', payload);
}

export async function obterProntuarioSau(pacienteId: string): Promise<AtendimentoSau[]> {
  return apiGet<AtendimentoSau[]>(`/api/v1/sau/pacientes/${encodeURIComponent(pacienteId)}/prontuario`);
}

export async function registrarAtendimentoSau(payload: AtendimentoSauCreate): Promise<AtendimentoSau> {
  return apiPost<AtendimentoSau>('/api/v1/sau/atendimentos', payload);
}

export async function listarAgendamentosSau(): Promise<AgendamentoSau[]> {
  return apiGet<AgendamentoSau[]>('/api/v1/sau/agendamentos');
}

export async function agendarConsultaSau(payload: AgendamentoSauCreate): Promise<AgendamentoSau> {
  return apiPost<AgendamentoSau>('/api/v1/sau/agendamentos', payload);
}

export async function confirmarAgendamentoSau(id: string): Promise<AgendamentoSau> {
  return apiPost<AgendamentoSau>(`/api/v1/sau/agendamentos/${encodeURIComponent(id)}/confirmar`, {});
}

export async function cancelarAgendamentoSau(id: string, motivo?: string): Promise<AgendamentoSau> {
  const qs = motivo ? `?motivo=${encodeURIComponent(motivo)}` : '';
  return apiPost<AgendamentoSau>(`/api/v1/sau/agendamentos/${encodeURIComponent(id)}/cancelar${qs}`, {});
}

export async function realizarAgendamentoSau(id: string): Promise<AgendamentoSau> {
  return apiPost<AgendamentoSau>(`/api/v1/sau/agendamentos/${encodeURIComponent(id)}/realizar`, {});
}

export async function listarRegulacoesSau(): Promise<RegulacaoSau[]> {
  return apiGet<RegulacaoSau[]>('/api/v1/sau/regulacoes');
}

export async function solicitarRegulacaoSau(payload: RegulacaoSauCreate): Promise<RegulacaoSau> {
  return apiPost<RegulacaoSau>('/api/v1/sau/regulacoes', payload);
}

export async function autorizarRegulacaoSau(id: string): Promise<RegulacaoSau> {
  return apiPost<RegulacaoSau>(`/api/v1/sau/regulacoes/${encodeURIComponent(id)}/autorizar`, {});
}

export async function negarRegulacaoSau(id: string, justificativa?: string): Promise<RegulacaoSau> {
  const qs = justificativa ? `?justificativa=${encodeURIComponent(justificativa)}` : '';
  return apiPost<RegulacaoSau>(`/api/v1/sau/regulacoes/${encodeURIComponent(id)}/negar${qs}`, {});
}

export async function listarMedicamentosSau(): Promise<MedicamentoSau[]> {
  return apiGet<MedicamentoSau[]>('/api/v1/sau/medicamentos');
}

export async function criarMedicamentoSau(payload: MedicamentoSauCreate): Promise<MedicamentoSau> {
  return apiPost<MedicamentoSau>('/api/v1/sau/medicamentos', payload);
}

export async function reporEstoqueSau(id: string, quantidade: number): Promise<MedicamentoSau> {
  return apiPost<MedicamentoSau>(
    `/api/v1/sau/medicamentos/${encodeURIComponent(id)}/repor?quantidade=${encodeURIComponent(String(quantidade))}`,
    {},
  );
}

export async function dispensarMedicamentoSau(payload: DispensacaoSauCreate): Promise<DispensacaoSau> {
  return apiPost<DispensacaoSau>('/api/v1/sau/dispensacoes', payload);
}


/* ------------------------------------------------------------------ */
/* DOM-EDU — Educação Municipal                                        */
/* ------------------------------------------------------------------ */

// Aluno
export interface AlunoEdu {
  id: string;
  nome: string;
  cpf: string | null;
  data_nascimento: string | null;
  sexo: string;
  nome_mae: string | null;
  telefone: string | null;
  endereco: string | null;
  status: string;
  created_at: string;
  updated_at: string | null;
}

export interface AlunoCreateRequest {
  nome: string;
  cpf?: string;
  data_nascimento?: string;
  sexo?: 'masculino' | 'feminino' | 'ignorado';
  nome_mae?: string;
  telefone?: string;
  endereco?: string;
  created_by: string;
}

export interface AlunoUpdateRequest {
  nome?: string;
  cpf?: string;
  data_nascimento?: string;
  sexo?: 'masculino' | 'feminino' | 'ignorado';
  nome_mae?: string;
  telefone?: string;
  endereco?: string;
  created_by: string;
}

export async function listarAlunos(): Promise<AlunoEdu[]> {
  return apiGet<AlunoEdu[]>('/api/v1/edu/alunos');
}

export async function obterAluno(id: string): Promise<AlunoEdu> {
  return apiGet<AlunoEdu>(`/api/v1/edu/alunos/${encodeURIComponent(id)}`);
}

export async function criarAluno(payload: AlunoCreateRequest): Promise<AlunoEdu> {
  return apiPost<AlunoEdu>('/api/v1/edu/alunos', payload);
}

export async function atualizarAluno(id: string, payload: AlunoUpdateRequest): Promise<AlunoEdu> {
  return apiPost<AlunoEdu>(`/api/v1/edu/alunos/${encodeURIComponent(id)}`, payload, false);
}

export async function inativarAluno(id: string, created_by: string): Promise<AlunoEdu> {
  return apiPost<AlunoEdu>(`/api/v1/edu/alunos/${encodeURIComponent(id)}/inativar`, { created_by });
}

export async function ativarAluno(id: string, created_by: string): Promise<AlunoEdu> {
  return apiPost<AlunoEdu>(`/api/v1/edu/alunos/${encodeURIComponent(id)}/ativar`, { created_by });
}


// Matrícula
export interface MatriculaEdu {
  id: string;
  aluno_id: string;
  escola: string;
  serie: string;
  turno: string;
  ano_letivo: number;
  data_matricula: string | null;
  status: string;
  escola_destino: string | null;
  motivo: string | null;
  created_at: string;
}

export interface MatriculaCreateRequest {
  aluno_id: string;
  escola: string;
  serie: string;
  turno: 'manha' | 'tarde' | 'noite';
  ano_letivo: number;
  created_by: string;
}

export interface MatriculaTransferRequest {
  escola_destino: string;
  motivo?: string;
  created_by: string;
}

export interface MatriculaCancelRequest {
  motivo?: string;
  created_by: string;
}

export async function listarMatriculas(): Promise<MatriculaEdu[]> {
  return apiGet<MatriculaEdu[]>('/api/v1/edu/matriculas');
}

export async function obterMatricula(id: string): Promise<MatriculaEdu> {
  return apiGet<MatriculaEdu>(`/api/v1/edu/matriculas/${encodeURIComponent(id)}`);
}

export async function criarMatricula(payload: MatriculaCreateRequest): Promise<MatriculaEdu> {
  return apiPost<MatriculaEdu>('/api/v1/edu/matriculas', payload);
}

export async function transferirMatricula(id: string, payload: MatriculaTransferRequest): Promise<MatriculaEdu> {
  return apiPost<MatriculaEdu>(`/api/v1/edu/matriculas/${encodeURIComponent(id)}/transferir`, payload);
}

export async function cancelarMatricula(id: string, payload: MatriculaCancelRequest): Promise<MatriculaEdu> {
  return apiPost<MatriculaEdu>(`/api/v1/edu/matriculas/${encodeURIComponent(id)}/cancelar`, payload);
}

export async function concluirMatricula(id: string, created_by: string): Promise<MatriculaEdu> {
  return apiPost<MatriculaEdu>(`/api/v1/edu/matriculas/${encodeURIComponent(id)}/concluir`, { created_by });
}


// Diário de Classe
export interface LancamentoDiarioEdu {
  id: string;
  matricula_id: string;
  data: string | null;
  presente: boolean;
  nota: number | null;
  observacao: string | null;
  created_at: string;
}

export interface LancamentoDiarioCreateRequest {
  matricula_id: string;
  data?: string;
  presente: boolean;
  nota?: number;
  observacao?: string;
  created_by: string;
}

export async function listarLancamentosDiario(): Promise<LancamentoDiarioEdu[]> {
  return apiGet<LancamentoDiarioEdu[]>('/api/v1/edu/diario/lancamentos');
}

export async function listarLancamentosPorMatricula(matricula_id: string): Promise<LancamentoDiarioEdu[]> {
  return apiGet<LancamentoDiarioEdu[]>(`/api/v1/edu/diario/lancamentos?matricula_id=${encodeURIComponent(matricula_id)}`);
}

export async function criarLancamentoDiario(payload: LancamentoDiarioCreateRequest): Promise<LancamentoDiarioEdu> {
  return apiPost<LancamentoDiarioEdu>('/api/v1/edu/diario/lancamentos', payload);
}


// Transporte Escolar
export interface RotaTransporteEdu {
  id: string;
  identificacao: string;
  veiculo: string | null;
  motorista: string;
  vagas: number;
  turno: string;
  status: string;
  created_at: string;
}

export interface RotaTransporteCreateRequest {
  identificacao: string;
  motorista: string;
  veiculo?: string;
  vagas: number;
  turno?: 'manha' | 'tarde' | 'noite';
  created_by: string;
}

export interface RotaTransporteUpdateRequest {
  identificacao?: string;
  veiculo?: string;
  motorista?: string;
  vagas?: number;
  turno?: 'manha' | 'tarde' | 'noite';
  created_by: string;
}

export interface PassagemTransporteEdu {
  id: string;
  rota_id: string;
  matricula_id: string;
  data: string | null;
  created_at: string;
}

export interface PassagemTransporteCreateRequest {
  rota_id: string;
  matricula_id: string;
  data?: string;
  created_by: string;
}

export async function listarRotasTransporte(): Promise<RotaTransporteEdu[]> {
  return apiGet<RotaTransporteEdu[]>('/api/v1/edu/transporte/rotas');
}

export async function obterRotaTransporte(id: string): Promise<RotaTransporteEdu> {
  return apiGet<RotaTransporteEdu>(`/api/v1/edu/transporte/rotas/${encodeURIComponent(id)}`);
}

export async function criarRotaTransporte(payload: RotaTransporteCreateRequest): Promise<RotaTransporteEdu> {
  return apiPost<RotaTransporteEdu>('/api/v1/edu/transporte/rotas', payload);
}

export async function atualizarRotaTransporte(id: string, payload: RotaTransporteUpdateRequest): Promise<RotaTransporteEdu> {
  return apiPost<RotaTransporteEdu>(`/api/v1/edu/transporte/rotas/${encodeURIComponent(id)}`, payload, false);
}

export async function inativarRotaTransporte(id: string, created_by: string): Promise<RotaTransporteEdu> {
  return apiPost<RotaTransporteEdu>(`/api/v1/edu/transporte/rotas/${encodeURIComponent(id)}/inativar`, { created_by });
}

export async function ativarRotaTransporte(id: string, created_by: string): Promise<RotaTransporteEdu> {
  return apiPost<RotaTransporteEdu>(`/api/v1/edu/transporte/rotas/${encodeURIComponent(id)}/ativar`, { created_by });
}

export async function listarPassagensTransporte(rota_id?: string): Promise<PassagemTransporteEdu[]> {
  const qs = rota_id ? `?rota_id=${encodeURIComponent(rota_id)}` : '';
  return apiGet<PassagemTransporteEdu[]>(`/api/v1/edu/transporte/passagens${qs}`);
}

export async function registrarPassagemTransporte(payload: PassagemTransporteCreateRequest): Promise<PassagemTransporteEdu> {
  return apiPost<PassagemTransporteEdu>('/api/v1/edu/transporte/passagens', payload);
}


// Merenda Escolar
export interface ItemMerendaEdu {
  id: string;
  nome: string;
  tipo: string;
  estoque: number;
  estoque_minimo: number;
  created_at: string;
}

export interface ItemMerendaCreateRequest {
  nome: string;
  tipo?: string;
  estoque?: number;
  estoque_minimo?: number;
  created_by: string;
}

export interface ItemMerendaUpdateRequest {
  nome?: string;
  tipo?: string;
  estoque_minimo?: number;
  created_by: string;
}

export interface DistribuicaoMerendaEdu {
  id: string;
  matricula_id: string;
  item_id: string;
  quantidade: number;
  data: string | null;
  refeicao: string;
  created_at: string;
}

export interface DistribuicaoMerendaCreateRequest {
  matricula_id: string;
  item_id: string;
  quantidade: number;
  refeicao?: 'almoco' | 'lanche' | 'jantar';
  data?: string;
  created_by: string;
}

export async function listarItensMerenda(): Promise<ItemMerendaEdu[]> {
  return apiGet<ItemMerendaEdu[]>('/api/v1/edu/merenda/itens');
}

export async function obterItemMerenda(id: string): Promise<ItemMerendaEdu> {
  return apiGet<ItemMerendaEdu>(`/api/v1/edu/merenda/itens/${encodeURIComponent(id)}`);
}

export async function criarItemMerenda(payload: ItemMerendaCreateRequest): Promise<ItemMerendaEdu> {
  return apiPost<ItemMerendaEdu>('/api/v1/edu/merenda/itens', payload);
}

export async function atualizarItemMerenda(id: string, payload: ItemMerendaUpdateRequest): Promise<ItemMerendaEdu> {
  return apiPost<ItemMerendaEdu>(`/api/v1/edu/merenda/itens/${encodeURIComponent(id)}`, payload, false);
}

export async function reporEstoqueMerenda(id: string, quantidade: number): Promise<ItemMerendaEdu> {
  return apiPost<ItemMerendaEdu>(`/api/v1/edu/merenda/itens/${encodeURIComponent(id)}/repor?quantidade=${encodeURIComponent(String(quantidade))}`, {});
}

export async function listarDistribuicoesMerenda(matricula_id?: string): Promise<DistribuicaoMerendaEdu[]> {
  const qs = matricula_id ? `?matricula_id=${encodeURIComponent(matricula_id)}` : '';
  return apiGet<DistribuicaoMerendaEdu[]>(`/api/v1/edu/merenda/distribuicoes${qs}`);
}

export async function distribuirMerenda(payload: DistribuicaoMerendaCreateRequest): Promise<DistribuicaoMerendaEdu> {
  return apiPost<DistribuicaoMerendaEdu>('/api/v1/edu/merenda/distribuicoes', payload);
}

/* ------------------------------------------------------------------ */
/* DOM-ASS — Assistência Social                                        */
/* ------------------------------------------------------------------ */

export interface FamiliaAss {
  id: string;
  nis: string;
  responsavel_nome: string;
  responsavel_cpf?: string | null;
  endereco?: string | null;
  telefone?: string | null;
  renda_per_capita: number;
  quantidade_pessoas: number;
  status: string;
  created_at: string;
  updated_at?: string | null;
}

export interface FamiliaAssCreate {
  nis: string;
  responsavel_nome: string;
  responsavel_cpf?: string;
  endereco?: string;
  telefone?: string;
  renda_per_capita?: number;
  quantidade_pessoas?: number;
}

export interface PessoaAss {
  id: string;
  familia_id: string;
  nome: string;
  cpf: string;
  data_nascimento?: string | null;
  sexo: string;
  nome_mae?: string | null;
  parentesco?: string | null;
  escolaridade?: string | null;
  ocupacao?: string | null;
  renda: number;
  created_at: string;
  updated_at?: string | null;
}

export interface PessoaAssCreate {
  familia_id: string;
  nome: string;
  cpf: string;
  data_nascimento?: string;
  sexo?: string;
  nome_mae?: string;
  parentesco?: string;
  escolaridade?: string;
  ocupacao?: string;
  renda?: number;
}

export interface UnidadeAss {
  id: string;
  codigo: string;
  nome: string;
  tipo: string;
  endereco?: string | null;
  telefone?: string | null;
  email?: string | null;
  responsavel?: string | null;
  status: string;
  created_at: string;
  updated_at?: string | null;
}

export interface UnidadeAssCreate {
  codigo: string;
  nome: string;
  tipo?: string;
  endereco?: string;
  telefone?: string;
  email?: string;
  responsavel?: string;
}

export interface BeneficioAss {
  id: string;
  familia_id: string;
  tipo: string;
  descricao?: string | null;
  valor: number;
  quantidade: number;
  data_solicitacao: string;
  data_aprovacao?: string | null;
  data_entrega?: string | null;
  status: string;
  unidade_id?: string | null;
  observacao?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface BeneficioAssCreate {
  familia_id: string;
  tipo?: string;
  descricao?: string;
  valor?: number;
  quantidade?: number;
  unidade_id?: string;
  observacao?: string;
}

export interface AtendimentoAss {
  id: string;
  pessoa_id: string;
  unidade_id: string;
  tipo: string;
  data?: string | null;
  descricao?: string | null;
  encaminhamento?: string | null;
  profissional: string;
  created_at: string;
}

export interface AtendimentoAssCreate {
  pessoa_id: string;
  unidade_id: string;
  tipo?: string;
  data?: string;
  descricao?: string;
  encaminhamento?: string;
  profissional: string;
}

export async function listarFamiliasAss(): Promise<FamiliaAss[]> {
  return apiGet<FamiliaAss[]>('/api/v1/ass/familias');
}

export async function obterFamiliaAss(id: string): Promise<FamiliaAss> {
  return apiGet<FamiliaAss>(`/api/v1/ass/familias/${encodeURIComponent(id)}`);
}

export async function obterFamiliaAssPorNis(nis: string): Promise<FamiliaAss> {
  return apiGet<FamiliaAss>(`/api/v1/ass/familias/nis/${encodeURIComponent(nis)}`);
}

export async function criarFamiliaAss(payload: FamiliaAssCreate): Promise<FamiliaAss> {
  return apiPost<FamiliaAss>('/api/v1/ass/familias', payload);
}

export async function listarPessoasAss(): Promise<PessoaAss[]> {
  return apiGet<PessoaAss[]>('/api/v1/ass/pessoas');
}

export async function obterPessoaAss(id: string): Promise<PessoaAss> {
  return apiGet<PessoaAss>(`/api/v1/ass/pessoas/${encodeURIComponent(id)}`);
}

export async function obterPessoaAssPorCpf(cpf: string): Promise<PessoaAss> {
  return apiGet<PessoaAss>(`/api/v1/ass/pessoas/cpf/${encodeURIComponent(cpf)}`);
}

export async function listarPessoasPorFamiliaAss(familiaId: string): Promise<PessoaAss[]> {
  return apiGet<PessoaAss[]>(`/api/v1/ass/familias/${encodeURIComponent(familiaId)}/pessoas`);
}

export async function criarPessoaAss(payload: PessoaAssCreate): Promise<PessoaAss> {
  return apiPost<PessoaAss>('/api/v1/ass/pessoas', payload);
}

export async function listarUnidadesAss(): Promise<UnidadeAss[]> {
  return apiGet<UnidadeAss[]>('/api/v1/ass/unidades');
}

export async function obterUnidadeAss(id: string): Promise<UnidadeAss> {
  return apiGet<UnidadeAss>(`/api/v1/ass/unidades/${encodeURIComponent(id)}`);
}

export async function criarUnidadeAss(payload: UnidadeAssCreate): Promise<UnidadeAss> {
  return apiPost<UnidadeAss>('/api/v1/ass/unidades', payload);
}

export async function listarBeneficiosAss(): Promise<BeneficioAss[]> {
  return apiGet<BeneficioAss[]>('/api/v1/ass/beneficios');
}

export async function obterBeneficioAss(id: string): Promise<BeneficioAss> {
  return apiGet<BeneficioAss>(`/api/v1/ass/beneficios/${encodeURIComponent(id)}`);
}

export async function listarBeneficiosPorFamiliaAss(familiaId: string): Promise<BeneficioAss[]> {
  return apiGet<BeneficioAss[]>(`/api/v1/ass/familias/${encodeURIComponent(familiaId)}/beneficios`);
}

export async function solicitarBeneficioAss(payload: BeneficioAssCreate): Promise<BeneficioAss> {
  return apiPost<BeneficioAss>('/api/v1/ass/beneficios', payload);
}

export async function aprovarBeneficioAss(id: string): Promise<BeneficioAss> {
  return apiPost<BeneficioAss>(`/api/v1/ass/beneficios/${encodeURIComponent(id)}/aprovar`, {});
}

export async function negarBeneficioAss(id: string, justificativa: string): Promise<BeneficioAss> {
  return apiPost<BeneficioAss>(`/api/v1/ass/beneficios/${encodeURIComponent(id)}/negar?justificativa=${encodeURIComponent(justificativa)}`, {});
}

export async function entregarBeneficioAss(id: string): Promise<BeneficioAss> {
  return apiPost<BeneficioAss>(`/api/v1/ass/beneficios/${encodeURIComponent(id)}/entregar`, {});
}

export async function cancelarBeneficioAss(id: string): Promise<BeneficioAss> {
  return apiPost<BeneficioAss>(`/api/v1/ass/beneficios/${encodeURIComponent(id)}/cancelar`, {});
}

export async function listarAtendimentosAss(): Promise<AtendimentoAss[]> {
  return apiGet<AtendimentoAss[]>('/api/v1/ass/atendimentos');
}

export async function obterAtendimentoAss(id: string): Promise<AtendimentoAss> {
  return apiGet<AtendimentoAss>(`/api/v1/ass/atendimentos/${encodeURIComponent(id)}`);
}

export async function listarAtendimentosPorPessoaAss(pessoaId: string): Promise<AtendimentoAss[]> {
  return apiGet<AtendimentoAss[]>(`/api/v1/ass/pessoas/${encodeURIComponent(pessoaId)}/atendimentos`);
}

export async function listarAtendimentosPorUnidadeAss(unidadeId: string): Promise<AtendimentoAss[]> {
  return apiGet<AtendimentoAss[]>(`/api/v1/ass/unidades/${encodeURIComponent(unidadeId)}/atendimentos`);
}

export async function registrarAtendimentoAss(payload: AtendimentoAssCreate): Promise<AtendimentoAss> {
  return apiPost<AtendimentoAss>('/api/v1/ass/atendimentos', payload);
}



/* --- Atualizacao e exclusao (acoes das listagens) --- */

export interface FamiliaAssUpdate {
  nis?: string;
  responsavel_nome?: string;
  responsavel_cpf?: string;
  endereco?: string;
  telefone?: string;
  renda_per_capita?: number;
  quantidade_pessoas?: number;
  status?: string;
}

export interface PessoaAssUpdate {
  familia_id?: string;
  nome?: string;
  cpf?: string;
  data_nascimento?: string;
  sexo?: string;
  nome_mae?: string;
  parentesco?: string;
  escolaridade?: string;
  ocupacao?: string;
  renda?: number;
}

export interface UnidadeAssUpdate {
  codigo?: string;
  nome?: string;
  tipo?: string;
  endereco?: string;
  telefone?: string;
  email?: string;
  responsavel?: string;
  status?: string;
}

export async function atualizarFamiliaAss(id: string, payload: FamiliaAssUpdate): Promise<FamiliaAss> {
  return apiPatch<FamiliaAss>(`/api/v1/ass/familias/${encodeURIComponent(id)}`, payload);
}

export async function excluirFamiliaAss(id: string): Promise<FamiliaAss> {
  return apiDelete<FamiliaAss>(`/api/v1/ass/familias/${encodeURIComponent(id)}`);
}

export async function atualizarPessoaAss(id: string, payload: PessoaAssUpdate): Promise<PessoaAss> {
  return apiPatch<PessoaAss>(`/api/v1/ass/pessoas/${encodeURIComponent(id)}`, payload);
}

export async function excluirPessoaAss(id: string): Promise<PessoaAss> {
  return apiDelete<PessoaAss>(`/api/v1/ass/pessoas/${encodeURIComponent(id)}`);
}

export async function atualizarUnidadeAss(id: string, payload: UnidadeAssUpdate): Promise<UnidadeAss> {
  return apiPatch<UnidadeAss>(`/api/v1/ass/unidades/${encodeURIComponent(id)}`, payload);
}

export async function excluirUnidadeAss(id: string): Promise<UnidadeAss> {
  return apiDelete<UnidadeAss>(`/api/v1/ass/unidades/${encodeURIComponent(id)}`);
}



/* ------------------------------------------------------------------ */
/* DOM-TEL — Gestão Territorial                                       */
/* ------------------------------------------------------------------ */

export interface BairroTel {
  id: string;
  codigo: string;
  nome: string;
  tipo: string;
  populacao_estimada: number;
  area_km2: number;
  situacao: string;
  created_at: string;
  updated_at?: string | null;
}

export interface BairroTelCreate {
  codigo: string;
  nome: string;
  tipo?: string;
  populacao_estimada?: number;
  area_km2?: number;
}

export interface BairroTelUpdate {
  codigo?: string;
  nome?: string;
  tipo?: string;
  populacao_estimada?: number;
  area_km2?: number;
  situacao?: string;
}

export interface LogradouroTel {
  id: string;
  codigo: string;
  nome: string;
  tipo: string;
  bairro_id: string;
  cep?: string | null;
  numero_inicial: number;
  numero_final: number;
  situacao: string;
  created_at: string;
  updated_at?: string | null;
}

export interface LogradouroTelCreate {
  codigo: string;
  nome: string;
  bairro_id: string;
  tipo?: string;
  cep?: string;
  numero_inicial?: number;
  numero_final?: number;
}

export interface LogradouroTelUpdate {
  codigo?: string;
  nome?: string;
  tipo?: string;
  bairro_id?: string;
  cep?: string;
  numero_inicial?: number;
  numero_final?: number;
  situacao?: string;
}

export interface PlantaValoresTel {
  id: string;
  ano: number;
  bairro_id: string;
  ocupacao: string;
  valor_terreno_m2: number;
  valor_construcao_m2: number;
  aliquota_percent: number;
  situacao: string;
  legislacao?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface PlantaValoresTelCreate {
  ano: number;
  bairro_id: string;
  ocupacao?: string;
  valor_terreno_m2?: number;
  valor_construcao_m2?: number;
  aliquota_percent?: number;
  legislacao?: string;
  ativar?: boolean;
}

export interface PlantaValoresTelUpdate {
  ano?: number;
  valor_terreno_m2?: number;
  valor_construcao_m2?: number;
  aliquota_percent?: number;
  legislacao?: string;
}

export interface VerticeTel {
  latitude: number;
  longitude: number;
}

export interface GeorreferenciaTel {
  id: string;
  bairro_id: string;
  logradouro_id: string;
  geometria: string;
  latitude: number;
  longitude: number;
  altitude_m?: number | null;
  vertices: VerticeTel[];
  datum: string;
  precisao_m: number;
  data_levantamento: string;
  created_at: string;
}

export interface GeorreferenciaTelCreate {
  bairro_id?: string;
  logradouro_id?: string;
  geometria?: string;
  latitude?: number;
  longitude?: number;
  altitude_m?: number | null;
  vertices?: VerticeTel[];
  datum?: string;
  precisao_m?: number;
  data_levantamento?: string;
}



/* --- DOM-TEL: bairros ------------------------------------------------- */

export async function listarBairrosTel(): Promise<BairroTel[]> {
  return apiGet<BairroTel[]>('/api/v1/tel/bairros?page_size=100');
}

export async function criarBairroTel(payload: BairroTelCreate): Promise<BairroTel> {
  return apiPost<BairroTel>('/api/v1/tel/bairros', payload);
}

export async function atualizarBairroTel(id: string, payload: BairroTelUpdate): Promise<BairroTel> {
  return apiPatch<BairroTel>(`/api/v1/tel/bairros/${encodeURIComponent(id)}`, payload);
}

export async function excluirBairroTel(id: string): Promise<BairroTel> {
  return apiDelete<BairroTel>(`/api/v1/tel/bairros/${encodeURIComponent(id)}`);
}

/** Detalhe de uma divisão territorial pelo identificador opaco (RN-TEL-001). */
export async function obterBairroTel(id: string): Promise<BairroTel> {
  return apiGet<BairroTel>(`/api/v1/tel/bairros/${encodeURIComponent(id)}`);
}

/** Busca de divisão territorial pelo código cadastral (chave natural). */
export async function obterBairroPorCodigoTel(codigo: string): Promise<BairroTel> {
  return apiGet<BairroTel>(`/api/v1/tel/bairros/codigo/${encodeURIComponent(codigo)}`);
}

/** Logradouros vinculados a uma divisão territorial (RN-TEL-002). */
export async function listarLogradourosDoBairroTel(bairroId: string): Promise<LogradouroTel[]> {
  return apiGet<LogradouroTel[]>(`/api/v1/tel/bairros/${encodeURIComponent(bairroId)}/logradouros`);
}

/* --- DOM-TEL: logradouros --------------------------------------------- */

export async function listarLogradourosTel(): Promise<LogradouroTel[]> {
  return apiGet<LogradouroTel[]>('/api/v1/tel/logradouros?page_size=100');
}

export async function criarLogradouroTel(payload: LogradouroTelCreate): Promise<LogradouroTel> {
  return apiPost<LogradouroTel>('/api/v1/tel/logradouros', payload);
}

export async function atualizarLogradouroTel(
  id: string,
  payload: LogradouroTelUpdate,
): Promise<LogradouroTel> {
  return apiPatch<LogradouroTel>(`/api/v1/tel/logradouros/${encodeURIComponent(id)}`, payload);
}

export async function excluirLogradouroTel(id: string): Promise<LogradouroTel> {
  return apiDelete<LogradouroTel>(`/api/v1/tel/logradouros/${encodeURIComponent(id)}`);
}

/** Detalhe de um logradouro pelo identificador opaco. */
export async function obterLogradouroTel(id: string): Promise<LogradouroTel> {
  return apiGet<LogradouroTel>(`/api/v1/tel/logradouros/${encodeURIComponent(id)}`);
}

/** Busca de logradouro pelo código cadastral (chave natural). */
export async function obterLogradouroPorCodigoTel(codigo: string): Promise<LogradouroTel> {
  return apiGet<LogradouroTel>(`/api/v1/tel/logradouros/codigo/${encodeURIComponent(codigo)}`);
}

/* --- DOM-TEL: planta genérica de valores ------------------------------ */

export async function listarPlantasValoresTel(): Promise<PlantaValoresTel[]> {
  return apiGet<PlantaValoresTel[]>('/api/v1/tel/plantas-valores?page_size=100');
}

export async function criarPlantaValoresTel(
  payload: PlantaValoresTelCreate,
): Promise<PlantaValoresTel> {
  return apiPost<PlantaValoresTel>('/api/v1/tel/plantas-valores', payload);
}

export async function atualizarPlantaValoresTel(
  id: string,
  payload: PlantaValoresTelUpdate,
): Promise<PlantaValoresTel> {
  return apiPatch<PlantaValoresTel>(`/api/v1/tel/plantas-valores/${encodeURIComponent(id)}`, payload);
}

export async function ativarPlantaValoresTel(id: string): Promise<PlantaValoresTel> {
  return apiPost<PlantaValoresTel>(`/api/v1/tel/plantas-valores/${encodeURIComponent(id)}/ativar`);
}

export async function revogarPlantaValoresTel(
  id: string,
  motivo: string,
): Promise<PlantaValoresTel> {
  return apiPost<PlantaValoresTel>(`/api/v1/tel/plantas-valores/${encodeURIComponent(id)}/revogar`, {
    motivo,
  });
}

/** Detalhe de uma planta genérica de valores. */
export async function obterPlantaValoresTel(id: string): Promise<PlantaValoresTel> {
  return apiGet<PlantaValoresTel>(`/api/v1/tel/plantas-valores/${encodeURIComponent(id)}`);
}

/**
 * Consulta a planta genérica de valores vigente para ano, divisão e ocupação.
 *
 * É o ponto de integração com o DOM-IMO: o cadastro imobiliário consome estes
 * valores unitários para apurar o valor venal (RN-IMO-005). Retorna HTTP 404
 * quando não há planta vigente para a combinação informada.
 */
export async function obterPlantaVigenteTel(
  ano: number,
  bairroId: string,
  ocupacao: string,
): Promise<PlantaValoresTel> {
  const parametros = new URLSearchParams({
    ano: String(ano),
    bairro_id: bairroId,
    ocupacao,
  });
  return apiGet<PlantaValoresTel>(`/api/v1/tel/plantas-valores/vigente?${parametros.toString()}`);
}

/* --- DOM-TEL: georreferenciamento ------------------------------------- */

export async function listarGeorreferenciasTel(): Promise<GeorreferenciaTel[]> {
  return apiGet<GeorreferenciaTel[]>('/api/v1/tel/georreferencias?page_size=100');
}

export async function registrarGeorreferenciaTel(
  payload: GeorreferenciaTelCreate,
): Promise<GeorreferenciaTel> {
  return apiPost<GeorreferenciaTel>('/api/v1/tel/georreferencias', payload);
}

export async function excluirGeorreferenciaTel(id: string): Promise<GeorreferenciaTel> {
  return apiDelete<GeorreferenciaTel>(`/api/v1/tel/georreferencias/${encodeURIComponent(id)}`);
}

/** Detalhe de uma georreferência. */
export async function obterGeorreferenciaTel(id: string): Promise<GeorreferenciaTel> {
  return apiGet<GeorreferenciaTel>(`/api/v1/tel/georreferencias/${encodeURIComponent(id)}`);
}

/**
 * Lista as georreferências vinculadas a uma divisão ou a um logradouro.
 *
 * A API exige ao menos um dos dois filtros (HTTP 422 caso nenhum seja informado),
 * refletindo a regra de que a georreferência referencia **um ou outro**, nunca
 * ambos (RN-TEL-005).
 */
export async function listarGeorreferenciasPorReferenciaTel(params: {
  bairroId?: string;
  logradouroId?: string;
}): Promise<GeorreferenciaTel[]> {
  const consulta = new URLSearchParams();
  if (params.bairroId) consulta.set('bairro_id', params.bairroId);
  if (params.logradouroId) consulta.set('logradouro_id', params.logradouroId);
  return apiGet<GeorreferenciaTel[]>(
    `/api/v1/tel/georreferencias/referencia?${consulta.toString()}`,
  );
}



/* ------------------------------------------------------------------ */
/* DOM-IMO — Cadastro Imobiliário                                     */
/* ------------------------------------------------------------------ */

export interface ImovelImo {
  id: string;
  inscricao_imobiliaria: string;
  logradouro_id: string;
  bairro_id: string;
  numero?: string | null;
  complemento?: string | null;
  tipo: string;
  situacao: string;
  tipo_propriedade: string;
  area_terreno_m2: number;
  area_construida_m2: number;
  ano_construcao?: number | null;
  created_at: string;
  updated_at?: string | null;
}

export interface ImovelImoCreate {
  inscricao_imobiliaria: string;
  logradouro_id: string;
  bairro_id: string;
  numero?: string;
  complemento?: string;
  tipo?: string;
  tipo_propriedade?: string;
  area_terreno_m2?: number;
  area_construida_m2?: number;
  ano_construcao?: number | null;
}

export interface ImovelImoUpdate {
  numero?: string;
  complemento?: string;
  tipo?: string;
  tipo_propriedade?: string;
  area_terreno_m2?: number;
  area_construida_m2?: number;
  ano_construcao?: number | null;
}

export interface ProprietarioImo {
  id: string;
  imovel_id: string;
  pessoa_id: string;
  nome: string;
  cpf: string;
  vinculo: string;
  principal: boolean;
  created_at: string;
  updated_at?: string | null;
}

export interface ProprietarioImoCreate {
  imovel_id: string;
  nome: string;
  cpf: string;
  pessoa_id?: string;
  vinculo?: string;
  principal?: boolean;
}

export interface AvaliacaoImo {
  id: string;
  imovel_id: string;
  ano: number;
  valor_terreno_m2_unitario: number;
  valor_construcao_m2_unitario: number;
  aliquota_percent: number;
  area_terreno_m2: number;
  area_construida_m2: number;
  valor_terreno: number;
  valor_construcao: number;
  valor_venal: number;
  valor_lancamento: number;
  situacao: string;
  data_avaliacao: string;
  created_at: string;
  updated_at?: string | null;
}

export interface AvaliacaoImoCreate {
  imovel_id: string;
  ano: number;
  valor_terreno_m2_unitario: number;
  valor_construcao_m2_unitario: number;
  aliquota_percent?: number;
  data_avaliacao?: string;
  concluir?: boolean;
}

export interface CaracteristicaImo {
  id: string;
  imovel_id: string;
  obra: string;
  numero_pavimentos: number;
  ano_renovacao?: number | null;
  observacao?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface CaracteristicaImoCreate {
  imovel_id: string;
  obra?: string;
  numero_pavimentos?: number;
  ano_renovacao?: number | null;
  observacao?: string;
}

export interface GeometriaImo {
  id: string;
  imovel_id: string;
  geometria: string;
  latitude: number;
  longitude: number;
  vertices: VerticeTel[];
  datum: string;
  precisao_m: number;
  data_levantamento: string;
  created_at: string;
}

export interface GeometriaImoCreate {
  imovel_id: string;
  geometria?: string;
  latitude?: number;
  longitude?: number;
  vertices?: VerticeTel[];
  datum?: string;
  precisao_m?: number;
  data_levantamento?: string;
}



/* --- DOM-IMO: imóveis ------------------------------------------------- */

export async function listarImoveisImo(): Promise<ImovelImo[]> {
  return apiGet<ImovelImo[]>('/api/v1/imo/imoveis?page_size=100');
}

export async function criarImovelImo(payload: ImovelImoCreate): Promise<ImovelImo> {
  return apiPost<ImovelImo>('/api/v1/imo/imoveis', payload);
}

export async function atualizarImovelImo(id: string, payload: ImovelImoUpdate): Promise<ImovelImo> {
  return apiPatch<ImovelImo>(`/api/v1/imo/imoveis/${encodeURIComponent(id)}`, payload);
}

export async function alterarSituacaoImovelImo(id: string, situacao: string): Promise<ImovelImo> {
  return apiPost<ImovelImo>(`/api/v1/imo/imoveis/${encodeURIComponent(id)}/situacao`, { situacao });
}

export async function excluirImovelImo(id: string): Promise<ImovelImo> {
  return apiDelete<ImovelImo>(`/api/v1/imo/imoveis/${encodeURIComponent(id)}`);
}

/** Detalhe de um imóvel pelo identificador opaco. */
export async function obterImovelImo(id: string): Promise<ImovelImo> {
  return apiGet<ImovelImo>(`/api/v1/imo/imoveis/${encodeURIComponent(id)}`);
}

/** Busca de imóvel pela inscrição imobiliária (chave natural, RN-IMO-001). */
export async function obterImovelPorInscricaoImo(inscricao: string): Promise<ImovelImo> {
  return apiGet<ImovelImo>(`/api/v1/imo/imoveis/inscricao/${encodeURIComponent(inscricao)}`);
}

/** Imóveis vinculados a um logradouro. */
export async function listarImoveisDoLogradouroImo(logradouroId: string): Promise<ImovelImo[]> {
  return apiGet<ImovelImo[]>(`/api/v1/imo/imoveis/logradouro/${encodeURIComponent(logradouroId)}`);
}

/** Imóveis vinculados a uma divisão territorial. */
export async function listarImoveisDoBairroImo(bairroId: string): Promise<ImovelImo[]> {
  return apiGet<ImovelImo[]>(`/api/v1/imo/imoveis/bairro/${encodeURIComponent(bairroId)}`);
}

/** Proprietários de um imóvel específico (drill-down do cadastro). */
export async function listarProprietariosDoImovelImo(imovelId: string): Promise<ProprietarioImo[]> {
  return apiGet<ProprietarioImo[]>(`/api/v1/imo/imoveis/${encodeURIComponent(imovelId)}/proprietarios`);
}

/* --- DOM-IMO: proprietários ------------------------------------------- */

export async function listarProprietariosImo(): Promise<ProprietarioImo[]> {
  return apiGet<ProprietarioImo[]>('/api/v1/imo/proprietarios?page_size=100');
}

export async function vincularProprietarioImo(
  payload: ProprietarioImoCreate,
): Promise<ProprietarioImo> {
  return apiPost<ProprietarioImo>('/api/v1/imo/proprietarios', payload);
}

export async function removerProprietarioImo(id: string): Promise<ProprietarioImo> {
  return apiDelete<ProprietarioImo>(`/api/v1/imo/proprietarios/${encodeURIComponent(id)}`);
}

/* --- DOM-IMO: avaliações ---------------------------------------------- */

export async function listarAvaliacoesImo(): Promise<AvaliacaoImo[]> {
  return apiGet<AvaliacaoImo[]>('/api/v1/imo/avaliacoes?page_size=100');
}

export async function avaliarImovelImo(payload: AvaliacaoImoCreate): Promise<AvaliacaoImo> {
  return apiPost<AvaliacaoImo>('/api/v1/imo/avaliacoes', payload);
}

export async function cancelarAvaliacaoImo(id: string, motivo: string): Promise<AvaliacaoImo> {
  return apiPost<AvaliacaoImo>(`/api/v1/imo/avaliacoes/${encodeURIComponent(id)}/cancelar`, {
    motivo,
  });
}

/**
 * Conclui uma avaliação em aberto, fixando o valor venal e o lançamento.
 *
 * Transição da máquina de estados de RN-IMO-005: a conclusão é definitiva e um
 * exercício já concluído não pode ser reavaliado.
 */
export async function concluirAvaliacaoImo(id: string): Promise<AvaliacaoImo> {
  return apiPost<AvaliacaoImo>(`/api/v1/imo/avaliacoes/${encodeURIComponent(id)}/concluir`);
}

/** Detalhe de uma avaliação. */
export async function obterAvaliacaoImo(id: string): Promise<AvaliacaoImo> {
  return apiGet<AvaliacaoImo>(`/api/v1/imo/avaliacoes/${encodeURIComponent(id)}`);
}

/** Avaliações de um imóvel específico (histórico por exercício). */
export async function listarAvaliacoesDoImovelImo(imovelId: string): Promise<AvaliacaoImo[]> {
  return apiGet<AvaliacaoImo[]>(`/api/v1/imo/avaliacoes/imovel/${encodeURIComponent(imovelId)}`);
}

/* --- DOM-IMO: características ------------------------------------------ */

export async function listarCaracteristicasImo(): Promise<CaracteristicaImo[]> {
  return apiGet<CaracteristicaImo[]>('/api/v1/imo/caracteristicas?page_size=100');
}

export async function registrarCaracteristicaImo(
  payload: CaracteristicaImoCreate,
): Promise<CaracteristicaImo> {
  return apiPost<CaracteristicaImo>('/api/v1/imo/caracteristicas', payload);
}

/** Características construtivas de um imóvel específico. */
export async function listarCaracteristicasDoImovelImo(imovelId: string): Promise<CaracteristicaImo[]> {
  return apiGet<CaracteristicaImo[]>(`/api/v1/imo/caracteristicas/imovel/${encodeURIComponent(imovelId)}`);
}

/* --- DOM-IMO: geometria do lote ---------------------------------------- */

export async function listarGeometriasImo(): Promise<GeometriaImo[]> {
  return apiGet<GeometriaImo[]>('/api/v1/imo/geometrias?page_size=100');
}

export async function registrarGeometriaImo(
  payload: GeometriaImoCreate,
): Promise<GeometriaImo> {
  return apiPost<GeometriaImo>('/api/v1/imo/geometrias', payload);
}

/** Geometria georreferenciada de um imóvel específico (RN-IMO-007). */
export async function listarGeometriasDoImovelImo(imovelId: string): Promise<GeometriaImo[]> {
  return apiGet<GeometriaImo[]>(`/api/v1/imo/geometrias/imovel/${encodeURIComponent(imovelId)}`);
}


/* ======================================================================
 * DOM-GEO — Geoinformação Municipal (mapas SIG)
 * ====================================================================== */

export interface CamadaGeo {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  tipo: string;
  formato: string;
  fonte?: string | null;
  data_atualizacao: string;
  datum: string;
  srid: number;
  url_servico?: string | null;
  zoom_minimo: number;
  zoom_maximo: number;
  visivel: boolean;
  situacao: string;
  created_at: string;
  updated_at?: string | null;
}

export interface CamadaGeoCreate {
  codigo: string;
  nome: string;
  descricao?: string;
  tipo?: string;
  formato?: string;
  fonte?: string;
  datum?: string;
  url_servico?: string;
  srid?: number;
  zoom_minimo?: number;
  zoom_maximo?: number;
  ativar?: boolean;
}

/** Campos atualizáveis da camada (todos opcionais). */
export type CamadaGeoUpdate = Partial<Omit<CamadaGeoCreate, 'ativar'>>;

export interface MapaSigGeo {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  tipo: string;
  situacao: string;
  datum: string;
  srid: number;
  escala_denominador: number;
  zoom_inicial: number;
  zoom_minimo: number;
  zoom_maximo: number;
  lat_min?: number | null;
  lon_min?: number | null;
  lat_max?: number | null;
  lon_max?: number | null;
  publicado_em?: string | null;
  criado_por?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface MapaSigGeoCreate {
  codigo: string;
  nome: string;
  descricao?: string;
  tipo?: string;
  escala_denominador?: number;
  lat_min?: number;
  lon_min?: number;
  lat_max?: number;
  lon_max?: number;
  datum?: string;
  srid?: number;
  zoom_inicial?: number;
  zoom_minimo?: number;
  zoom_maximo?: number;
}

/** Campos atualizáveis do mapa SIG (todos opcionais). */
export type MapaSigGeoUpdate = Partial<MapaSigGeoCreate>;

export interface MapaCamadaGeo {
  id: string;
  mapa_id: string;
  camada_id: string;
  ordem: number;
  opacidade: number;
  visivel: boolean;
  rotulo?: string | null;
  created_at: string;
}

export interface MapaCamadaGeoCreate {
  camada_id: string;
  ordem?: number;
  opacidade?: number;
  visivel?: boolean;
  rotulo?: string;
}

export interface VerticeGeo {
  latitude: number;
  longitude: number;
}

export interface FeatureGeo {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  camada_id: string;
  geometria: string;
  latitude: number;
  longitude: number;
  vertices: VerticeGeo[];
  datum: string;
  atributos: Record<string, unknown>;
  criado_por?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface FeatureGeoCreate {
  codigo: string;
  nome: string;
  descricao?: string;
  camada_id: string;
  geometria?: string;
  latitude?: number;
  longitude?: number;
  vertices?: VerticeGeo[];
  datum?: string;
  atributos?: Record<string, unknown>;
}

export interface ServicoGeo {
  id: string;
  codigo: string;
  nome: string;
  descricao?: string | null;
  tipo: string;
  situacao: string;
  url?: string | null;
  camada?: string | null;
  datum: string;
  srid: number;
  zoom_minimo: number;
  zoom_maximo: number;
  publico: boolean;
  created_at: string;
  updated_at?: string | null;
}

export interface ServicoGeoCreate {
  codigo: string;
  nome: string;
  descricao?: string;
  tipo?: string;
  url?: string;
  camada?: string;
  publico?: boolean;
  datum?: string;
  srid?: number;
  zoom_minimo?: number;
  zoom_maximo?: number;
}

/** Campos atualizáveis do serviço geoespacial (todos opcionais). */
export type ServicoGeoUpdate = Partial<ServicoGeoCreate>;

/** Lista as camadas cartograficas cadastradas. */
export async function listarCamadasGeo(): Promise<CamadaGeo[]> {
  return apiGet<CamadaGeo[]>('/api/v1/geo/camadas?page_size=100');
}

/** Cadastra uma camada cartografica (RN-GEO-001). */
export async function cadastrarCamadaGeo(payload: CamadaGeoCreate): Promise<CamadaGeo> {
  return apiPost<CamadaGeo>('/api/v1/geo/camadas', payload);
}

/** Atualiza uma camada cartografica. */
export async function atualizarCamadaGeo(id: string, payload: CamadaGeoUpdate): Promise<CamadaGeo> {
  return apiPatch<CamadaGeo>(`/api/v1/geo/camadas/${encodeURIComponent(id)}`, payload);
}

/** Detalhe de uma camada cartografica. */
export async function obterCamadaGeo(id: string): Promise<CamadaGeo> {
  return apiGet<CamadaGeo>(`/api/v1/geo/camadas/${encodeURIComponent(id)}`);
}

/** Ativa a camada para publicacao (RN-GEO-006). */
export async function ativarCamadaGeo(id: string): Promise<CamadaGeo> {
  return apiPost<CamadaGeo>(`/api/v1/geo/camadas/${encodeURIComponent(id)}/ativar`, {});
}

/** Desativa a camada (RN-GEO-006). */
export async function desativarCamadaGeo(id: string): Promise<CamadaGeo> {
  return apiPost<CamadaGeo>(`/api/v1/geo/camadas/${encodeURIComponent(id)}/desativar`, {});
}

/** Exclui (logicamente) uma camada de mapa. */
export async function excluirCamadaGeo(id: string): Promise<CamadaGeo> {
  return apiDelete<CamadaGeo>(`/api/v1/geo/camadas/${encodeURIComponent(id)}`);
}

/** Lista os mapas SIG cadastrados. */
export async function listarMapasGeo(): Promise<MapaSigGeo[]> {
  return apiGet<MapaSigGeo[]>('/api/v1/geo/mapas?page_size=100');
}

/** Cadastra um mapa SIG (RN-GEO-002). */
export async function cadastrarMapaGeo(payload: MapaSigGeoCreate): Promise<MapaSigGeo> {
  return apiPost<MapaSigGeo>('/api/v1/geo/mapas', payload);
}

/** Atualiza um mapa SIG. */
export async function atualizarMapaGeo(id: string, payload: MapaSigGeoUpdate): Promise<MapaSigGeo> {
  return apiPatch<MapaSigGeo>(`/api/v1/geo/mapas/${encodeURIComponent(id)}`, payload);
}

/** Exclui (logicamente) um mapa SIG. */
export async function excluirMapaGeo(id: string): Promise<MapaSigGeo> {
  return apiDelete<MapaSigGeo>(`/api/v1/geo/mapas/${encodeURIComponent(id)}`);
}

/** Publica o mapa no geoportal (RN-GEO-004). */
export async function publicarMapaGeo(id: string): Promise<MapaSigGeo> {
  return apiPost<MapaSigGeo>(`/api/v1/geo/mapas/${encodeURIComponent(id)}/publicar`, {});
}

/** Arquiva o mapa publicado (RN-GEO-004). */
export async function arquivarMapaGeo(id: string): Promise<MapaSigGeo> {
  return apiPost<MapaSigGeo>(`/api/v1/geo/mapas/${encodeURIComponent(id)}/arquivar`, {});
}

/** Camadas que compoem um mapa (RN-GEO-004). */
export async function listarComposicaoGeo(mapaId: string): Promise<MapaCamadaGeo[]> {
  return apiGet<MapaCamadaGeo[]>(`/api/v1/geo/mapas/${encodeURIComponent(mapaId)}/composicao`);
}

/** Adiciona uma camada a composicao do mapa (RN-GEO-004). */
export async function comporCamadaGeo(
  mapaId: string,
  payload: MapaCamadaGeoCreate,
): Promise<MapaCamadaGeo> {
  return apiPost<MapaCamadaGeo>(`/api/v1/geo/mapas/${encodeURIComponent(mapaId)}/composicao`, payload);
}

/** Remove uma camada da composicao do mapa (RN-GEO-004). */
export async function removerComposicaoGeo(mapaId: string, vinculoId: string): Promise<MapaCamadaGeo> {
  return apiDelete<MapaCamadaGeo>(
    `/api/v1/geo/mapas/${encodeURIComponent(mapaId)}/composicao/${encodeURIComponent(vinculoId)}`,
  );
}

/** Lista todos os elementos geoespaciais cadastrados. */
export async function listarTodasFeaturesGeo(): Promise<FeatureGeo[]> {
  return apiGet<FeatureGeo[]>('/api/v1/geo/features?page_size=100');
}

/** Lista os elementos geoespaciais de uma camada (RN-GEO-008). */
export async function listarFeaturesGeo(camadaId: string): Promise<FeatureGeo[]> {
  return apiGet<FeatureGeo[]>(`/api/v1/geo/features/camada/${encodeURIComponent(camadaId)}`);
}

/** Registra um elemento geoespacial (RN-GEO-003). */
export async function registrarFeatureGeo(payload: FeatureGeoCreate): Promise<FeatureGeo> {
  return apiPost<FeatureGeo>('/api/v1/geo/features', payload);
}

/** Exclui (logicamente) um elemento geoespacial. */
export async function excluirFeatureGeo(id: string): Promise<FeatureGeo> {
  return apiDelete<FeatureGeo>(`/api/v1/geo/features/${encodeURIComponent(id)}`);
}

/** Lista os servicos geoespaciais publicados (RN-GEO-007). */
export async function listarServicosGeo(): Promise<ServicoGeo[]> {
  return apiGet<ServicoGeo[]>('/api/v1/geo/servicos?page_size=100');
}

/** Cadastra um servico geoespacial (RN-GEO-007). */
export async function cadastrarServicoGeo(payload: ServicoGeoCreate): Promise<ServicoGeo> {
  return apiPost<ServicoGeo>('/api/v1/geo/servicos', payload);
}

/** Atualiza um servico geoespacial. */
export async function atualizarServicoGeo(
  id: string,
  payload: ServicoGeoUpdate,
): Promise<ServicoGeo> {
  return apiPatch<ServicoGeo>(`/api/v1/geo/servicos/${encodeURIComponent(id)}`, payload);
}

/** Detalhe de um servico geoespacial. */
export async function obterServicoGeo(id: string): Promise<ServicoGeo> {
  return apiGet<ServicoGeo>(`/api/v1/geo/servicos/${encodeURIComponent(id)}`);
}

/** Inativa um servico geoespacial (RN-GEO-007). */
export async function inativarServicoGeo(id: string): Promise<ServicoGeo> {
  return apiPost<ServicoGeo>(`/api/v1/geo/servicos/${encodeURIComponent(id)}/inativar`, {});
}

/** Exclui (logicamente) um servico geoespacial. */
export async function excluirServicoGeo(id: string): Promise<ServicoGeo> {
  return apiDelete<ServicoGeo>(`/api/v1/geo/servicos/${encodeURIComponent(id)}`);
}

/* ======================================================================
 * DOM-OBR — Obras e Infraestrutura (acompanhamento fisico-financeiro)
 * ====================================================================== */

export interface Obra {
  id: string;
  numero: string;
  nome: string;
  descricao?: string | null;
  tipo: string;
  situacao: string;
  tipo_contratacao: string;
  fonte_recurso: string;
  valor_orcado: number;
  valor_contratado: number;
  valor_mediado: number;
  valor_pago: number;
  percentual_fisico: number;
  percentual_financeiro: number;
  empresa_contratada?: string | null;
  numero_contrato?: string | null;
  responsavel_tecnico?: string | null;
  endereco?: string | null;
  bairro?: string | null;
  data_inicio_prevista?: string | null;
  data_fim_prevista?: string | null;
  data_inicio_real?: string | null;
  data_fim_real?: string | null;
  observacao?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface ObraCreate {
  numero: string;
  nome: string;
  descricao?: string;
  tipo?: string;
  tipo_contratacao?: string;
  fonte_recurso?: string;
  valor_orcado?: number;
  valor_contratado?: number;
  empresa_contratada?: string;
  numero_contrato?: string;
  responsavel_tecnico?: string;
  endereco?: string;
  bairro?: string;
  data_inicio_prevista?: string;
  data_fim_prevista?: string;
}

/** Campos atualizáveis da obra (todos opcionais; `numero` é imutável). */
export type ObraUpdate = Partial<Omit<ObraCreate, 'numero'>>;

export interface MedicaoObra {
  id: string;
  obra_id: string;
  numero: string;
  tipo: string;
  situacao: string;
  data: string;
  percentual_fisico: number;
  valor_medido: number;
  responsavel_tecnico: string;
  observacao?: string | null;
  created_at: string;
  updated_at?: string | null;
}

export interface MedicaoObraCreate {
  obra_id: string;
  numero: string;
  tipo?: string;
  data?: string;
  percentual_fisico?: number;
  valor_medido?: number;
  responsavel_tecnico: string;
  observacao?: string;
}

export interface DespesaObra {
  id: string;
  obra_id: string;
  medicao_id?: string | null;
  descricao: string;
  tipo: string;
  valor: number;
  data: string;
  documento?: string | null;
  credor?: string | null;
  observacao?: string | null;
  created_at: string;
}

export interface DespesaObraCreate {
  obra_id: string;
  medicao_id?: string;
  descricao: string;
  tipo?: string;
  valor: number;
  data?: string;
  credor?: string;
}

export interface EtapaObra {
  id: string;
  obra_id: string;
  numero: string;
  descricao: string;
  tipo: string;
  situacao: string;
  percentual_previsto: number;
  percentual_realizado: number;
  data_inicio_prevista?: string | null;
  data_fim_prevista?: string | null;
  data_conclusao?: string | null;
  responsavel: string;
  created_at: string;
  updated_at?: string | null;
}

export interface EtapaObraCreate {
  obra_id: string;
  numero: string;
  descricao: string;
  tipo?: string;
  percentual_previsto?: number;
  responsavel: string;
}

export interface VistoriaObra {
  id: string;
  obra_id: string;
  data: string;
  tipo: string;
  parecer: string;
  percentual_fisico_verificado: number;
  fiscal: string;
  observacao?: string | null;
  created_at: string;
}

export interface VistoriaObraCreate {
  obra_id: string;
  data?: string;
  tipo?: string;
  parecer?: string;
  percentual_fisico_verificado?: number;
  fiscal: string;
  observacao?: string;
}

/** Visao consolidada do acompanhamento fisico-financeiro da obra. */
export interface ObraDetalhe {
  obra: Obra;
  medicoes: MedicaoObra[];
  despesas: DespesaObra[];
  etapas: EtapaObra[];
  vistorias: VistoriaObra[];
}

/** Lista as obras publicas cadastradas. */
export async function listarObras(): Promise<Obra[]> {
  return apiGet<Obra[]>('/api/v1/obr/obras?page_size=100');
}

/** Cadastra uma obra publica (RN-OBR-001). */
export async function cadastrarObra(payload: ObraCreate): Promise<Obra> {
  return apiPost<Obra>('/api/v1/obr/obras', payload);
}

/** Atualiza os dados cadastrais de uma obra não concluída. */
export async function atualizarObra(id: string, payload: ObraUpdate): Promise<Obra> {
  return apiPatch<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}`, payload);
}

/** Acompanhamento fisico-financeiro consolidado da obra. */
export async function obterAcompanhamentoObra(id: string): Promise<ObraDetalhe> {
  return apiGet<ObraDetalhe>(`/api/v1/obr/obras/${encodeURIComponent(id)}/acompanhamento`);
}

/** Inicia a execucao fisica da obra (RN-OBR-002). */
export async function iniciarExecucaoObra(id: string, motivo?: string): Promise<Obra> {
  return apiPost<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}/iniciar-execucao`, {
    motivo: motivo ?? '',
  });
}

/** Suspende a execucao da obra (RN-OBR-002). */
export async function suspenderObra(id: string, motivo: string): Promise<Obra> {
  return apiPost<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}/suspender`, { motivo });
}

/** Conclui a obra, exigindo 100% do avanco fisico (RN-OBR-005). */
export async function concluirObra(id: string, motivo?: string): Promise<Obra> {
  return apiPost<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}/concluir`, {
    motivo: motivo ?? '',
  });
}

/** Cancela a obra (RN-OBR-002). */
export async function cancelarObra(id: string, motivo: string): Promise<Obra> {
  return apiPost<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}/cancelar`, { motivo });
}

/** Exclui (logicamente) uma obra sem dependencias financeiras. */
export async function excluirObra(id: string): Promise<Obra> {
  return apiDelete<Obra>(`/api/v1/obr/obras/${encodeURIComponent(id)}`);
}

/** Registra uma medicao fisico-financeira (RN-OBR-005). */
export async function registrarMedicaoObra(payload: MedicaoObraCreate): Promise<MedicaoObra> {
  return apiPost<MedicaoObra>('/api/v1/obr/medicoes', payload);
}

/** Confere e aprova a medicao, recompondo o avanco da obra (RN-OBR-005). */
export async function aprovarMedicaoObra(id: string): Promise<MedicaoObra> {
  return apiPost<MedicaoObra>(`/api/v1/obr/medicoes/${encodeURIComponent(id)}/aprovar`, {});
}

/** Glosa uma medicao, com justificativa obrigatoria (RN-OBR-005). */
export async function glosarMedicaoObra(id: string, motivo: string): Promise<MedicaoObra> {
  return apiPost<MedicaoObra>(`/api/v1/obr/medicoes/${encodeURIComponent(id)}/glosar`, { motivo });
}

/** Cancela uma medicao ainda nao aprovada (RN-OBR-005). */
export async function cancelarMedicaoObra(id: string, motivo = ''): Promise<MedicaoObra> {
  return apiPost<MedicaoObra>(`/api/v1/obr/medicoes/${encodeURIComponent(id)}/cancelar`, { motivo });
}

/** Registra uma despesa financeira da obra (RN-OBR-006). */
export async function registrarDespesaObra(payload: DespesaObraCreate): Promise<DespesaObra> {
  return apiPost<DespesaObra>('/api/v1/obr/despesas', payload);
}

/** Exclui (logicamente) uma despesa da obra. */
export async function excluirDespesaObra(id: string): Promise<DespesaObra> {
  return apiDelete<DespesaObra>(`/api/v1/obr/despesas/${encodeURIComponent(id)}`);
}

/** Cadastra uma etapa de execucao da obra (RN-OBR-007). */
export async function cadastrarEtapaObra(payload: EtapaObraCreate): Promise<EtapaObra> {
  return apiPost<EtapaObra>('/api/v1/obr/etapas', payload);
}

/** Atualiza o avanco fisico de uma etapa (RN-OBR-007). */
export async function atualizarEtapaObra(
  id: string,
  payload: { percentual_realizado?: number; situacao?: string },
): Promise<EtapaObra> {
  return apiPatch<EtapaObra>(`/api/v1/obr/etapas/${encodeURIComponent(id)}`, payload);
}

/** Conclui uma etapa, exigindo 100% do previsto (RN-OBR-007). */
export async function concluirEtapaObra(id: string): Promise<EtapaObra> {
  return apiPost<EtapaObra>(`/api/v1/obr/etapas/${encodeURIComponent(id)}/concluir`, {});
}

/** Registra uma vistoria fiscalizadora da obra (RN-OBR-008). */
export async function registrarVistoriaObra(payload: VistoriaObraCreate): Promise<VistoriaObra> {
  return apiPost<VistoriaObra>('/api/v1/obr/vistorias', payload);
}
