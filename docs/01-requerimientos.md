# Documento de Requerimientos — NextGame

Este documento explica que cosas tiene que hacer el programa (requerimientos funcionales), como tiene que comportarse tecnicamente (requerimientos no funcionales) y que cosas quedan afuera del proyecto.

---

## 1. Requerimientos Funcionales (Lo que hace el programa)

Son las funciones que el usuario puede usar desde el menu de la terminal:

* **RF01 — Carga de datos:** El sistema tiene que leer al iniciar un archivo `juegos.json` con al menos 200 videojuegos y cargarlos en memoria en todas las estructuras de datos.
* **RF02 — Busqueda de videojuegos:** El usuario puede escribir el nombre de un juego (o parte del nombre) y el sistema debe encontrarlo y mostrar sus datos (año, generos, desarrollador y calificacion).
* **RF03 — Explorador de categorias:** El sistema tiene que organizar los juegos en una jerarquia (Catalogo -> Generos -> Juegos) y permitir recorrerla nivel por nivel o ver el arbol completo con ramas.
* **RF04 — Ver juegos relacionados:** Al elegir un juego, el sistema tiene que buscar en el grafo que otros juegos estan conectados con el por compartir generos y mostrarlos ordenados por afinidad.
* **RF05 — Sistema de recomendaciones:** El usuario dice que juego le gusto y el sistema le sugiere 3 juegos parecidos con las mejores calificaciones.
* **RF06 — Ver Top 10:** El sistema tiene que mostrar los 10 videojuegos con mejor nota del catalogo usando una cola de prioridad (Heap).

---

## 2. Requerimientos No Funcionales (Como se comporta el sistema)

Son los requisitos para que el programa ande bien:

* **RNF01 — Busqueda rapida:** La busqueda por titulo no tiene que recorrer toda la lista uno por uno a lo bruto; debe resolverse en tiempo logaritmico $O(\log n)$ usando arboles de busqueda balanceados (AVL).
* **RNF02 — Estructuras propias:** Todas las estructuras principales (Arbol Binario, AVL, Arbol General, Heap y Grafo) estan programadas a mano por nosotros, sin usar librerias de Python como heapq o librerias de grafos.
* **RNF03 — Rendimiento en rankings:** Para sacar el Top 10 de mejores juegos no se debe ordenar toda la lista completa con `sort()`, sino usar un Max-Heap para extraer solo los 10 mejores eficientemente.
* **RNF04 — Interfaz accesible:** La aplicacion funciona en cualquier terminal estandar de texto (Windows, Linux, Mac) mediante opciones numeradas simples.

---

## 3. Alcance y Fuera de Alcance

Para tener en claro hasta donde llega el trabajo:

### Lo que si hace el sistema (Alcance):
* Funciona 100% por consola mediante menus de texto.
* Procesa un catalogo local de 200 videojuegos con datos reales.
* Conecta juegos entre si armando una red segun los generos en comun.
* Incluye scripts de prueba separados para demostrar el funcionamiento de cada estructura de datos.

### Lo que NO hace el sistema (Fuera de alcance):
* No tiene ventana grafica con botones, ni mouse, es solo terminal.
* No tiene sistema de usuarios, contraseñas, ni login.
* No guarda datos en bases de datos externas (MySQL); se maneja con el archivo `juegos.json`.
* No descarga datos de internet mientras se ejecuta.
