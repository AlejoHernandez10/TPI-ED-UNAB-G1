import sys
import os

# para poder importar cosas de las otras carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.grafo import Grafo
from modelos.juego import Juego

def probar_grafo():
    print("==========================================")
    print("        PRUEBA DE GRAFOS (TP 7)           ")
    print("==========================================\n")

    grafo = Grafo()

    # juegos de prueba con distintos generos
    j1 = Juego(1, "The Witcher 3", ["RPG", "Aventura", "Mundo Abierto"], "CD Projekt", 9.8, 2015)
    j2 = Juego(2, "Cyberpunk 2077", ["RPG", "Acción", "Mundo Abierto"], "CD Projekt", 8.8, 2020)
    j3 = Juego(3, "Elden Ring", ["RPG", "Aventura"], "FromSoftware", 9.5, 2022)
    j4 = Juego(4, "FIFA 23", ["Deportes", "Simulación"], "EA Sports", 7.5, 2022)

    juegos = [j1, j2, j3, j4]

    print("1. Agregando vertices al grafo...")
    for j in juegos:
        grafo.agregar_vertice(j)
        print(f"   Vertice creado: {j.titulo}")

    print("\n2. Conectando juegos que comparten generos (aristas con peso)...")
    for i in range(len(juegos)):
        for k in range(i + 1, len(juegos)):
            comunes = juegos[i].generos_en_comun(juegos[k])
            if comunes > 0:
                grafo.agregar_arista(juegos[i], juegos[k], peso=comunes)
                print(f"   Conectados: '{juegos[i].titulo}' <---> '{juegos[k].titulo}' (Generos en comun: {comunes})")

    print(f"\nResumen de la red:")
    print(f"- Total de vertices (juegos): {grafo.cantidad_vertices()}")
    print(f"- Total de aristas (conexiones): {grafo.cantidad_aristas()}")

    print("\n3. Consultando vecinos de 'The Witcher 3':")
    vecinos = grafo.obtener_vecinos(j1.id)
    for juego_vecino, peso in vecinos:
        print(f"   -> Relacionado con: {juego_vecino.titulo} | Peso arista: {peso}")

    print("\n4. Comprobando juego aislado ('FIFA 23'):")
    vecinos_fifa = grafo.obtener_vecinos(j4.id)
    if not vecinos_fifa:
        print("   FIFA 23 no tiene conexiones con los RPGs (correcto).")
    else:
        print(f"   Tiene {len(vecinos_fifa)} conexiones.")

    print("\n[OK] Grafo implementado con lista de adyacencia funcionando correctamente.")

if __name__ == "__main__":
    probar_grafo()
