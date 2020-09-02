from selenium import webdriver
from tipomoeda import Moeda
import time
import links
import hora

############## Achando a hora para inicio do programa #############

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://time.is/pt_br/Brazil")

hora_incial = hora.definindo_hora_inicial(driver)

driver.close()

################# Vendo valores para as moedas ####################

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

peso_argentino = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]', hora_incial)
dolar_canadense = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[3]/td[3]', hora_incial)
dolar_americano = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[6]/td[3]', hora_incial)
euro = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[7]/td[3]', hora_incial)
libra = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[8]/td[3]', hora_incial)

for i in range(0,2): # quantas vezes vai rodar no dia
    links.precessa_moeda(driver, peso_argentino, i)
    links.precessa_moeda(driver, dolar_canadense, i)
    links.precessa_moeda(driver, dolar_americano, i)
    links.precessa_moeda(driver, euro, i)
    links.precessa_moeda(driver, libra, i)
    time.sleep(3600)
    driver.refresh()

print(f"Peso Argentino: {peso_argentino}")
print(f"Dólar Canadense: {dolar_canadense}")
print(f"Dólar Americano: {dolar_americano}")
print(f"Euro: {euro}")
print(f"Libra: {libra}")

driver.close()

###################################################################