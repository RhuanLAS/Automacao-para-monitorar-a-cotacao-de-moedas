from urllib import request
import json

def abre_url_return_dic(sigla):
    r = request.urlopen(f"http://economia.awesomeapi.com.br/json/all/{sigla}-BRL")
    dados_moeda = json.load(r)
    return dados_moeda

def add(moeda, dicionario_moeda, sigla, hora):
    moeda.adiciona_valor(float(dicionario_moeda[sigla]["bid"]), float(dicionario_moeda[sigla]["ask"]), hora)