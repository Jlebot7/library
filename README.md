# Gestor de Inventario para Biblioteca Virtual

## Descripción
Sistema modular en Python para gestionar inventario de libros: registrar, listar, buscar, prestar/devolver, reportes. Persistencia en JSON. Interfaz por consola

## Estructura del Proyecto
```
Gestor_Biblioteca_Virtual/
├── main.py              # Menú principal
├── gestion_libros.py    # Registrar y listar libros
├── buscar_libros.py     # Búsqueda por título/autor/género
├── prestamos.py         # Prestar y devolver
├── reportes.py          # Reportes agrupados por género + JSON
├── data/
│   ├── libros.json      # Datos principales
│   └── reportes/        # Reportes generados (timestamped)
└── README.md
```

## Cómo Ejecutar
1. `cd biblioteca`
2. `python main.py`
3. Usa opciones 1-7.

## Ejemplos de Uso
- **Registrar**: Op1, ingresa datos → "Libro X registrado."
- **Listar**: Op2 → Tabla | Título | Autor | ...
- **Buscar "fantasía"**: Op3 → "Libros encontrados... - El Hobbit | Autor: ... | Estado: ..."
- **Prestar "1984" a "Juan"**: Op4 → Estado cambia a Prestado.
- **Devolver**: Op5 → Vuelve a Disponible.
- **Reporte**: Op6 → Muestra por género con pausas, guarda `reporte_libros_*.json`.

## Formato libros.json
```json
[{"Nombre":"1984","Autor":"George Orwell","Genero":"Ciencia Ficcion",...}]
```

