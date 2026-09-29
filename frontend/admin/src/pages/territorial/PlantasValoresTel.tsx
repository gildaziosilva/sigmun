import { useState } from 'react';
import type { PlantaValoresTel, PlantaValoresTelCreate } from '../../lib/api';
import {
  ativarPlantaValoresTel,
  criarPlantaValoresTel,
  revogarPlantaValoresTel,
} from '../../lib/api';
import type { TelResources } from './TelPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  OCUPACOES,
  SelectTerr,
  StatusTerr,
  bairroNome,
  formatarDataTerr,
  formatarMoedaTerr,
  formatarNumeroTerr,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: TelResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const ANO_ATUAL = new Date().getFullYear();

const FORM_VAZIO: PlantaValoresTelCreate = {
  ano: ANO_ATUAL,
  bairro_id: '',
  ocupacao: 'residencial',
  valor_terreno_m2: 0,
  valor_construcao_m2: 0,
  aliquota_percent: 0,
  legislacao: '',
  ativar: false,
};

export function PlantasValoresTel({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<PlantaValoresTelCreate>({ ...FORM_VAZIO });
  const [ano, setAno] = useState(String(ANO_ATUAL));
  const [vTerreno, setVTerreno] = useState('0');
  const [vConstrucao, setVConstrucao] = useState('0');
  const [aliquota, setAliquota] = useState('0');
  const [filtroSituacao, setFiltroSituacao] = useState('');

  const bairros = resources.bairros.data ?? [];
  const plantas = resources.plantas.data ?? [];
  const opcoesBairro = bairros.map((b) => ({ valor: b.id, rotulo: `${b.codigo} — ${b.nome}` }));

  const filtradas = plantas.filter((p) => filtroSituacao === '' || p.situacao === filtroSituacao);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: PlantaValoresTelCreate = {
      ano: paraNumero(ano, ANO_ATUAL),
      bairro_id: form.bairro_id,
      ocupacao: form.ocupacao,
      valor_terreno_m2: paraNumero(vTerreno),
      valor_construcao_m2: paraNumero(vConstrucao),
      aliquota_percent: paraNumero(aliquota),
      legislacao: form.legislacao ?? '',
      ativar: form.ativar ?? false,
    };
    const ok = await executar(
      () => criarPlantaValoresTel(payload),
      payload.ativar
        ? 'Planta genérica de valores criada e ativada!'
        : 'Planta genérica de valores criada em rascunho!',
    );
    if (ok) {
      setForm({ ...FORM_VAZIO });
      setVTerreno('0');
      setVConstrucao('0');
      setAliquota('0');
    }
  }

  async function handleAtivar(planta: PlantaValoresTel) {
    if (!window.confirm(`Ativar a planta de ${planta.ano} (${planta.ocupacao})?`)) return;
    await executar(() => ativarPlantaValoresTel(planta.id), 'Planta ativada com sucesso!');
  }

  async function handleRevogar(planta: PlantaValoresTel) {
    const justificativa = window.prompt(
      `Justificativa obrigatória para revogar a planta de ${planta.ano} (RN-TEL-004):`,
    );
    if (!justificativa) return;
    await executar(
      () => revogarPlantaValoresTel(planta.id, justificativa),
      'Planta revogada com sucesso!',
    );
  }

  return (
    <section className="stack terr-plantas">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>Cadastrar planta genérica de valores</h3>
        <p className="muted">
          A planta define os valores unitários por ano, bairro e ocupação. Após a ativação, ela é
          a referência para o cálculo do valor venal no DOM-IMO.
        </p>
        <div className="form-grid">
          <FieldTerr label="Ano de vigência" value={ano} onChange={setAno} type="number" min="1900" max="2200" step="1" required />
          <SelectTerr
            label="Bairro"
            value={form.bairro_id}
            opcoes={opcoesBairro}
            onChange={(v) => setForm({ ...form, bairro_id: v })}
            required
            vazio="Selecione..."
          />
          <SelectTerr
            label="Ocupação"
            value={form.ocupacao ?? 'residencial'}
            opcoes={OCUPACOES}
            onChange={(v) => setForm({ ...form, ocupacao: v })}
            required
          />
          <FieldTerr label="Valor do terreno (R$/m²)" value={vTerreno} onChange={setVTerreno} type="number" min="0" step="0.01" required />
          <FieldTerr label="Valor da construção (R$/m²)" value={vConstrucao} onChange={setVConstrucao} type="number" min="0" step="0.01" required />
          <FieldTerr label="Alíquota (%)" value={aliquota} onChange={setAliquota} type="number" min="0" max="100" step="0.01" />
          <FieldTerr label="Legislação" value={form.legislacao ?? ''} onChange={(v) => setForm({ ...form, legislacao: v })} placeholder="Lei Municipal 1.234/2026" />
          <label>
            <span>Ativar imediatamente</span>
            <input
              type="checkbox"
              checked={form.ativar ?? false}
              onChange={(e) => setForm({ ...form, ativar: e.target.checked })}
            />
            <small>Somente uma planta vigente por ano, bairro e ocupação (RN-TEL-003)</small>
          </label>
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {form.ativar ? 'Criar e ativar' : 'Criar em rascunho'}
          </button>
        </div>
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Plantas cadastradas ({filtradas.length} de {plantas.length})</h3>
          <select value={filtroSituacao} onChange={(e) => setFiltroSituacao(e.target.value)} className="terr-search">
            <option value="">Todas as situações</option>
            <option value="rascunho">Rascunho</option>
            <option value="vigente">Vigente</option>
            <option value="revogada">Revogada</option>
          </select>
        </div>
        {filtradas.length === 0 ? (
          <p className="muted">Nenhuma planta genérica de valores cadastrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Ano</th>
                <th>Bairro</th>
                <th>Ocupação</th>
                <th className="num">Terreno</th>
                <th className="num">Construção</th>
                <th className="num">Alíquota</th>
                <th>Situação</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {filtradas.map((p) => (
                <tr key={p.id}>
                  <td>{p.ano}</td>
                  <td>{bairroNome(bairros, p.bairro_id)}</td>
                  <td>{p.ocupacao}</td>
                  <td className="num">{formatarMoedaTerr(p.valor_terreno_m2)}</td>
                  <td className="num">{formatarMoedaTerr(p.valor_construcao_m2)}</td>
                  <td className="num">{formatarNumeroTerr(p.aliquota_percent, 2)}%</td>
                  <td><StatusTerr value={p.situacao} /></td>
                  <td>
                    {p.situacao === 'rascunho' && (
                      <>
                        <button type="button" className="button button--sm" onClick={() => handleAtivar(p)} disabled={salvando}>
                          Ativar
                        </button>{' '}
                      </>
                    )}
                    {p.situacao === 'vigente' && (
                      <button type="button" className="button button--danger button--sm" onClick={() => handleRevogar(p)} disabled={salvando}>
                        Revogar
                      </button>
                    )}
                    {p.situacao === 'revogada' && (
                      <span className="muted" title={p.legislacao ?? ''}>
                        {p.legislacao ? formatarDataTerr(p.updated_at) : '—'}
                      </span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}

