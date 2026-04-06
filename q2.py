# Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:

# 521 = cinco centenas, duas dezenas e uma unidade.
# 107 = uma centena e sete unidades.
# 80 = oito dezenas.
#entrada de dados
def entrada_dados():
    n = int(input("Informe um número inteiro menor que 1000: "))  # lê o número inteiro menor que 1000
    return n

#processamento de dados
def por_extenso(n):
    # nomes femininos para os dígitos de 1 a 9
    nomes = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    c = n // 100           # extrai as centenas
    d = (n % 100) // 10    # extrai as dezenas
    u = n % 10             # extrai as unidades

    partes = []
    if c > 0:
        # adiciona centena(s) no singular ou plural
        partes.append(f"{nomes[c]} {'centena' if c == 1 else 'centenas'}")
    if d > 0:
        # adiciona dezena(s) no singular ou plural
        partes.append(f"{nomes[d]} {'dezena' if d == 1 else 'dezenas'}")
    if u > 0:
        # adiciona unidade(s) no singular ou plural
        partes.append(f"{nomes[u]} {'unidade' if u == 1 else 'unidades'}")

    # monta a frase com vírgula entre partes e "e" antes da última
    if len(partes) == 1:
        return partes[0] + "."
    elif len(partes) == 2:
        return partes[0] + " e " + partes[1] + "."
    else:
        return partes[0] + ", " + partes[1] + " e " + partes[2] + "."

#função principal
def main():
    n = entrada_dados()           # obtém o número
    resultado = por_extenso(n)    # converte para extenso
    print(f"O número por extenso é: {resultado}")  # exibe o resultado
if __name__ == "__main__":    main()