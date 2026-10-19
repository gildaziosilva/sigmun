/** T-5.2 + T-5.4: api.ts do admin — Bearer, 401 global e correlation_id. */
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ApiError, apiGet, clearToken, onUnauthorized, setToken } from './api';

function mockFetchOnce(status: number, body: unknown, headers: Record<string, string> = {}) {
  const h = new Headers({ 'Content-Type': 'application/json', ...headers });
  globalThis.fetch = vi.fn(async () =>
    new Response(JSON.stringify(body), { status, headers: h }),
  ) as unknown as typeof fetch;
}

describe('admin api', () => {
  beforeEach(() => {
    onUnauthorized(null);
    clearToken();
    window.sessionStorage.clear();
  });

  it('injeta Authorization Bearer quando há token', async () => {
    setToken('tok-123');
    mockFetchOnce(200, { ok: true });
    await apiGet<{ ok: boolean }>('/api/v1/idn/usuarios');
    const init = (globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls[0][1] as RequestInit;
    expect((init.headers as Record<string, string>).Authorization).toBe('Bearer tok-123');
  });

  it('401 anônimo dispara handler e carrega correlation_id', async () => {
    const seen: number[] = [];
    onUnauthorized((s) => seen.push(s));
    mockFetchOnce(401, { detail: 'Expirada' }, { 'X-Correlation-ID': 'c-1' });
    try {
      await apiGet('/api/v1/compras');
      expect.unreachable();
    } catch (err) {
      expect(err).toBeInstanceOf(ApiError);
      expect((err as ApiError).correlationId).toBe('c-1');
    }
    expect(seen).toEqual([401]);
  });

  it('friendlyMessage inclui protocolo só em 5xx', () => {
    expect(new ApiError(500, 'X', 'k').friendlyMessage).toContain('k');
    expect(new ApiError(400, 'X', 'k').friendlyMessage).toBe('X');
  });
});
