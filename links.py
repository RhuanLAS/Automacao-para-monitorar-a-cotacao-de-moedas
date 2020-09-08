from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def precessa_moeda(driver, moeda, hora):
    xpath = moeda.mostra_xpath()
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        valor_str = driver.find_element_by_xpath(xpath)
        valor_str = valor_str.get_attribute('textContent')
        print(valor_str) # só para ter uma vizualização melhor. Programa final n terá isso
        moeda.cria_valor_momento(valor_str, hora)
    except NoSuchElementException as e:
        print(e)