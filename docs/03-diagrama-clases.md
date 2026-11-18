# Diagrama de Clases — NextGame
**Materia:** Estructuras de Datos — Universidad Nacional Guillermo Brown (UNAB)  
**Proyecto:** NextGame - Sistema de Recomendación de Videojuegos  
**Integrantes:** Hernandez Alejo, Mora Joaquín  

---

## 1. Descripción de la Arquitectura
El sistema está diseñado bajo el paradigma de Programación Orientada a Objetos (POO) con separación de responsabilidades:
- **`modelos/`**: Modela la entidad principal de dominio (`Juego`) con encapsulamiento de atributos privados y propiedades públicas.
- **`estructuras/`**: Contiene las estructuras de datos implementadas manualmente para la materia (BST, AVL, Árbol General, Max-Heap y Grafo).
- **`servicios/`**: `CatalogoJuegos` actúa como clase controladora central; compone y coordina todas las estructuras de datos sobre el conjunto de juegos.
- **`interfaz/`**: `InterfazConsola` desacopla la presentación en terminal de la lógica de negocio.

---

## 2. Diagrama Gráfico Renderizado

![Diagrama de Clases UML](03-diagrama-clases.png)

---

## 3. Especificación en Código Mermaid

```mermaid
classDiagram
    direction TB

    class Juego {
        -int _id
        -str _titulo
        -list _generos
        -str _desarrollador
        -float _calificacion
        -int _anio_publicacion
        -str _web
        +id int
        +titulo str
        +generos list
        +desarrollador str
        +calificacion float
        +anio_publicacion int
        +web str
        +tiene_genero(genero) bool
        +generos_en_comun(otro_juego) int
    }

    class ArbolBinarioBusqueda {
        +NodoArbol raiz
        +insertar(clave, valor)
        +buscar(clave) Any
        +inorder() list
        +preorder() list
        +postorder() list
    }

    class ArbolAVL {
        +NodoAVL raiz
        +insertar(clave, valor)
        +buscar(clave) Any
        +obtener_altura() int
        +obtener_balance() int
        +inorder() list
        +esta_balanceado() bool
    }

    class ArbolGeneral {
        +NodoGeneral raiz
        +establecer_raiz(clave, valor) NodoGeneral
        +agregar_hijo(clave_padre, clave_hijo, valor) bool
        +buscar(clave) NodoGeneral
        +recorrido_amplitud() list
        +recorrido_profundidad() list
        +mostrar_arbol() str
        +cantidad_nodos() int
    }

    class MaxHeap {
        +list datos
        +insertar(juego)
        +extraer_maximo() Juego
        +obtener_top_n(n) list
        +esta_vacio() bool
    }

    class Grafo {
        +dict vertices
        +agregar_vertice(juego)
        +agregar_arista(juego1, juego2, peso)
        +obtener_vecinos(id_juego) list
        +estan_conectados(id1, id2) bool
        +cantidad_vertices() int
        +cantidad_aristas() int
    }

    class CatalogoJuegos {
        -list _juegos
        -ArbolBinarioBusqueda _bst
        -ArbolAVL _avl
        -ArbolGeneral _arbol_categorias
        -MaxHeap _heap
        -Grafo _grafo
        +cargar_desde_json(ruta_archivo)
        +buscar_por_titulo(titulo) list
        +obtener_top_n(n) list
        +obtener_relacionados(juego_base, limite) list
        +obtener_recomendaciones(juego_base, limite) list
        +obtener_arbol_categorias() ArbolGeneral
        +obtener_por_genero(genero) list
        +obtener_todos_los_generos() list
    }

    class InterfazConsola {
        +mostrar_menu_principal() str
        +mostrar_menu_categorias() str
        +mostrar_lista_juegos(titulo, juegos)
        +mostrar_top_10(juegos)
        +mostrar_tarjeta_recomendaciones(juego_base, recs)
        +mostrar_jerarquia_arbol(arbol)
        +mostrar_recorrido_bfs(arbol)
        +mostrar_recorrido_dfs(arbol)
        +pedir_texto(mensaje) str
        +seleccionar_genero(generos) str
    }

    CatalogoJuegos *-- Juego : almacena lista
    CatalogoJuegos *-- ArbolBinarioBusqueda : integra (TP3)
    CatalogoJuegos *-- ArbolAVL : integra (TP4)
    CatalogoJuegos *-- ArbolGeneral : integra (TP5)
    CatalogoJuegos *-- MaxHeap : integra (TP6)
    CatalogoJuegos *-- Grafo : integra (TP7)

    ArbolBinarioBusqueda ..> Juego : guarda referencia
    ArbolAVL ..> Juego : indexa por titulo
    ArbolGeneral ..> Juego : almacena en hojas
    MaxHeap ..> Juego : ordena por calificacion
    Grafo ..> Juego : nodos y conexiones

    InterfazConsola ..> CatalogoJuegos : consulta operaciones
```
