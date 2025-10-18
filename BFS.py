import matplotlib.pyplot as plt
from Digrafo import Grafo

def Construir_adyacencias(grafo):
    """
    Intenta construir un diccionario de adyacencia {nodo: [vecinos]} a partir
    de la instancia 'grafo' (clase Grafo en Digrafo.py).
    Soporta varias representaciones:
      - grafo.getPeso() que devuelva lista de (u,v,p) o lista de (u,v)
      - grafo.pesos como dict {(u,v): peso}
      - grafo.aristas como lista de pares
      - grafo.vertices como lista de nodos (devuelve adyacencia vacía)
    """
    adj = {}

    # 1) intentar getPeso()
    if hasattr(grafo, "getPeso"):
        try:
            pesos = grafo.getPeso()
            if isinstance(pesos, dict):
                for (u, v), w in pesos.items():
                    adj.setdefault(u, []).append(v)
                    adj.setdefault(v, []).append(u)
                return adj
            # lista de tuplas
            for item in (pesos or []):
                if not item:
                    continue
                if isinstance(item, (list, tuple)) and len(item) >= 2:
                    u, v = item[0], item[1]
                    adj.setdefault(u, []).append(v)
                    adj.setdefault(v, []).append(u)
            if adj:
                return adj
        except Exception:
            pass

    # 2) intentar atributo aristas (lista de pares o triples)
    if hasattr(grafo, "aristas"):
        for e in getattr(grafo, "aristas") or []:
            if isinstance(e, (list, tuple)) and len(e) >= 2:
                u, v = e[0], e[1]
                adj.setdefault(u, []).append(v)
                adj.setdefault(v, []).append(u)
        if adj:
            return adj

    # 3) intentar atributo pesos (diccionario)
    if hasattr(grafo, "pesos") and isinstance(getattr(grafo, "pesos"), dict):
        for (u, v), w in grafo.pesos.items():
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        if adj:
            return adj

    # 4) si hay lista de vertices, crear claves sin vecinos
    if hasattr(grafo, "vertices"):
        for v in getattr(grafo, "vertices") or []:
            adj.setdefault(v, [])
        return adj

    return adj


def bfs_tree(grafo, origen):
    """
    Realiza BFS (estructura similar a conexion_vertice) y devuelve el árbol BFS:
      - tree_edges: lista de pares (padre, hijo)
      - node_level: dict {nodo: nivel}
    """
    adj = Construir_adyacencias(grafo)
    if not adj:
        raise ValueError("No se pudo construir la adyacencia desde el grafo.")

    if origen not in adj:
        raise ValueError(f"Origen {origen} no está en el grafo (nodos: {list(adj.keys())})")

    visitado = set([origen])
    pendientes = [origen]
    cabeza = 0

    parent = {origen: None}
    node_level = {origen: 0}
    tree_edges = []

    while cabeza < len(pendientes):
        nodo = pendientes[cabeza]
        cabeza += 1
        for vecino in adj.get(nodo, []):
            if vecino not in visitado:
                visitado.add(vecino)
                pendientes.append(vecino)
                parent[vecino] = nodo
                node_level[vecino] = node_level[nodo] + 1
                tree_edges.append((nodo, vecino))
    return tree_edges, node_level


def dibujar_arbol_bfs(tree_edges, node_level, mostrar_nombres=True):
    """
    Dibuja el árbol BFS con matplotlib.
    - tree_edges: lista de (padre,hijo)
    - node_level: dict {nodo: nivel}
    """
    # conjunto de nodos
    nodos = set()
    for u, v in tree_edges:
        nodos.add(u); nodos.add(v)
    for n in node_level.keys():
        nodos.add(n)

    # agrupar nodos por nivel
    niveles = {}
    max_level = 0
    for n, lv in node_level.items():
        niveles.setdefault(lv, []).append(n)
        if lv > max_level:
            max_level = lv

    # posiciones: para cada nivel colocar nodos horizontalmente espaciados
    positions = {}
    for lv in range(0, max_level + 1):
        lista = niveles.get(lv, [])
        k = len(lista)
        if k == 0:
            continue
        xs = [ -1 + 2*i/(k-1) if k > 1 else 0.0 for i in range(k) ]
        y = -lv
        for i, nodo in enumerate(lista):
            positions[nodo] = (xs[i], y)

    # crear figura y dibujar
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # aristas del árbol
    for u, v in tree_edges:
        if u in positions and v in positions:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1.5, zorder=1)

    # nodos
    xs = [positions[n][0] for n in positions]
    ys = [positions[n][1] for n in positions]
    ax.scatter(xs, ys, s=500, c='lightblue', edgecolors='k', zorder=2)

    # etiquetas
    if mostrar_nombres:
        for n, (x, y) in positions.items():
            ax.text(x, y, str(n), fontsize=10, ha='center', va='center', zorder=3)

    ax.set_title("Árbol BFS (resultante)")
    plt.tight_layout()
    plt.show(block=True)
    return fig


if __name__ == "__main__":
    # prueba rápida: crea el grafo desde Digrafo.Grafo y dibuja su árbol BFS partiendo del primer nodo disponible
    G = Grafo()
    try:
        adj = Construir_adyacencias(G)
        origen = next(iter(adj))
    except StopIteration:
        raise SystemExit("El grafo está vacío. Agrega vértices antes de ejecutar este script.")

    tree, levels = bfs_tree(G, origen)
    print("Aristas del árbol BFS:", tree)
    dibujar_arbol_bfs(tree, levels)