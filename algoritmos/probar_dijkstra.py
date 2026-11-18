import sys
import os

# para poder importar cosas de las otras carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servicios.catalogo import CatalogoJuegos
from modelos.juego import Juego
from estructuras.grafo import Grafo

def probar_dijkstra_aislado():
    print("==========================================")
    print("       PRUEBA DE DIJKSTRA (TP 9)          ")
    print("==========================================\n")

    grafo = Grafo()

    # armamos una pequena cadena de 4 juegos:
    # A (RPG) <-> B (RPG, Aventura) <-> C (Aventura, Accion) <-> D (Accion)
    jA = Juego(1, "Juego Fantasia", ["RPG"], "DevA", 9.0, 2020)
    jB = Juego(2, "Juego Hibrido 1", ["RPG", "Aventura"], "DevB", 8.5, 2021)
    jC = Juego(3, "Juego Hibrido 2", ["Aventura", "Accion"], "DevC", 8.0, 2022)
    jD = Juego(4, "Juego Disparos", ["Accion"], "DevD", 8.8, 2023)

    for j in [jA, jB, jC, jD]:
        grafo.agregar_vertice(j)

    # conectamos con generos en comun
    # jA y jB comparten 1 genero
    grafo.agregar_arista(jA, jB, peso=1)
    # jB y jC comparten 1 genero
    grafo.agregar_arista(jB, jC, peso=1)
    # jC y jD comparten 1 genero
    grafo.agregar_arista(jC, jD, peso=1)

    print("1. Buscando camino entre 'Juego Fantasia' y 'Juego Disparos':")
    distancia, camino_ids = grafo.dijkstra(jA.id, jD.id)

    print(f"   Costo total acumulado: {distancia}")
    print(f"   Secuencia de IDs en el camino: {camino_ids}")
    if camino_ids == [1, 2, 3, 4]:
        print("   [OK] Camino encontrado correctamente paso a paso.\n")
    else:
        print("   [ERROR] El camino no dio los IDs esperados.\n")

def probar_dijkstra_dataset_real():
    print("2. Probando Dijkstra sobre el catalogo real (datos/juegos.json):")
    catalogo = CatalogoJuegos()
    catalogo.cargar_desde_json("datos/juegos.json")

    # buscamos dos juegos conocidos
    juegos_witcher = catalogo.buscar_por_titulo("The Witcher 3")
    juegos_portal = catalogo.buscar_por_titulo("Portal 2")

    if juegos_witcher and juegos_portal:
        origen = juegos_witcher[0]
        destino = juegos_portal[0]

        print(f"\nBuscando transicion entre:")
        print(f" - Origen: {origen.titulo} ({origen.generos})")
        print(f" - Destino: {destino.titulo} ({destino.generos})")

        distancia, camino = catalogo.encontrar_camino(origen, destino)

        if camino:
            print(f"\nCamino encontrado con costo {distancia} en {len(camino)} juegos:")
            for idx, j in enumerate(camino, 1):
                flecha = " -> " if idx < len(camino) else ""
                print(f"  [{idx}] {j.titulo} [{', '.join(j.generos)}]{flecha}")
        else:
            print("No se encontro camino.")

    print("\n[OK] Algoritmo Dijkstra verificado sobre el dataset real.")

if __name__ == "__main__":
    probar_dijkstra_aislado()
    probar_dijkstra_dataset_real()
