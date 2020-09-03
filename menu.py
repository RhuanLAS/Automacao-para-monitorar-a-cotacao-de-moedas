
def menu():
    decoracao = "~" * 15
    print(f" {decoracao} Bem Vindo {decoracao}")
    print(end="\n")
    print(" Deseja obter os dados a cada quanto tempo? ")
    escolha = int(input(" Por favor, nos informe o tempo em minutos: "))
    escolha *= 60
    return escolha