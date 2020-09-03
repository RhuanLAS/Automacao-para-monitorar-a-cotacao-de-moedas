from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def definindo_hora_inicial(driver):
    if WebDriverWait(driver, 100).until(EC.title_contains("Brasil:")):
        hora = driver.title
        hora = (hora.lstrip("Brasil: ")).replace(":", ".")
        return float(hora)
    else:
        assert False

def hora_momento(driver_hora):
    hora_momento = definindo_hora_inicial(driver_hora)
    return hora_momento