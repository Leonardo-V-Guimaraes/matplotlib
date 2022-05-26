# Importando Tkinter - pip install tk
from tkinter import *
from tkinter import ttk

# Importando dependencia para o Matplotlib - pip install matplotlib e pip install pandas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Definindo cores
co0 = "#f0f3f5"      # Preto
co1 = "#fcfafa"      # Branco
co2 = "#6f9fbd"      # Azul
co3 = "#38576b"      # Valor
co4 = "#403d3d"      # Letra
co5 = "#e06636"      # - profit
co6 = "#6dd695"      # + profit
fundo = "#3f729b" 

# Criando a janela

janela = Tk()
janela.title('Trabalhando com gráficos')
janela.geometry("1190x500")
janela.resizable(width=FALSE, height=FALSE) # Bloqueando o tamanho da janela

# Dividindo a janela principal em duas partes usando frames
frame_top = Frame(janela, width=1370, height=45, pady=0, padx=0, bg=co1, relief='flat')
frame_top.grid(row=0,column=0)

frame_quadro = Frame(janela, width=1370, height=700, pady=10, padx=7, relief='flat')
frame_quadro.grid(row=1,column=0,pady=5, sticky=NW)

# Configurando frame top
app_nome = Label(frame_top, text='Dashboard de Vendas', width=20, height=2, pady=2, padx=0, bg=co1,fg= co4 ,relief='flat' ,anchor=N ,font=('Ivy 14 bold'))
app_nome.place(x=0, y=5)

# Configurando frame quadro

# Receitas de Vendas
frame_Total = Frame(frame_quadro, width=200, height=90, bg=co0, relief='flat')
frame_Total.place(x=0, y=0)

app_traco = Label(frame_Total, width=1, height=1, pady=0, padx=0, bg=co2,relief='flat' ,anchor=NW)
app_traco.place(x=0, y=0)

app_nome = Label(frame_Total, text='Receita de Vendas', width=30, height=1, pady=0, padx=0, bg=co1 ,fg= co4 ,relief='flat' ,anchor=NW ,font=('Ivy 10 bold'))
app_nome.place(x=12, y=1)

app_nome_valor = Label(frame_Total, text='R$ 789.157,15', width=13, height=1, pady=0, padx=0, bg=co1 ,fg= co3 ,relief='flat' ,anchor=CENTER ,font=('Ivy 18 bold'))
app_nome_valor.place(x=0, y=20)

app_nome_ganho = Label(frame_Total, text='+18% vs mês anterios', width=30, height=1, pady=0, padx=0, bg=co1 ,fg= co6 ,relief='flat' ,anchor=CENTER ,font=('Ivy 8 bold'))
app_nome_ganho.place(x=0, y=50)

janela.mainloop()