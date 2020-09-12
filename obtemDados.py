from urllib import request
import json

def abre_url_return_dic():
    r = request.urlopen("http://economia.awesomeapi.com.br/json/all")
    dados_moedas = json.load(r)
    return dados_moedas

def add(moeda, dicionario_moedas, hora):
    moeda_certa = dicionario_moedas[moeda.retorna_sigla()]
    moeda.adiciona_valor(moeda_certa["bid"], moeda_certa["ask"], hora)