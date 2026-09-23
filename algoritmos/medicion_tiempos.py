import time
import random
import string
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.juego import Juego
from estructuras.arbol_binario import ArbolBinarioBusqueda

def generar_juegos(n: int):
    juegos = []
    for i in range(1, n + 1):
        titulo = f"Juego {i} " + ''.join(random.choices(string.ascii_uppercase, k=5))
        juegos.append(Juego(i, titulo, ["Acción"], "Dev", 8.0, 2020))
    return juegos

def busqueda_secuencial(lista, clave):
    clave_limpia = clave.lower()
    for item in lista:
        if item.titulo.lower() == clave_limpia:
            return item
    return None

def busqueda_binaria(lista_ordenada, clave):
    clave_limpia = clave.lower()
    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        titulo_medio = lista_ordenada[medio].titulo.lower()
        if titulo_medio == clave_limpia:
            return lista_ordenada[medio]
        elif titulo_medio < clave_limpia:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

def medir():
    tamanos = [1000, 10000, 100000]
    clave_buscada = "juego_inexistente_peor_caso"

    print(f"{'N Elementos':<12} | {'Secuencial (ms)':<16} | {'Binaria (ms)':<15} | {'Árbol BST (ms)':<15}")
    print("-" * 68)

    for n in tamanos:
        juegos = generar_juegos(n)
        
        # Búsqueda secuencial (Lista desordenada)
        inicio = time.perf_counter()
        busqueda_secuencial(juegos, clave_buscada)
        t_secuencial = (time.perf_counter() - inicio) * 1000

        # Búsqueda binaria (Lista ordenada por título)
        juegos_ordenados = sorted(juegos, key=lambda x: x.titulo.lower())
        inicio = time.perf_counter()
        busqueda_binaria(juegos_ordenados, clave_buscada)
        t_binaria = (time.perf_counter() - inicio) * 1000

        # Árbol Binario de Búsqueda
        bst = ArbolBinarioBusqueda()
        for j in juegos:
            bst.insertar(j.titulo, j)
        
        inicio = time.perf_counter()
        bst.buscar(clave_buscada)
        t_arbol = (time.perf_counter() - inicio) * 1000

        print(f"{n:<12} | {t_secuencial:<16.4f} | {t_binaria:<15.4f} | {t_arbol:<15.4f}")

if __name__ == "__main__":
    medir()