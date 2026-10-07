import sys
from servicios.catalogo import CatalogoJuegos
from interfaz.menu import InterfazConsola


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    catalogo = CatalogoJuegos()
    catalogo.cargar_desde_json("datos/juegos.json")

    while True:
        opcion = InterfazConsola.mostrar_menu_principal()

        # 1. BUSCAR VIDEOJUEGO (Árbol AVL Balanceado)
        if opcion == "1":
            query = InterfazConsola.pedir_texto("Ingrese el título a buscar (Búsqueda AVL)")
            resultados = catalogo.buscar_por_titulo(query)
            InterfazConsola.mostrar_lista_juegos("Resultados de búsqueda [Árbol AVL]", resultados)
            InterfazConsola.pausar()

        # 2. EXPLORAR CATEGORÍAS (Árbol General N-ario)
        elif opcion == "2":
            arbol_cat = catalogo.obtener_arbol_categorias()
            while True:
                sub_opcion = InterfazConsola.mostrar_menu_categorias()
                if sub_opcion == "1":
                    InterfazConsola.mostrar_jerarquia_arbol(arbol_cat)
                    InterfazConsola.pausar()
                elif sub_opcion == "2":
                    InterfazConsola.mostrar_recorrido_bfs(arbol_cat)
                    InterfazConsola.pausar()
                elif sub_opcion == "3":
                    InterfazConsola.mostrar_recorrido_dfs(arbol_cat)
                    InterfazConsola.pausar()
                elif sub_opcion == "4":
                    generos = catalogo.obtener_todos_los_generos()
                    cat_sel = InterfazConsola.seleccionar_genero(generos)
                    InterfazConsola.mostrar_subarbol_categoria(arbol_cat, cat_sel)
                    InterfazConsola.pausar()
                elif sub_opcion == "0":
                    break
                else:
                    InterfazConsola.mostrar_mensaje("Opción inválida. Intente de nuevo.")
                    InterfazConsola.pausar()

        # 3. EXPLORAR POR GÉNERO
        elif opcion == "3":
            generos = catalogo.obtener_todos_los_generos()
            genero_sel = InterfazConsola.seleccionar_genero(generos)
            resultados = catalogo.obtener_por_genero(genero_sel)
            InterfazConsola.mostrar_lista_juegos(f"Videojuegos en '{genero_sel}'", resultados)
            InterfazConsola.pausar()

        # 4. VER JUEGOS RELACIONADOS
        elif opcion == "4":
            query = InterfazConsola.pedir_texto("Ingrese el título del juego base")
            coincidencias = catalogo.buscar_por_titulo(query)
            if coincidencias:
                juego = coincidencias[0]
                relacionados = catalogo.obtener_relacionados(juego, limite=5)
                InterfazConsola.mostrar_lista_juegos(f"Juegos relacionados con '{juego.titulo}'", relacionados)
            else:
                InterfazConsola.mostrar_mensaje("[!] No se encontró el juego especificado.")
            InterfazConsola.pausar()

        # 5. OBTENER RECOMENDACIONES
        elif opcion == "5":
            query = InterfazConsola.pedir_texto("¿Qué juego te gustó?")
            coincidencias = catalogo.buscar_por_titulo(query)
            if coincidencias:
                juego = coincidencias[0]
                recs = catalogo.obtener_recomendaciones(juego, limite=3)
                InterfazConsola.mostrar_tarjeta_recomendaciones(juego, recs)
            else:
                InterfazConsola.mostrar_mensaje("[!] No se encontró el juego especificado.")
            InterfazConsola.pausar()

        # 6. VER TOP 10
        elif opcion == "6":
            top_10 = catalogo.obtener_top_n(10)
            InterfazConsola.mostrar_top_10(top_10)
            InterfazConsola.pausar()

        # 0. SALIR
        elif opcion == "0":
            InterfazConsola.mostrar_mensaje("¡Gracias por usar NextGame!")
            break

        else:
            InterfazConsola.mostrar_mensaje("Opción inválida. Intente de nuevo.")
            InterfazConsola.pausar()


if __name__ == "__main__":
    main()