# Estrutura IF

# idade = int(input("Entre com sua idade: "))
# if idade >= 18:
#     print("Você pode entrar, pois é maior de idade.")
# else:
#     print("Você não pode entrar, pois não é adulto.")

#------------------------------------------------------------------

# pontos = int(input("Insira a quantidade de pontos feitos: "))

# if pontos >= 100:
#     print("Excelente!")
# elif pontos >= 50:
#     print("Pode melhorar")
# elif pontos >= 25:
#     print("Melhore.")
# else:
#     print("Melhore URGENTE!!!!")

#-------------------------------------------------------------------
# Operadores AND e OR 

usuario = input("Entre com o nome do usuário: ")
senha = int(input("Entre com a senha: "))

if usuario == "admin" and senha == 1234:
    print("Acesso liberado")
else:
    print("Tente novamente!")