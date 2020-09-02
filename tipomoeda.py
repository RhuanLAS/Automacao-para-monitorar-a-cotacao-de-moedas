
class Moeda:
    def __init__(self, xpath, hora):
        self._valoresDia = [xpath]
        self._horaComeco = hora

    def __str__(self):
        return f"{self._valoresDia[1:]}"

    def mostra_xpath(self):
        return self._valoresDia[0]

    def cria_valor_momento(self, valor_moeda, quantVezes):
        valor_moeda = self._transforma_em_int(valor_moeda)
        self._valoresDia.append({"Valor": valor_moeda, "Hora": self._horaComeco + quantVezes})

    def _transforma_em_int(self, valor_moeda):
        return (float((valor_moeda.replace(',', '.')).lstrip()))