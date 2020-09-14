import menu
import links
import moeda
import time
import obtemDados
import arquivo

menu.menu_bem_vindo()

while True:
    escolha = menu.menu_inicial()
    if escolha == 1:
        moeda_escolhida, tempo, num_de_vezes, hora = menu.menu_da_op_1()

        sigla = links.dicionario_moedas(moeda_escolhida.rstrip())
        moeda_e = moeda.Moeda(sigla, moeda_escolhida.rstrip())

        for i in range(0, num_de_vezes):
            dicionario_moeda = obtemDados.abre_url_return_dic(sigla)
            obtemDados.add(moeda_e, dicionario_moeda, sigla, hora)
            time.sleep(tempo*3600)
            hora = links.hora(hora, tempo)

        arquivo.coloca_dados_no_arquivo(moeda_e)

    elif escolha == 2:
        print()
        print(" Deseja acessar qual gráfico já plotado? ")
        nome = input(" Nome do arquivo (.png): ")
        arquivo.abre_os_graficos_feitos(nome)
    else:
        break

    escolha_continuar = menu.pergunta_continua()
    if escolha_continuar == "N":
        break

menu.mensagem_saida_programa()