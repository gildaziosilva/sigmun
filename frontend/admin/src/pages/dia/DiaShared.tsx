import type { ReactNode } from 'react';
import type {
  ViagemDia,
  DiariaDia,
  PrestacaoContasDia,
} from '../../lib/api';

// ==================== Tipos de Estado ====================

export interface DiaDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export interface DiaResources {
  viagens: DiaDataState<ViagemDia[]>;
  diariasPorStatus: DiaDataState<DiariaDia[]>;
  prestacoesAbertas: DiaDataState<PrestacaoContasDia[]>;
  recarregar: () => void;
}

export type ExecutarDia = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

// ==================== Abas ====================

export const DIA_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'viagens', rotulo: 'Viagens' },
  { id: 'diarias', rotulo: 'Diárias' },
  { id: 'prestacoes', rotulo: 'Prestações de contas' },
] as const;
export type DiaTab = (typeof DIA_TABS)[number]['id'];

// ==================== Catálogos ====================

export const DIA_STATUS_DIARIA: readonly { value: string; label: string }[] = [
  { value: 'SOLICITADA', label: 'Solicitada' },
  { value: 'AUTORIZADA', label: 'Autorizada' },
  { value: 'CALCULADA', label: 'Calculada' },
  { value: 'CONCEDIDA', label: 'Concedida' },
  { value: 'EM_PRESTACAO', label: 'Em prestação' },
  { value: 'PAGA', label: 'Paga' },
  { value: 'APROVADA', label: 'Aprovada' },
  { value: 'GLOSA', label: 'Glosada' },
  { value: 'RESTITUIDA', label: 'Restituída' },
  { value: 'CANCELADA', label: 'Cancelada' },
] as const;

export const DIA_STATUS_PRESTACAO: readonly { value: string; label: string }[] = [
  { value: 'aberta', label: 'Aberta' },
  { value: 'aprovada', label: 'Aprovada' },
  { value: 'glosa', label: 'Glosada' },
  { value: 'restituida', label: 'Restituída' },
] as const;

// ==================== Formatação ====================

export function formatarData(valor?: string | null): string {
  if (!valor) return '—';
  const data = new Date(valor);
  if (Number.isNaN(data.getTime())) return valor;
  return data.toLocaleDateString('pt-BR');
}

export function formatarMoeda(valor: number | null | undefined): string {
  if (valor === null || valor === undefined) return '—';
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export function formatarPeriodo(inicio?: string | null, fim?: string | null): string {
  if (!inicio && !fim) return '—';
  if (inicio && fim) return `${formatarData(inicio)} até ${formatarData(fim)}`;
  return formatarData(inicio ?? fim);
}

// ==================== Badges ====================

function badgeTone(status: string): string {
  const upper = status.toUpperCase();
  if (upper === 'APROVADA' || upper === 'PAGA' || upper === 'RESTITUIDA') return 'ok';
  if (upper === 'GLOSA' || upper === 'CANCELADA') return 'danger';
  if (upper === 'SOLICITADA' || upper === 'EM_PRESTACAO' || status === 'aberta') return 'warn';
  if (upper === 'AUTORIZADA' || upper === 'CALCULADA' || upper === 'CONCEDIDA') return 'info';
  return 'neutral';
}

export function StatusDiariaBadge({ value }: { value: string }) {
  const label = DIA_STATUS_DIARIA.find((s) => s.value === value)?.label ?? value;
  const tone = badgeTone(value);
  return <span className={tone === 'neutral' ? 'badge' : `badge badge--${tone}`}>{label}</span>;
}

export function StatusPrestacaoBadge({ value }: { value: string }) {
  const label = DIA_STATUS_PRESTACAO.find((s) => s.value === value)?.label ?? value;
  const tone = badgeTone(value);
  return <span className={tone === 'neutral' ? 'badge' : `badge badge--${tone}`}>{label}</span>;
}

// ==================== Campos de formulário ====================

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

// ==================== Agregações para visão geral ====================

export interface DiaResumo {
  totalViagens: number;
  totalDiarias: number;
  valorTotal: number;
  prestacoesAbertas: number;
  valorGlosado: number;
  porStatus: Record<string, number>;
}

export function resumirDia(
  viagens: ViagemDia[],
  diarias: DiariaDia[],
  prestacoes: PrestacaoContasDia[],
): DiaResumo {
  const porStatus: Record<string, number> = {};
  let valorTotal = 0;
  let valorGlosado = 0;
  for (const d of diarias) {
    porStatus[d.status] = (porStatus[d.status] ?? 0) + 1;
    valorTotal += d.valor_total ?? 0;
    valorGlosado += d.valor_glosado ?? 0;
  }
  return {
    totalViagens: viagens.length,
    totalDiarias: diarias.length,
    valorTotal,
    prestacoesAbertas: prestacoes.length,
    valorGlosado,
    porStatus,
  };
}
