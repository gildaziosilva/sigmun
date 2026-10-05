import { useState, type FormEvent } from 'react';
import { TabelaEstado } from '../../components/DataState';
import {
  registrarPedidoLaiOuv,
  responderManifestacaoOuv,
  alterarStatusOuv,
  prorrogarPrazoOuv,
  interporRecursoLaiOuv,
  decidirRecursoLaiOuv,
  type PedidoLaiOuv,
} from '../../lib/api';
import { StatusBadge,
  NivelSigiloBadge,
  PrazoBadge,
  CanalBadge,
  FormaRespostaBadge,
  Field,
  SelectField,
  TextAreaField,
  getProtocolo,
  getCidadaoNome,
  type OuvResources,
  type ExecutarOuv,
} from './OuvShared';

const NIVEIS_SIGILO: readonly { value: string; label: string }[] = [
  { value: 'publico', label: 'Público' },
  { value: 'restrito', label: 'Restrito (10 anos)' },
  { value: 'sigiloso', label: 'Sigiloso (25 anos)' },
  { value: 'ultra_sigiloso', label: 'Ultra-sigiloso (50 anos)' },
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

const FORMATOS: readonly { value: string; label: string }[] = [
  { value: 'digital', label: 'Digital' },
  { value: 'fisico', label: 'Físico' },
  { value: 'presencial', label: 'Presencial' },
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

export function PedidosLaiOuv({ resources, executar, salvando }: { resources: OuvResources; executar: ExecutarOuv; salvando: boolean }) {
  const [assunto, setAssunto] = useState('');
  const [descricao, setDescricao] = useState('');
  const [informacao_solicitada, setInformacaoSolicitada] = useState('');
  const [fundamentacao, setFundamentacao] = useState('');
  const [nivel_sigilo, setNivelSigilo] = useState('publico');
  const [fundamentacao_sigilo, setFundamentacaoSigilo] = useState('');
  const [dados_pessoais_terceiros, setDadosPessoaisTerceiros] = useState(false);
  const [formato_resposta, setFormatoResposta] = useState('digital');
  const [cidadao_nome, setCidadaoNome] = useState('');
  const [cidadao_cpf, setCidadaoCpf] = useState('');
  const [cidadao_email, setCidadaoEmail] = useState('');
  const [cidadao_telefone, setCidadaoTelefone] = useState('');
  const [cidadao_endereco, setCidadaoEndereco] = useState('');
  const [canal, setCanal] = useState('portal_cidadao');
  const [orgao_destino, setOrgaoDestino] = useState('');
  const [setor_responsavel, setSetorResponsavel] = useState('');
  const [prioridade, setPrioridade] = useState('normal');
  const [filtroStatus, setFiltroStatus] = useState('todos');
  const [filtroNivel, setFiltroNivel] = useState('todos');
  const [filtroRecurso, setFiltroRecurso] = useState('todos');

  const pedidos = resources.pedidosLai.data ?? [];
  const filtrados = pedidos.filter((p) => {
    const okStatus = filtroStatus === 'todos' || p.status === filtroStatus;
    const okNivel = filtroNivel === 'todos' || p.nivel_sigilo === filtroNivel;
    const okRecurso = filtroRecurso === 'todos' || (filtroRecurso === 'recurso' ? p.is_recurso : !p.is_recurso);
    return okStatus && okNivel && okRecurso;
  });

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!assunto.trim() || !informacao_solicitada.trim() || !fundamentacao.trim() || !cidadao_nome.trim() || !cidadao_email.trim() || !orgao_destino.trim()) {
      alert('Preencha os campos obrigatórios');
      return;
    }
    if (nivel_sigilo !== 'publico' && !fundamentacao_sigilo.trim()) {
      alert('Fundamentação do sigilo é obrigatória para informações não públicas');
      return;
    }
    const ok = await executar(
      () => registrarPedidoLaiOuv({
        assunto: assunto.trim(),
        descricao: descricao.trim(),
        informacao_solicitada: informacao_solicitada.trim(),
        fundamentacao: fundamentacao.trim(),
        nivel_sigilo,
        fundamentacao_sigilo: fundamentacao_sigilo.trim(),
        dados_pessoais_terceiros,
        formato_resposta,
        cidadao_nome: cidadao_nome.trim(),
        cidadao_cpf: cidadao_cpf.trim(),
        cidadao_email: cidadao_email.trim(),
        cidadao_telefone: cidadao_telefone.trim(),
        cidadao_endereco: cidadao_endereco.trim(),
        canal,
        orgao_destino: orgao_destino.trim(),
        setor_responsavel: setor_responsavel.trim(),
        prioridade,
        anexos: [],
      }),
      'Pedido LAI registrado com sucesso.'
    );
    if (ok) {
      setAssunto('');
      setDescricao('');
      setInformacaoSolicitada('');
      setFundamentacao('');
      setNivelSigilo('publico');
      setFundamentacaoSigilo('');
      setDadosPessoaisTerceiros(false);
      setCidadaoNome('');
      setCidadaoCpf('');
      setCidadaoEmail('');
      setCidadaoTelefone('');
      setCidadaoEndereco('');
      setOrgaoDestino('');
      setSetorResponsavel('');
    }
  }

  async function responder(p: PedidoLaiOuv) {
    const resposta = prompt('Resposta ao solicitante:');
    if (!resposta) return;
    const forma = prompt('Forma de resposta (portal/email/correios/presencial/telefone):', 'portal');
    if (!forma) return;
    await executar(() => responderManifestacaoOuv(p.id, resposta, forma), 'Resposta registrada.');
  }

  async function mudarStatus(p: PedidoLaiOuv, novoStatus: string) {
    const obs = prompt('Observação (opcional):', '');
    await executar(() => alterarStatusOuv(p.id, novoStatus, obs || ''), `Status alterado para ${novoStatus}.`);
  }

  async function prorrogar(p: PedidoLaiOuv) {
    const justificativa = prompt('Justificativa da prorrogação (máx. 10 dias - LAI Art. 11 §1º):');
    if (!justificativa) return;
    await executar(() => prorrogarPrazoOuv(p.id, justificativa), 'Prazo prorrogado por 10 dias.');
  }

  async function interporRecurso(p: PedidoLaiOuv) {
    if (!confirm('Interpor recurso contra decisão de indeferimento/arquivamento (LAI Art. 15)?')) return;
    await executar(() => interporRecursoLaiOuv(p.id), 'Recurso interposto.');
  }

  async function decidirRecurso(p: PedidoLaiOuv) {
    const deferido = confirm('Deferir o recurso? (Cancelar = Indefere)');
    const fundamentacao = prompt('Fundamentação da decisão:');
    if (!fundamentacao) return;
    await executar(() => decidirRecursoLaiOuv(p.id, deferido, fundamentacao), deferido ? 'Recurso deferido.' : 'Recurso indeferido.');
  }

  return (
    <div className="ouv-grid">
      <article className="card ouv-card">
        <h3>Novo pedido de acesso à informação (LAI)</h3>
        <p className="muted">Lei 12.527/2011 - Prazo: 20 dias, prorrogável por 10 (Art. 11).</p>
        <form className="ouv-form" onSubmit={handleSubmit}>
          <Field label="Assunto" value={assunto} onChange={setAssunto} required placeholder="Assunto do pedido" />
          <TextAreaField label="Descrição" value={descricao} onChange={setDescricao} rows={2} placeholder="Contexto adicional" />
          <Field label="Informação solicitada" value={informacao_solicitada} onChange={setInformacaoSolicitada} required placeholder="Descreva a informação que deseja acessar" />
          <TextAreaField label="Fundamentação" value={fundamentacao} onChange={setFundamentacao} required rows={3} placeholder="Justificativa do pedido" />
          <SelectField label="Nível de sigilo" value={nivel_sigilo} onChange={setNivelSigilo} options={NIVEIS_SIGILO} required />
          <TextAreaField label="Fundamentação do sigilo" value={fundamentacao_sigilo} onChange={setFundamentacaoSigilo} rows={2} placeholder="Obrigatório se não for público" />
          <label className="ouv-checkbox"><input type="checkbox" checked={dados_pessoais_terceiros} onChange={(e) => setDadosPessoaisTerceiros(e.target.checked)} /> Envolve dados pessoais de terceiros</label>
          <SelectField label="Formato de resposta" value={formato_resposta} onChange={setFormatoResposta} options={FORMATOS} required />
          <div className="ouv-form-row">
            <Field label="Nome do solicitante" value={cidadao_nome} onChange={setCidadaoNome} required placeholder="João da Silva" />
            <Field label="CPF" value={cidadao_cpf} onChange={setCidadaoCpf} placeholder="000.000.000-00" />
          </div>
          <div className="ouv-form-row">
            <Field label="E-mail" value={cidadao_email} onChange={setCidadaoEmail} type="email" required placeholder="solicitante@email.com" />
            <Field label="Telefone" value={cidadao_telefone} onChange={setCidadaoTelefone} placeholder="(00) 00000-0000" />
          </div>
          <Field label="Endereço" value={cidadao_endereco} onChange={setCidadaoEndereco} placeholder="Rua, número, bairro, cidade" />
          <SelectField label="Canal" value={canal} onChange={setCanal} options={CANAIS} required />
          <Field label="Órgão de destino" value={orgao_destino} onChange={setOrgaoDestino} required placeholder="Secretaria / Órgão responsável" />
          <Field label="Setor responsável" value={setor_responsavel} onChange={setSetorResponsavel} placeholder="Setor específico" />
          <SelectField label="Prioridade" value={prioridade} onChange={setPrioridade} options={PRIORIDADES} required />
          <button className="button button--primary" type="submit" disabled={salvando}>
            Registrar pedido LAI
          </button>
        </form>
      </article>

      <article className="card ouv-card ouv-card--full">
        <div className="ouv-card-title">
          <div>
            <h3>Pedidos LAI</h3>
            <p className="muted">Lei de Acesso à Informação (Lei 12.527/2011).</p>
          </div>
          <div className="ouv-filters">
            <select value={filtroStatus} onChange={(e) => setFiltroStatus(e.target.value)} aria-label="Filtrar por status">
              <option value="todos">Todos os status</option>
              {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
            </select>
            <select value={filtroNivel} onChange={(e) => setFiltroNivel(e.target.value)} aria-label="Filtrar por nível de sigilo">
              <option value="todos">Todos os níveis</option>
              {NIVEIS_SIGILO.map((n) => <option key={n.value} value={n.value}>{n.label}</option>)}
            </select>
            <select value={filtroRecurso} onChange={(e) => setFiltroRecurso(e.target.value)} aria-label="Filtrar recursos">
              <option value="todos">Todos</option>
              <option value="original">Pedidos originais</option>
              <option value="recurso">Recursos</option>
            </select>
          </div>
        </div>
        <TabelaEstado loading={resources.pedidosLai.loading} erro={resources.pedidosLai.erro} vazio={filtrados.length === 0}>
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Protocolo</th>
                  <th>Tipo</th>
                  <th>Assunto</th>
                  <th>Solicitante</th>
                  <th>Órgão</th>
                  <th>Canal</th>
                  <th>Prazo</th>
                  <th>Status</th>
                  <th>Sigilo</th>
                  <th>Formato</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {filtrados.map((p) => (
                  <tr key={p.id}>
                    <td><code>{getProtocolo(p)}</code>{p.is_recurso && <span className="ouv-recurso-tag">RECURSO</span>}</td>
                    <td>Pedido LAI</td>
                    <td>{p.assunto}</td>
                    <td>{getCidadaoNome(p)}</td>
                    <td>{p.orgao_destino}</td>
                    <td><CanalBadge value={p.canal} /></td>
                    <td><PrazoBadge prazo={p.prazo} /></td>
                    <td><StatusBadge value={p.status} /></td>
                    <td><NivelSigiloBadge value={p.nivel_sigilo} /></td>
                    <td><FormaRespostaBadge value={p.formato_resposta} /></td>
                    <td>
                      <div className="ouv-actions">
                        {p.status !== 'respondida' && p.status !== 'concluida' && p.status !== 'arquivada' && p.status !== 'cancelada' && (
                          <button onClick={() => responder(p)} className="button button--sm" title="Responder">Responder</button>
                        )}
                        <select
                          value={p.status}
                          onChange={(e) => mudarStatus(p, e.target.value)}
                          disabled={salvando}
                          className="ouv-status-select"
                          aria-label="Alterar status"
                        >
                          {STATUSES.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
                        </select>
                        {p.prazo && !p.prazo.prorrogado && !p.prazo.vencido && (
                          <button onClick={() => prorrogar(p)} className="button button--sm button--outline" title="Prorrogar (Art. 11 §1º)">+10d</button>
                        )}
                        {!p.is_recurso && p.status === 'arquivada' && (
                          <button onClick={() => interporRecurso(p)} className="button button--sm button--outline" title="Interpor recurso (Art. 15)">Recurso</button>
                        )}
                        {p.is_recurso && p.status !== 'concluida' && p.status !== 'arquivada' && (
                          <button onClick={() => decidirRecurso(p)} className="button button--sm button--outline" title="Decidir recurso">Decidir</button>
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
