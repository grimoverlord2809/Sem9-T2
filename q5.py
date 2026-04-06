# Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# a) "Telefonou para a vítima ?"

# b) "Esteve no local do crime ?"

# c) "Mora perto da vítima ?"

# d) "Devia para a vítima ?"

# e) "Já trabalhou com a vítima ?"

# Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
#entrada de dados
def entrada_dados():
    print("Responda com S (sim) ou N (não):")
    a = input("Telefonou para a vítima? ").strip()  # resposta: "Telefonou para a vítima?"
    b = input("Esteve no local do crime? ").strip()  # resposta: "Esteve no local do crime?"
    c = input("Mora perto da vítima? ").strip()  # resposta: "Mora perto da vítima?"
    d = input("Devia para a vítima? ").strip()  # resposta: "Devia para a vítima?"
    e = input("Já trabalhou com a vítima? ").strip()  # resposta: "Já trabalhou com a vítima?"
    return [a, b, c, d, e]

#processamento de dados
def classificar(respostas):
    # conta quantas respostas foram "S" (sim), ignorando maiúsculas/minúsculas
    positivas = sum(1 for r in respostas if r.upper() == 'S')

    if positivas == 5:          # todas positivas = Assassino
        return "Assassino"
    elif positivas >= 3:        # 3 ou 4 positivas = Cúmplice
        return "Cúmplice"
    elif positivas == 2:        # exatamente 2 positivas = Suspeito
        return "Suspeito"
    else:                       # 0 ou 1 positiva = Inocente
        return "Inocente"

#função principal
def main():
    respostas = entrada_dados()     # coleta as 5 respostas
    resultado = classificar(respostas)  # determina a classificação
    print(f"Classificação: {resultado}")  # exibe a classificação
if __name__ == "__main__":    main()