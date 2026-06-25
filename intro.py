nome_jogo = input("Digite o nome do jogo:")
preco_jogo = float(input("Digite o preço do jogo:"))
saldo_disponivel = float(input("Digite o valor que você tem disponivel:"))

saldo_final = saldo_disponivel - preco_jogo

if preco_jogo <= saldo_disponivel:

print("------ RESULTADO -------")
print("compra realizada com sucesso!")
print (f"Saldo final: {saldo_final: 2f}")

else: print()