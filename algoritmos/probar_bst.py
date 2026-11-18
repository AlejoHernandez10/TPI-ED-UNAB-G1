import sys
import os

# para poder importar desde la carpeta principal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.arbol_binario import ArbolBinarioBusqueda
from modelos.juego import Juego

def probar_bst():
    print("==========================================")
    print("     PRUEBA DE ARBOLES BINARIOS (BST)     ")
    print("==========================================\n")

    bst = ArbolBinarioBusqueda()

    # creamos unos juegos de prueba
    j1 = Juego(1, "Grand Theft Auto V", ["Acción"], "Rockstar", 8.9, 2013)
    j2 = Juego(2, "The Witcher 3", ["RPG"], "CD Projekt", 9.3, 2015)
    j3 = Juego(3, "Cyberpunk 2077", ["RPG"], "CD Projekt", 8.0, 2020)
    j4 = Juego(4, "Minecraft", ["Sandbox"], "Mojang", 9.0, 2011)

    # 1. insercion
    print("1. Insertando elementos...")
    bst.insertar(j1.titulo, j1)
    bst.insertar(j2.titulo, j2)
    bst.insertar(j3.titulo, j3)
    bst.insertar(j4.titulo, j4)
    print("   [OK] Insercion completada.\n")

    # 2. busqueda
    print("2. Probando busqueda:")
    busqueda = bst.buscar("Minecraft")
    if busqueda:
        print(f"   [OK] Encontrado: {busqueda.titulo} | Rating: {busqueda.calificacion}")
    else:
        print("   [ERROR] No encontrado")

    busqueda_falsa = bst.buscar("Juego Inexistente")
    print(f"   Busqueda inexistente: {'Encontrado' if busqueda_falsa else '[OK] Correcto (None)'}\n")

    # 3. recorridos
    print("3. Probando Recorridos:")
    print("   - Inorder (ordenado por titulo):")
    for j in bst.inorder():
        print(f"     - {j.titulo}")

    print("\n   - Preorder:")
    for j in bst.preorder():
        print(f"     - {j.titulo}")

    print("\n   - Postorder:")
    for j in bst.postorder():
        print(f"     - {j.titulo}")

if __name__ == "__main__":
    probar_bst()
