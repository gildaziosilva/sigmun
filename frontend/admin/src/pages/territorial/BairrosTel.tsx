import { useState } from 'react';
import type { BairroTel, BairroTelCreate } from '../../lib/api';
import { atualizarBairroTel, criarBairroTel, excluirBairroTel } from '../../lib/api';
import type { TelResources } from './TelPage';
import type { ExecutarTerr } from './TerrShared';
import { FieldTerr, SelectTerr, StatusTerr, TIPOS_BAIRRO, paraNumero } from './TerrShared';

interface Props {
  resources: TelResources;
  executar: ExecutarTerr;
  salvando: boolean;
}

const FORM_VAZIO: BairroTelCreate = {
  codigo: '',
  nome: '',
  tipo: 'bairro',
  populacao_estimada: 0,
  area_km2: 0,
};

export function BairrosTel({ resources, executar, salvando }: Props) {
  const [form, setForm] = useState<BairroTelCreate>({ ...FORM_VAZIO });
  const [populacao, setPopulacao] = useState('0');
  const [area, setArea] = useState('0');
  const [situacao, setSituacao] = useState('');
  const [editando, setEditando] = useState<BairroTel | null>(null);
  const [pesquisa, setPesquisa] = useState('');

  const bairros = resources.bairros.data ?? [];
  const filtrados = bairros.filter(
    (b) =>
      b.codigo.toLowerCase().includes(pesquisa.toLowerCase()) ||
      b.nome.toLowerCase().includes(pesquisa.toLowerCase()),
  );
  const logradouros = resources.logradouros.data ?? [];

  function iniciarEdicao(bairro: BairroTel) {
    setEditando(bairro);
    setForm({
      codigo: bairro.codigo,
      nome: bairro.nome,
      tipo: bairro.tipo,
      populacao_estimada: bairro.populacao_estimada,
      area_km2: bairro.area_km2,
    });
    setPopulacao(String(bairro.populacao_estimada));
    setArea(String(bairro.area_km2));
  }

  function cancelarEdicao() {
    setEditando(null);
    setForm({ ...FORM_VAZIO });
    setPopulacao('0');
    setArea('0');
    setSituacao('');
  }

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    const payload: BairroTelCreate = {
      ...form,
      populacao_estimada: paraNumero(populacao),
      area_km2: paraNumero(area),
    };
    if (editando) {
      const ok = await executar(
        () => atualizarBairroTel(editando.id, { ...payload, situacao: situacao || undefined }),
        'Bairro atualizado com sucesso!',
      );
      if (ok) cancelarEdicao();
      return;
    }
    const ok = await executar(() => criarBairroTel(payload), 'Bairro cadastrado com sucesso!');
    if (ok) cancelarEdicao();
  }

  async function handleExcluir(bairro: BairroTel) {
    const vinculados = logradouros.filter(
      (l) => l.bairro_id === bairro.id && l.situacao === 'ativo',
    ).length;
    const aviso =
      vinculados > 0
        ? `O bairro ${bairro.nome} possui ${vinculados} logradouro(s) ativo(s). A exclusão será recusada pelo sistema (RN-TEL-006). Confirmar?`
        : `Excluir o bairro ${bairro.codigo} - ${bairro.nome}?`;
    if (!window.confirm(aviso)) return;
    await executar(() => excluirBairroTel(bairro.id), 'Bairro excluído com sucesso!');
  }

  return (
    <section className="stack terr-bairros">
      <form className="card terr-form" onSubmit={handleSubmit}>
        <h3>{editando ? 'Editar divisão territorial' : 'Cadastrar nova divisão territorial'}</h3>
        <div className="form-grid">
          <FieldTerr
            label="Código"
            value={form.codigo}
            onChange={(v) => setForm({ ...form, codigo: v })}
            required
            hint="Único no município (RN-TEL-001)"
          />
          <FieldTerr label="Nome" value={form.nome} onChange={(v) => setForm({ ...form, nome: v })} required />
          <SelectTerr
            label="Tipo"
            value={form.tipo ?? 'bairro'}
            opcoes={TIPOS_BAIRRO}
            onChange={(v) => setForm({ ...form, tipo: v })}
            required
          />
          <FieldTerr label="População estimada" value={populacao} onChange={setPopulacao} type="number" min="0" step="1" />
          <FieldTerr label="Área (km²)" value={area} onChange={setArea} type="number" min="0" step="0.01" />
          {editando && (
            <SelectTerr
              label="Situação"
              value={situacao}
              opcoes={[
                { valor: 'ativo', rotulo: 'Ativo' },
                { valor: 'inativo', rotulo: 'Inativo' },
              ]}
              onChange={setSituacao}
              vazio="(sem alteração)"
            />
          )}
        </div>
        <div className="form-actions">
          <button type="submit" className="button" disabled={salvando}>
            {editando ? 'Atualizar' : 'Cadastrar divisão'}
          </button>
          {editando && (
            <button type="button" className="button button--ghost" onClick={cancelarEdicao}>
              Cancelar edição
            </button>
          )}
        </div>
      </form>

      <section className="card terr-lista">
        <div className="terr-lista-header">
          <h3>Divisões cadastradas ({bairros.length})</h3>
          <input
            type="text"
            placeholder="Filtrar por código ou nome..."
            value={pesquisa}
            onChange={(e) => setPesquisa(e.target.value)}
            className="terr-search"
          />
        </div>
        {filtrados.length === 0 ? (
          <p className="muted">Nenhuma divisão territorial cadastrada.</p>
        ) : (
          <table className="terr-table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Nome</th>
                <th>Tipo</th>
                <th className="num">População</th>
                <th className="num">Área (km²)</th>
                <th className="num">Logradouros</th>
                <th>Situação</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {filtrados.map((b) => (
                <tr key={b.id}>
                  <td>{b.codigo}</td>
                  <td>{b.nome}</td>
                  <td>{b.tipo.replaceAll('_', ' ')}</td>
                  <td className="num">{b.populacao_estimada.toLocaleString('pt-BR')}</td>
                  <td className="num">
                    {b.area_km2.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
                  </td>
                  <td className="num">{logradouros.filter((l) => l.bairro_id === b.id).length}</td>
                  <td><StatusTerr value={b.situacao} /></td>
                  <td>
                    <button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(b)}>
                      Editar
                    </button>{' '}
                    <button
                      type="button"
                      className="button button--danger button--sm"
                      onClick={() => handleExcluir(b)}
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

