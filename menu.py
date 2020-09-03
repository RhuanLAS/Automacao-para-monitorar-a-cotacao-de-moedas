
def menu():
    print(" Deseja obter os dados a cada quanto tempo? ")
    escolha = int(input(" Por favor, nos informe o tempo em minutos: "))
    escolha *= 60
    print(" Além disso, quantas vezes quer que obtenha os dados? ")
    escolha1 = int(input(" Quantidade: "))
    return escolha, escolha1

def menu1():
    decoracao = "~" * 15
    print(end="\n")
    print(f" {decoracao} Bem Vindo {decoracao}")
    print(end="\n")
    print(" Para a utilização do programa precisamos ter o driver do navegador (Chrome).")
    print(" Por favor, caso não tenha o driver baixado faça o download para continuar.")
    print(" Localização do driver na sua máquina. Por exemplo, C:\Program Files (x86)\chromedriver.exe")
    escolha = input(" Localização: ")
    return escolha