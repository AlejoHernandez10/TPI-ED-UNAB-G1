# Analisis de Complejidad y Comparativa de Algoritmos

Este documento resume los resultados del experimento que hicimos con el script `algoritmos/medicion_tiempos.py` para medir y comparar que tan rapido responden distintas estrategias de busqueda a medida que crece la cantidad de videojuegos.

---

## 1. El experimento

Para ver el comportamiento en el peor caso posible (buscar un elemento que no existe en el catalogo), generamos listas de juegos aleatorios de 3 tamanos distintos:
* **1.000 elementos**
* **10.000 elementos**
* **100.000 elementos**

Probamos tres formas diferentes de buscar el elemento:
1. **Busqueda secuencial:** Recorrer la lista elemento por elemento desde el primero hasta el ultimo.
2. **Busqueda binaria:** Ordenar la lista por titulo y buscar dividiendo a la mitad en cada paso.
3. **Arbol Binario de Busqueda (BST):** Buscar bajando por las ramas del arbol comparando si la clave es menor o mayor.

---

## 2. Tabla de mediciones reales

Los tiempos obtenidos en milisegundos (ms) con `time.perf_counter()` fueron los siguientes:

| N Elementos | Busqueda Secuencial (ms) | Busqueda Binaria (ms) | Arbol BST (ms) |
| :--- | :---: | :---: | :---: |
| **1.000** | 0.0807 ms | 0.0073 ms | 0.0083 ms |
| **10.000** | 0.7219 ms | 0.0096 ms | 0.0070 ms |
| **100.000** | 9.0033 ms | 0.0238 ms | 0.0051 ms |

---

## 3. Analisis teorico de complejidad (Notacion O)

* **Busqueda secuencial — $O(n)$:**  
  El tiempo crece de forma lineal y directamente proporcional a la cantidad de elementos. Si multiplicamos el dataset por 10, el tiempo se multiplica por 10 (se nota claramente al pasar de 0.7 ms a 9 ms con 100.000 elementos).
* **Busqueda binaria — $O(\log n)$:**  
  El tiempo crece muy despacio porque en cada comparacion se descarta la mitad de los datos. La desventaja es que para poder usarla la lista tiene que mantenerse ordenada previamente ($O(n \log n)$).
* **Arbol binario — $O(\log n)$ promedio:**  
  La busqueda en el arbol es igual de rapida que la binaria pero tiene la ventaja de que permite insertar elementos nuevos en tiempo logaritmico sin tener que reordenar toda la lista en memoria.

---

## 4. Conclusion tecnica

Para un catalogo chico de 200 juegos, cualquier metodo responde en menos de un milisegundo. Pero pensando en una base de datos real con decenas de miles de videojuegos, la busqueda secuencial es inviable. 

Por eso en NextGame elegimos indexar los titulos en estructuras de arbol (BST y AVL), garantizando busquedas en tiempo logaritmico $O(\log n)$ sin importar cuanto crezca el catalogo.
