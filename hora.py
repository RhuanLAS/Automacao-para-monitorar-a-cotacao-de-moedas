from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def definindo_hora_inicial(driver):
    if WebDriverWait(driver, 100).until(EC.title_contains("Brasil:")):
        string_com_hora = driver.title
        string_com_hora = string_com_hora.lstrip("Brasil: ")
        string_com_hora = string_com_hora.replace(":", ".")
        string_com_hora = float(string_com_hora)
    else:
        assert False
