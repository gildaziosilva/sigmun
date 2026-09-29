import { useEffect, useState } from 'react';
import {
  listarImoveisImo,
  listarProprietariosImo,
  listarAvaliacoesImo,
  listarCaracteristicasImo,
  listarGeometriasImo,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { ImoveisImo } from './ImoveisImo';
import { ProprietariosImo } from './ProprietariosImo';
import { AvaliacoesImo } from './AvaliacoesImo';
import { CaracteristicasGeometriasImo } from './CaracteristicasGeometriasImo';
import { VisaoGeralImo } from './VisaoGeralImo';
import type { ExecutarTerr, TerrDataState } from './TerrShared';
import type {
  ImovelImo,
  ProprietarioImo,
  AvaliacaoImo,
  CaracteristicaImo,
  GeometriaImo,
} from '../../lib/api';

const IMO_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'imoveis', rotulo: 'Imóveis (lotes)' },
  { id: 'proprietarios', rotulo: 'Proprietários' },
  { id: 'avaliacoes', rotulo: 'Avaliação de valor venal' },
  { id: 'caracteristicas', rotulo: 'Características e geometria' },
] as const;

type ImoTab = (typeof IMO_TABS)[number]['id'];

export interface ImoResources {
  imoveis: TerrDataState<ImovelImo[]>;
  proprietarios: TerrDataState<ProprietarioImo[]>;
  avaliacoes: TerrDataState<AvaliacaoImo[]>;
  caracteristicas: TerrDataState<CaracteristicaImo[]>;
  geometrias: TerrDataState<GeometriaImo[]>;
  recarregar: () => void;
}

export default function ImoPage() {
  const [aba, setAba] = useState<ImoTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [imoveis, recarregarImoveis] = useApiData(listarImoveisImo);
  const [proprietarios, recarregarProprietarios] = useApiData(listarProprietariosImo);
  const [avaliacoes, recarregarAvaliacoes] = useApiData(listarAvaliacoesImo);
  const [caracteristicas, recarregarCaracteristicas] = useApiData(listarCaracteristicasImo);
  const [geometrias, recarregarGeometrias] = useApiData(listarGeometriasImo);

  function recarregarTudo() {
    recarregarImoveis();
    recarregarProprietarios();
    recarregarAvaliacoes();
    recarregarCaracteristicas();
    recarregarGeometrias();
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

  const recursos: ImoResources = {
    imoveis,
    proprietarios,
    avaliacoes,
    caracteristicas,
    geometrias,
    recarregar: recarregarTudo,
  };
  const executarImo: ExecutarTerr = executar;
  const abaAtiva = IMO_TABS.find((t) => t.id === aba) ?? IMO_TABS[0];

  return (
    <section className="stack terr-shell">
      <div className="page-head terr-page-head">
        <div>
          <p className="terr-eyebrow">DOM-IMO · Cadastro Imobiliário</p>
          <h2 className="section-title">Lotes, proprietários, avaliação de valor venal e georreferenciamento</h2>
          <p className="muted">
            Cadastro imobiliário municipal, vinculado à planta genérica de valores do DOM-TEL.
          </p>
        </div>
        <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>
          Atualizar dados
        </button>
      </div>

      {(mensagem || erro) && (
        <p className={`terr-feedback ${erro ? 'terr-feedback--error' : 'terr-feedback--ok'}`} role={erro ? 'alert' : 'status'}>
          {erro || mensagem}
        </p>
      )}

      <nav className="terr-tabs" aria-label="Áreas do módulo de cadastro imobiliário">
        {IMO_TABS.map((t) => (
          <button
            key={t.id}
            id={`imo-tab-${t.id}`}
            type="button"
            role="tab"
            aria-selected={aba === t.id}
            aria-controls={`imo-painel-${t.id}`}
            className={aba === t.id ? 'terr-tab terr-tab--active' : 'terr-tab'}
            onClick={() => setAba(t.id)}
          >
            {t.rotulo}
          </button>
        ))}
      </nav>

      <div id={`imo-painel-${abaAtiva.id}`} role="tabpanel" aria-labelledby={`imo-tab-${abaAtiva.id}`}>
        {aba === 'visao-geral' && <VisaoGeralImo resources={recursos} />}
        {aba === 'imoveis' && <ImoveisImo resources={recursos} executar={executarImo} salvando={salvando} />}
        {aba === 'proprietarios' && <ProprietariosImo resources={recursos} executar={executarImo} salvando={salvando} />}
        {aba === 'avaliacoes' && <AvaliacoesImo resources={recursos} executar={executarImo} salvando={salvando} />}
        {aba === 'caracteristicas' && (
          <CaracteristicasGeometriasImo resources={recursos} executar={executarImo} salvando={salvando} />
        )}
      </div>
    </section>
  );
}
