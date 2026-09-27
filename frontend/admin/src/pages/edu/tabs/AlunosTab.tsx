import { useState } from 'react';
import { obterAluno, atualizarAluno, type AlunoEdu } from '../../../lib/api';
import type { EduResources, ExecutarEdu } from '../EduShared';
import { formatarData, StatusBadge, Field } from '../EduShared';

interface Props {
  resources: EduResources;
  executar: ExecutarEdu;
  salvando: boolean;
}

export function AlunosTab({ resources, executar, salvando }: Props) {
  const { alunos } = resources;
  const [editandoId, setEditandoId] = useState<string | null>(null);
  const [formData, setFormData] = useState<Partial<AlunoEdu>>({});

  async function iniciarEdicao(aluno: AlunoEdu) {
    const detalhe = await obterAluno(aluno.id);
    setFormData({
      nome: detalhe.nome,
      cpf: detalhe.cpf || '',
      data_nascimento: detalhe.data_nascimento || '',
      sexo: detalhe.sexo,
      nome_mae: detalhe.nome_mae || '',
      telefone: detalhe.telefone || '',
      endereco: detalhe.endereco || '',
      status: detalhe.status,
    });
    setEditandoId(aluno.id);
  }

  async function salvarEdicao(id: string) {
    await executar(async () => {
      const payload = Object.fromEntries(
        Object.entries(formData).filter(([, v]) => v !== null && v !== undefined)
      ) as Record<string, string>;
      await atualizarAluno(id, { ...payload, created_by: '' });
    }, 'Aluno atualizado com sucesso');
    setEditandoId(null);
  }

  return (
    <section className="sau-content">
      <header className="sau-section-head">
        <h3>Alunos</h3>
        <p className="muted">Cadastro de alunos da rede municipal de ensino.</p>
      </header>

      {alunos.loading && <p className="muted">Carregando alunos…</p>}
      {alunos.erro && <p className="sau-feedback sau-feedback--error" role="alert">{alunos.erro}</p>}
      {alunos.data?.length === 0 && !alunos.loading && !alunos.erro && <p className="muted">Nenhum aluno cadastrado.</p>}

      {alunos.data && alunos.data.length > 0 && (
        <div className="sau-table-wrap">
          <table className="sau-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>CPF</th>
                <th>Data Nasc.</th>
                <th>Sexo</th>
                <th>Status</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {alunos.data.map((a) => (
                <tr key={a.id}>
                  <td className="mono">{a.id.slice(0, 8)}…</td>
                  <td>
                    {editandoId === a.id ? (
                      <Field
                        label=""
                        value={formData.nome || ''}
                        onChange={(v) => setFormData({ ...formData, nome: v })}
                        placeholder="Nome"
                      />
                    ) : (
                      a.nome
                    )}
                  </td>
                  <td>{a.cpf || '—'}</td>
                  <td>{formatarData(a.data_nascimento)}</td>
                  <td>{a.sexo}</td>
                  <td><StatusBadge value={a.status} /></td>
                  <td className="sau-actions">
                    {editandoId === a.id ? (
                      <>
                        <button type="button" className="button button--primary button--sm" onClick={() => salvarEdicao(a.id)} disabled={salvando}>Salvar</button>
                        <button type="button" className="button button--ghost button--sm" onClick={() => setEditandoId(null)}>Cancelar</button>
                      </>
                    ) : (
                      <button type="button" className="button button--ghost button--sm" onClick={() => iniciarEdicao(a)}>Editar</button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
