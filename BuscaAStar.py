from queue import PriorityQueue
import math

class BuscaAStar():
    
    def heuristica(self, grafo, objetivo):
        for vertice in grafo.lista_Vertices:
            dx = abs(objetivo.getX() - vertice.getX())
            dy = abs(objetivo.getY() - vertice.getY())
            vertice.setHeuristica(math.sqrt(pow(dx, 2) + pow(dy, 2)))

    def cria_caminho(self, percurso, inicio, alvo):
        atual = percurso[alvo]
        caminho = [alvo]
        while atual != inicio:
            caminho.append(atual)
            atual = percurso[atual]
        caminho.append(inicio)
        saida = caminho[::-1] #inverte a listas
        return saida
    
    def busca(self, grafo, inicio, alvo):

        objetivo = grafo.busca_Vertice(alvo)
        self.heuristica(grafo, objetivo)
        caminho = [-1] * len(grafo.lista_Vertices)

        f = [ 0 for i in range(len(grafo.lista_Vertices)) ]
        g = [ 0 for i in range(len(grafo.lista_Vertices)) ]

        visitados = [0] * len(grafo.lista_Vertices)
        visitados[inicio] = 1

        pq = PriorityQueue()
        pq.put((0, inicio))
        while pq.empty() == 0:
            atual = pq.get()[1]
            if atual == alvo:
                break

            for vertice in grafo.busca_Vertice(atual).lista_Arestas:
                distancia = g[atual] + vertice.getPeso() + vertice.getDestino().getHeuristica()

                if visitados[vertice.getDestino().getId()] == 0:
                    g[vertice.getDestino().getId()] = g[atual] + vertice.getPeso()
                    f[vertice.getDestino().getId()] = distancia

                    caminho[vertice.getDestino().getId()] = atual
                    visitados[vertice.getDestino().getId()] = 1
                    pq.put((distancia, vertice.getDestino().getId()))
        saida = self.cria_caminho(caminho, inicio, alvo)
        return saida