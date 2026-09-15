# Evidência de Teste de Carga — DOM-GDO (Gestão Documental)

**Domínio:** DOM-GDO — Gestão Documental
**Data:** 2026-09-06 16:41:20
**Duração total:** 1.61s
**Base URL:** http://localhost:8010/api/v1/gdo
**Resultado:** SUCESSO

## Resultados por endpoint

| Método | Endpoint | Requisições | OK | Erros | Lat. média (ms) | p95 (ms) | Máx (ms) | Throughput (req/s) |
|--------|----------|-------------|----|-------|-----------------|----------|----------|--------------------|
| GET | /tipos-documentais | 50 | 50 | 0 | 32.21 | 50.05 | 53.21 | 277.47 |
| GET | /classificacoes | 50 | 50 | 0 | 36.08 | 69.09 | 71.63 | 247.22 |
| GET | /temporalidades/TEMP-001 | 50 | 50 | 0 | 37.43 | 62.86 | 65.66 | 243.85 |
| POST | /documentos | 1 | 1 | 0 | 14.27 | 14.27 | 14.27 | 69.5 |
| POST | /documentos | 1 | 1 | 0 | 15.94 | 15.94 | 15.94 | 62.31 |
| POST | /documentos | 1 | 1 | 0 | 14.1 | 14.1 | 14.1 | 70.13 |
| POST | /documentos | 1 | 1 | 0 | 13.33 | 13.33 | 13.33 | 74.56 |
| POST | /documentos | 1 | 1 | 0 | 24.58 | 24.58 | 24.58 | 40.42 |
| POST | /documentos | 1 | 1 | 0 | 13.44 | 13.44 | 13.44 | 73.91 |
| POST | /documentos | 1 | 1 | 0 | 20.94 | 20.94 | 20.94 | 47.48 |
| POST | /documentos | 1 | 1 | 0 | 12.8 | 12.8 | 12.8 | 76.74 |
| POST | /documentos | 1 | 1 | 0 | 13.03 | 13.03 | 13.03 | 76.13 |
| POST | /documentos | 1 | 1 | 0 | 11.73 | 11.73 | 11.73 | 84.45 |
| POST | /documentos | 1 | 1 | 0 | 12.08 | 12.08 | 12.08 | 82.19 |
| POST | /documentos | 1 | 1 | 0 | 12.77 | 12.77 | 12.77 | 77.56 |
| POST | /documentos | 1 | 1 | 0 | 12.29 | 12.29 | 12.29 | 80.6 |
| POST | /documentos | 1 | 1 | 0 | 24.66 | 24.66 | 24.66 | 40.31 |
| POST | /documentos | 1 | 1 | 0 | 13.11 | 13.11 | 13.11 | 75.67 |
| POST | /documentos | 1 | 1 | 0 | 12.49 | 12.49 | 12.49 | 79.47 |
| POST | /documentos | 1 | 1 | 0 | 11.75 | 11.75 | 11.75 | 84.39 |
| POST | /documentos | 1 | 1 | 0 | 12.16 | 12.16 | 12.16 | 81.49 |
| POST | /documentos | 1 | 1 | 0 | 12.42 | 12.42 | 12.42 | 79.89 |
| POST | /documentos | 1 | 1 | 0 | 13.17 | 13.17 | 13.17 | 75.28 |

**Latência média geral:** 17.25ms
**Total de testes:** 23 | **Falhas:** 0

## Critérios de aceitação (018-Plano-de-Testes)

- SLA GET p95 < 500ms: CUMPRIDO
- Erros HTTP: 0

---

**Documento:** 2026-09-06-teste-carga-gdo.md
**Última atualização:** 2026-09-06
**Responsável:** Equipe SIGMUN
**Status:** Concluído
