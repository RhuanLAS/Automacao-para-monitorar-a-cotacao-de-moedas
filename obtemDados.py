from urllib import request
import json
import re

def abre_url_return_dic(sigla):
    r = request.urlopen(f"http://economia.awesomeapi.com.br/json/all/{sigla}-BRL")
    dados_moeda = json.load(r)
    return dados_moeda

def add(moeda, dicionario_moeda, sigla):
    hora = dicionario_moeda[sigla]["create_date"]
    padrao_hora = "[0-9]{2}[:][0-9]{2}"
    hora = (re.search(padrao_hora, hora)).group()
    hora = float(hora.replace(":", "."))
    moeda.adiciona_valor(float(dicionario_moeda[sigla]["bid"]), float(dicionario_moeda[sigla]["ask"]), hora)