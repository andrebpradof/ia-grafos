class Vertice():
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.visitado = False
        self.heuristica = 0
        self.lista_Arestas = []


    def setX(self, valor):
        self.x = valor
    
    def getX(self):
        return self.x

    def setY(self, valor):
        self.y = valor
    
    def getY(self):
        return self.y

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def getVertice(self):
        return self

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getListaArestas(self):
        return self.lista_Arestas

    def addAresta(self, aresta):
        self.lista_Arestas.append(aresta)

    def setHeuristica(self,valor):
        self.heuristica = valor

    def getHeuristica(self):
        return self.heuristica