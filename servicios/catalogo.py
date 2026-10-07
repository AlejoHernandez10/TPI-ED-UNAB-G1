import json
from typing import List, Set, Optional
from modelos.juego import Juego
from estructuras.arbol_binario import ArbolBinarioBusqueda
from estructuras.avl import ArbolAVL
from estructuras.arbol_general import ArbolGeneral


class CatalogoJuegos:
    """
    Catálogo de videojuegos de NextGame.
    Integra BST, AVL y Árbol General para organizar los juegos y categorías.
    """

    def __init__(self):
        self._juegos: List[Juego] = []
        self._bst: ArbolBinarioBusqueda = ArbolBinarioBusqueda()
        self._avl: ArbolAVL = ArbolAVL()
        self._arbol_categorias: ArbolGeneral = ArbolGeneral()

    @property
    def avl(self) -> ArbolAVL:
        return self._avl

    @property
    def bst(self) -> ArbolBinarioBusqueda:
        return self._bst

    @property
    def arbol_categorias(self) -> ArbolGeneral:
        return self._arbol_categorias

    def cargar_desde_json(self, ruta_archivo: str) -> None:
        """Carga los videojuegos desde un JSON y los indexa en BST, AVL y Árbol General."""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                datos = json.load(file)
                self._juegos = []
                self._bst = ArbolBinarioBusqueda()
                self._avl = ArbolAVL()
                self._arbol_categorias = ArbolGeneral()
                self._arbol_categorias.establecer_raiz("Catálogo NextGame", "Jerarquía de Videojuegos por Categoría")

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

                    # Árbol AVL balanceado (TP4)
                    self._avl.insertar(juego.titulo, juego)

                    # Árbol General por categorías (TP5): Raíz -> Géneros -> Juegos
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

            print(f"[OK] Se cargaron {len(self._juegos)} videojuegos.")
            print(f"     * Árbol AVL: altura {self._avl.obtener_altura()}, balance {self._avl.obtener_balance()}")
            print(f"     * Árbol General: {self._arbol_categorias.cantidad_nodos()} nodos, {len(generos_creados)} categorías")
        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo '{ruta_archivo}'.")
        except json.JSONDecodeError:
            print(f"[ERROR] El archivo '{ruta_archivo}' no es un JSON válido.")

    # --- BÚSQUEDA INTEGRADA CON AVL ---
    def buscar_por_titulo(self, titulo: str) -> List[Juego]:
        """
        Busca videojuegos usando el Árbol AVL:
        1. Intenta búsqueda exacta balanceada O(log N).
        2. Si no hay coincidencia exacta, busca coincidencias parciales con el inorden.
        """
        resultado = self._avl.buscar(titulo)
        if resultado:
            return [resultado]

        # Búsqueda por subcadena sobre el inorden del AVL
        palabra = titulo.strip().lower()
        return [j for j in self._avl.inorder() if palabra in j.titulo.lower()]

    # --- JERARQUÍA CON ÁRBOL GENERAL ---
    def obtener_arbol_categorias(self) -> ArbolGeneral:
        """Devuelve el Árbol General con la jerarquía de categorías y videojuegos."""
        return self._arbol_categorias

    # --- MÉTODOS DE CONSULTA Y EXPLORACIÓN ---
    def obtener_por_genero(self, genero: str) -> List[Juego]:
        return [j for j in self._avl.inorder() if j.tiene_genero(genero)]

    def obtener_todos_los_generos(self) -> List[str]:
        todos: Set[str] = set()
        for j in self._avl.inorder():
            todos.update(j.generos)
        return sorted(list(todos))

    def obtener_relacionados(self, juego_base: Juego, limite: int = 5) -> List[Juego]:
        candidatos = []
        for j in self._avl.inorder():
            if j.id != juego_base.id:
                coincidencias = juego_base.generos_en_comun(j)
                if coincidencias > 0:
                    candidatos.append((j, coincidencias))

        candidatos.sort(key=lambda item: (item[1], item[0].calificacion), reverse=True)
        return [j for j, _ in candidatos[:limite]]

    def obtener_recomendaciones(self, juego_base: Juego, limite: int = 3) -> List[Juego]:
        relacionados = self.obtener_relacionados(juego_base, limite=limite * 2)
        recomendaciones = sorted(relacionados, key=lambda j: j.calificacion, reverse=True)
        return recomendaciones[:limite]

    def obtener_top_n(self, n: int = 10) -> List[Juego]:
        return sorted(self._avl.inorder(), key=lambda j: j.calificacion, reverse=True)[:n]