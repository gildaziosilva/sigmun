import { useEffect, useState } from 'react';
import {
  listarAbastecimentos,
  listarManutencoes,
  listarVeiculos,
  obterVeiculo,
  type AbastecimentoFro,
  type ManutencaoFro,
  type VeiculoFro,
} from '../../lib/api';
import { TabelaEstado, useApiData } from '../../components/DataState';

function formatarMoeda(valor: number): string {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}

export default function FroPage() {
  const [veiculos, recarregarVeiculos] = useApiData(() => listarVeiculos());
  const [abastecimentos, recarregarAbastecimentos] = useApiData(() => listarAbastecimentos());
  const [manutencoes, recarregarManutencoes] = useApiData(() => listarManutencoes());
  const [veiculoId, setVeiculoId] = useState('');
  const [veiculoDetalhe, setVeiculoDetalhe] = useState<VeiculoFro | null>(null);
  const [veiculoErro, setVeiculoErro] = useState('');

  async function consultarVeiculo() {
    const id = veiculoId.trim();
    if (!id) {
      setVeiculoErro('Informe o ID do veículo.');
      setVeiculoDetalhe(null);
      return;
    }
    setVeiculoErro('');
    try {
      setVeiculoDetalhe(await obterVeiculo(id));
    } catch (err) {
      setVeiculoDetalhe(null);
      setVeiculoErro(err instanceof Error ? err.message : 'Falha ao consultar veículo.');
    }
  }

  useEffect(() => {
    recarregarVeiculos();
    recarregarAbastecimentos();
    recarregarManutencoes();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <section className="stack">
      <div className="page-head">
        <h2 className="section-title">Gestão de Frota (FRO)</h2>
        <button
          type="button"
          className="button button--ghost"
          onClick={() => {
            recarregarVeiculos();
            recarregarAbastecimentos();
            recarregarManutencoes();
          }}
        >
          Recarregar
        </button>
      </div>
      <p className="muted">
        Veículos, abastecimentos e manutenções via GET /api/v1/fro/…. Detalhe avulso via
        GET /api/v1/fro/veiculos/:id. Rotas e ações de ciclo (baixar/concluir) evoluem na
        próxima iteração.
      </p>

      <article className="card">
        <h3>Veículo por ID</h3>
        <div className="consulta-row">
          <input
            value={veiculoId}
            onChange={(e) => setVeiculoId(e.target.value)}
            placeholder="ID do veículo"
            aria-label="ID do veículo"
          />
          <button type="button" className="button" onClick={consultarVeiculo}>
            Consultar
          </button>
        </div>
        {veiculoErro && (
          <p className="alert alert--error" role="alert">
            {veiculoErro}
          </p>
        )}
        {veiculoDetalhe && (
          <dl className="detail-list">
            <div>
              <dt>Placa</dt>
              <dd className="mono">{veiculoDetalhe.placa}</dd>
            </div>
            <div>
              <dt>Marca/Modelo</dt>
              <dd>
                {veiculoDetalhe.marca} {veiculoDetalhe.modelo}
              </dd>
            </div>
            <div>
              <dt>Tipo</dt>
              <dd>{veiculoDetalhe.tipo}</dd>
            </div>
            <div>
              <dt>Odômetro</dt>
              <dd>{veiculoDetalhe.odometro_atual.toLocaleString('pt-BR')} km</dd>
            </div>
            <div>
              <dt>Status</dt>
              <dd>{veiculoDetalhe.status}</dd>
            </div>
          </dl>
        )}
      </article>

      <article className="card">
        <h3>Veículos</h3>
        <TabelaEstado
          loading={veiculos.loading}
          erro={veiculos.erro}
          vazio={!veiculos.data || veiculos.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Placa</th>
                  <th>Marca/Modelo</th>
                  <th>Tipo</th>
                  <th>Odômetro</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {(veiculos.data ?? []).map((v: VeiculoFro) => (
                  <tr key={v.id}>
                    <td className="mono">{v.placa}</td>
                    <td>
                      {v.marca} {v.modelo}
                    </td>
                    <td>
                      <span className="badge">{v.tipo}</span>
                    </td>
                    <td>{v.odometro_atual.toLocaleString('pt-BR')} km</td>
                    <td>
                      <span className="badge">{v.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <article className="card">
        <h3>Abastecimentos</h3>
        <TabelaEstado
          loading={abastecimentos.loading}
          erro={abastecimentos.erro}
          vazio={!abastecimentos.data || abastecimentos.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Veículo</th>
                  <th>Data</th>
                  <th>Litros</th>
                  <th>Valor total</th>
                </tr>
              </thead>
              <tbody>
                {(abastecimentos.data ?? []).map((a: AbastecimentoFro) => (
                  <tr key={a.id}>
                    <td className="mono">{a.veiculo_id}</td>
                    <td>{a.data ?? '—'}</td>
                    <td>{a.quantidade_litros.toLocaleString('pt-BR')} L</td>
                    <td>{formatarMoeda(a.valor_total)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>

      <article className="card">
        <h3>Manutenções</h3>
        <TabelaEstado
          loading={manutencoes.loading}
          erro={manutencoes.erro}
          vazio={!manutencoes.data || manutencoes.data.length === 0}
        >
          <div className="table-wrap">
            <table className="table">
              <thead>
                <tr>
                  <th>Veículo</th>
                  <th>Tipo</th>
                  <th>Descrição</th>
                  <th>Valor</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {(manutencoes.data ?? []).map((m: ManutencaoFro) => (
                  <tr key={m.id}>
                    <td className="mono">{m.veiculo_id}</td>
                    <td>
                      <span className="badge">{m.tipo}</span>
                    </td>
                    <td>{m.descricao}</td>
                    <td>{formatarMoeda(m.valor)}</td>
                    <td>
                      <span className="badge">{m.status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabelaEstado>
      </article>
    </section>
  );
}
