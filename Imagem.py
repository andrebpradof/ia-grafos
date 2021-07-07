import networkx as netx
import matplotlib.pyplot as plt
import numpy as np

class Imagem():
    def start(grafo, numVertices, caminho, inicio, fim, nome_img):

        pontos = netx.Graph()
        percurso = netx.Graph()
        alvo = netx.Graph()

        m = np.zeros((numVertices, numVertices))

        for i in range(numVertices):
            for a in grafo.lista_Vertices[i].getListaArestas():
                v = a.getDestino().getId()
                m[i][v] = a.getPeso()

        for i in range(numVertices):
            for j in range(numVertices):
                if m[i][j] != 0:
                    pontos.add_edge(i,j,weight=m[i][j])
             
        for i in range(len(caminho)-1):
            percurso.add_edge((caminho[i]),(caminho[i+1]),weight=m[caminho[i]][caminho[i+1]])


        alvo.add_node(inicio)
        alvo.add_node(fim)    

        fig = plt.figure()
        ax = fig.add_subplot(111)

        coordenadas = {}

        for i in range(numVertices):
            coordenadas[(i)] = [grafo.lista_Vertices[i].getX(), grafo.lista_Vertices[i].getY()]

        netx.draw_networkx(pontos,alpha=0.6,node_size=10, with_labels=False,pos=coordenadas, font_size=8, node_color="gray",edge_color="gray", ax=ax, width = 1)
        netx.draw_networkx(percurso,alpha=0.6,node_size=20, with_labels=False,pos=coordenadas, font_size=8, node_color="b", edge_color="b", ax=ax, width = 3)
        netx.draw_networkx(alvo,alpha=0.6,node_size=70, with_labels=True,pos=coordenadas, node_color="g", font_size=10, ax=ax, width = 3)

        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

        plt.savefig(nome_img)
        plt.show()