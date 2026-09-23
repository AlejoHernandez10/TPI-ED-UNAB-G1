import sys
import os

# Ajuste de ruta para permitir importaciones desde la raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.arbol_binario import ArbolBinarioBusqueda
from modelos.juego import Juego

def probar_bst():
    print("==========================================")
    print("     PRUEBA DE ÁRBOLES BINARIOS (BST)     ")
    print("==========================================\n")

    bst = ArbolBinarioBusqueda()

    # Creación de datos de prueba
    j1 = Juego(1, "Grand Theft Auto V", ["Acción"], "Rockstar", 8.9, 2013)
    j2 = Juego(2, "The Witcher 3", ["RPG"], "CD Projekt", 9.3, 2015)
    j3 = Juego(3, "Cyberpunk 2077", ["RPG"], "CD Projekt", 8.0, 2020)
    j4 = Juego(4, "Minecraft", ["Sandbox"], "Mojang", 9.0, 2011)

    # 1. Prueba de inserción
    print("1. Insertando elementos...")
    bst.insertar(j1.titulo, j1)
    bst.insertar(j2.titulo, j2)
    bst.insertar(j3.titulo, j3)
    bst.insertar(j4.titulo, j4)
    print("   ✅ Inserción completada.\n")

    # 2. Prueba de búsqueda
    print("2. Probando Búsqueda:")
    busqueda = bst.buscar("Minecraft")
    if busqueda:
        print(f"   ✅ Encontrado: {busqueda.titulo} | Rating: {busqueda.calificacion}")
    else:
        print("   ❌ No encontrado")

    busqueda_falsa = bst.buscar("Juego Inexistente")
    print(f"   Búsqueda inexistente: {'Encontrado' if busqueda_falsa else '✅ Correcto (None)'}\n")

    # 3. Recorridos
    print("3. Probando Recorridos:")
    print("   • Inorder (Ordenado alfabéticamente):")
    for j in bst.inorder():
        print(f"     - {j.titulo}")

    print("\n   • Preorder:")
    for j in bst.preorder():
        print(f"     - {j.titulo}")

    print("\n   • Postorder:")
    for j in bst.postorder():
        print(f"     - {j.titulo}")

if __name__ == "__main__":
    probar_bst()