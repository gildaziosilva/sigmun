import type { ReactNode } from 'react';
import type {
  ManifestacaoOuv,
  DenunciaOuv,
  PedidoLaiOuv,
  ProtocoloOuv,
  DadosCidadaoOuv,
  PrazoRespostaOuv,
} from '../../lib/api';

// ==================== Tipos de Estado ====================

export interface OuvDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export interface OuvResources {
  manifestacoes: OuvDataState<ManifestacaoOuv[]>;
  denuncias: OuvDataState<DenunciaOuv[]>;
  pedidosLai: OuvDataState<PedidoLaiOuv[]>;
  recarregar: () => void;
}

export type ExecutarOuv = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

// ==================== Abas ====================

export const OUV_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'manifestacoes', rotulo: 'Manifestações' },
  { id: 'denuncias', rotulo: 'Denúncias' },
  { id: 'pedidos-lai', rotulo: 'Pedidos LAI' },
  { id: 'estatisticas', rotulo: 'Estatísticas' },
] as const;
export type OuvTab = (typeof OUV_TABS)[number]['id'];

// ==================== Componentes Compartilhados ====================

export function Field(props: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  children?: ReactNode;
  required?: boolean;
  hint?: string;
  type?: string;
  min?: string;
  max?: string;
  step?: string;
  placeholder?: string;
}) {
  const { label, value, onChange, children, required, hint, type = 'text', min, max, step, placeholder } = props;
  return (
    <label>
      <span>{label}{required ? ' *' : ''}</span>
      {children ?? (
        <input
          type={type}
          value={value}
          min={min}
          max={max}
          step={step}
          placeholder={placeholder}
          onChange={(event) => onChange(event.target.value)}
          required={required}
        />
      )}
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function SelectField(props: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  options: readonly { value: string; label: string }[];
  required?: boolean;
  hint?: string;
}) {
  const { label, value, onChange, options, required, hint } = props;
  return (
    <label>
      <span>{label}{required ? ' *' : ''}</span>
      <select value={value} onChange={(event) => onChange(event.target.value)} required={required}>
        <option value="">Selecione…</option>
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function TextAreaField(props: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  required?: boolean;
  hint?: string;
  rows?: number;
  placeholder?: string;
}) {
  const { label, value, onChange, required, hint, rows = 3, placeholder } = props;
  return (
    <label>
      <span>{label}{required ? ' *' : ''}</span>
      <textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        required={required}
        rows={rows}
        placeholder={placeholder}
      />
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function StatusBadge({ value }: { value: string }) {
  const normalized = value.toLocaleLowerCase('pt-BR');
  const tone =
    ['concluida', 'respondida', 'autorizada', 'deferido'].includes(normalized) ? 'ok' :
    ['cancelada', 'arquivada', 'negada', 'indeferido'].includes(normalized) ? 'danger' :
    ['registrada', 'em_analise', 'encaminhada', 'em_tratamento', 'aguardando_complementacao', 'solicitada'].includes(normalized) ? 'warning' :
    'neutral';
  const label = value.replaceAll('_', ' ').replace(/\w/g, (l) => l.toUpperCase());
  return <span className={`ouv-status ouv-status--${tone}`}>{label}</span>;
}

export function PrioridadeBadge({ value }: { value: string }) {
  const tone =
    value === 'urgente' ? 'danger' :
    value === 'alta' ? 'warning' :
    value === 'normal' ? 'ok' :
    'neutral';
  const label = value.charAt(0).toUpperCase() + value.slice(1);
  return <span className={`ouv-prioridade ouv-prioridade--${tone}`}>{label}</span>;
}

export function TipoManifestacaoBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    sugestao: 'Sugestão',
    elogio: 'Elogio',
    reclamacao: 'Reclamação',
    solicitacao: 'Solicitação',
    denuncia: 'Denúncia',
    pedido_acesso_informacao: 'Pedido LAI',
  };
  return <span className="ouv-tipo">{labels[value] ?? value}</span>;
}

export function formatarData(value?: string | null): string {
  if (!value) return '—';
  const date = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  return Number.isNaN(date.getTime()) ? value : new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(date);
}

export function formatarDataHora(value?: string | null): string {
  if (!value) return '—';
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? value : new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short', timeStyle: 'short' }).format(date);
}

export function formatarNumero(value: number): string {
  return new Intl.NumberFormat('pt-BR').format(value);
}

export function formatarMoeda(value: number | null | undefined): string {
  if (value === null || value === undefined) return '—';
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

export function getProtocolo(m: { protocolo?: ProtocoloOuv }): string {
  return m.protocolo ? `${m.protocolo.ano}-${m.protocolo.numero}` : '—';
}

export function getCidadaoNome(m: { cidadao?: DadosCidadaoOuv }): string {
  if (!m.cidadao) return '—';
  if (m.cidadao.anonimo) return 'Anônimo';
  return m.cidadao.nome || '—';
}

export function getCidadaoExibicao(m: { cidadao?: DadosCidadaoOuv }): string {
  if (!m.cidadao) return '—';
  if (m.cidadao.anonimo) return 'Anônimo';
  const partes = [];
  if (m.cidadao.nome) partes.push(m.cidadao.nome);
  if (m.cidadao.cpf) partes.push(`CPF: ${m.cidadao.cpf}`);
  if (m.cidadao.email) partes.push(m.cidadao.email);
  return partes.join(' · ') || '—';
}

export function getPrazoStatus(prazo?: PrazoRespostaOuv): { label: string; tone: 'ok' | 'warning' | 'danger' | 'neutral' } {
  if (!prazo) return { label: 'Sem prazo', tone: 'neutral' };
  if (prazo.vencido) return { label: 'Vencido', tone: 'danger' };
  if (prazo.dias_restantes <= 3) return { label: `${prazo.dias_restantes} dia(s)`, tone: 'danger' };
  if (prazo.dias_restantes <= 7) return { label: `${prazo.dias_restantes} dia(s)`, tone: 'warning' };
  return { label: `${prazo.dias_restantes} dia(s)`, tone: 'ok' };
}

export function PrazoBadge({ prazo }: { prazo?: PrazoRespostaOuv }) {
  const { label, tone } = getPrazoStatus(prazo);
  return <span className={`ouv-prazo ouv-prazo--${tone}`}>{label}</span>;
}

export function TipoDenunciaBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    corrupcao: 'Corrupção',
    improbidade: 'Improbidade',
    assedio: 'Assédio',
    desvio_verba: 'Desvio de Verba',
    nepotismo: 'Nepotismo',
    fraude_licitacao: 'Fraude em Licitação',
    outro: 'Outro',
  };
  return <span className="ouv-tipo-denuncia">{labels[value] ?? value}</span>;
}

export function NivelSigiloBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    publico: 'Público',
    restrito: 'Restrito',
    sigiloso: 'Sigiloso',
    ultra_sigiloso: 'Ultra-sigiloso',
  };
  const tone = value === 'publico' ? 'ok' : value === 'restrito' ? 'warning' : 'danger';
  return <span className={`ouv-nivel-sigilo ouv-nivel-sigilo--${tone}`}>{labels[value] ?? value}</span>;
}

export function FormaRespostaBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    portal: 'Portal',
    email: 'E-mail',
    correios: 'Correios',
    presencial: 'Presencial',
    telefone: 'Telefone',
  };
  return <span className="ouv-forma-resposta">{labels[value] ?? value}</span>;
}

export function CanalBadge({ value }: { value: string }) {
  const labels: Record<string, string> = {
    portal_cidadao: 'Portal do Cidadão',
    presencial: 'Presencial',
    telefone: 'Telefone',
    email: 'E-mail',
    correios: 'Correios',
    aplicativo: 'Aplicativo',
    outro: 'Outro',
  };
  return <span className="ouv-canal">{labels[value] ?? value}</span>;
}
