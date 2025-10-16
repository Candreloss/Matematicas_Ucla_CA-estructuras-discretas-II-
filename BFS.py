import networkx as nx
import matplotlib.pyplot as plt
from Digrafo import Grafo

# Crear instancia de Grafo
g = Grafo()

# Opción A: recorrer la lista 'peso' que devuelve getPeso() — es una lista de tuplas (u, v, w)
for i in g.getPeso():
    for u, v, w in g.getPeso():
        if u == v:
            print(f"Bucle en el vértice: {u} con peso: {w}")
        print(f"Arista: ({u}, {v}), Peso: {w}")


