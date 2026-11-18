from collections import deque

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

    # --- RECORRIDOS (TP 8) ---

    def bfs(self, id_origen):
        # recorrido en anchura usando cola FIFO
        # explora por niveles de distancia desde el origen
        if id_origen not in self.vertices:
            return []

        cola = deque([id_origen])
        visitados = {id_origen}
        orden = []

        while cola:
            actual = cola.popleft()
            orden.append(actual)

            # revisamos los vecinos
            for vecino, _ in self.vertices[actual]:
                # marcamos apenas lo descubrimos para no meterlo dos veces a la cola
                if vecino.id not in visitados:
                    visitados.add(vecino.id)
                    cola.append(vecino.id)

        return orden

    def dfs(self, id_origen, visitados=None):
        # recorrido en profundidad usando recursion
        # se mete a fondo por una rama y vuelve atras con backtracking
        if visitados is None:
            visitados = set()

        if id_origen not in self.vertices or id_origen in visitados:
            return []

        visitados.add(id_origen)
        orden = [id_origen]

        for vecino, _ in self.vertices[id_origen]:
            if vecino.id not in visitados:
                orden.extend(self.dfs(vecino.id, visitados))

        return orden

    # --- CAMINO MINIMO (TP 9) ---

    def dijkstra(self, id_origen, id_destino):
        # si alguno de los dos juegos no esta en el grafo, no hay camino
        if id_origen not in self.vertices or id_destino not in self.vertices:
            return None, []

        # arrancamos todas las distancias en infinito, salvo el origen que es 0
        distancias = {v: float('inf') for v in self.vertices}
        distancias[id_origen] = 0

        # guardamos el padre de cada nodo para reconstruir la ruta hacia atras
        padres = {v: None for v in self.vertices}

        # conjunto de nodos pendientes de visitar
        no_visitados = set(self.vertices.keys())

        while no_visitados:
            # elegimos el nodo no visitado que tenga la distancia acumulada mas chica
            actual = min(no_visitados, key=lambda v: distancias[v])

            # si ya no podemos alcanzar mas nodos o llegamos al destino, cortamos
            if distancias[actual] == float('inf') or actual == id_destino:
                break

            no_visitados.remove(actual)

            # miramos los vecinos del nodo actual
            for vecino, generos_comunes in self.vertices[actual]:
                if vecino.id in no_visitados:
                    # costo de pasar de un juego al otro:
                    # mas generos en comun = menor costo de transicion
                    costo = max(1, 5 - generos_comunes)
                    nueva_distancia = distancias[actual] + costo

                    # si encontramos un camino mas corto, lo actualizamos
                    if nueva_distancia < distancias[vecino.id]:
                        distancias[vecino.id] = nueva_distancia
                        padres[vecino.id] = actual

        # si nunca pudimos llegar al destino
        if distancias[id_destino] == float('inf'):
            return None, []

        # reconstruimos el camino hacia atras siguiendo los padres
        camino = []
        paso = id_destino
        while paso is not None:
            camino.append(paso)
            paso = padres[paso]

        # lo damos vuelta para que vaya desde el origen hasta el destino
        camino.reverse()
        return distancias[id_destino], camino
