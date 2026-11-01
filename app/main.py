"""Aplicación CRUD de postulantes - Punto de entrada principal."""

from __future__ import annotations

import sys
import os

from .models import Postulante
from .services import (
    crear_postulante,
    listar_postulantes,
    actualizar_postulante,
    eliminar_postulante,
    calcular_estado,
)


def mostrar_menu() -> None:
    """Muestra el menú principal y gestiona la opción elegida."""
    while True:
        print("\n========== MENÚ CRUD POSTULANTES ==========")
        print("1. Crear postulante")
        print("2. Leer / Listar postulantes")
        print("3. Actualizar postulante")
        print("4. Eliminar postulante")
        print("5. Salir")
        print("===========================================")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            try:
                edad = int(input("Edad: ").strip())
            except ValueError:
                print("Error: la edad debe ser un número entero.")
                continue
            crear_postulante(nombre, edad)

        elif opcion == "2":
            postulantes = listar_postulantes()
            if not postulantes:
                print("No hay postulantes registrados.")
                continue
            print("\n--- LISTADO DE POSTULANTES ---")
            for i, p in enumerate(postulantes, 1):
                print(f"{i}. Nombre: {p.nombre} | Edad: {p.edad} | Estado: {p.estado}")

        elif opcion == "3":
            postulantes = listar_postulantes()
            if not postulantes:
                print("No hay postulantes para actualizar.")
                continue
            print("\n--- LISTADO DE POSTULANTES ---")
            for i, p in enumerate(postulantes, 1):
                print(f"{i}. Nombre: {p.nombre} | Edad: {p.edad} | Estado: {p.estado}")
            try:
                indice = int(input("\nNúmero del postulante a actualizar: ")) - 1
            except ValueError:
                print("Debes ingresar un número.")
                continue

            nombre_input = input(
                f"Nuevo nombre (Enter para dejar '{postulantes[indice].nombre}'): "
            ).strip()
            edad_input = input(
                f"Nueva edad (Enter para dejar {postulantes[indice].edad}): "
            ).strip()

            nombre = nombre_input if nombre_input else None
            edad = int(edad_input) if edad_input else None

            if actualizar_postulante(indice, nombre, edad):
                print("Registro actualizado correctamente.")

        elif opcion == "4":
            postulantes = listar_postulantes()
            if not postulantes:
                print("No hay postulantes para eliminar.")
                continue
            print("\n--- LISTADO DE POSTULANTES ---")
            for i, p in enumerate(postulantes, 1):
                print(f"{i}. Nombre: {p.nombre} | Edad: {p.edad} | Estado: {p.estado}")
            try:
                indice = int(input("\nNúmero del postulante a eliminar: ")) - 1
            except ValueError:
                print("Debes ingresar un número.")
                continue
            if eliminar_postulante(indice):
                print("Postulante eliminado correctamente.")

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    print("Iniciando aplicación CRUD de postulantes...")
    mostrar_menu()