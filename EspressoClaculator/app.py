from tkinter import *
from ClassCafe import Cafe

# Função para calcular a extração do café
def regular_cafe():
    entrada_moinho_valor = entrada_moinho.get()
    gramas_cafe_valor = float(entrada_gramas.get())
    gramas_xicara_valor = float(entrada_cafe.get())
    tempo_extracao_valor = entrada_tempo.get()

    cafe = Cafe(entrada_moinho_valor, gramas_cafe_valor,
                gramas_xicara_valor, tempo_extracao_valor)
    resultado_extracao = (gramas_cafe_valor / gramas_xicara_valor) * 100
    resultado_extracao_arredondada = round(resultado_extracao, 1)

    if 50 <= resultado_extracao_arredondada <= 50.9:
        resultado.config(
            text=f'A porcentagem da sua extração arredondada foi de {resultado_extracao_arredondada}%\nSeu café espresso equilibrado\n Caracteristicas de um Café Equilibrado: Sabor Suave, Boa Doçura, Acidez Moderada, Corpó Adequado, Sabores Balanceados, Aroma Agradavel, Crema Rica, Bom equilibrio CORPO E ACIDEZ ')
    elif resultado_extracao_arredondada > 51:  # Super extração
        resultado.config(
            text=f'A porcentagem da sua extração arredondada foi de {resultado_extracao_arredondada}%\nSeu café espresso está super extraído\nCaracterísticas de Super-extração: Amargor Excessivo, Sabor Adstringente, Falta de Doçura, Corpo Leve, Sabor Queimado ou Carbonizado, Aroma Subdesenvolvido. Creme Fraco')
    elif resultado_extracao_arredondada < 49:  # Sub extração
        resultado.config(
            text=f'A porcentagem da sua extração arredondada foi de {resultado_extracao_arredondada}%\nSeu café espresso está sub-extrato\nCaracterísticas de Sub-extração: Sabor Acído, Faltade Corpo,  Falta de sabor, Aroma Fraco, Sabor Herbáceo ou Gramíneo, Falta de Doçura, Falta de Crema, Subdesenvolvimento, Coloração Clara, Sabor Aguado')
    else:
        resultado.config(text='ERRO')

# Criar a janela principal
janela = Tk()
janela.title("Espresso Calculator")
janela.resizable(False, False)

# Labels e entradas
texto_orietacao = Label(
    janela, text="Vamos calcular a extração do seu Café Espresso")
texto_orietacao.grid(column=0, row=0)

texto_orientacao_moinho = Label(janela, text="Como está regulado seu moinho? ")
texto_orientacao_moinho.grid(column=0, row=1)
entrada_moinho = Entry(janela)
entrada_moinho.grid(column=1, row=1)

texto_orientacao_gramas = Label(
    janela, text="Quantas gramas tem seu Espresso? ")  # IN
texto_orientacao_gramas.grid(column=0, row=2)
entrada_gramas = Entry(janela)
entrada_gramas.grid(column=1, row=2)

texto_orientacao_cafe = Label(
    janela, text="Quantas gramas tem seu Café espresso na Xicara? ")  # OUT
texto_orientacao_cafe.grid(column=0, row=3)
entrada_cafe = Entry(janela)
entrada_cafe.grid(column=1, row=3)

texto_orientacao_tempo = Label(
    janela, text="Qual foi o tempo de extração do seu Café")
texto_orientacao_tempo.grid(column=0, row=4)
entrada_tempo = Entry(janela)
entrada_tempo.grid(column=1, row=4)

botao = Button(janela, text="Calcular extração", command=regular_cafe)
botao.grid(column=0, row=5)

resultado = Label(janela, text="")
resultado.grid(column=0, row=6, columnspan=2)

janela.mainloop()
