
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure # Importamos Figure para usarla explícitamente
# Un digrafo tiene como atributos un conjunto de vertices y un conjunto de 
# aristas que los unen. Pero a demas existe una funcion de 
# incidencia asigna a cada par de vertices, al menos una arista, o tambien se puede decir
# que a una arista se le asigna un par ordenado de vertices.

class Digrafo:
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.pesos = {} 
        # Los pesos estan en un diccionario con tuplas (u,v) como llaves 
        # del diccionario, ahora, es un diccionario por que para asignarle 
        # el peso de una arista, la misma debe asociarse a dos vertices 
        # "inicial y final". Mientras que los vertices y aristas son 
        # listas, por que solo se necesita almacenar los elementos.
        
    # Funcion para agregar vertices a el array de vertices
    def agregar_vertice(self): 
        numVertices = int(input("Ingrese el numero de vertices que desea agregar: "))
        for i in range(numVertices):
            v = input("Ingrese el nombre del vertice: ")
            if v not in self.vertices:
                self.vertices.append(v)
            else:
                print("El vertice ya existe")
        
        print(self.vertices)
        return self.vertices
    
    #Angel


    # Funcion para agregar aristas a el array de aristas con su respectivo peso, y ademas se esta aplicando 
    # la funcion de incidencia, que hace corresponder a cada arista un par de vertices.
    def agregar_arista(self):
        while True:
            u = input("Ingrese el vértice inicial de la arista (o 'salir' para terminar): ")
            if u.lower() == 'salir':
                break
            v = input("Ingrese el vértice final de la arista: ")
            if u in self.vertices and v in self.vertices:
                peso = int(input("Ingrese el peso de la arista: "))
                self.aristas.append((u, v))

                # Agregar el peso a la lista correspondiente en el diccionario
                if (u, v) in self.pesos:
                    self.pesos[(u, v)].append(peso)
                else:
                    self.pesos[(u, v)] = [peso]

                print("Aristas actuales:", self.aristas)
                print("Pesos actuales:", self.pesos)
            else:
                print("Uno o ambos vértices no existen. Por favor, agréguelos primero.")
        return self.aristas, self.pesos
>>>>>>> 99516dfa8735a803a0692eeb9dba963e4271e623

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