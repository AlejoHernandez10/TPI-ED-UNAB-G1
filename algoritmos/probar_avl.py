import os
import sys
import json
import time
from typing import Optional, List, Dict, Any

# Ajuste de ruta para permitir importaciones desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Aumentar límite de recursión para soportar árboles BST degenerados de hasta 1000 nodos
sys.setrecursionlimit(max(sys.getrecursionlimit(), 2500))

from estructuras.avl import ArbolAVL, NodoAVL
from estructuras.arbol_binario import ArbolBinarioBusqueda, NodoArbol
from estructuras.arbol_general import ArbolGeneral, NodoGeneral
from modelos.juego import Juego


def calcular_altura_bst(nodo: Optional[NodoArbol]) -> int:
    """Calcula recursivamente la altura de un árbol BST estándar."""
    if nodo is None:
        return 0
    return 1 + max(calcular_altura_bst(nodo.izquierdo), calcular_altura_bst(nodo.derecho))


# ==============================================================================
# 1. PRUEBAS DE ÁRBOL AVL (ROTACIONES, INSERCIÓN, BÚSQUEDA Y RECORRIDOS)
# ==============================================================================
def probar_rotaciones_avl():
    print("=" * 75)
    print(" 1. PRUEBAS DE ÁRBOL AVL: 4 CASOS DE ROTACIÓN Y FACTORES DE BALANCE")
    print("=" * 75)

    # --- Caso LL (Izquierda - Izquierda) ---
    print("\n[Caso 1: Rotación Simple a la Derecha - Desbalance LL]")
    print("  Insertando claves decrecientes: '30', '20', '10'")
    avl_ll = ArbolAVL()
    avl_ll.insertar("30", 30)
    print(f"  -> Insertado '30' | Raíz: '{avl_ll.raiz.clave}', Balance: {avl_ll.obtener_balance()}, Altura: {avl_ll.obtener_altura()}")
    avl_ll.insertar("20", 20)
    print(f"  -> Insertado '20' | Raíz: '{avl_ll.raiz.clave}', Balance: {avl_ll.obtener_balance()}, Altura: {avl_ll.obtener_altura()}")
    avl_ll.insertar("10", 10)
    print(f"  -> Insertado '10' (Desbalance LL corregido)")
    print(f"     Resultado: Raíz='{avl_ll.raiz.clave}', HijoIzq='{avl_ll.raiz.izquierdo.clave}', HijoDer='{avl_ll.raiz.derecho.clave}'")
    print(f"     Balance raíz: {avl_ll.obtener_balance()} | Altura: {avl_ll.obtener_altura()} | ¿Balanceado?: {avl_ll.esta_balanceado()}")
    assert avl_ll.raiz.clave == "20"
    assert avl_ll.raiz.izquierdo.clave == "10"
    assert avl_ll.raiz.derecho.clave == "30"
    assert avl_ll.esta_balanceado() is True
    print("  [OK] Rotación simple derecha (LL) validada con éxito.")

    # --- Caso RR (Derecha - Derecha) ---
    print("\n[Caso 2: Rotación Simple a la Izquierda - Desbalance RR]")
    print("  Insertando claves crecientes: '10', '20', '30'")
    avl_rr = ArbolAVL()
    avl_rr.insertar("10", 10)
    print(f"  -> Insertado '10' | Raíz: '{avl_rr.raiz.clave}', Balance: {avl_rr.obtener_balance()}, Altura: {avl_rr.obtener_altura()}")
    avl_rr.insertar("20", 20)
    print(f"  -> Insertado '20' | Raíz: '{avl_rr.raiz.clave}', Balance: {avl_rr.obtener_balance()}, Altura: {avl_rr.obtener_altura()}")
    avl_rr.insertar("30", 30)
    print(f"  -> Insertado '30' (Desbalance RR corregido)")
    print(f"     Resultado: Raíz='{avl_rr.raiz.clave}', HijoIzq='{avl_rr.raiz.izquierdo.clave}', HijoDer='{avl_rr.raiz.derecho.clave}'")
    print(f"     Balance raíz: {avl_rr.obtener_balance()} | Altura: {avl_rr.obtener_altura()} | ¿Balanceado?: {avl_rr.esta_balanceado()}")
    assert avl_rr.raiz.clave == "20"
    assert avl_rr.raiz.izquierdo.clave == "10"
    assert avl_rr.raiz.derecho.clave == "30"
    assert avl_rr.esta_balanceado() is True
    print("  [OK] Rotación simple izquierda (RR) validada con éxito.")

    # --- Caso LR (Izquierda - Derecha) ---
    print("\n[Caso 3: Rotación Doble Izquierda-Derecha - Desbalance LR]")
    print("  Insertando claves zig-zag: '30', '10', '20'")
    avl_lr = ArbolAVL()
    avl_lr.insertar("30", 30)
    avl_lr.insertar("10", 10)
    avl_lr.insertar("20", 20)
    print(f"  -> Insertado '20' (Desbalance LR corregido)")
    print(f"     Resultado: Raíz='{avl_lr.raiz.clave}', HijoIzq='{avl_lr.raiz.izquierdo.clave}', HijoDer='{avl_lr.raiz.derecho.clave}'")
    print(f"     Balance raíz: {avl_lr.obtener_balance()} | Altura: {avl_lr.obtener_altura()} | ¿Balanceado?: {avl_lr.esta_balanceado()}")
    assert avl_lr.raiz.clave == "20"
    assert avl_lr.raiz.izquierdo.clave == "10"
    assert avl_lr.raiz.derecho.clave == "30"
    assert avl_lr.esta_balanceado() is True
    print("  [OK] Rotación doble izquierda-derecha (LR) validada con éxito.")

    # --- Caso RL (Derecha - Izquierda) ---
    print("\n[Caso 4: Rotación Doble Derecha-Izquierda - Desbalance RL]")
    print("  Insertando claves zig-zag: '10', '30', '20'")
    avl_rl = ArbolAVL()
    avl_rl.insertar("10", 10)
    avl_rl.insertar("30", 30)
    avl_rl.insertar("20", 20)
    print(f"  -> Insertado '20' (Desbalance RL corregido)")
    print(f"     Resultado: Raíz='{avl_rl.raiz.clave}', HijoIzq='{avl_rl.raiz.izquierdo.clave}', HijoDer='{avl_rl.raiz.derecho.clave}'")
    print(f"     Balance raíz: {avl_rl.obtener_balance()} | Altura: {avl_rl.obtener_altura()} | ¿Balanceado?: {avl_rl.esta_balanceado()}")
    assert avl_rl.raiz.clave == "20"
    assert avl_rl.raiz.izquierdo.clave == "10"
    assert avl_rl.raiz.derecho.clave == "30"
    assert avl_rl.esta_balanceado() is True
    print("  [OK] Rotación doble derecha-izquierda (RL) validada con éxito.")


def probar_busqueda_y_recorridos_avl():
    print("\n" + "-" * 75)
    print(" Inserción múltiple, Búsqueda exacta y Recorridos en ArbolAVL")
    print("-" * 75)

    juegos_muestra = [
        ("The Witcher 3", 9.8),
        ("Cyberpunk 2077", 8.8),
        ("Elden Ring", 9.5),
        ("Minecraft", 9.2),
        ("Grand Theft Auto V", 9.1),
        ("Portal 2", 8.9),
        ("Hades", 9.3),
        ("Celeste", 9.0)
    ]

    avl = ArbolAVL()
    for titulo, calif in juegos_muestra:
        avl.insertar(titulo, calif)

    print(f"  Total juegos insertados: {len(juegos_muestra)}")
    print(f"  Altura resultante AVL: {avl.obtener_altura()}")
    print(f"  ¿Árbol balanceado?: {avl.esta_balanceado()}")
    assert avl.esta_balanceado() is True

    # Búsqueda exacta exitosa y fallida
    print("\n  [Pruebas de Búsqueda Exacta]")
    buscados_exitosos = ["The Witcher 3", "ELDEN RING", "  hades  "]
    for b in buscados_exitosos:
        res = avl.buscar(b)
        print(f"   * Buscar '{b}': Calificación={res} [OK]")
        assert res is not None

    buscado_fallido = "Half-Life 3"
    res_fallido = avl.buscar(buscado_fallido)
    print(f"   * Buscar '{buscado_fallido}': {res_fallido} [OK, None]")
    assert res_fallido is None

    # Recorridos
    print("\n  [Recorridos AVL]")
    in_order = avl.inorder()
    pre_order = avl.preorder()
    post_order = avl.postorder()

    print(f"   * Inorden (ordenado por clave, n={len(in_order)}):")
    print(f"     {in_order}")
    print(f"   * Preorden (raíz-izq-der, n={len(pre_order)}):")
    print(f"     {pre_order}")
    print(f"   * Postorden (izq-der-raíz, n={len(post_order)}):")
    print(f"     {post_order}")

    assert len(in_order) == len(juegos_muestra)
    assert len(pre_order) == len(juegos_muestra)
    assert len(post_order) == len(juegos_muestra)
    print("  [OK] Recorridos y búsquedas validados.")


# ==============================================================================
# 2. COMPARATIVA EXPERIMENTAL: CASO DEGENERADO BST VS EQUILIBRADO AVL
# ==============================================================================
def comparar_desbalance_bst_vs_avl():
    print("\n" + "=" * 75)
    print(" 2. CASOS DE DESBALANCE GENERADOS: COMPARATIVA BST vs. AVL")
    print("=" * 75)
    print("  Se inserta una secuencia estrictamente ordenada en ambas estructuras.")
    print("  BST degenera a una lista enlazada O(N) con peor caso en búsqueda.")
    print("  AVL mantiene balance estricto O(log N) mediante rotaciones continuas.")
    print("  Se mide el tiempo promedio por búsqueda en el peor caso (último elemento).\n")

    tamanos = [50, 100, 200, 500]
    repeticiones = 1000

    print("+" + "-" * 8 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 16 + "+")
    print(f"| {'N':<6} | {'Altura BST':<10} | {'Altura AVL':<10} | {'T. BST (us)':<13} | {'T. AVL (us)':<13} | {'Aceleracion':<14} |")
    print("+" + "-" * 8 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 16 + "+")

    for n in tamanos:
        bst = ArbolBinarioBusqueda()
        avl = ArbolAVL()

        claves = [f"juego_{i:04d}" for i in range(1, n + 1)]
        for c in claves:
            bst.insertar(c, c)
            avl.insertar(c, c)

        h_bst = calcular_altura_bst(bst.raiz)
        h_avl = avl.obtener_altura()

        # Peor caso de búsqueda: la última clave insertada (profundidad máxima)
        peor_clave = claves[-1]

        # Medición BST
        t0 = time.perf_counter()
        for _ in range(repeticiones):
            bst.buscar(peor_clave)
        t_bst_us = ((time.perf_counter() - t0) * 1e6) / repeticiones

        # Medición AVL
        t0 = time.perf_counter()
        for _ in range(repeticiones):
            avl.buscar(peor_clave)
        t_avl_us = ((time.perf_counter() - t0) * 1e6) / repeticiones

        ratio = (t_bst_us / t_avl_us) if t_avl_us > 0 else 0.0

        # Verificaciones formales
        assert h_bst == n, f"El BST debió degenerar a altura {n}, pero dio {h_bst}"
        assert avl.esta_balanceado() is True, "El AVL debe estar balanceado"
        assert h_avl < h_bst, "La altura del AVL debe ser drásticamente menor a la del BST"

        acel_str = f"{ratio:.2f}x"
        print(f"| {n:<6} | {h_bst:<10} | {h_avl:<10} | {t_bst_us:<13.2f} | {t_avl_us:<13.2f} | {acel_str:<14} |")

    print("+" + "-" * 8 + "+" + "-" * 12 + "+" + "-" * 12 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 16 + "+")
    print("  Conclusión:")
    print("  - Con datos ordenados, el BST degenera en una lista enlazada (Altura = N).")
    print("  - El AVL se mantiene balanceado con altura logarítmica O(log2 N).")
    print("  - La diferencia en tiempo de búsqueda a favor del AVL se nota mucho más a medida que N crece.")


# ==============================================================================
# 3. PRUEBAS DE ÁRBOL GENERAL (N-ARIO) - DOMINIO NEXTGAME
# ==============================================================================
def probar_arbol_general():
    print("\n" + "=" * 75)
    print(" 3. PRUEBAS DE ÁRBOL GENERAL (N-ARIO): JERARQUÍA DE NEXTGAME")
    print("=" * 75)

    arbol = ArbolGeneral()
    arbol.establecer_raiz("NextGame", "Catálogo General de Videojuegos")

    # Géneros principales (nivel 1)
    generos = ["Acción", "RPG", "Estrategia", "Aventura", "Indie"]
    for g in generos:
        arbol.agregar_hijo("NextGame", g, f"Categoría de {g}")

    # Videojuegos por género (nivel 2)
    juegos_por_genero = {
        "Acción": ["Grand Theft Auto V", "Doom Eternal", "God of War"],
        "RPG": ["The Witcher 3: Wild Hunt", "Baldur's Gate 3", "Cyberpunk 2077", "Elden Ring"],
        "Estrategia": ["Civilization VI", "Age of Empires IV"],
        "Aventura": ["The Legend of Zelda", "Red Dead Redemption 2"],
        "Indie": ["Hollow Knight", "Celeste", "Hades"]
    }

    for genero, lista_titulos in juegos_por_genero.items():
        for titulo in lista_titulos:
            arbol.agregar_hijo(genero, titulo, {"tipo": "Juego", "categoria": genero})

    print(f"  Raíz establecida: '{arbol.raiz.clave}'")
    print(f"  Total nodos en el árbol: {arbol.cantidad_nodos()}")
    print(f"  Altura del árbol: {arbol.altura()}")
    print(f"  Total nodos hoja (videojuegos finales): {len(arbol.obtener_hojas())}")

    # Recorrido en Amplitud (BFS)
    print("\n  [Recorrido en Amplitud - BFS (Nivel por Nivel)]")
    nodos_bfs = arbol.recorrido_amplitud()
    claves_bfs = [n.clave for n in nodos_bfs]
    print(f"  Total nodos recorridos: {len(claves_bfs)}")
    print(f"  Primeros 6 nodos (Nivel 0 y 1): {claves_bfs[:6]}")
    assert claves_bfs[0] == "NextGame"
    for g in generos:
        assert g in claves_bfs[1:6]

    # Recorrido en Profundidad (DFS Preorden)
    print("\n  [Recorrido en Profundidad - DFS (Preorden)]")
    nodos_dfs = arbol.recorrido_profundidad()
    claves_dfs = [n.clave for n in nodos_dfs]
    print(f"  Total nodos recorridos: {len(claves_dfs)}")
    print(f"  Muestra primeros 8 nodos DFS: {claves_dfs[:8]}")
    assert claves_dfs[0] == "NextGame"

    # Búsqueda de nodos
    print("\n  [Búsqueda en Árbol General]")
    busqueda_rpg = arbol.buscar("RPG")
    print(f"  * Buscar 'RPG': Encontrado con {len(busqueda_rpg.hijos)} subnodos/juegos [OK]")
    assert busqueda_rpg is not None
    assert len(busqueda_rpg.hijos) == 4

    busqueda_juego = arbol.buscar("The Witcher 3: Wild Hunt")
    print(f"  * Buscar 'The Witcher 3: Wild Hunt': Encontrado (Valor={busqueda_juego.valor}) [OK]")
    assert busqueda_juego is not None

    busqueda_inexistente = arbol.buscar("Simulación")
    print(f"  * Buscar 'Simulación': {busqueda_inexistente} [OK, None]")
    assert busqueda_inexistente is None

    # Ruta jerárquica
    camino = arbol.obtener_camino("The Witcher 3: Wild Hunt")
    print(f"  * Ruta jerárquica: {' -> '.join(camino)} [OK]")
    assert camino == ["NextGame", "RPG", "The Witcher 3: Wild Hunt"]

    # Visualización jerárquica
    print("\n  [Visualización Jerárquica - mostrar_arbol()]")
    arbol_str = arbol.mostrar_arbol()
    print(arbol_str)
    assert "NextGame" in arbol_str
    assert "RPG" in arbol_str
    assert "The Witcher 3" in arbol_str
    print("\n  [OK] Árbol General validado con éxito.")


# ==============================================================================
# 4. PRUEBA CON DATASET REAL: 200 REGISTROS DE datos/juegos.json
# ==============================================================================
def probar_dataset_real_avl():
    print("\n" + "=" * 75)
    print(" 4. PRUEBA CON DATASET REAL: datos/juegos.json (200 REGISTROS)")
    print("=" * 75)

    ruta_json = os.path.join(os.path.dirname(__file__), '..', 'datos', 'juegos.json')
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    print(f"  Archivo cargado: 'datos/juegos.json' ({len(datos)} registros)")

    avl = ArbolAVL()
    for item in datos:
        juego = Juego(
            id_juego=item['id'],
            titulo=item['titulo'],
            generos=item['generos'],
            desarrollador=item['desarrollador'],
            calificacion=item['calificacion'],
            anio_publicacion=item['anioPublicacion'],
            web=item.get('web', '')
        )
        avl.insertar(juego.titulo, juego)

    altura_real = avl.obtener_altura()
    balance_raiz = avl.obtener_balance()
    esta_bal = avl.esta_balanceado()

    print(f"  Total juegos insertados en AVL: {len(datos)}")
    print(f"  Altura obtenida en el AVL: {altura_real}")
    print(f"  Factor de balance en la raíz: {balance_raiz}")
    print(f"  ¿Todos los nodos cumplen propiedad AVL (-1 <= bal <= 1)?: {esta_bal}")

    assert esta_bal is True, "El árbol AVL debe estar balanceado"
    assert 7 <= altura_real <= 10, f"Para N=200, la altura AVL esperada está en [7, 10], se obtuvo {altura_real}"

    # Búsqueda de juegos reales
    print("\n  [Búsqueda en catálogo AVL cargado]")
    ejemplos_a_buscar = [
        "Grand Theft Auto V",
        "The Witcher 3: Wild Hunt",
        "Portal 2",
        "Minecraft",
        "Divinity: Original Sin 2"
    ]

    for titulo in ejemplos_a_buscar:
        juego_hallado = avl.buscar(titulo)
        assert juego_hallado is not None
        print(f"  * [OK] '{juego_hallado.titulo}' | {juego_hallado.desarrollador} ({juego_hallado.anio_publicacion}) | Calificación: {juego_hallado.calificacion}")

    print("\n  [OK] Dataset real verificado e indexado exitosamente en ArbolAVL.")


# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================
def main():
    inicio_total = time.perf_counter()
    print("=" * 75)
    print("           PRUEBAS Y COMPARATIVA: AVL Y ÁRBOL GENERAL (NEXTGAME)        ")
    print("=" * 75)

    probar_rotaciones_avl()
    probar_busqueda_y_recorridos_avl()
    comparar_desbalance_bst_vs_avl()
    probar_arbol_general()
    probar_dataset_real_avl()

    tiempo_total = (time.perf_counter() - inicio_total) * 1000
    print("\n" + "=" * 75)
    print(f" [OK] Todas las pruebas y mediciones finalizaron correctamente ({tiempo_total:.2f} ms).")
    print("=" * 75)


if __name__ == "__main__":
    main()
