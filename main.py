import menu
import links
import moeda
import time
import obtemDados

escolha = menu.menu_bem_vindo()
if escolha == 1:
    moedas_escolhidas, tempo, num_de_vezes = menu.menu_da_op_1()
    ref_moedas = []
    for i in range(0, len(moedas_escolhidas)):
        sigla = links.dicionario_moedas(moedas_escolhidas[i].strip())
        ref_moedas.append(moeda.Moeda(sigla, moedas_escolhidas[i].rstrip()))

    for i in range(0, num_de_vezes):
        dicionario_moedas = obtemDados.abre_url_return_dic()
        for j in range(0, len(ref_moedas)):
            obtemDados.add(ref_moedas[j], dicionario_moedas)
            print(ref_moedas[j])
        time.sleep(tempo) # mudar para *3600 dps

else:
    pass


