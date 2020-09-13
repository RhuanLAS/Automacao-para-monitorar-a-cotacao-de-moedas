
class Moeda:
    def __init__(self, sigla, nome):
        self._sigla = sigla
        self._nomeMoeda = nome
        self._listaValores = []

    def __str__(self):
        return f"{self._listaValores}"

    def __len__(self):
        return len(self._listaValores)

    def retorna_sigla(self):
        return self._sigla

    def retorna_nome(self):
        return self._nomeMoeda

    def retorna_valores_compra(self, posicao):
        return self._listaValores[posicao]["Valor Compra"]

    def retorna_valores_venda(self, posicao):
        return self._listaValores[posicao]["Valor Venda"]

    def retorna_valores_hora(self, posicao):
        return self._listaValores[posicao]["Hora"]

    def adiciona_valor(self, valor_compra, valor_venda, hora):
        self._listaValores.append({"Valor Compra": valor_compra, "Valor Venda": valor_venda,"Hora": hora})