cursos = {
    "programacion": [
        {"nombre": "python basico", "instructor": "juan perez", "duracion": 20},
        {"nombre": "javascript", "instructor": "ana lopez", "duracion": 15}
    ],
    "diseno": [
        {"nombre": "photoshop", "instructor": "carlos ruiz", "duracion": 10}
    ]
}

# ---------------- MOSTRAR ----------------
def mostrar_cursos():
    for categoria, lista_cursos in cursos.items():
        print(f"\n====== CATEGORIA: {categoria} ======")
        for curso in lista_cursos:
            print(f"Curso: {curso['nombre']}, Instructor: {curso['instructor']}, Duración: {curso['duracion']} horas")


# ---------------- AGREGAR ----------------
def agregar_curso(categoria, nombre, instructor, duracion):
    categoria = categoria.strip().lower()
    
    if categoria not in cursos:
        cursos[categoria] = []
    
    cursos[categoria].append({
        "nombre": nombre,
        "instructor": instructor,
        "duracion": duracion
    })
    
    print(f"Curso '{nombre}' agregado a {categoria}")


# ---------------- BUSCAR ----------------
def buscar_curso(nombre):
    nombre = nombre.strip().lower()
    
    for categoria, lista_cursos in cursos.items():
        for curso in lista_cursos:
            if curso["nombre"].lower() == nombre:
                return curso, categoria
    
    return None, None


# ---------------- ELIMINAR CURSO ----------------
def eliminar_curso(nombre):
    curso, categoria = buscar_curso(nombre)
    
    if curso:
        cursos[categoria].remove(curso)
        print(f"Curso eliminado de {categoria}")
    else:
        print("Curso no encontrado")


# ---------------- ELIMINAR CATEGORIA ----------------
def eliminar_categoria(categoria):
    categoria = categoria.strip().lower()
    
    if categoria in cursos:
        del cursos[categoria]
        print(f"Categoría '{categoria}' eliminada")
    else:
        print("Categoría no encontrada")


# ---------------- MENU ----------------
def menu():
    opcion = ""
    
    while opcion != "6":
        print("\n=== MENÚ CURSOS ===")
        print("1. Mostrar cursos")
        print("2. Agregar curso")
        print("3. Buscar curso")
        print("4. Eliminar curso")
        print("5. Eliminar categoría")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_cursos()
        
        elif opcion == "2":
            categoria = input("Categoría: ")
            nombre = input("Nombre del curso: ")
            instructor = input("Instructor: ")
            duracion = int(input("Duración (horas): "))
            
            agregar_curso(categoria, nombre, instructor, duracion)
        
        elif opcion == "3":
            nombre = input("Curso a buscar: ")
            curso, categoria = buscar_curso(nombre)
            
            if curso:
                print(f"Encontrado: {curso} en '{categoria}'")
            else:
                print("Curso no encontrado")
        
        elif opcion == "4":
            nombre = input("Curso a eliminar: ")
            eliminar_curso(nombre)
        
        elif opcion == "5":
            categoria = input("Categoría a eliminar: ")
            eliminar_categoria(categoria)
        
        elif opcion == "6":
            print("Saliendo...")


menu()