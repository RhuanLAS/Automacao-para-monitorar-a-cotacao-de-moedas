import re

class Moeda(object):
    def __init__(self, xpath, hora):
        self._valoresDia = [xpath]
        self._horaComeco = hora

    def __str__(self):
        return f"{self._valoresDia[1:]}"

    def mostra_xpath(self):
        return self._valoresDia[0]

    def cria_valor_momento(self, valor_moeda, hora_momento):
        valor_valido = self.verifica_valor_valido(valor_moeda)
        if type(valor_valido) == re.Match:
            valor_moeda = self._transforma_em_float(valor_moeda)
        else:
            valor_moeda = "Atenção Valor Indisponível"
        self._valoresDia.append({"Valor": valor_moeda, "Hora": hora_momento})

    def _transforma_em_float(self, valor_moeda):
        valor_moeda = (valor_moeda.replace(",", ".")).lstrip()
        valor_moeda = float(valor_moeda)
        return valor_moeda

    def verifica_valor_valido(self, valor_moeda):
        identificador = "[0-9]{1,2}[,][0,9]{0,6}"
        retorno = re.search(identificador, valor_moeda)
        return retorno