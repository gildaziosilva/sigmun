import type { ReactNode } from 'react';
import type { AgendamentoSau, MedicamentoSau, PacienteSau, RegulacaoSau } from '../../lib/api';

export interface SauDataState<T> { data: T | null; loading: boolean; erro: string; }
export interface SauResources {
  pacientes: SauDataState<PacienteSau[]>;
  agendamentos: SauDataState<AgendamentoSau[]>;
  regulacoes: SauDataState<RegulacaoSau[]>;
  medicamentos: SauDataState<MedicamentoSau[]>;
  recarregar: () => void;
}
export type ExecutarSau = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;
export const SAU_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'prontuario', rotulo: 'Prontuário' },
  { id: 'agenda', rotulo: 'Agendamento SUS' },
  { id: 'regulacao', rotulo: 'Regulação' },
  { id: 'farmacia', rotulo: 'Farmácia básica' },
] as const;
export type SauTab = (typeof SAU_TABS)[number]['id'];

export function Field(props: { label: string; value: string; onChange: (value: string) => void; children?: ReactNode; required?: boolean; hint?: string; type?: string; min?: string; max?: string; step?: string; placeholder?: string; }) {
  const { label, value, onChange, children, required, hint, type = 'text', min, max, step, placeholder } = props;
  return <label><span>{label}{required ? ' *' : ''}</span>{children ?? <input type={type} value={value} min={min} max={max} step={step} placeholder={placeholder} onChange={(event) => onChange(event.target.value)} required={required} />}{hint && <small>{hint}</small>}</label>;
}
export function StatusBadge({ value }: { value: string }) {
  const normalized = value.toLocaleLowerCase('pt-BR');
  const tone = ['ativo', 'confirmado', 'realizado', 'autorizada'].includes(normalized) ? 'ok' : ['cancelado', 'negada', 'falta', 'urgencia'].includes(normalized) ? 'danger' : ['solicitada', 'agendado', 'agendada'].includes(normalized) ? 'warning' : 'neutral';
  return <span className={`sau-status sau-status--${tone}`}>{value.replaceAll('_', ' ')}</span>;
}
export function formatarData(value?: string | null): string {
  if (!value) return '—';
  const date = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  return Number.isNaN(date.getTime()) ? value : new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(date);
}
export function formatarNumero(value: number): string {
  return new Intl.NumberFormat('pt-BR').format(value);
}

export function pacienteNome(resources: SauResources, id: string): string {
  return resources.pacientes.data?.find((paciente) => paciente.id === id)?.nome ?? id;
}
