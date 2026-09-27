import type { ReactNode } from 'react';
import type {
  AlunoEdu,
  MatriculaEdu,
  LancamentoDiarioEdu,
  RotaTransporteEdu,
  PassagemTransporteEdu,
  ItemMerendaEdu,
  DistribuicaoMerendaEdu,
} from '../../lib/api';


export interface EduDataState<T> { data: T | null; loading: boolean; erro: string; }

export interface EduResources {
  alunos: EduDataState<AlunoEdu[]>;
  matriculas: EduDataState<MatriculaEdu[]>;
  lancamentos: EduDataState<LancamentoDiarioEdu[]>;
  rotas: EduDataState<RotaTransporteEdu[]>;
  passagens: EduDataState<PassagemTransporteEdu[]>;
  itensMerenda: EduDataState<ItemMerendaEdu[]>;
  distribuicoes: EduDataState<DistribuicaoMerendaEdu[]>;
  recarregar: () => void;
}

export type ExecutarEdu = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const EDU_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'alunos', rotulo: 'Alunos' },
  { id: 'matriculas', rotulo: 'Matrículas' },
  { id: 'diario', rotulo: 'Diário de Classe' },
  { id: 'transporte', rotulo: 'Transporte Escolar' },
  { id: 'merenda', rotulo: 'Merenda Escolar' },
] as const;
export type EduTab = (typeof EDU_TABS)[number]['id'];


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
      {children ?? <input type={type} value={value} min={min} max={max} step={step} placeholder={placeholder} onChange={(event) => onChange(event.target.value)} required={required} />}
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function StatusBadge({ value }: { value: string }) {
  const normalized = value.toLocaleLowerCase('pt-BR');
  const tone = ['ativo', 'ativa', 'confirmado', 'realizado', 'autorizada'].includes(normalized) ? 'ok' : ['cancelado', 'negada', 'falta', 'urgencia'].includes(normalized) ? 'danger' : ['solicitada', 'agendado', 'agendada', 'inativa'].includes(normalized) ? 'warning' : 'neutral';
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
