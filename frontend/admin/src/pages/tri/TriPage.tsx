import { useEffect, useState } from 'react';
import {
  listarContribuintes,
  listarDividaAtiva,
  listarImoveis,
  listarLancamentos,
  obterCertidao,
  obterContribuinte,
  obterImovel,
  obterLancamento,
  pagarLancamento,
  type CertidaoTri,
  type ContribuinteTri,
  type DividaAtivaTri,
  type ImovelTri,
  type LancamentoTri,
} from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

function formatarMoeda(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export default function TriPage() {
  const [lancamentos, recarregarLancamentos] = useApiData(() => listarLancamentos());
  const [divida, recarregarDivida] = useApiData(() => listarDividaAtiva());
  const [contribuintes, recarregarContribuintes] = useApiData(() => listarContribuintes());
  const [imoveis, recarregarImoveis] = useApiData(() => listarImoveis());
  const [lancamentoDetalhe, setLancamentoDetalhe] = useState<LancamentoTri | null>(null);
  const [lancamentoId, setLancamentoId] = useState('');
  const [lancamentoErro, setLancamentoErro] = useState('');
  const [lancamentoCarregando, setLancamentoCarregando] = useState(false);
  const [pagamentoData, setPagamentoData] = useState('');
  const [pagamentoMsg, setPagamentoMsg] = useState('');
  const [certidao, setCertidao] = useState<CertidaoTri | null>(null);
  const [certidaoId, setCertidaoId] = useState('');
  const [certidaoErro, setCertidaoErro] = useState('');

  useEffect(() => {
    recarregarLancamentos();
    recarregarDivida();
    recarregarContribuintes();
    recarregarImoveis();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function recarregarTudo() {
    recarregarLancamentos();
    recarregarDivida();
    recarregarContribuintes();
    recarregarImoveis();
  }

  async function consultarLancamento() {
    const id = lancamentoId.trim();
    if (!id) {
      setLancamentoErro('Informe o ID do lançamento.');
      setLancamentoDetalhe(null);
      return;
    }
    setLancamentoCarregando(true);
    setLancamentoErro('');
    setPagamentoMsg('');
    try {
      setLancamentoDetalhe(await obterLancamento(id));
    } catch (err) {
      setLancamentoDetalhe(null);
      setLancamentoErro(err instanceof Error ? err.message : 'Falha ao consultar lançamento.');
    } finally {
      setLancamentoCarregando(false);
    }
  }

  async function pagar() {
    const id = lancamentoId.trim();
    if (!id) {
      setLancamentoErro('Informe o ID do lançamento.');
      return;
    }
    setLancamentoCarregando(true);
    setLancamentoErro('');
    setPagamentoMsg('');
    try {
      const pago = await pagarLancamento(id, pagamentoData.trim() || undefined);
      setLancamentoDetalhe(pago);
      setPagamentoMsg(`Lançamento ${pago.numero_lancamento} pago com sucesso.`);
      recarregarLancamentos();
      recarregarDivida();
    } catch (err) {
      setLancamentoErro(err instanceof Error ? err.message : 'Falha ao pagar lançamento.');
    } finally {
      setLancamentoCarregando(false);
    }
  }

  async function consultarCertidao() {
    const id = certidaoId.trim();
    if (!id) {
      setCertidaoErro('Informe o ID da certidão.');
      setCertidao(null);
      return;
    }
    setCertidaoErro('');
    try {
      setCertidao(await obterCertidao(id));
    } catch (err) {
      setCertidao(null);
      setCertidaoErro(err instanceof Error ? err.message : 'Falha ao consultar certidão.');
    }
  }

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Administração Tributária (TRI)</h2>
        <button type="button" className="button button--ghost" onClick={recarregarTudo}>
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

      <article className="card">
        <h3>Contribuintes</h3>
        <p className="muted">GET /api/v1/tri/contribuintes.</p>
        <TabelaEstado
          loading={contribuintes.loading}
          erro={contribuintes.erro}
          vazio={!contribuintes.data || contribuintes.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Nome</th>
                  <th>Tipo</th>
                  <th>Documento</th>
                  <th>Situação</th>
                </tr>
              </thead>
              <tbody>
                {(contribuintes.data ?? []).map((c: ContribuinteTri) => (
                  <tr key={c.id}>
                    <td>{c.nome}</td>
                    <td>
                      <span className="badge">{c.tipo}</span>
                    </td>
                    <td className="mono">{c.cpf_cnpj}</td>
                    <td>
                      <span className="badge">{c.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <article className="card">
        <h3>Imóveis</h3>
        <p className="muted">GET /api/v1/tri/imoveis.</p>
        <TabelaEstado
          loading={imoveis.loading}
          erro={imoveis.erro}
          vazio={!imoveis.data || imoveis.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Inscrição</th>
                  <th>Endereço</th>
                  <th>Área</th>
                  <th>Valor venal</th>
                </tr>
              </thead>
              <tbody>
                {(imoveis.data ?? []).map((m: ImovelTri) => (
                  <tr key={m.id}>
                    <td className="mono">{m.inscricao_imobiliaria}</td>
                    <td>
                      {[m.logradouro, m.numero, m.bairro, m.cidade, m.uf]
                        .filter(Boolean)
                        .join(', ') || '—'}
                    </td>
                    <td>{m.area_terreno.toLocaleString('pt-BR')} m²</td>
                    <td>{formatarMoeda(m.valor_venal)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <article className="card">
        <h3>Lançamento por ID + pagamento</h3>
        <p className="muted">
          GET /api/v1/tri/lancamentos/:id e POST /api/v1/tri/lancamentos/:id/pagar.
        </p>
        <div className="consulta-row">
          <input
            value={lancamentoId}
            onChange={(e) => setLancamentoId(e.target.value)}
            placeholder="ID do lançamento"
            aria-label="ID do lançamento"
          />
          <input
            value={pagamentoData}
            onChange={(e) => setPagamentoData(e.target.value)}
            placeholder="Data pagamento (opcional, AAAA-MM-DD)"
            aria-label="Data do pagamento"
          />
          <button type="button" className="button" onClick={consultarLancamento}>
            Consultar
          </button>
          <button
            type="button"
            className="button button--ghost"
            onClick={pagar}
            disabled={lancamentoCarregando}
          >
            {lancamentoCarregando ? 'Processando…' : 'Pagar'}
          </button>
        </div>
        {lancamentoErro && (
          <p className="alert alert--error" role="alert">
            {lancamentoErro}
          </p>
        )}
        {pagamentoMsg && <p className="alert alert--ok">{pagamentoMsg}</p>}
        {lancamentoDetalhe && (
          <dl className="detail-list">
            <div>
              <dt>Número</dt>
              <dd className="mono">{lancamentoDetalhe.numero_lancamento}</dd>
            </div>
            <div>
              <dt>Tributo</dt>
              <dd>{lancamentoDetalhe.tipo_tributo}</dd>
            </div>
            <div>
              <dt>Exercício</dt>
              <dd>{lancamentoDetalhe.exercicio}</dd>
            </div>
            <div>
              <dt>Valor total</dt>
              <dd>{formatarMoeda(lancamentoDetalhe.valor_total)}</dd>
            </div>
            <div>
              <dt>Status</dt>
              <dd>{lancamentoDetalhe.status}</dd>
            </div>
          </dl>
        )}
      </article>

      <article className="card">
        <h3>Certidão por ID</h3>
        <p className="muted">GET /api/v1/tri/certidoes/:id.</p>
        <div className="consulta-row">
          <input
            value={certidaoId}
            onChange={(e) => setCertidaoId(e.target.value)}
            placeholder="ID da certidão"
            aria-label="ID da certidão"
          />
          <button type="button" className="button" onClick={consultarCertidao}>
            Consultar
          </button>
        </div>
        {certidaoErro && (
          <p className="alert alert--error" role="alert">
            {certidaoErro}
          </p>
        )}
        {certidao && (
          <dl className="detail-list">
            <div>
              <dt>Número</dt>
              <dd className="mono">{certidao.numero}</dd>
            </div>
            <div>
              <dt>Tipo</dt>
              <dd>{certidao.tipo}</dd>
            </div>
            <div>
              <dt>Situação</dt>
              <dd>{certidao.status}</dd>
            </div>
            <div>
              <dt>Válida até</dt>
              <dd>{certidao.valido_ate ?? '—'}</dd>
            </div>
          </dl>
        )}
      </article>

      <ConsultaContribuinteImovel />
    </section>
  );
}

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
