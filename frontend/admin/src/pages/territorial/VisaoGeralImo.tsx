import type { ImoResources } from './ImoPage';
import {
  Progresso,
  coberturaAvaliacao,
  coberturaCaracteristica,
  coberturaGeometria,
  coberturaTitular,
  formatarMoedaTerr,
  formatarNumeroTerr,
  imovelInscricao,
} from './TerrShared';

interface Props {
  resources: ImoResources;
}

export function VisaoGeralImo({ resources }: Props) {
  const { imoveis, proprietarios, avaliacoes, geometrias, caracteristicas } = resources;

  const totalImoveis = imoveis.data?.length ?? 0;
  const ativos = imoveis.data?.filter((i) => i.situacao === 'ativo').length ?? 0;
  const emObra = imoveis.data?.filter((i) => i.situacao === 'em_obra').length ?? 0;
  const demolidos = imoveis.data?.filter((i) => i.situacao === 'demolido').length ?? 0;

  const areaTotal = imoveis.data?.reduce((t, i) => t + i.area_terreno_m2, 0) ?? 0;
  const areaConstruida = imoveis.data?.reduce((t, i) => t + i.area_construida_m2, 0) ?? 0;

  const concluidas = avaliacoes.data?.filter((a) => a.situacao === 'concluida') ?? [];
  const valorVenalTotal = concluidas.reduce((t, a) => t + a.valor_venal, 0);
  const lancamentoTotal = concluidas.reduce((t, a) => t + a.valor_lancamento, 0);
  const maiores = [...concluidas].sort((a, b) => b.valor_venal - a.valor_venal).slice(0, 5);

  const anoCorrente = new Date().getFullYear();

  return (
    <section className="stack terr-visao-geral">
      <div className="card-grid terr-kpis">
        <article className="card kpi">
          <h3>Imóveis cadastrados</h3>
          <p className="kpi-value">{formatarNumeroTerr(totalImoveis)}</p>
        </article>
        <article className="card kpi">
          <h3>Imóveis ativos</h3>
          <p className="kpi-value">{formatarNumeroTerr(ativos)}</p>
        </article>
        <article className="card kpi">
          <h3>Imóveis em obra</h3>
          <p className="kpi-value">{formatarNumeroTerr(emObra)}</p>
        </article>
        <article className="card kpi">
          <h3>Imóveis demolidos</h3>
          <p className="kpi-value">{formatarNumeroTerr(demolidos)}</p>
        </article>
        <article className="card kpi">
          <h3>Área de terreno</h3>
          <p className="kpi-value">{formatarNumeroTerr(areaTotal, 2)} m²</p>
        </article>
        <article className="card kpi">
          <h3>Área construída</h3>
          <p className="kpi-value">{formatarNumeroTerr(areaConstruida, 2)} m²</p>
        </article>
        <article className="card kpi">
          <h3>Valor venal apurado</h3>
          <p className="kpi-value">{formatarMoedaTerr(valorVenalTotal)}</p>
        </article>
        <article className="card kpi">
          <h3>Lançamento estimado</h3>
          <p className="kpi-value">{formatarMoedaTerr(lancamentoTotal)}</p>
        </article>
      </div>

      <div className="terr-recentes">
        <section className="card terr-recentes-card">
          <h3>Maiores valores venais apurados</h3>
          {maiores.length === 0 ? (
            <p className="muted">Nenhuma avaliação concluída.</p>
          ) : (
            <table className="terr-table">
              <thead>
                <tr>
                  <th>Inscrição</th>
                  <th>Ano</th>
                  <th className="num">Terreno</th>
                  <th className="num">Construção</th>
                  <th className="num">Valor venal</th>
                  <th className="num">Lançamento</th>
                </tr>
              </thead>
              <tbody>
                {maiores.map((a) => (
                  <tr key={a.id}>
                    <td>{imovelInscricao(imoveis.data ?? [], a.imovel_id)}</td>
                    <td>{a.ano}</td>
                    <td className="num">{formatarMoedaTerr(a.valor_terreno)}</td>
                    <td className="num">{formatarMoedaTerr(a.valor_construcao)}</td>
                    <td className="num">{formatarMoedaTerr(a.valor_venal)}</td>
                    <td className="num">{formatarMoedaTerr(a.valor_lancamento)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>

        <section className="card terr-recentes-card">
          <h3>Cobertura cadastral</h3>
          <table className="terr-table">
            <thead>
              <tr>
                <th>Indicador</th>
                <th className="num">Imóveis</th>
                <th>Cobertura</th>
              </tr>
            </thead>
            <tbody>
              <Indicador
                rotulo="Com geometria georreferenciada"
                quantidade={(imoveis.data ?? []).filter((i) =>
                  (geometrias.data ?? []).some((g) => g.imovel_id === i.id),
                ).length}
                percentual={coberturaGeometria(totalImoveis, geometrias.data ?? [])}
              />
              <Indicador
                rotulo="Com característica construtiva"
                quantidade={(imoveis.data ?? []).filter((i) =>
                  (caracteristicas.data ?? []).some((c) => c.imovel_id === i.id),
                ).length}
                percentual={coberturaCaracteristica(totalImoveis, caracteristicas.data ?? [])}
              />
              <Indicador
                rotulo="Com proprietário titular"
                quantidade={(imoveis.data ?? []).filter((i) =>
                  (proprietarios.data ?? []).some((p) => p.imovel_id === i.id && p.principal),
                ).length}
                percentual={coberturaTitular(totalImoveis, proprietarios.data ?? [])}
              />
              <Indicador
                rotulo={`Avaliados em ${anoCorrente}`}
                quantidade={(imoveis.data ?? []).filter((i) =>
                  (avaliacoes.data ?? []).some((a) => a.imovel_id === i.id && a.ano === anoCorrente),
                ).length}
                percentual={coberturaAvaliacao(totalImoveis, avaliacoes.data ?? [])}
              />
            </tbody>
          </table>
        </section>
      </div>
    </section>
  );
}

function Indicador(props: { rotulo: string; quantidade: number; percentual: number }) {
  return (
    <tr>
      <td>{props.rotulo}</td>
      <td className="num">{formatarNumeroTerr(props.quantidade)}</td>
      <td><Progresso valor={props.percentual} /></td>
    </tr>
  );
}

