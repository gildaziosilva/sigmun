import { useState, type FormEvent } from 'react';
import { TabelaEstado } from '../../components/DataState';
import {
  registrarDenunciaOuv,
  responderManifestacaoOuv,
  alterarStatusOuv,
  prorrogarPrazoOuv,
  encaminharDenunciaOuv,
  type DenunciaOuv,
} from '../../lib/api';
import { StatusBadge,
  PrioridadeBadge,
  TipoDenunciaBadge,
  PrazoBadge,
  CanalBadge,
  Field,
  SelectField,
  TextAreaField,
  getProtocolo,
  getCidadaoNome,
  type OuvResources,
  type ExecutarOuv,
} from './OuvShared';

const TIPOS_DENUNCIA = [
  { value: 'corrupcao', label: 'Corrupção' },
  { value: 'improbidade', label: 'Improbidade' },
  { value: 'assedio', label: 'Assédio' },
  { value: 'desvio_verba', label: 'Desvio de Verba' },
  { value: 'nepotismo', label: 'Nepotismo' },
  { value: 'fraude_licitacao', label: 'Fraude em Licitação' },
  { value: 'outro', label: 'Outro' },
] as const;

const CANAIS = [
  { value: 'portal_cidadao', label: 'Portal do Cidadão' },
  { value: 'presencial', label: 'Presencial' },
  { value: 'telefone', label: 'Telefone' },
  { value: 'email', label: 'E-mail' },
  { value: 'correios', label: 'Correios' },
  { value: 'aplicativo', label: 'Aplicativo' },
  { value: 'outro', label: 'Outro' },
] as const;

const PRIORIDADES = [
  { value: 'baixa', label: 'Baixa' },
  { value: 'normal', label: 'Normal' },
  { value: 'alta', label: 'Alta' },
  { value: 'urgente', label: 'Urgente' },
] as const;

const STATUSES = [
  { value: 'registrada', label: 'Registrada' },
  { value: 'em_analise', label: 'Em Análise' },
  { value: 'encaminhada', label: 'Encaminhada' },
  { value: 'em_tratamento', label: 'Em Tratamento' },
  { value: 'aguardando_complementacao', label: 'Aguardando Complementação' },
  { value: 'respondida', label: 'Respondida' },
  { value: 'concluida', label: 'Concluída' },
  { value: 'arquivada', label: 'Arquivada' },
  { value: 'cancelada', label: 'Cancelada' },
] as const;

const ORGAOS_EXTERNOS = [
  { value: 'MP', label: 'Ministério Público' },
  { value: 'PF', label: 'Polícia Federal' },
  { value: 'TCE', label: 'Tribunal de Contas do Estado' },
  { value: 'TCU', label: 'Tribunal de Contas da União' },
  { value: 'CGU', label: 'Controladoria-Geral da União' },
] as const;

export function DenunciasOuv({ resources, executar, salvando }: { resources: OuvResources; executar: ExecutarOuv; salvando: boolean }) {
  const [assunto, setAssunto] = useState('');
  const [descricao, setDescricao] = useState('');
  const [tipo_denuncia, setTipoDenuncia] = useState('outro');
  const [envolve_servidor_publico, setEnvolveServidorPublico] = useState(false);
  const [servidor_envolvido, setServidorEnvolvido] = useState('');
  const [valor_envolvido, setValorEnvolvido] = useState('');
  const [local_fato, setLocalFato] = useState('');
  const [data_fato, setDataFato] = useState('');
  const [cidadao_nome, setCidadaoNome] = useState('');
  const [cidadao_cpf, setCidadaoCpf] = useState('');
  const [cidadao_email, setCidadaoEmail] = useState('');
  const [cidadao_telefone, setCidadaoTelefone] = useState('');
  const [cidadao_endereco, setCidadaoEndereco] = useState('');
  const [cidadao_anonimo, setCidadaoAnonimo] = useState(true);
  const [canal, setCanal] = useState('portal_cidadao');
  const [orgao_destino, setOrgaoDestino] = useState('');
  const [setor_responsavel, setSetorResponsavel] = useState('');
  const [prioridade, setPrioridade] = useState('alta');
  const [filtroStatus, setFiltroStatus] = useState('todos');
  const [filtroTipo, setFiltroTipo] = useState('todos');

  const denuncias = resources.denuncias.data ?? [];
  const filtradas = denuncias.filter((d) => {
    const okStatus = filtroStatus === 'todos' || d.status === filtroStatus;
    const okTipo = filtroTipo === 'todos' || d.tipo_denuncia === filtroTipo;
    return okStatus && okTipo;
  });

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!assunto.trim() || !descricao.trim() || !local_fato.trim() || !data_fato || !orgao_destino.trim()) {
      alert('Preencha os campos obrigatórios');
      return;
    }
    const ok = await executar(
      () =>
        registrarDenunciaOuv({
          assunto: assunto.trim(),
          descricao: descricao.trim(),
          tipo_denuncia,
          envolve_servidor_publico,
          servidor_envolvido: servidor_envolvido.trim(),
          valor_envolvido: valor_envolvido ? parseFloat(valor_envolvido) : undefined,
          local_fato: local_fato.trim(),
          data_fato,
          cidadao_nome: cidadao_nome.trim(),
          cidadao_cpf: cidadao_cpf.trim(),
          cidadao_email: cidadao_email.trim(),
          cidadao_telefone: cidadao_telefone.trim(),
          cidadao_endereco: cidadao_endereco.trim(),
          cidadao_anonimo,
          canal,
          orgao_destino: orgao_destino.trim(),
          setor_responsavel: setor_responsavel.trim(),
          prioridade,
          anexos: [],
        }),
      'Denúncia registrada com sucesso.'
    );
    if (ok) {
      setAssunto('');
      setDescricao('');
      setTipoDenuncia('outro');
      setEnvolveServidorPublico(false);
      setServidorEnvolvido('');
      setValorEnvolvido('');
      setLocalFato('');
      setDataFato('');
      setCidadaoNome('');
      setCidadaoCpf('');
      setCidadaoEmail('');
      setCidadaoTelefone('');
      setCidadaoEndereco('');
      setCidadaoAnonimo(true);
      setOrgaoDestino('');
      setSetorResponsavel('');
    }
  }

  async function responder(d: DenunciaOuv) {
    const resposta = prompt('Resposta ao denunciante:');
    if (!resposta) return;
    const forma = prompt('Forma de resposta (portal/email/correios/presencial/telefone):', 'portal');
    if (!forma) return;
    await executar(() => responderManifestacaoOuv(d.id, resposta, forma), 'Resposta registrada.');
  }

  async function mudarStatus(d: DenunciaOuv, novoStatus: string) {
    const obs = prompt('Observação (opcional):', '');
    await executar(() => alterarStatusOuv(d.id, novoStatus, obs || ''), `Status alterado para ${novoStatus}.`);
  }

  async function prorrogar(d: DenunciaOuv) {
    const justificativa = prompt('Justificativa da prorrogação:');
    if (!justificativa) return;
    await executar(() => prorrogarPrazoOuv(d.id, justificativa), 'Prazo prorrogado por 10 dias.');
  }

  async function encaminhar(d: DenunciaOuv) {
    // O dominio aceita apenas MP|PF|TCE|TCU|CGU (ADR do dominio OUV).
    const entrada = prompt(
      `Órgão de destino:\n${ORGAOS_EXTERNOS.map((o) => `${o.value} — ${o.label}`).join('\n')}`,
      'MP',
    );
    const orgao = entrada?.trim().toUpperCase() ?? '';
    if (!ORGAOS_EXTERNOS.some((o) => o.value === orgao)) {
      alert('Órgão inválido. Use: MP, PF, TCE, TCU ou CGU.');
      return;
    }
    const numero = prompt('Número do processo/inquérito:');
    if (!numero) return;
    await executar(() => encaminharDenunciaOuv(d.id, orgao, numero), `Denúncia encaminhada ao ${orgao}.`);
  }

  return (
    <div className="ouv-grid">
      <article className="card ouv-card">
        <h3>Nova denúncia</h3>
        <p className="muted">Pode ser anônima. Dados do denunciante são protegidos (sigilo).</p>
        <form className="ouv-form" onSubmit={handleSubmit}>
          <Field label="Assunto" value={assunto} onChange={setAssunto} required placeholder="Assunto da denúncia" />
          <TextAreaField label="Descrição" value={descricao} onChange={setDescricao} required rows={3} placeholder="Descreva os fatos" />
          <SelectField label="Tipo de denúncia" value={tipo_denuncia} onChange={setTipoDenuncia} options={TIPOS_DENUNCIA} required />
          <label className="ouv-checkbox"><input type="checkbox" checked={envolve_servidor_publico} onChange={(e) => setEnvolveServidorPublico(e.target.checked)} /> Envolve servidor público</label>
          <Field label="Servidor envolvido" value={servidor_envolvido} onChange={setServidorEnvolvido} placeholder="Nome/matrícula do servidor" />
          <Field label="Valor envolvido (R$)" value={valor_envolvido} onChange={setValorEnvolvido} type="number" step="0.01" min="0" placeholder="0.00" />
          <Field label="Local do fato" value={local_fato} onChange={setLocalFato} required placeholder="Onde ocorreu" />
          <Field label="Data do fato" value={data_fato} onChange={setDataFato} type="date" required />
          <div className="ouv-form-row">
            <Field label="Nome do denunciante" value={cidadao_nome} onChange={setCidadaoNome} placeholder="João da Silva" />
            <Field label="CPF" value={cidadao_cpf} onChange={setCidadaoCpf} placeholder="000.000.000-00" />
          </div>
          <div className="ouv-form-row">
            <Field label="E-mail" value={cidadao_email} onChange={setCidadaoEmail} type="email" placeholder="denunciante@email.com" />
            <Field label="Telefone" value={cidadao_telefone} onChange={setCidadaoTelefone} placeholder="(00) 00000-0000" />
          </div>
          <Field label="Endereço" value={cidadao_endereco} onChange={setCidadaoEndereco} placeholder="Rua, número, bairro, cidade" />
          <label className="ouv-checkbox"><input type="checkbox" checked={cidadao_anonimo} onChange={(e) => setCidadaoAnonimo(e.target.checked)} /> Anônimo (dados protegidos por sigilo)</label>
          <SelectField label="Canal" value={canal} onChange={setCanal} options={CANAIS} required />
          <Field label="Órgão de destino" value={orgao_destino} onChange={setOrgaoDestino} required placeholder="Secretaria / Órgão responsável" />
          <Field label="Setor responsável" value={setor_responsavel} onChange={setSetorResponsavel} placeholder="Setor específico" />
          <SelectField label="Prioridade" value={prioridade} onChange={setPrioridade} options={PRIORIDADES} required />
          <button className="button button--primary" type="submit" disabled={salvando}>
            Registrar denúncia
          </button>
        </form>
      </article>

      <article className="card ouv-card ouv-card--full">
        <div className="ouv-card-title">
          <div>
            <h3>Denúncias</h3>
            <p className="muted">Denúncias recebidas com proteção ao denunciante.</p>
          </div>
          <div className="ouv-filters">
            <select value={filtroStatus} onChange={(e) => setFiltroStatus(e.target.value)} aria-label="Filtrar por status">
              <option value="todos">Todos os status</option>
              {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
            </select>
            <select value={filtroTipo} onChange={(e) => setFiltroTipo(e.target.value)} aria-label="Filtrar por tipo">
              <option value="todos">Todos os tipos</option>
              {TIPOS_DENUNCIA.map((t) => <option key={t.value} value={t.value}>{t.label}</option>)}
            </select>
          </div>
        </div>
        <TabelaEstado loading={resources.denuncias.loading} erro={resources.denuncias.erro} vazio={filtradas.length === 0}>
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Protocolo</th>
                  <th>Tipo</th>
                  <th>Assunto</th>
                  <th>Denunciante</th>
                  <th>Órgão</th>
                  <th>Canal</th>
                  <th>Prazo</th>
                  <th>Status</th>
                  <th>Prioridade</th>
                  <th>Encaminhamentos</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {filtradas.map((d) => (
                  <tr key={d.id}>
                    <td><code>{getProtocolo(d)}</code></td>
                    <td><TipoDenunciaBadge value={d.tipo_denuncia} /></td>
                    <td>{d.assunto}</td>
                    <td>{getCidadaoNome(d)}{d.sigilo_denunciante && <span className="ouv-sigilo" title="Dados do denunciante protegidos por sigilo"> 🔒</span>}</td>
                    <td>{d.orgao_destino}</td>
                    <td><CanalBadge value={d.canal} /></td>
                    <td><PrazoBadge prazo={d.prazo} /></td>
                    <td><StatusBadge value={d.status} /></td>
                    <td><PrioridadeBadge value={d.prioridade} /></td>
                    <td>
                      <div className="ouv-encaminhamentos">
                        {d.encaminhada_mp && <span className="ouv-enc-tag ouv-enc-tag--mp">MP</span>}
                        {d.encaminhada_pf && <span className="ouv-enc-tag ouv-enc-tag--pf">PF</span>}
                        {d.encaminhada_tce && <span className="ouv-enc-tag ouv-enc-tag--tce">TCE</span>}
                      </div>
                    </td>
                    <td>
                      <div className="ouv-actions">
                        {d.status !== 'respondida' && d.status !== 'concluida' && d.status !== 'arquivada' && d.status !== 'cancelada' && (
                          <button onClick={() => responder(d)} className="button button--sm" title="Responder">Responder</button>
                        )}
                        <select
                          value={d.status}
                          onChange={(e) => mudarStatus(d, e.target.value)}
                          disabled={salvando}
                          className="ouv-status-select"
                          aria-label="Alterar status"
                        >
                          {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
                        </select>
                        {d.prazo && !d.prazo.prorrogado && !d.prazo.vencido && (
                          <button onClick={() => prorrogar(d)} className="button button--sm button--outline" title="Prorrogar">+10d</button>
                        )}
                        <button onClick={() => encaminhar(d)} className="button button--sm button--outline" title="Encaminhar a órgão externo">Encaminhar</button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>
    </div>
  );
}
