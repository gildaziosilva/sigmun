# 003 – Mapa de Processos – Cadastro Imobiliário

#### Mapa de Processos – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-003

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato descreve os processos de negócio do domínio de Cadastro Imobiliário,
da intenção do ator à alteração do estado, evidenciando entradas, saídas e
regras aplicadas.

---

# 2. Convenções

* **Gatilho:** evento ou condição que dispara o processo.
* **Objetivo:** resultado pretendido pelo processo.
* **Passos:** sequência lógica; as regras de negócio aplicadas aparecem entre
  parênteses na etapa correspondente.

---

# 3. Visão Geral

| ID | Processo | Gatilho | Objetivo |
| --- | | --- | | --- | |
| PRO-IMO-001 | Cadastrar lote | Levantamento predial, loteamento novo ou regularização cadastral. | Registrar a unidade imobiliária com sua inscrição definitiva. |
| PRO-IMO-002 | Vincular titularidade | Aquisição de título, escritura, contrato ou atualização de cadastro. | Manter a titularidade do imóvel com um único titular principal. |
| PRO-IMO-003 | Alterar situação do imóvel | Obra, ocupação, demolição ou regularização cadastral. | Manter a situação cadastral coerente com a realidade do imóvel. |
| PRO-IMO-004 | Avaliar o valor venal | Início do exercício fiscal ou revisão cadastral do imóvel. | Apurar o valor venal e o lançamento estimado do imóvel. |
| PRO-IMO-005 | Consultar cadastro e contestar valor | Solicitação do cidadão ou de órgão de controle. | Prestar esclarecimento sobre a inscrição, a titularidade e o valor venal. |
| PRO-IMO-006 | Georreferenciar o lote | Levantamento topográfico ou certificação pelo registro do imóvel. | Vincular a geometria fundiária ao cadastro do lote. |


---

# 4. Detalhamento

### PRO-IMO-001 — Cadastrar lote

**Gatilho:** Levantamento predial, loteamento novo ou regularização cadastral.

**Objetivo:** Registrar a unidade imobiliária com sua inscrição definitiva.

**Entradas:** Inscrição imobiliária; logradouro; bairro; número; tipo; áreas; ano de construção

**Saídas:** Imóvel cadastrado

**Regras aplicadas:** RN-IMO-001, RN-IMO-002, RN-IMO-003

**Passos:**

1. S
2. e
3. l
4. e
5. c
6. i
7. o
8. n
9. a
10. r
11.  
12. o
13.  
14. l
15. o
16. g
17. r
18. a
19. d
20. o
21. u
22. r
23. o
24.  
25. e
26.  
27. o
28.  
29. b
30. a
31. i
32. r
33. r
34. o
35.  
36. d
37. e
38.  
39. v
40. i
41. n
42. c
43. u
44. l
45. a
46. ç
47. ã
48. o
49.  
50. (
51. R
52. N
53. -
54. I
55. M
56. O
57. -
58. 0
59. 0
60. 2
61. )
62. ;
63.  
64. v
65. e
66. r
67. i
68. f
69. i
70. c
71. a
72. r
73.  
74. a
75.  
76. u
77. n
78. i
79. c
80. i
81. d
82. a
83. d
84. e
85.  
86. d
87. a
88.  
89. i
90. n
91. s
92. c
93. r
94. i
95. ç
96. ã
97. o
98.  
99. (
100. R
101. N
102. -
103. I
104. M
105. O
106. -
107. 0
108. 0
109. 1
110. )
111. ;
112.  
113. i
114. n
115. f
116. o
117. r
118. m
119. a
120. r
121.  
122. a
123. s
124.  
125. á
126. r
127. e
128. a
129. s
130.  
131. (
132. R
133. N
134. -
135. I
136. M
137. O
138. -
139. 0
140. 0
141. 3
142. )
143. ;
144.  
145. g
146. r
147. a
148. v
149. a
150. r
151.  
152. c
153. o
154. m
155.  
156. s
157. i
158. t
159. u
160. a
161. ç
162. ã
163. o
164.  
165. a
166. t
167. i
168. v
169. a
170. .

---
### PRO-IMO-002 — Vincular titularidade

**Gatilho:** Aquisição de título, escritura, contrato ou atualização de cadastro.

**Objetivo:** Manter a titularidade do imóvel com um único titular principal.

**Entradas:** Imóvel; nome; CPF ou CNPJ; vínculo; indicador de principal

**Saídas:** Vínculo de propriedade registrado

**Regras aplicadas:** RN-IMO-006

**Passos:**

1. S
2. e
3. l
4. e
5. c
6. i
7. o
8. n
9. a
10. r
11.  
12. o
13.  
14. i
15. m
16. ó
17. v
18. e
19. l
20. ;
21.  
22. i
23. n
24. f
25. o
26. r
27. m
28. a
29. r
30.  
31. o
32. s
33.  
34. d
35. a
36. d
37. o
38. s
39.  
40. d
41. o
42.  
43. p
44. r
45. o
46. p
47. r
48. i
49. e
50. t
51. á
52. r
53. i
54. o
55. ;
56.  
57. o
58.  
59. s
60. i
61. s
62. t
63. e
64. m
65. a
66.  
67. i
68. m
69. p
70. e
71. d
72. e
73.  
74. t
75. i
76. t
77. u
78. l
79. a
80. r
81.  
82. p
83. r
84. i
85. n
86. c
87. i
88. p
89. a
90. l
91.  
92. d
93. u
94. p
95. l
96. i
97. c
98. a
99. d
100. o
101.  
102. e
103.  
104. v
105. í
106. n
107. c
108. u
109. l
110. o
111.  
112. r
113. e
114. p
115. e
116. t
117. i
118. d
119. o
120.  
121. (
122. R
123. N
124. -
125. I
126. M
127. O
128. -
129. 0
130. 0
131. 6
132. )
133. ;
134.  
135. g
136. r
137. a
138. v
139. a
140. r
141.  
142. o
143.  
144. v
145. í
146. n
147. c
148. u
149. l
150. o
151. .

---
### PRO-IMO-003 — Alterar situação do imóvel

**Gatilho:** Obra, ocupação, demolição ou regularização cadastral.

**Objetivo:** Manter a situação cadastral coerente com a realidade do imóvel.

**Entradas:** Imóvel; nova situação

**Saídas:** Imóvel com situação alterada

**Regras aplicadas:** RN-IMO-004

**Passos:**

1. S
2. o
3. l
4. i
5. c
6. i
7. t
8. a
9. r
10.  
11. a
12.  
13. n
14. o
15. v
16. a
17.  
18. s
19. i
20. t
21. u
22. a
23. ç
24. ã
25. o
26. ;
27.  
28. o
29.  
30. s
31. i
32. s
33. t
34. e
35. m
36. a
37.  
38. v
39. a
40. l
41. i
42. d
43. a
44.  
45. a
46.  
47. t
48. r
49. a
50. n
51. s
52. i
53. ç
54. ã
55. o
56.  
57. c
58. o
59. n
60. t
61. r
62. a
63.  
64. a
65.  
66. m
67. á
68. q
69. u
70. i
71. n
72. a
73.  
74. d
75. e
76.  
77. e
78. s
79. t
80. a
81. d
82. o
83. s
84.  
85. (
86. R
87. N
88. -
89. I
90. M
91. O
92. -
93. 0
94. 0
95. 4
96. )
97. ;
98.  
99. t
100. r
101. a
102. n
103. s
104. i
105. ç
106. õ
107. e
108. s
109.  
110. i
111. n
112. v
113. á
114. l
115. i
116. d
117. a
118. s
119.  
120. s
121. ã
122. o
123.  
124. r
125. e
126. c
127. u
128. s
129. a
130. d
131. a
132. s
133.  
134. c
135. o
136. m
137.  
138. H
139. T
140. T
141. P
142.  
143. 4
144. 0
145. 9
146. .

---
### PRO-IMO-004 — Avaliar o valor venal

**Gatilho:** Início do exercício fiscal ou revisão cadastral do imóvel.

**Objetivo:** Apurar o valor venal e o lançamento estimado do imóvel.

**Entradas:** Imóvel; exercício; valor do terreno por m²; valor da construção por m²; alíquota

**Saídas:** Avaliação concluída com valor venal

**Regras aplicadas:** RN-IMO-005

**Passos:**

1. C
2. o
3. n
4. s
5. u
6. l
7. t
8. a
9. r
10.  
11. a
12.  
13. p
14. l
15. a
16. n
17. t
18. a
19.  
20. v
21. i
22. g
23. e
24. n
25. t
26. e
27.  
28. n
29. o
30.  
31. D
32. O
33. M
34. -
35. T
36. E
37. L
38. ;
39.  
40. c
41. a
42. l
43. c
44. u
45. l
46. a
47. r
48.  
49. t
50. e
51. r
52. r
53. e
54. n
55. o
56. ,
57.  
58. c
59. o
60. n
61. s
62. t
63. r
64. u
65. ç
66. ã
67. o
68. ,
69.  
70. v
71. a
72. l
73. o
74. r
75.  
76. v
77. e
78. n
79. a
80. l
81.  
82. e
83.  
84. l
85. a
86. n
87. ç
88. a
89. m
90. e
91. n
92. t
93. o
94.  
95. (
96. R
97. N
98. -
99. I
100. M
101. O
102. -
103. 0
104. 0
105. 5
106. )
107. ;
108.  
109. i
110. m
111. p
112. e
113. d
114. i
115. r
116.  
117. r
118. e
119. a
120. v
121. a
122. l
123. i
124. a
125. ç
126. ã
127. o
128.  
129. d
130. e
131.  
132. e
133. x
134. e
135. r
136. c
137. í
138. c
139. i
140. o
141.  
142. c
143. o
144. n
145. c
146. l
147. u
148. í
149. d
150. o
151. ;
152.  
153. r
154. e
155. g
156. i
157. s
158. t
159. r
160. a
161. r
162.  
163. e
164.  
165. c
166. o
167. n
168. c
169. l
170. u
171. i
172. r
173. .

---
### PRO-IMO-005 — Consultar cadastro e contestar valor

**Gatilho:** Solicitação do cidadão ou de órgão de controle.

**Objetivo:** Prestar esclarecimento sobre a inscrição, a titularidade e o valor venal.

**Entradas:** Inscrição imobiliária

**Saídas:** Dados cadastrais e avaliação do exercício

**Regras aplicadas:** RN-IMO-001, RN-IMO-005

**Passos:**

1. C
2. o
3. n
4. s
5. u
6. l
7. t
8. a
9. r
10.  
11. o
12.  
13. i
14. m
15. ó
16. v
17. e
18. l
19.  
20. p
21. e
22. l
23. a
24.  
25. i
26. n
27. s
28. c
29. r
30. i
31. ç
32. ã
33. o
34. ;
35.  
36. e
37. x
38. i
39. b
40. i
41. r
42.  
43. s
44. i
45. t
46. u
47. a
48. ç
49. ã
50. o
51. ,
52.  
53. á
54. r
55. e
56. a
57. s
58. ,
59.  
60. t
61. i
62. t
63. u
64. l
65. a
66. r
67. i
68. d
69. a
70. d
71. e
72.  
73. e
74.  
75. a
76. v
77. a
78. l
79. i
80. a
81. ç
82. õ
83. e
84. s
85. .

---
### PRO-IMO-006 — Georreferenciar o lote

**Gatilho:** Levantamento topográfico ou certificação pelo registro do imóvel.

**Objetivo:** Vincular a geometria fundiária ao cadastro do lote.

**Entradas:** Imóvel; tipo de geometria; vértices; datum; precisão

**Saídas:** Geometria do lote registrada

**Regras aplicadas:** RN-IMO-007

**Passos:**

1. S
2. e
3. l
4. e
5. c
6. i
7. o
8. n
9. a
10. r
11.  
12. o
13.  
14. i
15. m
16. ó
17. v
18. e
19. l
20. ;
21.  
22. i
23. n
24. f
25. o
26. r
27. m
28. a
29. r
30.  
31. g
32. e
33. o
34. m
35. e
36. t
37. r
38. i
39. a
40. ,
41.  
42. v
43. é
44. r
45. t
46. i
47. c
48. e
49. s
50.  
51. e
52.  
53. d
54. a
55. t
56. u
57. m
58.  
59. (
60. R
61. N
62. -
63. I
64. M
65. O
66. -
67. 0
68. 0
69. 7
70. )
71. ;
72.  
73. o
74.  
75. s
76. i
77. s
78. t
79. e
80. m
81. a
82.  
83. v
84. a
85. l
86. i
87. d
88. a
89.  
90. e
91.  
92. s
93. u
94. b
95. s
96. t
97. i
98. t
99. u
100. i
101.  
102. a
103.  
104. g
105. e
106. o
107. m
108. e
109. t
110. r
111. i
112. a
113.  
114. v
115. i
116. g
117. e
118. n
119. t
120. e
121. .

---

# 5. Processos por Capacidade

| Processo | Capacidades | Regras |
| --- | | --- | |
| PRO-IMO-001 — Cadastrar lote | CAP-IMO-001 | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| PRO-IMO-002 — Vincular titularidade | CAP-IMO-002 | RN-IMO-006 |
| PRO-IMO-003 — Alterar situação do imóvel | CAP-IMO-003 | RN-IMO-004 |
| PRO-IMO-004 — Avaliar o valor venal | CAP-IMO-004 | RN-IMO-005 |
| PRO-IMO-005 — Consultar cadastro e contestar valor | CAP-IMO-005 | RN-IMO-001, RN-IMO-005 |
| PRO-IMO-006 — Georreferenciar o lote | CAP-IMO-006 | RN-IMO-007 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 003-Mapa-de-Processos-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
