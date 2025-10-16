<<<<<<< HEAD
# Proyecto Estructuras Discretas
## Planteamiento:

Considere el grafo adjunto, bajo las ponderaciones establecidas, que
corresponden al costo de envió entre una ciudad Quíbor con la ciudad
Barquisimeto. El análisis es para responder a la Empresa MATEMÁTICAS
UCLA C.A., que desea realizar las entregas de sus productos al menor
costo. Basándonos en el siguiente planteamiento donde el grupo debe
seguir las siguientes instrucciones:

⦁ Utilizarán el último dígito de la cedula de identidad del participante
(son 7 ), de la siguiente manera:

Primer integrante: xx.xxx.xxa

Segundo integrante: xx.xxx.xxb y así sucesivamente hasta llegar a la f

⦁ Si el dígito es cero, el participante puede utilizar el número
anterior, si es cero volver a aplicar hasta encontrar que sea distinto
de cero. Si hay preguntas dirigirse a cualquiera de los dos docentes a
cargo de la asignatura.

⦁ No deben destruir la forma del diagrama.


Realice un programa que contenga un menú de opciones, las cuales
permitirán:

### A 
**Establecer el recorrido en anchura (BFS)**. Muestre cómo queda el árbol recubridor. Para esta opción debe considerar: el vértice inicial, árbol raíz al vértice A, las adyacencias para cada uno de los vértices establecidos, visualizar los hijos de la raíz.

### B 
**Establecer el recorrido de búsqueda en profundidad (DFS) de este grafo comenzando desde el vértice A.** Muestre cómo queda el árbol recubridor estableciendo orden fijo y las adyacencias de cada uno de los vértices.

### C 
**Establecer el árbol generador de mínimo peso del grafo dado aplicando el algoritmo de Kruskal**. Muestre el árbol generador con los pesos asignados en cada una de las adyacencias preestablecidas con anterioridad.

### E 
**Establecer el árbol generador de mínimo peso, utilizando el algoritmo Prim.** Considerando como vértice inicial A. Ilustrar el árbol recubridor óptimo bajo las condiciones establecidas en la figura ilustrada.

## Consideraciones finales: 

Como programadores de la empresa MATEMÁTICAS C.A, están en la libertad de utilizar las herramientas gráficas que le ofrece el lenguaje Python, específicamente para la ilustraciones de cada árbol generado.

El proyecto será ponderado sobre 100 puntos, para poder abordar las
diferentes consideraciones en la rúbrica de evaluación, dicha
ponderación se transformará a la escala de 10pts.

Los docentes escogerán al azar quienes defenderán el proyecto, el resto responderán las preguntas generadas o en su defecto se abocaran a los cambios solicitados en in situ en el momento de la defensa.

Trabajos con igual o similar contenido serán penalizados. Dos códigos
iguales se ponderarán con la mínima puntuación 0 pts, por no cumplir con
la pauta de originalidad. Cabe señalar que si se evidencia el uso de
Inteligencia Artificial para obtener código, los participantes que
incurran en tal falta **serán penalizados.**

**Queda prohibido el uso de librerías que realicen los cálculos por sí
mismas, el código ha de implementar manualmente los métodos necesarios
para resolver el problema.**

## Librerías permitidas:

-   **Pandas**: Formato para variables.
-   **Matplotlib**: Librería principal para gráficos.
-   **Networkx**: Permite definir y modificar grafos, añadiendo o
    modificando nodos y aristas para representar datos y relaciones. En
    este caso, se permite su uso solo para representar el grafo y
    dibujarlo, pero no se permite el uso de sus algoritmos.
-   **NumPy:** Ideal para operaciones matemáticas.
-   **Collections**: **Proporciona estructuras de datos especializadas.**
-   **Tkinter/Pygubu:** Para la interfaz gráfica.

## Librerías NO permitidas:

-   **OpenGL**
-   **python-igraph, graph-tool...**
-   **Otras librerías de grafos que proporcionen los algoritmos
    solicitados, o librerías de inteligencia artificial.**


## Rubrica de evaluación
<table>
    <tr>
        <th>Categoria</th>
        <th>Elemento</th>
        <th>Descripcion</th>
        <th>Puntuacion</th>
    </tr>
    <tr>
        <th rowspan="2">Clases</th>
        <td>Diseño</td>
        <td>El diseño de las clases se corresponde con el enunciado y funciona de pmanera práctica para resolver el problema</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Implementación</td>
        <td>Las clases funcionan correctamente implementadas, tanto es sus métodos ocmo en el algortimo planteado</td>
        <td>10</td>
    </tr>
    <tr>
        <th rowspan="2">Funcionalidad</th>
        <td>Amigabilidad</td>
        <td>El programa es amable con el usuario, funciona de manera adecuada, con mensajes de  error y éxtico  bien estructurados, claros y concisos de tal manera que sea entendible a cualquier usuario</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Funcionalidad</td>
        <td>El programa se ejecuta correctamente, sin ningún tipo de error con los datos utilizados por el instructor</td>
        <td>10</td>
    </tr>
    <tr>
        <th rowspan="5">Código</th>
        <td>Orden</td>
        <td>El código fuente del proyecto se encuentra bien estructurado y ordenado en carpetas</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Indentación</td>
        <td>El código fuente del proyecto se encuentra con una indentación adecuada</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Abstracción</td>
        <td>El código fuente implementa métodos parametrizados y generales que se ejecutan de forma acorde para ahorrar código</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Nombres</td>
        <td>Las clases, atributos y métodos están identificados con nombres que se pueden reconocer de forma inmediata</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Librerías</td>
        <td>Las librerías utilizadas deberán ser aquellas que estén autorizadas</td>
        <td>5</td>
    </tr>
    <tr>
        <th rowspan="5">Exposición</th>
        <td>Claridad</td>
        <td>La exposición fue clara y concisa en la forma que se explicaron las funcionalidades y la estructura fundamental del proyecto</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Tiempo</td>
        <td>La exposición fue clara y concisa en la forma que se explicaron las funcionalidades y l aestructura fundamental del proyecto</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Muestra</td>
        <td>El participante mostró de forma correcta todas las funcionalidades ddel programa</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Gestión de pánico</td>
        <td>El participante manejó correctamente situaciones adversas que pudieran aparecer durante su exposición</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Trabajo en equipo</td>
        <td>El participante manejó correctamente situaciones adversas que pudieran aparecer durante su exposición</td>
        <td>10</td>
    </tr>
    <tr>
        <th colspan="3">Total</th>
        <td>x</td>
    </tr>
    <tr>
        <th colspan="3">Puntuación mínima aprobatoria</th>
        <td>x</td>
    </tr>
</table>
=======
# Proyecto Estructuras Discretas
## Planteamiento:

Considere el grafo adjunto, bajo las ponderaciones establecidas, que
corresponden al costo de envió entre una ciudad Quíbor con la ciudad
Barquisimeto. El análisis es para responder a la Empresa MATEMÁTICAS
UCLA C.A., que desea realizar las entregas de sus productos al menor
costo. Basándonos en el siguiente planteamiento donde el grupo debe
seguir las siguientes instrucciones:

⦁ Utilizarán el último dígito de la cedula de identidad del participante
(son 7 ), de la siguiente manera:

Primer integrante: xx.xxx.xxa

Segundo integrante: xx.xxx.xxb y así sucesivamente hasta llegar a la f

⦁ Si el dígito es cero, el participante puede utilizar el número
anterior, si es cero volver a aplicar hasta encontrar que sea distinto
de cero. Si hay preguntas dirigirse a cualquiera de los dos docentes a
cargo de la asignatura.

⦁ No deben destruir la forma del diagrama.


Realice un programa que contenga un menú de opciones, las cuales
permitirán:

a) **Establecer el recorrido en anchura (BFS)**. Muestre cómo queda el árbol recubridor. Para esta opción debe considerar: el vértice inicial, árbol raíz al vértice A, las adyacencias para cada uno de los vértices establecidos, visualizar los hijos de la raíz.

b) **Establecer el recorrido de búsqueda en profundidad (DFS) de este grafo comenzando desde el vértice A.** Muestre cómo queda el árbol recubridor estableciendo orden fijo y las adyacencias de cada uno de los vértices.

c) **Establecer el árbol generador de mínimo peso del grafo dado aplicando el algoritmo de Kruskal**. Muestre el árbol generador con los pesos asignados en cada una de las adyacencias preestablecidas con anterioridad.

d) **Establecer el árbol generador de mínimo peso, utilizando el algoritmo Prim.** Considerando como vértice inicial A. Ilustrar el árbol recubridor óptimo bajo las condiciones establecidas en la figura ilustrada.

## Consideraciones finales: 

Como programadores de la empresa MATEMÁTICAS C.A, están en la libertad de utilizar las herramientas gráficas que le ofrece el lenguaje Python, específicamente para la ilustraciones de cada árbol generado.

El proyecto será ponderado sobre 100 puntos, para poder abordar las
diferentes consideraciones en la rúbrica de evaluación, dicha
ponderación se transformará a la escala de 10pts.

Los docentes escogerán al azar quienes defenderán el proyecto, el resto responderán las preguntas generadas o en su defecto se abocaran a los cambios solicitados en in situ en el momento de la defensa.

Trabajos con igual o similar contenido serán penalizados. Dos códigos
iguales se ponderarán con la mínima puntuación 0 pts, por no cumplir con
la pauta de originalidad. Cabe señalar que si se evidencia el uso de
Inteligencia Artificial para obtener código, los participantes que
incurran en tal falta **serán penalizados.**

**Queda prohibido el uso de librerías que realicen los cálculos por sí
mismas, el código ha de implementar manualmente los métodos necesarios
para resolver el problema.**

## Librerías permitidas:

-   **Pandas**: Formato para variables.
-   **Matplotlib**: Librería principal para gráficos.
-   **Networkx**: Permite definir y modificar grafos, añadiendo o
    modificando nodos y aristas para representar datos y relaciones. En
    este caso, se permite su uso solo para representar el grafo y
    dibujarlo, pero no se permite el uso de sus algoritmos.
-   **NumPy:** Ideal para operaciones matemáticas.
-   **Collections**: **Proporciona estructuras de datos especializadas.**
-   **Tkinter/Pygubu:** Para la interfaz gráfica.

## Librerías NO permitidas:

-   **OpenGL**
-   **python-igraph, graph-tool...**
-   **Otras librerías de grafos que proporcionen los algoritmos
    solicitados, o librerías de inteligencia artificial.**


## Rubrica de evaluación
<table>
    <tr>
        <th>Categoria</th>
        <th>Elemento</th>
        <th>Descripcion</th>
        <th>Puntuacion</th>
    </tr>
    <tr>
        <th rowspan="2">Clases</th>
        <td>Diseño</td>
        <td>El diseño de las clases se corresponde con el enunciado y funciona de pmanera práctica para resolver el problema</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Implementación</td>
        <td>Las clases funcionan correctamente implementadas, tanto es sus métodos ocmo en el algortimo planteado</td>
        <td>10</td>
    </tr>
    <tr>
        <th rowspan="2">Funcionalidad</th>
        <td>Amigabilidad</td>
        <td>El programa es amable con el usuario, funciona de manera adecuada, con mensajes de  error y éxtico  bien estructurados, claros y concisos de tal manera que sea entendible a cualquier usuario</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Funcionalidad</td>
        <td>El programa se ejecuta correctamente, sin ningún tipo de error con los datos utilizados por el instructor</td>
        <td>10</td>
    </tr>
    <tr>
        <th rowspan="5">Código</th>
        <td>Orden</td>
        <td>El código fuente del proyecto se encuentra bien estructurado y ordenado en carpetas</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Indentación</td>
        <td>El código fuente del proyecto se encuentra con una indentación adecuada</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Abstracción</td>
        <td>El código fuente implementa métodos parametrizados y generales que se ejecutan de forma acorde para ahorrar código</td>
        <td>10</td>
    </tr>
    <tr>
        <td>Nombres</td>
        <td>Las clases, atributos y métodos están identificados con nombres que se pueden reconocer de forma inmediata</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Librerías</td>
        <td>Las librerías utilizadas deberán ser aquellas que estén autorizadas</td>
        <td>5</td>
    </tr>
    <tr>
        <th rowspan="5">Exposición</th>
        <td>Claridad</td>
        <td>La exposición fue clara y concisa en la forma que se explicaron las funcionalidades y la estructura fundamental del proyecto</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Tiempo</td>
        <td>La exposición fue clara y concisa en la forma que se explicaron las funcionalidades y l aestructura fundamental del proyecto</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Muestra</td>
        <td>El participante mostró de forma correcta todas las funcionalidades ddel programa</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Gestión de pánico</td>
        <td>El participante manejó correctamente situaciones adversas que pudieran aparecer durante su exposición</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Trabajo en equipo</td>
        <td>El participante manejó correctamente situaciones adversas que pudieran aparecer durante su exposición</td>
        <td>10</td>
    </tr>
    <tr>
        <th colspan="3">Total</th>
        <td>x</td>
    </tr>
    <tr>
        <th colspan="3">Puntuación mínima aprobatoria</th>
        <td>x</td>
    </tr>
</table>
>>>>>>> 99516dfa8735a803a0692eeb9dba963e4271e623
