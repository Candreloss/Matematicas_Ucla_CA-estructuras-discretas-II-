import networkx as nx
import matplotlib.pyplot as mat

vertices = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']

def agregar_vertice (G, vertices):
        G.add_nodes_from(vertices)

def agregar_arista(G, u, v, p=0):
    G.add_edge(u, v, peso=p)


if __name__ == '__main__':
    G = nx.Graph()
    agregar_vertice(G, vertices)
    agregar_arista(G, "A", "B", 8)
    agregar_arista(G, "A", "D", 5)
    agregar_arista(G, "A", "E", 4)
    agregar_arista(G, "B", "C", 3)
    agregar_arista(G, "B", "F", 4)
    agregar_arista(G, "B", "E", 4)
    agregar_arista(G, "C", "F", 6)
    agregar_arista(G, "C", "G", 7)
    agregar_arista(G, "D", "E", 1)
    agregar_arista(G, "D", "I", 2)
    agregar_arista(G, "D", "H", 3)
    agregar_arista(G, "E", "F", 3)
    agregar_arista(G, "E", "I", 2)
    agregar_arista(G, "F", "G", 1)
    agregar_arista(G, "F", "K", 14)
    agregar_arista(G, "F", "I", 3)
    agregar_arista(G, "G", "K", 2)
    agregar_arista(G, "G", "L", 3)
    agregar_arista(G, "H", "I", 11)
    agregar_arista(G, "H", "M", 6)
    agregar_arista(G, "I", "K", 6)
    agregar_arista(G, "I", "P", 15)
    agregar_arista(G, "I", "N", 2)
    agregar_arista(G, "I", "M", 5)
    agregar_arista(G, "K", "L", 8)
    agregar_arista(G, "K", "P", 3)
    agregar_arista(G, "L", "P", 6)
    agregar_arista(G, "M", "N", 1)
    agregar_arista(G, "N", "P", 13)
    print(G.number_of_nodes())
    print(G.number_of_edges())
    """e= str(input('Ingrese el nombre del vertice a agregar:'))
    if e in list(G.nodes):
        print("Este vértice ya existe en el grafo")
    else:
        print("Agregado con éxito")
        agregar_vertice(G, e)
        print(list(G.nodes))"""
    pos = nx.spring_layout(G, seed=100, k=0.5, iterations=100)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'peso')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    mat.title("Grafo con NetworkX")
    mat.show()




































"""

class Grafo:
    def __init__(self):
        self.vertices = ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H',  'I', 'K', 'L', 'M', 'N', 'P']
        self.aristas =[]
        self.pesos = {('A', 'B'): 8, ("A", "D"): 5, ("A", "E"): 4, ("B", "C"):3, ("B", "F"): 4, ("B", "E"): 4, ("C", "F"):6   } 
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

            

if __name__ == "__main__":
    d = Grafo()
    G = nx.Graph()
    G.add_nodes_from(["1", "2", "3"])
    G.add_edges_from([(1, 2), (1, 3)])
    print(G.adj)

"""
