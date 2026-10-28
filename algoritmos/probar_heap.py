import sys
import os

# para poder importar cosas de las otras carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.heap import MaxHeap
from modelos.juego import Juego

def probar_heap():
    print("==========================================")
    print("      PRUEBA DE MAX-HEAP (TP 6)          ")
    print("==========================================\n")

    heap = MaxHeap()

    # armamos unos juegos de prueba con notas desordenadas
    j1 = Juego(1, "The Witcher 3", ["RPG"], "CD Projekt", 9.8, 2015)
    j2 = Juego(2, "Cyberpunk 2077", ["RPG"], "CD Projekt", 8.8, 2020)
    j3 = Juego(3, "Elden Ring", ["RPG"], "FromSoftware", 9.5, 2022)
    j4 = Juego(4, "Minecraft", ["Sandbox"], "Mojang", 9.2, 2011)
    j5 = Juego(5, "Juego Promedio", ["Casual"], "Indie", 6.5, 2019)

    print("1. Insertando juegos en el Heap...")
    for j in [j1, j2, j3, j4, j5]:
        heap.insertar(j)
        print(f"   -> Insertado: {j.titulo} (Nota: {j.calificacion})")

    print(f"\nTotal juegos en el Heap: {len(heap)}")

    print("\n2. Probando sacar el Top 3 con el Heap:")
    top3 = heap.obtener_top_n(3)
    for puesto, juego in enumerate(top3, 1):
        print(f"   Puesto {puesto}: {juego.titulo} - Nota: {juego.calificacion}")

    print("\n3. Extrayendo los elementos uno a uno (deben salir de mayor a menor nota):")
    while len(heap) > 0:
        j = heap.extraer_maximo()
        print(f"   - {j.titulo} ({j.calificacion})")

    print("\n[OK] Heap manual funcionando correctamente sin usar librerias raras.")

if __name__ == "__main__":
    probar_heap()
