import { useEffect, useState } from 'react';
import {
  listarCamadasGeo,
  listarMapasGeo,
  listarServicosGeo,
  listarTodasFeaturesGeo,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { CamadasGeo } from './CamadasGeo';
import { MapasGeo } from './MapasGeo';
import { FeaturesGeo } from './FeaturesGeo';
import { ServicosGeo } from './ServicosGeo';
import { VisaoGeralGeo } from './VisaoGeralGeo';
import type { ExecutarGeo, GeoDataState } from './GeoShared';
import type { CamadaGeo, FeatureGeo, MapaSigGeo, ServicoGeo } from '../../lib/api';

const GEO_TABS = [
  { id: 'visao-geral', rotulo: 'Visao geral' },
  { id: 'camadas', rotulo: 'Camadas' },
  { id: 'mapas', rotulo: 'Mapas SIG' },
  { id: 'features', rotulo: 'Elementos' },
  { id: 'servicos', rotulo: 'Servicos' },
] as const;

type GeoTab = (typeof GEO_TABS)[number]['id'];

export interface GeoPageResources {
  camadas: GeoDataState<CamadaGeo[]>;
  mapas: GeoDataState<MapaSigGeo[]>;
  features: GeoDataState<FeatureGeo[]>;
  servicos: GeoDataState<ServicoGeo[]>;
  recarregar: () => void;
}

export default function GeoPage() {
  const [aba, setAba] = useState<GeoTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [camadas, recarregarCamadas] = useApiData(listarCamadasGeo);
  const [mapas, recarregarMapas] = useApiData(listarMapasGeo);
  const [features, recarregarFeatures] = useApiData(listarTodasFeaturesGeo);
  const [servicos, recarregarServicos] = useApiData(listarServicosGeo);

  function recarregarTudo() {
    recarregarCamadas();
    recarregarMapas();
    recarregarFeatures();
    recarregarServicos();
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
      setErro(falha instanceof Error ? falha.message : 'Nao foi possivel concluir a operacao.');
      return false;
    } finally {
      setSalvando(false);
    }
  }

  const recursos: GeoPageResources = {
    camadas,
    mapas,
    features,
    servicos,
    recarregar: recarregarTudo,
  };
  const executarGeo: ExecutarGeo = executar;
  const abaAtiva = GEO_TABS.find((t) => t.id === aba) ?? GEO_TABS[0];

  return (
    <section className="stack geo-shell">
      <div className="page-head geo-page-head">
        <div>
          <p className="geo-eyebrow">DOM-GEO &middot; Geoinformacao Municipal</p>
          <h2 className="section-title">Mapas SIG, camadas e servicos geoespaciais</h2>
          <p className="muted">
            Geoportal municipal da Prefeitura Municipal de Camacan-BA.
          </p>
        </div>
        <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>
          Atualizar dados
        </button>
      </div>

      {(mensagem || erro) && (
        <p className={`geo-feedback ${erro ? 'geo-feedback--error' : 'geo-feedback--ok'}`} role={erro ? 'alert' : 'status'}>
          {erro || mensagem}
        </p>
      )}

      <nav className="geo-tabs" aria-label="Areas do modulo de geoinformacao">
        {GEO_TABS.map((t) => (
          <button
            key={t.id}
            id={`geo-tab-${t.id}`}
            type="button"
            role="tab"
            aria-selected={aba === t.id}
            aria-controls={`geo-painel-${t.id}`}
            className={aba === t.id ? 'geo-tab geo-tab--active' : 'geo-tab'}
            onClick={() => setAba(t.id)}
          >
            {t.rotulo}
          </button>
        ))}
      </nav>

      <div id={`geo-painel-${abaAtiva.id}`} role="tabpanel" aria-labelledby={`geo-tab-${abaAtiva.id}`}>
        {aba === 'visao-geral' && <VisaoGeralGeo resources={recursos} />}
        {aba === 'camadas' && <CamadasGeo resources={recursos} executar={executarGeo} salvando={salvando} />}
        {aba === 'mapas' && <MapasGeo resources={recursos} executar={executarGeo} salvando={salvando} />}
        {aba === 'features' && <FeaturesGeo resources={recursos} executar={executarGeo} salvando={salvando} />}
        {aba === 'servicos' && <ServicosGeo resources={recursos} executar={executarGeo} salvando={salvando} />}
      </div>
    </section>
  );
}
