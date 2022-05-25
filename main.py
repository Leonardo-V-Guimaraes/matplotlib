# Importando Tkinter - pip install tk
from tkinter import *
from tkinter import ttk

# Importando dependencia para o Matplotlib - pip install matplotlib e pip install pandas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Definindo cores
co0 = "#f0f3f5"     # Preto
co1 = "#ffffff"      # Branco
co2 = "6f9fbd"      # Azul
co3 = "#38576b"     # Valor
co4 = "403d3d"      # Letra
co5 = "e06636"      # - profit
co6 = "6dd695"      # + profit
fundo = "3f729b" 

# Criando a janela

janela = Tk()
janela.title('Trabalhando com gráficos')
janela.geometry("1190x500")
janela.resizable(width=FALSE, height=FALSE) # Bloqueando o tamanho da janela

# Dividindo a janela principal em duas partes usando frames
frame_top = Frame(janela, width=1370, height=45, pady=0, padx=0, bg=co1, relief='flat')
frame_top.grid(row=0,column=0)

frame_quadro = Frame(janela, width=1370, height=700, pady=15, padx=7, bg=co1, relief='flat')
frame_quadro.grid(row=1,column=0, sticky=NW)

janela.mainloop()