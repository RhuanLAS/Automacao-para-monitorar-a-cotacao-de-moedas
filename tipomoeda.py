
class Moeda:
    def __init__(self, xpath, hora):
        self._valoresDia = [xpath]
        self._horaComeco = hora

    def __str__(self):
        return f"{self._valoresDia[1:]}"

    def mostra_xpath(self):
        return self._valoresDia[0]

    def cria_valor_momento(self, valor_moeda, hora_momento):
        valor_moeda = self._transforma_em_float(valor_moeda)
        self._valoresDia.append({"Valor": valor_moeda, "Hora": hora_momento})

    def _transforma_em_float(self, valor_moeda):
        return float((valor_moeda.replace(',', '.')).lstrip())