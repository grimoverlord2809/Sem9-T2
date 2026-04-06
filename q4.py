# Um sacolão está vendendo frutas com a seguinte tabela de preços:

# Item	Até 5Kg	Acima de 5Kg
# Morango	R$ 2,50	R$ 2,20
# Maça	R$ 1,80	R$ 1,50
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#entrada de dados
def entrada_dados():
    kg_morango = float(input("Quantidade de morango (kg): "))  # lê a quantidade de morango em kg
    kg_maca    = float(input("Quantidade de maçã (kg): "))  # lê a quantidade de maçã em kg
    return kg_morango, kg_maca

#processamento de dados
def calcular_valor(kg_morango, kg_maca):
    # calcula o valor do morango conforme a faixa de peso
    if kg_morango <= 5:
        valor_morango = kg_morango * 2.50   # preço até 5 kg
    else:
        valor_morango = kg_morango * 2.20   # preço acima de 5 kg

    # calcula o valor da maçã conforme a faixa de peso
    if kg_maca <= 5:
        valor_maca = kg_maca * 1.80         # preço até 5 kg
    else:
        valor_maca = kg_maca * 1.50         # preço acima de 5 kg

    total    = valor_morango + valor_maca   # soma total da compra
    total_kg = kg_morango + kg_maca         # soma total em kg

    # aplica 10% de desconto se total de kg > 8 ou valor > R$25,00
    if total_kg > 8 or total > 25:
        total = total * 0.90

    return total

#função principal
def main():
    kg_morango, kg_maca = entrada_dados()          # obtém as quantidades
    resultado = calcular_valor(kg_morango, kg_maca) # calcula o valor final
    print(f"Valor a pagar: R$ {round(resultado, 2)}")  # exibe o valor a pagar
if __name__ == "__main__":    main()
