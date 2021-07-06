import math

class BuscaA():

    def heuristica(self, grafo, objetivo):
        for vertice in grafo.lista_Vertices:
            dx = abs(objetivo.getX() - vertice.getX())
            dy = abs(objetivo.getY() - vertice.getY())
            vertice.setHeuristica(math.sqrt(pow(dx, 2) + pow(dy, 2)))

    def start(self, grafo, inicio, fim):
        f = [ 0 for i in range(len(grafo)) ]
        g = [ 0 for i in range(len(grafo)) ]

        objetivo = grafo.busca_Vertice(fim)
        self.heuristica(grafo, objetivo)