from selenium import webdriver
from tipomoeda import Moeda
import time
import links
import hora
import menu

######### Chamando o menu para saber o intervalo de tempo #########

intevalo_de_tempo = menu.menu()

############## Achando a hora para inicio do programa #############

hora_momento = hora.hora_momento()

################# Vendo valores para as moedas ####################

peso_argentino = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]', hora_momento)
dolar_canadense = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[3]/td[3]', hora_momento)
dolar_americano = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[6]/td[3]', hora_momento)
euro = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[7]/td[3]', hora_momento)
libra = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[8]/td[3]', hora_momento)

driver_moedas = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver_moedas.get("https://www.infomoney.com.br/ferramentas/cambio/")

for i in range(0,2): # quantas vezes vai rodar
    links.precessa_moeda(driver_moedas, peso_argentino, hora_momento)
    links.precessa_moeda(driver_moedas, dolar_canadense, hora_momento)
    links.precessa_moeda(driver_moedas, dolar_americano, hora_momento)
    links.precessa_moeda(driver_moedas, euro, hora_momento)
    links.precessa_moeda(driver_moedas, libra, hora_momento)
    if i != 1:
        time.sleep(intevalo_de_tempo)
        hora_momento = hora.hora_momento()
        driver_moedas.refresh()
    else:
        driver_moedas.close()

print(f"Peso Argentino: {peso_argentino}")
print(f"Dólar Canadense: {dolar_canadense}")
print(f"Dólar Americano: {dolar_americano}")
print(f"Euro: {euro}")
print(f"Libra: {libra}")

###################################################################