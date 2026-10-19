/** T-5.2 + T-5.4: api.ts do Portal do Fornecedor — paginação, 401 e correlation_id. */
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ApiError, listarContratos, listarLicitacoes, onUnauthorized } from './api';

function mockFetchOnce(status: number, body: unknown, headers: Record<string, string> = {}) {
  const h = new Headers({ 'Content-Type': 'application/json', ...headers });
  globalThis.fetch = vi.fn(async () =>
    new Response(JSON.stringify(body), { status, headers: h }),
  ) as unknown as typeof fetch;
}

describe('listarLicitacoes', () => {
  beforeEach(() => {
    onUnauthorized(null);
  });

  it('monta query com page/page_size e filtro', async () => {
    mockFetchOnce(200, { total: 0, page: 1, page_size: 10, items: [] });
    const r = await listarLicitacoes(1, 10, 'PUBLICADA');
    expect(r.page).toBe(1);
    const url = (globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls[0][0] as string;
    expect(url).toContain('page=1');
    expect(url).toContain('situacao=PUBLICADA');
  });

  it('propaga correlation_id no ApiError 500', async () => {
    mockFetchOnce(500, { detail: 'Falha' }, { 'X-Correlation-ID': 'abc-1' });
    try {
      await listarLicitacoes();
      expect.unreachable();
    } catch (err) {
      expect(err).toBeInstanceOf(ApiError);
      expect((err as ApiError).correlationId).toBe('abc-1');
      expect((err as ApiError).friendlyMessage).toContain('abc-1');
    }
  });

  it('avisa handler global em 403', async () => {
    const seen: number[] = [];
    onUnauthorized((s) => seen.push(s));
    mockFetchOnce(403, { detail: 'Proibido' });
    await expect(listarContratos()).rejects.toBeInstanceOf(ApiError);
    expect(seen).toEqual([403]);
  });
});
