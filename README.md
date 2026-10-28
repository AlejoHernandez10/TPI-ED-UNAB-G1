# 🎮 NextGame — Catálogo y Sistema de Recomendación de Videojuegos

**NextGame** es una aplicación por consola desarrollada en Python para la materia **Estructuras de Datos (UNaB - 2026)**. Permite cargar un catálogo de más de 200 videojuegos, buscar títulos a alta velocidad, navegar categorías jerárquicas, consultar rankings de mejores puntuados y descubrir juegos relacionados a través de una red de conexiones.

---

##  Integrantes del Equipo (Grupo 1 - Comisión 3)
* **Hernandez Alejo**  
* **Mora Joaquin**  
* **Docente:** Angel Leonardo Bianco

---

##  Estructuras de Datos Implementadas

Todas las estructuras principales fueron programadas manualmente por el equipo sin usar librerías externas que resuelvan la lógica:

* **TP 3 — Árbol Binario de Búsqueda (BST):** Inserción, recorridos (inorden, preorden, postorden) y búsqueda por clave.
* **TP 4 — Árbol AVL Balanceado:** Búsqueda en $O(\log n)$ con cálculo de alturas, factor de balance y las 4 rotaciones (LL, RR, LR, RL). Resuelve la búsqueda principal por título.
* **TP 5 — Árbol General (N-ario):** Jerarquía de categorías (Catálogo -> Géneros -> Videojuegos) con recorridos en amplitud (BFS) y profundidad (DFS).
* **TP 6 — Max-Heap:** Cola de prioridad manual basada en una lista que resuelve el Top 10 de mejores calificaciones de manera eficiente en $O(k \log n)$ sin ordenar toda la lista.
* **TP 7 — Grafo No Dirigido:** Red de videojuegos mediante lista de adyacencia. Las aristas conectan juegos que comparten géneros (con peso según la cantidad de coincidencias) para recomendar títulos parecidos.

---

##  Documentación del Proyecto

Los documentos formales requeridos por la cátedra se encuentran en la carpeta `docs/`:

*  [01-requerimientos.md](docs/01-requerimientos.md) — Requerimientos funcionales, no funcionales y alcance.
*  [02-casos-de-uso.md](docs/02-casos-de-uso.md) — Descripción de los 5 casos de uso principales.
*  [05-gestion-proyecto.md](docs/05-gestion-proyecto.md) — Metodología de trabajo, equipo y tablero de tareas.

---

## 🚀 Instalación y Ejecución

### Requisitos
* Python 3.10 o superior instalado.

### 1. Ejecutar el sistema completo
```bash
py main.py
```

### 2. Ejecutar las pruebas individuales de cada etapa
```bash
# Probar Árbol Binario (TP 3)
py algoritmos/probar_bst.py

# Probar AVL y comparativa con BST degenerado (TP 4 y TP 5)
py algoritmos/probar_avl.py

# Probar Max-Heap de calificaciones (TP 6)
py algoritmos/probar_heap.py

# Probar Grafo de relaciones (TP 7)
py algoritmos/probar_grafo.py
```
