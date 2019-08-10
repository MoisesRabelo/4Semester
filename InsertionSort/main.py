import timeit
from random import randint
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista
      
def geraListaRandomica(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def drawGraph(x,lista1,lista2,xl = "Entradas", yl = "Y",name="out", label1 = "Lista Randomica", label2= "Lista Invertida"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.plot(x, lista2, label = label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

operacoes =[]

def InsertionSort(lista):
	count = 0
	for x in range(0, len(lista)):
		key = lista[x]
		y = x-1
		while key < lista[y] and y>=0:
			lista[y+1] = lista[y]
			y-=1
			count+=1
		lista[y+1] = key
		count+=1
	operacoes.append(count)


quant = [10000, 20000, 50000, 100000]
tempoRandomica = []
tempoInvertida = []

for i in range(len(quant)):
    listaRandomica = geraListaRandomica(quant[i])
    tempoRandomica.append(timeit.timeit("InsertionSort({})".format(listaRandomica),setup="from __main__ import InsertionSort",number=1))
operacoesRandomica = operacoes
operacoes = []

for i in range(len(quant)):
    listaInvertida = geraListaInvertida(quant[i])
    tempoInvertida.append(timeit.timeit("InsertionSort({})".format(listaInvertida),setup="from __main__ import InsertionSort",number=1))

operacoesInvertida = operacoes
operacoes = []


drawGraph(quant,tempoRandomica,tempoInvertida,"Tamanho", "Tempo", "Tempo")
drawGraph(quant,operacoesRandomica,operacoesInvertida, "Tamanho", "Operacoes", "Operacoes")
