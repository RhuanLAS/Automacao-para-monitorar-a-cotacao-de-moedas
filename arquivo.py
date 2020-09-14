from matplotlib import pyplot as plt
from PIL import Image

def coloca_dados_no_arquivo(moeda):
    v_Compra = []
    v_Venda = []
    v_Hora = []
    for i in range(0, len(moeda)):
        v_Compra.append(moeda.retorna_valores_compra(i))
        v_Venda.append(moeda.retorna_valores_venda(i))
        v_Hora.append(moeda.retorna_valores_hora(i))

    faz_plot(v_Hora, v_Compra, moeda, "Valor de Compra")
    faz_plot(v_Hora, v_Venda, moeda, "Valor de Venda")

def faz_plot(x, y, moeda, str):
    plt.bar(x, y)
    plt.title(f"{moeda.retorna_nome()} - {moeda.retorna_sigla()}")
    plt.ylabel(str)
    plt.xlabel("Hora")
    print()
    nome = input(" Nome da figura para salvar (.png). Nome: ")
    plt.savefig(f"graficos/{nome}.png")
    escolha = escolha_de_plot()
    if escolha == "S":
        plt.show()

def escolha_de_plot():
    escolha = (input(" Deseja ver o gráfico gerado? [S] - SIM e [N] - NÃO: ")).upper()
    while True:
        if escolha == "S":
            break
        elif escolha == "N":
            break
        else:
            print(" Você digitou uma letra inválida. Tente novamente.")
            print()
    return escolha

def abre_os_graficos_feitos(nome):
    f = Image.open(f"graficos/{nome}.png")
    f.show()
