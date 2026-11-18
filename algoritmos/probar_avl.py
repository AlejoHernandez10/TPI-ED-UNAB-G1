import sys
import os

# para poder importar desde la carpeta principal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.avl import ArbolAVL
from modelos.juego import Juego

def probar_avl():
    print("==========================================")
    print("        PRUEBA DE ARBOL AVL (TP 4)        ")
    print("==========================================\n")

    avl = ArbolAVL()

    # creamos juegos de prueba
    j1 = Juego(1, "The Witcher 3", ["RPG"], "CD Projekt", 9.8, 2015)
    j2 = Juego(2, "Cyberpunk 2077", ["RPG"], "CD Projekt", 8.8, 2020)
    j3 = Juego(3, "Elden Ring", ["RPG"], "FromSoftware", 9.5, 2022)
    j4 = Juego(4, "Minecraft", ["Sandbox"], "Mojang", 9.2, 2011)
    j5 = Juego(5, "Portal 2", ["Puzzle"], "Valve", 8.9, 2011)

    # 1. insercion y balanceo
    print("1. Insertando juegos en el arbol AVL...")
    for j in [j1, j2, j3, j4, j5]:
        avl.insertar(j.titulo, j)
        print(f"   -> Insertado: {j.titulo}")

    print(f"\nAltura total del arbol: {avl.obtener_altura()}")
    print(f"Balance en la raiz: {avl.obtener_balance()}")
    print(f"¿Esta balanceado?: {'Si' if avl.esta_balanceado() else 'No'}\n")

    # 2. busqueda
    print("2. Probando busqueda exacta:")
    buscado = avl.buscar("Elden Ring")
    if buscado:
        print(f"   [OK] Encontrado: {buscado.titulo} | Nota: {buscado.calificacion}")
    else:
        print("   [ERROR] No encontrado")

    busqueda_falsa = avl.buscar("Juego Que No Existe")
    print(f"   Busqueda inexistente: {'Encontrado' if busqueda_falsa else '[OK] Correcto (None)'}\n")

    # 3. recorridos
    print("3. Probando recorridos:")
    print("   - Inorder (debe salir ordenado por titulo alfabeticamente):")
    for j in avl.inorder():
        print(f"     - {j.titulo}")

    print("\n   - Preorder (raiz primero):")
    for j in avl.preorder():
        print(f"     - {j.titulo}")

    print("\n[OK] Arbol AVL probado correctamente con auto-balanceo.")

if __name__ == "__main__":
    probar_avl()
