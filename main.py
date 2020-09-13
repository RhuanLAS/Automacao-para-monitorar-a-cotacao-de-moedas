import menu
import links
import moeda
import time
import obtemDados
import arquivo

escolha = menu.menu_bem_vindo()
if escolha == 1:
    moeda_escolhida, tempo, num_de_vezes = menu.menu_da_op_1()

    sigla = links.dicionario_moedas(moeda_escolhida.rstrip())
    moeda_e = moeda.Moeda(sigla, moeda_escolhida.rstrip())

    for i in range(0, num_de_vezes):
        dicionario_moeda = obtemDados.abre_url_return_dic(sigla)
        obtemDados.add(moeda_e, dicionario_moeda, sigla)
        time.sleep(tempo) # mudar para *3600 dps

    arquivo.coloca_dados_no_arquivo(moeda_e)

else:
    pass


