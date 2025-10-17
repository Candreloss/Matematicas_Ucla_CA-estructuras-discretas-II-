import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()
G.add_edges_from([("V1", "V2"), ("V2", "V3"), ("V3", "V1")])

# Asignar pesos
G["V1"]["V2"]["weight"] = 5.0
G["V2"]["V3"]["weight"] = 3.0
G["V3"]["V1"]["weight"] = 4.0

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)

# Mostrar etiquetas de los pesos
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Grafo con pesos en las aristas")
plt.show()