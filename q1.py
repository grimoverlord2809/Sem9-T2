# Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.
#entrada de dados
def entrada_dados():
    numero = int(input(" Informe o número correspondente ao dia da semana: "))  # lê o número correspondente ao dia da semana
    return numero

#processamento de dados
def dia_semana(numero):
    if numero == 1:
        return "domingo"          # 1 = domingo
    elif numero == 2:
        return "segunda-feira"    # 2 = segunda-feira
    elif numero == 3:
        return "terça-feira"      # 3 = terça-feira
    elif numero == 4:
        return "quarta-feira"     # 4 = quarta-feira
    elif numero == 5:
        return "quinta-feira"     # 5 = quinta-feira
    elif numero == 6:
        return "sexta-feira"      # 6 = sexta-feira
    elif numero == 7:
        return "sábado"           # 7 = sábado
    else:
        return "valor inválido"   # número fora do intervalo 1-7

#função principal
def main():
    numero = entrada_dados()       # obtém o número digitado
    resultado = dia_semana(numero) # determina o dia da semana
    print(f"Dia da semana: {resultado}")  # exibe o resultado
if __name__ == "__main__":    main()