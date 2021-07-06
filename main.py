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
    numVertices = 10
    k = 3

    grafo = Grafo()

    random.seed(7)

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


    grafo.imprime_grafo()

    print(grafo.bfs(1,6))

if __name__ == '__main__':
    main()