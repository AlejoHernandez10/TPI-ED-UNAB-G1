# 🎮 NextGame — Catalogo y Sistema de Recomendacion de Videojuegos

**NextGame** es una aplicacion por consola desarrollada en Python para la materia **Estructuras de Datos (UNaB - 2026)**. Permite cargar un catalogo de mas de 200 videojuegos, buscar titulos a alta velocidad, navegar categorias jerarquicas, consultar rankings de mejores puntuados y descubrir juegos relacionados a traves de una red de conexiones.

---

##  Integrantes del Equipo (Grupo 1 - Comision 3)
* **Hernandez Alejo**  
* **Mora Joaquin**  
* **Docente:** Angel Leonardo Bianco

---

##  Estructuras de Datos Implementadas

Todas las estructuras principales fueron programadas manualmente por el equipo sin usar librerias externas que resuelvan la logica:

* **TP 3 — Arbol Binario de Busqueda (BST):** Insercion, recorridos (inorden, preorden, postorden) y busqueda por clave.
* **TP 4 — Arbol AVL Balanceado:** Busqueda en $O(\log n)$ con calculo de alturas, factor de balance y las 4 rotaciones (LL, RR, LR, RL). Resuelve la busqueda principal por titulo.
* **TP 5 — Arbol General (N-ario):** Jerarquia de categorias (Catalogo -> Generos -> Videojuegos) con recorridos en amplitud (BFS) y profundidad (DFS).
* **TP 6 — Max-Heap:** Cola de prioridad manual basada en una lista que resuelve el Top 10 de mejores calificaciones de manera eficiente en $O(k \log n)$ sin ordenar toda la lista.
* **TP 7 — Grafo No Dirigido:** Red de videojuegos mediante lista de adyacencia. Las aristas conectan juegos que comparten generos (con peso segun la cantidad de coincidencias) para recomendar titulos parecidos.

---

##  Documentacion del Proyecto

Los documentos formales requeridos por la catedra se encuentran en la carpeta `docs/`:

*  [01-requerimientos.md](docs/01-requerimientos.md) — Requerimientos funcionales, no funcionales y alcance.
*  [02-casos-de-uso.md](docs/02-casos-de-uso.md) — Descripcion de los 5 casos de uso principales.
*  [05-gestion-proyecto.md](docs/05-gestion-proyecto.md) — Metodologia de trabajo, equipo y tablero de tareas.

---

## 🚀 Instalacion y Ejecucion

### Requisitos
 [![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)



### 1. Ejecutar el sistema completo
```bash
py main.py
```

### 2. Ejecutar las pruebas individuales de cada etapa
```bash
# Probar Arbol Binario (TP 3)
py algoritmos/probar_bst.py

# Probar AVL y comparativa con BST degenerado (TP 4 y TP 5)
py algoritmos/probar_avl.py

# Probar Max-Heap de calificaciones (TP 6)
py algoritmos/probar_heap.py

# Probar Grafo de relaciones (TP 7)
py algoritmos/probar_grafo.py
```
