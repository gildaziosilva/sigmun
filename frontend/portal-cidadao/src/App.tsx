import { useEffect, useState } from 'react';
import type { FormEvent } from 'react';
import { consultarProtocolo, fetchHealth, type DocumentoPublico, type HealthStatus } from './lib/api';

type Rota = 'inicio' | 'protocolos' | 'certidoes' | 'servicos';

function PortalCidadao() {
  const [rota, setRota] = useState<Rota>('inicio');
  const [codigo, setCodigo] = useState('');
  const [resultados, setResultados] = useState<DocumentoPublico[] | null>(null);
  const [buscaErro, setBuscaErro] = useState('');
  const [buscando, setBuscando] = useState(false);
  const [saude, setSaude] = useState<HealthStatus | null>(null);

  useEffect(() => {
    fetchHealth().then(setSaude).catch(() => undefined);
  }, []);

  async function buscar(event: FormEvent) {
    event.preventDefault();
    if (!codigo.trim()) {
      setBuscaErro('Informe o código do protocolo.');
      return;
    }
    setBuscaErro('');
    setBuscando(true);
    try {
      setResultados(await consultarProtocolo(codigo));
    } catch (err) {
      setBuscaErro(err instanceof Error ? err.message : 'Falha na consulta.');
    } finally {
      setBuscando(false);
    }
  }

  return (
    <div className="portal">
      <header className="portal-header">
        <div className="brand">
          <span className="brand-mark" aria-hidden="true">S</span>
          <div>
            <strong>SIGMUN — Portal do Cidadão</strong>
            <small>Prefeitura de Camacan-BA · serviços digitais</small>
          </div>
        </div>
        <nav className="portal-nav" aria-label="Navegação do portal">
          {(
            [
              ['inicio', 'Início'],
              ['protocolos', 'Protocolos'],
              ['certidoes', 'Certidões'],
              ['servicos', 'Serviços'],
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
        {rota === 'inicio' && (
          <section className="portal-hero">
            <h1>Serviços digitais da Prefeitura</h1>
            <p>Consulte protocolos, solicite certidões e acompanhe serviços públicos.</p>
            <button type="button" className="button button--primary" onClick={() => setRota('protocolos')}>
              Consultar protocolo
            </button>
          </section>
        )}

        {rota === 'protocolos' && (
          <section className="card">
            <h2>Consulta de protocolos</h2>
            <p className="muted">Busca pública por código (documentos não sigilosos · GET /api/v1/gdo/documentos).</p>
            <form className="inline-form" onSubmit={buscar}>
              <label htmlFor="codigo">
                Código do protocolo
                <input
                  id="codigo"
                  value={codigo}
                  onChange={(e) => setCodigo(e.target.value)}
                  placeholder="Ex.: DOC-2026-0001"
                />
              </label>
              <button type="submit" className="button button--primary" disabled={buscando}>
                {buscando ? 'Buscando…' : 'Buscar'}
              </button>
            </form>
            {buscaErro && <p className="alert alert--error" role="alert">{buscaErro}</p>}
            {resultados && (
              resultados.length === 0 ? (
                <p className="muted">Nenhum protocolo público encontrado para esse código.</p>
              ) : (
                <ul className="result-list">
                  {resultados.map((d) => (
                    <li key={d.id}>
                      <strong className="mono">{d.codigo}</strong> — {d.titulo}
                      <span className="badge">{d.status}</span>
                    </li>
                  ))}
                </ul>
              )
            )}
          </section>
        )}

        {rota === 'certidoes' && (
          <section className="card">
            <h2>Emissão de certidões</h2>
            <p className="muted">
              A emissão online de certidões (negativa de débitos, uso do solo) será habilitada após
              o DOM-TRI (Onda 3). Por ora, solicite presencialmente na Central de Atendimento.
            </p>
          </section>
        )}

        {rota === 'servicos' && (
          <section className="card">
            <h2>Serviços públicos</h2>
            <ul className="service-list">
              <li>Iluminação pública — abertura de chamado</li>
              <li>Coleta de resíduos — dias e horários por bairro</li>
              <li>Ouvidoria (DOM-OUV) — manifestações e LAI</li>
            </ul>
          </section>
        )}
      </main>

      <footer className="portal-footer">
        <small>
          {saude ? `API ${saude.service} v${saude.version} conectada` : 'Portal do Cidadão · Camacan-BA'}
        </small>
      </footer>
    </div>
  );
}

export default PortalCidadao;

