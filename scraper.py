"""
Scraper de 200 juegos desde la API de RAWG.
Genera un archivo juegos.json con la estructura:
{
    "id": 1,
    "titulo": "The Witcher 3",
    "generos": ["RPG", "Acción", ...],
    "desarrollador": "CD Projekt Red",
    "calificacion": 9.8,
    "anioPublicacion": 2015,
    "web": "https://thewitcher.com/3"
}

Requisitos:
    pip install requests

Uso:
    1. Crear una cuenta gratis en https://rawg.io/apidocs y obtener una API key.
    2. Pegar la key en API_KEY (o exportarla como variable de entorno RAWG_API_KEY).
    3. python scraper_rawg.py
"""

import json
import os
import time

import requests

API_KEY = os.environ.get("RAWG_API_KEY", "PONE TU CLAVE ACA")
BASE_URL = "https://api.rawg.io/api"
TOTAL_JUEGOS = 200
PAGE_SIZE = 40  # maximo que permite RAWG por pagina
PAUSA_SEGUNDOS = 0.3  # para no saturar la API

# traduccion de generos al espanol
GENEROS_ES = {
    "Action": "Acción",
    "Adventure": "Aventura",
    "RPG": "RPG",
    "Strategy": "Estrategia",
    "Shooter": "Shooter",
    "Casual": "Casual",
    "Simulation": "Simulación",
    "Puzzle": "Puzzle",
    "Arcade": "Arcade",
    "Platformer": "Plataformas",
    "Racing": "Carreras",
    "Sports": "Deportes",
    "Fighting": "Lucha",
    "Family": "Familiar",
    "Board Games": "Juegos de mesa",
    "Educational": "Educativo",
    "Card": "Cartas",
    "Massively Multiplayer": "Multijugador masivo",
    "Indie": "Indie",
}


def obtener_lista_juegos(cantidad):
    # trae la lista basica de juegos (ordenados por popularidad)
    juegos = []
    pagina = 1
    while len(juegos) < cantidad:
        resp = requests.get(
            f"{BASE_URL}/games",
            params={
                "key": API_KEY,
                "page": pagina,
                "page_size": PAGE_SIZE,
                "ordering": "-added",  # los mas populares primero
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        juegos.extend(data.get("results", []))
        if not data.get("next"):
            break
        pagina += 1
        time.sleep(PAUSA_SEGUNDOS)
    return juegos[:cantidad]


def obtener_detalle(juego_id):
    # el endpoint de detalle trae desarrollador y sitio web
    resp = requests.get(
        f"{BASE_URL}/games/{juego_id}",
        params={"key": API_KEY},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def transformar(idx, basico, detalle):
    generos = [
        GENEROS_ES.get(g["name"], g["name"]) for g in basico.get("genres", [])
    ]
    desarrolladores = detalle.get("developers", [])
    desarrollador = desarrolladores[0]["name"] if desarrolladores else "Desconocido"

    # RAWG califica de 0 a 5, lo pasamos a escala de 0 a 10
    rating = basico.get("rating") or 0
    calificacion = round(rating * 2, 1)

    released = basico.get("released") or ""
    anio = int(released[:4]) if released[:4].isdigit() else None

    return {
        "id": idx,
        "titulo": basico.get("name", ""),
        "generos": generos,
        "desarrollador": desarrollador,
        "calificacion": calificacion,
        "anioPublicacion": anio,
        "web": detalle.get("website") or "",
    }


def main():
    if API_KEY == "TU_API_KEY_ACA":
        raise SystemExit(
            "Falta la API key. Conseguí una gratis en https://rawg.io/apidocs "
            "y pegala en API_KEY o exportá RAWG_API_KEY."
        )

    print(f"Descargando lista de {TOTAL_JUEGOS} juegos...")
    lista = obtener_lista_juegos(TOTAL_JUEGOS)
    print(f"Lista obtenida: {len(lista)} juegos. Descargando detalles...")

    resultado = []
    for i, juego in enumerate(lista, start=1):
        try:
            detalle = obtener_detalle(juego["id"])
            resultado.append(transformar(i, juego, detalle))
            print(f"[{i}/{len(lista)}] {juego['name']}")
        except requests.RequestException as e:
            print(f"[{i}/{len(lista)}] Error con {juego.get('name')}: {e}")
        time.sleep(PAUSA_SEGUNDOS)

    with open("juegos.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"\nListo: {len(resultado)} juegos guardados en juegos.json")


if __name__ == "__main__":
    main()