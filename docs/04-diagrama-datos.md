# Diagrama de Datos y Conexión de Estructuras — NextGame
**Materia:** Estructuras de Datos — Universidad Nacional Guillermo Brown (UNAB)  
**Proyecto:** NextGame - Sistema de Recomendación de Videojuegos  
**Integrantes:** Hernandez Alejo, Mora Joaquín  

---

## 1. Descripción del Flujo de Datos
El diagrama modela el ciclo de vida de la información en NextGame:
1. **Fuente de Datos:** Se leen 200 videojuegos estructurados en formato JSON desde `datos/juegos.json`.
2. **Carga y Deserialización:** `CatalogoJuegos.cargar_desde_json()` parsea los registros e instancia los objetos de dominio `Juego` (`modelos/juego.py`).
3. **Distribución en Estructuras de Memoria:**
   - **Árbol AVL (TP4):** Indexación balanceada por título para búsquedas rápidas en tiempo logarítmico $O(\log n)$.
   - **Árbol Binario de Búsqueda (TP3):** Estructura previa de indexación binaria por título.
   - **Árbol General N-ario (TP5):** Estructura jerárquica multinivel: Raíz ("Catálogo NextGame") $\rightarrow$ Categorías/Géneros $\rightarrow$ Videojuegos en hojas.
   - **Max-Heap Binario (TP6):** Montículo de máximos ordenado por calificación para resolver eficientemente el Top 10 sin necesidad de ordenar la totalidad del dataset.
   - **Grafo No Dirigido Ponderado (TP7):** Red de videojuegos interconectados donde los vértices representan juegos y las aristas están ponderadas según la cantidad de géneros compartidos.
4. **Conexión con el Menú e Interacción con el Usuario:** Cada opción del menú principal en `InterfazConsola` consulta la estructura especializada adecuada y muestra los resultados formateados en la terminal.

---

## 2. Diagrama Gráfico Renderizado

![Diagrama de Conexión de Estructuras](04-diagrama-datos.png)

---

## 3. Especificación en Código Mermaid

```mermaid
flowchart TD
    subgraph OrigenDatos [Fuente de Datos]
        JSON[("datos/juegos.json<br>(Dataset 200 videojuegos)")]
    end

    subgraph Carga [Procesamiento y Modelado]
        LOAD["CatalogoJuegos.cargar_desde_json()"]
        JUEGOS["Objetos Juego (modelos/juego.py)<br>[id, titulo, generos, calificacion, etc.]"]
    end

    subgraph Estructuras [Estructuras de Datos en Memoria]
        AVL["Árbol AVL (TP4)<br>Indexación balanceada por título<br>Búsqueda en O(log n)"]
        BST["Árbol Binario de Búsqueda (TP3)<br>Indexación por título"]
        AG["Árbol General N-ario (TP5)<br>Jerarquía: Catálogo -> Géneros -> Juegos"]
        HEAP["Max-Heap Binario (TP6)<br>Montículo ordenado por calificación"]
        GRAFO["Grafo No Dirigido Ponderado (TP7)<br>Vértices = Juegos, Peso = Géneros en común"]
    end

    subgraph Menu [InterfazConsola / Menú de Opciones]
        OP1["Opción 1: Buscar Videojuego"]
        OP2["Opción 2: Explorar Categorías<br>(Jerarquía, BFS, DFS, Subárbol)"]
        OP3["Opción 3: Explorar por Género"]
        OP4["Opción 4: Ver Juegos Relacionados"]
        OP5["Opción 5: Obtener Recomendaciones"]
        OP6["Opción 6: Ver Top 10"]
    end

    subgraph Usuario [Usuario Final]
        USER["👤 Jugador / Usuario"]
    end

    JSON -->|Lectura y deserialización JSON| LOAD
    LOAD -->|Instanciación de objetos| JUEGOS

    JUEGOS -->|Insertar clave=titulo, valor=juego| AVL
    JUEGOS -->|Insertar clave=titulo, valor=juego| BST
    JUEGOS -->|Insertar categorías y hojas| AG
    JUEGOS -->|Insertar juego por rating| HEAP
    JUEGOS -->|Agregar vértices y aristas ponderadas| GRAFO

    AVL -->|Búsqueda exacta y por prefijo| OP1
    AG -->|Recorridos BFS, DFS y jerarquía| OP2
    AVL -->|Recorrido Inorden filtrado| OP3
    GRAFO -->|Vecinos adyacentes de mayor peso| OP4
    GRAFO -->|Vecinos de mayor calificación| OP5
    HEAP -->|Extracción de N máximos| OP6

    USER -->|Selecciona opciones e inputs| Menu
    Menu -->|Muestra resultados formateados en consola| USER
```
