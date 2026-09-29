import { useCallback, useEffect, useState } from 'react';
import type { MedicaoObra, MedicaoObraCreate } from '../../lib/api';
import {
  aprovarMedicaoObra,
  cancelarMedicaoObra,
  glosarMedicaoObra,
  obterAcompanhamentoObra,
  registrarMedicaoObra,
} from '../../lib/api';
import type { ExecutarObras } from './ObrasShared';
import {
  FieldObras,
  SelectObras,
  StatusObras,
  TIPOS_MEDICAO,
  formatarDataObras,
  formatarMoedaObras,
  paraNumeroObras,
} from './ObrasShared';

interface Props {
  obraId: string;
  executar: ExecutarObras;
  salvando: boolean;
}

export function MedicoesObras({ obraId, executar, salvando }: Props) {
  const [numero, setNumero] = useState('');
  const [tipo, setTipo] = useState('avanco');
  const [percentual, setPercentual] = useState('0');
  const [valor, setValor] = useState('0');
  const [responsavel, setResponsavel] = useState('');
  const [medicoes, setMedicoes] = useState<MedicaoObra[]>([]);
  const [erro, setErro] = useState('');

  const carregar = useCallback(() => {
    if (!obraId) return;
    obterAcompanhamentoObra(obraId)
      .then((detalhe) => {
        setMedicoes(detalhe.medicoes);
        setErro('');
      })
      .catch((falha: unknown) =>
        setErro(falha instanceof Error ? falha.message : 'Falha ao carregar medicoes.'),
      );
  }, [obraId]);

  useEffect(() => {
    carregar();
  }, [carregar]);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: MedicaoObraCreate = {
      obra_id: obraId,
      numero,
      tipo,
      percentual_fisico: paraNumeroObras(percentual),
      valor_medido: paraNumeroObras(valor),
      responsavel_tecnico: responsavel,
    };
    const ok = await executar(() => registrarMedicaoObra(payload), 'Medicao registrada com sucesso!');
    if (ok) {
      setNumero('');
      setPercentual('0');
      setValor('0');
      setResponsavel('');
      carregar();
    }
  }

  return (
    <section className="stack">
      <form className="card obras-form" onSubmit={handleSubmit}>
        <h3>Nova medicao fisico-financeira (RN-OBR-005)</h3>
        <div className="form-grid">
          <FieldObras label="Numero" value={numero} onChange={setNumero} required />
          <SelectObras label="Tipo" value={tipo} opcoes={TIPOS_MEDICAO} onChange={setTipo} />
          <FieldObras label="Avanco fisico (%)" type="number" min="0" max="100" step="0.01" value={percentual} onChange={setPercentual} required />
          <FieldObras label="Valor medido (R$)" type="number" min="0" step="0.01" value={valor} onChange={setValor} required hint="Nao pode superar o valor contratado." />
          <FieldObras label="Responsavel tecnico" value={responsavel} onChange={setResponsavel} required />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Registrar medicao
          </button>
        </div>
      </form>

      {erro && <p className="alert alert--error">{erro}</p>}

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Medicoes da obra ({medicoes.length})</h3>
        </div>
        {medicoes.length === 0 ? (
          <p className="muted">Nenhuma medicao registrada.</p>
        ) : (
          <table className="obras-table">
            <thead>
              <tr>
                <th>Numero</th>
                <th>Tipo</th>
                <th>Data</th>
                <th className="num">Fisico</th>
                <th className="num">Valor</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {medicoes.map((m) => (
                <tr key={m.id}>
                  <td>{m.numero}</td>
                  <td>{m.tipo}</td>
                  <td>{formatarDataObras(m.data)}</td>
                  <td className="num">{m.percentual_fisico.toFixed(2)}%</td>
                  <td className="num">{formatarMoedaObras(m.valor_medido)}</td>
                  <td>
                    <StatusObras value={m.situacao} />
                  </td>
                  <td className="obras-acoes">
                    {m.situacao === 'registrada' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => executar(() => aprovarMedicaoObra(m.id), 'Medicao aprovada!')}
                        disabled={salvando}
                        title="Conferir e aprovar (RN-OBR-005)"
                      >
                        Aprovar
                      </button>
                    )}
                    {m.situacao === 'registrada' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => {
                          const justificativa = window.prompt('Justificativa da glosa:');
                          if (justificativa) {
                            executar(() => glosarMedicaoObra(m.id, justificativa), 'Medicao glosada!');
                            carregar();
                          }
                        }}
                        disabled={salvando}
                        title="Glosar medicao"
                      >
                        Glosar
                      </button>
                    )}
                    {m.situacao === 'registrada' && (
                      <button
                        type="button"
                        className="button button--danger button--sm"
                        onClick={() => {
                          const justificativa = window.prompt(
                            'Justificativa do cancelamento da medicao:',
                          );
                          if (justificativa !== null) {
                            executar(
                              () => cancelarMedicaoObra(m.id, justificativa),
                              'Medicao cancelada!',
                            );
                            carregar();
                          }
                        }}
                        disabled={salvando}
                        title="Cancelar medicao nao aprovada (RN-OBR-005)"
                      >
                        Cancelar
                      </button>
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
