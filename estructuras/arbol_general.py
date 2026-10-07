from collections import deque
from typing import Optional, List, Any


class NodoGeneral:
    """Nodo para un Árbol General (puede tener cualquier cantidad de hijos)."""

    def __init__(self, clave: str, valor: Any = None):
        self.clave: str = clave.strip()
        self.valor: Any = valor
        self.hijos: List['NodoGeneral'] = []

    def agregar_hijo(self, nodo_hijo: 'NodoGeneral') -> None:
        """Agrega un nodo a la lista de hijos."""
        self.hijos.append(nodo_hijo)

    def es_hoja(self) -> bool:
        """Indica si el nodo es hoja (no tiene hijos)."""
        return len(self.hijos) == 0

    def __repr__(self) -> str:
        return f"NodoGeneral(clave='{self.clave}', valor={self.valor}, hijos={len(self.hijos)})"

    def __str__(self) -> str:
        if self.valor is not None:
            return f"{self.clave} ({self.valor})"
        return self.clave


class ArbolGeneral:
    """Árbol General (N-ario) para modelar la jerarquía de categorías y juegos."""

    def __init__(self):
        self.raiz: Optional[NodoGeneral] = None

    def es_vacio(self) -> bool:
        """Indica si el árbol está vacío."""
        return self.raiz is None

    # --- INSERCIÓN Y ESTRUCTURA ---
    def establecer_raiz(self, clave: str, valor: Any = None) -> NodoGeneral:
        """Crea y asigna el nodo raíz del árbol."""
        self.raiz = NodoGeneral(clave=clave, valor=valor)
        return self.raiz

    def agregar_hijo(self, clave_padre: str, clave_hijo: str, valor_hijo: Any = None) -> bool:
        """Busca el nodo padre y le agrega un nuevo hijo. Retorna True si lo encontró."""
        padre = self.buscar(clave_padre)
        if padre is None:
            return False

        nuevo_hijo = NodoGeneral(clave=clave_hijo, valor=valor_hijo)
        padre.agregar_hijo(nuevo_hijo)
        return True

    # --- BÚSQUEDA ---
    def buscar(self, clave: str) -> Optional[NodoGeneral]:
        """Busca un nodo por su clave usando DFS recursivo. Retorna el nodo o None."""
        if self.raiz is None:
            return None

        clave_normalizada = clave.strip().lower()
        return self._buscar_recursivo(self.raiz, clave_normalizada)

    def _buscar_recursivo(self, nodo: NodoGeneral, clave_buscada: str) -> Optional[NodoGeneral]:
        if nodo.clave.strip().lower() == clave_buscada:
            return nodo

        for hijo in nodo.hijos:
            resultado = self._buscar_recursivo(hijo, clave_buscada)
            if resultado is not None:
                return resultado

        return None

    # --- RECORRIDOS ---
    def recorrido_amplitud(self) -> List[NodoGeneral]:
        """Recorrido por niveles (BFS) usando una cola FIFO."""
        if self.raiz is None:
            return []

        resultado: List[NodoGeneral] = []
        cola: deque[NodoGeneral] = deque([self.raiz])

        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual)
            for hijo in nodo_actual.hijos:
                cola.append(hijo)

        return resultado

    def recorrido_profundidad(self) -> List[NodoGeneral]:
        """Recorrido en profundidad (DFS) en preorden."""
        if self.raiz is None:
            return []

        resultado: List[NodoGeneral] = []
        self._dfs_recursivo(self.raiz, resultado)
        return resultado

    def _dfs_recursivo(self, nodo: NodoGeneral, lista: List[NodoGeneral]) -> None:
        lista.append(nodo)
        for hijo in nodo.hijos:
            self._dfs_recursivo(hijo, lista)

    # --- MÉTODOS ÚTILES ---
    def altura(self) -> int:
        """Calcula la altura del árbol (0 si está vacío, 1 si solo tiene la raíz)."""
        if self.raiz is None:
            return 0
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo: NodoGeneral) -> int:
        if not nodo.hijos:
            return 1
        return 1 + max(self._altura_recursiva(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self) -> int:
        """Devuelve la cantidad total de nodos del árbol."""
        return len(self.recorrido_amplitud())

    def obtener_hojas(self) -> List[NodoGeneral]:
        """Devuelve todos los nodos hoja (los que no tienen hijos)."""
        return [nodo for nodo in self.recorrido_profundidad() if nodo.es_hoja()]

    def obtener_hijos(self, clave: str) -> List[NodoGeneral]:
        """Devuelve la lista de hijos directos del nodo indicado."""
        nodo = self.buscar(clave)
        if nodo is None:
            return []
        return list(nodo.hijos)

    def obtener_camino(self, clave: str) -> Optional[List[str]]:
        """Obtiene la ruta de nombres desde la raíz hasta el nodo buscado."""
        if self.raiz is None:
            return None

        clave_normalizada = clave.strip().lower()
        camino_actual: List[str] = []

        if self._construir_camino(self.raiz, clave_normalizada, camino_actual):
            return camino_actual
        return None

    def _construir_camino(self, nodo: NodoGeneral, clave_buscada: str, camino: List[str]) -> bool:
        camino.append(nodo.clave)

        if nodo.clave.strip().lower() == clave_buscada:
            return True

        for hijo in nodo.hijos:
            if self._construir_camino(hijo, clave_buscada, camino):
                return True

        camino.pop()
        return False

    # --- VISUALIZACIÓN ---
    def mostrar_arbol(self, usar_unicode: bool = False) -> str:
        """Genera el árbol en formato texto con ramas e indentación."""
        if self.raiz is None:
            return "Árbol vacío"

        lineas: List[str] = []

        c_intermedio = "├── " if usar_unicode else "|-- "
        c_final = "└── " if usar_unicode else "\\-- "
        e_vertical = "│   " if usar_unicode else "|   "
        e_vacio = "    "

        def _formatear_nodo(nodo: NodoGeneral) -> str:
            if nodo.valor is None:
                return nodo.clave

            # Si el nodo guarda un juego, mostramos año y calificación
            if hasattr(nodo.valor, 'anio_publicacion') and hasattr(nodo.valor, 'calificacion'):
                return f"{nodo.clave} ({nodo.valor.anio_publicacion}) [Rating: {nodo.valor.calificacion}]"

            # Si es otro dato, lo mostramos como texto
            valor_str = str(nodo.valor).replace("⭐", "Rating:")
            return f"{nodo.clave} ({valor_str})"

        def _recorrer(nodo: NodoGeneral, prefijo: str = "", es_ultimo: bool = True, es_raiz: bool = True) -> None:
            if es_raiz:
                lineas.append(_formatear_nodo(nodo))
                nuevo_prefijo = ""
            else:
                conector = c_final if es_ultimo else c_intermedio
                lineas.append(f"{prefijo}{conector}{_formatear_nodo(nodo)}")
                nuevo_prefijo = prefijo + (e_vacio if es_ultimo else e_vertical)

            total_hijos = len(nodo.hijos)
            for i, hijo in enumerate(nodo.hijos):
                ultimo = (i == total_hijos - 1)
                _recorrer(hijo, nuevo_prefijo, ultimo, False)

        _recorrer(self.raiz)
        return "\n".join(lineas)

    def __len__(self) -> int:
        return self.cantidad_nodos()

    def __repr__(self) -> str:
        return f"ArbolGeneral(raiz={repr(self.raiz)}, total_nodos={self.cantidad_nodos()})"
