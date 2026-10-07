import os
from typing import List, Optional
from modelos.juego import Juego
from estructuras.arbol_general import ArbolGeneral


class InterfazConsola:

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresione ENTER para continuar...")

    @staticmethod
    def mostrar_menu_principal() -> str:
        InterfazConsola.limpiar_pantalla()
        print("========================================")
        print("              NEXTGAME")
        print("========================================")
        print("1. Buscar videojuego (Arbol AVL)")
        print("2. Explorar categorias (Arbol General)")
        print("3. Explorar por genero")
        print("4. Ver juegos relacionados")
        print("5. Obtener recomendaciones")
        print("6. Ver Top 10")
        print("0. Salir")
        print("----------------------------------------")
        return input("Seleccione una opcion: ").strip()

    # --- Métodos de Entrada ---
    @staticmethod
    def pedir_texto(mensaje: str) -> str:
        return input(f"\n{mensaje}: ").strip()

    @staticmethod
    def seleccionar_genero(generos: List[str]) -> str:
        """Muestra los géneros numerados y permite seleccionar por número o texto."""
        print("\nGeneros disponibles:")
        for idx, g in enumerate(generos, 1):
            print(f"  {idx:2d}. {g}")

        entrada = input("\nIngrese el numero o el nombre del genero: ").strip()

        if entrada.isdigit():
            idx = int(entrada) - 1
            if 0 <= idx < len(generos):
                return generos[idx]

        return entrada

    # --- Métodos de Salida / Visualización ---
    @staticmethod
    def mostrar_lista_juegos(titulo_seccion: str, juegos: List[Juego]):
        print(f"\n{titulo_seccion} ({len(juegos)}):")
        if not juegos:
            print("  [!] No se encontraron videojuegos.")
            return

        for j in juegos:
            print(f" * {j.titulo} ({j.anio_publicacion}) - [{', '.join(j.generos)}] | Rating: {j.calificacion}")

    @staticmethod
    def mostrar_tarjeta_recomendaciones(juego_base: Juego, recomendaciones: List[Juego]):
        titulo_base = juego_base.titulo.upper()

        print("\n=======================================================")
        print("                     NEXTGAME                          ")
        print("=======================================================")
        print(f" Si te gusto {titulo_base}:")
        print(" Te recomendamos probar los siguientes titulos:\n")

        for idx, r in enumerate(recomendaciones, 1):
            print(f"  {idx}. {r.titulo} | Rating: {r.calificacion}")

        print("=======================================================")

    @staticmethod
    def mostrar_top_10(juegos: List[Juego]):
        print("\n========================================")
        print("           TOP 10 VIDEOJUEGOS")
        print("----------------------------------------")
        for idx, j in enumerate(juegos, 1):
            print(f"{idx:2d}. {j.titulo:<28} Rating: {j.calificacion}")
        print("----------------------------------------")

    @staticmethod
    def mostrar_mensaje(mensaje: str):
        print(f"\n{mensaje}")

    # --- Visualización y Recorridos de Árbol General ---
    @staticmethod
    def mostrar_menu_categorias() -> str:
        print("\n=======================================================")
        print("      EXPLORADOR DE CATEGORIAS (ARBOL GENERAL)")
        print("=======================================================")
        print("1. Ver arbol completo con categorias y juegos")
        print("2. Recorrido en amplitud (BFS - por niveles)")
        print("3. Recorrido en profundidad (DFS - preorden)")
        print("4. Ver juegos de una categoria")
        print("0. Volver al menu principal")
        print("-------------------------------------------------------")
        return input("Seleccione una opcion: ").strip()

    @staticmethod
    def mostrar_jerarquia_arbol(arbol: ArbolGeneral):
        print("\n=======================================================")
        print(" JERARQUIA COMPLETA DEL CATALOGO (ARBOL GENERAL)")
        print("=======================================================\n")
        print(arbol.mostrar_arbol())
        print("\n-------------------------------------------------------")
        print(f"  Total nodos: {arbol.cantidad_nodos()} | Altura: {arbol.altura()} | Hojas: {len(arbol.obtener_hojas())}")
        print("=======================================================")

    @staticmethod
    def mostrar_recorrido_bfs(arbol: ArbolGeneral):
        nodos = arbol.recorrido_amplitud()
        print("\n=======================================================")
        print(" RECORRIDO EN AMPLITUD (BFS - POR NIVELES)")
        print("=======================================================")
        print(f"Total nodos visitados: {len(nodos)}\n")
        for idx, n in enumerate(nodos, 1):
            tipo = "Raiz" if idx == 1 else ("Categoria" if n.hijos else "Videojuego")
            print(f"  [{idx:3d}] ({tipo:<10}) {n.clave}")
        print("=======================================================")

    @staticmethod
    def mostrar_recorrido_dfs(arbol: ArbolGeneral):
        nodos = arbol.recorrido_profundidad()
        print("\n=======================================================")
        print(" RECORRIDO EN PROFUNDIDAD (DFS - PREORDEN)")
        print("=======================================================")
        print(f"Total nodos visitados: {len(nodos)}\n")
        for idx, n in enumerate(nodos, 1):
            tipo = "Raiz" if idx == 1 else ("Categoria" if n.hijos else "Videojuego")
            print(f"  [{idx:3d}] ({tipo:<10}) {n.clave}")
        print("=======================================================")

    @staticmethod
    def mostrar_subarbol_categoria(arbol: ArbolGeneral, categoria: str):
        nodo = arbol.buscar(categoria)
        if nodo is None:
            print(f"\n[!] La categoria '{categoria}' no existe en el arbol.")
            return

        print(f"\n=======================================================")
        print(f" CATEGORIA: {nodo.clave.upper()}")
        print("=======================================================")
        print(f"Subnodos/Juegos asociados: {len(nodo.hijos)}\n")
        for idx, hijo in enumerate(nodo.hijos, 1):
            if isinstance(hijo.valor, Juego):
                print(f"  {idx:2d}. {hijo.valor.titulo} ({hijo.valor.anio_publicacion}) | Rating: {hijo.valor.calificacion}")
            else:
                print(f"  {idx:2d}. {hijo.clave}")
        print("=======================================================")