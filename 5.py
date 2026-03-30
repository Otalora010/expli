biblioteca = {
    "libros": [
        {"id": 1, "titulo": "el principito", "autor": "antoine", "disponible": True},
        {"id": 2, "titulo": "1984", "autor": "orwell", "disponible": True}
    ],
    "usuarios": [],
    "prestamos": []
}

# -------- VALIDACIONES --------

def texto_valido(texto):
    return len(texto.strip()) > 0

def numero_valido(valor):
    return valor.isdigit()


# -------- MOSTRAR --------

def mostrar_libros():
    print("\n=== LIBROS ===")
    for l in biblioteca["libros"]:
        estado = "Disponible" if l["disponible"] else "Prestado"
        print(f"ID: {l['id']} | {l['titulo']} | {estado}")


def mostrar_usuarios():
    print("\n=== USUARIOS ===")
    for u in biblioteca["usuarios"]:
        print(f"ID: {u['id']} | {u['nombre']}")


def mostrar_prestamos():
    print("\n=== PRESTAMOS ===")
    for p in biblioteca["prestamos"]:
        print(f"Usuario: {p['usuario']} | Libro: {p['libro']}")


# -------- AGREGAR --------

def agregar_usuario():
    nombre = input("Nombre usuario: ")
    while not texto_valido(nombre):
        nombre = input("Error. Nombre usuario: ")

    nuevo_id = len(biblioteca["usuarios"]) + 1

    biblioteca["usuarios"].append({
        "id": nuevo_id,
        "nombre": nombre.lower()
    })

    print("Usuario agregado")


# -------- BUSCAR --------

def buscar_libro(id_buscar):
    for l in biblioteca["libros"]:
        if l["id"] == id_buscar:
            return l
    return None


def buscar_usuario(id_buscar):
    for u in biblioteca["usuarios"]:
        if u["id"] == id_buscar:
            return u
    return None


# -------- PRESTAR LIBRO --------

def prestar_libro():
    mostrar_libros()
    id_libro = input("ID libro: ")

    if not numero_valido(id_libro):
        print("ID inválido")
        return

    libro = buscar_libro(int(id_libro))

    if not libro:
        print("Libro no existe")
        return

    if not libro["disponible"]:
        print("Libro ya prestado")
        return

    mostrar_usuarios()
    id_usuario = input("ID usuario: ")

    if not numero_valido(id_usuario):
        print("ID inválido")
        return

    usuario = buscar_usuario(int(id_usuario))

    if not usuario:
        print("Usuario no existe")
        return

    # marcar como prestado
    libro["disponible"] = False

    biblioteca["prestamos"].append({
        "usuario": usuario["nombre"],
        "libro": libro["titulo"]
    })

    print("Préstamo realizado")


# -------- DEVOLVER LIBRO --------

def devolver_libro():
    mostrar_libros()
    id_libro = input("ID libro a devolver: ")

    if not numero_valido(id_libro):
        return

    libro = buscar_libro(int(id_libro))

    if libro and not libro["disponible"]:
        libro["disponible"] = True
        print("Libro devuelto")
    else:
        print("No se puede devolver")


# -------- MENU --------

def menu():
    opcion = ""

    while opcion != "6":
        print("\n=== BIBLIOTECA ===")
        print("1. Ver libros")
        print("2. Agregar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver prestamos")
        print("6. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_libros()

        elif opcion == "2":
            agregar_usuario()

        elif opcion == "3":
            prestar_libro()

        elif opcion == "4":
            devolver_libro()

        elif opcion == "5":
            mostrar_prestamos()

        elif opcion == "6":
            print("Saliendo...")


menu()