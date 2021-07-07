
from collections import deque

class BuscaProfundidade():
    def __init__(self):
        self.visitados = []
        self.caminho = []

    def DFS(self, grafo, inicio, fim):

        self.caminho.append(inicio)
        self.visitados.append(inicio)

        if inicio == fim:
            return self.caminho
        else:
            for j in grafo.lista_Vertices[inicio].getListaArestas():
                nodo = j.getDestino().getId()
                if nodo not in self.visitados:
                    volta = self.DFS(grafo, nodo, fim)
                    if volta is not None:
                        return self.caminho
        self.caminho.pop()

    def start(self, grafo, inicio, fim):
        return self.DFS(grafo, inicio, fim)