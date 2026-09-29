import type { ReactNode } from 'react';
import type {
  DespesaObra,
  EtapaObra,
  MedicaoObra,
  Obra,
  VistoriaObra,
} from '../../lib/api';

export type { Obra, MedicaoObra, DespesaObra, EtapaObra, VistoriaObra };

export interface ObrasDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export type ExecutarObras = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const TIPOS_OBRA = [
  { valor: 'pavimentacao', rotulo: 'Pavimentacao' },
  { valor: 'drenagem', rotulo: 'Drenagem' },
  { valor: 'construcao', rotulo: 'Construcao' },
  { valor: 'reforma', rotulo: 'Reforma' },
  { valor: 'iluminacao', rotulo: 'Iluminacao' },
  { valor: 'saneamento', rotulo: 'Saneamento' },
  { valor: 'ponte', rotulo: 'Ponte' },
  { valor: 'praca', rotulo: 'Praca' },
  { valor: 'quadra', rotulo: 'Quadra' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const SITUACOES_OBRA = [
  { valor: 'planejada', rotulo: 'Planejada' },
  { valor: 'em_licitacao', rotulo: 'Em licitacao' },
  { valor: 'contratada', rotulo: 'Contratada' },
  { valor: 'em_execucao', rotulo: 'Em execucao' },
  { valor: 'suspensa', rotulo: 'Suspensa' },
  { valor: 'concluida', rotulo: 'Concluida' },
  { valor: 'cancelada', rotulo: 'Cancelada' },
];

export const FONTES_RECURSO = [
  { valor: 'orcamento_proprio', rotulo: 'Orcamento proprio' },
  { valor: 'convenio', rotulo: 'Convenio' },
  { valor: 'convenio_estadual', rotulo: 'Convenio estadual' },
  { valor: 'convenio_federal', rotulo: 'Convenio federal' },
  { valor: 'transferencia', rotulo: 'Transferencia' },
  { valor: 'operacao_credito', rotulo: 'Operacao de credito' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const TIPOS_CONTRATACAO = [
  { valor: 'licitacao', rotulo: 'Licitacao' },
  { valor: 'dispensa', rotulo: 'Dispensa' },
  { valor: 'inexigibilidade', rotulo: 'Inexigibilidade' },
  { valor: 'convenio', rotulo: 'Convenio' },
  { valor: 'contrato_direto', rotulo: 'Contrato direto' },
];

export const TIPOS_MEDICAO = [
  { valor: 'avanco', rotulo: 'Avanco' },
  { valor: 'etapa', rotulo: 'Etapa' },
  { valor: 'final', rotulo: 'Medicao final' },
  { valor: 'revisional', rotulo: 'Revisional' },
];

export const TIPOS_DESPESA = [
  { valor: 'medicao', rotulo: 'Medicao' },
  { valor: 'repasse', rotulo: 'Repasse' },
  { valor: 'material', rotulo: 'Material' },
  { valor: 'mao_de_obra', rotulo: 'Mao de obra' },
  { valor: 'tributos', rotulo: 'Tributos' },
  { valor: 'custos', rotulo: 'Custos' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const TIPOS_ETAPA = [
  { valor: 'projeto', rotulo: 'Projeto' },
  { valor: 'terraplanagem', rotulo: 'Terraplanagem' },
  { valor: 'fundacao', rotulo: 'Fundacao' },
  { valor: 'estrutura', rotulo: 'Estrutura' },
  { valor: 'acabamento', rotulo: 'Acabamento' },
  { valor: 'instalacao', rotulo: 'Instalacao' },
  { valor: 'pavimentacao', rotulo: 'Pavimentacao' },
  { valor: 'paisagismo', rotulo: 'Paisagismo' },
  { valor: 'recepcao', rotulo: 'Recepcao' },
];

export const TIPOS_VISTORIA = [
  { valor: 'periodica', rotulo: 'Periodica' },
  { valor: 'parcial', rotulo: 'Parcial' },
  { valor: 'final', rotulo: 'Final' },
  { valor: 'recepcao', rotulo: 'Recepcao' },
];

export const PARECERES_VISTORIA = [
  { valor: 'aprovado', rotulo: 'Aprovado' },
  { valor: 'aprovado_com_ressalvas', rotulo: 'Aprovado com ressalvas' },
  { valor: 'reprovado', rotulo: 'Reprovado' },
];

/** Tons do selo de situacao, por valor de dominio. */
const TONS: Record<string, 'ok' | 'warning' | 'danger' | 'info' | 'neutral'> = {
  ativa: 'ok',
  concluida: 'ok',
  em_execucao: 'warning',
  em_licitacao: 'warning',
  em_andamento: 'warning',
  registrada: 'warning',
  conferida: 'warning',
  pendente: 'warning',
  planejada: 'neutral',
  contratada: 'neutral',
  suspensa: 'warning',
  atrasada: 'danger',
  glosada: 'danger',
  cancelada: 'danger',
  reprovado: 'danger',
};

export function StatusObras({ value }: { value: string }) {
  const normalizado = value.toLocaleLowerCase('pt-BR');
  const tom = TONS[normalizado] ?? 'neutral';
  return <span className={`obras-status obras-status--${tom}`}>{value.replaceAll('_', ' ')}</span>;
}

export function FieldObras(props: {
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
  readOnly?: boolean;
}) {
  const {
    label,
    value,
    onChange,
    children,
    required,
    hint,
    type = 'text',
    min,
    max,
    step,
    placeholder,
    readOnly,
  } = props;
  return (
    <label>
      <span>
        {label}
        {required ? ' *' : ''}
      </span>
      {children ?? (
        <input
          type={type}
          value={value}
          min={min}
          max={max}
          step={step}
          placeholder={placeholder}
          readOnly={readOnly}
          onChange={(event) => onChange(event.target.value)}
          required={required}
        />
      )}
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function SelectObras(props: {
  label: string;
  value: string;
  opcoes: { valor: string; rotulo: string }[];
  onChange: (value: string) => void;
  required?: boolean;
  vazio?: string;
  hint?: string;
}) {
  const { label, value, opcoes, onChange, required, vazio, hint } = props;
  return (
    <label>
      <span>
        {label}
        {required ? ' *' : ''}
      </span>
      <select value={value} onChange={(event) => onChange(event.target.value)} required={required}>
        {vazio !== undefined && <option value="">{vazio}</option>}
        {opcoes.map((o) => (
          <option key={o.valor} value={o.valor}>
            {o.rotulo}
          </option>
        ))}
      </select>
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function formatarDataObras(value?: string | null): string {
  if (!value) return '—';
  const data = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  if (Number.isNaN(data.getTime())) return value;
  return new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(data);
}

export function formatarMoedaObras(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export function paraNumeroObras(valor: string): number {
  const convertido = Number(valor.replace(',', '.'));
  return Number.isFinite(convertido) ? convertido : 0;
}
