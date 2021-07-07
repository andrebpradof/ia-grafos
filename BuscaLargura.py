from collections import deque

class BuscaLargura():

    def busca(grafo, inicio, fim):

        fila = deque([inicio])
        visitas = {inicio}
        caminho = {}

        while fila:
            vert = fila.popleft()
            if vert == fim:
                break
            for a in grafo.busca_Vertice(vert).getListaArestas():
                vizinho = a.getDestino().getId()
                if vizinho not in visitas:
                    visitas.add(vizinho)
                    caminho[vizinho] = vert
                    fila.append(vizinho)
        path = [fim]
        while path[-1] != inicio:
            last_node = path[-1]
            next_node = caminho[last_node]
            path.append(next_node)

        return path[::-1]