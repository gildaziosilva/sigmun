import { useState } from 'react';
import type {
  BairroTel,
  GeorreferenciaTel,
  LogradouroTel,
  PlantaValoresTel,
} from '../../lib/api';
import {
  listarGeorreferenciasPorReferenciaTel,
  listarLogradourosDoBairroTel,
  obterBairroPorCodigoTel,
  obterLogradouroPorCodigoTel,
  obterPlantaVigenteTel,
} from '../../lib/api';
import type { TelResources } from './TelPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  OCUPACOES,
  SelectTerr,
  StatusTerr,
  bairroNome,
  formatarMoedaTerr,
  formatarNumeroTerr,
  logradouroNome,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: TelResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const ANO_ATUAL = new Date().getFullYear();

/**
 * Consultas pontuais do território.
 *
 * Agrupa as operações de leitura que não são listagens: busca pela chave natural
 * (código cadastral), consulta da planta de valores vigente — que é o contrato
 * consumido pelo DOM-IMO para apurar o valor venal (RN-IMO-005) — e
 * georreferências filtradas pela referência (RN-TEL-005).
 */
export function ConsultasTel({ resources, executar, salvando }: Props) {
  const bairros = resources.bairros.data ?? [];
  const logradouros = resources.logradouros.data ?? [];

  const [codigoBairro, setCodigoBairro] = useState('');
  const [bairroEncontrado, setBairroEncontrado] = useState<BairroTel | null>(null);
  const [logradourosDoBairro, setLogradourosDoBairro] = useState<LogradouroTel[]>([]);

  const [codigoLogradouro, setCodigoLogradouro] = useState('');
  const [logradouroEncontrado, setLogradouroEncontrado] = useState<LogradouroTel | null>(null);

  const [ano, setAno] = useState(String(ANO_ATUAL));
  const [bairroPlanta, setBairroPlanta] = useState('');
  const [ocupacao, setOcupacao] = useState('residencial');
  const [plantaVigente, setPlantaVigente] = useState<PlantaValoresTel | null>(null);

  const [tipoReferencia, setTipoReferencia] = useState<'bairro' | 'logradouro'>('bairro');
  const [referenciaId, setReferenciaId] = useState('');
  const [georreferencias, setGeorreferencias] = useState<GeorreferenciaTel[]>([]);

  async function buscarBairroPorCodigo() {
    if (!codigoBairro.trim()) return;
    const ok = await executar(async () => {
      const bairro = await obterBairroPorCodigoTel(codigoBairro.trim());
      setBairroEncontrado(bairro);
      setLogradourosDoBairro(await listarLogradourosDoBairroTel(bairro.id));
    }, 'Divisão territorial localizada.');
    if (!ok) {
      setBairroEncontrado(null);
      setLogradourosDoBairro([]);
    }
  }

  async function buscarLogradouroPorCodigo() {
    if (!codigoLogradouro.trim()) return;
    const ok = await executar(async () => {
      setLogradouroEncontrado(await obterLogradouroPorCodigoTel(codigoLogradouro.trim()));
    }, 'Logradouro localizado.');
    if (!ok) setLogradouroEncontrado(null);
  }

  async function consultarPlantaVigente() {
    if (!bairroPlanta) return;
    const anoNumero = paraNumero(ano, ANO_ATUAL);
    const ok = await executar(async () => {
      setPlantaVigente(await obterPlantaVigenteTel(anoNumero, bairroPlanta, ocupacao));
    }, 'Planta vigente localizada.');
    if (!ok) setPlantaVigente(null);
  }

  async function consultarGeorreferencias() {
    if (!referenciaId) return;
    const ok = await executar(async () => {
      const params =
        tipoReferencia === 'bairro' ? { bairroId: referenciaId } : { logradouroId: referenciaId };
      setGeorreferencias(await listarGeorreferenciasPorReferenciaTel(params));
    }, 'Georreferências consultadas.');
    if (!ok) setGeorreferencias([]);
  }

  const opcoesBairro = bairros.map((b) => ({ valor: b.id, rotulo: `${b.codigo} — ${b.nome}` }));
  const opcoesLogradouro = logradouros.map((l) => ({
    valor: l.id,
    rotulo: `${l.codigo} — ${l.nome}`,
  }));

  return (
    <section className="stack terr-consultas">
      <section className="card">
        <h3>Buscar divisão territorial por código</h3>
        <p className="muted">
          Consulta pela chave natural cadastral e traz os logradouros vinculados (RN-TEL-002).
        </p>
        <form
          className="form-grid"
          onSubmit={(event) => {
            event.preventDefault();
            void buscarBairroPorCodigo();
          }}
        >
          <FieldTerr
            label="Código cadastral"
            value={codigoBairro}
            onChange={setCodigoBairro}
            required
            placeholder="Ex.: B-001"
          />
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando}>
              Buscar
            </button>
          </div>
        </form>

        {bairroEncontrado && (
          <div className="terr-resultado">
            <dl className="terr-detalhes">
              <div>
                <dt>Código</dt>
                <dd>{bairroEncontrado.codigo}</dd>
              </div>
              <div>
                <dt>Nome</dt>
                <dd>{bairroEncontrado.nome}</dd>
              </div>
              <div>
                <dt>Tipo</dt>
                <dd>{bairroEncontrado.tipo.replaceAll('_', ' ')}</dd>
              </div>
              <div>
                <dt>População</dt>
                <dd>{bairroEncontrado.populacao_estimada.toLocaleString('pt-BR')}</dd>
              </div>
              <div>
                <dt>Área (km²)</dt>
                <dd>{formatarNumeroTerr(bairroEncontrado.area_km2, 2)}</dd>
              </div>
              <div>
                <dt>Situação</dt>
                <dd>
                  <StatusTerr value={bairroEncontrado.situacao} />
                </dd>
              </div>
            </dl>
            <h4>Logradouros vinculados ({logradourosDoBairro.length})</h4>
            {logradourosDoBairro.length === 0 ? (
              <p className="muted">Nenhum logradouro vinculado a esta divisão.</p>
            ) : (
              <table className="terr-table">
                <thead>
                  <tr>
                    <th>Código</th>
                    <th>Nome</th>
                    <th>Tipo</th>
                    <th className="num">Numeração</th>
                    <th>Situação</th>
                  </tr>
                </thead>
                <tbody>
                  {logradourosDoBairro.map((l) => (
                    <tr key={l.id}>
                      <td>{l.codigo}</td>
                      <td>{l.nome}</td>
                      <td>{l.tipo.replaceAll('_', ' ')}</td>
                      <td className="num">
                        {l.numero_inicial}–{l.numero_final}
                      </td>
                      <td>
                        <StatusTerr value={l.situacao} />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        )}
      </section>

      <section className="card">
        <h3>Buscar logradouro por código</h3>
        <form
          className="form-grid"
          onSubmit={(event) => {
            event.preventDefault();
            void buscarLogradouroPorCodigo();
          }}
        >
          <FieldTerr
            label="Código cadastral"
            value={codigoLogradouro}
            onChange={setCodigoLogradouro}
            required
            placeholder="Ex.: LG-001"
          />
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando}>
              Buscar
            </button>
          </div>
        </form>
        {logradouroEncontrado && (
          <div className="terr-resultado">
            <dl className="terr-detalhes">
              <div>
                <dt>Código</dt>
                <dd>{logradouroEncontrado.codigo}</dd>
              </div>
              <div>
                <dt>Nome</dt>
                <dd>{logradouroEncontrado.nome}</dd>
              </div>
              <div>
                <dt>Divisão territorial</dt>
                <dd>{bairroNome(bairros, logradouroEncontrado.bairro_id)}</dd>
              </div>
              <div>
                <dt>Numeração</dt>
                <dd>
                  {logradouroEncontrado.numero_inicial}–{logradouroEncontrado.numero_final}
                </dd>
              </div>
              <div>
                <dt>CEP</dt>
                <dd>{logradouroEncontrado.cep ?? '—'}</dd>
              </div>
              <div>
                <dt>Situação</dt>
                <dd>
                  <StatusTerr value={logradouroEncontrado.situacao} />
                </dd>
              </div>
            </dl>
          </div>
        )}
      </section>

      <section className="card">
        <h3>Consultar planta genérica de valores vigente</h3>
        <p className="muted">
          Retorna os valores unitários consumidos pelo DOM-IMO para apurar o valor venal
          (RN-TEL-003 e RN-IMO-005). Quando não há planta vigente para a combinação, a API
          responde HTTP 404.
        </p>
        <form
          className="form-grid"
          onSubmit={(event) => {
            event.preventDefault();
            void consultarPlantaVigente();
          }}
        >
          <FieldTerr
            label="Ano"
            value={ano}
            onChange={setAno}
            type="number"
            min="1900"
            max="2200"
            step="1"
            required
          />
          <SelectTerr
            label="Divisão territorial"
            value={bairroPlanta}
            opcoes={opcoesBairro}
            onChange={setBairroPlanta}
            required
            vazio="(selecione)"
          />
          <SelectTerr label="Ocupação" value={ocupacao} opcoes={OCUPACOES} onChange={setOcupacao} required />
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando || !bairroPlanta}>
              Consultar
            </button>
          </div>
        </form>
        {plantaVigente && (
          <div className="terr-resultado">
            <dl className="terr-detalhes">
              <div>
                <dt>Exercício</dt>
                <dd>{plantaVigente.ano}</dd>
              </div>
              <div>
                <dt>Divisão</dt>
                <dd>{bairroNome(bairros, plantaVigente.bairro_id)}</dd>
              </div>
              <div>
                <dt>Ocupação</dt>
                <dd>{plantaVigente.ocupacao.replaceAll('_', ' ')}</dd>
              </div>
              <div>
                <dt>Valor do terreno (m²)</dt>
                <dd>{formatarMoedaTerr(plantaVigente.valor_terreno_m2)}</dd>
              </div>
              <div>
                <dt>Valor da construção (m²)</dt>
                <dd>{formatarMoedaTerr(plantaVigente.valor_construcao_m2)}</dd>
              </div>
              <div>
                <dt>Alíquota</dt>
                <dd>{formatarNumeroTerr(plantaVigente.aliquota_percent, 2)}%</dd>
              </div>
              <div>
                <dt>Legislação</dt>
                <dd>{plantaVigente.legislacao ?? '—'}</dd>
              </div>
              <div>
                <dt>Situação</dt>
                <dd>
                  <StatusTerr value={plantaVigente.situacao} />
                </dd>
              </div>
            </dl>
          </div>
        )}
      </section>

      <section className="card">
        <h3>Consultar georreferências por referência</h3>
        <p className="muted">
          A georreferência referencia uma divisão <strong>ou</strong> um logradouro, nunca
          ambos (RN-TEL-005).
        </p>
        <form
          className="form-grid"
          onSubmit={(event) => {
            event.preventDefault();
            void consultarGeorreferencias();
          }}
        >
          <SelectTerr
            label="Tipo de referência"
            value={tipoReferencia}
            opcoes={[
              { valor: 'bairro', rotulo: 'Divisão territorial' },
              { valor: 'logradouro', rotulo: 'Logradouro' },
            ]}
            onChange={(v) => {
              setTipoReferencia(v === 'logradouro' ? 'logradouro' : 'bairro');
              setReferenciaId('');
            }}
            required
          />
          {tipoReferencia === 'bairro' ? (
            <SelectTerr
              label="Divisão territorial"
              value={referenciaId}
              opcoes={opcoesBairro}
              onChange={setReferenciaId}
              required
              vazio="(selecione)"
            />
          ) : (
            <SelectTerr
              label="Logradouro"
              value={referenciaId}
              opcoes={opcoesLogradouro}
              onChange={setReferenciaId}
              required
              vazio="(selecione)"
            />
          )}
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando || !referenciaId}>
              Consultar
            </button>
          </div>
        </form>
        {georreferencias.length > 0 && (
          <div className="terr-resultado">
            <table className="terr-table">
              <thead>
                <tr>
                  <th>Geometria</th>
                  <th>Referência</th>
                  <th className="num">Latitude</th>
                  <th className="num">Longitude</th>
                  <th>Datum</th>
                  <th className="num">Precisão (m)</th>
                </tr>
              </thead>
              <tbody>
                {georreferencias.map((g) => (
                  <tr key={g.id}>
                    <td>{g.geometria}</td>
                    <td>
                      {g.bairro_id
                        ? bairroNome(bairros, g.bairro_id)
                        : logradouroNome(logradouros, g.logradouro_id)}
                    </td>
                    <td className="num">{formatarNumeroTerr(g.latitude, 6)}</td>
                    <td className="num">{formatarNumeroTerr(g.longitude, 6)}</td>
                    <td>{g.datum}</td>
                    <td className="num">{formatarNumeroTerr(g.precisao_m, 2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </section>
  );
}
