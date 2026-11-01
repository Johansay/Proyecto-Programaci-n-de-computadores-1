"""Módulo de servicios de negocio para el CRUD de postulantes."""
import os
from typing import Optional
from .models import Postulante, PostulanteList
from .storage import cargar_postulantes, guardar_postulantes


def verificar_edad(edad: int) -> bool:
    """Retorna True si la edad está entre 18 y 27 años inclusive."""
    return 18 <= edad <= 27


def calcular_estado(edad: int) -> str:
    """Determina el estado basándose en la edad."""
    if verificar_edad(edad):
        return "Elegible"
    return "No elegible"


def crear_postulante(nombre: str, edad: int) -> Optional[Postulante]:
    """Crea un nuevo postulante y lo guarda en el archivo."""
    if not nombre or not nombre.strip():
        print("Error: el nombre no puede estar vacío.")
        return None

    estado = calcular_estado(edad)
    postulantes = cargar_postulantes()
    postulantes.append(Postulante(nombre=nombre.strip(), edad=edad, estado=estado))
    guardar_postulantes(postulantes)
    return postulantes[-1]


def listar_postulantes() -> PostulanteList:
    """Retorna la lista completa de postulantes."""
    return cargar_postulantes()


def actualizar_postulante(indice: int, nombre: Optional[str] = None,
                          edad: Optional[int] = None) -> bool:
    """Actualiza un postulante por índice. Retorna True si tuvo éxito."""
    postulantes = cargar_postulantes()
    if indice < 0 or indice >= len(postulantes):
        print("Número inválido.")
        return False

    p = postulantes[indice]
    if nombre is not None:
        p.nombre = nombre.strip() if nombre else p.nombre
    if edad is not None:
        p.edad = edad
        p.estado = calcular_estado(edad)

    guardar_postulantes(postulantes)
    return True


def eliminar_postulante(indice: int) -> bool:
    """Elimina un postulante por índice. Retorna True si tuvo éxito."""
    postulantes = cargar_postulantes()
    if indice < 0 or indice >= len(postulantes):
        print("Número inválido.")
        return False

    eliminado = postulantes.pop(indice)
    guardar_postulantes(postulantes)
    return True