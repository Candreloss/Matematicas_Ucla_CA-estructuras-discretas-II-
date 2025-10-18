import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure # Importamos Figure para usarla explícitamente
# Un digrafo tiene como atributos un conjunto de vertices y un conjunto de 
# aristas que los unen. Pero a demas existe una funcion de 
# incidencia asigna a cada par de vertices, al menos una arista, o tambien se puede decir
# que a una arista se le asigna un par ordenado de vertices.

class Grafo:
    #Creamos la clase Grafo, quien será la instancia de las futuras maravillas que verán :D
    def __init__(self):
        
        self.G= nx.Graph()
        self.vertice = ['A', 'B', 'C', 'E', 'D',
                        'F', 'G', 'H',  'I', 'K',
                        'L', 'M', 'N', 'P']
        self.peso = [("A", "B", 8), ("A", "D", 5),
                     ("A", "E", 4), ("B", "C", 3),
                     ("B", "F", 4), ("B", "E", 4),
                     ("C", "F", 6), ("C", "G", 7),
                     ("D", "E", 1), ("D", "I", 2),
                     ("D", "H", 3), ("E", "F", 3),
                     ("E", "I", 2), ("F", "G", 1),
                     ("F", "K", 14), ("F", "I", 3),
                     ("G", "K", 2), ("G", "L", 3),
                     ("H", "I", 11), ("H", "M", 6),
                     ("I", "K", 6), ("I", "P", 15),
                     ("I", "N", 2), ("I", "M", 5),
                     ("K", "L", 8), ("K", "P", 3),
                     ("L", "P", 6), ("M", "N", 1),
                     ("N", "P", 13)]
        self.pos= {'A': (-100, 150),'B': (10, 225),
                   'C': (80, 305), 'D': (-15, 50),
                   'E': (85, 150), 'F': (160, 225),
                   'G': (230, 305), 'H': (141.26, 10),
                   'I': (300, 100), 'K': (310, 225),
                   'L': (380, 305), 'M': (280, 20),
                   'N': (450, 80), 'P': (460, 225) }
        
         # Los pesos estan en un diccionario con tuplas (u,v) como llaves 
        # del diccionario, ahora, es un diccionario por que para asignarle 
        # el peso de una arista, la misma debe asociarse a dos vertices 
        # "inicial y final". Mientras que los vertices y aristas son 
        # listas, por que solo se necesita almacenar los elementos.

        self.G.add_nodes_from(self.vertice) #Cargamos los vértices al grafo
        self.G.add_weighted_edges_from([(u, v, p) for (u, v, p) in self.peso]) #Añadimos las aristas con sus pesos
        self.dirigido = self.G.is_directed()
       
    
    # --- Método para generar la figura del grafo ---
    def generar_figura_matplotlib(self):
            grafo= self
            fig = Figure(figsize=(4.6, 3.4), dpi=100) # El figsize se ajusta al tamaño del frame 
            ax = fig.add_subplot(111) # Añadimos un sub-gráfico
                
            # Dibujar el grafo
            nx.draw(
                grafo.G, 
                pos=grafo.pos, 
                ax=ax, # Dibujamos en el sub-gráfico 'ax'
                with_labels=True, 
                node_color="#8585f7", # Color azul bonito :3
                node_size=300, 
                font_size=8,
                font_weight="bold",
                font_color="black"
            )
                
            # Mostramos los pesos de las aristas
            labels = nx.get_edge_attributes(grafo.G, 'weight')
            nx.draw_networkx_edge_labels(grafo.G, grafo.pos, edge_labels=labels, ax=ax)
                
            ax.set_title("Grafo de la Red") # Título
            ax.axis('off') # Ocultar los ejes de Matplotlib
            
            return fig
    
    def agregar_vertice (self, vertice, pos=None): #Funcion para agregar vértices, nos ayudarán más adelante para modificaciones del grafo
        self.G.add_node(vertice)
        self.vertice.append(vertice)
        if pos:
             self.pos[vertice]= pos


    def agregar_arista(self, u, v, p=0): #Funcion para agregar aristas, nos ayudarán más adelante para modificaciones del grafo
        self.G.add_edge(u, v, weight=p)
        self.peso.append((u, v, p))

    def ordenar_por_peso(self):
        # Ordena una lista de aristas por su tercer elemento (peso).
        # Entrada esperada: lista de tuplas (u, v, peso)
        # Devuelve: lista ordenada ascendentemente por peso
        lista_aristas = []
        for u, v, datos in self.G.edges(data=True):
            peso = datos.get("weight", datos.get("peso", 0))
            lista_aristas.append((u, v, peso))
        lista_ordenada = sorted(lista_aristas, key=lambda x: x[2])
        return lista_ordenada

    def conexion_vertice(self, arbol, origen, destino):
        
        if origen == destino:
            return True
        
        adyacencia = {} 
        for u, v, _ in arbol:
            adyacencia.setdefault(u, []).append(v)
            adyacencia.setdefault(v, []).append(u) 
        # asigna por defecto una lista vacía si la clave no existe
        visitado = set()
        # NOTA. set() convierte a una lista en un conjunto (sin elementos repetidos)
        
        pendientes = [origen] # Vertices por visitar (cola) o podriamos decir tambien que 
                              # son los vertices ya estan descubiertos pero aun no hemos 
                              # pasado por alli.
        cabeza = 0 # Indice de la cabeza de la cola (pendientes)
        
        while cabeza < len(pendientes): #Se asegura que la cola no este vacia
            vertice_actual = pendientes[cabeza]
            cabeza += 1 # Incrementa la cabeza, todo esto es para evitar que mas adelante
                        # Eliminemos el elemento que acabamos de ingresar en esa posicion
                        # De hecho, esa es la razon de "cabeza" desde que se declara 
                        # la variable arriba
            
            if vertice_actual == destino:
                return True
            
            visitado.add(vertice_actual) # Ahora agregamos el vertice a la lista de visitados
            
            # Luego verificamos que el vertice vecino no haya sido visitado y que
            # no este en la cola aun, en ese caso lo agregamos a la cola
            for vecino in adyacencia.get(vertice_actual, []):
                if vecino not in visitado and vecino not in pendientes: 
                    pendientes.append(vecino)  
        
        return False


    def kruskal(self):
        
        # Implementación sencilla de Kruskal:
        # Realizar un árbol con la lista de aristas seleccionadas.
        # Añadir aristas en orden creciente de peso siempre que no creen ciclo.
        # Para la detección de ciclos se usa networkx.has_path sobre un grafo temporal
        # construido con las aristas ya seleccionadas (g_temp).
        
        lista_ordenada = self.ordenar_por_peso()
        arbol = []  # lista donde guardaremos las aristas del MST parcial

        # Si no hay aristas, devolvemos la lista vacía inmediatamente
        if not lista_ordenada:
            return arbol

        # Obtener el conjunto de vértices a partir de la lista de aristas.
        # Esto nos permite conocer n (número de vértices).
        vertices = set()
        for u, v, _ in lista_ordenada:
            vertices.add(u)
            vertices.add(v)
        n_vertices = len(vertices) # número total de vértices

        # Recorremos las aristas ordenadas por peso y las intentamos añadir al arbol
        for u, v, peso in lista_ordenada:
            # condición de parada: un árbol con n vértices tiene exactamente n-1 aristas
            if len(arbol) >= n_vertices - 1:
                break

            # Construimos un grafo temporal con las aristas que ya hemos seleccionado.
            # NOTA: esto se crea cada iteración; es simple y claro aunque no es la solución más eficiente.
            
            if self.conexion_vertice(arbol, u, v): 
                continue
            arbol.append((u, v, peso))

        return arbol


    # --- Función para graficar el árbol resultante (MST) usando matplotlib ---
    def generar_figura_kruskal(self):

        self.validar_grafo()

        arbol = self.kruskal()
        Arbol_optimo = nx.Graph()

        # Si la instancia del grafo tiene atributo 'vertice', se usa para añadir nodos
        if hasattr(self, "vertice"):
            Arbol_optimo.add_nodes_from(self.vertice)
        else:
            # Si no, infiere nodos de las aristas del árbol
            nodos = set()
            for u, v, _ in arbol:
                nodos.add(u)
                nodos.add(v)
            Arbol_optimo.add_nodes_from(nodos)

        # Añadimos las aristas (con peso) al grafo que vamos a dibujar
        Arbol_optimo.add_weighted_edges_from(arbol)

        # Usamos las posiciones originales del grafo base si existen
        pos = getattr(self, "pos", None)
        if not pos:
            pos = nx.spring_layout(Arbol_optimo, seed=42)

        # Creamos figura y dibujamos nodos y etiquetas
        fig = Figure(figsize=(4.6, 3.4), dpi=100)
        ax = fig.add_subplot(111)
        nx.draw(Arbol_optimo, pos,
                with_labels=True, 
                node_color="#8585f7", 
                node_size=300, 
                font_size=8,
                font_weight="bold",
                font_color="black",
                ax=ax)

        # Dibujamos etiquetas de pesos en las aristas
        edge_labels = nx.get_edge_attributes(Arbol_optimo, 'weight')
        nx.draw_networkx_edge_labels(Arbol_optimo, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        ax.set_title("Árbol resultante (Kruskal)")
        ax.axis('off')

        return fig
    
    def dfs(self, inicio):
        #Extiende Grafo con un método dfs() que devuelve
        #un diccionario hijo->padre (árbol DFS).
        if inicio not in self.G:
            raise KeyError(f"El nodo '{inicio}' no existe en el grafo.")
        visited = set()
        parent = {n: None for n in self.G.nodes()}
        stack = [inicio]
        visited.add(inicio)
        parent[inicio] = None

        while stack:
            u = stack.pop()
            # iterar vecinos en orden determinista
            for v in sorted(self.G.neighbors(u)):
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    stack.append(v)
        return parent

    def generar_figura_dfs(self, arbol_dfs, frame_destino):
        
        #Dibuja solo el árbol DFS, sin las aristas extra del grafo original.
        #arbol_dfs: diccionario {hijo: padre}
        #frame_destino: Frame de Tkinter donde se dibuja la figura
        self.validar_grafo()

        # Crear grafo temporal solo con nodos y aristas DFS
        tree_edges = [(padre, hijo) for hijo, padre in arbol_dfs.items() if padre is not None]
        arbol = nx.DiGraph() if self.dirigido else nx.Graph()
        arbol.add_nodes_from(self.G.nodes())  # mantener todos los nodos visibles
        arbol.add_edges_from(tree_edges)

            # Extraer los pesos de las aristas originales
        for u, v in tree_edges:
            if self.G.has_edge(u, v):
                arbol[u][v]['weight'] = self.G[u][v].get('weight', 1)
            else:
                arbol[u][v]['weight'] = 1  # valor por defecto si algo falla


        # Posiciones (usamos las mismas que el grafo original si existen)
        pos = getattr(self, "pos", None)

        # Crear figura
        fig = Figure(figsize=(4.6, 3.4), dpi=100)
        ax = fig.add_subplot(111)

        # Dibujar solo el árbol DFS
        nx.draw(arbol, pos,
                ax=ax,
                with_labels=True,
                node_size=300,
                node_color="#8585f7",
                font_size=8,
                font_weight="bold",
                font_color="black",
                arrows=self.dirigido)
        
        edge_labels = nx.get_edge_attributes(arbol, 'weight')
        nx.draw_networkx_edge_labels(arbol, pos, edge_labels=edge_labels, font_size=8, ax=ax)


        ax.set_title("Árbol DFS generado")
        ax.axis('off')

        # Mostrar en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_destino)
        canvas.draw()
        widget_grafo = canvas.get_tk_widget()
        widget_grafo.pack(fill="both", expand=True)

    def bfs(self, inicio):
        
        #Extiende Grafo con un método bfs() que devuelve
        #un diccionario hijo->padre (árbol BFS) y un dict de niveles.
        # Construimos adyacencias a partir del grafo NetworkX
        adj = {n: list(self.G.neighbors(n)) for n in self.G.nodes()}
        if inicio not in adj:
            raise KeyError(f"El nodo '{inicio}' no existe en el grafo.")

        visitado = set([inicio])
        parent = {inicio: None}
        node_level = {inicio: 0}
        pendientes = [inicio]
        cabeza = 0
        tree_edges = []

        while cabeza < len(pendientes):
            nodo = pendientes[cabeza]
            cabeza += 1
            for vecino in sorted(adj.get(nodo, [])):  # orden determinista
                if vecino not in visitado:
                    visitado.add(vecino)
                    pendientes.append(vecino)
                    parent[vecino] = nodo
                    node_level[vecino] = node_level[nodo] + 1
                    tree_edges.append((nodo, vecino))
        return parent, node_level, tree_edges


    def generar_figura_bfs(self, tree_edges, node_level, frame_destino, mostrar_nombres=True):
        
        #Dibuja el árbol BFS en Tkinter con el mismo estilo que DFS.
        #- tree_edges: lista de (padre, hijo)
        #- node_level: dict {nodo: nivel} (no se usa para la posición, solo para info)
        #- frame_destino: Frame de Tkinter donde se mostrará

        self.validar_grafo()
        # Crear grafo temporal solo con nodos y aristas BFS
        arbol_bfs = nx.DiGraph() if getattr(self, "dirigido", False) else nx.Graph()
        arbol_bfs.add_nodes_from(self.G.nodes())  # mantener todos los nodos visibles
        arbol_bfs.add_edges_from(tree_edges)

        # Extraer los pesos de las aristas originales
        for u, v in tree_edges:
            if self.G.has_edge(u, v):
                arbol_bfs[u][v]['weight'] = self.G[u][v].get('weight', 1)
            else:
                arbol_bfs[u][v]['weight'] = 1  # valor por defecto

        # Posiciones (reproducibles como DFS)
        pos = getattr(self, "pos", None)

        # Crear figura
        fig = Figure(figsize=(4.6, 3.4), dpi=100)
        ax = fig.add_subplot(111)

        # Dibujar nodos y aristas
        nx.draw(arbol_bfs, pos,
                ax=ax,
                with_labels=mostrar_nombres,
                node_size=300,
                node_color="#8585f7",
                font_size=8,
                font_weight="bold",
                font_color="black",
                arrows=getattr(self, "dirigido", False))

        # Dibujar etiquetas de peso
        edge_labels = nx.get_edge_attributes(arbol_bfs, 'weight')
        nx.draw_networkx_edge_labels(arbol_bfs, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        ax.set_title("Árbol BFS generado")
        ax.axis('off')

        # Mostrar en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_destino)
        canvas.draw()
        widget_grafo = canvas.get_tk_widget()
        widget_grafo.pack(fill="both", expand=True)


    def prim(self, vertice_inicial):
        
        #Algoritmo de Prim para obtener el Árbol de Expansión Mínimo (MST).
        #Devuelve una lista de aristas ponderadas [(u, v, peso), ...].

        

        # --- Inicialización ---
        visitados = set()
        aristas_resultado = []
        pesos = nx.get_edge_attributes(self.G, "weight")

        if vertice_inicial not in self.G:
            raise ValueError(f"El vértice inicial '{vertice_inicial}' no existe en el grafo.")

        visitados.add(vertice_inicial)

        # --- Bucle principal ---
        while len(visitados) < self.G.number_of_nodes():
            # Buscar la arista de menor peso entre los nodos visitados y no visitados
            arista_min = None
            peso_min = float("inf")

            for u in visitados:
                for v in self.G.neighbors(u):
                    if v not in visitados:
                        peso = self.G[u][v].get("weight", 1)
                        if peso < peso_min:
                            peso_min = peso
                            arista_min = (u, v, peso)

            if arista_min is None:
                # El grafo no es completamente conexo
                break

            aristas_resultado.append(arista_min)
            visitados.add(arista_min[1])

        return aristas_resultado


    def generar_figura_prim(self, vertice_inicial):
        
        #Genera y devuelve la figura del Árbol de Expansión Mínimo usando Prim,
        #para mostrar en un Frame de Tkinter.
        
        self.validar_grafo()

        aristas_prim = self.prim(vertice_inicial)
        if not aristas_prim:
            raise RuntimeError("No se pudo generar el árbol de Prim (grafo posiblemente no conexo).")

        mst = nx.Graph()
        mst.add_weighted_edges_from(aristas_prim)

        pos = getattr(self, "pos", None)
        if not pos:
            pos = nx.spring_layout(mst, seed=42)

        fig = Figure(figsize=(4.6, 3.4), dpi=100)
        ax = fig.add_subplot(111)

        nx.draw(
            mst, pos,
            ax=ax,
            with_labels=True,
            node_color="#8585f7",
            node_size=300,
            font_size=8,
            font_weight="bold",
            font_color="black"
        )

        edge_labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        ax.set_title("Árbol de Expansión Mínimo (Prim)")
        ax.axis("off")

        return fig
    
    def validar_grafo(self):
        
        #Valida las condiciones básicas antes de ejecutar un algoritmo.
        #Lanza RuntimeError con mensajes claros si algo no cumple.
        
        if self.G.number_of_nodes() == 0:
            raise RuntimeError("El grafo no tiene vértices. Agrega al menos uno antes de continuar.")

        if self.G.number_of_edges() == 0:
            raise RuntimeError("El grafo no tiene aristas. Agrega aristas antes de ejecutar el algoritmo.")

        if not nx.is_connected(self.G.to_undirected()):
            raise RuntimeError("El grafo no es conexo. Los algoritmos de árbol no se pueden aplicar.")