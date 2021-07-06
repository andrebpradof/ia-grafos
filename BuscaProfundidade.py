def busca_Profundidade(self, grafo, origem, destino):
        """Executa a busca em profundidade a partir do vértice start
        Args:
            start (int): vértice start
        Returns:
            list: lista com a ordem de vértices visitados 
        """
        visitados = []
        visitados.append(origem)
        pilha = [origem]
        
        if origem != destino:
            while pilha:
                u = pilha.pop()

                #if u not in visitados:
                #    visitados.append(u)

                for v in grafo[u]:
                    if v not in visitados:
                        visitados.append(v)
                        pilha.append(v)
                    if v == destino:
                        return visitados