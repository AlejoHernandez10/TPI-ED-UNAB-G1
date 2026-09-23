import json
from typing import List, Set, Optional
from modelos.juego import Juego
from estructuras.arbol_binario import ArbolBinarioBusqueda

class CatalogoJuegos:
    def __init__(self):
        self._juegos: List[Juego] = []
        self._bst: ArbolBinarioBusqueda = ArbolBinarioBusqueda()

    def cargar_desde_json(self, ruta_archivo: str) -> None:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                datos = json.load(file)
                self._juegos = []
                self._bst = ArbolBinarioBusqueda()
                
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
                    self._juegos.append(juego)
                    # Integración: Insertar en el Árbol Binario de Búsqueda
                    self._bst.insertar(juego.titulo, juego)

            print(f"✅ Se cargaron exitosamente {len(self._juegos)} videojuegos.")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{ruta_archivo}' no es un JSON válido.")

    # --- BÚSQUEDA INTEGRADA CON BST ---
    def buscar_por_titulo(self, titulo: str) -> List[Juego]:
        """Usa el BST para la búsqueda de la aplicación."""
        resultado = self._bst.buscar(titulo)
        if resultado:
            return [resultado]
        
        # Búsqueda por subcadena dentro de los nodos recorridos (inorder) si no hay coincidencia exacta
        palabra = titulo.strip().lower()
        return [j for j in self._bst.inorder() if palabra in j.titulo.lower()]

    def obtener_por_genero(self, genero: str) -> List[Juego]:
        return [j for j in self._bst.inorder() if j.tiene_genero(genero)]

    def obtener_todos_los_generos(self) -> List[str]:
        todos: Set[str] = set()
        for j in self._bst.inorder():
            todos.update(j.generos)
        return sorted(list(todos))

    def obtener_relacionados(self, juego_base: Juego, limite: int = 5) -> List[Juego]:
        candidatos = []
        for j in self._bst.inorder():
            if j.id != juego_base.id:
                coincidencias = juego_base.generos_en_comun(j)
                if coincidencias > 0:
                    candidatos.append((j, coincidencias))

        candidatos.sort(key=lambda item: (item[1], item[0].calificacion), reverse=True)
        return [j for j, _ in candidatos[:limite]]

    def obtener_recomendaciones(self, juego_base: Juego, limite: int = 3) -> List[Juego]:
        relacionados = self.obtener_relacionados(juego_base, limite=limite * 2)
        recomendaciones = sorted(relacionados, key=lambda j: j.calificacion, reverse=True)
        return recomendaciones[:limite]

    def obtener_top_n(self, n: int = 10) -> List[Juego]:
        return sorted(self._bst.inorder(), key=lambda j: j.calificacion, reverse=True)[:n]