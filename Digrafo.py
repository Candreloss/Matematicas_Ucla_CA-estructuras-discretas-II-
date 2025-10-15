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

            

if __name__ == "__main__":
    d = Digrafo()
    d.agregar_vertice()
    d.agregar_arista()
    
    