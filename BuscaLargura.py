def bfs(self, inicio, fim):
        fila = deque()
        fila.append(inicio)
        visitados = []

        visitados.append(inicio)

        if inicio != fim:
            while len(fila) > 0:
                u = fila.popleft()
                for a in self.busca_Vertice(u).getListaArestas():
                    v = a.getDestino().getId()
                    if v not in visitados:
                        visitados.append(v)
                        if v == fim:
                            print('fim')
                            return visitados
                print('>>', fila)
            print('fim 2')
            return visitados
        else:
            return visitados