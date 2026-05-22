# sistema de cálculo de desconto

print("Sistema de cálculo de desconto")

produto = input("Digite o nome do produto: ")

preco = float(input("Digite o preço do produto: "))

# cálculo do desconto
desconto = preco * 0.10

# preço final
preco_final = preco - desconto

# saída de dados
print("Produto:", produto)
print("Desconto:", desconto)
print("Preço final:", preco_final)