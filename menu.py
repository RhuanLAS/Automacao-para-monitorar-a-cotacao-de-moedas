
def menu_bem_vindo():
    decoracao = "*" * 30
    print()
    print(f" {decoracao} BEM VINDO {decoracao}")
    print()

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
    print()
    print(" Aqui está todas as moedas que oferecemos para obtenção de informações: ")
    print(" Dólar Comercial              Dólar Turismo              Dólar Canadense")
    print(" Dólar Australiano            Euro                       Libra Esterlina")
    print(" Peso Argentino               Iene Japonês               Franco Suíço")
    print(" Yuan Chinês                  Novo Shekel Israelense     Bitcoin")
    print(" Litecoin                     Ethereum                   Ripple")
    print()
    print(" Precisamos saber qual moeda você deseja obter os dados.")
    print(" Obs: certifique-se que a entrada seja exatamente o que está nas informções acima.")
    while True:
        moeda_escolha = input(" Escolha: ")
        if verifica(moeda_escolha.rstrip()):
            decisao_usuario = decisao(moeda_escolha)
            if decisao_usuario == 'S':
                break
        else:
            print(" ERRO: Você pode ter digitado uma moeda repetida ou ela não está presente em nossa lista.")
            print()

    print()
    tempo = int(input(" Por favor, nos informe o tempo para obter informações no programa. Em horas: "))
    print()
    num_de_vezes = int(input(" Número de vezes para resgatar possíveis mudanças na cotação: "))
    print()
    hora = float(input(" Horário que foi iniciado o programa (0 - 23.59): "))

    return moeda_escolha, tempo, num_de_vezes, hora

def verifica(moeda): # melhorar a verificação das moedas depois
    lista_moedas_validas = ["Dólar Comercial", "Dólar Turismo", "Dólar Canadense", "Dólar Australiano", "Euro", "Libra Esterlina", "Peso Argentino", "Iene Japonês", "Franco Suíço", "Yuan Chinês", "Novo Shekel Israelense", "Bitcoin", "Litecoin", "Ethereum", "Ripple"]
    if moeda in lista_moedas_validas:
        return True
    else:
        return False

def decisao(moeda_escolha):
    print()
    decisao = (input(f" Sua escolha foi: {moeda_escolha}. Tem certeza da sua escolha? [S] - SIM e [N] - NÃO: ")).upper()
    if decisao != "S" and decisao != "N":
        print(" Você digitou uma letra não permitida. Digite novamente.")
        print()
        decisao()

    return decisao

def pergunta_continua():
    print()
    escolha = (input(" Deseja acessar mais uma funcionalidade do programa? [S] - SIM ou [N] - NÃO: ")).upper()
    print()
    while True:
        if escolha == "S" or escolha == "N":
            break
        else:
            print(" Por favor, digite uma letra válida")
            print()
    return escolha