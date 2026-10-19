import { useEffect, useState } from 'react';
import type { FormEvent } from 'react';
import {
  abrirDenuncia,
  abrirManifestacao,
  abrirPedidoLai,
  ApiError,
  consultarProtocolo,
  fetchHealth,
  formatProtocolo,
  onUnauthorized,
  type DocumentoPublico,
  type HealthStatus,
  type TipoDenuncia,
  type TipoManifestacao,
} from './lib/api';

type Rota = 'inicio' | 'protocolos' | 'manifestacoes' | 'denuncias' | 'lai' | 'servicos';

function PortalCidadao() {
  const [rota, setRota] = useState<Rota>('inicio');
  const [codigo, setCodigo] = useState('');
  const [resultados, setResultados] = useState<DocumentoPublico[] | null>(null);
  const [buscaErro, setBuscaErro] = useState('');
  const [buscando, setBuscando] = useState(false);
  const [saude, setSaude] = useState<HealthStatus | null>(null);
  const [avisoSessao, setAvisoSessao] = useState('');

  const [manTipo, setManTipo] = useState<TipoManifestacao>('solicitacao');
  const [manAssunto, setManAssunto] = useState('');
  const [manDescricao, setManDescricao] = useState('');
  const [manOrgao, setManOrgao] = useState('');
  const [manNome, setManNome] = useState('');
  const [manAnonimo, setManAnonimo] = useState(false);
  const [manMsg, setManMsg] = useState('');
  const [manErro, setManErro] = useState('');
  const [manEnviando, setManEnviando] = useState(false);

  const [denAssunto, setDenAssunto] = useState('');
  const [denDescricao, setDenDescricao] = useState('');
  const [denTipo, setDenTipo] = useState<TipoDenuncia>('outro');
  const [denLocal, setDenLocal] = useState('');
  const [denData, setDenData] = useState('');
  const [denOrgao, setDenOrgao] = useState('');
  const [denMsg, setDenMsg] = useState('');
  const [denErro, setDenErro] = useState('');
  const [denEnviando, setDenEnviando] = useState(false);

  const [laiAssunto, setLaiAssunto] = useState('');
  const [laiInfo, setLaiInfo] = useState('');
  const [laiFund, setLaiFund] = useState('');
  const [laiNome, setLaiNome] = useState('');
  const [laiOrgao, setLaiOrgao] = useState('');
  const [laiMsg, setLaiMsg] = useState('');
  const [laiErro, setLaiErro] = useState('');
  const [laiEnviando, setLaiEnviando] = useState(false);

  useEffect(() => {
    fetchHealth().then(setSaude).catch(() => undefined);
    onUnauthorized(() => setAvisoSessao('Sessão expirada. Entre novamente.'));
    return () => onUnauthorized(null);
  }, []);

  function erroAmigavel(err: unknown, fallback: string): string {
    if (err instanceof ApiError) return err.friendlyMessage;
    return err instanceof Error ? err.message : fallback;
  }

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
      setBuscaErro(erroAmigavel(err, 'Falha na consulta.'));
    } finally {
      setBuscando(false);
    }
  }

  async function enviarManifestacao(event: FormEvent) {
    event.preventDefault();
    if (!manAssunto.trim() || !manDescricao.trim() || !manOrgao.trim()) {
      setManErro('Preencha assunto, descrição e órgão de destino.');
      return;
    }
    // Regra do domínio: manifestação não anônima exige nome.
    if (!manAnonimo && !manNome.trim()) {
      setManErro('Informe seu nome ou marque a opção de anonimato.');
      return;
    }
    setManErro('');
    setManMsg('');
    setManEnviando(true);
    try {
      const r = await abrirManifestacao({
        tipo: manTipo,
        assunto: manAssunto.trim(),
        descricao: manDescricao.trim(),
        cidadao_nome: manAnonimo ? undefined : manNome.trim(),
        cidadao_anonimo: manAnonimo,
        orgao_destino: manOrgao.trim(),
      });
      setManMsg(`Manifestação registrada! Protocolo ${formatProtocolo(r.protocolo)}.`);
      setManAssunto('');
      setManDescricao('');
    } catch (err) {
      setManErro(erroAmigavel(err, 'Falha ao registrar manifestação.'));
    } finally {
      setManEnviando(false);
    }
  }

  async function enviarDenuncia(event: FormEvent) {
    event.preventDefault();
    if (!denAssunto.trim() || !denDescricao.trim() || !denLocal.trim() || !denData || !denOrgao.trim()) {
      setDenErro('Preencha assunto, descrição, local, data e órgão.');
      return;
    }
    setDenErro('');
    setDenMsg('');
    setDenEnviando(true);
    try {
      const r = await abrirDenuncia({
        assunto: denAssunto.trim(),
        descricao: denDescricao.trim(),
        tipo_denuncia: denTipo,
        local_fato: denLocal.trim(),
        data_fato: denData,
        cidadao_anonimo: true,
        orgao_destino: denOrgao.trim(),
      });
      setDenMsg(`Denúncia sigilosa registrada! Protocolo ${formatProtocolo(r.protocolo)}.`);
      setDenAssunto('');
      setDenDescricao('');
      setDenLocal('');
    } catch (err) {
      setDenErro(erroAmigavel(err, 'Falha ao registrar denúncia.'));
    } finally {
      setDenEnviando(false);
    }
  }

  async function enviarLai(event: FormEvent) {
    event.preventDefault();
    if (!laiAssunto.trim() || !laiInfo.trim() || !laiFund.trim() || !laiNome.trim() || !laiOrgao.trim()) {
      setLaiErro('Preencha todos os campos obrigatórios.');
      return;
    }
    setLaiErro('');
    setLaiMsg('');
    setLaiEnviando(true);
    try {
      const r = await abrirPedidoLai({
        assunto: laiAssunto.trim(),
        descricao: laiInfo.trim(),
        informacao_solicitada: laiInfo.trim(),
        fundamentacao: laiFund.trim(),
        cidadao_nome: laiNome.trim(),
        orgao_destino: laiOrgao.trim(),
      });
      setLaiMsg(`Pedido LAI registrado! Protocolo ${formatProtocolo(r.protocolo)}. Prazo: 20 dias.`);
      setLaiAssunto('');
      setLaiInfo('');
      setLaiFund('');
    } catch (err) {
      setLaiErro(erroAmigavel(err, 'Falha ao registrar pedido LAI.'));
    } finally {
      setLaiEnviando(false);
    }
  }

  return (
    <div className="portal">
      <a className="skip-link" href="#conteudo">Pular para o conteúdo</a>
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
              ['manifestacoes', 'Ouvidoria'],
              ['denuncias', 'Denúncia'],
              ['lai', 'Acesso à Informação'],
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

      <main id="conteudo" className="portal-main" tabIndex={-1}>
        {avisoSessao && <p className="alert alert--error" role="alert">{avisoSessao}</p>}
        {rota === 'inicio' && (
          <section className="portal-hero" aria-labelledby="titulo-inicio">
            <h1 id="titulo-inicio">Serviços digitais da Prefeitura</h1>
            <p>Consulte protocolos, abra manifestações, denuncie com sigilo e peça informações (LAI).</p>
            <div className="hero-actions">
              <button type="button" className="button button--primary" onClick={() => setRota('protocolos')}>
                Consultar protocolo
              </button>
              <button type="button" className="button button--ghost" onClick={() => setRota('manifestacoes')}>
                Abrir manifestação
              </button>
            </div>
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

        {rota === 'manifestacoes' && (
          <section className="card" aria-labelledby="titulo-man">
            <h2 id="titulo-man">Ouvidoria — abrir manifestação</h2>
            <p className="muted">POST /api/v1/ouv/manifestacoes (anônimo permitido).</p>
            <form className="form" onSubmit={enviarManifestacao}>
              <label htmlFor="man-tipo">
                Tipo
                <select id="man-tipo" value={manTipo} onChange={(e) => setManTipo(e.target.value as TipoManifestacao)}>
                  <option value="solicitacao">Solicitação</option>
                  <option value="reclamacao">Reclamação</option>
                  <option value="sugestao">Sugestão</option>
                  <option value="elogio">Elogio</option>
                </select>
              </label>
              <label htmlFor="man-assunto">
                Assunto
                <input id="man-assunto" value={manAssunto} onChange={(e) => setManAssunto(e.target.value)} maxLength={200} required />
              </label>
              <label htmlFor="man-descricao">
                Descrição
                <textarea id="man-descricao" value={manDescricao} onChange={(e) => setManDescricao(e.target.value)} rows={4} required />
              </label>
              <label htmlFor="man-orgao">
                Órgão de destino
                <input id="man-orgao" value={manOrgao} onChange={(e) => setManOrgao(e.target.value)} required />
              </label>
              <label htmlFor="man-nome">
                Seu nome (obrigatório, exceto se anônimo)
                <input id="man-nome" value={manNome} onChange={(e) => setManNome(e.target.value)} disabled={manAnonimo} autoComplete="name" required={!manAnonimo} />
              </label>
              <label className="check" htmlFor="man-anonimo">
                <input id="man-anonimo" type="checkbox" checked={manAnonimo} onChange={(e) => setManAnonimo(e.target.checked)} />
                Quero manifestar anonimamente
              </label>
              {manErro && <p className="alert alert--error" role="alert">{manErro}</p>}
              {manMsg && <output className="alert alert--success">{manMsg}</output>}
              <button type="submit" className="button button--primary" disabled={manEnviando}>
                {manEnviando ? 'Enviando…' : 'Registrar manifestação'}
              </button>
            </form>
          </section>
        )}

        {rota === 'denuncias' && (
          <section className="card" aria-labelledby="titulo-den">
            <h2 id="titulo-den">Denúncia com sigilo</h2>
            <p className="muted">POST /api/v1/ouv/denuncias. Não pedimos identificação.</p>
            <form className="form" onSubmit={enviarDenuncia}>
              <label htmlFor="den-tipo">
                Tipo
                <select id="den-tipo" value={denTipo} onChange={(e) => setDenTipo(e.target.value as TipoDenuncia)}>
                  <option value="outro">Outro</option>
                  <option value="corrupcao">Corrupção</option>
                  <option value="improbidade">Improbidade</option>
                  <option value="assedio">Assédio</option>
                  <option value="desvio_verba">Desvio de verba</option>
                  <option value="nepotismo">Nepotismo</option>
                  <option value="fraude_licitacao">Fraude em licitação</option>
                </select>
              </label>
              <label htmlFor="den-assunto">
                Assunto
                <input id="den-assunto" value={denAssunto} onChange={(e) => setDenAssunto(e.target.value)} maxLength={200} required />
              </label>
              <label htmlFor="den-descricao">
                Descrição do fato
                <textarea id="den-descricao" value={denDescricao} onChange={(e) => setDenDescricao(e.target.value)} rows={4} required />
              </label>
              <label htmlFor="den-local">
                Local do fato
                <input id="den-local" value={denLocal} onChange={(e) => setDenLocal(e.target.value)} required />
              </label>
              <label htmlFor="den-data">
                Data do fato
                <input id="den-data" type="date" value={denData} onChange={(e) => setDenData(e.target.value)} required />
              </label>
              <label htmlFor="den-orgao">
                Órgão de destino
                <input id="den-orgao" value={denOrgao} onChange={(e) => setDenOrgao(e.target.value)} required />
              </label>
              {denErro && <p className="alert alert--error" role="alert">{denErro}</p>}
              {denMsg && <output className="alert alert--success">{denMsg}</output>}
              <button type="submit" className="button button--primary" disabled={denEnviando}>
                {denEnviando ? 'Enviando…' : 'Registrar denúncia sigilosa'}
              </button>
            </form>
          </section>
        )}

        {rota === 'lai' && (
          <section className="card" aria-labelledby="titulo-lai">
            <h2 id="titulo-lai">Acesso à Informação (LAI)</h2>
            <p className="muted">Lei 12.527/2011 · POST /api/v1/ouv/pedidos-lai. Resposta em até 20 dias.</p>
            <form className="form" onSubmit={enviarLai}>
              <label htmlFor="lai-assunto">
                Assunto
                <input id="lai-assunto" value={laiAssunto} onChange={(e) => setLaiAssunto(e.target.value)} maxLength={200} required />
              </label>
              <label htmlFor="lai-info">
                Informação solicitada
                <textarea id="lai-info" value={laiInfo} onChange={(e) => setLaiInfo(e.target.value)} rows={4} required />
              </label>
              <label htmlFor="lai-fund">
                Fundamentação
                <textarea id="lai-fund" value={laiFund} onChange={(e) => setLaiFund(e.target.value)} rows={3} required />
              </label>
              <label htmlFor="lai-nome">
                Seu nome
                <input id="lai-nome" value={laiNome} onChange={(e) => setLaiNome(e.target.value)} autoComplete="name" required />
              </label>
              <label htmlFor="lai-orgao">
                Órgão de destino
                <input id="lai-orgao" value={laiOrgao} onChange={(e) => setLaiOrgao(e.target.value)} required />
              </label>
              {laiErro && <p className="alert alert--error" role="alert">{laiErro}</p>}
              {laiMsg && <output className="alert alert--success">{laiMsg}</output>}
              <button type="submit" className="button button--primary" disabled={laiEnviando}>
                {laiEnviando ? 'Enviando…' : 'Registrar pedido LAI'}
              </button>
            </form>
          </section>
        )}

        {rota === 'servicos' && (
          <section className="card" aria-labelledby="titulo-serv">
            <h2 id="titulo-serv">Serviços públicos</h2>
            <ul className="service-list">
              <li>Iluminação pública — use a Ouvidoria acima (tipo Solicitação)</li>
              <li>Coleta de resíduos — dias e horários por bairro (Central de Atendimento)</li>
              <li>Certidões — solicite presencialmente até o DOM-TRI (Onda 3)</li>
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

