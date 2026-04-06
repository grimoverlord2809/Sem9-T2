<div align="center">

# 📘 Semana 9 — Tarefa 2 (Sem9-T2)

### Condicionais Aninhadas

| Informação | Detalhe |
|:---:|:---:|
| **Turma** | 166/186 |
| **Período** | 2026-1 |
| **Professor** | Ritomar Torquato |
| **Instituição** | IFPI |
| **Linguagem** | Python 3 |

</div>

---

## 📂 Estrutura do Projeto

```
t2/
├── q1.py   → Dia da semana
├── q2.py   → Número por extenso
├── q3.py   → Validação de data
├── q4.py   → Sacolão de frutas
├── q5.py   → Classificação criminal
└── README.md
```

---

## 🔹 Questão 1 — Dia da semana (`q1.py`)

**Enunciado:** Leia um número de 1 a 7 e exiba o dia da semana correspondente. Qualquer outro valor exibe "valor inválido".

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    numero = int(input("Informe o número correspondente ao dia da semana: "))
    return numero

def dia_semana(numero):
    if numero == 1:
        return "domingo"
    elif numero == 2:
        return "segunda-feira"
    elif numero == 3:
        return "terça-feira"
    elif numero == 4:
        return "quarta-feira"
    elif numero == 5:
        return "quinta-feira"
    elif numero == 6:
        return "sexta-feira"
    elif numero == 7:
        return "sábado"
    else:
        return "valor inválido"

def main():
    numero = entrada_dados()
    resultado = dia_semana(numero)
    print(f"Dia da semana: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê um número inteiro de 1 a 7 |
| **Processamento** | Usa cadeia `if/elif/else` para mapear número → dia |
| **Saída** | Exibe o nome do dia ou "valor inválido" |

**Mapeamento dos dias:**

| Número | Dia |
|:---:|:---:|
| 1 | domingo |
| 2 | segunda-feira |
| 3 | terça-feira |
| 4 | quarta-feira |
| 5 | quinta-feira |
| 6 | sexta-feira |
| 7 | sábado |
| outro | valor inválido |

**▶️ Exemplo de execução:**
```
Informe o número correspondente ao dia da semana: 4
Dia da semana: quarta-feira
```

---

## 🔹 Questão 2 — Número por extenso (`q2.py`)

**Enunciado:** Leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades, respeitando singular/plural, vírgula, "e" e ponto final.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    n = int(input("Informe um número inteiro menor que 1000: "))
    return n

def por_extenso(n):
    nomes = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    partes = []
    if c > 0:
        partes.append(f"{nomes[c]} {'centena' if c == 1 else 'centenas'}")
    if d > 0:
        partes.append(f"{nomes[d]} {'dezena' if d == 1 else 'dezenas'}")
    if u > 0:
        partes.append(f"{nomes[u]} {'unidade' if u == 1 else 'unidades'}")

    if len(partes) == 1:
        return partes[0] + "."
    elif len(partes) == 2:
        return partes[0] + " e " + partes[1] + "."
    else:
        return partes[0] + ", " + partes[1] + " e " + partes[2] + "."

def main():
    n = entrada_dados()
    resultado = por_extenso(n)
    print(f"O número por extenso é: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê um inteiro menor que 1000 |
| **Decomposição** | Separa centenas (`n // 100`), dezenas (`(n % 100) // 10`) e unidades (`n % 10`) |
| **Extenso** | Converte cada dígito para nome feminino usando lista `nomes[]` |
| **Formatação** | Aplica singular/plural e conectores (vírgula, "e", ponto final) |

**Regras de formatação:**

```
1 parte  → "oito dezenas."
2 partes → "uma centena e sete unidades."
3 partes → "cinco centenas, duas dezenas e uma unidade."
```

**▶️ Exemplos de execução:**
```
Informe um número inteiro menor que 1000: 521
O número por extenso é: cinco centenas, duas dezenas e uma unidade.
```
```
Informe um número inteiro menor que 1000: 107
O número por extenso é: uma centena e sete unidades.
```
```
Informe um número inteiro menor que 1000: 80
O número por extenso é: oito dezenas.
```

---

## 🔹 Questão 3 — Validação de data (`q3.py`)

**Enunciado:** Leia uma data no formato DDMMAAAA e informe se é válida. Sem usar bibliotecas de datas, considerando anos bissextos.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    data = input("Informe a data no formato DDMMAAAA: ")
    return data

def validar_data(data):
    if len(data) != 8:
        return False

    dd   = int(data[0:2])
    mm   = int(data[2:4])
    aaaa = int(data[4:8])

    if mm < 1 or mm > 12:
        return False

    bissexto = (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0)

    dias_por_mes = [0, 31, 29 if bissexto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dd < 1 or dd > dias_por_mes[mm]:
        return False

    return True

def main():
    data = entrada_dados()
    resultado = validar_data(data)
    if resultado:
        print("Data válida")
    else:
        print("Data inválida")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê a data como string de 8 dígitos (`DDMMAAAA`) |
| **Extração** | Fatia a string: `data[0:2]` → dia, `data[2:4]` → mês, `data[4:8]` → ano |
| **Validação do mês** | Verifica se está entre 1 e 12 |
| **Ano bissexto** | `(ano % 4 == 0 e ano % 100 != 0) ou (ano % 400 == 0)` |
| **Validação do dia** | Compara com os dias máximos do mês (lista `dias_por_mes`) |

**Regra de ano bissexto:**

```
Bissexto = (divisível por 4 E não divisível por 100) OU (divisível por 400)

Exemplos:
  2024 → 2024 % 4 == 0 e 2024 % 100 != 0  → Bissexto ✅
  1900 → 1900 % 4 == 0 mas 1900 % 100 == 0 e 1900 % 400 != 0 → Não bissexto ❌
  2000 → 2000 % 400 == 0 → Bissexto ✅
```

**Dias por mês:**

| Mês | Jan | Fev | Mar | Abr | Mai | Jun | Jul | Ago | Set | Out | Nov | Dez |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Dias** | 31 | 28/29 | 31 | 30 | 31 | 30 | 31 | 31 | 30 | 31 | 30 | 31 |

**▶️ Exemplos de execução:**
```
Informe a data no formato DDMMAAAA: 29022024
Data válida
```
```
Informe a data no formato DDMMAAAA: 29022023
Data inválida
```

---

## 🔹 Questão 4 — Sacolão de frutas (`q4.py`)

**Enunciado:** Calcule o valor a pagar por morangos e maçãs com preços diferenciados por faixa de peso, aplicando 10% de desconto se o total ultrapassar 8 kg ou R$ 25,00.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    kg_morango = float(input("Quantidade de morango (kg): "))
    kg_maca    = float(input("Quantidade de maçã (kg): "))
    return kg_morango, kg_maca

def calcular_valor(kg_morango, kg_maca):
    if kg_morango <= 5:
        valor_morango = kg_morango * 2.50
    else:
        valor_morango = kg_morango * 2.20

    if kg_maca <= 5:
        valor_maca = kg_maca * 1.80
    else:
        valor_maca = kg_maca * 1.50

    total    = valor_morango + valor_maca
    total_kg = kg_morango + kg_maca

    if total_kg > 8 or total > 25:
        total = total * 0.90

    return total

def main():
    kg_morango, kg_maca = entrada_dados()
    resultado = calcular_valor(kg_morango, kg_maca)
    print(f"Valor a pagar: R$ {round(resultado, 2)}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê quantidade de morango e maçã em kg |
| **Preço por faixa** | Aplica preço conforme peso ≤ 5 kg ou > 5 kg |
| **Desconto** | Se total de kg > 8 **ou** valor > R$ 25 → desconto de 10% |
| **Saída** | Exibe o valor final a pagar |

**Tabela de preços:**

| Fruta | ≤ 5 Kg | > 5 Kg |
|:---:|:---:|:---:|
| 🍓 Morango | R$ 2,50/kg | R$ 2,20/kg |
| 🍎 Maçã | R$ 1,80/kg | R$ 1,50/kg |

**Regra de desconto:**

```
Se total_kg > 8  OU  total_valor > R$ 25,00:
    total_final = total × 0.90   (desconto de 10%)
```

**▶️ Exemplo de execução:**
```
Quantidade de morango (kg): 3
Quantidade de maçã (kg): 6

Morango: 3 × R$ 2,50 = R$ 7,50    (≤ 5 kg)
Maçã:    6 × R$ 1,50 = R$ 9,00    (> 5 kg)
Total:   R$ 16,50
Total kg: 9 kg (> 8 → desconto 10%)
Final:   R$ 16,50 × 0,90 = R$ 14,85

Valor a pagar: R$ 14.85
```

---

## 🔹 Questão 5 — Classificação criminal (`q5.py`)

**Enunciado:** Faça 5 perguntas (S/N) sobre um crime e classifique a pessoa conforme o número de respostas positivas.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    print("Responda com S (sim) ou N (não):")
    a = input("Telefonou para a vítima? ").strip()
    b = input("Esteve no local do crime? ").strip()
    c = input("Mora perto da vítima? ").strip()
    d = input("Devia para a vítima? ").strip()
    e = input("Já trabalhou com a vítima? ").strip()
    return [a, b, c, d, e]

def classificar(respostas):
    positivas = sum(1 for r in respostas if r.upper() == 'S')

    if positivas == 5:
        return "Assassino"
    elif positivas >= 3:
        return "Cúmplice"
    elif positivas == 2:
        return "Suspeito"
    else:
        return "Inocente"

def main():
    respostas = entrada_dados()
    resultado = classificar(respostas)
    print(f"Classificação: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Coleta 5 respostas (S/N) sobre o crime |
| **Contagem** | Conta respostas "S" usando `sum()` com expressão geradora |
| **Classificação** | Aplica a faixa correspondente ao número de positivas |
| **Saída** | Exibe a classificação |

**As 5 perguntas:**

| # | Pergunta |
|:---:|---|
| a | Telefonou para a vítima? |
| b | Esteve no local do crime? |
| c | Mora perto da vítima? |
| d | Devia para a vítima? |
| e | Já trabalhou com a vítima? |

**Tabela de classificação:**

| Respostas "S" | Classificação |
|:---:|:---:|
| 0 ou 1 | 🟢 Inocente |
| 2 | 🟡 Suspeito |
| 3 ou 4 | 🟠 Cúmplice |
| 5 | 🔴 Assassino |

**Lógica da contagem:**

```python
positivas = sum(1 for r in respostas if r.upper() == 'S')
# Percorre cada resposta, converte para maiúscula e conta quantas são "S"
```

**▶️ Exemplo de execução:**
```
Responda com S (sim) ou N (não):
Telefonou para a vítima? S
Esteve no local do crime? N
Mora perto da vítima? S
Devia para a vítima? S
Já trabalhou com a vítima? N
Classificação: Cúmplice
```

> 3 respostas positivas → **Cúmplice**

---

<div align="center">

**IFPI — Instituto Federal do Piauí** • Período 2026-1 • Prof. Ritomar Torquato

</div>
