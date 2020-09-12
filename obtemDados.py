from urllib import request
import json
import re

def abre_url_return_dic():
    r = request.urlopen("http://economia.awesomeapi.com.br/json/all")
    dados_moedas = json.load(r)
    return dados_moedas

def add(moeda, dicionario_moedas):
    moeda_certa = dicionario_moedas[moeda.retorna_sigla()]
    hora = moeda_certa["create_date"]
    data = moeda_certa["create_date"]
    padrao_hora = "[0-9]{2}[:][0-9]{2}"
    padrao_data = "[0-9]{4}[-][0-9]{2}[-][0-9]{2}"
    hora = (re.search(padrao_hora, hora)).group()
    hora = float(hora.replace(":", "."))
    data = (re.search(padrao_data, data)).group()
    moeda.adiciona_valor(float(moeda_certa["bid"]), float(moeda_certa["ask"]), hora, data)