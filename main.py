from urllib import request
import json
import menu
import links
import moeda
import time

escolha = menu.menu_bem_vindo()
if escolha == 1:
    moedas_escolhidas, tempo, num_de_vezes = menu.menu_da_op_1()
    ref_moedas = []
    for i in range(0, len(moedas_escolhidas)):
        sigla = links.dicionario_moedas(moedas_escolhidas[i].strip())
        ref_moedas.append(moeda.Moeda(sigla, moedas_escolhidas[i].rstrip())) # logo cada posição vai ser uma referencia do obj criado



else:
    pass


# r = request.urlopen("http://economia.awesomeapi.com.br/json/all")
# data = json.load(r)
# print(data)
# print()
# print(type(data))
