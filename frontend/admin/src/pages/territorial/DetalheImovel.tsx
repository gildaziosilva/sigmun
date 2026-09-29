import { useEffect, useState } from 'react';
import type {
  AvaliacaoImo,
  CaracteristicaImo,
  GeometriaImo,
  ImovelImo,
  LogradouroTel,
  ProprietarioImo,
} from '../../lib/api';
import {
  listarAvaliacoesDoImovelImo,
  listarCaracteristicasDoImovelImo,
  listarGeometriasDoImovelImo,
  listarProprietariosDoImovelImo,
  obterImovelImo,
} from '../../lib/api';
import {
  StatusTerr,
  bairroNome,
  formatarDataTerr,
  formatarMoedaTerr,
  formatarNumeroTerr,
  logradouroNome,
} from './TerrShared';

interface Props {
  imovelId: string;
  bairros: readonly { id: string; nome?: string | null }[];
  logradouros: readonly LogradouroTel[];
  onClose: () => void;
}

type Secao = 'proprietarios' | 'avaliacoes' | 'caracteristicas' | 'geometrias';

const SECOES: { id: Secao; rotulo: string }[] = [
  { id: 'proprietarios', rotulo: 'Proprietários' },
  { id: 'avaliacoes', rotulo: 'Avaliações' },
  { id: 'caracteristicas', rotulo: 'Características' },
  { id: 'geometrias', rotulo: 'Geometria' },
];

/**
 * Ficha completa de um imóvel.
 *
 * Reúne, a partir dos identificadores do imóvel, os vínculos de titularidade, o
 * histórico de avaliações por exercício, as características construtivas e a
 * geometria georreferenciada. Cada painel consome a operação dedicada da API
 * (`/imoveis/{id}/proprietarios`, `/avaliacoes/imovel/{id}`,
 * `/caracteristicas/imovel/{id}` e `/geometrias/imovel/{id}`).
 */
export function DetalheImovel({ imovelId, bairros, logradouros, onClose }: Props) {
  const [imovel, setImovel] = useState<ImovelImo | null>(null);
  const [proprietarios, setProprietarios] = useState<ProprietarioImo[]>([]);
  const [avaliacoes, setAvaliacoes] = useState<AvaliacaoImo[]>([]);
  const [caracteristicas, setCaracteristicas] = useState<CaracteristicaImo[]>([]);
  const [geometrias, setGeometrias] = useState<GeometriaImo[]>([]);
  const [secao, setSecao] = useState<Secao>('proprietarios');
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState('');

  useEffect(() => {
    let cancelado = false;
    Promise.all([
      obterImovelImo(imovelId),
      listarProprietariosDoImovelImo(imovelId),
      listarAvaliacoesDoImovelImo(imovelId),
      listarCaracteristicasDoImovelImo(imovelId),
      listarGeometriasDoImovelImo(imovelId),
    ])
      .then(([imovelDados, props, aval, caract, geom]) => {
        if (cancelado) return;
        setImovel(imovelDados);
        setProprietarios(props);
        setAvaliacoes(aval);
        setCaracteristicas(caract);
        setGeometrias(geom);
      })
      .catch((falha: unknown) => {
        if (cancelado) return;
        setErro(falha instanceof Error ? falha.message : 'Não foi possível carregar o imóvel.');
      })
      .finally(() => {
        if (!cancelado) setCarregando(false);
      });
    return () => {
      cancelado = true;
    };
  }, [imovelId]);

  const contagem: Record<Secao, number> = {
    proprietarios: proprietarios.length,
    avaliacoes: avaliacoes.length,
    caracteristicas: caracteristicas.length,
    geometrias: geometrias.length,
  };

  return (
    <section className="card terr-detalhe-imovel" aria-label="Ficha do imóvel">
      <div className="terr-lista-header">
        <h3>{imovel ? `Imóvel ${imovel.inscricao_imobiliaria}` : 'Ficha do imóvel'}</h3>
        <button type="button" className="button button--ghost button--sm" onClick={onClose}>
          Fechar
        </button>
      </div>

      {carregando && <p className="muted">Carregando ficha do imóvel...</p>}
      {erro && (
        <p className="terr-feedback terr-feedback--error" role="alert">
          {erro}
        </p>
      )}

      {imovel && !carregando && (
        <>
          <dl className="terr-detalhes">
            <div>
              <dt>Inscrição imobiliária</dt>
              <dd>{imovel.inscricao_imobiliaria}</dd>
            </div>
            <div>
              <dt>Logradouro</dt>
              <dd>{logradouroNome(logradouros, imovel.logradouro_id)}</dd>
            </div>
            <div>
              <dt>Divisão territorial</dt>
              <dd>{bairroNome(bairros, imovel.bairro_id)}</dd>
            </div>
            <div>
              <dt>Número</dt>
              <dd>{imovel.numero ?? '—'}</dd>
            </div>
            <div>
              <dt>Tipo</dt>
              <dd>{imovel.tipo.replaceAll('_', ' ')}</dd>
            </div>
            <div>
              <dt>Tipo de propriedade</dt>
              <dd>{imovel.tipo_propriedade.replaceAll('_', ' ')}</dd>
            </div>
            <div>
              <dt>Área do terreno (m²)</dt>
              <dd>{formatarNumeroTerr(imovel.area_terreno_m2, 2)}</dd>
            </div>
            <div>
              <dt>Área construída (m²)</dt>
              <dd>{formatarNumeroTerr(imovel.area_construida_m2, 2)}</dd>
            </div>
            <div>
              <dt>Ano de construção</dt>
              <dd>{imovel.ano_construcao ?? '—'}</dd>
            </div>
            <div>
              <dt>Situação</dt>
              <dd>
                <StatusTerr value={imovel.situacao} />
              </dd>
            </div>
          </dl>

          <nav className="terr-tabs" aria-label="Seções da ficha do imóvel">
            {SECOES.map((s) => (
              <button
                key={s.id}
                type="button"
                role="tab"
                aria-selected={secao === s.id}
                className={secao === s.id ? 'terr-tab terr-tab--active' : 'terr-tab'}
                onClick={() => setSecao(s.id)}
              >
                {s.rotulo} ({contagem[s.id]})
              </button>
            ))}
          </nav>

          {secao === 'proprietarios' && (
            <div role="tabpanel">
              {proprietarios.length === 0 ? (
                <p className="muted">Nenhum proprietário vinculado a este imóvel.</p>
              ) : (
                <table className="terr-table">
                  <thead>
                    <tr>
                      <th>Nome</th>
                      <th>CPF/CNPJ</th>
                      <th>Vínculo</th>
                      <th>Principal</th>
                    </tr>
                  </thead>
                  <tbody>
                    {proprietarios.map((p) => (
                      <tr key={p.id}>
                        <td>{p.nome}</td>
                        <td>{p.cpf}</td>
                        <td>{p.vinculo.replaceAll('_', ' ')}</td>
                        <td>{p.principal ? 'Sim' : 'Não'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          )}

          {secao === 'avaliacoes' && (
            <div role="tabpanel">
              {avaliacoes.length === 0 ? (
                <p className="muted">Nenhuma avaliação registrada para este imóvel.</p>
              ) : (
                <table className="terr-table">
                  <thead>
                    <tr>
                      <th>Exercício</th>
                      <th className="num">Valor venal</th>
                      <th className="num">Lançamento</th>
                      <th>Situação</th>
                    </tr>
                  </thead>
                  <tbody>
                    {avaliacoes.map((a) => (
                      <tr key={a.id}>
                        <td>{a.ano}</td>
                        <td className="num">{formatarMoedaTerr(a.valor_venal)}</td>
                        <td className="num">{formatarMoedaTerr(a.valor_lancamento)}</td>
                        <td>
                          <StatusTerr value={a.situacao} />
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          )}

          {secao === 'caracteristicas' && (
            <div role="tabpanel">
              {caracteristicas.length === 0 ? (
                <p className="muted">Nenhuma característica construtiva registrada.</p>
              ) : (
                <table className="terr-table">
                  <thead>
                    <tr>
                      <th>Obra</th>
                      <th className="num">Pavimentos</th>
                      <th className="num">Ano da renovação</th>
                      <th>Observação</th>
                    </tr>
                  </thead>
                  <tbody>
                    {caracteristicas.map((c) => (
                      <tr key={c.id}>
                        <td>{c.obra}</td>
                        <td className="num">{c.numero_pavimentos}</td>
                        <td className="num">{c.ano_renovacao ?? '—'}</td>
                        <td>{c.observacao ?? '—'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          )}

          {secao === 'geometrias' && (
            <div role="tabpanel">
              {geometrias.length === 0 ? (
                <p className="muted">Nenhuma geometria georreferenciada registrada (RN-IMO-007).</p>
              ) : (
                <table className="terr-table">
                  <thead>
                    <tr>
                      <th>Geometria</th>
                      <th className="num">Latitude</th>
                      <th className="num">Longitude</th>
                      <th className="num">Vértices</th>
                      <th>Datum</th>
                      <th>Levantamento</th>
                    </tr>
                  </thead>
                  <tbody>
                    {geometrias.map((g) => (
                      <tr key={g.id}>
                        <td>{g.geometria}</td>
                        <td className="num">{formatarNumeroTerr(g.latitude, 6)}</td>
                        <td className="num">{formatarNumeroTerr(g.longitude, 6)}</td>
                        <td className="num">{g.vertices.length}</td>
                        <td>{g.datum}</td>
                        <td>{formatarDataTerr(g.data_levantamento)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          )}
        </>
      )}
    </section>
  );
}
