# Semana 9 — Tarefa 2 (Sem9-T2)

**Turma:** 166/186  
**Período:** 2026-1  
**Professor:** Ritomar Torquato  
**Instituição:** IFPI  
**Tema:** Condicionais Aninhadas

---

## Questão 1 — Dia da semana (`q1.py`)

**Enunciado:** Leia um número de 1 a 7 e exiba o dia da semana correspondente. Qualquer outro valor exibe "valor inválido".

**Como funciona:**

1. A função `entrada_dados()` lê um número inteiro correspondente ao dia da semana.
2. A função `dia_semana(numero)` usa condicionais `if/elif/else` para mapear:
   - `1` → domingo, `2` → segunda-feira, `3` → terça-feira, `4` → quarta-feira, `5` → quinta-feira, `6` → sexta-feira, `7` → sábado.
   - Qualquer outro valor → `"valor inválido"`.
3. O dia é exibido com `print()`.

**Exemplo:**
```
Entrada: 4
Saída: Dia da semana: quarta-feira
```

---

## Questão 2 — Número por extenso (`q2.py`)

**Enunciado:** Leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades, respeitando singular/plural, vírgula, "e" e ponto final.

**Como funciona:**

1. A função `entrada_dados()` lê um número inteiro (< 1000).
2. A função `por_extenso(n)` decompõe o número:
   - `c = n // 100` → centenas.
   - `d = (n % 100) // 10` → dezenas.
   - `u = n % 10` → unidades.
3. Para cada parte > 0, adiciona o nome por extenso com singular ou plural (ex.: "uma centena" vs "cinco centenas").
4. Monta a frase usando vírgula entre as duas primeiras partes e "e" antes da última, finalizando com ponto.

**Exemplo:**
```
Entrada: 521
Saída: O número por extenso é: cinco centenas, duas dezenas e uma unidade.

Entrada: 107
Saída: O número por extenso é: uma centena e sete unidades.

Entrada: 80
Saída: O número por extenso é: oito dezenas.
```

---

## Questão 3 — Validação de data (`q3.py`)

**Enunciado:** Leia uma data no formato DDMMAAAA e informe se é válida. Sem usar bibliotecas de datas, considerando anos bissextos.

**Como funciona:**

1. A função `entrada_dados()` lê a data como string de 8 caracteres.
2. A função `validar_data(data)` executa:
   - Verifica se a string tem exatamente 8 caracteres.
   - Extrai dia (`dd`), mês (`mm`) e ano (`aaaa`) usando fatiamento de string.
   - Valida o mês (1 a 12).
   - Calcula se o ano é bissexto: divisível por 4 mas não por 100, **ou** divisível por 400.
   - Define os dias máximos por mês (fevereiro = 29 se bissexto, 28 caso contrário).
   - Valida se o dia está dentro do intervalo do mês.
3. Exibe "Data válida" ou "Data inválida".

**Exemplo:**
```
Entrada: 29022024
Saída: Data válida (2024 é bissexto)

Entrada: 29022023
Saída: Data inválida (2023 não é bissexto)
```

---

## Questão 4 — Sacolão de frutas (`q4.py`)

**Enunciado:** Calcule o valor a pagar por morangos e maçãs com preços diferenciados por faixa de peso, aplicando 10% de desconto se o total ultrapassar 8 kg ou R$ 25,00.

**Tabela de preços:**

| Fruta   | Até 5 Kg  | Acima de 5 Kg |
|---------|-----------|---------------|
| Morango | R$ 2,50   | R$ 2,20       |
| Maçã    | R$ 1,80   | R$ 1,50       |

**Como funciona:**

1. A função `entrada_dados()` lê as quantidades em kg de morango e maçã.
2. A função `calcular_valor(kg_morango, kg_maca)`:
   - Aplica o preço por kg conforme a faixa (≤ 5 kg ou > 5 kg) para cada fruta.
   - Soma os valores e os pesos totais.
   - Se `total_kg > 8` **ou** `total > 25` → aplica desconto de 10% (`total * 0.90`).
3. Exibe o valor final a pagar.

**Exemplo:**
```
Entrada: 3 (kg morango), 6 (kg maçã)
Morango: 3 × 2.50 = 7.50
Maçã: 6 × 1.50 = 9.00
Total: 16.50 | Total kg: 9 (> 8, desconto 10%)
Saída: Valor a pagar: R$ 14.85
```

---

## Questão 5 — Classificação criminal (`q5.py`)

**Enunciado:** Faça 5 perguntas (S/N) sobre um crime e classifique a pessoa conforme o número de respostas positivas.

**Perguntas:**
- a) Telefonou para a vítima?
- b) Esteve no local do crime?
- c) Mora perto da vítima?
- d) Devia para a vítima?
- e) Já trabalhou com a vítima?

**Classificação:**
| Respostas "S" | Classificação |
|---------------|---------------|
| 0 ou 1        | Inocente      |
| 2             | Suspeito      |
| 3 ou 4        | Cúmplice      |
| 5             | Assassino     |

**Como funciona:**

1. A função `entrada_dados()` exibe cada pergunta e coleta S ou N para cada uma, armazenando em uma lista.
2. A função `classificar(respostas)` conta quantas respostas são `"S"` (ignorando maiúsculas) usando `sum()` com expressão geradora.
3. Compara a contagem com as faixas e retorna a classificação correspondente.
4. A classificação é exibida.

**Exemplo:**
```
Respostas: S, N, S, S, N (3 positivas)
Saída: Classificação: Cúmplice
```
