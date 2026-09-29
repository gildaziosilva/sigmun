import { useCallback, useState } from 'react';
import type { MapaCamadaGeo, MapaSigGeo, MapaSigGeoCreate, MapaSigGeoUpdate } from '../../lib/api';
import {
  arquivarMapaGeo,
  atualizarMapaGeo,
  cadastrarMapaGeo,
  comporCamadaGeo,
  excluirMapaGeo,
  listarComposicaoGeo,
  publicarMapaGeo,
  removerComposicaoGeo,
} from '../../lib/api';
import type { GeoPageResources } from './GeoPage';
import type { ExecutarGeo } from './GeoShared';
import { DATUMS, FieldGeo, SelectGeo, StatusGeo, TIPOS_MAPA, formatarDataGeo } from './GeoShared';

interface Props {
  resources: GeoPageResources;
  executar: ExecutarGeo;
  salvando: boolean;
}

const VAZIA: MapaSigGeoCreate = { codigo: '', nome: '' };

export function MapasGeo({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<MapaSigGeoCreate>(VAZIA);
  const [editando, setEditando] = useState<MapaSigGeo | null>(null);
  const [mapaSelecionado, setMapaSelecionado] = useState('');
  const [camadaSelecionada, setCamadaSelecionada] = useState('');
  const [composicao, setComposicao] = useState<MapaCamadaGeo[]>([]);
  const [erroComposicao, setErroComposicao] = useState('');

  const mapas = resources.mapas.data ?? [];
  const camadas = resources.camadas.data ?? [];
  const ativas = camadas.filter((c) => c.situacao === 'ativa');

  function alterar(campo: keyof MapaSigGeoCreate, valor: string | number | undefined) {
    setForm((atual) => ({ ...atual, [campo]: valor }));
  }

  function limpar() {
    setForm(VAZIA);
    setEditando(null);
  }

  function editar(mapa: MapaSigGeo) {
    setEditando(mapa);
    setForm({
      codigo: mapa.codigo,
      nome: mapa.nome,
      descricao: mapa.descricao ?? '',
      tipo: mapa.tipo,
      datum: mapa.datum,
      srid: mapa.srid,
      escala_denominador: mapa.escala_denominador,
      zoom_inicial: mapa.zoom_inicial,
      zoom_minimo: mapa.zoom_minimo,
      zoom_maximo: mapa.zoom_maximo,
      lat_min: mapa.lat_min ?? undefined,
      lon_min: mapa.lon_min ?? undefined,
      lat_max: mapa.lat_max ?? undefined,
      lon_max: mapa.lon_max ?? undefined,
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  const carregarComposicao = useCallback((mapaId: string) => {
    if (!mapaId) return;
    listarComposicaoGeo(mapaId)
      .then(setComposicao)
      .catch((falha: unknown) =>
        setErroComposicao(
          falha instanceof Error ? falha.message : 'Falha ao carregar a composicao do mapa.',
        ),
      );
  }, []);

  /** Troca o mapa em exibicao e recarrega a composicao sob demanda. */
  function selecionarMapa(mapaId: string) {
    setMapaSelecionado(mapaId);
    setErroComposicao('');
    setComposicao([]);
    if (mapaId) carregarComposicao(mapaId);
  }

  function nomeCamada(camadaId: string): string {
    const camada = camadas.find((c) => c.id === camadaId);
    return camada ? `${camada.codigo} — ${camada.nome}` : camadaId;
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    if (editando) {
      const payload: MapaSigGeoUpdate = { ...form };
      const ok = await executar(
        () => atualizarMapaGeo(editando.id, payload),
        'Mapa atualizado com sucesso!',
      );
      if (ok) limpar();
      return;
    }
    const ok = await executar(() => cadastrarMapaGeo(form), 'Mapa SIG cadastrado com sucesso!');
    if (ok) setForm(VAZIA);
  }

  async function adicionarCamada() {
    if (!mapaSelecionado || !camadaSelecionada) return;
    const ok = await executar(
      () => comporCamadaGeo(mapaSelecionado, { camada_id: camadaSelecionada }),
      'Camada adicionada a composicao!',
    );
    if (ok) {
      setCamadaSelecionada('');
      carregarComposicao(mapaSelecionado);
    }
  }

  async function removerCamada(vinculo: MapaCamadaGeo) {
    const ok = await executar(
      () => removerComposicaoGeo(mapaSelecionado, vinculo.id),
      'Camada removida da composicao!',
    );
    if (ok) carregarComposicao(mapaSelecionado);
  }

  const mapaEmEdicao = mapas.find((m) => m.id === editando?.id);
  const composicaoBloqueada = mapaEmEdicao?.situacao !== 'rascunho';

  return (
    <section className="stack">
      <form className="card geo-form" onSubmit={handleSubmit}>
        <h3>{editando ? `Editar mapa ${editando.codigo}` : 'Novo mapa SIG'}</h3>
        {editando && (
          <p className="muted">
            Mapas publicados nao aceitam alteracao de composicao (RN-GEO-004).
          </p>
        )}
        <div className="form-grid">
          <FieldGeo
            label="Codigo"
            value={form.codigo}
            onChange={(v) => alterar('codigo', v)}
            required
            readOnly={editando?.situacao === 'publicado'}
            hint={
              editando?.situacao === 'publicado'
                ? 'O codigo identifica o mapa publicado e nao pode ser alterado (RN-GEO-004).'
                : undefined
            }
          />
          <FieldGeo label="Nome" value={form.nome} onChange={(v) => alterar('nome', v)} required />
          <SelectGeo
            label="Tipo"
            value={form.tipo ?? 'tematico'}
            opcoes={TIPOS_MAPA}
            onChange={(v) => alterar('tipo', v)}
          />
          <SelectGeo
            label="Datum"
            value={form.datum ?? 'sirgas2000'}
            opcoes={DATUMS}
            onChange={(v) => alterar('datum', v)}
          />
          <FieldGeo
            label="Escala (denominador)"
            type="number"
            min="0"
            value={String(form.escala_denominador ?? 0)}
            onChange={(v) => alterar('escala_denominador', v)}
          />
          <FieldGeo
            label="Zoom inicial"
            type="number"
            min="0"
            max="24"
            value={String(form.zoom_inicial ?? 13)}
            onChange={(v) => alterar('zoom_inicial', Number(v))}
          />
          <FieldGeo
            label="Lat. minima"
            type="number"
            step="0.000001"
            value={form.lat_min === undefined ? '' : String(form.lat_min)}
            onChange={(v) => alterar('lat_min', v === '' ? undefined : Number(v))}
          />
          <FieldGeo
            label="Lat. maxima"
            type="number"
            step="0.000001"
            value={form.lat_max === undefined ? '' : String(form.lat_max)}
            onChange={(v) => alterar('lat_max', v === '' ? undefined : Number(v))}
          />
          <FieldGeo
            label="Lon. minima"
            type="number"
            step="0.000001"
            value={form.lon_min === undefined ? '' : String(form.lon_min)}
            onChange={(v) => alterar('lon_min', v === '' ? undefined : Number(v))}
          />
          <FieldGeo
            label="Lon. maxima"
            type="number"
            step="0.000001"
            value={form.lon_max === undefined ? '' : String(form.lon_max)}
            onChange={(v) => alterar('lon_max', v === '' ? undefined : Number(v))}
          />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Salvar alteracoes' : 'Cadastrar mapa'}
          </button>
          {editando && (
            <button type="button" className="button button--ghost" onClick={limpar} disabled={salvando}>
              Cancelar edicao
            </button>
          )}
        </div>
      </form>

      <section className="card geo-form">
        <h3>Composicao do mapa (RN-GEO-004)</h3>
        <p className="muted">
          Somente mapas em rascunho aceitam alteracao de composicao. A publicacao exige ao menos
          uma camada ativa.
        </p>
        <div className="form-grid">
          <SelectGeo
            label="Mapa"
            value={mapaSelecionado}
            opcoes={mapas.map((m) => ({ valor: m.id, rotulo: `${m.codigo} — ${m.nome}` }))}
            onChange={selecionarMapa}
            vazio="Selecione o mapa"
          />
          <SelectGeo
            label="Camada ativa"
            value={camadaSelecionada}
            opcoes={ativas.map((c) => ({ valor: c.id, rotulo: `${c.codigo} — ${c.nome}` }))}
            onChange={setCamadaSelecionada}
            vazio="Selecione a camada"
          />
        </div>
        <div className="form-actions">
          <button
            type="button"
            className="button"
            disabled={salvando || !mapaSelecionado || !camadaSelecionada || composicaoBloqueada}
            onClick={adicionarCamada}
          >
            Adicionar camada ao mapa
          </button>
        </div>

        {erroComposicao && <p className="alert alert--error">{erroComposicao}</p>}

        {mapaSelecionado && (
          <div className="geo-composicao">
            <h4>Camadas do mapa ({composicao.length})</h4>
            {composicao.length === 0 ? (
              <p className="muted">Este mapa ainda nao possui camadas na composicao.</p>
            ) : (
              <table className="geo-table">
                <thead>
                  <tr>
                    <th className="num">Ordem</th>
                    <th>Camada</th>
                    <th>Rotulo</th>
                    <th className="num">Opacidade</th>
                    <th>Visivel</th>
                    <th>Acoes</th>
                  </tr>
                </thead>
                <tbody>
                  {composicao.map((v) => (
                    <tr key={v.id}>
                      <td className="num">{v.ordem}</td>
                      <td>{nomeCamada(v.camada_id)}</td>
                      <td>{v.rotulo || '—'}</td>
                      <td className="num">{v.opacidade.toFixed(0)}%</td>
                      <td>{v.visivel ? 'Sim' : 'Nao'}</td>
                      <td className="geo-acoes">
                        <button
                          type="button"
                          className="button button--danger button--sm"
                          onClick={() => removerCamada(v)}
                          disabled={salvando || composicaoBloqueada}
                        >
                          Remover
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        )}
      </section>

      <section className="card geo-lista">
        <div className="geo-lista-header">
          <h3>Mapas cadastrados ({mapas.length})</h3>
        </div>
        {mapas.length === 0 ? (
          <p className="muted">Nenhum mapa cadastrado.</p>
        ) : (
          <table className="geo-table">
            <thead>
              <tr>
                <th>Codigo</th>
                <th>Nome</th>
                <th>Tipo</th>
                <th>Escala</th>
                <th>Publicacao</th>
                <th>Situacao</th>
                <th>Acoes</th>
              </tr>
            </thead>
            <tbody>
              {mapas.map((m) => (
                <tr key={m.id} className={editando?.id === m.id ? 'geo-linha--editando' : undefined}>
                  <td>{m.codigo}</td>
                  <td>{m.nome}</td>
                  <td>{m.tipo}</td>
                  <td>
                    {m.escala_denominador ? `1:${m.escala_denominador.toLocaleString('pt-BR')}` : '—'}
                  </td>
                  <td>{formatarDataGeo(m.publicado_em)}</td>
                  <td>
                    <StatusGeo value={m.situacao} />
                  </td>
                  <td className="geo-acoes">
                    <button
                      type="button"
                      className="button button--sm"
                      onClick={() => editar(m)}
                      disabled={salvando}
                    >
                      Editar
                    </button>
                    {m.situacao === 'rascunho' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => executar(() => publicarMapaGeo(m.id), 'Mapa publicado no geoportal!')}
                        disabled={salvando}
                      >
                        Publicar
                      </button>
                    )}
                    {m.situacao === 'publicado' && (
                      <button
                        type="button"
                        className="button button--ghost button--sm"
                        onClick={() => executar(() => arquivarMapaGeo(m.id), 'Mapa arquivado!')}
                        disabled={salvando}
                      >
                        Arquivar
                      </button>
                    )}
                    {m.situacao !== 'publicado' && (
                      <button
                        type="button"
                        className="button button--danger button--sm"
                        onClick={() => executar(() => excluirMapaGeo(m.id), 'Mapa excluido!')}
                        disabled={salvando}
                      >
                        Excluir
                      </button>
                    )}
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
