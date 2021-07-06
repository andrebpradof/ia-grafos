from Vertice import Vertice
from Aresta import Aresta


class Grafo:
    def __init__(self, direcionado=False):
        self.lista_Vertices = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_Vertice(self, vertice):
        self.lista_Vertices.append(vertice)

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i.getVertice()
        else:
            return None

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            origem_aux.addAresta(Aresta(destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

    def busca_Aresta(self, origem, destino):
        vertice = self.busca_Vertice(origem)
        for aux in vertice.getListaArestas():
            if(destino == aux.getDestino().getId()):
                return True
        return False

    def imprime_grafo(self):
        aux = "oi"
        for vertice in self.lista_Vertices:
            aux = ""+str(vertice.getId())+"->"
            for aresta in vertice.getListaArestas():
                aux += ""+str(aresta.getDestino().getId())+" - "
            print(aux)

    

   
