from Modelo_Grafo import Grafo
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

"""
['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']
---------------------------------
[("A", "B", 8), ("A", "D", 5), ("A", "E", 4),
 ("B", "C", 3), ("B", "F", 4), ("B", "E", 4),
 ("C", "F", 6), ("C", "G", 7), 
 ("D", "E", 1),("D", "I", 2), ("D", "H", 3), 
 ("E", "F", 3), ("E", "I", 2), 
 ("F", "G", 1), ("F", "K", 14), ("F", "I", 3), 
 ("G", "K", 2), ("G", "L", 3), 
 ("H", "I", 11), ("H", "M", 6), 
 ("I", "K", 6), ("I", "P", 15), ("I", "N", 2), ("I", "M", 5), 
 ("K", "L", 8), ("K", "P", 3), 
 ("L", "P", 6), 
 ("M", "N", 1), 
 ("N", "P", 13)]

def prim(G, vi):
    visitados = []
    verticesRest = G.vertice
    pesos = [a[3] for a in G.pesos]
    INFINITO = 10 * max(pesos)
    matrizPonderada = [[INFINITO] * len(G.vertice) for i in range(len(vertice))]
    visitados.append(vi)
    verticesRest.remove(vi)
    for i in range(len(G.vertices)):

# Mi estilo
def prim(G, vi):
    visitados = []
    verticesRest = G.vertice
    pesos = [a[3] for a in G.pesos]
    INFINITO = 10 * max(pesos)
    matrizPonderada = [[INFINITO] * len(G.vertice) for i in range(len(vertice))]
    visitados.append(vi)
    verticesRest.remove(vi)
    for i in range(len(G.vertices)):
"""


#Sin matriz de adyacencia
def prim(G, vi): #La funcion toma como argumentos un grafo y un vertice
    pesos = nx.get_edge_attributes(G,"weight")
    """crea un diccionario usando como clave las aristas, definidas como tuplas, y como valores sus respectivos pesos"""
    
    #pesos = [[(a[0],a[1]): a[2]] for a in G.pesos]
    
    INFINITO = 10 * max(pesos.values()) # infinito es un numero mas grande que el mayor peso de las aristas
    cola, anterior = {}, {}
    """Crea dos diccionarios: una cola de prioridades y otro que define que vertice antecede a quien"""
    
    for v in G.vertice: # Inicializa la cola de prioridad y el diccinario de vertices respectivamente
        cola[u] = INFINITO
        vecino[u] = None
    
    cola[vi] = 0 # Asigna la maxima prioridad al vertice inicial
    porVisitar = G.vertice # Crea una lista con todos los vertices del grafo

    while porVisitar != list([]):
        u = min([[cola[v],v] for v in porVisitar])[1]
        # u es el vertice con mayor prioridad (con el valor de cola minimo)
        porVisitar.remove(u) # Elimina el vertice de la lista de vertices por visitar
        for v in G.vAdyacentes(u): #Recorre todas las aristas adyacentes
            a = (u,v) 
            if v in porVisitar and pesos[a] < cola[a]:
                # Si el vertice no ha sido visitado y tiene menor peso (y por tanto mayor prioridad)
                vecino[u] = v # el vertice sera vecino
                cola[a] = pesos[a] # y el peso de la arista sera el menor
        #Al final queda como vecino el vertice con la arista de menor ponderacion
    #Se repite con todos los vertices hasta que que no quede ninguno por visitar

    aristasArbol = [(v,vecino[v]) for v in G.vertice]  # Hace una lista de las aristas del grafo
    
    pesosArbol = []
    #Crea las aristas ponderadas del arbol
    for a in aristasArbol:
        if a in pesos:
            aristasArbol.append(pesos[a])
        if (a[1],a[0]) in pesos:
            aristasArbol.append(pesos[(a[1]),a[0]]
    return pesosArbol #Retorna las aristas del arbol con su ponderacion


    def generar_figura_prim(self):
        """Genera la figura del Árbol de Expansión Mínimo (Prim) para mostrar en Tkinter."""
        mst = nx.Graph()
        mst.add_weighted_edges_from(prim(G,vi))
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
        ax.set_title("Árbol de Expansión Mínimo (Prim)")
        ax.axis("off")
        return fig


"""
def prim(G: Grafo , pesos)
    # pre: pesos un diccionario donde las claves son las aristas y los valores son reales no negativos. 
    # post: devuelve mst un MST de G. 
    r = next(iter(G.vertices())) # toma un vértice de G sin quitarlo
    clave, padre = {}, {} # dos diccionarios vacíos. El primero es una "cola de prioridad". El segundo indicará quien será el padre en el MST.
    INFINITO = 2 * max(pesos.values()) # INFINITO es un valor más alto que todos los pesos
    for u in G.vertices():
        clave[u] = INFINITO 
        padre[u] = None # Cuando el algoritmo termina padre[v] será el padre de v en el MST, para los v que no son raíz (el vértice r). 
    clave[r] = 0
    cola = G.vertices()
    while cola != set({}):
        u = min([[clave[v],v] for v in cola])[1] # un vértice de cola con clave[u] mínima
        cola.remove(u)
        for v in G.adyacentes(u):
            e = frozenset({u, v})
            if v in cola and pesos[e] < clave[v]:
                padre[v] = u
                clave[v] = pesos[e]
    mst = Grafo(G.vertices(), set({})) # este va a ser el MST. Se inicializa como un grafo con todos los vértices de G y si aristas. 
    for v in mst.vertices() - {r}:
        mst.agregar_arista(frozenset({v,padre[v]}))
    return mst
"""