from queue import PriorityQueue
import math

class BuscaBestFirst():

    def heuristica(self, grafo, objetivo):
        for vertice in grafo.lista_Vertices:
            dx = abs(objetivo.getX() - vertice.getX())
            dy = abs(objetivo.getY() - vertice.getY())
            vertice.setHeuristica(math.sqrt(pow(dx, 2) + pow(dy, 2)))


    def busca(self, grafo, inicio, alvo):
        objetivo = grafo.busca_Vertice(alvo)
        self.heuristica(grafo, objetivo)
        visited = [0] * len(grafo.lista_Vertices)
        visited[inicio] = 1

        pq = PriorityQueue()
        pq.put((0, inicio))
        while pq.empty() == 0:
            atual = pq.get()[1]
            print(atual, end=" ")
            if atual == alvo:
                #print(sucessores)
                break
    
            for vertice in grafo.busca_Vertice(atual).lista_Arestas:
                distancia = vertice.getDestino().getHeuristica()
                if visited[vertice.getDestino().getId()] == 0:
                    #sucessores[vertice] = atual
                    visited[vertice.getDestino().getId()] = 1
                    pq.put((distancia, vertice.getDestino().getId()))
        print()

    
