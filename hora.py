from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def definindo_hora_inicial(driver):
    if WebDriverWait(driver, 100).until(EC.title_contains("Brasil:")):
        return float(((driver.title).lstrip("Brasil: ")).replace(":", "."))
    else:
        assert False
