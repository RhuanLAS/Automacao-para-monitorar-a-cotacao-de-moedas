from selenium import webdriver
from tipomoeda import Moeda
import time
import links
import hora
import menu

######### Chamando o menu 1 para saber o driver do Chrome #########

localizacao_driver_Chrome = menu.menu1()

######### Chamando o menu para saber o intervalo de tempo #########

intevalo_de_tempo, quant_vezes_no_tempo = menu.menu()

############## Achando a hora para inicio do programa #############

driver_hora = webdriver.Chrome(localizacao_driver_Chrome) # C:\Program Files (x86)\chromedriver.exe
driver_hora.get("https://time.is/pt_br/Brazil")
hora_momento = hora.hora_momento(driver_hora)

################# Vendo valores para as moedas ####################

peso_argentino = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[3]', hora_momento)
dolar_canadense = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[3]/td[3]', hora_momento)
dolar_americano = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[6]/td[3]', hora_momento)
euro = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[7]/td[3]', hora_momento)
libra = Moeda('/html/body/div[4]/div/div[1]/div[2]/div/div/table/tbody/tr[8]/td[3]', hora_momento)

driver_moedas = webdriver.Chrome(localizacao_driver_Chrome) # C:\Program Files (x86)\chromedriver.exe
driver_moedas.get("https://www.infomoney.com.br/ferramentas/cambio/")

for i in range(0,quant_vezes_no_tempo): # quantas vezes vai rodar
    links.precessa_moeda(driver_moedas, peso_argentino, hora_momento)
    links.precessa_moeda(driver_moedas, dolar_canadense, hora_momento)
    links.precessa_moeda(driver_moedas, dolar_americano, hora_momento)
    links.precessa_moeda(driver_moedas, euro, hora_momento)
    links.precessa_moeda(driver_moedas, libra, hora_momento)
    if i != quant_vezes_no_tempo-1:
        time.sleep(intevalo_de_tempo)
        hora_momento = hora.hora_momento(driver_hora)
        driver_moedas.refresh()

driver_moedas.close()
driver_hora.close()

print(f" Peso Argentino: {peso_argentino}")
print(f" Dólar Canadense: {dolar_canadense}")
print(f" Dólar Americano: {dolar_americano}")
print(f" Euro: {euro}")
print(f" Libra: {libra}")

###################################################################