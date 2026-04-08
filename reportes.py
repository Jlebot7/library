import json
import os
from collections import defaultdict
from datetime import datetime

def generar_reporte():
    ruta = "data/libros.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario para generar reporte.')
        input('Presione ENTER para continuar...')
        return

    if not libros:
        print('El inventario está vacío.')
        input('Presione ENTER para continuar...')
        return

    # Group by Genero
    grupos = defaultdict(list)
    for libro in libros:
        grupos[libro['Genero']].append(libro)

    print('=' * 50)
    print('REPORTE DEL INVENTARIO DE LIBROS')
    print('=' * 50)

    reporte_data = []
    for genero, lista_libros in grupos.items():
        print(f'{genero}:')
        for libro in lista_libros:
            estado_str = libro['Estado']
            if libro['Estado'] == 'Prestado' and libro['Prestado a']:
                estado_str += f" | {libro['Prestado a']}"
            print(f'- {libro["Nombre"]} | Autor: {libro["Autor"]} | Estado: {estado_str}')
        print('-' * 50)
        input('Presione ENTER para continuar al siguiente género...')

        libros_info = []
        for lb in lista_libros:
            est = lb['Estado']
            if lb['Prestado a']:
                est += f" a {lb['Prestado a']}"
            libros_info.append({
                "titulo": lb['Nombre'],
                "autor": lb['Autor'],
                "estado": est
            })
        reporte_data.append({
            "categoria": genero,
            "libros": libros_info
        })

    os.makedirs('data/reportes', exist_ok=True)
    fecha = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"data/reportes/reporte_libros_{fecha}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reporte_data, f, indent=4, ensure_ascii=False)
    print(f'Reporte guardado en {filename}')

    input('Presione ENTER para volver al menú...')

