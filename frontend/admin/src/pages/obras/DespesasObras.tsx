import { useCallback, useEffect, useState } from 'react';
import type { DespesaObra, DespesaObraCreate, ObraDetalhe } from '../../lib/api';
import { excluirDespesaObra, obterAcompanhamentoObra, registrarDespesaObra } from '../../lib/api';
import type { ExecutarObras } from './ObrasShared';
import {
  FieldObras,
  SelectObras,
  TIPOS_DESPESA,
  formatarDataObras,
  formatarMoedaObras,
  paraNumeroObras,
} from './ObrasShared';

interface Props {
  obraId: string;
  executar: ExecutarObras;
  salvando: boolean;
}

export function DespesasObras({ obraId, executar, salvando }: Props) {
  const [descricao, setDescricao] = useState('');
  const [tipo, setTipo] = useState('repasse');
  const [valor, setValor] = useState('0');
  const [credor, setCredor] = useState('');
  const [detalhe, setDetalhe] = useState<ObraDetalhe | null>(null);
  const [erro, setErro] = useState('');

  const carregar = useCallback(() => {
    if (!obraId) return;
    obterAcompanhamentoObra(obraId)
      .then((d) => {
        setDetalhe(d);
        setErro('');
      })
      .catch((falha: unknown) =>
        setErro(falha instanceof Error ? falha.message : 'Falha ao carregar despesas.'),
      );
  }, [obraId]);

  useEffect(() => {
    carregar();
  }, [carregar]);

  const despesas: DespesaObra[] = detalhe?.despesas ?? [];
  const saldo = detalhe ? detalhe.obra.valor_mediado - detalhe.obra.valor_pago : 0;

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: DespesaObraCreate = {
      obra_id: obraId,
      descricao,
      tipo,
      valor: paraNumeroObras(valor),
      credor,
    };
    const ok = await executar(() => registrarDespesaObra(payload), 'Despesa registrada com sucesso!');
    if (ok) {
      setDescricao('');
      setValor('0');
      setCredor('');
      carregar();
    }
  }

  return (
    <section className="stack">
      <form className="card obras-form" onSubmit={handleSubmit}>
        <h3>Nova despesa financeira (RN-OBR-006)</h3>
        <p className="muted">
          Saldo medido a pagar: <strong>{formatarMoedaObras(saldo)}</strong>. A despesa nao pode
          ultrapassar o valor medido e ainda nao pago.
        </p>
        <div className="form-grid">
          <FieldObras label="Descricao" value={descricao} onChange={setDescricao} required />
          <SelectObras label="Tipo" value={tipo} opcoes={TIPOS_DESPESA} onChange={setTipo} />
          <FieldObras label="Valor (R$)" type="number" min="0.01" step="0.01" value={valor} onChange={setValor} required />
          <FieldObras label="Credor" value={credor} onChange={setCredor} />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Registrar despesa
          </button>
        </div>
      </form>

      {erro && <p className="alert alert--error">{erro}</p>}

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Despesas da obra ({despesas.length})</h3>
        </div>
        {despesas.length === 0 ? (
          <p className="muted">Nenhuma despesa registrada.</p>
        ) : (
          <table className="obras-table">
            <thead>
              <tr>
                <th>Data</th>
                <th>Descricao</th>
                <th>Tipo</th>
                <th>Credor</th>
                <th className="num">Valor</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {despesas.map((d) => (
                <tr key={d.id}>
                  <td>{formatarDataObras(d.data)}</td>
                  <td>{d.descricao}</td>
                  <td>{d.tipo}</td>
                  <td>{d.credor || '—'}</td>
                  <td className="num">{formatarMoedaObras(d.valor)}</td>
                  <td>
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => executar(() => excluirDespesaObra(d.id), 'Despesa excluida!')}
                      disabled={salvando}
                    >
                      Excluir
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
