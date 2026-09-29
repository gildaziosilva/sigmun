import { useCallback, useEffect, useState } from 'react';
import type { EtapaObra, EtapaObraCreate, ObraDetalhe } from '../../lib/api';
import {
  atualizarEtapaObra,
  cadastrarEtapaObra,
  concluirEtapaObra,
  obterAcompanhamentoObra,
} from '../../lib/api';
import type { ExecutarObras } from './ObrasShared';
import {
  FieldObras,
  SelectObras,
  StatusObras,
  TIPOS_ETAPA,
  formatarDataObras,
  paraNumeroObras,
} from './ObrasShared';

interface Props {
  obraId: string;
  executar: ExecutarObras;
  salvando: boolean;
}

export function EtapasObras({ obraId, executar, salvando }: Props) {
  const [numero, setNumero] = useState('');
  const [descricao, setDescricao] = useState('');
  const [tipo, setTipo] = useState('estrutura');
  const [previsto, setPrevisto] = useState('0');
  const [responsavel, setResponsavel] = useState('');
  const [etapas, setEtapas] = useState<EtapaObra[]>([]);
  const [erro, setErro] = useState('');

  const carregar = useCallback(() => {
    if (!obraId) return;
    obterAcompanhamentoObra(obraId)
      .then((d: ObraDetalhe) => {
        setEtapas(d.etapas);
        setErro('');
      })
      .catch((falha: unknown) =>
        setErro(falha instanceof Error ? falha.message : 'Falha ao carregar etapas.'),
      );
  }, [obraId]);

  useEffect(() => {
    carregar();
  }, [carregar]);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: EtapaObraCreate = {
      obra_id: obraId,
      numero,
      descricao,
      tipo,
      percentual_previsto: paraNumeroObras(previsto),
      responsavel,
    };
    const ok = await executar(() => cadastrarEtapaObra(payload), 'Etapa cadastrada com sucesso!');
    if (ok) {
      setNumero('');
      setDescricao('');
      setPrevisto('0');
      setResponsavel('');
      carregar();
    }
  }

  return (
    <section className="stack">
      <form className="card obras-form" onSubmit={handleSubmit}>
        <h3>Nova etapa de execucao (RN-OBR-007)</h3>
        <div className="form-grid">
          <FieldObras label="Numero" value={numero} onChange={setNumero} required />
          <FieldObras label="Descricao" value={descricao} onChange={setDescricao} required />
          <SelectObras label="Tipo" value={tipo} opcoes={TIPOS_ETAPA} onChange={setTipo} />
          <FieldObras label="Percentual previsto (%)" type="number" min="0" max="100" step="0.01" value={previsto} onChange={setPrevisto} required />
          <FieldObras label="Responsavel" value={responsavel} onChange={setResponsavel} required />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            Cadastrar etapa
          </button>
        </div>
      </form>

      {erro && <p className="alert alert--error">{erro}</p>}

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Etapas da obra ({etapas.length})</h3>
        </div>
        {etapas.length === 0 ? (
          <p className="muted">Nenhuma etapa cadastrada.</p>
        ) : (
          <table className="obras-table">
            <thead>
              <tr>
                <th>Numero</th>
                <th>Descricao</th>
                <th>Tipo</th>
                <th className="num">Previsto</th>
                <th className="num">Realizado</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {etapas.map((e) => (
                <tr key={e.id}>
                  <td>{e.numero}</td>
                  <td>{e.descricao}</td>
                  <td>{e.tipo}</td>
                  <td className="num">{e.percentual_previsto.toFixed(1)}%</td>
                  <td className="num">{e.percentual_realizado.toFixed(1)}%</td>
                  <td>
                    <StatusObras value={e.situacao} />
                  </td>
                  <td className="obras-acoes">
                    {e.situacao !== 'concluida' && e.situacao !== 'cancelada' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => {
                          const realizado = window.prompt('Percentual realizado (0-100):', '100');
                          if (realizado !== null) {
                            executar(
                              () => atualizarEtapaObra(e.id, { percentual_realizado: paraNumeroObras(realizado) }),
                              'Etapa atualizada!',
                            );
                            carregar();
                          }
                        }}
                        disabled={salvando}
                        title="Atualizar avanco fisico"
                      >
                        Avanco
                      </button>
                    )}
                    {e.situacao !== 'concluida' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => concluirEtapaObra(e.id), 'Etapa concluida!')}
                        disabled={salvando}
                        title="Exige 100% do previsto (RN-OBR-007)"
                      >
                        Concluir
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
        {etapas.some((e) => e.data_conclusao) && (
          <p className="muted">
            Conclusoes registradas em{' '}
            {etapas
              .filter((e) => e.data_conclusao)
              .map((e) => formatarDataObras(e.data_conclusao))
              .join(', ')}
            .
          </p>
        )}
      </section>
    </section>
  );
}
