import { useCallback, useEffect, useState } from 'react';
import {
  ApiError,
  listarContratos,
  listarLicitacoes,
  obterContrato,
  obterLicitacao,
  onUnauthorized,
  type ContratoPublico,
  type LicitacaoPublica,
} from './lib/api';

type Rota = 'inicio' | 'licitacoes' | 'contratos' | 'pagamentos';

const PAGE_SIZE = 10;

function PortalFornecedor() {
  const [rota, setRota] = useState<Rota>('inicio');
  const [licitacoes, setLicitacoes] = useState<LicitacaoPublica[]>([]);
  const [licTotal, setLicTotal] = useState(0);
  const [licPage, setLicPage] = useState(0);
  const [licSituacao, setLicSituacao] = useState('');
  const [contratos, setContratos] = useState<ContratoPublico[]>([]);
  const [contTotal, setContTotal] = useState(0);
  const [contPage, setContPage] = useState(0);
  const [contSituacao, setContSituacao] = useState('');
  const [detalhe, setDetalhe] = useState<LicitacaoPublica | ContratoPublico | null>(null);
  const [detalheTipo, setDetalheTipo] = useState<'licitacao' | 'contrato' | null>(null);
  const [erro, setErro] = useState('');
  const [carregando, setCarregando] = useState(false);
  const [avisoSessao, setAvisoSessao] = useState('');

  function erroAmigavel(err: unknown): string {
    if (err instanceof ApiError) return err.friendlyMessage;
    return err instanceof Error ? err.message : 'API indisponível';
  }

  const carregarLicitacoes = useCallback(async (page: number, situacao: string) => {
    setCarregando(true);
    setErro('');
    try {
      const r = await listarLicitacoes(page, PAGE_SIZE, situacao || undefined);
      setLicitacoes(r.items);
      setLicTotal(r.total);
      setLicPage(r.page);
    } catch (err) {
      setErro(erroAmigavel(err));
    } finally {
      setCarregando(false);
    }
  }, []);

  const carregarContratos = useCallback(async (page: number, situacao: string) => {
    setCarregando(true);
    setErro('');
    try {
      const r = await listarContratos(page, PAGE_SIZE, situacao || undefined);
      setContratos(r.items);
      setContTotal(r.total);
      setContPage(r.page);
    } catch (err) {
      setErro(erroAmigavel(err));
    } finally {
      setCarregando(false);
    }
  }, []);

  useEffect(() => {
    onUnauthorized(() => setAvisoSessao('Acesso não autorizado (401/403).'));
    carregarLicitacoes(0, '');
    carregarContratos(0, '');
    return () => onUnauthorized(null);
  }, [carregarLicitacoes, carregarContratos]);

  async function verLicitacao(id: string) {
    setErro('');
    try {
      setDetalhe(await obterLicitacao(id));
      setDetalheTipo('licitacao');
    } catch (err) {
      setErro(erroAmigavel(err));
    }
  }

  async function verContrato(id: string) {
    setErro('');
    try {
      setDetalhe(await obterContrato(id));
      setDetalheTipo('contrato');
    } catch (err) {
      setErro(erroAmigavel(err));
    }
  }

  return (
    <div className="portal">
      <a className="skip-link" href="#conteudo">Pular para o conteúdo</a>
      <header className="portal-header">
        <div className="brand">
          <span className="brand-mark" aria-hidden="true">S</span>
          <div>
            <strong>SIGMUN — Portal do Fornecedor</strong>
            <small>Camacan-BA · licitações, contratos e pagamentos</small>
          </div>
        </div>
        <nav className="portal-nav" aria-label="Navegação do portal">
          {(
            [
              ['inicio', 'Início'],
              ['licitacoes', 'Licitações'],
              ['contratos', 'Contratos'],
              ['pagamentos', 'Pagamentos'],
            ] as [Rota, string][]
          ).map(([id, rotulo]) => (
            <button
              key={id}
              type="button"
              className={rota === id ? 'active' : ''}
              aria-current={rota === id ? 'page' : undefined}
              onClick={() => { setRota(id); setDetalhe(null); setDetalheTipo(null); }}
            >
              {rotulo}
            </button>
          ))}
        </nav>
      </header>

      <main id="conteudo" className="portal-main" tabIndex={-1}>
        {avisoSessao && <p className="alert alert--error" role="alert">{avisoSessao}</p>}
        {erro && <p className="alert alert--error" role="alert">{erro}</p>}

        {rota === 'inicio' && (
          <section className="portal-hero" aria-labelledby="titulo-ini-f">
            <h1 id="titulo-ini-f">Acompanhe licitações e contratos</h1>
            <p>Área pública de acompanhamento para fornecedores municipais.</p>
            <div className="hero-actions">
              <button type="button" className="button button--primary" onClick={() => setRota('licitacoes')}>
                Ver licitações
              </button>
              <button type="button" className="button button--ghost" onClick={() => setRota('contratos')}>
                Ver contratos
              </button>
            </div>
          </section>
        )}

        {rota === 'licitacoes' && (
          <section className="card" aria-labelledby="titulo-lic">
            <h2 id="titulo-lic">Licitações · GET /api/v1/compras</h2>
            <form className="inline-form" onSubmit={(e) => { e.preventDefault(); carregarLicitacoes(0, licSituacao); }}>
              <label htmlFor="lic-situacao">
                Situação
                <input id="lic-situacao" value={licSituacao} onChange={(e) => setLicSituacao(e.target.value)} placeholder="Ex.: PUBLICADA" />
              </label>
              <button type="submit" className="button button--primary" disabled={carregando}>Filtrar</button>
            </form>
            {carregando && <output className="muted">Carregando…</output>}
            {licitacoes.length === 0 && !carregando ? (
              <p className="muted">Nenhuma licitação publicada.</p>
            ) : (
              <ul className="result-list">
                {licitacoes.map((l) => (
                  <li key={l.id}>
                    <button type="button" className="link" onClick={() => verLicitacao(l.id)}>
                      <strong className="mono">{l.numero}</strong>
                    </button>
                    <span className="badge">{l.situacao}</span>
                    <span className="muted"> · {l.valor_total ?? 'valor sob consulta'}</span>
                  </li>
                ))}
              </ul>
            )}
            <div className="pager">
              <button type="button" className="button button--ghost" disabled={licPage === 0 || carregando} onClick={() => carregarLicitacoes(licPage - 1, licSituacao)}>Anterior</button>
              <span className="muted">Página {licPage + 1} · {licTotal} no total</span>
              <button type="button" className="button button--ghost" disabled={(licPage + 1) * PAGE_SIZE >= licTotal || carregando} onClick={() => carregarLicitacoes(licPage + 1, licSituacao)}>Próxima</button>
            </div>
          </section>
        )}

        {rota === 'contratos' && (
          <section className="card" aria-labelledby="titulo-cont">
            <h2 id="titulo-cont">Contratos · GET /api/v1/contratos</h2>
            <form className="inline-form" onSubmit={(e) => { e.preventDefault(); carregarContratos(0, contSituacao); }}>
              <label htmlFor="cont-situacao">
                Situação
                <input id="cont-situacao" value={contSituacao} onChange={(e) => setContSituacao(e.target.value)} placeholder="Ex.: VIGENTE" />
              </label>
              <button type="submit" className="button button--primary" disabled={carregando}>Filtrar</button>
            </form>
            {contratos.length === 0 && !carregando ? (
              <p className="muted">Nenhum contrato publicado.</p>
            ) : (
              <ul className="result-list">
                {contratos.map((c) => (
                  <li key={c.id}>
                    <button type="button" className="link" onClick={() => verContrato(c.id)}>
                      <strong className="mono">{c.numero ?? String(c.id).slice(0, 8)}</strong>
                    </button>
                    {c.situacao && <span className="badge">{c.situacao}</span>}
                  </li>
                ))}
              </ul>
            )}
            <div className="pager">
              <button type="button" className="button button--ghost" disabled={contPage === 0 || carregando} onClick={() => carregarContratos(contPage - 1, contSituacao)}>Anterior</button>
              <span className="muted">Página {contPage + 1} · {contTotal} no total</span>
              <button type="button" className="button button--ghost" disabled={(contPage + 1) * PAGE_SIZE >= contTotal || carregando} onClick={() => carregarContratos(contPage + 1, contSituacao)}>Próxima</button>
            </div>
          </section>
        )}

        {detalhe && detalheTipo && (rota === 'licitacoes' || rota === 'contratos') && (
          <section className="card" aria-labelledby="titulo-det" aria-live="polite">
            <h2 id="titulo-det">Detalhe {detalheTipo === 'licitacao' ? 'da licitação' : 'do contrato'}</h2>
            <dl className="detail-list">
              <dt>Número</dt>
              <dd className="mono">{'numero' in detalhe ? (detalhe.numero ?? detalhe.id) : detalhe.id}</dd>
              <dt>Situação</dt>
              <dd>{'situacao' in detalhe ? String(detalhe.situacao ?? '—') : '—'}</dd>
              <dt>Valor</dt>
              <dd>{'valor_total' in detalhe ? String(detalhe.valor_total ?? 'sob consulta') : String((detalhe as ContratoPublico).valor ?? 'sob consulta')}</dd>
            </dl>
            <button type="button" className="button button--ghost" onClick={() => { setDetalhe(null); setDetalheTipo(null); }}>
              Fechar detalhe
            </button>
          </section>
        )}

        {rota === 'pagamentos' && (
          <section className="card" aria-labelledby="titulo-pag">
            <h2 id="titulo-pag">Pagamentos</h2>
            <p className="muted">
              O cronograma de pagamentos por contrato será publicado com o DOM-ORC (Onda 3).
              Por ora, acompanhe a situação do seu contrato na aba Contratos e, em caso de
              dúvida, procure a Secretaria de Finanças com o número do contrato.
            </p>
          </section>
        )}
      </main>

      <footer className="portal-footer">
        <small>Portal do Fornecedor · Camacan-BA</small>
      </footer>
    </div>
  );
}

export default PortalFornecedor;

