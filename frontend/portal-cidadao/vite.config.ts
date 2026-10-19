import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
// T-5.2: seção `test` — Vitest + jsdom (api.ts + fluxos OUV).
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    proxy: {
      // Em desenvolvimento, repassa chamadas da API para o backend local.
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/health': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    include: ['src/**/*.test.{ts,tsx}'],
  },
})
