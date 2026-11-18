# estructuras/avl.py

class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave.strip().lower()
        self.valor = valor
        self.altura = 1
        self.izquierdo = None
        self.derecho = None

    def __repr__(self):
        return f"NodoAVL(clave='{self.clave}', valor={self.valor}, altura={self.altura})"


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        # devuelve la altura del nodo o 0 si es None
        return nodo.altura if nodo else 0

    def obtener_altura(self):
        # devuelve la altura total del arbol avl
        return self._altura(self.raiz)

    def _factor_balance(self, nodo):
        # balance = altura(izq) - altura(der)
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def obtener_balance(self, nodo=None):
        # devuelve el balance del nodo o de la raiz si no se pasa ninguno
        nodo_a_evaluar = nodo if nodo is not None else self.raiz
        return self._factor_balance(nodo_a_evaluar)

    def _rotacion_derecha(self, y):
        # rotacion simple a la derecha
        x = y.izquierdo
        if x is None:
            return y
        t2 = x.derecho

        # hacemos la rotacion
        x.derecho = y
        y.izquierdo = t2

        # recalculamos alturas
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))

        return x

    def _rotacion_izquierda(self, x):
        # rotacion simple a la izquierda
        y = x.derecho
        if y is None:
            return x
        t2 = y.izquierdo

        # hacemos la rotacion
        y.izquierdo = x
        x.derecho = t2

        # recalculamos alturas
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))

        return y

    def _rotacion_doble_izq_der(self, nodo):
        # rotacion doble izquierda-derecha (LR)
        if nodo.izquierdo is not None:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
        return self._rotacion_derecha(nodo)

    def _rotacion_doble_der_izq(self, nodo):
        # rotacion doble derecha-izquierda (RL)
        if nodo.derecho is not None:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
        return self._rotacion_izquierda(nodo)

    def insertar(self, clave, valor):
        # inserta manteniendo el balance avl
        clave_norm = clave.strip().lower()
        self.raiz = self._insertar_recursivo(self.raiz, clave_norm, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        # 1. insercion normal como bst
        if nodo is None:
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            # si la clave ya existe actualizamos el valor
            nodo.valor = valor
            return nodo

        # 2. actualizamos la altura del nodo actual
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

        # 3. calculamos el balance
        balance = self._factor_balance(nodo)

        # 4. aplicamos rotaciones si quedo desbalanceado
        # caso 1: izquierda izquierda (LL)
        if balance > 1 and self._factor_balance(nodo.izquierdo) >= 0:
            return self._rotacion_derecha(nodo)

        # caso 2: izquierda derecha (LR)
        if balance > 1 and self._factor_balance(nodo.izquierdo) < 0:
            return self._rotacion_doble_izq_der(nodo)

        # caso 3: derecha derecha (RR)
        if balance < -1 and self._factor_balance(nodo.derecho) <= 0:
            return self._rotacion_izquierda(nodo)

        # caso 4: derecha izquierda (RL)
        if balance < -1 and self._factor_balance(nodo.derecho) > 0:
            return self._rotacion_doble_der_izq(nodo)

        return nodo

    def buscar(self, clave):
        # busca un elemento por su clave exacta
        return self._buscar_recursivo(self.raiz, clave.strip().lower())

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None

        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo.derecho, clave)

    def inorder(self):
        # recorrido inorden: izquierda, raiz, derecha
        resultados = []
        self._inorder_recursivo(self.raiz, resultados)
        return resultados

    def _inorder_recursivo(self, nodo, lista):
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, lista)

    def preorder(self):
        # recorrido preorden: raiz, izquierda, derecha
        resultados = []
        self._preorder_recursivo(self.raiz, resultados)
        return resultados

    def _preorder_recursivo(self, nodo, lista):
        if nodo:
            lista.append(nodo.valor)
            self._preorder_recursivo(nodo.izquierdo, lista)
            self._preorder_recursivo(nodo.derecho, lista)

    def postorder(self):
        # recorrido postorden: izquierda, derecha, raiz
        resultados = []
        self._postorder_recursivo(self.raiz, resultados)
        return resultados

    def _postorder_recursivo(self, nodo, lista):
        if nodo:
            self._postorder_recursivo(nodo.izquierdo, lista)
            self._postorder_recursivo(nodo.derecho, lista)
            lista.append(nodo.valor)

    def esta_balanceado(self):
        # revisa si el arbol cumple la condicion de avl en todos sus nodos
        return self._esta_balanceado_recursivo(self.raiz)[0]

    def _esta_balanceado_recursivo(self, nodo):
        if nodo is None:
            return True, 0

        bal_izq, alt_izq = self._esta_balanceado_recursivo(nodo.izquierdo)
        bal_der, alt_der = self._esta_balanceado_recursivo(nodo.derecho)

        actual_balance = alt_izq - alt_der
        es_balanceado = bal_izq and bal_der and abs(actual_balance) <= 1
        altura_calculada = 1 + max(alt_izq, alt_der)

        return es_balanceado, altura_calculada
