
def menu_bem_vindo():
    decoracao = "*" * 30
    print()
    print(f" {decoracao} BEM VINDO {decoracao}")
    print()
    escolha = menu_inicial()
    return escolha

def menu_inicial():
    decoracao = "+" * 28
    while True:
        print(f" {decoracao} MENU INICIAL {decoracao}")
        print()
        print(" 1 - Para obter dados novos")
        print(" 2 - Para acessar dados já armazenados")
        print(" 0 - Sair")
        escolha = int(input(" Sua escolha: "))
        if escolha > 0 and escolha <= 2:
            break
        elif escolha == 0:
            mensagem_saida_programa()
            exit()
        else:
            print(f" Esta entrada: {escolha} é inválida. Digite novamente")
            print()

    return escolha

def mensagem_saida_programa():
    print()
    print(" Obrigado por usar o programa !!")

def menu_da_op_1():
    moedas_usuario = []
    print()
    print(" Aqui está todas as moedas que oferecemos para obtenção de informações: ")
    print(" Dólar Comercial              Dólar Turismo              Dólar Canadense")
    print(" Dólar Australiano            Euro                       Libra Esterlina")
    print(" Peso Argentino               Iene Japonês               Franco Suíço")
    print(" Yuan Chinês                  Novo Shekel Israelense     Bitcoin")
    print(" Litecoin                     Ethereum                   Ripple")
    print()
    print(" Precisamos saber qual(ais) moeda(s) você deseja obter os dados.")
    print(" Obs: certifique-se que a entrada seja exatamente o que está nas informções acima.")
    while True:
        moeda_escolha = input(" Escolha: ")
        if verifica(moeda_escolha.strip(), moedas_usuario):
            moedas_usuario.append(moeda_escolha)
            decisao_usuario = decisao()
            if decisao_usuario == 'N':
                break
        else:
            print(" ERRO: Você pode ter digitado uma moeda novamente ou ela não está presente em nossa lista.")
            print()

    print()
    tempo = int(input(" Por favor, nos informe o tempo para execução do programa. Em horas: "))
    print()
    num_de_vezes = int(input(" Número de vezes para resgatar possíveis mudanças na cotação: "))

    return moedas_usuario, tempo, num_de_vezes

def verifica(moeda, moedas_usuario): # melhorar a verificação das moedas depois
    lista_moedas_validas = ["DólarComercial", "DólarTurismo", "DólarCanadense", "DólarAustraliano", "Euro", "LibraEsterlina", "PesoArgentino", "IeneJaponês", "FrancoSuíço", "YuanChinês", "NovoShekelIsraelense", "Bitcoin", "Litecoin", "Ethereum", "Ripple"]
    if moeda in lista_moedas_validas and moeda not in moedas_usuario:
        return True
    else:
        return False

def decisao():
    print()
    decisao = (input(" Deseja continuar escolhendo alguma moeda? [S] - SIM e [N] - NÃO: ")).upper()
    if decisao != "S" and decisao != "N":
        print(" Você digitou uma letra não permitida. Digite novamente.")
        print()
        decisao()

    return decisao