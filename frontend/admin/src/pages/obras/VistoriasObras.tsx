import { useCallback, useEffect, useState } from 'react';
import type { ObraDetalhe, VistoriaObra, VistoriaObraCreate } from '../../lib/api';
import { obterAcompanhamentoObra, registrarVistoriaObra } from '../../lib/api';
import type { ExecutarObras } from './ObrasShared';
import {
  FieldObras,
  PARECERES_VISTORIA,
  SelectObras,
  StatusObras,
  TIPOS_VISTORIA,
  formatarDataObras,
  paraNumeroObras,
} from './ObrasShared';

interface Props {
  obraId: string;
  executar: ExecutarObras;
  salvando: boolean;
}

export function VistoriasObras({ obraId, executar, salvando }: Props) {
  const [tipo, setTipo] = useState('periodica');
  const [parecer, setParecer] = useState('aprovado');
  const [percentual, setPercentual] = useState('0');
  const [fiscal, setFiscal] = useState('');
  const [observacao, setObservacao] = useState('');
  const [vistorias, setVistorias] = useState<VistoriaObra[]>([]);
  const [erro, setErro] = useState('');

  const carregar = useCallback(() => {
    if (!obraId) return;
    obterAcompanhamentoObra(obraId)
      .then((d: ObraDetalhe) => {
        setVistorias(d.vistorias);
        setErro('');
      })
      .catch((falha: unknown) =>
        setErro(falha instanceof Error ? falha.message : 'Falha ao carregar vistorias.'),
      );
  }, [obraId]);

  useEffect(() => {
    carregar();
  }, [carregar]);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: VistoriaObraCreate = {
      obra_id: obraId,
      tipo,
      parecer,
      percentual_fisico_verificado: paraNumeroObras(percentual),
      fiscal,
      observacao,
    };
    const ok = await executar(() => registrarVistoriaObra(payload), 'Vistoria registrada com sucesso!');
    if (ok) {
      setPercentual('0');
      setFiscal('');
      setObservacao('');
      carregar();
    }
  }

  return (
    <section className="stack">
      <form className="card obras-form" onSubmit={handleSubmit}>
        <h3>Nova vistoria fiscalizadora (RN-OBR-008)</h3>
        <div className="form-grid">
          <SelectObras label="Tipo" value={tipo} opcoes={TIPOS_VISTORIA} onChange={setTipo} />
          <SelectObras label="Parecer" value={parecer} opcoes={PARECERES_VISTORIA} onChange={setParecer} />
          <FieldObras
            label="Avanco fisico verificado (%)"
            type="number"
            min="0"
            max="100"
            step="0.01"
            value={percentual}
            onChange={setPercentual}
            required
          />
          <FieldObras label="Fiscal" value={fiscal} onChange={setFiscal} required />
          <FieldObras label="Observacao" value={observacao} onChange={setObservacao} />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Registrar vistoria
          </button>
        </div>
      </form>

      {erro && <p className="alert alert--error">{erro}</p>}

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Vistorias realizadas ({vistorias.length})</h3>
        </div>
        {vistorias.length === 0 ? (
          <p className="muted">Nenhuma vistoria registrada.</p>
        ) : (
          <table className="obras-table">
            <thead>
              <tr>
                <th>Data</th>
                <th>Tipo</th>
                <th>Parecer</th>
                <th className="num">Verificado</th>
                <th>Fiscal</th>
              </tr>
            </thead>
            <tbody>
              {vistorias.map((v) => (
                <tr key={v.id}>
                  <td>{formatarDataObras(v.data)}</td>
                  <td>{v.tipo}</td>
                  <td>
                    <StatusObras value={v.parecer} />
                  </td>
                  <td className="num">{v.percentual_fisico_verificado.toFixed(1)}%</td>
                  <td>{v.fiscal}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}
