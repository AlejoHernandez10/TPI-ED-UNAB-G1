# Gestion del Proyecto y Organizacion del Equipo — NextGame

Este documento describe como nos organizamos en el grupo para ir haciendo las entregas del trabajo practico integrador a lo largo de la cursada.

---

##  Integrantes del Equipo
* **Hernandez Alejo**
* **Mora Joaquin**

---

##  Metodologia de Trabajo

1. **Reuniones breves:** Nos coordinamos por Discord y WhatsApp para charlar sobre que estructuras tocaba hacer en cada TP, definir quien encaraba cada parte y probar el codigo juntos.
2. **Control de versiones con Git:** Usamos GitHub con un unico repositorio compartido.

---

##  Tablero de Tareas (Trello / GitHub Projects)

Organizamos las tareas del proyecto dividiendo las actividades en 3 columnas clasicas:

* **1. Sin Hacer** Trabajos pendientes.
* **2. En progreso:** Cosas en las que estamos trabajando activamente.
* **3. Terminado:** TPs que ya andan bien y estan integradas al menu principal.

> **Enlace al tablero del equipo:**  
> https://trello.com/invite/b/6ae28500c98dd978a4caf32e/ATTI4aed07b14ca86f750e9522324e538b52D012C3EB/nextgame

---

##  Historias de Usuario

pensamos en lo que necesita una persona al usar NextGame:

* **Historia 1 (Busqueda):**  
  * *Como* jugador indeciso, mirando su biblioteca  
  * *quiero* buscar un juego por su nombre,  
  * *para* ver rapidamente de que genero es y que puntaje tiene sin tardar mucho.  
  * **Criterio de aceptacion:** La busqueda responde al instante y utiliza el Arbol AVL balanceado.

* **Historia 2 (Top 10):**  
  * *Como* usuario que busca sugerencias rapidas,  
  * *quiero* ver una lista de los 10 mejores juegos del catalogo,  
  * *para* elegir alguno de los titulos mas reconocidos para probarlo.  
  * **Criterio de aceptacion:** Se muestran exactamente 10 juegos ordenados de mayor a menor nota, usando la estructura Max-Heap.

* **Historia 3 (Juegos parecidos):**  
  * *Como* fanatico de un videojuego en particular,  
  * *quiero* ver que otros juegos se le parecen,  
  * *para* descubrir titulos nuevos con tematicas similares.  
  * **Criterio de aceptacion:** El sistema consulta las conexiones en el Grafo y devuelve los juegos que mas generos comparten con el titulo elegido.
