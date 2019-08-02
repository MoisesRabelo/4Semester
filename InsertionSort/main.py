import timeit
from random import randint
import matplotlib.pyplot as plt

def geraVetor(tam):
    vetor = []
    while len(vetor) < tam:
        n = randint(1,1*tam)
        if n not in vetor: vetor.append(n)
    return vetor

def drawGraph(x,lista,xl = "Entradas", yl = "Y",nam="out"):
    plt.plot(x,lista, label = "Insertion Sort")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

graf_operacoes =[]

def insertionSort(vetor): 
    count = 0
    for i in range(1, len(vetor)):   
        key = vetor[i] 
        j = i-1
        while j >=0 and key < vetor[j] : 
                vetor[j+1] = vetor[j] 
                j -= 1
                count+=1
        vetor[j+1] = key
    graf_operacoes.append(count)

quant = [10000, 20000, 50000, 100000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraVetor(quant[i])
    graf_tempo.append(timeit.timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort",number=1))

drawGraph(quant,graf_tempo,"Tamanho", "Tempo", "time")
drawGraph(quant,graf_operacoes , "Tamanho", "Operações", "operacoes")
