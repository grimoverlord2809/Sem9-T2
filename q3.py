# Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.

# OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.

#entrada de dados
def entrada_dados():
    data = input("Informe a data no formato DDMMAAAA: ")  # lê a data no formato DDMMAAAA (8 dígitos)
    return data

#processamento de dados
def validar_data(data):
    if len(data) != 8:          # verifica se a string tem exatamente 8 caracteres
        return False

    dd   = int(data[0:2])       # extrai o dia
    mm   = int(data[2:4])       # extrai o mês
    aaaa = int(data[4:8])       # extrai o ano

    if mm < 1 or mm > 12:       # valida o intervalo do mês (1 a 12)
        return False

    # verifica se o ano é bissexto (divisível por 4 mas não por 100, ou divisível por 400)
    bissexto = (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0)

    # dias máximos por mês (índice 0 ignorado)
    dias_por_mes = [0, 31, 29 if bissexto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dd < 1 or dd > dias_por_mes[mm]:  # valida o dia dentro do mês
        return False

    return True

#função principal
def main():
    data = entrada_dados()          # obtém a data digitada
    resultado = validar_data(data)  # valida a data
    if resultado:
        print("Data válida")                   # exibe o resultado
    else:
        print("Data inválida")
if __name__ == "__main__":    main()