
class lista_com_dic:
    def __init__(self):
        self._listaMoedas = []

    def __str__(self):
        return f"{self._listaMoedas[0:]}"

    def coloca_na_lista(self, variavel):
        self._listaMoedas.append(variavel)

    def moeda_a_usar(self,posicao):
        a = self._listaMoedas[posicao]
        return a


def xpath_peso_argentino():
    return '/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]'

def xpath_dolar_canadense():
    return '/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[3]/td[3]'

def xpath_dolar_americano():
    return '/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[6]/td[3]'

def xpath_euro():
    return '/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[7]/td[3]'

def xpath_libra():
    return '/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[8]/td[3]'


