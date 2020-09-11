from urllib import request
import json
import menu

escolha = menu.menu_bem_vindo()
if escolha == 1:
    moedas_escolhidas = menu.menu_da_op_1()

else:
    pass


# r = request.urlopen("http://economia.awesomeapi.com.br/json/all")
# data = json.load(r)
# print(data)
# print()
# print(type(data))
