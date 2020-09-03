from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def precessa_moeda(driver, moeda, hora):
    xpath = moeda.mostra_xpath()
    if WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH, xpath))):
        valor_str = driver.find_element_by_xpath(xpath).text
        moeda.cria_valor_momento(valor_str, hora)
    else:
        assert False