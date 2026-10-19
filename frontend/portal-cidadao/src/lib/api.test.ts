/** T-5.2 + T-5.4: api.ts do Portal do Cidadão — erro, 401/403 e correlation_id. */
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ApiError, abrirManifestacao, consultarProtocolo, extractErrorMessage, formatProtocolo, onUnauthorized } from './api';

function mockFetchOnce(status: number, body: unknown, headers: Record<string, string> = {}) {
  const h = new Headers({ 'Content-Type': 'application/json', ...headers });
  globalThis.fetch = vi.fn(async () =>
    new Response(JSON.stringify(body), { status, headers: h }),
  ) as unknown as typeof fetch;
}

describe('ApiError', () => {
  it('expõe correlation_id em erro 500 via friendlyMessage', () => {
    const err = new ApiError(500, 'Erro interno', 'corr-123');
    expect(err.correlationId).toBe('corr-123');
    expect(err.friendlyMessage).toContain('corr-123');
  });

  it('não anexa protocolo em erro 4xx', () => {
    const err = new ApiError(404, 'Não encontrado', 'corr-9');
    expect(err.friendlyMessage).toBe('Não encontrado');
  });
});

describe('consultarProtocolo', () => {
  beforeEach(() => {
    onUnauthorized(null);
    vi.unstubAllGlobals();
  });

  it('filtra sigilosos e casa por código (case-insensitive)', async () => {
    mockFetchOnce(200, {
      total: 2,
      page: 0,
      page_size: 200,
      items: [
        { id: '1', codigo: 'DOC-2026-0001', titulo: 'Público', status: 'ativo' },
        { id: '2', codigo: 'DOC-2026-0001', titulo: 'Sigiloso', status: 'ativo', is_sigiloso: true },
      ],
    });
    const r = await consultarProtocolo('doc-2026-0001');
    expect(r).toHaveLength(1);
    expect(r[0].titulo).toBe('Público');
  });

  it('dispara handler global em 401', async () => {
    const seen: number[] = [];
    onUnauthorized((s) => seen.push(s));
    mockFetchOnce(401, { detail: 'Não autenticado' });
    await expect(consultarProtocolo('X')).rejects.toBeInstanceOf(ApiError);
    expect(seen).toEqual([401]);
  });

  it('lê a mensagem do envelope padrão da API (error.message)', async () => {
    onUnauthorized(null);
    mockFetchOnce(422, {
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Nome é obrigatório para manifestação não anônima',
        correlation_id: 'c-1',
        timestamp: '2026-10-10T00:00:00Z',
      },
    });
    const err = await abrirManifestacao({
      tipo: 'reclamacao',
      assunto: 'Buraco na rua',
      descricao: 'Buraco sem correção.',
      cidadao_anonimo: false,
      orgao_destino: 'Obras',
    }).catch((e: unknown) => e);
    expect(err).toBeInstanceOf(ApiError);
    expect((err as ApiError).status).toBe(422);
    expect((err as ApiError).detail).toContain('Nome é obrigatório');
  });
});

describe('extractErrorMessage', () => {
  it('prioriza error.message, depois detail, depois fallback', () => {
    expect(
      extractErrorMessage({ error: { message: 'Domínio recusou' } }, '/x', 422),
    ).toBe('Domínio recusou');
    expect(extractErrorMessage({ detail: 'FastAPI padrão' }, '/x', 422)).toBe('FastAPI padrão');
    expect(extractErrorMessage(null, '/x', 500)).toBe('Falha ao acessar /x (HTTP 500)');
  });
});

describe('formatProtocolo', () => {
  it('formata numero/ano e trata nulo', () => {
    expect(formatProtocolo({ numero: '2026-000001', ano: 2026 })).toBe('2026-000001/2026');
    expect(formatProtocolo(null)).toBe('protocolo pendente');
  });
});
