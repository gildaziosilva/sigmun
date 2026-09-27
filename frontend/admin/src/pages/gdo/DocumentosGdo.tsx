import { useState } from 'react';
import { TabelaEstado } from '../../components/DataState';
import { type DocumentoCreateRequest, criarDocumento } from '../../lib/api';
import { type GdoResources, type ExecutarGdo, Field, StatusBadge } from './GdoShared';

export interface DocumentosGdoProps {
  resources: GdoResources;
  executar: ExecutarGdo;
  salvando: boolean;
  onVerDetalhe: (id: string) => void;
}

export function DocumentosGdo({ resources, executar, salvando, onVerDetalhe }: DocumentosGdoProps) {
  const [mostrarForm, setMostrarForm] = useState(false);
  const [form, setForm] = useState<DocumentoCreateRequest>({
    codigo: '',
    numero: '',
    ano: new Date().getFullYear(),
    tipo_documental_id: '',
    titulo: '',
    descricao: '',
    unidade_autor_id: '',
    unidade_arquivo_id: '',
    processo_id: '',
    is_sigiloso: false,
    conteudo_ref: '',
    hash_integridade: '',
  });

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    await executar(
      async () => {
        await criarDocumento(form);
        setMostrarForm(false);
        setForm({
          codigo: '',
          numero: '',
          ano: new Date().getFullYear(),
          tipo_documental_id: '',
          titulo: '',
          descricao: '',
          unidade_autor_id: '',
          unidade_arquivo_id: '',
          processo_id: '',
          is_sigiloso: false,
          conteudo_ref: '',
          hash_integridade: '',
        });
      },
      'Documento criado com sucesso',
    );
  }

  return (
    <div className="stack gdo-tab-content">
      <div className="gdo-toolbar">
        <button type="button" className="button" onClick={() => setMostrarForm(!mostrarForm)}>
          {mostrarForm ? 'Cancelar' : 'Novo Documento'}
        </button>
      </div>

      {mostrarForm && (
        <form onSubmit={handleSubmit} className="card card--form gdo-form">
          <h3>Novo Documento</h3>
          <div className="grid grid--2">
            <Field label="Código" value={form.codigo} onChange={(v) => setForm({ ...form, codigo: v })} required hint="Código único do documento" />
            <Field label="Número" value={form.numero} onChange={(v) => setForm({ ...form, numero: v })} required />
            <Field label="Ano" type="number" value={String(form.ano)} onChange={(v) => setForm({ ...form, ano: Number(v) })} required min="1900" max="2100" />
            <Field label="Tipo Documental ID" value={form.tipo_documental_id} onChange={(v) => setForm({ ...form, tipo_documental_id: v })} required hint="Código do tipo documental" />
          </div>
          <div className="grid grid--2">
            <Field label="Título" value={form.titulo} onChange={(v) => setForm({ ...form, titulo: v })} required />
            <Field label="Unidade Autora ID" value={form.unidade_autor_id} onChange={(v) => setForm({ ...form, unidade_autor_id: v })} required />
            <Field label="Unidade Arquivo ID" value={form.unidade_arquivo_id ?? ''} onChange={(v) => setForm({ ...form, unidade_arquivo_id: v })} />
            <Field label="Processo ID" value={form.processo_id ?? ''} onChange={(v) => setForm({ ...form, processo_id: v })} />
          </div>
          <Field label="Descrição" value={form.descricao ?? ''} onChange={(v) => setForm({ ...form, descricao: v })} />
          <div className="grid grid--2">
            <label>
              <span>Sigiloso</span>
              <input type="checkbox" checked={form.is_sigiloso} onChange={(e) => setForm({ ...form, is_sigiloso: e.target.checked })} />
            </label>
          </div>
          <div className="form-actions">
            <button type="button" className="button button--ghost" onClick={() => setMostrarForm(false)}>Cancelar</button>
            <button type="submit" className="button" disabled={salvando}>{salvando ? 'Salvando...' : 'Criar'}</button>
          </div>
        </form>
      )}

      <TabelaEstado
        loading={resources.documentos.loading}
        erro={resources.documentos.erro}
        vazio={!resources.documentos.data || resources.documentos.data.items.length === 0}
      >
        <div className="table-wrap">
          <table className="table">
            <thead>
              <tr>
                <th>Código</th>
                <th>Título</th>
                <th>Ano</th>
                <th>Status</th>
                <th aria-label="Ações" />
              </tr>
            </thead>
            <tbody>
              {resources.documentos.data?.items.map((d) => (
                <tr key={d.id}>
                  <td className="mono">{d.codigo}</td>
                  <td>{d.titulo}</td>
                  <td>{d.ano}</td>
                  <td>
                    <StatusBadge value={d.status} />
                    {d.is_sigiloso && <span className="badge badge--warn">sigiloso</span>}
                  </td>
                  <td>
                    <button type="button" className="link" onClick={() => onVerDetalhe(d.id)}>
                      Detalhe
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="muted">Total: {resources.documentos.data?.total ?? 0} documentos</p>
      </TabelaEstado>
    </div>
  );
}