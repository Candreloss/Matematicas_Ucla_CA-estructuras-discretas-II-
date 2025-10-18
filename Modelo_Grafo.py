import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure # Importamos Figure para usarla explícitamente
# Un digrafo tiene como atributos un conjunto de vertices y un conjunto de 
# aristas que los unen. Pero a demas existe una funcion de 
# incidencia asigna a cada par de vertices, al menos una arista, o tambien se puede decir
# que a una arista se le asigna un par ordenado de vertices.

class Grafo:
    def __init__(self):
        
        self.G= nx.Graph()
        self.vertice = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']
        self.peso = [("A", "B", 8), ("A", "D", 5), ("A", "E", 4), ("B", "C", 3), ("B", "F", 4), ("B", "E", 4), ("C", "F", 6), ("C", "G", 7), ("D", "E", 1), ("D", "I", 2), ("D", "H", 3), ("E", "F", 3), ("E", "I", 2), ("F", "G", 1), ("F", "K", 14), ("F", "I", 3), ("G", "K", 2), ("G", "L", 3), ("H", "I", 11), ("H", "M", 6), ("I", "K", 6), ("I", "P", 15), ("I", "N", 2), ("I", "M", 5), ("K", "L", 8), ("K", "P", 3), ("L", "P", 6), ("M", "N", 1), ("N", "P", 13)]
        self.pos= {'A': (-100, 150),'B': (10, 225), 'C': (80, 305), 'D': (-15, 50), 'E': (85, 150), 'F': (160, 225), 'G': (230, 305), 'H': (141.26, 10), 'I': (300, 100), 'K': (310, 225), 'L': (380, 305), 'M': (280, 20), 'N': (450, 80), 'P': (460, 225) }
        self.G.add_nodes_from(self.vertice)
        self.G.add_weighted_edges_from([(u, v, p) for (u, v, p) in self.peso])
        # Los pesos estan en un diccionario con tuplas (u,v) como llaves 
        # del diccionario, ahora, es un diccionario por que para asignarle 
        # el peso de una arista, la misma debe asociarse a dos vertices 
        # "inicial y final". Mientras que los vertices y aristas son 
        # listas, por que solo se necesita almacenar los elementos.
    
    # --- NUEVO MÉTODO PARA GENERAR LA FIGURA ---
    def generar_figura_matplotlib(self):
            grafo= self
            # Creamos una figura de Matplotlib (no usamos plt.figure() directamente)
            fig = Figure(figsize=(4.6, 3.4), dpi=100) # El figsize se ajusta al tamaño de tu frame (460x344 / 100 dpi)
            ax = fig.add_subplot(111) # Añadimos un sub-gráfico

            # Determinación de las posiciones
                
            # Dibujar el grafo
            nx.draw(
                grafo.G, 
                pos=grafo.pos, 
                ax=ax, # ¡Importante! Dibujar en el sub-gráfico 'ax'
                with_labels=True, 
                node_color="#8585f7", # Color azul que se acerca a tu esquema
                node_size=300, 
                font_size=8,
                font_weight="bold",
                font_color="black"
            )
                
            # Mostrar los pesos de las aristas
            labels = nx.get_edge_attributes(grafo.G, 'weight')
            nx.draw_networkx_edge_labels(grafo.G, grafo.pos, edge_labels=labels, ax=ax)
                
            ax.set_title("Grafo de la Red") # Establecer el título
            ax.axis('off') # Ocultar los ejes de Matplotlib
            
            # Devolvemos el objeto Figure
            return fig
    
    def agregar_vertice (self, vertice, pos=None):
        self.G.add_node(vertice)
        self.vertice.append(vertice)
        if pos:
             self.pos[vertice]= pos


    def agregar_arista(self, u, v, p=0):
        self.G.add_edge(u, v, weight=p)
        self.peso.append((u, v, p))

    def ordenar_por_peso(self):
        """Devuelve una lista de aristas (u, v, peso) ordenadas por peso ascendente."""
        return sorted([(u, v, d['weight']) for u, v, d in self.G.edges(data=True)], key=lambda x: x[2])

    def conexion_vertice(self, arbol, origen, destino):
        """Determina si ya existe un camino entre 'origen' y 'destino' dentro del árbol parcial."""
        if origen == destino:
            return True

        adyacencia = {}
        for u, v, _ in arbol:
            adyacencia.setdefault(u, []).append(v)
            adyacencia.setdefault(v, []).append(u)

        visitado = set()
        pendientes = [origen]
        cabeza = 0

        while cabeza < len(pendientes):
            actual = pendientes[cabeza]
            cabeza += 1

            if actual == destino:
                return True

            visitado.add(actual)
            for vecino in adyacencia.get(actual, []):
                if vecino not in visitado and vecino not in pendientes:
                    pendientes.append(vecino)

        return False

    def kruskal(self):
        """Implementa el algoritmo de Kruskal sin funciones automáticas de NetworkX."""
        lista_ordenada = self.ordenar_por_peso()
        arbol = []

        if not lista_ordenada:
            return arbol

        vertices = set()
        for u, v, _ in lista_ordenada:
            vertices.add(u)
            vertices.add(v)

        n_vertices = len(vertices)

        for u, v, peso in lista_ordenada:
            if len(arbol) >= n_vertices - 1:
                break
            if self.conexion_vertice(arbol, u, v):
                continue
            arbol.append((u, v, peso))
        return arbol

    def generar_figura_kruskal(self):
        """Genera la figura del Árbol de Expansión Mínimo (Kruskal) para mostrar en Tkinter."""
        arbol = self.kruskal()
        import networkx as nx
        from matplotlib.figure import Figure

        mst = nx.Graph()
        mst.add_weighted_edges_from(arbol)
        pos = nx.spring_layout(mst, seed=42)

        fig = Figure(figsize=(4.6, 3.4), dpi=100)
        ax = fig.add_subplot(111)

        nx.draw(
            mst, pos, ax=ax,
            with_labels=True,
            node_color="#80bfff",
            node_size=500,
            font_size=9,
            font_weight="bold"
        )

        edge_labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, ax=ax)
        ax.set_title("Árbol de Expansión Mínimo (Kruskal)")
        ax.axis("off")
        return fig
""""
def agregar_vertice(self, vertice): # Cambiado para ser método de instancia
        self.G.add_nodes_from(vertice)

def agregar_arista(self, u, v, p=0): # Cambiado para ser método de instancia
        self.G.add_edge(u, v, weight=p)

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
    labels = nx.get_edge_attributes(grafo.G, 'weight') 
    nx.draw_networkx_edge_labels(grafo.G, pos, edge_labels=labels)
        
    plt.title("Grafo con NetworkX")
    plt.show()    
    
"""
    

if __name__ == "__main__":
    # La sección __main__ ahora utiliza el nuevo método para probarlo (opcional)
    grafo = Grafo()
    fig = grafo.generar_figura_matplotlib()
    plt.show()
