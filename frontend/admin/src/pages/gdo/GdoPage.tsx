import { useEffect, useState } from 'react';
import {
  listarDocumentos,
  obterDocumento,
  listarTramitacoes,
  listarVersoes,
  listarAssinaturas,
  listarTiposDocumentais,
  listarClassificacoes,
  obterProcesso,
  obterTemporalidade,
  type DocumentoGDO,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { DocumentosGdo } from './DocumentosGdo';
import { TramitacoesGdo } from './TramitacoesGdo';
import { VersoesGdo } from './VersoesGdo';
import { ArquivamentosGdo } from './ArquivamentosGdo';
import { AssinaturasGdo } from './AssinaturasGdo';
import { TiposDocumentaisGdo } from './TiposDocumentaisGdo';
import { ClassificacoesGdo } from './ClassificacoesGdo';
import { ProcessosGdo } from './ProcessosGdo';
import { TemporalidadesGdo } from './TemporalidadesGdo';
import { GDO_TABS, type GdoResources, type GdoTab } from './GdoShared';
import { formatarData, tipoDocumentalNome } from './GdoShared';

export default function GdoPage() {
  const [aba, setAba] = useState<GdoTab>('documentos');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);
  const [detalheDocumento, setDetalheDocumento] = useState<DocumentoGDO | null>(null);

  const [documentos, recarregarDocumentos] = useApiData(() =>
    listarDocumentos().then((r) => ({ items: r.items, total: r.total, page: r.page, page_size: r.page_size })),
  );
  const [tramitacoes] = useApiData(() => listarTramitacoes(''));
  const [versoes] = useApiData(() => listarVersoes(''));
  const [assinaturas] = useApiData(() => listarAssinaturas(''));
  const [tiposDocumentais, recarregarTiposDocumentais] = useApiData(listarTiposDocumentais);
  const [classificacoes, recarregarClassificacoes] = useApiData(() =>
    listarClassificacoes().then((r) => ({ items: r.items, total: r.total, page: r.page, page_size: r.page_size })),
  );
  const [processos] = useApiData(() => obterProcesso(''));
  const [temporalidades] = useApiData(() => obterTemporalidade(''));

  function recarregarTudo() {
    recarregarDocumentos();
    recarregarTiposDocumentais();
    recarregarClassificacoes();
    setMensagem('');
    setErro('');
  }

  useEffect(() => {
    recarregarTudo();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function executar(acao: () => Promise<unknown>, sucesso: string): Promise<boolean> {
    if (salvando) return false;
    setSalvando(true);
    setErro('');
    setMensagem('');
    try {
      await acao();
      setMensagem(sucesso);
      recarregarTudo();
      return true;
    } catch (falha) {
      setErro(falha instanceof Error ? falha.message : 'Não foi possível concluir a operação.');
      return false;
    } finally {
      setSalvando(false);
    }
  }

  const resources: GdoResources = {
    documentos,
    tramitacoes,
    versoes,
    arquivamentos: { data: null, loading: false, erro: '' },
    assinaturas,
    tiposDocumentais,
    classificacoes,
    processos: { data: processos.data ? [processos.data] : null, loading: processos.loading, erro: processos.erro },
    temporalidades: { data: temporalidades.data ? [temporalidades.data] : null, loading: temporalidades.loading, erro: temporalidades.erro },
    recarregar: recarregarTudo,
  };

  async function verDetalhe(id: string) {
    setErro('');
    try {
      setDetalheDocumento(await obterDocumento(id));
    } catch (err) {
      setErro(err instanceof Error ? err.message : 'Falha ao carregar documento.');
    }
  }

  return (
    <section className="stack gdo-shell">
      <div className="page-head gdo-page-head">
        <div>
          <p className="gdo-eyebrow">DOM-GDO · Gestão Documental</p>
          <h2 className="section-title">Documentos, tramitações, versionamento, arquivamento e assinaturas</h2>
          <p className="muted">Gestão integrada do ciclo de vida documental municipal.</p>
        </div>
        <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>
          Atualizar dados
        </button>
      </div>

      {(mensagem || erro) && (
        <p className={`gdo-feedback ${erro ? 'gdo-feedback--error' : 'gdo-feedback--ok'}`} role={erro ? 'alert' : 'status'}>
          {erro || mensagem}
        </p>
      )}

      <nav className="gdo-tabs" aria-label="Áreas do módulo de gestão documental">
        {GDO_TABS.map((tab) => (
          <button
            key={tab.id}
            id={`gdo-tab-${tab.id}`}
            type="button"
            role="tab"
            aria-selected={aba === tab.id}
            aria-controls={`gdo-painel-${tab.id}`}
            className={aba === tab.id ? 'gdo-tab gdo-tab--active' : 'gdo-tab'}
            onClick={() => setAba(tab.id)}
          >
            {tab.rotulo}
          </button>
        ))}
      </nav>

      <div id={`gdo-painel-${aba}`} role="tabpanel" aria-labelledby={`gdo-tab-${aba}`}>
        {aba === 'documentos' && <DocumentosGdo resources={resources} executar={executar} salvando={salvando} onVerDetalhe={verDetalhe} />}
        {aba === 'tramitacoes' && <TramitacoesGdo resources={resources} executar={executar} salvando={salvando} />}
        {aba === 'versoes' && <VersoesGdo resources={resources} executar={executar} salvando={salvando} />}
        {aba === 'arquivamentos' && <ArquivamentosGdo executar={executar} salvando={salvando} />}
        {aba === 'assinaturas' && <AssinaturasGdo resources={resources} executar={executar} salvando={salvando} />}
        {aba === 'tipos-documentais' && <TiposDocumentaisGdo executar={executar} salvando={salvando} />}
        {aba === 'classificacoes' && <ClassificacoesGdo executar={executar} salvando={salvando} />}
        {aba === 'processos' && <ProcessosGdo />}
        {aba === 'temporalidades' && <TemporalidadesGdo />}
      </div>

      {detalheDocumento && (
        <article className="card card--detail gdo-detail-overlay">
          <h3>
            {detalheDocumento.codigo} — {detalheDocumento.titulo}
            <button type="button" className="link link--close" onClick={() => setDetalheDocumento(null)}>
              Fechar
            </button>
          </h3>
          <dl className="detail-list">
            <div>
              <dt>Número/Ano</dt>
              <dd>{detalheDocumento.numero}/{detalheDocumento.ano}</dd>
            </div>
            <div>
              <dt>Tipo documental</dt>
              <dd className="mono">{tipoDocumentalNome(resources, detalheDocumento.tipo_documental_id)}</dd>
            </div>
            <div>
              <dt>Unidade autora</dt>
              <dd className="mono">{detalheDocumento.unidade_autor_id}</dd>
            </div>
            <div>
              <dt>Status</dt>
              <dd>
                <span className="badge">{detalheDocumento.status}</span>
                {detalheDocumento.is_sigiloso && <span className="badge badge--warn">sigiloso</span>}
              </dd>
            </div>
            <div>
              <dt>Descrição</dt>
              <dd>{detalheDocumento.descricao || '—'}</dd>
            </div>
            <div>
              <dt>Criado em</dt>
              <dd>{formatarData(detalheDocumento.created_at)}</dd>
            </div>
          </dl>
        </article>
      )}
    </section>
  );
}