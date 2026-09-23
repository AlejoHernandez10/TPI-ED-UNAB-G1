from typing import Optional, List, Any

class NodoArbol:
    def __init__(self, clave: str, valor: Any):
        self.clave: str = clave.strip().lower()
        self.valor: Any = valor
        self.izquierdo: Optional['NodoArbol'] = None
        self.derecho: Optional['NodoArbol'] = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz: Optional[NodoArbol] = None

    # --- INSERCIÓN ---
    def insertar(self, clave: str, valor: Any) -> None:
        """Inserta un nodo en el BST utilizando la clave en minúsculas."""
        self.raiz = self._insertar_recursivo(self.raiz, clave.strip().lower(), valor)

    def _insertar_recursivo(self, nodo: Optional[NodoArbol], clave: str, valor: Any) -> NodoArbol:
        if nodo is None:
            return NodoArbol(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor  # Actualiza si la clave ya existe

        return nodo

    # --- BÚSQUEDA ---
    def buscar(self, clave: str) -> Optional[Any]:
        """Busca un elemento en el BST dada su clave exacta."""
        return self._buscar_recursivo(self.raiz, clave.strip().lower())

    def _buscar_recursivo(self, nodo: Optional[NodoArbol], clave: str) -> Optional[Any]:
        if nodo is None:
            return None

        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo.derecho, clave)

    # --- RECORRIDOS ---
    def inorder(self) -> List[Any]:
        """Recorrido Inorden (Izquierda, Raíz, Derecha). Devuelve la lista ordenada por clave."""
        resultados = []
        self._inorder_recursivo(self.raiz, resultados)
        return resultados

    def _inorder_recursivo(self, nodo: Optional[NodoArbol], lista: List[Any]) -> None:
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, lista)

    def preorder(self) -> List[Any]:
        """Recorrido Preorden (Raíz, Izquierda, Derecha)."""
        resultados = []
        self._preorder_recursivo(self.raiz, resultados)
        return resultados

    def _preorder_recursivo(self, nodo: Optional[NodoArbol], lista: List[Any]) -> None:
        if nodo:
            lista.append(nodo.valor)
            self._preorder_recursivo(nodo.izquierdo, lista)
            self._preorder_recursivo(nodo.derecho, lista)

    def postorder(self) -> List[Any]:
        """Recorrido Postorden (Izquierda, Derecha, Raíz)."""
        resultados = []
        self._postorder_recursivo(self.raiz, resultados)
        return resultados

    def _postorder_recursivo(self, nodo: Optional[NodoArbol], lista: List[Any]) -> None:
        if nodo:
            self._postorder_recursivo(nodo.izquierdo, lista)
            self._postorder_recursivo(nodo.derecho, lista)
            lista.append(nodo.valor)