import { useState, type FormEvent } from 'react';
import { TabelaEstado } from '../../components/DataState';
import {
  registrarManifestacaoOuv,
  responderManifestacaoOuv,
  alterarStatusOuv,
  prorrogarPrazoOuv,
  avaliarManifestacaoOuv,
  type ManifestacaoOuv,
} from '../../lib/api';
import { StatusBadge,
  PrioridadeBadge,
  TipoManifestacaoBadge,
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
const TIPOS_MANIFESTACAO: readonly { value: string; label: string }[] = [
  { value: 'sugestao', label: 'Sugestão' },
  { value: 'elogio', label: 'Elogio' },
  { value: 'reclamacao', label: 'Reclamação' },
  { value: 'solicitacao', label: 'Solicitação' },
] as const;

const CANAIS: readonly { value: string; label: string }[] = [
  { value: 'portal_cidadao', label: 'Portal do Cidadão' },
  { value: 'presencial', label: 'Presencial' },
  { value: 'telefone', label: 'Telefone' },
  { value: 'email', label: 'E-mail' },
  { value: 'correios', label: 'Correios' },
  { value: 'aplicativo', label: 'Aplicativo' },
  { value: 'outro', label: 'Outro' },
] as const;

const PRIORIDADES: readonly { value: string; label: string }[] = [
  { value: 'baixa', label: 'Baixa' },
  { value: 'normal', label: 'Normal' },
  { value: 'alta', label: 'Alta' },
  { value: 'urgente', label: 'Urgente' },
] as const;

const STATUSES: readonly { value: string; label: string }[] = [
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


export function ManifestacoesOuv({ resources, executar, salvando }: { resources: OuvResources; executar: ExecutarOuv; salvando: boolean }) {
  const [tipo, setTipo] = useState('solicitacao');
  const [assunto, setAssunto] = useState('');
  const [descricao, setDescricao] = useState('');
  const [cidadao_nome, setCidadaoNome] = useState('');
  const [cidadao_cpf, setCidadaoCpf] = useState('');
  const [cidadao_email, setCidadaoEmail] = useState('');
  const [cidadao_telefone, setCidadaoTelefone] = useState('');
  const [cidadao_endereco, setCidadaoEndereco] = useState('');
  const [cidadao_anonimo, setCidadaoAnonimo] = useState(false);
  const [canal, setCanal] = useState('portal_cidadao');
  const [orgao_destino, setOrgaoDestino] = useState('');
  const [setor_responsavel, setSetorResponsavel] = useState('');
  const [prioridade, setPrioridade] = useState('normal');
  const [filtroStatus, setFiltroStatus] = useState('todos');
  const [filtroTipo, setFiltroTipo] = useState('todos');

  const manifestacoes = resources.manifestacoes.data ?? [];
  const filtradas = manifestacoes.filter((m) => {
    const okStatus = filtroStatus === 'todos' || m.status === filtroStatus;
    const okTipo = filtroTipo === 'todos' || m.tipo === filtroTipo;
    return okStatus && okTipo;
  });

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!assunto.trim() || !descricao.trim() || !orgao_destino.trim()) {
      alert('Preencha os campos obrigatórios');
      return;
    }
    if (!cidadao_anonimo && !cidadao_nome.trim()) {
      alert('Nome do cidadão é obrigatório para manifestações não anônimas');
      return;
    }
    const ok = await executar(
      () =>
        registrarManifestacaoOuv({
          tipo,
          assunto: assunto.trim(),
          descricao: descricao.trim(),
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
      'Manifestação registrada com sucesso.'
    );
    if (ok) {
      setAssunto('');
      setDescricao('');
      setCidadaoNome('');
      setCidadaoCpf('');
      setCidadaoEmail('');
      setCidadaoTelefone('');
      setCidadaoEndereco('');
      setCidadaoAnonimo(false);
      setOrgaoDestino('');
      setSetorResponsavel('');
    }
  }

  async function responder(m: ManifestacaoOuv) {
    const resposta = prompt('Resposta ao cidadão:');
    if (!resposta) return;
    const forma = prompt('Forma de resposta (portal/email/correios/presencial/telefone):', 'portal');
    if (!forma) return;
    await executar(() => responderManifestacaoOuv(m.id, resposta, forma), 'Resposta registrada.');
  }

  async function mudarStatus(m: ManifestacaoOuv, novoStatus: string) {
    const obs = prompt('Observação (opcional):', '');
    await executar(() => alterarStatusOuv(m.id, novoStatus, obs || ''), `Status alterado para ${novoStatus}.`);
  }

  async function prorrogar(m: ManifestacaoOuv) {
    const justificativa = prompt('Justificativa da prorrogação:');
    if (!justificativa) return;
    await executar(() => prorrogarPrazoOuv(m.id, justificativa), 'Prazo prorrogado por 10 dias.');
  }

  async function avaliar(m: ManifestacaoOuv) {
    const nota = prompt('Avaliação (1-5):');
    if (!nota) return;
    const n = parseInt(nota, 10);
    if (isNaN(n) || n < 1 || n > 5) return alert('Nota inválida');
    const comentario = prompt('Comentário (opcional):', '');
    await executar(() => avaliarManifestacaoOuv(m.id, n, comentario || ''), 'Avaliação registrada.');
  }

  return (
    <div className="ouv-grid">
      <article className="card ouv-card">
        <h3>Nova manifestação</h3>
        <p className="muted">Sugestão, elogio, reclamação ou solicitação (não anônima).</p>
        <form className="ouv-form" onSubmit={handleSubmit}>
          <SelectField label="Tipo" value={tipo} onChange={setTipo} options={TIPOS_MANIFESTACAO} required />
          <Field label="Assunto" value={assunto} onChange={setAssunto} required placeholder="Assunto da manifestação" />
          <TextAreaField label="Descrição" value={descricao} onChange={setDescricao} required rows={3} placeholder="Descreva a manifestação" />
          <div className="ouv-form-row">
            <Field label="Nome do cidadão" value={cidadao_nome} onChange={setCidadaoNome} placeholder="João da Silva" />
            <Field label="CPF" value={cidadao_cpf} onChange={setCidadaoCpf} placeholder="000.000.000-00" />
          </div>
          <div className="ouv-form-row">
            <Field label="E-mail" value={cidadao_email} onChange={setCidadaoEmail} type="email" placeholder="cidadao@email.com" />
            <Field label="Telefone" value={cidadao_telefone} onChange={setCidadaoTelefone} placeholder="(00) 00000-0000" />
          </div>
          <Field label="Endereço" value={cidadao_endereco} onChange={setCidadaoEndereco} placeholder="Rua, número, bairro, cidade" />
          <label className="ouv-checkbox"><input type="checkbox" checked={cidadao_anonimo} onChange={(e) => setCidadaoAnonimo(e.target.checked)} /> Anônimo</label>
          <SelectField label="Canal" value={canal} onChange={setCanal} options={CANAIS} required />
          <Field label="Órgão de destino" value={orgao_destino} onChange={setOrgaoDestino} required placeholder="Secretaria / Órgão responsável" />
          <Field label="Setor responsável" value={setor_responsavel} onChange={setSetorResponsavel} placeholder="Setor específico" />
          <SelectField label="Prioridade" value={prioridade} onChange={setPrioridade} options={PRIORIDADES} required />
          <button className="button button--primary" type="submit" disabled={salvando}>
            Registrar manifestação
          </button>
        </form>
      </article>

      <article className="card ouv-card ouv-card--full">
        <div className="ouv-card-title">
          <div>
            <h3>Manifestações</h3>
            <p className="muted">Lista de sugestões, elogios, reclamações e solicitações.</p>
          </div>
          <div className="ouv-filters">
            <select value={filtroStatus} onChange={(e) => setFiltroStatus(e.target.value)} aria-label="Filtrar por status">
              <option value="todos">Todos os status</option>
              {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
            </select>
            <select value={filtroTipo} onChange={(e) => setFiltroTipo(e.target.value)} aria-label="Filtrar por tipo">
              <option value="todos">Todos os tipos</option>
              {TIPOS_MANIFESTACAO.map((t) => <option key={t.value} value={t.value}>{t.label}</option>)}
            </select>
          </div>
        </div>
        <TabelaEstado loading={resources.manifestacoes.loading} erro={resources.manifestacoes.erro} vazio={filtradas.length === 0}>
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Protocolo</th>
                  <th>Tipo</th>
                  <th>Assunto</th>
                  <th>Cidadão</th>
                  <th>Órgão</th>
                  <th>Canal</th>
                  <th>Prazo</th>
                  <th>Status</th>
                  <th>Prioridade</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {filtradas.map((m) => (
                  <tr key={m.id}>
                    <td><code>{getProtocolo(m)}</code></td>
                    <td><TipoManifestacaoBadge value={m.tipo} /></td>
                    <td>{m.assunto}</td>
                    <td>{getCidadaoNome(m)}</td>
                    <td>{m.orgao_destino}</td>
                    <td><CanalBadge value={m.canal} /></td>
                    <td><PrazoBadge prazo={m.prazo} /></td>
                    <td><StatusBadge value={m.status} /></td>
                    <td><PrioridadeBadge value={m.prioridade} /></td>
                    <td>
                      <div className="ouv-actions">
                        {m.status !== 'respondida' && m.status !== 'concluida' && m.status !== 'arquivada' && m.status !== 'cancelada' && (
                          <button onClick={() => responder(m)} className="button button--sm" title="Responder">Responder</button>
                        )}
                        <select
                          value={m.status}
                          onChange={(e) => mudarStatus(m, e.target.value)}
                          disabled={salvando}
                          className="ouv-status-select"
                          aria-label="Alterar status"
                        >
                          {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
                        </select>
                        {m.prazo && !m.prazo.prorrogado && !m.prazo.vencido && (
                          <button onClick={() => prorrogar(m)} className="button button--sm button--outline" title="Prorrogar">+10d</button>
                        )}
                        {m.status === 'respondida' && m.avaliacao_cidadao === null && (
                          <button onClick={() => avaliar(m)} className="button button--sm button--outline" title="Avaliar">★</button>
                        )}
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
