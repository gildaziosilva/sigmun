import type { ReactNode } from 'react';
import type { CamadaGeo, MapaCamadaGeo, MapaSigGeo, ServicoGeo, FeatureGeo } from '../../lib/api';

export type {
  CamadaGeo,
  MapaSigGeo,
  MapaCamadaGeo,
  FeatureGeo,
  ServicoGeo,
};

export interface GeoDataState<T> {
  data: T | null;
  loading: boolean;
  erro: string;
}

export type ExecutarGeo = (acao: () => Promise<unknown>, sucesso: string) => Promise<boolean>;

export const TIPOS_CAMADA = [
  { valor: 'ortofoto', rotulo: 'Ortofoto' },
  { valor: 'hipsometria', rotulo: 'Hipsometria' },
  { valor: 'hipsografia', rotulo: 'Hipsografia' },
  { valor: 'topografia', rotulo: 'Topografia' },
  { valor: 'hidrografia', rotulo: 'Hidrografia' },
  { valor: 'uso_solo', rotulo: 'Uso do solo' },
  { valor: 'vegetacao', rotulo: 'Vegetacao' },
  { valor: 'malha_urbana', rotulo: 'Malha urbana' },
  { valor: 'infraestrutura', rotulo: 'Infraestrutura' },
  { valor: 'cadastro_territorial', rotulo: 'Cadastro territorial' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const FORMATOS_CAMADA = [
  { valor: 'geotiff', rotulo: 'GeoTIFF' },
  { valor: 'shapefile', rotulo: 'Shapefile' },
  { valor: 'geojson', rotulo: 'GeoJSON' },
  { valor: 'kml', rotulo: 'KML' },
  { valor: 'postgis', rotulo: 'PostGIS' },
  { valor: 'wms', rotulo: 'WMS' },
  { valor: 'wfs', rotulo: 'WFS' },
  { valor: 'wmts', rotulo: 'WMTS' },
  { valor: 'xyz', rotulo: 'XYZ' },
  { valor: 'vetorial', rotulo: 'Vetorial' },
];

/** Formatos de serviço que exigem URL na publicação (RN-GEO-006). */
export const FORMATOS_SERVICO = new Set(['wms', 'wfs', 'wmts', 'xyz']);

export const DATUMS = [
  { valor: 'sirgas2000', rotulo: 'SIRGAS 2000' },
  { valor: 'sad69', rotulo: 'SAD 69' },
  { valor: 'wgs84', rotulo: 'WGS 84' },
];

export const TIPOS_MAPA = [
  { valor: 'tematico', rotulo: 'Tematico' },
  { valor: 'cadastral', rotulo: 'Cadastral' },
  { valor: 'basemap', rotulo: 'Basemap' },
  { valor: 'infraestrutura', rotulo: 'Infraestrutura' },
  { valor: 'ambiental', rotulo: 'Ambiental' },
  { valor: 'outro', rotulo: 'Outro' },
];

export const TIPOS_SERVICO = [
  { valor: 'wms', rotulo: 'WMS' },
  { valor: 'wfs', rotulo: 'WFS' },
  { valor: 'wmts', rotulo: 'WMTS' },
  { valor: 'xyz', rotulo: 'XYZ' },
  { valor: 'rest', rotulo: 'REST' },
];

export const GEOMETRIAS = [
  { valor: 'ponto', rotulo: 'Ponto', minimo: 1 },
  { valor: 'linha', rotulo: 'Linha', minimo: 2 },
  { valor: 'poligono', rotulo: 'Poligono', minimo: 3 },
];

/** Tons do selo de situacao, por valor de dominio. */
const TONS: Record<string, 'ok' | 'warning' | 'danger' | 'info' | 'neutral'> = {
  ativo: 'ok',
  ativa: 'ok',
  publicado: 'ok',
  aprovada: 'ok',
  concluida: 'ok',
  em_execucao: 'warning',
  em_licitacao: 'warning',
  em_andamento: 'warning',
  rascunho: 'warning',
  registrada: 'warning',
  conferida: 'warning',
  desativada: 'neutral',
  inativo: 'neutral',
  arquivado: 'neutral',
  glosada: 'danger',
  cancelada: 'danger',
  reprovado: 'danger',
};

export function StatusGeo({ value }: { value: string }) {
  const normalizado = value.toLocaleLowerCase('pt-BR');
  const tom = TONS[normalizado] ?? 'neutral';
  return <span className={`geo-status geo-status--${tom}`}>{value.replaceAll('_', ' ')}</span>;
}

export function FieldGeo(props: {
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

export function SelectGeo(props: {
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

export function formatarDataGeo(value?: string | null): string {
  if (!value) return '—';
  const data = new Date(value.length === 10 ? `${value}T00:00:00` : value);
  if (Number.isNaN(data.getTime())) return value;
  return new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short' }).format(data);
}

export function paraNumeroGeo(valor: string): number {
  const convertido = Number(valor.replace(',', '.'));
  return Number.isFinite(convertido) ? convertido : 0;
}
