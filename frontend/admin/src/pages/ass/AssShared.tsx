import type { ReactNode } from 'react';
import type { FamiliaAss, FamiliaAssCreate, PessoaAss, PessoaAssCreate, UnidadeAss, UnidadeAssCreate, BeneficioAss, BeneficioAssCreate, AtendimentoAss, AtendimentoAssCreate } from '../../lib/api';

export type { FamiliaAss, FamiliaAssCreate, PessoaAss, PessoaAssCreate, UnidadeAss, UnidadeAssCreate, BeneficioAss, BeneficioAssCreate, AtendimentoAss, AtendimentoAssCreate };

export interface AssDataState<T> { data: T | null; loading: boolean; erro: string; }

export interface AssResources {
  familias: AssDataState<FamiliaAss[]>;
  pessoas: AssDataState<PessoaAss[]>;
  unidades: AssDataState<UnidadeAss[]>;
  beneficios: AssDataState<BeneficioAss[]>;
  atendimentos: AssDataState<AtendimentoAss[]>;
  recarregar: () => void;
}

export type ExecutarAss = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const ASS_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'familias', rotulo: 'Famílias (CadÚnico)' },
  { id: 'pessoas', rotulo: 'Pessoas' },
  { id: 'unidades', rotulo: 'Unidades CRAS/CREAS' },
  { id: 'beneficios', rotulo: 'Benefícios Eventuais' },
  { id: 'atendimentos', rotulo: 'Atendimentos Sociais' },
] as const;

export type AssTab = (typeof ASS_TABS)[number]['id'];

export function Field(props: { label: string; value: string; onChange: (value: string) => void; children?: ReactNode; required?: boolean; hint?: string; type?: string; min?: string; max?: string; step?: string; placeholder?: string; pattern?: string; }) {
  const { label, value, onChange, children, required, hint, type = 'text', min, max, step, placeholder, pattern } = props;
  return <label><span>{label}{required ? ' *' : ''}</span>{children ?? <input type={type} value={value} min={min} max={max} step={step} placeholder={placeholder} pattern={pattern} onChange={(event) => onChange(event.target.value)} required={required} />}{hint && <small>{hint}</small>}</label>;
}

export function StatusBadge({ value }: { value: string }) {
  const normalized = value.toLocaleLowerCase('pt-BR');
  const tone = ['ativa', 'ativo', 'aprovado', 'entregue', 'realizado'].includes(normalized) ? 'ok' : ['cancelado', 'negado', 'inativa', 'excluida'].includes(normalized) ? 'danger' : ['solicitado', 'pendente'].includes(normalized) ? 'warning' : 'neutral';
  return <span className={`ass-status ass-status--${tone}`}>{value.replaceAll('_', ' ')}</span>;
}

export function formatarData(value?: string | null): string {
  if (!value) return '—';
  const date = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  return Number.isNaN(date.getTime()) ? value : new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(date);
}

export function formatarNumero(value: number): string {
  return new Intl.NumberFormat('pt-BR').format(value);
}

export function formatarMoeda(value: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

export function familiaNome(resources: AssResources, id: string): string {
  return resources.familias.data?.find((f) => f.id === id)?.responsavel_nome ?? id;
}

export function pessoaNome(resources: AssResources, id: string): string {
  return resources.pessoas.data?.find((p) => p.id === id)?.nome ?? id;
}

export function unidadeNome(resources: AssResources, id: string): string {
  return resources.unidades.data?.find((u) => u.id === id)?.nome ?? id;
}