import { useState } from 'react';
import type { Obra, ObraCreate, ObraUpdate } from '../../lib/api';
import {
  atualizarObra,
  cancelarObra,
  cadastrarObra,
  concluirObra,
  excluirObra,
  iniciarExecucaoObra,
  suspenderObra,
} from '../../lib/api';
import type { ObrasPageResources } from './ObrasPage';
import type { ExecutarObras } from './ObrasShared';
import {
  FieldObras,
  FONTES_RECURSO,
  SelectObras,
  StatusObras,
  TIPOS_CONTRATACAO,
  TIPOS_OBRA,
  formatarMoedaObras,
} from './ObrasShared';

interface Props {
  resources: ObrasPageResources;
  executar: ExecutarObras;
  salvando: boolean;
}

const VAZIA: ObraCreate = { numero: '', nome: '' };

export function ObrasObras({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<ObraCreate>(VAZIA);
  const [editando, setEditando] = useState<Obra | null>(null);
  const [motivo, setMotivo] = useState('');
  const obras = resources.obras.data ?? [];

  function alterar(campo: keyof ObraCreate, valor: string) {
    setForm((atual) => ({ ...atual, [campo]: valor }));
  }

  function limpar() {
    setForm(VAZIA);
    setEditando(null);
  }

  function editar(obra: Obra) {
    setEditando(obra);
    setForm({
      numero: obra.numero,
      nome: obra.nome,
      descricao: obra.descricao ?? '',
      tipo: obra.tipo,
      tipo_contratacao: obra.tipo_contratacao,
      fonte_recurso: obra.fonte_recurso,
      valor_orcado: obra.valor_orcado,
      valor_contratado: obra.valor_contratado,
      empresa_contratada: obra.empresa_contratada ?? '',
      numero_contrato: obra.numero_contrato ?? '',
      responsavel_tecnico: obra.responsavel_tecnico ?? '',
      endereco: obra.endereco ?? '',
      bairro: obra.bairro ?? '',
      data_inicio_prevista: obra.data_inicio_prevista ?? '',
      data_fim_prevista: obra.data_fim_prevista ?? '',
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      // `numero` e imutavel na API (RN-OBR-001) e nao faz parte do payload.
      const { numero: _numero, ...resto } = form;
      const payload: ObraUpdate = resto;
      const ok = await executar(
        () => atualizarObra(editando.id, payload),
        'Obra atualizada com sucesso!',
      );
      if (ok) limpar();
      return;
    }
    const ok = await executar(() => cadastrarObra(form), 'Obra cadastrada com sucesso!');
    if (ok) setForm(VAZIA);
  }

  return (
    <section className="stack">
      <form className="card obras-form" onSubmit={handleSubmit}>
        <h3>{editando ? `Editar obra ${editando.numero}` : 'Nova obra publica (RN-OBR-001)'}</h3>
        {editando?.situacao === 'concluida' && (
          <p className="muted">Obra concluida: a API nao aceita alteracoes (RN-OBR-002).</p>
        )}
        <div className="form-grid">
          <FieldObras
            label="Numero"
            value={form.numero}
            onChange={(v) => alterar('numero', v)}
            required
            readOnly={Boolean(editando)}
            hint={editando ? 'O numero identifica a obra e e imutavel (RN-OBR-001).' : undefined}
          />
          <FieldObras label="Nome" value={form.nome} onChange={(v) => alterar('nome', v)} required />
          <SelectObras
            label="Tipo"
            value={form.tipo ?? 'outro'}
            opcoes={TIPOS_OBRA}
            onChange={(v) => alterar('tipo', v)}
          />
          <SelectObras
            label="Contratacao"
            value={form.tipo_contratacao ?? 'licitacao'}
            opcoes={TIPOS_CONTRATACAO}
            onChange={(v) => alterar('tipo_contratacao', v)}
          />
          <SelectObras
            label="Fonte de recurso"
            value={form.fonte_recurso ?? 'orcamento_proprio'}
            opcoes={FONTES_RECURSO}
            onChange={(v) => alterar('fonte_recurso', v)}
          />
          <FieldObras
            label="Valor orcado (R$)"
            type="number"
            min="0"
            step="0.01"
            value={String(form.valor_orcado ?? 0)}
            onChange={(v) => alterar('valor_orcado', v)}
          />
          <FieldObras
            label="Valor contratado (R$)"
            type="number"
            min="0"
            step="0.01"
            value={String(form.valor_contratado ?? 0)}
            onChange={(v) => alterar('valor_contratado', v)}
            hint="Nao pode superar o valor orcado (RN-OBR-004)."
          />
          <FieldObras
            label="Empresa contratada"
            value={form.empresa_contratada ?? ''}
            onChange={(v) => alterar('empresa_contratada', v)}
          />
          <FieldObras
            label="Numero do contrato"
            value={form.numero_contrato ?? ''}
            onChange={(v) => alterar('numero_contrato', v)}
          />
          <FieldObras
            label="Responsavel tecnico"
            value={form.responsavel_tecnico ?? ''}
            onChange={(v) => alterar('responsavel_tecnico', v)}
          />
          <FieldObras
            label="Endereco"
            value={form.endereco ?? ''}
            onChange={(v) => alterar('endereco', v)}
          />
          <FieldObras
            label="Bairro"
            value={form.bairro ?? ''}
            onChange={(v) => alterar('bairro', v)}
          />
          <FieldObras
            label="Inicio previsto"
            type="date"
            value={form.data_inicio_prevista ?? ''}
            onChange={(v) => alterar('data_inicio_prevista', v)}
          />
          <FieldObras
            label="Fim previsto"
            type="date"
            value={form.data_fim_prevista ?? ''}
            onChange={(v) => alterar('data_fim_prevista', v)}
          />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Salvar alteracoes' : 'Cadastrar obra'}
          </button>
          {editando && (
            <button
              type="button"
              className="button button--ghost"
              onClick={limpar}
              disabled={salvando}
            >
              Cancelar edicao
            </button>
          )}
        </div>
      </form>

      <section className="card obras-lista">
        <div className="obras-lista-header">
          <h3>Obras cadastradas ({obras.length})</h3>
        </div>
        <label className="obras-motivo">
          <span>Justificativa (suspensao / cancelamento)</span>
          <input value={motivo} onChange={(event) => setMotivo(event.target.value)} />
        </label>
        {obras.length === 0 ? (
          <p className="muted">Nenhuma obra cadastrada.</p>
        ) : (
          <table className="obras-table">
            <thead>
              <tr>
                <th>Numero</th>
                <th>Obra</th>
                <th>Tipo</th>
                <th className="num">Orcado</th>
                <th className="num">Medido</th>
                <th className="num">Pago</th>
                <th className="num">Fisico</th>
                <th className="num">Financeiro</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {obras.map((o) => (
                <tr key={o.id} className={editando?.id === o.id ? 'obras-linha--editando' : undefined}>
                  <td>{o.numero}</td>
                  <td>{o.nome}</td>
                  <td>{o.tipo.replaceAll('_', ' ')}</td>
                  <td className="num">{formatarMoedaObras(o.valor_orcado)}</td>
                  <td className="num">{formatarMoedaObras(o.valor_mediado)}</td>
                  <td className="num">{formatarMoedaObras(o.valor_pago)}</td>
                  <td className="num">{o.percentual_fisico.toFixed(1)}%</td>
                  <td className="num">{o.percentual_financeiro.toFixed(1)}%</td>
                  <td>
                    <StatusObras value={o.situacao} />
                  </td>
                  <td className="obras-acoes">
                    <button
                      type="button"
                      className="button button--sm"
                      onClick={() => editar(o)}
                      disabled={salvando || o.situacao === 'concluida'}
                      title={
                        o.situacao === 'concluida'
                          ? 'Obra concluida nao aceita alteracoes (RN-OBR-002)'
                          : undefined
                      }
                    >
                      Editar
                    </button>
                    {o.situacao === 'contratada' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => executar(() => iniciarExecucaoObra(o.id), 'Execucao iniciada!')}
                        disabled={salvando}
                      >
                        Iniciar
                      </button>
                    )}
                    {(o.situacao === 'em_execucao' || o.situacao === 'contratada') && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => suspenderObra(o.id, motivo), 'Obra suspensa!')}
                        disabled={salvando}
                      >
                        Suspender
                      </button>
                    )}
                    {o.situacao === 'em_execucao' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => executar(() => concluirObra(o.id), 'Obra concluida!')}
                        disabled={salvando}
                        title="Exige 100% do avanco fisico (RN-OBR-005)"
                      >
                        Concluir
                      </button>
                    )}
                    {o.situacao !== 'concluida' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => cancelarObra(o.id, motivo), 'Obra cancelada!')}
                        disabled={salvando}
                      >
                        Cancelar
                      </button>
                    )}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => executar(() => excluirObra(o.id), 'Obra excluida!')}
                      disabled={salvando}
                    >
                      Excluir
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </section>
  );
}
