# ------------------ BIBLIOTECA ------------------
# Biblioteca en memoria: diccionario con secciones y listas de libros
biblioteca = {
    "Ficción": [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
        {"titulo": "1984", "autor": "George Orwell", "anio": 1949}
    ],
    "Ciencia": [
        {"titulo": "Breve historia del tiempo", "autor": "Stephen Hawking", "anio": 1988}
    ],
    "Historia": []
}

# ------------------ FUNCIONES CRUD ------------------
# Mostrar todos los libros
def mostrar_biblioteca():
    for seccion, libros in biblioteca.items():
        print(f"\n=== Sección: {seccion} ===")
        if not libros:
            print("  (Vacía)")
        else:
            for libro in libros:
                print(f"  Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['anio']}")

# Agregar libro
def agregar_libro(seccion, titulo, autor, anio):
    if seccion not in biblioteca:
        biblioteca[seccion] = []
    biblioteca[seccion].append({"titulo": titulo, "autor": autor, "anio": anio})
    print(f"Libro '{titulo}' agregado a la sección '{seccion}'\n")

# Buscar libro
def buscar_libro(titulo):
    for seccion, libros in biblioteca.items():
        for libro in libros:
            if libro["titulo"].lower() == titulo.lower():
                return libro, seccion
    return None, None

# Actualizar libro
def actualizar_libro(titulo, nuevo_titulo=None, nuevo_autor=None, nuevo_anio=None):
    libro, seccion = buscar_libro(titulo)
    if libro:
        if nuevo_titulo:
            libro["titulo"] = nuevo_titulo
        if nuevo_autor:
            libro["autor"] = nuevo_autor
        if nuevo_anio:
            libro["anio"] = nuevo_anio
        print(f"Libro '{titulo}' actualizado en la sección '{seccion}'\n")
        return True
    print("Libro no encontrado.\n")
    return False

# Eliminar libro
def eliminar_libro(titulo):
    libro, seccion = buscar_libro(titulo)
    if libro:
        biblioteca[seccion].remove(libro)
        print(f"Libro '{titulo}' eliminado de la sección '{seccion}'\n")
        return True
    print("Libro no encontrado.\n")
    return False

# ------------------ MENÚ PRINCIPAL ------------------
def menu():
    opcion = ""
    while opcion != "6":
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Mostrar biblioteca")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            seccion = input("Sección: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            agregar_libro(seccion, titulo, autor, anio)

        elif opcion == "2":
            mostrar_biblioteca()

        elif opcion == "3":
            titulo = input("Título a buscar: ")
            libro, seccion = buscar_libro(titulo)
            if libro:
                print(f"Encontrado: {libro} en sección '{seccion}'\n")
            else:
                print("Libro no encontrado.\n")

        elif opcion == "4":
            titulo = input("Título del libro a actualizar: ")
            nuevo_titulo = input("Nuevo título (enter para omitir): ")
            nuevo_autor = input("Nuevo autor (enter para omitir): ")
            nuevo_anio = input("Nuevo año (enter para omitir): ")
            nuevo_anio = int(nuevo_anio) if nuevo_anio else None
            actualizar_libro(titulo, nuevo_titulo or None, nuevo_autor or None, nuevo_anio)

        elif opcion == "5":
            titulo = input("Título del libro a eliminar: ")
            eliminar_libro(titulo)

        elif opcion == "6":
            print("Saliendo...")

        else:
            print("Opción inválida\n")

# Ejecutar menú
menu()