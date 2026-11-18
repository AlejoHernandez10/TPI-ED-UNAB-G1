# estructuras/arbol_binario.py

class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave.strip().lower()
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        # insertamos pasando la clave en minusculas
        self.raiz = self._insertar_recursivo(self.raiz, clave.strip().lower(), valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        # si llegamos a un nodo vacio creamos el nuevo nodo aca
        if nodo is None:
            return NodoArbol(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            # si la clave ya existe actualizamos el valor
            nodo.valor = valor

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
