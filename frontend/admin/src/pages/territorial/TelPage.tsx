import { useEffect, useState } from 'react';
import {
  listarBairrosTel,
  listarLogradourosTel,
  listarPlantasValoresTel,
  listarGeorreferenciasTel,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { BairrosTel } from './BairrosTel';
import { LogradourosTel } from './LogradourosTel';
import { PlantasValoresTel } from './PlantasValoresTel';
import { GeorreferenciasTel } from './GeorreferenciasTel';
import { ConsultasTel } from './ConsultasTel';
import { VisaoGeralTel } from './VisaoGeralTel';
import type { ExecutarTerr, TerrDataState } from './TerrShared';
import type {
  BairroTel,
  LogradouroTel,
  PlantaValoresTel,
  GeorreferenciaTel,
} from '../../lib/api';

const TEL_TABS = [
  { id: 'visao-geral', rotulo: 'Visão geral' },
  { id: 'bairros', rotulo: 'Bairros' },
  { id: 'logradouros', rotulo: 'Logradouros' },
  { id: 'plantas-valores', rotulo: 'Planta de valores' },
  { id: 'georreferencias', rotulo: 'Georreferenciamento' },
  { id: 'consultas', rotulo: 'Consultas' },
] as const;

type TelTab = (typeof TEL_TABS)[number]['id'];

export interface TelResources {
  bairros: TerrDataState<BairroTel[]>;
  logradouros: TerrDataState<LogradouroTel[]>;
  plantas: TerrDataState<PlantaValoresTel[]>;
  georreferencias: TerrDataState<GeorreferenciaTel[]>;
  recarregar: () => void;
}

export default function TelPage() {
  const [aba, setAba] = useState<TelTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [bairros, recarregarBairros] = useApiData(listarBairrosTel);
  const [logradouros, recarregarLogradouros] = useApiData(listarLogradourosTel);
  const [plantas, recarregarPlantas] = useApiData(listarPlantasValoresTel);
  const [georreferencias, recarregarGeorreferencias] = useApiData(listarGeorreferenciasTel);

  function recarregarTudo() {
    recarregarBairros();
    recarregarLogradouros();
    recarregarPlantas();
    recarregarGeorreferencias();
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

  const recursos: TelResources = {
    bairros,
    logradouros,
    plantas,
    georreferencias,
    recarregar: recarregarTudo,
  };
  const executarTel: ExecutarTerr = executar;

  const abaAtiva = TEL_TABS.find((t) => t.id === aba) ?? TEL_TABS[0];

  return (
    <section className="stack terr-shell">
      <div className="page-head terr-page-head">
        <div>
          <p className="terr-eyebrow">DOM-TEL · Gestão Territorial</p>
          <h2 className="section-title">Bairros, logradouros, planta de valores e georreferenciamento</h2>
          <p className="muted">
            Base territorial e tabela de valores da Prefeitura Municipal de Camacan-BA.
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

      <nav className="terr-tabs" aria-label="Áreas do módulo de gestão territorial">
        {TEL_TABS.map((t) => (
          <button
            key={t.id}
            id={`tel-tab-${t.id}`}
            type="button"
            role="tab"
            aria-selected={aba === t.id}
            aria-controls={`tel-painel-${t.id}`}
            className={aba === t.id ? 'terr-tab terr-tab--active' : 'terr-tab'}
            onClick={() => setAba(t.id)}
          >
            {t.rotulo}
          </button>
        ))}
      </nav>

      <div id={`tel-painel-${abaAtiva.id}`} role="tabpanel" aria-labelledby={`tel-tab-${abaAtiva.id}`}>
        {aba === 'visao-geral' && <VisaoGeralTel resources={recursos} />}
        {aba === 'bairros' && <BairrosTel resources={recursos} executar={executarTel} salvando={salvando} />}
        {aba === 'logradouros' && <LogradourosTel resources={recursos} executar={executarTel} salvando={salvando} />}
        {aba === 'plantas-valores' && <PlantasValoresTel resources={recursos} executar={executarTel} salvando={salvando} />}
        {aba === 'georreferencias' && <GeorreferenciasTel resources={recursos} executar={executarTel} salvando={salvando} />}
        {aba === 'consultas' && <ConsultasTel resources={recursos} executar={executarTel} salvando={salvando} />}
      </div>
    </section>
  );
}
