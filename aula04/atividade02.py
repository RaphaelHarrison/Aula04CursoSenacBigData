# refazer a atividade 01, mas o desconto só deve ser aplicado se duas condições forem atendidas ao MESMO tempo
# valor de compra ACIMA de 250 e a forma de pagamento ser à vista

valor = float(input("Entre com o valor da compra: "))
pagamento = input("Qual será a forma de pagamento(debito ou parcelado): ").lower()

if valor > 250 and pagamento == "debito":
    novo_valor = valor - (valor * 0.16)
    print(f"O valor da compra é: {novo_valor}")
else:
    print(f"O valor da compra é: {valor}")