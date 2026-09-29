import { useEffect, useState } from 'react';
import type { AvaliacaoImo, AvaliacaoImoCreate } from '../../lib/api';
import {
  avaliarImovelImo,
  cancelarAvaliacaoImo,
  concluirAvaliacaoImo,
  listarBairrosTel,
  listarImoveisImo,
  listarPlantasValoresTel,
} from '../../lib/api';
import type { ImoResources } from './ImoPage';
import type { ExecutarTerr } from './TerrShared';
import {
  FieldTerr,
  SelectTerr,
  StatusTerr,
  bairroNome,
  formatarDataTerr,
  formatarMoedaTerr,
  imovelInscricao,
  paraNumero,
} from './TerrShared';

interface Props {
  resources: ImoResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const ANO_ATUAL = new Date().getFullYear();

const OCUPACOES = [
  { valor: 'residencial', rotulo: 'Residencial' },
  { valor: 'comercial', rotulo: 'Comercial' },
  { valor: 'industrial', rotulo: 'Industrial' },
  { valor: 'institucional', rotulo: 'Institucional' },
  { valor: 'misto', rotulo: 'Misto' },
  { valor: 'terreno', rotulo: 'Terreno' },
];

interface PlantaVigente {
  id: string;
  ano: number;
  bairro_id: string;
  ocupacao: string;
  valor_terreno_m2: number;
  valor_construcao_m2: number;
  aliquota_percent: number;
}

export function AvaliacoesImo({ resources, executar, salvando }: Props) {
  const [imoveis, setImoveis] = useState<{ id: string; inscricao_imobiliaria: string; bairro_id: string; area_terreno_m2: number; area_construida_m2: number }[]>([]);
  const [bairros, setBairros] = useState<{ id: string; nome: string }[]>([]);
  const [plantas, setPlantas] = useState<PlantaVigente[]>([]);

  const [imovelId, setImovelId] = useState('');
  const [ano, setAno] = useState(String(ANO_ATUAL));
  const [ocupacao, setOcupacao] = useState('residencial');
  const [vTerreno, setVTerreno] = useState('0');
  const [vConstrucao, setVConstrucao] = useState('0');
  const [aliquota, setAliquota] = useState('0');
  const [simulacao, setSimulacao] = useState({ terreno: 0, construcao: 0, venal: 0, lancamento: 0 });

  const avaliacoes = resources.avaliacoes.data ?? [];
  const imoveisLista = resources.imoveis.data ?? [];

  // O cadastro imobiliário e a planta de valores vivem em domínios distintos.
  useEffect(() => {
    listarImoveisImo().then(setImoveis).catch(() => setImoveis([]));
    listarBairrosTel().then(setBairros).catch(() => setBairros([]));
    listarPlantasValoresTel()
      .then((p) => setPlantas(p.filter((x) => x.situacao === 'vigente')))
      .catch(() => setPlantas([]));
  }, []);

  const imovelSelecionado = imoveis.find((i) => i.id === imovelId);

  /** Simula o valor venal antes de gravar, com os valores unitários informados. */
  function simular() {
    const areaT = imovelSelecionado?.area_terreno_m2 ?? 0;
    const areaC = imovelSelecionado?.area_construida_m2 ?? 0;
    const vt = paraNumero(vTerreno);
    const vc = paraNumero(vConstrucao);
    const aliquotaInformada = paraNumero(aliquota);
    const terreno = Math.round(areaT * vt * 100) / 100;
    const construcao = Math.round(areaC * vc * 100) / 100;
    const venal = Math.round((terreno + construcao) * 100) / 100;
    setSimulacao({
      terreno,
      construcao,
      venal,
      lancamento: Math.round(venal * (aliquotaInformada / 100) * 100) / 100,
    });
  }

  /** Preenche os valores unitários a partir da planta vigente do DOM-TEL. */
  function aplicarPlanta() {
    if (!imovelSelecionado) {
      window.alert('Selecione o imóvel antes de aplicar a planta genérica de valores.');
      return;
    }
    const anoInformado = paraNumero(ano, ANO_ATUAL);
    const planta = plantas.find(
      (p) =>
        p.bairro_id === imovelSelecionado.bairro_id &&
        p.ocupacao === ocupacao &&
        p.ano === anoInformado,
    );
    if (!planta) {
      window.alert(
        `Não há planta genérica de valores vigente para ${bairroNome(bairros, imovelSelecionado.bairro_id)}, ` +
          `ocupação "${ocupacao}" e ano ${anoInformado} no DOM-TEL.`,
      );
      return;
    }
    setVTerreno(String(planta.valor_terreno_m2));
    setVConstrucao(String(planta.valor_construcao_m2));
    setAliquota(String(planta.aliquota_percent));
    simularCom(planta.valor_terreno_m2, planta.valor_construcao_m2, planta.aliquota_percent);
  }

  function simularCom(vt: number, vc: number, aliquotaInformada: number) {
    const areaT = imovelSelecionado?.area_terreno_m2 ?? 0;
    const areaC = imovelSelecionado?.area_construida_m2 ?? 0;
    const terreno = Math.round(areaT * vt * 100) / 100;
    const construcao = Math.round(areaC * vc * 100) / 100;
    const venal = Math.round((terreno + construcao) * 100) / 100;
    setSimulacao({
      terreno,
      construcao,
      venal,
      lancamento: Math.round(venal * (aliquotaInformada / 100) * 100) / 100,
    });
  }


  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: AvaliacaoImoCreate = {
      imovel_id: imovelId,
      ano: paraNumero(ano, ANO_ATUAL),
      valor_terreno_m2_unitario: paraNumero(vTerreno),
      valor_construcao_m2_unitario: paraNumero(vConstrucao),
      aliquota_percent: paraNumero(aliquota),
      concluir: true,
    };
    const ok = await executar(
      () => avaliarImovelImo(payload),
      `Avaliação concluída: valor venal de ${formatarMoedaTerr(simulacao.venal)}!`,
    );
    if (ok) setSimulacao({ terreno: 0, construcao: 0, venal: 0, lancamento: 0 });
  }

  /**
   * Conclui a avaliação, fixando o valor venal e o lançamento.
   *
   * A transição é definitiva: um exercício já concluído não pode ser
   * reavaliado (RN-IMO-005).
   */
  async function handleConcluir(avaliacao: AvaliacaoImo) {
    const inscricao = imovelInscricao(imoveisLista, avaliacao.imovel_id);
    const aviso = `Concluir a avaliação de ${inscricao} (${avaliacao.ano}) no valor venal de ${formatarMoedaTerr(
      avaliacao.valor_venal,
    )}? A conclusão é definitiva e o exercício não poderá ser reavaliado.`;
    if (!window.confirm(aviso)) return;
    await executar(() => concluirAvaliacaoImo(avaliacao.id), 'Avaliação concluída com sucesso!');
  }

  async function handleCancelar(avaliacao: AvaliacaoImo) {
    const motivo = window.prompt(
      `Justificativa para cancelar a avaliação de ${imovelInscricao(imoveisLista, avaliacao.imovel_id)} (${avaliacao.ano}):`,
    );
    if (!motivo) return;
    await executar(
      () => cancelarAvaliacaoImo(avaliacao.id, motivo),
      'Avaliação cancelada com sucesso!',
    );
  }

  return (
    <section className="stack terr-avaliacoes">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>Avaliar valor venal do imóvel</h3>
        <p className="muted">
          O valor venal é apurado com os valores unitários vigentes da planta genérica de valores
          (RN-IMO-005). O botão <strong>Aplicar planta vigente</strong> busca a PGV no DOM-TEL para o
          ano, bairro e ocupação do imóvel selecionado.
        </p>
        <div className="form-grid">
          <SelectTerr
            label="Imóvel"
            value={imovelId}
            opcoes={imoveis.map((i) => ({
              valor: i.id,
              rotulo: `${i.inscricao_imobiliaria} — ${i.area_terreno_m2.toLocaleString('pt-BR')} m² terreno`,
            }))}
            onChange={(v) => {
              setImovelId(v);
              setSimulacao({ terreno: 0, construcao: 0, venal: 0, lancamento: 0 });
            }}
            required
            vazio="Selecione..."
          />
          <FieldTerr label="Exercício" value={ano} onChange={setAno} type="number" min="1900" max="2200" step="1" required />
          <SelectTerr label="Ocupação" value={ocupacao} opcoes={OCUPACOES} onChange={setOcupacao} required />
          <FieldTerr label="Valor do terreno (R$/m²)" value={vTerreno} onChange={setVTerreno} type="number" min="0" step="0.01" required />
          <FieldTerr label="Valor da construção (R$/m²)" value={vConstrucao} onChange={setVConstrucao} type="number" min="0" step="0.01" required />
          <FieldTerr label="Alíquota (%)" value={aliquota} onChange={setAliquota} type="number" min="0" max="100" step="0.01" />
        </div>
        <div className="form-actions">
          <button type="button" className="button button--ghost" onClick={aplicarPlanta} disabled={salvando}>
            Aplicar planta vigente (DOM-TEL)
          </button>
          <button type="button" className="button button--ghost" onClick={simular} disabled={salvando}>
            Simular cálculo
          </button>
          <button type="submit" className="button" disabled={salvando}>
            Registrar avaliação
          </button>
        </div>
        {simulacao.venal > 0 && (
          <div className="card-grid terr-kpis" style={{ marginTop: '0.75rem' }}>
            <article className="card kpi">
              <h3>Valor do terreno</h3>
              <p className="kpi-value">{formatarMoedaTerr(simulacao.terreno)}</p>
            </article>
            <article className="card kpi">
              <h3>Valor da construção</h3>
              <p className="kpi-value">{formatarMoedaTerr(simulacao.construcao)}</p>
            </article>
            <article className="card kpi">
              <h3>Valor venal</h3>
              <p className="kpi-value">{formatarMoedaTerr(simulacao.venal)}</p>
            </article>
            <article className="card kpi">
              <h3>Lançamento estimado</h3>
              <p className="kpi-value">{formatarMoedaTerr(simulacao.lancamento)}</p>
            </article>
          </div>
        )}
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Avaliações registradas ({avaliacoes.length})</h3>
        </div>
        {avaliacoes.length === 0 ? (
          <p className="muted">Nenhuma avaliação registrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Inscrição</th>
                <th>Ano</th>
                <th className="num">V. terreno (R$/m²)</th>
                <th className="num">V. construção (R$/m²)</th>
                <th className="num">Valor venal</th>
                <th className="num">Lançamento</th>
                <th>Situação</th>
                <th>Data</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {avaliacoes.map((a) => (
                <tr key={a.id}>
                  <td>{imovelInscricao(imoveisLista, a.imovel_id)}</td>
                  <td>{a.ano}</td>
                  <td className="num">{formatarMoedaTerr(a.valor_terreno_m2_unitario)}</td>
                  <td className="num">{formatarMoedaTerr(a.valor_construcao_m2_unitario)}</td>
                  <td className="num">{formatarMoedaTerr(a.valor_venal)}</td>
                  <td className="num">{formatarMoedaTerr(a.valor_lancamento)}</td>
                  <td><StatusTerr value={a.situacao} /></td>
                  <td>{formatarDataTerr(a.data_avaliacao)}</td>
                  <td>
                    {a.situacao === 'rascunho' && (
                      <button
                        type="button"
                        className="button button--sm"
                        onClick={() => handleConcluir(a)}
                        disabled={salvando}
                      >
                        Concluir
                      </button>
                    )}{' '}
                    {a.situacao !== 'concluida' && (
                      <button
                        type="button"
                        className="button button--danger button--sm"
                        onClick={() => handleCancelar(a)}
                        disabled={salvando}
                      >
                        Cancelar
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


