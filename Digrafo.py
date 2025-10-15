import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, di=False):
        if di:
            self.G= nx.Digraph()
        else:
            self.G= nx.Graph()
        self.vertice = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']
        self.peso = [("A", "B", 8), ("A", "D", 5), ("A", "E", 4), ("B", "C", 3), ("B", "F", 4), ("B", "E", 4), ("C", "F", 6), ("C", "G", 7), ("D", "E", 1), ("D", "I", 2), ("D", "H", 3), ("E", "F", 3), ("E", "I", 2), ("F", "G", 1), ("F", "K", 14), ("F", "I", 3), ("G", "K", 2), ("G", "L", 3), ("H", "I", 11), ("H", "M", 6), ("I", "K", 6), ("I", "P", 15), ("I", "N", 2), ("I", "M", 5), ("K", "L", 8), ("K", "P", 3), ("L", "P", 6), ("M", "N", 1), ("N", "P", 13)]
        self.pos= {'A': (0, 0), 'B': (0, 0), 'C': (0, 0), 'E': (0, 0), 'D': (0, 0), 'F': (0, 0), 'G': (0, 0), 'H': (0, 0),  'I': (0, 0), 'K': (0, 0), 'L': (0, 0), 'M': (0, 0), 'N': (0, 0), 'P': (0, 0)}
        self.G.add_nodes_from(self.vertice)
        self.G.add_weighted_edges_from(self.peso)
        # Los pesos estan en un diccionario con tuplas (u,v) como llaves 
        # del diccionario, ahora, es un diccionario por que para asignarle 
        # el peso de una arista, la misma debe asociarse a dos vertices 
        # "inicial y final". Mientras que los vertices y aristas son 
        # listas, por que solo se necesita almacenar los elementos.
    
def agregar_vertice (G, vertice):
        G.add_nodes_from(vertice)

def agregar_arista(G, u, v, p=0):
    G.add_edge(u, v, peso=p)

if __name__ == "__main__":
    grafo = Grafo()
   
    pos = nx.spring_layout(grafo.G, seed=100, k=0.5, iterations=100)
        
    plt.figure(figsize=(10,6))
    nx.draw(
            grafo.G, 
            pos=pos, 
            with_labels=True, 
            node_color="skyblue", 
            node_size=1200, 
            font_weight="bold"
        )
        
        # Mostrar los pesos de las aristas
    labels = nx.get_edge_attributes(grafo.G, 'weight')  # ojo, es 'weight'
    nx.draw_networkx_edge_labels(grafo.G, pos, edge_labels=labels)
        
    plt.title("Grafo con NetworkX")
    plt.show()
