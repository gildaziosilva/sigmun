import type { ReactNode } from 'react';
import type {
  DocumentoGDO,
  TramitacaoGDO,
  VersaoDocumentoGDO,
  ArquivamentoGDO,
  AssinaturaGDO,
  TipoDocumentalGDO,
  ClassificacaoDocumentalGDO,
  ProcessoDocumentoGDO,
  TabelaTemporalidadeGDO,
} from '../../lib/api';

export interface GdoDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export interface GdoResources {
  documentos: GdoDataState<{ items: DocumentoGDO[]; total: number; page: number; page_size: number }>;
  tramitacoes: GdoDataState<TramitacaoGDO[]>;
  versoes: GdoDataState<VersaoDocumentoGDO[]>;
  arquivamentos: GdoDataState<ArquivamentoGDO[]>;
  assinaturas: GdoDataState<AssinaturaGDO[]>;
  tiposDocumentais: GdoDataState<TipoDocumentalGDO[]>;
  classificacoes: GdoDataState<{ items: ClassificacaoDocumentalGDO[]; total: number; page: number; page_size: number }>;
  processos: GdoDataState<ProcessoDocumentoGDO[]>;
  temporalidades: GdoDataState<TabelaTemporalidadeGDO[]>;
  recarregar: () => void;
}

export type ExecutarGdo = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const GDO_TABS = [
  { id: 'documentos', rotulo: 'Documentos' },
  { id: 'tramitacoes', rotulo: 'Tramitações' },
  { id: 'versoes', rotulo: 'Versões' },
  { id: 'arquivamentos', rotulo: 'Arquivamentos' },
  { id: 'assinaturas', rotulo: 'Assinaturas' },
  { id: 'tipos-documentais', rotulo: 'Tipos Documentais' },
  { id: 'classificacoes', rotulo: 'Classificações' },
  { id: 'processos', rotulo: 'Processos' },
  { id: 'temporalidades', rotulo: 'Temporalidades' },
] as const;

export type GdoTab = (typeof GDO_TABS)[number]['id'];

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

export function StatusBadge({ value }: { value: string }) {
  const normalized = value.toLocaleLowerCase('pt-BR');
  const tone =
    ['ativo', 'confirmado', 'realizado', 'autorizada', 'arquivado', 'assinado', 'valido'].includes(normalized)
      ? 'ok'
      : ['cancelado', 'negada', 'falta', 'rejeitado', 'eliminado', 'revogada', 'inativo'].includes(normalized)
      ? 'danger'
      : ['solicitada', 'agendado', 'agendada', 'pendente', 'rascunho', 'em_analise'].includes(normalized)
      ? 'warning'
      : 'neutral';
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

export function documentoTitulo(resources: GdoResources, id: string): string {
  return resources.documentos.data?.items.find((d) => d.id === id)?.titulo ?? id;
}

export function tipoDocumentalNome(resources: GdoResources, id: string): string {
  return resources.tiposDocumentais.data?.find((t) => t.id === id)?.nome ?? id;
}