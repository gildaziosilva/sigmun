import { useEffect, useState } from 'react';
import {
  listarBens,
  listarDepreciacoes,
  obterBem,
  type BemPat,
  type DepreciacaoPat,
} from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

function formatarMoeda(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export default function PatPage() {
  const [bens, recarregar] = useApiData(() => listarBens());
  const [bemSelecionado, setBemSelecionado] = useState<string | null>(null);
  const [bemDetalhe, setBemDetalhe] = useState<BemPat | null>(null);
  const [bemId, setBemId] = useState('');
  const [bemErro, setBemErro] = useState('');
  const [depreciacoes, setDepreciacoes] = useState<DepreciacaoPat[]>([]);
  const [depErro, setDepErro] = useState('');
  const [depCarregando, setDepCarregando] = useState(false);

  async function consultarBem() {
    const id = bemId.trim();
    if (!id) {
      setBemErro('Informe o ID do bem.');
      setBemDetalhe(null);
      return;
    }
    setBemErro('');
    try {
      setBemDetalhe(await obterBem(id));
    } catch (err) {
      setBemDetalhe(null);
      setBemErro(err instanceof Error ? err.message : 'Falha ao consultar bem.');
    }
  }

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function verDepreciacoes(bemId: string) {
    setBemSelecionado(bemId);
    setDepCarregando(true);
    setDepErro('');
    try {
      setDepreciacoes(await listarDepreciacoes(bemId));
    } catch (err) {
      setDepreciacoes([]);
      setDepErro(err instanceof Error ? err.message : 'Falha ao carregar depreciações.');
    } finally {
      setDepCarregando(false);
    }
  }

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Gestão Patrimonial (PAT)</h2>
        <button type="button" className="button button--ghost" onClick={recarregar}>
          Recarregar
        </button>
      </div>
      <p className="muted">
        Bens móveis/imóveis com tombamento via GET /api/v1/pat/bens. Depreciações por bem via
        GET /api/v1/pat/bens/:id/depreciacoes. Detalhe avulso via GET /api/v1/pat/bens/:id.
      </p>
      <article className="card">
        <h3>Bem por ID</h3>
        <div className="consulta-row">
          <input
            value={bemId}
            onChange={(e) => setBemId(e.target.value)}
            placeholder="ID do bem"
            aria-label="ID do bem"
          />
          <button type="button" className="button" onClick={consultarBem}>
            Consultar
          </button>
        </div>
        {bemErro && (
          <p className="alert alert--error" role="alert">
            {bemErro}
          </p>
        )}
        {bemDetalhe && (
          <dl className="detail-list">
            <div>
              <dt>Código</dt>
              <dd className="mono">{bemDetalhe.codigo}</dd>
            </div>
            <div>
              <dt>Descrição</dt>
              <dd>{bemDetalhe.descricao}</dd>
            </div>
            <div>
              <dt>Tipo</dt>
              <dd>{bemDetalhe.tipo}</dd>
            </div>
            <div>
              <dt>Valor contábil</dt>
              <dd>{formatarMoeda(bemDetalhe.valor_contabil)}</dd>
            </div>
            <div>
              <dt>Status</dt>
              <dd>{bemDetalhe.status}</dd>
            </div>
          </dl>
        )}
      </article>
      <TabelaEstado loading={bens.loading} erro={bens.erro} vazio={!bens.data || bens.data.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Descrição</th>
                <th>Tipo</th>
                <th>Valor contábil</th>
                <th>Status</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {(bens.data ?? []).map((b: BemPat) => (
                <tr key={b.id} className={b.id === bemSelecionado ? 'row--active' : ''}>
                  <td className="mono">{b.codigo}</td>
                  <td>{b.descricao}</td>
                  <td>
                    <span className="badge">{b.tipo}</span>
                  </td>
                  <td>{formatarMoeda(b.valor_contabil)}</td>
                  <td>
                    <span className="badge">{b.status}</span>
                  </td>
                  <td>
                    <button type="button" className="link" onClick={() => verDepreciacoes(b.id)}>
                      Depreciações
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>

      {bemSelecionado && (
        <article className="card card--detail">
          <h3>Depreciações do bem</h3>
          {depCarregando && <p className="muted">Consultando API…</p>}
          {depErro && (
            <p className="alert alert--error" role="alert">
              {depErro}
            </p>
          )}
          {!depCarregando && !depErro && depreciacoes.length === 0 && (
            <p className="muted">Nenhuma depreciação registrada para este bem.</p>
          )}
          {depreciacoes.length > 0 && (
            <div className="table-wrap">
              <table className="table">
                <thead>
                  <tr>
                    <th>Data</th>
                    <th>Valor depreciado</th>
                    <th>Acumulado</th>
                    <th>Valor líquido</th>
                  </tr>
                </thead>
                <tbody>
                  {depreciacoes.map((d) => (
                    <tr key={d.id}>
                      <td>{d.data ?? '—'}</td>
                      <td>{formatarMoeda(d.valor_depreciado)}</td>
                      <td>{formatarMoeda(d.valor_acumulado)}</td>
                      <td>{formatarMoeda(d.valor_liquido)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
          <button type="button" className="link" onClick={() => setBemSelecionado(null)}>
            Fechar
          </button>
        </article>
      )}
    </section>
  );
}
