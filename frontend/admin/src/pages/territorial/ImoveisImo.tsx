import { useEffect, useState } from 'react';
import type { BairroTel, ImovelImo, ImovelImoCreate, LogradouroTel } from '../../lib/api';
import {
  alterarSituacaoImovelImo,
  atualizarImovelImo,
  criarImovelImo,
  excluirImovelImo,
  listarBairrosTel,
  listarImoveisDoBairroImo,
  listarImoveisDoLogradouroImo,
  listarLogradourosTel,
  obterImovelPorInscricaoImo,
} from '../../lib/api';
import { DetalheImovel } from './DetalheImovel';
import type { ImoResources } from './ImoPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  SITUACOES_IMOVEL,
  StatusTerr,
  TIPOS_IMOVEL,
  bairroNome,
  formatarNumeroTerr,
  logradouroNome,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: ImoResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const FORM_VAZIO: ImovelImoCreate = {
  inscricao_imobiliaria: '',
  logradouro_id: '',
  bairro_id: '',
  numero: '',
  complemento: '',
  tipo: 'lote',
  tipo_propriedade: 'proprio',
  area_terreno_m2: 0,
  area_construida_m2: 0,
};

const TIPO_PROPRIEDADE = [
  { valor: 'proprio', rotulo: 'Próprio' },
  { valor: 'alugado', rotulo: 'Alugado' },
  { valor: 'cedido', rotulo: 'Cedido' },
  { valor: 'invencionado', rotulo: 'Invencionado' },
];

export function ImoveisImo({ resources, executar, salvando }: Props) {
  const [logradouros, setLogradouros] = useState<LogradouroTel[]>([]);
  const [bairros, setBairros] = useState<BairroTel[]>([]);
  const [form, setForm] = useState<ImovelImoCreate>({ ...FORM_VAZIO });
  const [areaTerreno, setAreaTerreno] = useState('0');
  const [areaConstruida, setAreaConstruida] = useState('0');
  const [anoConstrucao, setAnoConstrucao] = useState('');
  const [editando, setEditando] = useState<ImovelImo | null>(null);
  const [pesquisa, setPesquisa] = useState('');
  const [filtroSituacao, setFiltroSituacao] = useState('');
  const [escopo, setEscopo] = useState<{ tipo: 'todos' | 'bairro' | 'logradouro'; id: string }>({
    tipo: 'todos',
    id: '',
  });
  const [resultadoBusca, setResultadoBusca] = useState<ImovelImo | null>(null);
  const [inscricaoBusca, setInscricaoBusca] = useState('');
  const [imovelAberto, setImovelAberto] = useState<string | null>(null);

  // O cadastro imobiliário referencia o território do DOM-TEL: a divisão
  // territorial é derivada do logradouro escolhido, sem nova consulta.
  useEffect(() => {
    listarLogradourosTel().then((l) => setLogradouros(l)).catch(() => setLogradouros([]));
    listarBairrosTel().then((b) => setBairros(b)).catch(() => setBairros([]));
  }, []);

  /**
   * Quando um escopo territorial é selecionado, a lista passa a ser servida pela
   * operação dedicada da API (`/imoveis/bairro/{id}` ou
   * `/imoveis/logradouro/{id}`) em vez da listagem geral.
   */
  const chaveEscopo = escopo.tipo === 'todos' ? '' : `${escopo.tipo}:${escopo.id}`;
  const [resultadoEscopo, setResultadoEscopo] = useState<{ chave: string; imoveis: ImovelImo[] } | null>(
    null,
  );
  const [carregandoEscopo, setCarregandoEscopo] = useState(false);

  useEffect(() => {
    if (!chaveEscopo) return;
    let cancelado = false;
    const separador = chaveEscopo.indexOf(':');
    const tipo = chaveEscopo.slice(0, separador);
    const id = chaveEscopo.slice(separador + 1);
    const busca =
      tipo === 'bairro' ? listarImoveisDoBairroImo(id) : listarImoveisDoLogradouroImo(id);
    busca
      .then((lista) => {
        if (!cancelado) setResultadoEscopo({ chave: chaveEscopo, imoveis: lista });
      })
      .catch(() => {
        if (!cancelado) setResultadoEscopo({ chave: chaveEscopo, imoveis: [] });
      });
    return () => {
      cancelado = true;
    };
  }, [chaveEscopo]);

  // Enquanto o escopo troca, mantém a listagem geral até a resposta chegar.
  const emTransicao = carregandoEscopo && resultadoEscopo?.chave !== chaveEscopo;
  const imoveisEscopo = !chaveEscopo || emTransicao ? null : resultadoEscopo?.imoveis ?? null;
  const imoveis = imoveisEscopo ?? resources.imoveis.data ?? [];

  const filtrados = imoveis.filter(
    (i) =>
      (filtroSituacao === '' || i.situacao === filtroSituacao) &&
      (i.inscricao_imobiliaria.toLowerCase().includes(pesquisa.toLowerCase()) ||
        (i.numero ?? '').toLowerCase().includes(pesquisa.toLowerCase())),
  );

  const opcoesLogradouro = logradouros.map((l) => ({
    valor: l.id,
    rotulo: `${l.codigo} — ${l.nome}`,
  }));
  const bairroDoLogradouro = (logradouroId: string): string => {
    const lg = logradouros.find((l) => l.id === logradouroId);
    if (!lg) return '';
    // O vínculo territorial é feito pelo identificador opaco do bairro (RN-TEL-002),
    // e não pelo código do logradouro.
    return lg.bairro_id;
  };

  /** Busca o imóvel pela inscrição imobiliária (chave natural, RN-IMO-001). */
  async function handleBuscarInscricao(event: React.FormEvent) {
    event.preventDefault();
    if (!inscricaoBusca.trim()) return;
    const ok = await executar(async () => {
      setResultadoBusca(await obterImovelPorInscricaoImo(inscricaoBusca.trim()));
    }, 'Imóvel localizado.');
    if (!ok) setResultadoBusca(null);
  }

  function iniciarEdicao(imovel: ImovelImo) {
    setEditando(imovel);
    setForm({
      inscricao_imobiliaria: imovel.inscricao_imobiliaria,
      logradouro_id: imovel.logradouro_id,
      bairro_id: imovel.bairro_id,
      numero: imovel.numero ?? '',
      complemento: imovel.complemento ?? '',
      tipo: imovel.tipo,
      tipo_propriedade: imovel.tipo_propriedade,
      area_terreno_m2: imovel.area_terreno_m2,
      area_construida_m2: imovel.area_construida_m2,
    });
    setAreaTerreno(String(imovel.area_terreno_m2));
    setAreaConstruida(String(imovel.area_construida_m2));
    setAnoConstrucao(imovel.ano_construcao ? String(imovel.ano_construcao) : '');
  }

  function cancelarEdicao() {
    setEditando(null);
    setForm({ ...FORM_VAZIO });
    setAreaTerreno('0');
    setAreaConstruida('0');
    setAnoConstrucao('');
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const ano = anoConstrucao.trim() ? paraNumero(anoConstrucao) : null;
    if (editando) {
      const ok = await executar(
        () =>
          atualizarImovelImo(editando.id, {
            numero: form.numero,
            complemento: form.complemento,
            tipo: form.tipo,
            tipo_propriedade: form.tipo_propriedade,
            area_terreno_m2: paraNumero(areaTerreno),
            area_construida_m2: paraNumero(areaConstruida),
            ano_construcao: ano,
          }),
        'Imóvel atualizado com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(
      () =>
        criarImovelImo({
          ...form,
          logradouro_id: form.logradouro_id,
          bairro_id: form.bairro_id || bairroDoLogradouro(form.logradouro_id),
          area_terreno_m2: paraNumero(areaTerreno),
          area_construida_m2: paraNumero(areaConstruida),
          ano_construcao: ano,
        }),
      'Imóvel cadastrado com sucesso!',
    );
    if (ok) cancelarEdicao();
  }

  async function handleExcluir(imovel: ImovelImo) {
    if (
      !window.confirm(
        `Excluir o imóvel ${imovel.inscricao_imobiliaria}? A exclusão é lógica e preserva o histórico.`,
      )
    )
      return;
    await executar(() => excluirImovelImo(imovel.id), 'Imóvel excluído com sucesso!');
  }

  /** Altera a situação do imóvel; o servidor valida a transição (RN-IMO-004). */
  async function handleSituacao(imovel: ImovelImo, situacao: string) {
    const rotulo = SITUACOES_IMOVEL.find((s) => s.valor === situacao)?.rotulo ?? situacao;
    if (!window.confirm(`Alterar a situação do imóvel ${imovel.inscricao_imobiliaria} para "${rotulo}"?`))
      return;
    await executar(
      () => alterarSituacaoImovelImo(imovel.id, situacao),
      'Situação do imóvel atualizada com sucesso!',
    );
  }


  return (
    <section className="stack terr-imoveis">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>{editando ? 'Editar imóvel' : 'Cadastrar novo imóvel (lote)'}</h3>
        <p className="muted">
          O cadastro imobiliário exige logradouro e bairro vinculados ao DOM-TEL (RN-IMO-002).
        </p>
        <div className="form-grid">
          <FieldTerr
            label="Inscrição imobiliária"
            value={form.inscricao_imobiliaria}
            onChange={(v) => setForm({ ...form, inscricao_imobiliaria: v })}
            required
            readOnly={editando !== null}
            hint={editando ? 'A inscrição é imutável (RN-IMO-001)' : 'Única no município (RN-IMO-001)'}
          />
          <SelectTerr
            label="Logradouro"
            value={form.logradouro_id}
            opcoes={opcoesLogradouro}
            onChange={(v) => setForm({ ...form, logradouro_id: v, bairro_id: bairroDoLogradouro(v) })}
            required
            vazio="Selecione..."
          />
          <FieldTerr label="Número" value={form.numero ?? ''} onChange={(v) => setForm({ ...form, numero: v })} />
          <FieldTerr label="Complemento" value={form.complemento ?? ''} onChange={(v) => setForm({ ...form, complemento: v })} />
          <SelectTerr
            label="Tipo"
            value={form.tipo ?? 'lote'}
            opcoes={TIPOS_IMOVEL}
            onChange={(v) => setForm({ ...form, tipo: v })}
            required
          />
          <SelectTerr
            label="Tipo de propriedade"
            value={form.tipo_propriedade ?? 'proprio'}
            opcoes={TIPO_PROPRIEDADE}
            onChange={(v) => setForm({ ...form, tipo_propriedade: v })}
            required
          />
          <FieldTerr label="Área do terreno (m²)" value={areaTerreno} onChange={setAreaTerreno} type="number" min="0" step="0.01" required />
          <FieldTerr label="Área construída (m²)" value={areaConstruida} onChange={setAreaConstruida} type="number" min="0" step="0.01" />
          <FieldTerr label="Ano de construção" value={anoConstrucao} onChange={setAnoConstrucao} type="number" min="1800" max="2200" step="1" />
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Atualizar' : 'Cadastrar imóvel'}
          </button>
          {editando && (
            <button type="button" className="button button--ghost" onClick={cancelarEdicao}>
              Cancelar edição
            </button>
          )}
        </div>
      </form>

      <section className="card">
        <h3>Buscar imóvel por inscrição imobiliária</h3>
        <p className="muted">Consulta pela chave natural cadastral (RN-IMO-001).</p>
        <form className="form-grid" onSubmit={handleBuscarInscricao}>
          <FieldTerr
            label="Inscrição imobiliária"
            value={inscricaoBusca}
            onChange={setInscricaoBusca}
            required
            placeholder="Ex.: 1.2.3.4"
          />
          <div className="form-actions">
            <button type="submit" className="button" disabled={salvando}>
              Buscar
            </button>
            {resultadoBusca && (
              <button
                type="button"
                className="button button--ghost"
                onClick={() => setResultadoBusca(null)}
              >
                Limpar resultado
              </button>
            )}
          </div>
        </form>
        {resultadoBusca && (
          <div className="terr-resultado">
            <dl className="terr-detalhes">
              <div>
                <dt>Inscrição</dt>
                <dd>{resultadoBusca.inscricao_imobiliaria}</dd>
              </div>
              <div>
                <dt>Logradouro</dt>
                <dd>{logradouroNome(logradouros, resultadoBusca.logradouro_id)}</dd>
              </div>
              <div>
                <dt>Divisão territorial</dt>
                <dd>{bairroNome(bairros, resultadoBusca.bairro_id)}</dd>
              </div>
              <div>
                <dt>Número</dt>
                <dd>{resultadoBusca.numero ?? '—'}</dd>
              </div>
              <div>
                <dt>Área do terreno (m²)</dt>
                <dd>{formatarNumeroTerr(resultadoBusca.area_terreno_m2, 2)}</dd>
              </div>
              <div>
                <dt>Situação</dt>
                <dd>
                  <StatusTerr value={resultadoBusca.situacao} />
                </dd>
              </div>
            </dl>
            <div className="form-actions">
              <button
                type="button"
                className="button button--ghost button--sm"
                onClick={() => setImovelAberto(resultadoBusca.id)}
              >
                Abrir ficha completa
              </button>
            </div>
          </div>
        )}
      </section>

      {imovelAberto && (
        <DetalheImovel
          // A `key` remonta a ficha a cada imóvel, reiniciando o carregamento
          // sem precisar redefinir estado dentro do efeito.
          key={imovelAberto}
          imovelId={imovelAberto}
          bairros={bairros}
          logradouros={logradouros}
          onClose={() => setImovelAberto(null)}
        />
      )}

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Imóveis cadastrados ({filtrados.length} de {imoveis.length})</h3>
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            <select value={filtroSituacao} onChange={(e) => setFiltroSituacao(e.target.value)} className="terr-search">
              <option value="">Todas as situações</option>
              {SITUACOES_IMOVEL.map((s) => (
                <option key={s.valor} value={s.valor}>{s.rotulo}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Filtrar por inscrição ou número..."
              value={pesquisa}
              onChange={(e) => setPesquisa(e.target.value)}
              className="terr-search"
            />
            <select
              value={
                escopo.tipo === 'todos' ? '' : `${escopo.tipo === 'bairro' ? 'bairro' : 'log'}:${escopo.id}`
              }
              onChange={(e) => {
                const valor = e.target.value;
                setResultadoEscopo(null);
                setCarregandoEscopo(Boolean(valor));
                if (!valor) {
                  setEscopo({ tipo: 'todos', id: '' });
                } else if (valor.startsWith('bairro:')) {
                  setEscopo({ tipo: 'bairro', id: valor.slice(7) });
                } else if (valor.startsWith('log:')) {
                  setEscopo({ tipo: 'logradouro', id: valor.slice(4) });
                }
              }}
              className="terr-search"
            >
              <option value="">Todos os territórios</option>
              <optgroup label="Por divisão territorial">
                {bairros.map((b) => (
                  <option key={b.id} value={`bairro:${b.id}`}>
                    {b.codigo} — {b.nome}
                  </option>
                ))}
              </optgroup>
              <optgroup label="Por logradouro">
                {logradouros.map((l) => (
                  <option key={l.id} value={`log:${l.id}`}>
                    {l.codigo} — {l.nome}
                  </option>
                ))}
              </optgroup>
            </select>
          </div>
        </div>
        {filtrados.length === 0 ? (
          <p className="muted">Nenhum imóvel cadastrado.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Inscrição</th>
                <th>Logradouro</th>
                <th>Número</th>
                <th>Tipo</th>
                <th className="num">Terreno (m²)</th>
                <th className="num">Construída (m²)</th>
                <th>Situação</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {filtrados.map((i) => (
                <tr key={i.id}>
                  <td>{i.inscricao_imobiliaria}</td>
                  <td>{logradouroNome(logradouros, i.logradouro_id)}</td>
                  <td>{i.numero || 's/n'}</td>
                  <td>{i.tipo}</td>
                  <td className="num">{formatarNumeroTerr(i.area_terreno_m2, 2)}</td>
                  <td className="num">{formatarNumeroTerr(i.area_construida_m2, 2)}</td>
                  <td><StatusTerr value={i.situacao} /></td>
                  <td>
                    <button
                      type="button"
                      className="button button--ghost button--sm"
                      onClick={() => setImovelAberto(i.id)}
                    >
                      Ficha
                    </button>{' '}
                    <button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(i)}>
                      Editar
                    </button>{' '}
                    {i.situacao !== 'demolido' && (
                      <SituacaoMenu imovel={i} onAlterar={handleSituacao} desabilitado={salvando} />
                    )}{' '}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => handleExcluir(i)}
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

/**
 * Controle de situação do imóvel. A máquina de estados (RN-IMO-004) é aplicada
 * pelo servidor; as transições oferecidas aqui são as usuais e o sistema
 * recusa qualquer transição inválida com HTTP 409.
 */
function SituacaoMenu(props: {
  imovel: ImovelImo;
  onAlterar: (imovel: ImovelImo, situacao: string) => void;
  desabilitado: boolean;
}) {
  const [aberto, setAberto] = useState(false);
  return (
    <span style={{ position: 'relative', display: 'inline-block' }}>
      <button
        type="button"
        className="button button--ghost button--sm"
        onClick={() => setAberto((v) => !v)}
        disabled={props.desabilitado}
        aria-expanded={aberto}
      >
        Situação
      </button>
      {aberto && (
        <span
          style={{
            position: 'absolute',
            right: 0,
            top: '100%',
            zIndex: 20,
            display: 'flex',
            flexDirection: 'column',
            minWidth: '9rem',
            background: 'var(--cor-superficie)',
            border: '1px solid var(--cor-borda)',
            borderRadius: '0.5rem',
            boxShadow: 'var(--sombra)',
          }}
        >
          {SITUACOES_IMOVEL.filter((s) => s.valor !== props.imovel.situacao).map((s) => (
            <button
              key={s.valor}
              type="button"
              className="button button--ghost button--sm"
              style={{ justifyContent: 'flex-start', borderRadius: 0 }}
              onClick={() => {
                setAberto(false);
                props.onAlterar(props.imovel, s.valor);
              }}
            >
              {s.rotulo}
            </button>
          ))}
        </span>
      )}
    </span>
  );
}

