# Sistema de cadastro de personagens de RPG

print("=== Cadastro de Personagem RPG ===")

# Entrada de dados
nome = input("Digite o nome do personagem: ")
classe = input("Digite a classe do personagem: ")
forca = int(input("Digite a força do personagem: "))

# Cálculo do nível
if forca > 20:
    nivel = 10
elif forca >= 10:
    nivel = 5
else:
    nivel = 1

# Saída de dados
print("\n=== Dados do Personagem ===")
print("Nome:", nome)
print("Classe:", classe)
print("Força:", forca)
print("Nível:", nivel)