import { useState } from 'react';
import type { ServicoGeo, ServicoGeoCreate, ServicoGeoUpdate } from '../../lib/api';
import {
  atualizarServicoGeo,
  cadastrarServicoGeo,
  excluirServicoGeo,
  inativarServicoGeo,
} from '../../lib/api';
import type { GeoPageResources } from './GeoPage';
import type { ExecutarGeo } from './GeoShared';
import { DATUMS, FieldGeo, SelectGeo, StatusGeo, TIPOS_SERVICO } from './GeoShared';

interface Props {
  resources: GeoPageResources;
  executar: ExecutarGeo;
  salvando: boolean;
}

const VAZIA: ServicoGeoCreate = { codigo: '', nome: '' };

export function ServicosGeo({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<ServicoGeoCreate>(VAZIA);
  const [editando, setEditando] = useState<ServicoGeo | null>(null);
  const servicos = resources.servicos.data ?? [];

  function alterar(campo: keyof ServicoGeoCreate, valor: string | number | boolean) {
    setForm((atual) => ({ ...atual, [campo]: valor }));
  }

  function limpar() {
    setForm(VAZIA);
    setEditando(null);
  }

  function editar(servico: ServicoGeo) {
    setEditando(servico);
    setForm({
      codigo: servico.codigo,
      nome: servico.nome,
      descricao: servico.descricao ?? '',
      tipo: servico.tipo,
      url: servico.url ?? '',
      camada: servico.camada ?? '',
      datum: servico.datum,
      srid: servico.srid,
      zoom_minimo: servico.zoom_minimo,
      zoom_maximo: servico.zoom_maximo,
      publico: servico.publico,
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      const payload: ServicoGeoUpdate = { ...form };
      const ok = await executar(
        () => atualizarServicoGeo(editando.id, payload),
        'Servico geoespacial atualizado!',
      );
      if (ok) limpar();
      return;
    }
    const ok = await executar(
      () => cadastrarServicoGeo(form),
      'Servico geoespacial cadastrado!',
    );
    if (ok) setForm(VAZIA);
  }

  return (
    <section className="stack">
      <form className="card geo-form" onSubmit={handleSubmit}>
        <h3>
          {editando ? `Editar servico ${editando.codigo}` : 'Novo servico geoespacial (RN-GEO-007)'}
        </h3>
        <div className="form-grid">
          <FieldGeo
            label="Codigo"
            value={form.codigo}
            onChange={(v) => alterar('codigo', v)}
            required
          />
          <FieldGeo label="Nome" value={form.nome} onChange={(v) => alterar('nome', v)} required />
          <SelectGeo
            label="Protocolo"
            value={form.tipo ?? 'wms'}
            opcoes={TIPOS_SERVICO}
            onChange={(v) => alterar('tipo', v)}
          />
          <SelectGeo
            label="Datum"
            value={form.datum ?? 'sirgas2000'}
            opcoes={DATUMS}
            onChange={(v) => alterar('datum', v)}
          />
          <FieldGeo
            label="URL"
            value={form.url ?? ''}
            onChange={(v) => alterar('url', v)}
            required
            hint="Servicos ativos exigem URL http/https."
          />
          <FieldGeo
            label="Camada publicada"
            value={form.camada ?? ''}
            onChange={(v) => alterar('camada', v)}
            hint="Obrigatoria em WMS e WFS."
          />
          <FieldGeo
            label="Zoom minimo"
            type="number"
            min="0"
            max="24"
            value={String(form.zoom_minimo ?? 0)}
            onChange={(v) => alterar('zoom_minimo', Number(v))}
          />
          <FieldGeo
            label="Zoom maximo"
            type="number"
            min="0"
            max="24"
            value={String(form.zoom_maximo ?? 24)}
            onChange={(v) => alterar('zoom_maximo', Number(v))}
          />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Salvar alteracoes' : 'Cadastrar servico'}
          </button>
          {editando && (
            <button type="button" className="button button--ghost" onClick={limpar} disabled={salvando}>
              Cancelar edicao
            </button>
          )}
        </div>
      </form>

      <section className="card geo-lista">
        <div className="geo-lista-header">
          <h3>Servicos publicados ({servicos.length})</h3>
        </div>
        {servicos.length === 0 ? (
          <p className="muted">Nenhum servico geoespacial cadastrado.</p>
        ) : (
          <table className="geo-table">
            <thead>
              <tr>
                <th>Codigo</th>
                <th>Nome</th>
                <th>Protocolo</th>
                <th>Camada</th>
                <th>Publico</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {servicos.map((s) => (
                <tr key={s.id} className={editando?.id === s.id ? 'geo-linha--editando' : undefined}>
                  <td>{s.codigo}</td>
                  <td>{s.nome}</td>
                  <td>{s.tipo.toUpperCase()}</td>
                  <td>{s.camada || '—'}</td>
                  <td>{s.publico ? 'Sim' : 'Nao'}</td>
                  <td>
                    <StatusGeo value={s.situacao} />
                  </td>
                  <td className="geo-acoes">
                    <button
                      type="button"
                      className="button button--sm"
                      onClick={() => editar(s)}
                      disabled={salvando}
                    >
                      Editar
                    </button>
                    {s.situacao === 'ativo' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => inativarServicoGeo(s.id), 'Servico inativado!')}
                        disabled={salvando}
                      >
                        Inativar
                      </button>
                    )}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => executar(() => excluirServicoGeo(s.id), 'Servico excluido!')}
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
