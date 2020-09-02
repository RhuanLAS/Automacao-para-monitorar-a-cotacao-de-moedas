from selenium import webdriver
from tipomoeda import Moeda
import time
import links

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

peso_argentino = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]')
dolar_canadense = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[3]/td[3]')
dolar_americano = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[6]/td[3]')
euro = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[7]/td[3]')
libra = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[8]/td[3]')

for i in range(0,2): # quantas vezes vai rodar no dia
    links.precessa_moeda(driver, peso_argentino)
    links.precessa_moeda(driver, dolar_canadense)
    links.precessa_moeda(driver, dolar_americano)
    links.precessa_moeda(driver, euro)
    links.precessa_moeda(driver, libra)
    time.sleep(2)

print(f"Peso Argentino: {peso_argentino}")
print(f"Dólar Canadense: {dolar_canadense}")
print(f"Dólar Americano: {dolar_americano}")
print(f"Euro: {euro}")
print(f"Libra: {libra}")

driver.close()