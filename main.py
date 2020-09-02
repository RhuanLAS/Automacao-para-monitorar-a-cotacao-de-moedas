from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tipomoeda import Moeda
import links
import time

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

peso_argentino = Moeda()
dolar_canadense = Moeda()
dolar_americano = Moeda()
euro = Moeda()
libra = Moeda()

a = links.lista_com_dic()
a.coloca_na_lista(peso_argentino)
a.coloca_na_lista(dolar_canadense)
a.coloca_na_lista(dolar_americano)
a.coloca_na_lista(euro)
a.coloca_na_lista(libra)

# for i in range(0,2):
#     for j in range(0,5):
#         WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, links.xpath_peso_argentino())))
#         valor_str = driver.find_element_by_xpath(links.xpath_peso_argentino()).text
#         peso_argentino.cria_valor_momento(valor_str)
#         time.sleep(2)


# WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, links.xpath_peso_argentino())))
# valor_str = driver.find_element_by_xpath(links.xpath_peso_argentino()).text
# peso_argentino.cria_valor_momento(valor_str)
# time.sleep(2)
#print(peso_argentino)


driver.close()