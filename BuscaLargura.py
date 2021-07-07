from collections import deque

class BuscaLargura():

    def busca(grafo, inicio, fim):
        fila = deque()
        fila.append(inicio)
        visitados = []

        visitados.append(inicio)

        if inicio != fim:
            while len(fila) > 0:
                u = fila.popleft()
                for a in grafo.busca_Vertice(u).getListaArestas():
                    v = a.getDestino().getId()
                    if v not in visitados:
                        visitados.append(v)
                        if v == fim:
                            return visitados
                        fila.append(v); 
            return -1
        else:
            return visitados