import type { ReactNode } from 'react';
import type {
  BairroTel,
  LogradouroTel,
  PlantaValoresTel,
  GeorreferenciaTel,
  ImovelImo,
  ProprietarioImo,
  AvaliacaoImo,
  CaracteristicaImo,
  GeometriaImo,
} from '../../lib/api';

export type {
  BairroTel,
  LogradouroTel,
  PlantaValoresTel,
  GeorreferenciaTel,
  ImovelImo,
  ProprietarioImo,
  AvaliacaoImo,
  CaracteristicaImo,
  GeometriaImo,
};

export interface TerrDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export type ExecutarTerr = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const TIPOS_BAIRRO = [
  { valor: 'bairro', rotulo: 'Bairro' },
  { valor: 'distrito', rotulo: 'Distrito' },
  { valor: 'setor', rotulo: 'Setor' },
  { valor: 'zona_rural', rotulo: 'Zona rural' },
];

export const TIPOS_LOGRADOURO = [
  { valor: 'rua', rotulo: 'Rua' },
  { valor: 'avenida', rotulo: 'Avenida' },
  { valor: 'travessa', rotulo: 'Travessa' },
  { valor: 'praca', rotulo: 'Praça' },
  { valor: 'rodovia', rotulo: 'Rodovia' },
  { valor: 'estrada', rotulo: 'Estrada' },
  { valor: 'alameda', rotulo: 'Alameda' },
  { valor: 'parque', rotulo: 'Parque' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const OCUPACOES = [
  { valor: 'residencial', rotulo: 'Residencial' },
  { valor: 'comercial', rotulo: 'Comercial' },
  { valor: 'industrial', rotulo: 'Industrial' },
  { valor: 'institucional', rotulo: 'Institucional' },
  { valor: 'misto', rotulo: 'Misto' },
  { valor: 'terreno', rotulo: 'Terreno' },
];

export const TIPOS_IMOVEL = [
  { valor: 'lote', rotulo: 'Lote' },
  { valor: 'casa', rotulo: 'Casa' },
  { valor: 'apartamento', rotulo: 'Apartamento' },
  { valor: 'loja', rotulo: 'Loja' },
  { valor: 'galpao', rotulo: 'Galpão' },
  { valor: 'terreno', rotulo: 'Terreno' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const SITUACOES_IMOVEL = [
  { valor: 'ativo', rotulo: 'Ativo' },
  { valor: 'inativo', rotulo: 'Inativo' },
  { valor: 'em_obra', rotulo: 'Em obra' },
  { valor: 'desocupado', rotulo: 'Desocupado' },
  { valor: 'demolido', rotulo: 'Demolido' },
];

export const TIPOS_VINCULO = [
  { valor: 'titular', rotulo: 'Titular' },
  { valor: 'parceiro', rotulo: 'Parceiro' },
  { valor: 'comodato', rotulo: 'Comodato' },
  { valor: 'arrendamento', rotulo: 'Arrendamento' },
  { valor: 'usufruto', rotulo: 'Usufruto' },
];

/** Campos de status do domínio territorial e imobiliário, por tom do selo. */
const TONS: Record<string, 'ok' | 'warning' | 'danger' | 'info' | 'neutral'> = {
  ativo: 'ok',
  ativa: 'ok',
  vigente: 'ok',
  concluida: 'ok',
  em_obra: 'warning',
  rascunho: 'warning',
  em_andamento: 'warning',
  inativo: 'neutral',
  demolido: 'danger',
  revogada: 'danger',
  cancelada: 'danger',
};

export function StatusTerr({ value }: { value: string }) {
  const normalizado = value.toLocaleLowerCase('pt-BR');
  const tom = TONS[normalizado] ?? 'neutral';
  return <span className={`terr-status terr-status--${tom}`}>{value.replaceAll('_', ' ')}</span>;
}


export function FieldTerr(props: {
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
  pattern?: string;
}) {
  const { label, value, onChange, children, required, hint, type = 'text', min, max, step, placeholder, readOnly, pattern } = props;
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
          readOnly={readOnly}
          pattern={pattern}
          onChange={(event) => onChange(event.target.value)}
          required={required}
        />
      )}
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function SelectTerr(props: {
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
      <span>{label}{required ? ' *' : ''}</span>
      <select value={value} onChange={(event) => onChange(event.target.value)} required={required}>
        {vazio !== undefined && <option value="">{vazio}</option>}
        {opcoes.map((o) => (
          <option key={o.valor} value={o.valor}>{o.rotulo}</option>
        ))}
      </select>
      {hint && <small>{hint}</small>}
    </label>
  );
}

export function formatarDataTerr(value?: string | null): string {
  if (!value) return '—';
  const data = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  if (Number.isNaN(data.getTime())) return value;
  return new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(data);
}

export function formatarMoedaTerr(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export function formatarNumeroTerr(valor: number, casas = 0): string {
  return new Intl.NumberFormat('pt-BR', {
    minimumFractionDigits: casas,
    maximumFractionDigits: casas,
  }).format(valor);
}

/**
 * Resolve um nome a partir de uma lista. Aceita objetos parciais porque as
 * telas carregam projeções enxutas (apenas `id` e `nome`) do território.
 */
function nomePorId(
  lista: readonly { id: string; nome?: string | null }[],
  id: string,
  padrao: string,
): string {
  return lista.find((item) => item.id === id)?.nome || padrao;
}

/** Resolve o nome de um bairro a partir do id (usado nos cadastros). */
export function bairroNome(bairros: readonly { id: string; nome?: string | null }[], id: string): string {
  return nomePorId(bairros, id, '(não informado)');
}

/** Resolve o nome de um logradouro a partir do id. */
export function logradouroNome(
  logradouros: readonly { id: string; nome?: string | null }[],
  id: string,
): string {
  return nomePorId(logradouros, id, '(não informado)');
}

/** Resolve a inscrição imobiliária a partir do id do imóvel. */
export function imovelInscricao(imoveis: ImovelImo[], id: string): string {
  const encontrado = imoveis.find((i) => i.id === id);
  return encontrado?.inscricao_imobiliaria || '(sem imóvel)';
}

/** Converte um valor numérico digitado em número, tolerando texto vazio. */
export function paraNumero(valor: string, padrao = 0): number {
  if (!valor.trim()) return padrao;
  const n = Number(valor.replace(',', '.'));
  return Number.isFinite(n) ? n : padrao;
}

/** Barra de progresso para os indicadores de cobertura cadastral. */
export function Progresso({ valor }: { valor: number }) {
  const pct = Math.max(0, Math.min(100, Math.round(valor)));
  return (
    <span
      style={{ display: 'block', minWidth: '8rem', height: '0.5rem', background: '#e6ebf2', borderRadius: '999px' }}
      role="progressbar"
      aria-valuenow={pct}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label={`${pct}% de cobertura`}
    >
      <span
        style={{
          display: 'block',
          width: `${pct}%`,
          height: '100%',
          background: pct === 100 ? '#126843' : '#1f5d4c',
          borderRadius: '999px',
        }}
      />
    </span>
  );
}

/** Percentual de imóveis com geometria georreferenciada. */
export function coberturaGeometria(total: number, geometrias: GeometriaImo[]): number {
  if (total === 0) return 0;
  return (new Set(geometrias.map((g) => g.imovel_id)).size / total) * 100;
}

/** Percentual de imóveis com característica construtiva registrada. */
export function coberturaCaracteristica(total: number, caracteristicas: CaracteristicaImo[]): number {
  if (total === 0) return 0;
  return (new Set(caracteristicas.map((c) => c.imovel_id)).size / total) * 100;
}

/** Percentual de imóveis com proprietário titular definido. */
export function coberturaTitular(total: number, proprietarios: ProprietarioImo[]): number {
  if (total === 0) return 0;
  const titulares = new Set(
    proprietarios.filter((p) => p.principal).map((p) => p.imovel_id),
  );
  return (titulares.size / total) * 100;
}

/** Percentual de imóveis avaliados no exercício corrente. */
export function coberturaAvaliacao(total: number, avaliacoes: AvaliacaoImo[]): number {
  if (total === 0) return 0;
  const ano = new Date().getFullYear();
  const avaliados = new Set(
    avaliacoes.filter((a) => a.ano === ano).map((a) => a.imovel_id),
  );
  return (avaliados.size / total) * 100;
}

