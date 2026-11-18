# Justificacion y Explicacion de Dijkstra (Caminos Minimos)

Este documento explica de forma simple como funciona el algoritmo de Dijkstra en nuestro proyecto, como definimos el "costo" entre juegos y por que usamos este algoritmo segun la teoria de la materia.

---

## 1. ¿Que problema resuelve en NextGame?

Imaginemos que a un usuario le gusta mucho *The Witcher 3* (un RPG de fantasia y accion) pero quiere probar *Portal 2* (un juego de puzzles y disparos) y siente que son dos mundos totalmente distintos.

Dijkstra nos permite encontrar la **secuencia de transicion mas suave** entre ambos titulos, usando juegos puente que comparten generos intermedios.

Por ejemplo, el sistema encuentra:
`The Witcher 3 (Accion, RPG)` $\rightarrow$ `Borderlands 2 (Accion, Shooter, RPG)` $\rightarrow$ `Portal 2 (Shooter, Puzzle)`

*Borderlands 2* actua como el puente ideal porque comparte generos con ambos extremos.

---

## 2. ¿Que significa "Costo" en nuestro grafo? (Definicion de la metrica)

Dijkstra siempre busca el camino con **menor costo acumulado** (la ruta mas corta).

En nuestro grafo del TP 7, el peso de la arista era la cantidad de generos en comun (mas generos = mas parecidos). Si usaramos ese numero directo, Dijkstra elegiria juegos que comparten pocos generos porque busca numeros chicos.

Para solucionarlo, definimos el costo como el **esfuerzo de transicion**:
$$\text{Costo} = 5 - \text{generos en comun}$$

* Si comparten 4 generos $\rightarrow$ Costo = 1 (estan muy cerca, son casi iguales).
* Si comparten 1 solo genero $\rightarrow$ Costo = 4 (estan mas lejos, el salto es mas brusco).

De esta manera, el algoritmo elige el camino donde los juegos son lo mas parecidos posible entre si.

---

## 3. ¿Como funciona el algoritmo paso a paso?

La implementacion en `estructuras/grafo.py` es super directa y facil de explicar:

1. **Tabla de distancias:** Creamos un diccionario con todos los juegos arrancando en distancia infinito ($\infty$), salvo el juego de inicio que arranca en 0.
2. **Tabla de padres:** Guardamos quien fue el nodo anterior de cada juego para poder acordarnos del camino.
3. **Bucle principal:**
   * De los juegos que todavia no visitamos, elegimos el que tenga la menor distancia acumulada hasta el momento.
   * Si llegamos al destino, cortamos.
   * Revisamos todos sus vecinos conectados. Si pasar por el juego actual hacia el vecino es mas corto que la distancia que tenia antes, actualizamos su distancia y anotamos su padre (a esto en la teoria se le llama *relajacion de aristas*).
4. **Reconstruccion del camino:** Cuando termina, arrancamos desde el destino y vamos yendo hacia atras mirando el diccionario de padres hasta llegar al origen. Damos vuelta la lista y tenemos la ruta exacta.

---

## 4. Justificacion teorica (Preguntas de examen)

* **¿Por que Dijkstra y no Bellman-Ford?**  
  Bellman-Ford es un algoritmo mas pesado y lento que solo se justifica si hubiera aristas con pesos o costos negativos. En NextGame todos los costos son positivos ($costo \ge 1$), por lo que Dijkstra es la opcion correcta, optima y mucho mas rapida.

* **¿Que diferencia hay entre Dijkstra y BFS?**  
  BFS solo cuenta la cantidad de saltos (aristas), ignorando que tan parecidos son los juegos entre si. Podria dar un camino de 2 saltos pero con juegos muy distintos. Dijkstra, en cambio, tiene en cuenta el peso de afinidad y busca la transicion con menor costo total acumulado.

* **¿Cual es la complejidad temporal?**  
  Nuestra implementacion busca el minimo recorriendo el conjunto de vertices no visitados, lo que cuesta $O(V^2)$. Para un catalogo de 200 videojuegos esto toma apenas 2 milisegundos. Si el catalogo creciera a 100.000 juegos, convendria usar una cola de prioridad (Min-Heap) para que la complejidad baje a $O((V + E) \log V)$.
