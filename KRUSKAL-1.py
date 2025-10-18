import networkx as nx                      # librería para grafos (usada aquí para detectar caminos/ciclos)
import matplotlib.pyplot as plt            # sólo se importa por si quieres dibujar el grafo más adelante
from Modelo_Grafo import Grafo                   # importa la clase Grafo definida en tu archivo digrafo.py

# Creamos una instancia del grafo definido en Digrafo.py.
# Se asume que Grafo.getPeso() devuelve una lista de tuplas (u, v, peso)
G = Grafo()

def ordenar_por_peso(aristas):
    # Ordena una lista de aristas por su tercer elemento (peso).
    # Entrada esperada: lista de tuplas (u, v, peso)
    # Devuelve: lista ordenada ascendentemente por peso
    lista_ordenada = sorted(aristas, key=lambda x: x[2])
    return lista_ordenada

# La funcion en esencia construye el arbol BFS porque va chequeando las
# conexiones vertice a vertice, si el vertice que queremos agregar, ya tiene
# una conexion con otro vertice del arbol, entonces se omite esa arista para no
# crear ciclos. Recibe como parametros el arbol (vacio, por el momento)
# El vertice de origen y el vertice final.
def conexion_vertice(arbol, origen, destino):
    
    if origen == destino:
        return True
    
    adyacencia = {} 
    for u, v, _ in arbol:
        adyacencia.setdefault(u, []).append(v)
        adyacencia.setdefault(v, []).append(u) 
    # asigna por defecto una lista vacía si la clave no existe
    visitado = set()
    # NOTAAAA. set() convierte a una lista en un conjunto (sin elementos repetidos)
    
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


def kruskal(lista_ordenada):
    
    
    
    # Implementación sencilla de Kruskal usando la lógica que venías aplicando:
    # - Mantener un 'arbol' (lista de aristas seleccionadas).
    # - Añadir aristas en orden creciente de peso siempre que no creen ciclo.
    # Para la detección de ciclos se usa networkx.has_path sobre un grafo temporal
    # construido con las aristas ya seleccionadas (g_temp).
    
    arbol = []                                # lista donde guardaremos las aristas del MST parcial

    # Si no hay aristas, devolvemos la lista vacía inmediatamente
    if not lista_ordenada:
        return arbol

    # Obtener el conjunto de vértices a partir de la lista de aristas.
    # Esto nos permite conocer n (número de vértices) sin depender de otras estructuras.
    vertices = set()
    for u, v, _ in lista_ordenada:
        vertices.add(u)
        vertices.add(v)
    n_vertices = len(vertices)                # número total de vértices

    # Recorremos las aristas ordenadas por peso y las intentamos añadir al arbol
    for u, v, peso in lista_ordenada:
        # condición de parada: un árbol con n vértices tiene exactamente n-1 aristas
        if len(arbol) >= n_vertices - 1:
            break

        # Construimos un grafo temporal con las aristas que ya hemos seleccionado.
        # NOTA: esto se crea cada iteración; es simple y claro aunque no es la solución más eficiente.
        
        if conexion_vertice(arbol, u, v): 
            continue
        arbol.append((u, v, peso))

    return arbol

# --- NUEVO: función para graficar el árbol resultante (MST) usando matplotlib ---
def plot_arbol(arbol, grafo=None):
    
    ###Construye un networkx.Graph() con las aristas de 'arbol' y dibuja la figura.
    ###- arbol: lista de tuplas (u, v, peso)
    ###- grafo: (opcional) instancia de tu clase Grafo para obtener la lista completa de nodos
    
    Arbol_optimo = nx.Graph()

    # Si la instancia del grafo tiene atributo 'vertice', se usa para añadir nodos
    if grafo is not None and hasattr(grafo, "vertice"):
        Arbol_optimo.add_nodes_from(grafo.vertice)
    else:
        # Si no, infiere nodos de las aristas del árbol
        nodos = set()
        for u, v, _ in arbol:
            nodos.add(u)
            nodos.add(v)
        Arbol_optimo.add_nodes_from(nodos)

    # Añadimos las aristas (con peso) al grafo que vamos a dibujar
    Arbol_optimo.add_weighted_edges_from(arbol)

    # Calculamos posiciones para los nodos (layout)
    pos = nx.spring_layout(Arbol_optimo, seed=42)

    # Creamos figura y dibujamos nodos y etiquetas
    fig = plt.figure(figsize=(8, 6))
    nx.draw(Arbol_optimo, pos,
            with_labels=True,
            node_color='lightblue',
            node_size=800,
            font_size=10,
            edge_color='gray')

    # Dibujamos etiquetas de pesos en las aristas
    edge_labels = nx.get_edge_attributes(Arbol_optimo, 'weight')
    nx.draw_networkx_edge_labels(Arbol_optimo, pos, edge_labels=edge_labels, font_size=9)

    plt.title("Árbol resultante (Kruskal)")
    plt.tight_layout()
    plt.show()

# Imprimimos la lista ordenada y el árbol resultante para verificar y graficar.
ordered = ordenar_por_peso(G.getPeso())
Arbol_optimo = kruskal(ordered)
print("Lista ordenada por peso:", ordered)
print("arbol:", Arbol_optimo)

# Llamada a la función de graficado (mostrará una ventana con la figura)
plot_arbol(Arbol_optimo, G)



