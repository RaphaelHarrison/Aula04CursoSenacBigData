# realizar um programa que sempre que o cliente realizar uma compra acima de R$ 250,00, o sistema deve aplicar 16% de desconto. Caso contário, o valor da compra deve permanecer o mesmo

valor = float(input("Entre com o valor da compra: "))
if valor >= 250:
    novo_valor = valor - (valor * 0.16)
    print(f"O novo valor é {novo_valor}")
else:
    print(f"O valor da compra é: {valor}")