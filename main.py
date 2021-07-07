from Vertice import Vertice
from Grafo import Grafo
from BuscaLargura import BuscaLargura
from BuscaProfundidade import BuscaProfundidade
from BuscaBestFirst import BuscaBestFirst
from BuscaA import BuscaA
from BuscaAStar import BuscaAStar
import random
import math
import numpy as np
import time

from Grafico import Grafico

class Euclidianas:
    def __init__(self,id,distancia):
        self.id = id
        self.distancia = distancia

    def getDistancia(self):
        return self.distancia

    def getId(self):
        return self.id

    def setDistancia(self, dist):
        self.distancia = dist

    def setId(self, id):
        self.id = id

def main():
    numVertices = 20
    k = 3
    grafo = Grafo()
    random.seed(9)
    inicio = 1
    alvo = 10

    for i in range(numVertices):
        x = random.randrange(1,numVertices)
        y = random.randrange(1,numVertices)
        vertice = Vertice(i, x, y)
        grafo.novo_Vertice(vertice)
    
    matrizEuclidianas = np.empty((numVertices,numVertices), dtype=object)


    for i in range(numVertices):
        vertice_i = grafo.busca_Vertice(i)
        for j in range(numVertices):
            if i == j:
                matrizEuclidianas[i][j] = Euclidianas(j,np.inf)
            else:
                vertice_j = grafo.busca_Vertice(j)
                valor = math.sqrt(math.pow(vertice_i.getX() - vertice_j.getX(),2) + math.pow(vertice_i.getY() - vertice_j.getY(),2))
                matrizEuclidianas[i][j] = Euclidianas(j,valor)

    for i in range(numVertices):
        matrizEuclidianas[i] = sorted(matrizEuclidianas[i], key=Euclidianas.getDistancia)
        for j in range(k):
            if(grafo.busca_Aresta(i, matrizEuclidianas[i][j].getId()) == False):
                grafo.nova_Aresta(i, matrizEuclidianas[i][j].getId(), matrizEuclidianas[i][j].getDistancia())
            if(grafo.busca_Aresta(matrizEuclidianas[i][j].getId(), i) == False):
                grafo.nova_Aresta(matrizEuclidianas[i][j].getId(), i, matrizEuclidianas[i][j].getDistancia())

    print("**** Busca em Largura ****")
    t = time.time()
    trajeto1 = BuscaLargura.busca(grafo,inicio,alvo)
    tf = time.time() - t
    print(">> Tempo: {:.4f}".format(tf))
    print(">> Trajeto: ", trajeto1)
    print()
    
    Grafico.start(grafo, numVertices, inicio , alvo, trajeto1,'graph-largura.png')

    print("**** Busca em profundidade ****")
    t = time.time()
    trajeto2 = BuscaProfundidade().start(grafo, inicio,alvo)
    tf = time.time() - t
    print(">> Tempo: {:.4f}".format(tf))
    print(">> Trajeto: ", trajeto2)
    print()

    Grafico.start(grafo, numVertices, inicio , alvo, trajeto2,'graph-profundidade.png')

    print("**** Busca Best First ****")
    t = time.time()
    trajeto3 = BuscaBestFirst().busca(grafo, inicio, alvo)
    tf = time.time() - t
    print(">> Tempo: {:.4f}".format(tf))
    print(">> Trajeto: ", trajeto3)
    print()

    Grafico.start(grafo, numVertices, inicio , alvo, trajeto3,'graph-best-first.png')

    print("**** Busca A ****")
    t = time.time()
    trajeto4 = BuscaA().busca(grafo, inicio, alvo)
    tf = time.time() - t
    print(">> Tempo: {:.4f}".format(tf))
    print(">> Trajeto: ", trajeto4)
    print()

    Grafico.start(grafo, numVertices, inicio , alvo, trajeto4,'graph-a.png')

    print("**** Busca A-Star ****")
    t = time.time()
    trajeto5 = BuscaAStar().busca(grafo, inicio, alvo)
    tf = time.time() - t
    print(">> Tempo: {:.4f}".format(tf))
    print(">> Trajeto: ", trajeto5)
    print()

    Grafico.start(grafo, numVertices, inicio , alvo, trajeto5,'graph-a-star.png')

if __name__ == '__main__':
    main()