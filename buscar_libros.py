import json
import os
import difflib

def buscar_libros():
    criterio_input = input('Ingrese un criterio de búsqueda (título, autor o género): ').strip()
    criterio = criterio_input.lower()
    if not criterio:
        print('Criterio vacio')
        return

    ruta = "data/libros.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario')
        return

    encontrados = []
    tipo_busqueda = None

    criterio_display = criterio_input.title()

    encontrados = []
    for libro in libros:
        matches = []
        nombre_lower = libro['Nombre'].lower()
        autor_lower = libro['Autor'].lower()
        genero_lower = libro['Genero'].lower()
        
        # Substring match
        if criterio in nombre_lower:
            matches.append('nombre')
        if criterio in autor_lower:
            matches.append('autor')
        if criterio in genero_lower:
            matches.append('genero')
        
        # Fuzzy if no substring and criterio long enough
        if not matches and len(criterio) > 2:
            for field, field_lower in [('Nombre', nombre_lower), ('Autor', autor_lower), ('Genero', genero_lower)]:
                best_match = difflib.get_close_matches(criterio, [field_lower], n=1, cutoff=0.7)
                if best_match:
                    if field == 'Nombre':
                        matches.append('nombre')
                    elif field == 'Autor':
                        matches.append('autor')
                    else:
                        matches.append('genero')
                    break  # One fuzzy per book
        
        if matches:
            libro['_matches'] = matches  # Temp store
            encontrados.append(libro)

    if not encontrados:
        print(f'No se encontraron libros por "{criterio_display}".')
    else:
        for libro in encontrados:
            types_str = ', '.join(libro['_matches'])
            print(f'Libros encontrados por "{criterio_display}" ({types_str}):')
            estado_str = libro['Estado']
            if libro['Estado'] == 'Prestado' and libro['Prestado a']:
                estado_str += f" a {libro['Prestado a']}"
            print(f'- {libro["Nombre"]} | Autor: {libro["Autor"]} | Estado: {estado_str}')
            del libro['_matches']  # Clean up

