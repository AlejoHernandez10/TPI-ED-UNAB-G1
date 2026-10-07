from typing import Optional, List, Any


class NodoAVL:
    """Nodo para la estructura de Árbol AVL."""

    def __init__(self, clave: str, valor: Any):
        self.clave: str = clave.strip().lower()
        self.valor: Any = valor
        self.altura: int = 1
        self.izquierdo: Optional['NodoAVL'] = None
        self.derecho: Optional['NodoAVL'] = None

    def __repr__(self) -> str:
        return f"NodoAVL(clave='{self.clave}', valor={self.valor}, altura={self.altura})"


class ArbolAVL:
    """Árbol Binario de Búsqueda Auto-balanceado (AVL)."""

    def __init__(self):
        self.raiz: Optional[NodoAVL] = None

    # --- CÁLCULO DE ALTURA Y FACTOR DE BALANCE ---
    def _altura(self, nodo: Optional[NodoAVL]) -> int:
        """Devuelve la altura de un nodo o 0 si es None."""
        return nodo.altura if nodo else 0

    def obtener_altura(self) -> int:
        """Devuelve la altura total del árbol AVL (altura de la raíz)."""
        return self._altura(self.raiz)

    def _factor_balance(self, nodo: Optional[NodoAVL]) -> int:
        """
        Calcula el factor de balance de un nodo:
        balance = altura(izq) - altura(der)
        """
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def obtener_balance(self, nodo: Optional[NodoAVL] = None) -> int:
        """
        Devuelve el factor de balance del nodo dado, o de la raíz si no se especifica.
        """
        nodo_a_evaluar = nodo if nodo is not None else self.raiz
        return self._factor_balance(nodo_a_evaluar)

    # --- ROTACIONES ---
    def _rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
        r"""
        Rotación simple a la derecha.
             y                x
            / \              / \
           x   T3    ==>    T1  y
          / \                  / \
         T1  T2               T2  T3
        """
        x = y.izquierdo
        if x is None:
            return y
        t2 = x.derecho

        # Realizar rotación
        x.derecho = y
        y.izquierdo = t2

        # Actualizar alturas (primero el hijo y, luego la nueva raíz x)
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))

        return x

    def _rotacion_izquierda(self, x: NodoAVL) -> NodoAVL:
        r"""
        Rotación simple a la izquierda.
           x                   y
          / \                 / \
         T1  y       ==>     x   T3
            / \             / \
           T2  T3          T1  T2
        """
        y = x.derecho
        if y is None:
            return x
        t2 = y.izquierdo

        # Realizar rotación
        y.izquierdo = x
        x.derecho = t2

        # Actualizar alturas (primero el hijo x, luego la nueva raíz y)
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))

        return y

    def _rotacion_doble_izq_der(self, nodo: NodoAVL) -> NodoAVL:
        """
        Rotación doble Izquierda-Derecha (LR).
        Primero rotación simple a la izquierda sobre el hijo izquierdo,
        seguido de rotación simple a la derecha sobre el nodo actual.
        """
        if nodo.izquierdo is not None:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
        return self._rotacion_derecha(nodo)

    def _rotacion_doble_der_izq(self, nodo: NodoAVL) -> NodoAVL:
        """
        Rotación doble Derecha-Izquierda (RL).
        Primero rotación simple a la derecha sobre el hijo derecho,
        seguido de rotación simple a la izquierda sobre el nodo actual.
        """
        if nodo.derecho is not None:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
        return self._rotacion_izquierda(nodo)

    # --- INSERCIÓN ---
    def insertar(self, clave: str, valor: Any) -> None:
        """Inserta un par clave-valor en el árbol AVL manteniendo el balance."""
        clave_norm = clave.strip().lower()
        self.raiz = self._insertar_recursivo(self.raiz, clave_norm, valor)

    def _insertar_recursivo(self, nodo: Optional[NodoAVL], clave: str, valor: Any) -> NodoAVL:
        # 1. Inserción normal de BST
        if nodo is None:
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            # Actualizar valor si la clave ya existe
            nodo.valor = valor
            return nodo

        # 2. Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

        # 3. Obtener el factor de balance
        balance = self._factor_balance(nodo)

        # 4. Aplicar rotaciones si el nodo se desbalanceó
        # Caso 1: Desbalance Izquierda-Izquierda (LL)
        if balance > 1 and self._factor_balance(nodo.izquierdo) >= 0:
            return self._rotacion_derecha(nodo)

        # Caso 2: Desbalance Izquierda-Derecha (LR)
        if balance > 1 and self._factor_balance(nodo.izquierdo) < 0:
            return self._rotacion_doble_izq_der(nodo)

        # Caso 3: Desbalance Derecha-Derecha (RR)
        if balance < -1 and self._factor_balance(nodo.derecho) <= 0:
            return self._rotacion_izquierda(nodo)

        # Caso 4: Desbalance Derecha-Izquierda (RL)
        if balance < -1 and self._factor_balance(nodo.derecho) > 0:
            return self._rotacion_doble_der_izq(nodo)

        return nodo

    # --- BÚSQUEDA ---
    def buscar(self, clave: str) -> Optional[Any]:
        """Busca un elemento en el árbol AVL dada su clave exacta."""
        return self._buscar_recursivo(self.raiz, clave.strip().lower())

    def _buscar_recursivo(self, nodo: Optional[NodoAVL], clave: str) -> Optional[Any]:
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
        resultados: List[Any] = []
        self._inorder_recursivo(self.raiz, resultados)
        return resultados

    def _inorder_recursivo(self, nodo: Optional[NodoAVL], lista: List[Any]) -> None:
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, lista)

    def preorder(self) -> List[Any]:
        """Recorrido Preorden (Raíz, Izquierda, Derecha)."""
        resultados: List[Any] = []
        self._preorder_recursivo(self.raiz, resultados)
        return resultados

    def _preorder_recursivo(self, nodo: Optional[NodoAVL], lista: List[Any]) -> None:
        if nodo:
            lista.append(nodo.valor)
            self._preorder_recursivo(nodo.izquierdo, lista)
            self._preorder_recursivo(nodo.derecho, lista)

    def postorder(self) -> List[Any]:
        """Recorrido Postorden (Izquierda, Derecha, Raíz)."""
        resultados: List[Any] = []
        self._postorder_recursivo(self.raiz, resultados)
        return resultados

    def _postorder_recursivo(self, nodo: Optional[NodoAVL], lista: List[Any]) -> None:
        if nodo:
            self._postorder_recursivo(nodo.izquierdo, lista)
            self._postorder_recursivo(nodo.derecho, lista)
            lista.append(nodo.valor)

    # --- VALIDACIÓN DE BALANCE ---
    def esta_balanceado(self) -> bool:
        """Verifica si todos los nodos cumplen la propiedad AVL (-1 <= balance <= 1)."""
        return self._esta_balanceado_recursivo(self.raiz)[0]

    def _esta_balanceado_recursivo(self, nodo: Optional[NodoAVL]) -> tuple[bool, int]:
        if nodo is None:
            return True, 0

        bal_izq, alt_izq = self._esta_balanceado_recursivo(nodo.izquierdo)
        bal_der, alt_der = self._esta_balanceado_recursivo(nodo.derecho)

        actual_balance = alt_izq - alt_der
        es_balanceado = bal_izq and bal_der and abs(actual_balance) <= 1
        altura_calculada = 1 + max(alt_izq, alt_der)

        return es_balanceado, altura_calculada
