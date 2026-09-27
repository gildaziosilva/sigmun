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


