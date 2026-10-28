# estructuras/grafo.py

class Grafo:
    def __init__(self):
        # lista de adyacencia usando un diccionario comun
        # clave: id del juego
        # valor: lista de tuplas con (juego_vecino, peso)
        self.vertices = {}

    def agregar_vertice(self, juego):
        # si el juego todavia no esta en el grafo, le creamos su lista de vecinos vacia
        if juego.id not in self.vertices:
            self.vertices[juego.id] = []

    def agregar_arista(self, juego1, juego2, peso=1):
        # nos aseguramos de que ambos esten registrados
        self.agregar_vertice(juego1)
        self.agregar_vertice(juego2)

        # como el grafo no es dirigido, conectamos de ida y de vuelta
        if not self.estan_conectados(juego1.id, juego2.id):
            self.vertices[juego1.id].append((juego2, peso))
            self.vertices[juego2.id].append((juego1, peso))

    def estan_conectados(self, id1, id2):
        # revisa si ya existe conexion entre id1 e id2
        if id1 not in self.vertices:
            return False
        for vecino, _ in self.vertices[id1]:
            if vecino.id == id2:
                return True
        return False

    def obtener_vecinos(self, id_juego):
        # devuelve la lista de vecinos (juego, peso) de ese juego
        return self.vertices.get(id_juego, [])

    def cantidad_vertices(self):
        return len(self.vertices)

    def cantidad_aristas(self):
        # sumamos todas las conexiones y dividimos por 2 porque estan duplicadas (ida y vuelta)
        total = sum(len(vecinos) for vecinos in self.vertices.values())
        return total // 2
