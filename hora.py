from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def definindo_hora_inicial(driver):
    if WebDriverWait(driver, 100).until(EC.title_contains("Brasil:")):
        return float(((driver.title).lstrip("Brasil: ")).replace(":", "."))
    else:
        assert False

def hora_momento():
    driver_hora = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    driver_hora.get("https://time.is/pt_br/Brazil")
    hora_momento = definindo_hora_inicial(driver_hora)
    driver_hora.close()
    return hora_momento