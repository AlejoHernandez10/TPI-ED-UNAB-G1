import json
from typing import List, Set, Optional
from modelos.juego import Juego
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import MaxHeap
from estructuras.grafo import Grafo


class CatalogoJuegos:
    """
    Catalogo de videojuegos de NextGame.
    Integra BST, AVL, Arbol General, Max-Heap y Grafo.
    """

    def __init__(self):
        self._juegos: List[Juego] = []
        self._bst: ArbolBinarioBusqueda = ArbolBinarioBusqueda()
        self._avl: ArbolAVL = ArbolAVL()
        self._arbol_categorias: ArbolGeneral = ArbolGeneral()
        self._heap: MaxHeap = MaxHeap()
        self._grafo: Grafo = Grafo()

    @property
    def avl(self) -> ArbolAVL:
        return self._avl

    @property
    def bst(self) -> ArbolBinarioBusqueda:
        return self._bst

    @property
    def arbol_categorias(self) -> ArbolGeneral:
        return self._arbol_categorias

    @property
    def heap(self) -> MaxHeap:
        return self._heap

    @property
    def grafo(self) -> Grafo:
        return self._grafo

    def cargar_desde_json(self, ruta_archivo: str) -> None:
        """Carga los videojuegos desde un JSON y los indexa en todas las estructuras."""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                datos = json.load(file)
                self._juegos = []
                self._bst = ArbolBinarioBusqueda()
                self._avl = ArbolAVL()
                self._arbol_categorias = ArbolGeneral()
                self._arbol_categorias.establecer_raiz("Catálogo NextGame", "Jerarquía de Videojuegos por Categoría")
                self._heap = MaxHeap()
                self._grafo = Grafo()

                generos_creados: Set[str] = set()

                for item in datos:
                    juego = Juego(
                        id_juego=item['id'],
                        titulo=item['titulo'],
                        generos=item['generos'],
                        desarrollador=item['desarrollador'],
                        calificacion=item['calificacion'],
                        anio_publicacion=item['anioPublicacion'],
                        web=item.get('web', '')
                    )
                    self._juegos.append(juego)

                    # BST (TP3)
                    self._bst.insertar(juego.titulo, juego)

                    # Arbol AVL balanceado (TP4)
                    self._avl.insertar(juego.titulo, juego)

                    # Heap para el Top 10 (TP6)
                    self._heap.insertar(juego)

                    # Agregamos el vertice al grafo (TP7)
                    self._grafo.agregar_vertice(juego)

                    # Arbol General por categorias (TP5): Raiz -> Generos -> Juegos
                    for genero in juego.generos:
                        gen_limpio = genero.strip()
                        if gen_limpio not in generos_creados:
                            self._arbol_categorias.agregar_hijo(
                                "Catálogo NextGame",
                                gen_limpio,
                                f"Categoría {gen_limpio}"
                            )
                            generos_creados.add(gen_limpio)

                        self._arbol_categorias.agregar_hijo(gen_limpio, juego.titulo, juego)

                # Conectamos en el grafo los juegos que comparten generos (TP7)
                total = len(self._juegos)
                for i in range(total):
                    for j in range(i + 1, total):
                        j1 = self._juegos[i]
                        j2 = self._juegos[j]
                        comunes = j1.generos_en_comun(j2)
                        # si tienen generos en comun, creamos la arista con ese peso
                        if comunes > 0:
                            self._grafo.agregar_arista(j1, j2, peso=comunes)

            print(f"[OK] Se cargaron {len(self._juegos)} videojuegos.")
            print(f"     * Árbol AVL: altura {self._avl.obtener_altura()}, balance {self._avl.obtener_balance()}")
            print(f"     * Árbol General: {self._arbol_categorias.cantidad_nodos()} nodos, {len(generos_creados)} categorías")
            print(f"     * Max-Heap (TP6): {len(self._heap)} juegos cargados")
            print(f"     * Grafo (TP7): {self._grafo.cantidad_vertices()} vértices, {self._grafo.cantidad_aristas()} conexiones")
        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo '{ruta_archivo}'.")
        except json.JSONDecodeError:
            print(f"[ERROR] El archivo '{ruta_archivo}' no es un JSON válido.")

    # --- BUSQUEDA CON AVL ---
    def buscar_por_titulo(self, titulo: str) -> List[Juego]:
        """Busca videojuegos usando el Arbol AVL."""
        resultado = self._avl.buscar(titulo)
        if resultado:
            return [resultado]

        palabra = titulo.strip().lower()
        return [j for j in self._avl.inorder() if palabra in j.titulo.lower()]

    # --- CATEGORIAS CON ARBOL GENERAL ---
    def obtener_arbol_categorias(self) -> ArbolGeneral:
        return self._arbol_categorias

    # --- CONSULTAS Y EXPLORACION ---
    def obtener_por_genero(self, genero: str) -> List[Juego]:
        return [j for j in self._avl.inorder() if j.tiene_genero(genero)]

    def obtener_todos_los_generos(self) -> List[str]:
        todos: Set[str] = set()
        for j in self._avl.inorder():
            todos.update(j.generos)
        return sorted(list(todos))

    # --- RELACIONADOS Y RECOMENDACIONES CON GRAFOS (TP7) ---
    def obtener_relacionados(self, juego_base: Juego, limite: int = 5) -> List[Juego]:
        """Busca en el grafo los vecinos conectados al juego y los ordena por similitud."""
        vecinos = self._grafo.obtener_vecinos(juego_base.id)
        # ordenamos primero por cantidad de generos en comun (peso) y despues por nota
        vecinos_ordenados = sorted(vecinos, key=lambda item: (item[1], item[0].calificacion), reverse=True)
        return [juego for juego, _ in vecinos_ordenados[:limite]]

    def obtener_recomendaciones(self, juego_base: Juego, limite: int = 3) -> List[Juego]:
        """Toma los vecinos del grafo y devuelve los de mejor calificacion."""
        relacionados = self.obtener_relacionados(juego_base, limite=limite * 2)
        recomendaciones = sorted(relacionados, key=lambda j: j.calificacion, reverse=True)
        return recomendaciones[:limite]

    # --- RANKINGS CON MAX-HEAP (TP6) ---
    def obtener_top_n(self, n: int = 10) -> List[Juego]:
        """Devuelve el Top N usando la estructura Max-Heap propia."""
        return self._heap.obtener_top_n(n)
