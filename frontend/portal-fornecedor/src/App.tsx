import { useEffect, useState } from 'react';
import { listarContratos, listarLicitacoes, type ContratoPublico, type LicitacaoPublica } from './lib/api';

type Rota = 'inicio' | 'licitacoes' | 'contratos' | 'empenhos';

function PortalFornecedor() {
  const [rota, setRota] = useState<Rota>('inicio');
  const [licitacoes, setLicitacoes] = useState<LicitacaoPublica[]>([]);
  const [contratos, setContratos] = useState<ContratoPublico[]>([]);
  const [erro, setErro] = useState('');

  useEffect(() => {
    Promise.all([listarLicitacoes(), listarContratos()])
      .then(([lic, cont]) => {
        setLicitacoes(lic.items);
        setContratos(cont.items);
      })
      .catch((err: unknown) => {
        setErro(err instanceof Error ? err.message : 'API indisponível');
      });
  }, []);

  return (
    <div className="portal">
      <header className="portal-header">
        <div className="brand">
          <span className="brand-mark" aria-hidden="true">S</span>
          <div>
            <strong>SIGMUN — Portal do Fornecedor</strong>
            <small>Camacan-BA · licitações, empenhos e contratos</small>
          </div>
        </div>
        <nav className="portal-nav" aria-label="Navegação do portal">
          {(
            [
              ['inicio', 'Início'],
              ['licitacoes', 'Licitações'],
              ['contratos', 'Contratos'],
              ['empenhos', 'Empenhos'],
            ] as [Rota, string][]
          ).map(([id, rotulo]) => (
            <button
              key={id}
              type="button"
              className={rota === id ? 'active' : ''}
              aria-current={rota === id ? 'page' : undefined}
              onClick={() => setRota(id)}
            >
              {rotulo}
            </button>
          ))}
        </nav>
      </header>

      <main className="portal-main">
        {erro && <p className="alert alert--error" role="alert">{erro}</p>}

        {rota === 'inicio' && (
          <section className="portal-hero">
            <h1>Acompanhe licitações e contratos</h1>
            <p>Área pública de acompanhamento para fornecedores municipais.</p>
            <button type="button" className="button button--primary" onClick={() => setRota('licitacoes')}>
              Ver licitações
            </button>
          </section>
        )}

        {rota === 'licitacoes' && (
          <section className="card">
            <h2>Licitações · GET /api/v1/compras</h2>
            {licitacoes.length === 0 ? (
              <p className="muted">Nenhuma licitação publicada.</p>
            ) : (
              <ul className="result-list">
                {licitacoes.map((l) => (
                  <li key={l.id}>
                    <strong className="mono">{l.numero}</strong>
                    <span className="badge">{l.situacao}</span>
                    <span className="muted"> · {l.valor_total ?? 'valor sob consulta'}</span>
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}

        {rota === 'contratos' && (
          <section className="card">
            <h2>Contratos · GET /api/v1/contratos</h2>
            {contratos.length === 0 ? (
              <p className="muted">Nenhum contrato publicado.</p>
            ) : (
              <ul className="result-list">
                {contratos.map((c) => (
                  <li key={c.id}>
                    <strong className="mono">{c.numero ?? String(c.id).slice(0, 8)}</strong>
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}

        {rota === 'empenhos' && (
          <section className="card">
            <h2>Empenhos</h2>
            <p className="muted">
              O acompanhamento de empenhos será habilitado com o DOM-ORC (Onda 3). Por ora,
              consulte empenhos no Portal da Transparência do município.
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

