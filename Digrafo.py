# Un grafo tiene como atributos un conjunto de nodos y un conjunto de 
# aristas que los unen. Pero a demas existe una funcion de 
# incidencia asigna a cada par de vertices, al menos una arista.

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
    
    
    # Funcion para agregar aristas a el array de aristas con su respectivo peso, y ademas se esta aplicando 
    # la funcion de incidencia, que hace corresponder a cada arista un par de vertices.
    def agregar_arista(self):
        while True:
            u = input("Ingrese el vertice inicial de la arista (o 'salir' para terminar): ")
            if u.lower() == 'salir':
                break
            v = input("Ingrese el vertice final de la arista: ")
            if u in self.vertices and v in self.vertices:
                self.aristas.append((u, v))
                peso = float(input("Ingrese el peso de la arista: "))
                self.pesos[(u, v)] = peso
                print(self.aristas)
                print(self.pesos)
                return self.aristas, self.pesos
            else:
                print("Uno o ambos vertices no existen. Por favor, agreguelos primero.")
            

if __name__ == "__main__":
    d = Digrafo()
    d.agregar_vertice()
    d.agregar_arista()
    d.print("Vertices del grafo:", d.vertices)
    d.print("Aristas del grafo:", d.aristas)
    d.print("Pesos de las aristas:", d.pesos)
    