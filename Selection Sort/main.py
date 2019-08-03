import timeit
from random import randint
import matplotlib.pyplot as plt

def geraListaInvertida(tam):
    lista = []
    while tam:
        lista.append(tam)
        tam-=1
    return lista

      
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def drawGraph(x,lista1,lista2,xl = "Entradas", yl = "Y",name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = "Vetor Randomico")
    ax.plot(x, lista2, label = "Vetor Invertido")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

operacoes1 =[]
operacoes2 =[]

def selection1(lista):
    count=0
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
            if lista[i] != lista[minimo]:
                lista[minimo], lista[i] = lista[i], lista[minimo]
                count+=1
    operacoes1.append(count)


def selection2(lista):
    count=0
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
            if lista[i] != lista[minimo]:
                lista[minimo], lista[i] = lista[i], lista[minimo]
                count+=1
    operacoes2.append(count)


quantidade = [10000, 20000, 50000, 100000]

tempo1 = []
tempo2 = []

for i in range(len(quantidade)):
    print(quantidade[i])
    vetor1 = geraLista(quantidade[i])
    vetor2 = geraListaInvertida(quantidade[i])
    tempo1.append(timeit.timeit("selection1({})".format(vetor1),setup="from __main__ import selection1",number=1))
    tempo2.append(timeit.timeit("selection2({})".format(vetor2), setup="from __main__ import selection2", number=1))

drawGraph(quantidade,tempo1,tempo2,"Tamanho", "Tempo", "tempo")
drawGraph(quantidade,operacoes1,operacoes2, "Tamanho", "Operacoes", "operacoes")
