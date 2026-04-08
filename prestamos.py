import json
import os

def prestar_libro():
    titulo = input('Ingrese el título del libro que desea prestar: ').title().strip()
    if not titulo:
        print('Título vacío.')
        return

    usuario = input('Ingrese el nombre del usuario que tomará el libro prestado: ').title().strip()

    ruta = "data/libros.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario.')
        return

    encontrado = False
    for libro in libros:
        if libro['Nombre'] == titulo:
            if libro['Estado'] == 'Disponible':
                libro['Estado'] = 'Prestado'
                libro['Prestado a'] = usuario
                os.makedirs('data', exist_ok=True)
                with open(ruta, 'w', encoding='utf-8') as datos:
                    json.dump(libros, datos, indent=4, ensure_ascii=False)
                print(f'Libro "{titulo}" prestado a {usuario}.')
                encontrado = True
                break
            else:
                print(f'Libro "{titulo}" no está disponible (estado: {libro["Estado"]}).')
                encontrado = True
                break

    if not encontrado:
        print(f'Libro "{titulo}" no encontrado.')

def devolver_libro():
    titulo = input('Ingrese el título del libro que desea devolver: ').title().strip()
    if not titulo:
        print('Título vacío.')
        return

    ruta = "data/libros.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario.')
        return

    encontrado = False
    for libro in libros:
        if libro['Nombre'] == titulo:
            if libro['Estado'] == 'Prestado':
                libro['Estado'] = 'Disponible'
                libro['Prestado a'] = None
                os.makedirs('data', exist_ok=True)
                with open(ruta, 'w', encoding='utf-8') as datos:
                    json.dump(libros, datos, indent=4, ensure_ascii=False)
                print(f'Libro "{titulo}" ha sido devuelto y está disponible nuevamente.')
                encontrado = True
                break
            else:
                print(f'Libro "{titulo}" no está prestado (estado: {libro["Estado"]}).')
                encontrado = True
                break

    if not encontrado:
        print(f'Libro "{titulo}" no encontrado.')

