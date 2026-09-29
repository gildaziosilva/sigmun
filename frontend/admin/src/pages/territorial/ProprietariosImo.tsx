import { useState } from 'react';
import type { ProprietarioImo, ProprietarioImoCreate } from '../../lib/api';
import { removerProprietarioImo, vincularProprietarioImo } from '../../lib/api';
import type { ImoResources } from './ImoPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  StatusTerr,
  TIPOS_VINCULO,
  formatarDataTerr,
  imovelInscricao,
} from './TerrShared';

interface Props {
  resources: ImoResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const FORM_VAZIO: ProprietarioImoCreate = {
  imovel_id: '',
  nome: '',
  cpf: '',
  pessoa_id: '',
  vinculo: 'titular',
  principal: false,
};

export function ProprietariosImo({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<ProprietarioImoCreate>({ ...FORM_VAZIO });
  const [pesquisa, setPesquisa] = useState('');
  const [filtroImovel, setFiltroImovel] = useState('');

  const imoveis = resources.imoveis.data ?? [];
  const proprietarios = resources.proprietarios.data ?? [];
  const opcoesImovel = imoveis.map((i) => ({
    valor: i.id,
    rotulo: `${i.inscricao_imobiliaria} — ${i.numero || 's/n'}`,
  }));

  const filtrados = proprietarios.filter(
    (p) =>
      (filtroImovel === '' || p.imovel_id === filtroImovel) &&
      (p.nome.toLowerCase().includes(pesquisa.toLowerCase()) ||
        p.cpf.includes(pesquisa)),
  );

  /** Identifica o imóvel pelo CPF/inscrição quando o usuário digita a inscrição. */
  function resolverImovel(valor: string): string {
    const porId = imoveis.find((i) => i.id === valor);
    if (porId) return porId.id;
    return imoveis.find((i) => i.inscricao_imobiliaria === valor)?.id ?? valor;
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: ProprietarioImoCreate = {
      ...form,
      imovel_id: resolverImovel(form.imovel_id),
    };
    const ok = await executar(
      () => vincularProprietarioImo(payload),
      'Proprietário vinculado com sucesso!',
    );
    if (ok) setForm({ ...FORM_VAZIO });
  }

  async function handleRemover(proprietario: ProprietarioImo) {
    if (!window.confirm(`Remover o vínculo de ${proprietario.nome} (${proprietario.cpf})?`)) return;
    await executar(
      () => removerProprietarioImo(proprietario.id),
      'Vínculo de propriedade removido com sucesso!',
    );
  }


  return (
    <section className="stack terr-proprietarios">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>Vincular proprietário ao imóvel</h3>
        <p className="muted">
          Cada imóvel admite no máximo um proprietário <strong>titular principal</strong> (RN-IMO-006).
          O documento aceita CPF (11 dígitos) ou CNPJ (14 dígitos).
        </p>
        <div className="form-grid">
          <SelectTerr
            label="Imóvel"
            value={form.imovel_id}
            opcoes={opcoesImovel}
            onChange={(v) => setForm({ ...form, imovel_id: v })}
            required
            vazio="Selecione..."
          />
          <FieldTerr label="Nome" value={form.nome} onChange={(v) => setForm({ ...form, nome: v })} required />
          <FieldTerr
            label="CPF / CNPJ"
            value={form.cpf}
            onChange={(v) => setForm({ ...form, cpf: v })}
            required
            pattern="\d{11,14}"
            hint="Somente dígitos: 11 (CPF) ou 14 (CNPJ)"
          />
          <SelectTerr
            label="Vínculo"
            value={form.vinculo ?? 'titular'}
            opcoes={TIPOS_VINCULO}
            onChange={(v) => setForm({ ...form, vinculo: v })}
            required
          />
          <label>
            <span>Titular principal</span>
            <input
              type="checkbox"
              checked={form.principal ?? false}
              onChange={(e) => setForm({ ...form, principal: e.target.checked })}
            />
            <small>Somente vínculos do tipo titular podem ser principais (RN-IMO-006)</small>
          </label>
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Vincular proprietário
          </button>
        </div>
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Vínculos cadastrados ({filtrados.length} de {proprietarios.length})</h3>
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            <select value={filtroImovel} onChange={(e) => setFiltroImovel(e.target.value)} className="terr-search">
              <option value="">Todos os imóveis</option>
              {imoveis.map((i) => (
                <option key={i.id} value={i.id}>{i.inscricao_imobiliaria}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Filtrar por nome ou CPF..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
              className="terr-search"
            />
          </div>
        </div>
        {filtrados.length === 0 ? (
          <p className="muted">Nenhum proprietário vinculado.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Imóvel</th>
                <th>Nome</th>
                <th>CPF / CNPJ</th>
                <th>Vínculo</th>
                <th>Principal</th>
                <th>Vinculado em</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {filtrados.map((p) => (
                <tr key={p.id}>
                  <td>{imovelInscricao(imoveis, p.imovel_id)}</td>
                  <td>{p.nome}</td>
                  <td>{p.cpf}</td>
                  <td>{p.vinculo}</td>
                  <td>
                    {p.principal ? <StatusTerr value="principal" /> : <span className="muted">—</span>}
                  </td>
                  <td>{formatarDataTerr(p.created_at)}</td>
                  <td>
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => handleRemover(p)}
                      disabled={salvando}
                    >
                      Remover
                    </button>
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
