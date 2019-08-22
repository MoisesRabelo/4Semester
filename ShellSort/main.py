import timeit
from random import shuffle
import matplotlib.pyplot as plt


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def gerlistaaI(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def gerlistaaO(tam):
    lista = list(range(1, tam + 1))
    return lista


def drawGraph(x,SHSort , xLabel = "Entradas", yLabel = "Saídas", nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,SHSort, label = "Shell Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(nam)


def shellSort(lista): 
  gap=int(len(lista)/2) 
  while gap > 0: 
    for i in range(gap,len(lista)): 
      aux=lista[i] 
      j=i 
      while j>=gap and lista[j-gap]>aux: 
        lista[j]=lista[j-gap] 
        j-=gap 
      lista[j]=aux
    gap=int(gap/2)


lista = [100000, 200000, 400000, 500000, 1000000, 2000000]
saidaSH = []

for i in range(len(lista)):
  saidaSH.append(timeit.timeit("shellSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,shellSort",number=1))
  print(str(lista[i]))

drawGraph(lista, saidaSH, nam="Tempo")
