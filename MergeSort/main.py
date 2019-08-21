import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
      

def drawGraph(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def Merge_sort(lista): 
    if len(lista) >1: 
        meio = int(len(lista)/2)
        left = [] 
        right = []
        for i in range(0, meio):
            left.append(lista[i])
        for i in range(meio, len(lista)):
            right.append(lista[i])
  
        Merge_sort(left) 
        Merge_sort(right) 
  
        i = j = k = 0     
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                lista[k] = left[i] 
                i+=1
            else: 
                lista[k] = right[j] 
                j+=1
            k+=1
          
        while i < len(left): 
            lista[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            lista[k] = right[j] 
            j+=1
            k+=1

quant = [100000,200000,400000,500000,1000000,2000000]
tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    tempo.append(timeit.timeit("Merge_sort({})".format(lista),setup="from __main__ import Merge_sort",number=1))


drawGraph(quant,tempo,"Tamanho", "Tempo", "tempo", label1 = "Lista")
