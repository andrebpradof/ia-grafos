from queue import PriorityQueue
import math

class BuscaAStar():
    
    def heuristica(self, grafo, objetivo):
        for vertice in grafo.lista_Vertices:
            dx = abs(objetivo.getX() - vertice.getX())
            dy = abs(objetivo.getY() - vertice.getY())
            vertice.setHeuristica(math.sqrt(pow(dx, 2) + pow(dy, 2)))

    def cria_caminho(percurso, inicio, alvo):
        atual = percurso[alvo]
        caminho = [alvo]
        while atual != inicio:
            caminho.append(atual)
            atual = percurso[atual]
        caminho.append(inicio)
        saida = caminho[::-1] #inverte a listas
        return saida
    
    def busca(self, grafo, inicio, alvo):
        f = [ 0 for i in range(len(grafo)) ]
        g = [ 0 for i in range(len(grafo)) ]

        objetivo = grafo.busca_Vertice(alvo)
        self.heuristica(grafo, objetivo)

        visited = [0] * len(grafo)
        visited[inicio] = 1

        pq = PriorityQueue()
        pq.put((0, inicio))
        while pq.empty() == 0:
            atual = pq.get()[1]
            print(u, end=" ")
            if atual == alvo:
                break
    
            for vertice in grafo.busca_Vertice(atual).lista_Arestas:
                distancia = g[atual] + grafo[atual][vertice] + h[vertice]

                if visited[vertice] == 0:
                    g[vertice] = g[atual] + grafo[atual][vertice]
                    f[vertice] = distancia

                    sucessores[vertice] = atual
                    visited[vertice] = 1
                    pq.put((distancia, vertice))