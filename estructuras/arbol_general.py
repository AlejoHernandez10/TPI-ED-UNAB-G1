# estructuras/arbol_general.py
from collections import deque

class NodoGeneral:
    def __init__(self, clave, valor=None):
        self.clave = clave.strip()
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        # agrega un nodo a la lista de hijos
        self.hijos.append(nodo_hijo)

    def es_hoja(self):
        # revisa si el nodo no tiene hijos
        return len(self.hijos) == 0

    def __repr__(self):
        return f"NodoGeneral(clave='{self.clave}', valor={self.valor}, hijos={len(self.hijos)})"

    def __str__(self):
        if self.valor is not None:
            return f"{self.clave} ({self.valor})"
        return self.clave


class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        # devuelve true si el arbol no tiene raiz
        return self.raiz is None

    def establecer_raiz(self, clave, valor=None):
        # crea y asigna la raiz del arbol
        self.raiz = NodoGeneral(clave=clave, valor=valor)
        return self.raiz

    def agregar_hijo(self, clave_padre, clave_hijo, valor_hijo=None):
        # busca al padre y le agrega un nuevo hijo
        padre = self.buscar(clave_padre)
        if padre is None:
            return False

        nuevo_hijo = NodoGeneral(clave=clave_hijo, valor=valor_hijo)
        padre.agregar_hijo(nuevo_hijo)
        return True

    def buscar(self, clave):
        # busca un nodo por clave usando dfs recursivo
        if self.raiz is None:
            return None

        clave_normalizada = clave.strip().lower()
        return self._buscar_recursivo(self.raiz, clave_normalizada)

    def _buscar_recursivo(self, nodo, clave_buscada):
        if nodo.clave.strip().lower() == clave_buscada:
            return nodo

        for hijo in nodo.hijos:
            resultado = self._buscar_recursivo(hijo, clave_buscada)
            if resultado is not None:
                return resultado

        return None

    def recorrido_amplitud(self):
        # recorrido por niveles usando una cola
        if self.raiz is None:
            return []

        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual)
            for hijo in nodo_actual.hijos:
                cola.append(hijo)

        return resultado

    def recorrido_profundidad(self):
        # recorrido en profundidad (dfs)
        if self.raiz is None:
            return []

        resultado = []
        self._dfs_recursivo(self.raiz, resultado)
        return resultado

    def _dfs_recursivo(self, nodo, lista):
        lista.append(nodo)
        for hijo in nodo.hijos:
            self._dfs_recursivo(hijo, lista)

    def altura(self):
        # calcula la altura del arbol
        if self.raiz is None:
            return 0
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if not nodo.hijos:
            return 1
        return 1 + max(self._altura_recursiva(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self):
        # devuelve la cantidad total de nodos
        return len(self.recorrido_amplitud())

    def obtener_hojas(self):
        # devuelve todos los nodos hoja
        return [nodo for nodo in self.recorrido_profundidad() if nodo.es_hoja()]

    def obtener_hijos(self, clave):
        # devuelve la lista de hijos directos del nodo
        nodo = self.buscar(clave)
        if nodo is None:
            return []
        return list(nodo.hijos)

    def obtener_camino(self, clave):
        # obtiene el camino desde la raiz hasta el nodo buscado
        if self.raiz is None:
            return None

        clave_normalizada = clave.strip().lower()
        camino_actual = []

        if self._construir_camino(self.raiz, clave_normalizada, camino_actual):
            return camino_actual
        return None

    def _construir_camino(self, nodo, clave_buscada, camino):
        camino.append(nodo.clave)

        if nodo.clave.strip().lower() == clave_buscada:
            return True

        for hijo in nodo.hijos:
            if self._construir_camino(hijo, clave_buscada, camino):
                return True

        camino.pop()
        return False

    def mostrar_arbol(self, usar_unicode=False):
        # arma el arbol en formato texto con ramas
        if self.raiz is None:
            return "Arbol vacio"

        lineas = []

        c_intermedio = "├── " if usar_unicode else "|-- "
        c_final = "└── " if usar_unicode else "\\-- "
        e_vertical = "│   " if usar_unicode else "|   "
        e_vacio = "    "

        def _formatear_nodo(nodo):
            if nodo.valor is None:
                return nodo.clave

            # si guarda un juego mostramos anio y calificacion
            if hasattr(nodo.valor, 'anio_publicacion') and hasattr(nodo.valor, 'calificacion'):
                return f"{nodo.clave} ({nodo.valor.anio_publicacion}) [Rating: {nodo.valor.calificacion}]"

            # si es otro dato lo mostramos como texto
            valor_str = str(nodo.valor).replace("⭐", "Rating:")
            return f"{nodo.clave} ({valor_str})"

        def _recorrer(nodo, prefijo="", es_ultimo=True, es_raiz=True):
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

    def __len__(self):
        return self.cantidad_nodos()

    def __repr__(self):
        return f"ArbolGeneral(raiz={repr(self.raiz)}, total_nodos={self.cantidad_nodos()})"
