# estructuras/heap.py

class MaxHeap:
    def __init__(self):
        # aca guardamos los elementos en una lista comun
        # cada elemento sera una tupla: (calificacion, juego)
        self.datos = []

    def insertar(self, juego):
        # metemos el juego al final de la lista
        self.datos.append((juego.calificacion, juego))
        # lo hacemos subir a su lugar
        self._subir(len(self.datos) - 1)

    def _subir(self, indice):
        # mientras no estemos en la raiz
        while indice > 0:
            padre = (indice - 1) // 2
            # si el actual tiene mejor nota que su padre, los cambiamos
            if self.datos[indice][0] > self.datos[padre][0]:
                self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
                indice = padre
            else:
                break

    def extraer_maximo(self):
        # si el heap esta vacio devolvemos None
        if not self.datos:
            return None

        # si queda solo un elemento lo sacamos directo
        if len(self.datos) == 1:
            return self.datos.pop()[1]

        # guardamos el mejor (la raiz)
        maximo = self.datos[0][1]
        # pasamos el ultimo elemento a la raiz
        self.datos[0] = self.datos.pop()
        # lo acomodamos para abajo
        self._bajar(0)

        return maximo

    def _bajar(self, indice):
        n = len(self.datos)
        while True:
            hijo_izq = 2 * indice + 1
            hijo_der = 2 * indice + 2
            mayor = indice

            # nos fijamos si el hijo izquierdo tiene mejor nota
            if hijo_izq < n and self.datos[hijo_izq][0] > self.datos[mayor][0]:
                mayor = hijo_izq

            # nos fijamos si el hijo derecho tiene mejor nota que el mayor hasta ahora
            if hijo_der < n and self.datos[hijo_der][0] > self.datos[mayor][0]:
                mayor = hijo_der

            # si alguno de los hijos es mayor, cambiamos de lugar y seguimos bajando
            if mayor != indice:
                self.datos[indice], self.datos[mayor] = self.datos[mayor], self.datos[indice]
                indice = mayor
            else:
                break

    def obtener_top_n(self, n):
        # hacemos una copia rapida de la lista para no vaciar el heap original
        copia = MaxHeap()
        copia.datos = list(self.datos)

        top = []
        cantidad = min(n, len(copia.datos))
        for _ in range(cantidad):
            top.append(copia.extraer_maximo())

        return top

    def __len__(self):
        return len(self.datos)
