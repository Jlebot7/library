import json
import os

def reg_libros():
    nombre = input('Ingrese el título del libro: ').title()
    autor = input('Ingrese el nombre del autor: ').title()
    genero = input('Ingrese el género del libro: ').title()
    try:
        year = int(input('Ingrese el año de publicación: '))
    except ValueError:
        print('Año inválido')
        return
    estado = input('Ingrese status del libro (Disponible/Prestado): ').capitalize()
    if estado not in ['Disponible', 'Prestado']:
        print('Estado inválido. Usando Disponible.')
        estado = 'Disponible'
    if estado == 'Prestado':
        prestado = input('Ingrese la persona a la que se presto el libro: ').title()
    else:
        prestado = None

    ruta = "data/libros.json"

    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        libros = []

    if any(libro['Nombre'] == nombre for libro in libros):
        print(f'Libro "{nombre}" ya existe en el inventario.')
        input('Presione ENTER para continuar...')
        return

    libro = {
        'Nombre': nombre,
        'Autor': autor,
        'Genero': genero,
        'Year': year,
        'Estado': estado,
        'Prestado a': prestado
    }
    libros.append(libro)

    os.makedirs('data', exist_ok=True)
    with open(ruta, 'w', encoding='utf-8') as datos:
        json.dump(libros, datos, indent=4, ensure_ascii=False)
    print(f'Libro "{nombre}" registrado exitosamente.')

def listar_libros():
    ruta = "data/libros.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario.')
        return

    if not libros:
        print('El inventario está vacío.')
        return

    print('=' * 80)
    print('| Título           | Autor            | Género        | Estado          |')
    print('=' * 80)
    for libro in libros:
        titulo = libro['Nombre'][:15].ljust(15)
        autor = libro['Autor'][:16].ljust(16)
        genero = libro['Genero'][:12].ljust(12)
        estado_str = f"{libro['Estado']}"
        if libro['Estado'] == 'Prestado' and libro['Prestado a']:
            estado_str += f" a {libro['Prestado a'][:10]}"
        estado_str = estado_str[:16].ljust(16)
        print(f'| {titulo} | {autor} | {genero} | {estado_str} |')
    print('=' * 80)

