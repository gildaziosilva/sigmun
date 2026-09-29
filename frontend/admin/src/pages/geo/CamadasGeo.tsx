import { useState } from 'react';
import type { CamadaGeo, CamadaGeoCreate, CamadaGeoUpdate } from '../../lib/api';
import {
  ativarCamadaGeo,
  atualizarCamadaGeo,
  cadastrarCamadaGeo,
  desativarCamadaGeo,
  excluirCamadaGeo,
} from '../../lib/api';
import type { GeoPageResources } from './GeoPage';
import type { ExecutarGeo } from './GeoShared';
import {
  DATUMS,
  FORMATOS_CAMADA,
  FieldGeo,
  SelectGeo,
  StatusGeo,
  TIPOS_CAMADA,
  formatarDataGeo,
} from './GeoShared';

interface Props {
  resources: GeoPageResources;
  executar: ExecutarGeo;
  salvando: boolean;
}

const VAZIA: CamadaGeoCreate = { codigo: '', nome: '' };

export function CamadasGeo({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<CamadaGeoCreate>(VAZIA);
  const [editando, setEditando] = useState<CamadaGeo | null>(null);
  const camadas = resources.camadas.data ?? [];

  function alterar(campo: keyof CamadaGeoCreate, valor: string | number | boolean) {
    setForm((atual) => ({ ...atual, [campo]: valor }));
  }

  function limpar() {
    setForm(VAZIA);
    setEditando(null);
  }

  /** Carrega a camada selecionada no formulario (modo edicao). */
  function editar(camada: CamadaGeo) {
    setEditando(camada);
    setForm({
      codigo: camada.codigo,
      nome: camada.nome,
      descricao: camada.descricao ?? '',
      tipo: camada.tipo,
      formato: camada.formato,
      fonte: camada.fonte ?? '',
      datum: camada.datum,
      url_servico: camada.url_servico ?? '',
      srid: camada.srid,
      zoom_minimo: camada.zoom_minimo,
      zoom_maximo: camada.zoom_maximo,
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      const payload: CamadaGeoUpdate = { ...form };
      const ok = await executar(
        () => atualizarCamadaGeo(editando.id, payload),
        'Camada atualizada com sucesso!',
      );
      if (ok) limpar();
      return;
    }
    const ok = await executar(() => cadastrarCamadaGeo(form), 'Camada cadastrada com sucesso!');
    if (ok) setForm(VAZIA);
  }

  return (
    <section className="stack">
      <form className="card geo-form" onSubmit={handleSubmit}>
        <h3>{editando ? `Editar camada ${editando.codigo}` : 'Nova camada cartografica'}</h3>
        {editando && (
          <p className="muted">
            Alterando <strong>{editando.nome}</strong>. A situacao da camada e controlada pelos botoes
            ativar/desativar na tabela (RN-GEO-006).
          </p>
        )}
        <div className="form-grid">
          <FieldGeo
            label="Codigo"
            value={form.codigo}
            onChange={(v) => alterar('codigo', v)}
            required
          />
          <FieldGeo label="Nome" value={form.nome} onChange={(v) => alterar('nome', v)} required />
          <SelectGeo
            label="Tipo"
            value={form.tipo ?? 'outro'}
            opcoes={TIPOS_CAMADA}
            onChange={(v) => alterar('tipo', v)}
          />
          <SelectGeo
            label="Formato"
            value={form.formato ?? 'geojson'}
            opcoes={FORMATOS_CAMADA}
            onChange={(v) => alterar('formato', v)}
          />
          <SelectGeo
            label="Datum"
            value={form.datum ?? 'sirgas2000'}
            opcoes={DATUMS}
            onChange={(v) => alterar('datum', v)}
          />
          <FieldGeo
            label="Fonte"
            value={form.fonte ?? ''}
            onChange={(v) => alterar('fonte', v)}
          />
          <FieldGeo
            label="URL do servico"
            value={form.url_servico ?? ''}
            onChange={(v) => alterar('url_servico', v)}
            hint="Obrigatoria para formatos WMS/WFS/WMTS/XYZ na publicacao (RN-GEO-006)."
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
            {editando ? 'Salvar alteracoes' : 'Cadastrar camada'}
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

      <section className="card geo-lista">
        <div className="geo-lista-header">
          <h3>Camadas cadastradas ({camadas.length})</h3>
        </div>
        {camadas.length === 0 ? (
          <p className="muted">Nenhuma camada cadastrada.</p>
        ) : (
          <table className="geo-table">
            <thead>
              <tr>
                <th>Codigo</th>
                <th>Nome</th>
                <th>Tipo</th>
                <th>Formato</th>
                <th>Datum</th>
                <th>Atualizacao</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {camadas.map((c) => (
                <tr key={c.id} className={editando?.id === c.id ? 'geo-linha--editando' : undefined}>
                  <td>{c.codigo}</td>
                  <td>{c.nome}</td>
                  <td>{c.tipo.replaceAll('_', ' ')}</td>
                  <td>{c.formato.toUpperCase()}</td>
                  <td>{c.datum.toUpperCase()}</td>
                  <td>{formatarDataGeo(c.data_atualizacao)}</td>
                  <td>
                    <StatusGeo value={c.situacao} />
                  </td>
                  <td className="geo-acoes">
                    <button
                      type="button"
                      className="button button--sm"
                      onClick={() => editar(c)}
                      disabled={salvando}
                    >
                      Editar
                    </button>
                    {c.situacao === 'rascunho' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => executar(() => ativarCamadaGeo(c.id), 'Camada ativada!')}
                        disabled={salvando}
                      >
                        Ativar
                      </button>
                    )}
                    {c.situacao === 'ativa' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => desativarCamadaGeo(c.id), 'Camada desativada!')}
                        disabled={salvando}
                      >
                        Desativar
                      </button>
                    )}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => executar(() => excluirCamadaGeo(c.id), 'Camada excluida!')}
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
