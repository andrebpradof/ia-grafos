from Vertice import Vertice
from Grafo import Grafo
import random
import math
import numpy as np


class Aux_vertice:
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

    for i in range(numVertices):
        x = random.randrange(1,numVertices)
        y = random.randrange(1,numVertices)
        vertice = Vertice(i, x, y)
        grafo.novo_Vertice(vertice)
    
    matrizEuclidianas = np.zeros((numVertices,numVertices))

    for i in range(numVertices):
        vertice_i = grafo.busca_Vertice(i)
        for j in range(i, numVertices):
            if i == j:
                matrizEuclidianas[i][j] = np.inf
            else:
                vertice_j = grafo.busca_Vertice(j)
                matrizEuclidianas[i][j] = math.sqrt(math.pow(vertice_i.getX() - vertice_j.getX(),2) + math.pow(vertice_i.getY() - vertice_j.getY(),2))

    menor_valores = np.empty((numVertices,k), dtype=object)

    for i in range(numVertices):
        menor_valores[i]
        for l in range(k):
            menor_valores[i][l] = Aux_vertice(-1, np.inf)

    
    for i in range(numVertices):
        for j in range(numVertices):
            
            if(i > j):
                i_aux = j
                j_aux = i
            else:
                i_aux = i
                j_aux = j

            print('Ordem:', i_aux, j_aux)
            # ///////
            for l in range(k):
                aux_dis = matrizEuclidianas[i_aux][j_aux]
                #print(i, aux_dis)
                if(aux_dis < menor_valores[i][l].getDistancia()):
                    print(i, aux_dis)
                    menor_valores[i][l].setId(j_aux)
                    menor_valores[i][l].setDistancia(aux_dis)
                    break
            # ////////

        for l in range(k):
            grafo.nova_Aresta(i,menor_valores[i][l].getId(), menor_valores[i][l].getDistancia())
    
    grafo.imprime_grafo()



if __name__ == '__main__':
    main()