import { useEffect, useState } from 'react';
import {
  listarFamiliasAss,
  listarPessoasAss,
  listarUnidadesAss,
  listarBeneficiosAss,
  listarAtendimentosAss,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { FamiliasAss } from './FamiliasAss';
import { PessoasAss } from './PessoasAss';
import { UnidadesAss } from './UnidadesAss';
import { BeneficiosAss } from './BeneficiosAss';
import { AtendimentosAss } from './AtendimentosAss';
import { ASS_TABS, type AssResources, type AssTab } from './AssShared';
import { VisaoGeralAss } from './VisaoGeralAss';

export default function AssPage() {
  const [aba, setAba] = useState<AssTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [familias, recarregarFamilias] = useApiData(listarFamiliasAss);
  const [pessoas, recarregarPessoas] = useApiData(listarPessoasAss);
  const [unidades, recarregarUnidades] = useApiData(listarUnidadesAss);
  const [beneficios, recarregarBeneficios] = useApiData(listarBeneficiosAss);
  const [atendimentos, recarregarAtendimentos] = useApiData(listarAtendimentosAss);

  function recarregarTudo() {
    recarregarFamilias();
    recarregarPessoas();
    recarregarUnidades();
    recarregarBeneficios();
    recarregarAtendimentos();
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

  const resources: AssResources = {
    familias,
    pessoas,
    unidades,
    beneficios,
    atendimentos,
    recarregar: recarregarTudo,
  };

  return <section className="stack ass-shell">
    <div className="page-head ass-page-head">
      <div>
        <p className="ass-eyebrow">DOM-ASS · Assistência Social</p>
        <h2 className="section-title">CadÚnico local, benefícios eventuais, CRAS/CREAS</h2>
        <p className="muted">Gestão integrada dos serviços de assistência social da rede municipal.</p>
      </div>
      <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>Atualizar dados</button>
    </div>

    {(mensagem || erro) && <p className={`ass-feedback ${erro ? 'ass-feedback--error' : 'ass-feedback--ok'}`} role={erro ? 'alert' : 'status'}>{erro || mensagem}</p>}

    <nav className="ass-tabs" aria-label="Áreas do módulo de assistência social">
      {ASS_TABS.map((tab) => <button key={tab.id} id={`ass-tab-${tab.id}`} type="button" role="tab" aria-selected={aba === tab.id} aria-controls={`ass-painel-${tab.id}`} className={aba === tab.id ? 'ass-tab ass-tab--active' : 'ass-tab'} onClick={() => setAba(tab.id)}>{tab.rotulo}</button>)}
    </nav>

    <div id={`ass-painel-${aba}`} role="tabpanel" aria-labelledby={`ass-tab-${aba}`}>
      {aba === 'visao-geral' && <VisaoGeralAss resources={resources} />}
      {aba === 'familias' && <FamiliasAss resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'pessoas' && <PessoasAss resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'unidades' && <UnidadesAss resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'beneficios' && <BeneficiosAss resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'atendimentos' && <AtendimentosAss resources={resources} executar={executar} salvando={salvando} />}
    </div>
  </section>;
}