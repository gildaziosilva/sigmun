import { useState } from 'react';
import {
  listarDiariasPorServidor,
  listarDiariasPorStatus,
  listarPrestacoesAbertas,
  listarViagensPorServidor,
  type DiariaDia,
  type PrestacaoContasDia,
  type ViagemDia,
} from '../../lib/api';

function formatarData(valor?: string | null): string {
  if (!valor) return '—';

  const data = new Date(valor);
  if (Number.isNaN(data.getTime())) return valor;

  return data.toLocaleDateString('pt-BR');
}

function formatarMoeda(valor: number): string {
  return new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  }).format(valor);
}

function MensagemEstado({
  carregando,
  erro,
  vazio,
}: {
  carregando: boolean;
  erro: string;
  vazio: boolean;
}) {
  if (carregando) {
    return <p className="muted">Consultando API…</p>;
  }

  if (erro) {
    return <p className="error">{erro}</p>;
  }

  if (vazio) {
    return <p className="muted">Nenhum registro encontrado.</p>;
  }

  return null;
}

export default function DiaPage() {
  const [servidorId, setServidorId] = useState('');

  const [viagens, setViagens] = useState<ViagemDia[]>([]);
  const [viagensCarregando, setViagensCarregando] = useState(false);
  const [viagensErro, setViagensErro] = useState('');

  const [diarias, setDiarias] = useState<DiariaDia[]>([]);
  const [diariasCarregando, setDiariasCarregando] = useState(false);
  const [diariasErro, setDiariasErro] = useState('');

  const [status, setStatus] = useState('');
  const [diariasStatus, setDiariasStatus] = useState<DiariaDia[]>([]);
  const [statusCarregando, setStatusCarregando] = useState(false);
  const [statusErro, setStatusErro] = useState('');

  const [prestacoes, setPrestacoes] = useState<PrestacaoContasDia[]>([]);
  const [prestacoesCarregando, setPrestacoesCarregando] = useState(false);
  const [prestacoesErro, setPrestacoesErro] = useState('');

  async function consultarViagens() {
    const id = servidorId.trim();

    if (!id) {
      setViagensErro('Informe o ID do servidor.');
      setViagens([]);
      return;
    }

    setViagensCarregando(true);
    setViagensErro('');

    try {
      setViagens(await listarViagensPorServidor(id));
    } catch (err: unknown) {
      setViagens([]);
      setViagensErro(err instanceof Error ? err.message : 'Falha ao consultar viagens.');
    } finally {
      setViagensCarregando(false);
    }
  }

  async function consultarDiarias() {
    const id = servidorId.trim();

    if (!id) {
      setDiariasErro('Informe o ID do servidor.');
      setDiarias([]);
      return;
    }

    setDiariasCarregando(true);
    setDiariasErro('');

    try {
      setDiarias(await listarDiariasPorServidor(id));
    } catch (err: unknown) {
      setDiarias([]);
      setDiariasErro(err instanceof Error ? err.message : 'Falha ao consultar diárias.');
    } finally {
      setDiariasCarregando(false);
    }
  }

  async function consultarDiariasPorStatus() {
    const valor = status.trim();

    if (!valor) {
      setStatusErro('Informe o status da diária.');
      setDiariasStatus([]);
      return;
    }

    setStatusCarregando(true);
    setStatusErro('');

    try {
      setDiariasStatus(await listarDiariasPorStatus(valor));
    } catch (err: unknown) {
      setDiariasStatus([]);
      setStatusErro(
        err instanceof Error ? err.message : 'Falha ao consultar diárias por status.',
      );
    } finally {
      setStatusCarregando(false);
    }
  }

  async function consultarPrestacoes() {
    setPrestacoesCarregando(true);
    setPrestacoesErro('');

    try {
      setPrestacoes(await listarPrestacoesAbertas());
    } catch (err: unknown) {
      setPrestacoes([]);
      setPrestacoesErro(
        err instanceof Error ? err.message : 'Falha ao consultar prestações abertas.',
      );
    } finally {
      setPrestacoesCarregando(false);
    }
  }

  return (
    <section>
      <div className="page-head">
        <div>
          <h2 className="section-title">Diárias e Viagens (DOM-DIA)</h2>
          <p className="muted">
            Consulta operacional de viagens, diárias e prestações de contas.
          </p>
        </div>
        <button type="button" className="button button--ghost" onClick={consultarPrestacoes}>
          Atualizar prestações
        </button>
      </div>

      <article className="card">
        <div className="page-head">
          <div>
            <h3>Viagens por servidor</h3>
            <p className="muted">
              Consulta GET /api/v1/dia/viagens/servidor/{'{servidor_id}'}.
            </p>
          </div>
        </div>

        <div className="form-row">
          <label className="field">
            <span>ID do servidor</span>
            <input
              value={servidorId}
              onChange={(event) => setServidorId(event.target.value)}
              placeholder="UUID do servidor"
            />
          </label>
          <button type="button" className="button" onClick={consultarViagens}>
            Consultar viagens
          </button>
        </div>

        <MensagemEstado
          carregando={viagensCarregando}
          erro={viagensErro}
          vazio={!viagensCarregando && !viagensErro && viagens.length === 0}
        />

        {viagens.length > 0 && (
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Destino</th>
                  <th>Motivo</th>
                  <th>Início</th>
                  <th>Fim</th>
                  <th>Antecipação</th>
                </tr>
              </thead>
              <tbody>
                {viagens.map((viagem) => (
                  <tr key={viagem.id}>
                    <td>{viagem.destino}</td>
                    <td>{viagem.motivo}</td>
                    <td>{formatarData(viagem.data_inicio)}</td>
                    <td>{formatarData(viagem.data_fim)}</td>
                    <td>
                      <span className="badge">{viagem.is_antecipacao ? 'Sim' : 'Não'}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>

      <article className="card">
        <div className="page-head">
          <div>
            <h3>Diárias por servidor</h3>
            <p className="muted">
              Consulta das diárias vinculadas ao servidor informado.
            </p>
          </div>
        </div>

        <div className="form-row">
          <button type="button" className="button" onClick={consultarDiarias}>
            Consultar diárias
          </button>
        </div>

        <MensagemEstado
          carregando={diariasCarregando}
          erro={diariasErro}
          vazio={!diariasCarregando && !diariasErro && diarias.length === 0}
        />

        {diarias.length > 0 && (
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Categoria</th>
                  <th>Descrição</th>
                  <th>Período</th>
                  <th>Valor total</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {diarias.map((diaria) => (
                  <tr key={diaria.id}>
                    <td>{diaria.categoria}</td>
                    <td>{diaria.descricao}</td>
                    <td>
                      {formatarData(diaria.data_inicio)} até {formatarData(diaria.data_fim)}
                    </td>
                    <td>{formatarMoeda(diaria.valor_total)}</td>
                    <td>
                      <span className="badge">{diaria.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>

      <article className="card">
        <div className="page-head">
          <div>
            <h3>Diárias por status</h3>
            <p className="muted">
              Consulta transversal pelo status registrado no DOM-DIA.
            </p>
          </div>
        </div>

        <div className="form-row">
          <label className="field">
            <span>Status</span>
            <input
              value={status}
              onChange={(event) => setStatus(event.target.value)}
              placeholder="Ex.: SOLICITADA"
            />
          </label>
          <button type="button" className="button" onClick={consultarDiariasPorStatus}>
            Consultar status
          </button>
        </div>

        <MensagemEstado
          carregando={statusCarregando}
          erro={statusErro}
          vazio={!statusCarregando && !statusErro && diariasStatus.length === 0}
        />

        {diariasStatus.length > 0 && (
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Servidor</th>
                  <th>Categoria</th>
                  <th>Período</th>
                  <th>Valor total</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {diariasStatus.map((diaria) => (
                  <tr key={diaria.id}>
                    <td className="mono">{diaria.servidor_id}</td>
                    <td>{diaria.categoria}</td>
                    <td>
                      {formatarData(diaria.data_inicio)} até {formatarData(diaria.data_fim)}
                    </td>
                    <td>{formatarMoeda(diaria.valor_total)}</td>
                    <td>
                      <span className="badge">{diaria.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>

      <article className="card">
        <div className="page-head">
          <div>
            <h3>Prestações de contas abertas</h3>
            <p className="muted">
              Consulta GET /api/v1/dia/prestacoes/abertas.
            </p>
          </div>
        </div>

        <MensagemEstado
          carregando={prestacoesCarregando}
          erro={prestacoesErro}
          vazio={!prestacoesCarregando && !prestacoesErro && prestacoes.length === 0}
        />

        {prestacoes.length > 0 && (
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Servidor</th>
                  <th>Emissão</th>
                  <th>Vencimento</th>
                  <th>Valor previsto</th>
                  <th>Valor líquido</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {prestacoes.map((prestacao) => (
                  <tr key={prestacao.id}>
                    <td className="mono">{prestacao.servidor_id}</td>
                    <td>{formatarData(prestacao.data_emissao)}</td>
                    <td>{formatarData(prestacao.data_vencimento)}</td>
                    <td>{formatarMoeda(prestacao.valor_previsto)}</td>
                    <td>{formatarMoeda(prestacao.valor_liquido)}</td>
                    <td>
                      <span className="badge">{prestacao.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </article>
    </section>
  );
}
