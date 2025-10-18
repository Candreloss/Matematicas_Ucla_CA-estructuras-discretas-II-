from Digrafo import Grafo

# Implementar un clase Grafo donde los vértices es un conjunto y las aristas es un conjunto de 2-subconjuntos de vértices.
# Los 2-subconjuntos se implementan con frozenset({v, w}) si v, w vértices (pues Python no admite conjuntos de conjuntos)
# Las funciones y métodos son los obvios. Si G es grafo:
#     G.vertices(): es el conjunto de vértices
#     G.aristas(): es el conjunto de aristas
#     G.adyacentes(v): es el conjunto de vértices adyacentes a un vértice v
#     G.agregar_arista(e): agrega la arista e

# vi = vertice inicial

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
def prim(G, vi):
    visitados = []
    pesos = [[(a[0],a[1]): a[2]] for a in G.pesos]
    INFINITO = 10 * max(pesos)
    cola, anterior = {}, {}
    for v in G.vertice:
        cola[u] = INFINITO
        anterior[u] = None
    cola[vi] = 0
    porVisitar = G.vertice
    while porVisitar != set({}):
        u = min([cola[v],v for v in porVisitar])[1]
        porVisitar.remove(u)
        for v in G.vAdyacentes(u):
            e = (u,v)
            if v in porVisitar and pesos[e] < cola[e]:
                anterior[u] = v
                cola[e] = pesos[e]
    arbol = Grafo()
    aristasArbol = [(v,anterior[v]) for v in G.vertice]
    pesosArbol = []
    for a in aristasArbol:
        if a in pesos:
            aristasArbol.append(pesos[a])
        if (a[1],a[0]) in pesos:
            aristasArbol.append(pesos[(a[1]),a[0]]
    
    return pesosArbol

        

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