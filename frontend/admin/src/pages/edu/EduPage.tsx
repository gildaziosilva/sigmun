import { useEffect, useState } from 'react';
import {
  listarAlunos,
  listarMatriculas,
  listarRotasTransporte,
  listarItensMerenda,
  listarDistribuicoesMerenda,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { AlunosTab } from './tabs/AlunosTab';
import { MatriculasTab } from './tabs/MatriculasTab';
import { DiarioTab } from './tabs/DiarioTab';
import { TransporteTab } from './tabs/TransporteTab';
import { MerendaTab } from './tabs/MerendaTab';
import { VisaoGeralEdu } from './VisaoGeralEdu';
import { EDU_TABS, type EduResources, type EduTab } from './EduShared';


export default function EduPage() {
  const [aba, setAba] = useState<EduTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);

  const [alunos, recarregarAlunos] = useApiData(listarAlunos);
  const [matriculas, recarregarMatriculas] = useApiData(listarMatriculas);
  const [rotas, recarregarRotas] = useApiData(listarRotasTransporte);
  const [itensMerenda, recarregarItensMerenda] = useApiData(listarItensMerenda);
  const [distribuicoes, recarregarDistribuicoes] = useApiData(listarDistribuicoesMerenda);

  function recarregarTudo() {
    recarregarAlunos();
    recarregarMatriculas();
    recarregarRotas();
    recarregarItensMerenda();
    recarregarDistribuicoes();
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

  const resources: EduResources = {
    alunos,
    matriculas,
    lancamentos: { data: null, loading: false, erro: '' },
    rotas,
    passagens: { data: null, loading: false, erro: '' },
    itensMerenda,
    distribuicoes,
    recarregar: recarregarTudo,
  };

  return (
    <section className="stack sau-shell">
      <div className="page-head sau-page-head">
        <div>
          <p className="sau-eyebrow">DOM-EDU · Educação Municipal</p>
          <h2 className="section-title">Alunos, matrículas, diário, transporte e merenda</h2>
          <p className="muted">Gestão integrada dos serviços de educação da rede municipal.</p>
        </div>
        <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>Atualizar dados</button>
      </div>

      {(mensagem || erro) && <p className={`sau-feedback ${erro ? 'sau-feedback--error' : 'sau-feedback--ok'}`} role={erro ? 'alert' : 'status'}>{erro || mensagem}</p>}

      <nav className="sau-tabs" aria-label="Áreas do módulo de educação">
        {EDU_TABS.map((tab) => (
          <button
            key={tab.id}
            id={`edu-tab-${tab.id}`}
            type="button"
            role="tab"
            aria-selected={aba === tab.id}
            aria-controls={`edu-painel-${tab.id}`}
            className={aba === tab.id ? 'sau-tab sau-tab--active' : 'sau-tab'}
            onClick={() => setAba(tab.id)}
          >
            {tab.rotulo}
          </button>
        ))}
      </nav>

      <div id={`edu-painel-${aba}`} role="tabpanel" aria-labelledby={`edu-tab-${aba}`}>
        {aba === 'visao-geral' && <VisaoGeralEdu resources={resources} />}
        {aba === 'alunos' && <AlunosTab resources={resources} executar={executar} salvando={salvando} />}
        {aba === 'matriculas' && <MatriculasTab resources={resources} />}
        {aba === 'diario' && <DiarioTab resources={resources} executar={executar} salvando={salvando} />}
        {aba === 'transporte' && <TransporteTab resources={resources} />}
        {aba === 'merenda' && <MerendaTab resources={resources} />}
      </div>
    </section>
  );
}
