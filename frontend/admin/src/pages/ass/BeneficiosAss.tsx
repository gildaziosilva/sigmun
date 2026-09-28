import { useState, type FormEvent } from 'react';
import { solicitarBeneficioAss, aprovarBeneficioAss, entregarBeneficioAss, cancelarBeneficioAss, negarBeneficioAss, type BeneficioAssCreate } from '../../lib/api';
import { Field, formatarData, formatarMoeda, StatusBadge, type ExecutarAss, type AssResources, type FamiliaAss } from './AssShared';

// Benefícios seguem uma máquina de estados (SOLICITADO -> APROVADO/NEGADO ->
// ENTREGUE ou CANCELADO). Por isso não há edição de campos: a única forma de
// alterar um benefício é pelas ações de transição abaixo.

export function BeneficiosAss({ resources, executar, salvando }: { resources: AssResources; executar: ExecutarAss; salvando: boolean }) {
  const [novoBeneficio, setNovoBeneficio] = useState<BeneficioAssCreate>({
    familia_id: '',
    tipo: '',
    descricao: '',
    valor: 0,
    quantidade: 1,
    unidade_id: '',
    observacao: '',
  });
  const [pesquisa, setPesquisa] = useState('');

  const beneficios = resources.beneficios.data ?? [];

  async function handleSubmit(evento: FormEvent<HTMLFormElement>) {
    evento.preventDefault();
    const ok = await executar(() => solicitarBeneficioAss(novoBeneficio), 'Benefício solicitado com sucesso!');
    if (ok) setNovoBeneficio({ familia_id: '', tipo: '', descricao: '', valor: 0, quantidade: 1, unidade_id: '', observacao: '' });
  }

  async function handleAprovar(id: string) {
    await executar(() => aprovarBeneficioAss(id), 'Benefício aprovado com sucesso!');
  }

  async function handleNegar(id: string) {
    const justificativa = window.prompt('Informe a justificativa para negar o benefício:');
    if (!justificativa || !justificativa.trim()) return;
    await executar(() => negarBeneficioAss(id, justificativa.trim()), 'Benefício negado com sucesso!');
  }

  async function handleEntregar(id: string) {
    await executar(() => entregarBeneficioAss(id), 'Benefício entregue com sucesso!');
  }

  async function handleCancelar(id: string) {
    const confirmado = window.confirm('Cancelar este benefício?');
    if (!confirmado) return;
    await executar(() => cancelarBeneficioAss(id), 'Benefício cancelado com sucesso!');
  }

  const filtrados = beneficios.filter(
    (b) =>
      b.tipo.toLowerCase().includes(pesquisa.toLowerCase()) ||
      b.descricao?.toLowerCase().includes(pesquisa.toLowerCase()) ||
      b.familia_id.includes(pesquisa),
  );

  return (
    <section className="stack ass-beneficios">
      <form className="card ass-form" onSubmit={handleSubmit}>
        <h3>Solicitar novo benefício</h3>
        <div className="form-grid">
          <Field label="Família (NIS/Responsável)" value={novoBeneficio.familia_id} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, familia_id: v })} required>
            <select value={novoBeneficio.familia_id} onChange={(e) => setNovoBeneficio({ ...novoBeneficio, familia_id: e.target.value || '' })} required>
              <option value="">Selecione a família</option>
              {resources.familias.data?.map((f) => (
                <option key={f.id} value={f.id}>{f.nis} - {f.responsavel_nome}</option>
              ))}
            </select>
          </Field>
          <Field label="Tipo" value={novoBeneficio.tipo ?? ''} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, tipo: v })} required>
            <select value={novoBeneficio.tipo ?? ''} onChange={(e) => setNovoBeneficio({ ...novoBeneficio, tipo: e.target.value || '' })} required>
              <option value="">Selecione o tipo</option>
              <option value="alimentacao">Alimentação</option>
              <option value="aluguel">Aluguel</option>
              <option value="medicamento">Medicamento</option>
              <option value="funeral">Funeral</option>
              <option value="natalidade">Natalidade</option>
              <option value="calamidade">Calamidade</option>
              <option value="outro">Outro</option>
            </select>
          </Field>
          <Field label="Descrição" value={novoBeneficio.descricao ?? ''} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, descricao: v })} />
          <Field label="Valor" value={String(novoBeneficio.valor)} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, valor: Number(v) || 0 })} type="number" step="0.01" min="0" />
          <Field label="Quantidade" value={String(novoBeneficio.quantidade)} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, quantidade: Number(v) || 1 })} type="number" min="1" />
          <Field label="Unidade (CRAS/CREAS)" value={novoBeneficio.unidade_id ?? ''} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, unidade_id: v })}>
            <select value={novoBeneficio.unidade_id ?? ''} onChange={(e) => setNovoBeneficio({ ...novoBeneficio, unidade_id: e.target.value || '' })}>
              <option value="">Selecione a unidade</option>
              {resources.unidades.data?.map((u) => (
                <option key={u.id} value={u.id}>{u.codigo} - {u.nome}</option>
              ))}
            </select>
          </Field>
          <Field label="Observação" value={novoBeneficio.observacao ?? ''} onChange={(v) => setNovoBeneficio({ ...novoBeneficio, observacao: v })} />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>Solicitar benefício</button>
        </div>
      </form>

      <section className="card ass-lista">
        <div className="ass-lista-header">
          <h3>Benefícios solicitados ({beneficios.length})</h3>
          <input type="text" placeholder="Filtrar por tipo, descrição ou família..." value={pesquisa} onChange={(e) => setPesquisa(e.target.value)} className="ass-search" />
        </div>
        {beneficios.length === 0 ? (
          <p className="muted">Nenhum benefício solicitado.</p>
        ) : (
          <table className="ass-table">
            <thead>
              <tr><th>Tipo</th><th>Família</th><th>Valor</th><th>Qtd.</th><th>Status</th><th>Solicitado em</th><th>Aprovado em</th><th>Entregue em</th><th>Ações</th></tr>
            </thead>
            <tbody>
              {filtrados.map((b) => (
                <tr key={b.id}>
                  <td>{b.tipo}</td>
                  <td>{familiaNome(resources, b.familia_id)}</td>
                  <td>{formatarMoeda(b.valor)}</td>
                  <td>{b.quantidade}</td>
                  <td><StatusBadge value={b.status} /></td>
                  <td>{formatarData(b.data_solicitacao)}</td>
                  <td>{formatarData(b.data_aprovacao)}</td>
                  <td>{formatarData(b.data_entrega)}</td>
                  <td>
                    {b.status === 'solicitado' && (
                      <>
                        <button type="button" className="button button--ghost button--sm" onClick={() => handleAprovar(b.id)} disabled={salvando}>Aprovar</button>
                        <button type="button" className="button button--danger button--sm" onClick={() => handleNegar(b.id)} disabled={salvando}>Negar</button>
                        <button type="button" className="button button--ghost button--sm" onClick={() => handleCancelar(b.id)} disabled={salvando}>Cancelar</button>
                      </>
                    )}
                    {b.status === 'aprovado' && (
                      <>
                        <button type="button" className="button button--ghost button--sm" onClick={() => handleEntregar(b.id)} disabled={salvando}>Entregar</button>
                        <button type="button" className="button button--ghost button--sm" onClick={() => handleCancelar(b.id)} disabled={salvando}>Cancelar</button>
                      </>
                    )}
                    {(b.status === 'entregue' || b.status === 'negado' || b.status === 'cancelado') && (
                      <span className="muted">Sem ações disponíveis</span>
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

function familiaNome(resources: AssResources, id: string): string {
  return resources.familias.data?.find((f: FamiliaAss) => f.id === id)?.responsavel_nome ?? id;
}
