import { useEffect, useState } from 'react';
import { listarObras } from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { VisaoGeralObras } from './VisaoGeralObras';
import { ObrasObras } from './ObrasLista';
import { MedicoesObras } from './MedicoesObras';
import { DespesasObras } from './DespesasObras';
import { EtapasObras } from './EtapasObras';
import { VistoriasObras } from './VistoriasObras';
import type { ExecutarObras, ObrasDataState } from './ObrasShared';
import type { Obra } from '../../lib/api';

const OBRAS_TABS = [
  { id: 'visao-geral', rotulo: 'Visao geral' },
  { id: 'obras', rotulo: 'Obras' },
  { id: 'medicoes', rotulo: 'Medicoes' },
  { id: 'despesas', rotulo: 'Despesas' },
  { id: 'etapas', rotulo: 'Etapas' },
  { id: 'vistorias', rotulo: 'Vistorias' },
] as const;

type ObrasTab = (typeof OBRAS_TABS)[number]['id'];

export interface ObrasPageResources {
  obras: ObrasDataState<Obra[]>;
  recarregar: () => void;
}

export default function ObrasPage() {
  const [aba, setAba] = useState<ObrasTab>('visao-geral');
  const [obraSelecionada, setObraSelecionada] = useState('');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [obras, recarregarObras] = useApiData(listarObras);

  function recarregarTudo() {
    recarregarObras();
    setMensagem('');
    setErro('');
  }

  useEffect(() => {
    recarregarObras();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Mantem a selecao valida quando a lista de obras muda.
  useEffect(() => {
    const lista = obras.data ?? [];
    if (lista.length === 0) {
      setObraSelecionada('');
      return;
    }
    if (!obraSelecionada || !lista.some((o) => o.id === obraSelecionada)) {
      setObraSelecionada(lista[0].id);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [obras.data]);

  async function executar(acao: () => Promise<unknown>, sucesso: string): Promise<boolean> {
    if (salvando) return false;
    setSalvando(true);
    setErro('');
    setMensagem('');
    try {
      await acao();
      setMensagem(sucesso);
      recarregarObras();
      return true;
    } catch (falha) {
      setErro(falha instanceof Error ? falha.message : 'Nao foi possivel concluir a operacao.');
      return false;
    } finally {
      setSalvando(false);
    }
  }

  const recursos: ObrasPageResources = { obras, recarregar: recarregarTudo };
  const executarObras: ExecutarObras = executar;
  const abaAtiva = OBRAS_TABS.find((t) => t.id === aba) ?? OBRAS_TABS[0];

  const abaComObra = (node: React.ReactNode) => (
    <div className="obras-contexto">
      <label className="obras-seletor">
        <span>Obra</span>
        <select
          value={obraSelecionada}
          onChange={(event) => setObraSelecionada(event.target.value)}
        >
          {(obras.data ?? []).map((o) => (
            <option key={o.id} value={o.id}>
              {o.numero} — {o.nome}
            </option>
          ))}
        </select>
      </label>
      {obraSelecionada ? node : <p className="muted">Selecione uma obra para continuar.</p>}
    </div>
  );

  return (
    <section className="stack obras-shell">
      <div className="page-head obras-page-head">
        <div>
          <p className="obras-eyebrow">DOM-OBR &middot; Obras e Infraestrutura</p>
          <h2 className="section-title">Acompanhamento fisico-financeiro de obras publicas</h2>
          <p className="muted">
            Medicoes, despesas, etapas e vistorias da Prefeitura Municipal de Camacan-BA.
          </p>
        </div>
        <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>
          Atualizar dados
        </button>
      </div>

      {(mensagem || erro) && (
        <p className={`obras-feedback ${erro ? 'obras-feedback--error' : 'obras-feedback--ok'}`} role={erro ? 'alert' : 'status'}>
          {erro || mensagem}
        </p>
      )}

      <nav className="obras-tabs" aria-label="Areas do modulo de obras">
        {OBRAS_TABS.map((t) => (
          <button
            key={t.id}
            id={`obras-tab-${t.id}`}
            type="button"
            role="tab"
            aria-selected={aba === t.id}
            aria-controls={`obras-painel-${t.id}`}
            className={aba === t.id ? 'obras-tab obras-tab--active' : 'obras-tab'}
            onClick={() => setAba(t.id)}
          >
            {t.rotulo}
          </button>
        ))}
      </nav>

      <div id={`obras-painel-${abaAtiva.id}`} role="tabpanel" aria-labelledby={`obras-tab-${abaAtiva.id}`}>
        {aba === 'visao-geral' && <VisaoGeralObras resources={recursos} />}
        {aba === 'obras' && <ObrasObras resources={recursos} executar={executarObras} salvando={salvando} />}
        {aba === 'medicoes' &&
          abaComObra(
            <MedicoesObras
              obraId={obraSelecionada}
              executar={executarObras}
              salvando={salvando}
            />,
          )}
        {aba === 'despesas' &&
          abaComObra(
            <DespesasObras obraId={obraSelecionada} executar={executarObras} salvando={salvando} />,
          )}
        {aba === 'etapas' &&
          abaComObra(
            <EtapasObras obraId={obraSelecionada} executar={executarObras} salvando={salvando} />,
          )}
        {aba === 'vistorias' &&
          abaComObra(
            <VistoriasObras obraId={obraSelecionada} executar={executarObras} salvando={salvando} />,
          )}
      </div>
    </section>
  );
}
