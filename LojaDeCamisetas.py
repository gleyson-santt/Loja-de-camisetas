# Mensagem de boas-vindas e lista de produtos
print("Bem vindo(a) a loja de camisetas em atacado Gleyson Lima dos Santos")
print(25 * '-')
print("-> Camiseta Manga Curta Simples (MCS) = R$ 1,80")
print("-> Camiseta Manga Longa Simples (MLS) = R$ 2,10")
print("-> Camiseta Manga Curta Com Estampa (MCE) = R$ 2,90")
print("-> Camiseta Manga Longa Com Estampa (MLE) = R$ 3,20")
print(25 * '-')

def Modelo():
    """
    Solicita ao usuário o modelo de camiseta desejado e retorna o valor correspondente.
    """
    modelo = input("Qual o modelo de camiseta desejado? ").strip().upper()

    match modelo:
        case "MCS":
            return 1.80
        case "MLS":
            return 2.10
        case "MCE":
            return 2.90
        case "MLE":
            return 3.20
        case _:
            print("Modelo inválido. Tente novamente.")
            return Modelo()

def totalCamisetas(valor):
    """
    Solicita ao usuário a quantidade de camisetas desejada e calcula o total com base nos descontos aplicáveis.
    """
    try:
        quantidade = int(input("Quantas camisetas deseja comprar? "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return totalCamisetas(valor)
    else:
        if quantidade < 20:
            return valor * quantidade
        elif 20 <= quantidade < 200:
            return valor * quantidade * 0.95  # 5% de desconto
        elif 200 <= quantidade < 2000:
            return valor * quantidade * 0.93  # 7% de desconto
        elif 2000 <= quantidade <= 20000:
            return valor * quantidade * 0.88  # 12% de desconto
        else:
            print("Não é aceito pedidos nessa quantidade de camisetas!")
            return totalCamisetas(valor)

def frete():
    """
    Solicita ao usuário o tipo de serviço de frete desejado e retorna o valor correspondente.
    """
    try:
        valor = int(input("Qual serviço de frete você deseja?\n0) Retirar na fábrica, R$ 0\n1) Transportadora, R$ 100\n2) Sedex, R$ 200\n"))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return frete()

    match valor:
        case 0:
            return 0
        case 1:
            return 100
        case 2:
            return 200
        case _:
            print("Valor inválido. Tente novamente.")
            return frete()

# Executando as funções
valor = Modelo()
total = totalCamisetas(valor) + frete()

# Exibindo o valor total da compra
print(f"O valor total da sua compra é R$ {total:.2f}")
