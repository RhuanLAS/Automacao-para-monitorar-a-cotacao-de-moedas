
class Moeda:
    def __init__(self, sigla, nome):
        self._sigla = sigla
        self._nomeMoeda = nome
        self._listaValores = []

    def __str__(self):
        return f"{self._listaValores}"

    def retorna_sigla(self):
        return self._sigla

    def adiciona_valor(self, valor_compra, valor_venda, hora, data):
        self._listaValores.append({"Valor Compra": valor_compra, "Valor Venda": valor_venda,"Hora": hora, "data": data})