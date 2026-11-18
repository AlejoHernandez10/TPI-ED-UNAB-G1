"""
Script para generar las imágenes PNG de alta resolución de los diagramas Mermaid de NextGame.
Utiliza las APIs públicas de renderizado de Mermaid (Kroki y Mermaid.ink como fallback).
"""
import os
import urllib.request
import base64
import json

DIAGRAMA_CLASES = """classDiagram
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
"""

DIAGRAMA_DATOS = """flowchart TD
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
"""


def render_mermaid_kroki(mermaid_code: str) -> bytes:
    url = "https://kroki.io/mermaid/png"
    req = urllib.request.Request(
        url,
        data=mermaid_code.encode("utf-8"),
        headers={
            "Content-Type": "text/plain; charset=utf-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) NextGame-Diagram-Renderer",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def render_mermaid_ink(mermaid_code: str) -> bytes:
    payload = {"code": mermaid_code, "mermaid": {"theme": "default"}}
    json_bytes = json.dumps(payload).encode("utf-8")
    b64_str = base64.urlsafe_b64encode(json_bytes).decode("ascii")
    url = f"https://mermaid.ink/img/{b64_str}?scale=2"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) NextGame-Diagram-Renderer",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def generar_imagen(nombre: str, mermaid_code: str, ruta_salida: str):
    print(f"[*] Generando {nombre} -> {ruta_salida}...")
    png_bytes = None
    try:
        png_bytes = render_mermaid_kroki(mermaid_code)
        print(f"    [OK] Renderizado exitoso con Kroki. Tamaño: {len(png_bytes):,} bytes")
    except Exception as e_kroki:
        print(f"    [!] Kroki falló ({e_kroki}), intentando con Mermaid.ink...")
        try:
            png_bytes = render_mermaid_ink(mermaid_code)
            print(f"    [OK] Renderizado exitoso con Mermaid.ink. Tamaño: {len(png_bytes):,} bytes")
        except Exception as e_ink:
            raise RuntimeError(f"Error renderizando {nombre} en ambos servicios: Kroki={e_kroki}, Ink={e_ink}")

    if png_bytes:
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        with open(ruta_salida, "wb") as f:
            f.write(png_bytes)
        print(f"    [+] Guardado en: {ruta_salida} ({os.path.getsize(ruta_salida):,} bytes)")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, "docs")
    os.makedirs(docs_dir, exist_ok=True)

    ruta_clases = os.path.join(docs_dir, "03-diagrama-clases.png")
    ruta_datos = os.path.join(docs_dir, "04-diagrama-datos.png")

    generar_imagen("Diagrama de Clases UML", DIAGRAMA_CLASES, ruta_clases)
    generar_imagen("Diagrama de Flujo de Datos", DIAGRAMA_DATOS, ruta_datos)

    # Validaciones requeridas
    for ruta in [ruta_clases, ruta_datos]:
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No se encontró el archivo generado: {ruta}")
        tam = os.path.getsize(ruta)
        if tam <= 15 * 1024:
            raise ValueError(f"El archivo {ruta} tiene un tamaño de {tam} bytes (menor a 15 KB)")
        print(f"[VERIFICACIÓN OK] {os.path.basename(ruta)} -> {tam:,} bytes (> 15 KB)")


if __name__ == "__main__":
    main()
