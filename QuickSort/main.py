import timeit
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista


def drawGraph(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def QuickSort(lista, inicio = 0, fim = 0):
	i = inicio
	f = fim-1
	pivo = lista[int((inicio+fim)/2)]
	while(i <= f):
		while(lista[i] < pivo and i < fim):
			i= i + 1
		while(lista[f] > pivo and f > inicio):
			f= f -1
		if i <= f:
			lista[i], lista[f] = lista[f],lista[i]
			i = i + 1
			f = f - 1
	if f > inicio:
		QuickSort(lista, inicio, f+1)
	if i < fim:
		QuickSort(lista, i, fim)


quant = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
tempoInvertido = []


for i in quant:
    print(i)
    listaInvertida = geraListaInvertida(i)
    tempoInvertido.append(timeit.timeit("QuickSort({},{},{})".format(listaInvertida, 0,i-1),setup="from __main__ import QuickSort",number=1))


drawGraph(quant,tempoInvertido,"Tamanho", "Tempo", "Tempo_saida", label1 = "Lista Invertida")

