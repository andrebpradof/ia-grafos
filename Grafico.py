from igraph import *


class Grafico():
    def start(grafo, numVertices, inicio, fim, caminho, nome_img):
        
        weights = []
        edges = []

        color = [ 0 for i in range(numVertices) ]
        color_es = []

        g = Graph(directed=False)
        g.add_vertices(numVertices)

        # Add ids and labels to vertices
        for i in range(len(g.vs)):
            g.vs[i]["id"]= i
            g.vs[i]["label"]= str(i)

            if i in caminho:
                color[i] = 'red'
            else:
                color[i] = 'blue'

            if i == inicio or i == fim:
                color[i] = 'green'
        
        g.vs['color'] = color

        for i in range(numVertices):
            for a in grafo.busca_Vertice(i).getListaArestas():
                v = a.getDestino().getId()
                p = a.getPeso()
                if (v,i) not in edges:
                    edges.append((i,v))
                    weights.append(p)
                    color_es.append('red')
        
        g.add_edges(edges)
        g.es['weight'] = weights
        g.es['color'] = color_es
        
        visual_style = {}
        # Set bbox and margin
        visual_style["bbox"] = (2000,2000)
        visual_style["margin"] = 10

        # # Set vertex size
        # visual_style["vertex_size"] = 45
        # # Set vertex lable size
        # visual_style["vertex_label_size"] = 22
        # # Don't curve the edges
        # visual_style["edge_curved"] = False
        # # Set the layout
        #my_layout = g.layout_lgl()
        #visual_style["layout"] = my_layout
        # Plot the graph
        plot(g, nome_img, **visual_style)