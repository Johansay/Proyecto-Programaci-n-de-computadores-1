# ============================================================
# CRUD COMPLETO DE POSTULANTES
# Almacenamiento: archivo TXT (postulantes.txt)
# Formato de cada línea: nombre|edad|estado
# ============================================================

import os

ARCHIVO = "postulantes.txt"


# ------------------------------------------------------------
# Funciones de utilidad
# ------------------------------------------------------------
def verificar_edad(edad):
    """Retorna True si la edad está entre 18 y 27 años inclusive."""
    return 18 <= edad <= 27


def cargar_postulantes():
    """Lee el archivo y devuelve una lista de diccionarios."""
    postulantes = []
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
                        postulantes.append({
                            "nombre": nombre,
                            "edad": int(edad_str),
                            "estado": estado
                        })
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return postulantes


def guardar_postulantes(postulantes):
    """Escribe toda la lista de postulantes en el archivo."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for p in postulantes:
                f.write(f"{p['nombre']}|{p['edad']}|{p['estado']}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


# ------------------------------------------------------------
# Operaciones del CRUD
# ------------------------------------------------------------
def crear_registro():
    print("\n--- CREAR NUEVO POSTULANTE ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return

    try:
        edad = int(input("Edad: ").strip())
    except ValueError:
        print("Error: la edad debe ser un número entero.")
        return

    if verificar_edad(edad):
        estado = "Elegible"
    else:
        estado = "No elegible"

    postulantes = cargar_postulantes()
    postulantes.append({"nombre": nombre, "edad": edad, "estado": estado})
    guardar_postulantes(postulantes)
    print(f"Postulante '{nombre}' creado con estado: {estado}")


def leer_registros():
    print("\n--- LISTADO DE POSTULANTES ---")

    postulantes = cargar_postulantes()

    if not postulantes:
        print("No hay postulantes registrados.")
        return

    for i, p in enumerate(postulantes, 1):
        print(f"{i}. Nombre: {p['nombre']} | Edad: {p['edad']} | Estado: {p['estado']}")
def actualizar_registro():
    print("\n--- ACTUALIZAR POSTULANTE ---")
    postulantes = cargar_postulantes()
    if not postulantes:
        print("No hay postulantes para actualizar.")
        return

    leer_registros()
    try:
        indice = int(input("\nNúmero del postulante a actualizar: ")) - 1
        if indice < 0 or indice >= len(postulantes):
            print("Número inválido.")
            return
    except ValueError:
        print("Debes ingresar un número.")
        return

    print(f"\nEditando a: {postulantes[indice]['nombre']}")
    
    nuevo_nombre = input(f"Nuevo nombre (Enter para dejar '{postulantes[indice]['nombre']}'): ").strip()
    if nuevo_nombre:
        postulantes[indice]["nombre"] = nuevo_nombre

    nueva_edad_str = input(f"Nueva edad (Enter para dejar {postulantes[indice]['edad']}): ").strip()
    if nueva_edad_str:
        try:
            nueva_edad = int(nueva_edad_str)
            postulantes[indice]["edad"] = nueva_edad
            postulantes[indice]["estado"] = "Elegible" if verificar_edad(nueva_edad) else "No elegible"
        except ValueError:
            print("Edad inválida. No se modificó.")
            return

    guardar_postulantes(postulantes)
    print("Registro actualizado correctamente.")


def eliminar_registro():
    print("\n--- ELIMINAR POSTULANTE ---")
    postulantes = cargar_postulantes()
    if not postulantes:
        print("No hay postulantes para eliminar.")
        return

    leer_registros()
    try:
        indice = int(input("\nNúmero del postulante a eliminar: ")) - 1
        if indice < 0 or indice >= len(postulantes):
            print("Número inválido.")
            return
    except ValueError:
        print("Debes ingresar un número.")
        return

    eliminado = postulantes.pop(indice)
    guardar_postulantes(postulantes)
    print(f"Postulante '{eliminado['nombre']}' eliminado correctamente.")


# ------------------------------------------------------------
# Menú principal
# ------------------------------------------------------------
def menu():
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
            crear_registro()
        elif opcion == "2":
            leer_registros()
        elif opcion == "3":
            actualizar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# ------------------------------------------------------------
# Ejecución
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()