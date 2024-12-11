print("Bem vindo(a) a loja de camisetas em atacado Gleyson Lima dos Santos")
print(25 * '-')
print("-> Camiseta Manga Curta Simples (MCS) = R$ 1,80")
print("-> Camiseta Manga Longa Simples (MLS) = R$ 2,10")
print("-> Camiseta Manga Curta Com Estampa (MCE) = R$ 2,90")
print("-> Camiseta Manga Longa Com Estampa (MLE) = R$ 3,20")
print(25 * '-')

def Modelo():
    # Solicita ao usuário o modelo de camiseta desejado e retorna o valor correspondente.
    modelo = input("Qual o modelo de camiseta desejado? ").strip().upper()

    return {
        "MCS": 1.80,
        "MLS": 2.10,
        "MCE": 2.90,
        "MLE": 3.20
    }.get(modelo, ModeloInvalido())

def ModeloInvalido():
    print("Modelo inválido. Tente novamente.")
    return Modelo()

def totalCamisetas(valor):
    # Solicita ao usuário a quantidade de camisetas desejada e calcula o total com base nos descontos aplicáveis.
    try:
        quantidade = int(input("Quantas camisetas deseja comprar? "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return totalCamisetas(valor)

    if quantidade < 20:
        return valor * quantidade
    descontos = [(20, 0.95), (200, 0.93), (2000, 0.88)]
    for limite, desconto in descontos:
        if quantidade < limite:
            return valor * quantidade * desconto
    print("Não é aceito pedidos nessa quantidade de camisetas!")
    return totalCamisetas(valor)

def frete():
    # Solicita ao usuário o tipo de serviço de frete desejado e retorna o valor correspondente.
    try:
        valor = int(input("Qual serviço de frete você deseja?\n0) Retirar na fábrica, R$ 0\n1) Transportadora, R$ 100\n2) Sedex, R$ 200\n"))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return frete()

    return {0: 0, 1: 100, 2: 200}.get(valor, ValorInvalido())

def ValorInvalido():
    print("Valor inválido. Tente novamente.")
    return frete()

valor = Modelo()
total = totalCamisetas(valor) + frete()

print(f"O valor total da sua compra é R$ {total:.2f}")
