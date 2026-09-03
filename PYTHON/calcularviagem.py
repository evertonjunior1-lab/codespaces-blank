# Função para calcular os custos da viagem
def calcular_custos(passagem, hospedagem, alimentacao):
    return passagem + hospedagem + alimentacao


# Função para verificar o status do custo
def verificar_status(custos):
    if custos >= 2100:
        return "Caro"
    elif custos >= 2000:
        return "Na média"
    else:
        return "Barato"


# Função principal
def main():
    print("----- Sistema de calcular custos de viagens -----")

    continuar = "s"

    while continuar == "s":

        nome = input("Digite o nome do lugar que deseja ir: ")

        passagem = float(input("Digite o valor da passagem: "))
        hospedagem = float(input("Digite o valor da hospedagem: "))
        alimentacao = float(input("Digite o valor da alimentação: "))

        custos = calcular_custos(passagem, hospedagem, alimentacao)

        status = verificar_status(custos)

        print("\n------ RESULTADO -------")
        print(f"Lugar: {nome}")
        print(f"Custos totais: R$ {custos:.2f}")
        print(f"Status: {status}")

        continuar = input("\nDeseja cadastrar outra viagem? (s/n): ").lower()


# Executa o programa
main()