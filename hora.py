from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

def definindo_hora_inicial(driver):
    try:
        WebDriverWait(driver, 20).until(EC.title_contains("Brasil:"))
        hora = driver.title
        hora_valida = verifica_valor_hora(hora)
        if type(hora_valida) == re.Match:
            hora = (hora.lstrip("Brasil: ")).replace(":", ".")
            hora = float(hora)
            return hora
        else:
            return "Atencao Hora Indisponivel"
    except NoSuchElementException as e:
        print(e)

def hora_momento(driver_hora):
    hora_momento = definindo_hora_inicial(driver_hora)
    return hora_momento

def verifica_valor_hora(hora):
    identificador = "[0-9]{1,2}[:][0-9]{1,2}"
    retorno = re.search(identificador, hora)
    return retorno