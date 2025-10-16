import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure # Importamos Figure para usarla explícitamente
# Un digrafo tiene como atributos un conjunto de vertices y un conjunto de 
# aristas que los unen. Pero a demas existe una funcion de 
# incidencia asigna a cada par de vertices, al menos una arista, o tambien se puede decir
# que a una arista se le asigna un par ordenado de vertices.

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

class Grafo:
    def __init__(self, di=False):
        if di:
            self.G = nx.DiGraph()
        else:
            self.G = nx.Graph()
            
        self.vertice = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']
        self.peso = [("A", "B", 8), ("A", "D", 5), ("A", "E", 4), ("B", "C", 3), ("B", "F", 4), ("B", "E", 4), ("C", "F", 6), ("C", "G", 7), ("D", "E", 1), ("D", "I", 2), ("D", "H", 3), ("E", "F", 3), ("E", "I", 2), ("F", "G", 1), ("F", "K", 14), ("F", "I", 3), ("G", "K", 2), ("G", "L", 3), ("H", "I", 11), ("H", "M", 6), ("I", "K", 6), ("I", "P", 15), ("I", "N", 2), ("I", "M", 5), ("K", "L", 8), ("K", "P", 3), ("L", "P", 6), ("M", "N", 1), ("N", "P", 13)]
        
        self.G.add_nodes_from(self.vertice)
        self.G.add_weighted_edges_from(self.peso)
    
    def getPeso(self):
        return self.peso
    
    def agregar_vertice(self, vertice): # Cambiado para ser método de instancia
        self.G.add_nodes_from(vertice)

    def agregar_arista(self, u, v, p=0): # Cambiado para ser método de instancia
        self.G.add_edge(u, v, weight=p)

    
    
    
    
    # --- NUEVO MÉTODO PARA GENERAR LA FIGURA ---
    def generar_figura_matplotlib(self):
        # Creamos una figura de Matplotlib (no usamos plt.figure() directamente)
        fig = Figure(figsize=(4.6, 3.4), dpi=100) # El figsize se ajusta al tamaño de tu frame (460x344 / 100 dpi)
        ax = fig.add_subplot(111) # Añadimos un sub-gráfico

        # Determinación de las posiciones
        pos = nx.spring_layout(self.G, seed=100, k=0.5, iterations=100)
            
        # Dibujar el grafo
        nx.draw(
            self.G, 
            pos=pos, 
            ax=ax, # ¡Importante! Dibujar en el sub-gráfico 'ax'
            with_labels=True, 
            node_color="#8585f7", # Color azul que se acerca a tu esquema
            node_size=800, 
            font_weight="bold",
            font_color="black"
        )
            
        # Mostrar los pesos de las aristas
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, ax=ax)
            
        ax.set_title("Grafo de la Red") # Establecer el título
        ax.axis('off') # Ocultar los ejes de Matplotlib
        
        # Devolvemos el objeto Figure
        return fig

if __name__ == "__main__":
    # La sección __main__ ahora utiliza el nuevo método para probarlo (opcional)
    grafo = Grafo()
    fig = grafo.generar_figura_matplotlib()
    plt.show()
