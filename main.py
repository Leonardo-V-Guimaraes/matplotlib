from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,6], "g--") # o primeiro parametro recebe o eixo X e o segundo eixo Y. O terceiro argumento é a cor e o tipo de linha
                     # ..."--", color="#03fc24") assim é possivel alterara a cor da linha e o estilo
                     # ..."--", color="cor", lw = 5) Espessura da linha - LW = linewidth 
# USANDO DIFERENTES ESTILOS PARA O TITULO DO GRÁFICO #
#plt.title("Usando Python")
plt.title("Titulo esquerda", fontdict={'family': 'serif', 'color': 'darkblue' , 'weight': 'bold', 'size': 16},loc='left')
plt.title("Titulo central", fontdict={'family': 'monospace', 'color': 'red' , 'weight': 'bold', 'size': 16},loc='center')
plt.title("Titulo direita", fontdict={'family': 'fantasy', 'color': 'black' , 'weight': 'bold', 'size': 16},loc='right')

# ADICIONANDO NOME AOS EIXOS X e Y #

# plt.xlabel('Valores do eixo X')
# plt.ylabel('Valores do eixo Y')
# Ou 
plt.xlabel("Valores do eixo X", family='serif', color='r', weight='normal', size=16, labelpad=6) # labelpad é a distancia entre o titulo e os numeros do grafico
plt.ylabel("Valores do eixo Y", family='serif', color='r', weight='normal', size=16, labelpad=6)

plt.show() # Sempre deve ter o .show, caso contrario nao ira apresentar o grafico
