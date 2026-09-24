import { useEffect, useState } from 'react';
import {
  listarAgendamentosSau,
  listarMedicamentosSau,
  listarPacientesSau,
  listarRegulacoesSau,
} from '../../lib/api';
import { useApiData } from '../../components/DataState';
import { AgendaSau } from './AgendaSau';
import { FarmaciaSau } from './FarmaciaSau';
import { ProntuarioSau } from './ProntuarioSau';
import { RegulacaoSau } from './RegulacaoSau';
import { SAU_TABS, type SauResources, type SauTab } from './SauShared';
import { VisaoGeralSau } from './VisaoGeralSau';

export default function SauPage() {
  const [aba, setAba] = useState<SauTab>('visao-geral');
  const [mensagem, setMensagem] = useState('');
  const [erro, setErro] = useState('');
  const [salvando, setSalvando] = useState(false);
  const [pacientes, recarregarPacientes] = useApiData(listarPacientesSau);
  const [agendamentos, recarregarAgendamentos] = useApiData(listarAgendamentosSau);
  const [regulacoes, recarregarRegulacoes] = useApiData(listarRegulacoesSau);
  const [medicamentos, recarregarMedicamentos] = useApiData(listarMedicamentosSau);

  function recarregarTudo() {
    recarregarPacientes();
    recarregarAgendamentos();
    recarregarRegulacoes();
    recarregarMedicamentos();
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

  const resources: SauResources = {
    pacientes,
    agendamentos,
    regulacoes,
    medicamentos,
    recarregar: recarregarTudo,
  };

  return <section className="stack sau-shell">
    <div className="page-head sau-page-head">
      <div>
        <p className="sau-eyebrow">DOM-SAU · Saúde Municipal</p>
        <h2 className="section-title">Prontuário, agenda, regulação e farmácia</h2>
        <p className="muted">Gestão integrada dos serviços de saúde da rede municipal.</p>
      </div>
      <button type="button" className="button button--ghost" onClick={recarregarTudo} disabled={salvando}>Atualizar dados</button>
    </div>

    {(mensagem || erro) && <p className={`sau-feedback ${erro ? 'sau-feedback--error' : 'sau-feedback--ok'}`} role={erro ? 'alert' : 'status'}>{erro || mensagem}</p>}

    <nav className="sau-tabs" aria-label="Áreas do módulo de saúde">
      {SAU_TABS.map((tab) => <button key={tab.id} id={`sau-tab-${tab.id}`} type="button" role="tab" aria-selected={aba === tab.id} aria-controls={`sau-painel-${tab.id}`} className={aba === tab.id ? 'sau-tab sau-tab--active' : 'sau-tab'} onClick={() => setAba(tab.id)}>{tab.rotulo}</button>)}
    </nav>

    <div id={`sau-painel-${aba}`} role="tabpanel" aria-labelledby={`sau-tab-${aba}`}>
      {aba === 'visao-geral' && <VisaoGeralSau resources={resources} />}
      {aba === 'prontuario' && <ProntuarioSau resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'agenda' && <AgendaSau resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'regulacao' && <RegulacaoSau resources={resources} executar={executar} salvando={salvando} />}
      {aba === 'farmacia' && <FarmaciaSau resources={resources} executar={executar} salvando={salvando} />}
    </div>
  </section>;
}
