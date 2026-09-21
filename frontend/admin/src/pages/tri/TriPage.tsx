import { useEffect } from 'react';
import {
  listarDividaAtiva,
  listarLancamentos,
  obterContribuinte,
  obterImovel,
  type DividaAtivaTri,
  type LancamentoTri,
} from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

function formatarMoeda(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export default function TriPage() {
  const [lancamentos, recarregarLancamentos] = useApiData(() => listarLancamentos());
  const [divida, recarregarDivida] = useApiData(() => listarDividaAtiva());

  useEffect(() => {
    recarregarLancamentos();
    recarregarDivida();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Administração Tributária (TRI)</h2>
        <button
          type="button"
          className="button button--ghost"
          onClick={() => {
            recarregarLancamentos();
            recarregarDivida();
          }}
        >
          Recarregar
        </button>
      </div>
      <p className="muted">
        Lançamentos de crédito tributário (IPTU/ISSQN/ITBI/taxas) e inscrições em dívida
        ativa via GET /api/v1/tri/…. Detalhe de contribuinte/imóvel sob demanda.
      </p>

      <article className="card">
        <h3>Lançamentos</h3>
        <TabelaEstado
          loading={lancamentos.loading}
          erro={lancamentos.erro}
          vazio={!lancamentos.data || lancamentos.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Número</th>
                  <th>Tributo</th>
                  <th>Exercício</th>
                  <th>Valor total</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {(lancamentos.data ?? []).map((l: LancamentoTri) => (
                  <tr key={l.id}>
                    <td className="mono">{l.numero_lancamento}</td>
                    <td>
                      <span className="badge">{l.tipo_tributo}</span>
                    </td>
                    <td>{l.exercicio}</td>
                    <td>{formatarMoeda(l.valor_total)}</td>
                    <td>
                      <span className="badge">{l.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <article className="card">
        <h3>Dívida ativa</h3>
        <TabelaEstado
          loading={divida.loading}
          erro={divida.erro}
          vazio={!divida.data || divida.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Inscrição</th>
                  <th>Valor original</th>
                  <th>Valor atualizado</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {(divida.data ?? []).map((d: DividaAtivaTri) => (
                  <tr key={d.id}>
                    <td className="mono">{d.numero_inscricao}</td>
                    <td>{formatarMoeda(d.valor_original)}</td>
                    <td>{formatarMoeda(d.valor_atualizado)}</td>
                    <td>
                      <span className="badge">{d.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <ConsultaContribuinteImovel />
    </section>
  );
}

import { useState } from 'react';

function ConsultaContribuinteImovel() {
  const [id, setId] = useState('');
  const [resultado, setResultado] = useState('');
  const [erro, setErro] = useState('');
  const [carregando, setCarregando] = useState(false);

  async function consultar(tipo: 'contribuinte' | 'imovel') {
    const valor = id.trim();
    if (!valor) {
      setErro('Informe o ID do registro.');
      setResultado('');
      return;
    }
    setCarregando(true);
    setErro('');
    try {
      const dados = tipo === 'contribuinte' ? await obterContribuinte(valor) : await obterImovel(valor);
      setResultado(JSON.stringify(dados, null, 2));
    } catch (err) {
      setResultado('');
      setErro(err instanceof Error ? err.message : 'Falha na consulta.');
    } finally {
      setCarregando(false);
    }
  }

  return (
    <article className="card">
      <h3>Consulta de cadastro</h3>
      <p className="muted">GET /api/v1/tri/contribuintes/:id e GET /api/v1/tri/imoveis/:id.</p>
      <div className="consulta-row">
        <input
          value={id}
          onChange={(e) => setId(e.target.value)}
          placeholder="ID do contribuinte ou imóvel"
          aria-label="ID do registro"
        />
        <button type="button" className="button" onClick={() => consultar('contribuinte')}>
          Contribuinte
        </button>
        <button type="button" className="button button--ghost" onClick={() => consultar('imovel')}>
          Imóvel
        </button>
      </div>
      {carregando && <p className="muted">Consultando API…</p>}
      {erro && (
        <p className="alert alert--error" role="alert">
          {erro}
        </p>
      )}
      {resultado && <pre className="mono bloco-json">{resultado}</pre>}
    </article>
  );
}
