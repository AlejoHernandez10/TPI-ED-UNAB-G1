# Justificacion de Recorridos en Grafos (BFS y DFS) 

Este documento explica por que tenemos implementados BFS y DFS como metodos genericos dentro de la clase Grafo, pero decidimos no meterlos directamente en el menu de recomendaciones del usuario final.

---

## 1. Lo que pide la teoria y lo que tenemos en el codigo

Tanto BFS como DFS estan programados adentro de `estructuras/grafo.py` y funcionan con la logica estandar:

* **BFS (Recorrido en anchura):** Usa una cola (FIFO) con `deque`. Explora los vecinos por niveles de distancia. El primer camino que encuentra entre dos nodos es el que menos saltos tiene.
* **DFS (Recorrido en profundidad):** Esta hecho de forma recursiva. Se mete a fondo por una rama hasta que no puede avanzar mas y despues vuelve atras.
* **Control de ciclos:** En ambos usamos un conjunto `visitados` donde agregamos el nodo apenas lo descubrimos para no quedarnos en un bucle infinito ni meter cosas repetidas a la cola.
* **Complejidad:** Ambos algoritmos cuestan $O(V + E)$ porque revisan cada vertice y cada arista una sola vez sobre nuestra lista de adyacencia.

---

## 2. Por que no los usamos para recomendar juegos en la terminal

Decidimos no ponerlos en el menu de opciones por los siguientes motivos practicos:

### El problema de la red densa
Nuestro catalogo tiene 200 videojuegos y mas de 15.000 conexiones porque muchisimos juegos comparten etiquetas comunes como "Accion", "Aventura" o "RPG". 

* **El problema de DFS como recomendador:**
  DFS explora a lo profundo. Si arrancamos en *The Witcher 3* (RPG de fantasia), puede saltar a *Cyberpunk* por compartir "RPG", de ahi a *GTA V* por "Mundo Abierto", de ahi a un juego de carreras y terminar recomendandole al usuario un juego que nada que ver con lo que pidio.

* **El problema de BFS como recomendador:**
  Como casi todos los juegos estan conectados en el primer nivel (comparten al menos una etiqueta), un BFS tiraria una lista gigante de mas de 100 juegos sin criterio de orden por nota ni por cantidad de coincidencias.

### Como lo solucionamos
Para que las recomendaciones tengan sentido real para el jugador:
1. Miramos los **vecinos directos** en el Grafo.
2. Usamos el **peso de la arista** (la cantidad exacta de generos que comparten los dos juegos).
3. Usamos nuestro **Max-Heap** para ordenar y mostrar solo los mejores puntuados.

---

## 3. ¿En que casos si tendria sentido usar BFS y DFS en nuestro proyecto?

Aunque no los mostramos en el menu principal, los algoritmos estan en la clase Grafo porque serian muy utiles para otras funciones:

1. **Uso de BFS — Grados de separacion entre juegos:**
   Serviria para responder: *"¿A cuantos saltos esta The Witcher 3 de Portal 2?"*. Como BFS encuentra el camino con menor cantidad de aristas, podria mostrar la cadena mas corta de juegos puente que conectan dos titulos distintos.

2. **Uso de DFS — Deteccion de juegos aislados:**
   Serviria para herramientas de administracion del catalogo. Si agregamos juegos nuevos que no comparten ningun genero con nadie (como un juego de deportes o educativo), con DFS podemos detectar componentes inconexas o juegos "huerfanos" que quedaron sueltos sin relacion con la red.
