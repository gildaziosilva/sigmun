import { useEffect, useState } from 'react';
import {
  listarUsuarios,
  criarUsuario,
  obterUsuario,
  ativarUsuario,
  desativarUsuario,
  bloquearUsuario,
  type Usuario,
} from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

const TIPOS_STATUS: Record<string, { label: string; className?: string }> = {
  ATIVO: { label: 'Ativo' },
  INATIVO: { label: 'Inativo', className: 'badge--warn' },
  BLOQUEADO: { label: 'Bloqueado', className: 'badge--warn' },
  PENDENTE: { label: 'Pendente', className: 'badge--warn' },
};

/** Normaliza o status vindo da API (domínio usa caixa baixa: "ativo", ...). */
function normalizarStatus(status: string): string {
  return (status ?? '').toUpperCase();
}

function BadgeStatus({ status }: { status: string }) {
  const norm = normalizarStatus(status);
  const cfg = TIPOS_STATUS[norm] ?? { label: status };
  return (
    <span className={`badge ${cfg.className ?? ''}`}>{cfg.label}</span>
  );
}

function AcoesLinha({
  usuario,
  onAtivar,
  onDesativar,
  onBloquear,
  onDetalhe,
  loading,
}: {
  usuario: Usuario;
  onAtivar: (id: string) => Promise<unknown>;
  onDesativar: (id: string) => Promise<unknown>;
  onBloquear: (id: string) => Promise<unknown>;
  onDetalhe: (id: string) => Promise<unknown>;
  loading: boolean;
}) {
  // O backend persiste o status em caixa baixa ("ativo", "inativo", ...).
  const status = normalizarStatus(usuario.status);
  const podeDesativarOuBloquear = status === 'ATIVO';
  const podeAtivar = status === 'INATIVO' || status === 'BLOQUEADO' || status === 'PENDENTE';
  return (
    <div className="actions">
      <button
        type="button"
        className="button button--ghost button--sm"
        disabled={loading}
        onClick={() => onDetalhe(usuario.id)}
        title="Ver detalhes"
      >
        Detalhes
      </button>
      {podeDesativarOuBloquear && (
        <>
          <button
            type="button"
            className="button button--ghost button--sm"
            disabled={loading}
            onClick={() => onDesativar(usuario.id)}
            title="Desativar"
          >
            Desativar
          </button>
          <button
            type="button"
            className="button button--ghost button--sm"
            disabled={loading}
            onClick={() => onBloquear(usuario.id)}
            title="Bloquear"
          >
            Bloquear
          </button>
        </>
      )}
      {podeAtivar && !podeDesativarOuBloquear && (
        <button
          type="button"
          className="button button--ghost button--sm"
          disabled={loading}
          onClick={() => onAtivar(usuario.id)}
          title={status === 'BLOQUEADO' ? 'Desbloquear (reativar)' : 'Ativar'}
        >
          {status === 'BLOQUEADO' ? 'Desbloquear' : 'Ativar'}
        </button>
      )}
    </div>
  );
}

const FORM_INICIAL = {
  login: '',
  email: '',
  nome: '',
  senha: '',
  unidades_ids: '',
  roles_ids: '',
};

export default function IdnPage() {
  const [lista, recarregar] = useApiData(() => listarUsuarios());
  const [detalhe, setDetalhe] = useState<Usuario | null>(null);
  const [acaoEmAndamento, setAcaoEmAndamento] = useState<string | null>(null);
  const [feed, setFeed] = useState<string[]>([]);
  const [form, setForm] = useState(FORM_INICIAL);

  useEffect(() => {
    recarregar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function atualizarCampo(campo: keyof typeof FORM_INICIAL, valor: string) {
    setForm((atual) => ({ ...atual, [campo]: valor }));
  }

  function parseIds(valor: string): string[] {
    return valor.split(',').map((v) => v.trim()).filter((v) => v.length > 0);
  }

  async function handleCriar(evento: React.FormEvent) {
    evento.preventDefault();
    setAcaoEmAndamento('criar');
    setFeed((m) => [...m, `Criando usuário ${form.login}…`]);
    try {
      const criado = await criarUsuario({
        login: form.login.trim(),
        email: form.email.trim(),
        nome: form.nome.trim(),
        senha: form.senha,
        unidades_ids: parseIds(form.unidades_ids),
        roles_ids: parseIds(form.roles_ids),
      });
      setForm(FORM_INICIAL);
      recarregar();
      setDetalhe(criado);
      setFeed((m) => [...m, `Usuário ${criado.login} criado com sucesso.`]);
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Falha ao criar usuário.';
      setFeed((m) => [...m, msg]);
    } finally {
      setAcaoEmAndamento(null);
    }
  }

  async function handleObter(id: string) {
    setFeed((m) => [...m, `Carregando detalhes de ${id}…`]);
    try {
      const u = await obterUsuario(id);
      setDetalhe(u);
      setFeed((m) => [...m, `Detalhes de ${u.login} carregados.`]);
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Falha ao buscar usuário.';
      setFeed((m) => [...m, msg]);
    }
  }

  async function executarAcao(nome: string, fn: (id: string) => Promise<unknown>, id: string) {
    setAcaoEmAndamento(nome);
    setFeed((m) => [...m, `Solicitando ${nome} para ${id}…`]);
    try {
      await fn(id);
      recarregar();
      setFeed((m) => [...m, `${nome} executado com sucesso.`]);
    } catch (err) {
      const msg = err instanceof Error ? err.message : `Falha ao ${nome}.`;
      setFeed((m) => [...m, msg]);
    } finally {
      setAcaoEmAndamento(null);
    }
  }

  return (
    <section>
      <div className="page-head">
        <h2 className="section-title">Identidade e Acesso (IDN)</h2>
        <div className="page-actions">
          <button
            type="button"
            className="button button--ghost"
            onClick={recarregar}
            disabled={acaoEmAndamento !== null}
          >
            Recarregar
          </button>
        </div>
      </div>

      <p className="muted">
        Gestão de usuários via GET /api/v1/idn/usuarios e ciclo de vida via
        POST /api/v1/idn/usuarios/{'{id}'}/ativar|desativar|bloquear.
      </p>

      <article className="card">
        <h3>Novo usuário</h3>
        <form className="form" onSubmit={handleCriar}>
          <label>Login
            <input value={form.login} onChange={(e) => atualizarCampo('login', e.target.value)} required minLength={3} autoComplete="off" />
          </label>
          <label>E-mail
            <input type="email" value={form.email} onChange={(e) => atualizarCampo('email', e.target.value)} required autoComplete="off" />
          </label>
          <label>Nome
            <input value={form.nome} onChange={(e) => atualizarCampo('nome', e.target.value)} required autoComplete="off" />
          </label>
          <label>Senha
            <input type="password" value={form.senha} onChange={(e) => atualizarCampo('senha', e.target.value)} required minLength={8} autoComplete="new-password" />
          </label>
          <label>Unidades (IDs separados por vírgula)
            <input value={form.unidades_ids} onChange={(e) => atualizarCampo('unidades_ids', e.target.value)} placeholder="opcional" autoComplete="off" />
          </label>
          <label>Roles (IDs separados por vírgula)
            <input value={form.roles_ids} onChange={(e) => atualizarCampo('roles_ids', e.target.value)} placeholder="opcional" autoComplete="off" />
          </label>
          <div>
            <button type="submit" className="button button--primary" disabled={acaoEmAndamento !== null}>
              {acaoEmAndamento === 'criar' ? 'Criando…' : 'Criar usuário'}
            </button>
          </div>
        </form>
      </article>

      <TabelaEstado loading={lista.loading} erro={lista.erro} vazio={!lista.data || lista.data.items.length === 0}>
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Nome</th>
                <th>Login</th>
                <th>E-mail</th>
                <th>Status</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {(lista.data?.items ?? []).map((u) => (
                <tr key={u.id}>
                  <td>{u.nome}</td>
                  <td className="mono">{u.login}</td>
                  <td>{u.email}</td>
                  <td>
                    <BadgeStatus status={u.status} />
                  </td>
                  <td>
                    <AcoesLinha
                      usuario={u}
                      onAtivar={(id) => executarAcao('ativar', ativarUsuario, id)}
                      onDesativar={(id) => executarAcao('desativar', desativarUsuario, id)}
                      onBloquear={(id) => executarAcao('bloquear', bloquearUsuario, id)}
                      onDetalhe={(id) => handleObter(id)}
                      loading={!!acaoEmAndamento}
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </TabelaEstado>

      {detalhe && (
        <article className="card card--detail">
          <h3>Detalhes — {detalhe.login}</h3>
          <dl className="detail-list">
            <div><dt>ID</dt><dd><span className="mono">{detalhe.id}</span></dd></div>
            <div><dt>Nome</dt><dd>{detalhe.nome}</dd></div>
            <div><dt>E-mail</dt><dd>{detalhe.email}</dd></div>
            <div><dt>Status</dt><dd><BadgeStatus status={detalhe.status} /></dd></div>
            <div><dt>Criado em</dt><dd>{detalhe.created_at ? new Date(detalhe.created_at).toLocaleString('pt-BR') : '—'}</dd></div>
            {/* Sem gestão de Role/Permissão: a API atual não expõe endpoints HTTP
                de Role/Permissão; unidades_ids/roles_ids aparecem só como leitura. */}
            <div><dt>Unidades</dt><dd>{detalhe.unidades_ids.length ? detalhe.unidades_ids.join(', ') : '—'}</dd></div>
            <div><dt>Roles</dt><dd>{detalhe.roles_ids.length ? detalhe.roles_ids.join(', ') : '—'}</dd></div>
          </dl>
          <div className="card__footer">
            <button
              type="button"
              className="button button--ghost"
              onClick={() => setDetalhe(null)}
            >
              Fechar detalhes
            </button>
          </div>
        </article>
      )}

      {feed.length > 0 && (
        <aside className="feed" aria-live="polite">
          {feed.map((m, i) => (
            <p key={i} className="feed__item">{m}</p>
          ))}
        </aside>
      )}
    </section>
  );
}
