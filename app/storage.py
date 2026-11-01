import os
from typing import List
from .models import Postulante, PostulanteList

# Ruta relative al archivo de datos (data/postulantes.txt)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ARCHIVO = os.path.join(DATA_DIR, "postulantes.txt")


def cargar_postulantes() -> PostulanteList:
    """Lee el archivo y devuelve una lista de objetos Postulante."""
    postulantes: PostulanteList = []
    if not os.path.exists(ARCHIVO):
        return postulantes

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    partes = linea.split("|")
                    if len(partes) == 3:
                        nombre, edad_str, estado = partes
                        try:
                            edad = int(edad_str)
                            postulantes.append(Postulante(nombre=nombre, edad=edad, estado=estado))
                        except ValueError:
                            # Si la edad no es válida, skippear esa línea
                            continue
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return postulantes


def guardar_postulantes(postulantes: PostulanteList) -> None:
    """Escribe toda la lista de postulantes en el archivo."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for p in postulantes:
                f.write(f"{p.nombre}|{p.edad}|{p.estado}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")