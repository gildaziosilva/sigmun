/** T-5.2: Login do admin — render, validação e labels (a11y). */
import { describe, expect, it, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Login from '../pages/Login';

vi.mock('../auth/AuthContext', () => ({
  useAuth: () => ({
    entrar: vi.fn(),
    erro: '',
  }),
}));

vi.mock('../lib/api', async (importOriginal) => {
  const mod = await importOriginal<typeof import('../lib/api')>();
  return { ...mod, fetchHealth: vi.fn(async () => ({ status: 'ok', service: 'sigmun', version: 'x' })) };
});

describe('Login', () => {
  it('renderiza campos com labels e valida vazio', async () => {
    render(<Login />);
    expect(screen.getByLabelText(/login/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/senha/i)).toBeInTheDocument();
    await userEvent.click(screen.getByRole('button', { name: /entrar/i }));
    expect(await screen.findByRole('alert')).toHaveTextContent(/preencha login e senha/i);
  });
});
