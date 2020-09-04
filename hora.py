from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def definindo_hora_inicial(driver):
    try:
        WebDriverWait(driver, 250).until(EC.title_contains("Brasil:"))
        hora = driver.title
        hora = (hora.lstrip("Brasil: ")).replace(":", ".")
        #return float(hora)
        return hora
    except NoSuchElementException as e:
        print(e)

def hora_momento(driver_hora):
    hora_momento = definindo_hora_inicial(driver_hora)
    return hora_momento