print("Bem-vindo(a) à loja de camisetas em atacado Gleyson Lima dos Santos")
print(25 * '-')
print("-> Camiseta Manga Curta Simples (MCS) = R$ 1,80")
print("-> Camiseta Manga Longa Simples (MLS) = R$ 2,10")
print("-> Camiseta Manga Curta Com Estampa (MCE) = R$ 2,90")
print("-> Camiseta Manga Longa Com Estampa (MLE) = R$ 3,20")
print(25 * '-')

def Modelo():
    modelo = input("Qual o modelo de camiseta desejado? ").strip().upper()

    if modelo == "MCS":
        return 1.80
    elif modelo == "MLS":
        return 2.10
    elif modelo == "MCE":
        return 2.90
    elif modelo == "MLE":
        return 3.20
    else:
        print("Modelo inválido. Tente novamente.")
        return Modelo()

def totalCamisetas(valor):
    try:
        quantidade = int(input("Quantas camisetas deseja comprar? "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return totalCamisetas(valor)
    
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
    try:
        valor = int(input("Qual serviço de frete você deseja?\n0) Retirar na fábrica, R$ 0\n1) Transportadora, R$ 100\n2) Sedex, R$ 200\n"))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return frete()

    if valor == 0:
        return 0
    elif valor == 1:
        return 100
    elif valor == 2:
        return 200
    else:
        print("Valor inválido. Tente novamente.")
        return frete()

valor = Modelo()
total = totalCamisetas(valor) + frete()

print(f"O valor total da sua compra é R$ {total:.2f}")
