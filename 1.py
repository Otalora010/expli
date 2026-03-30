
biblioteca = {
    "accion": [
        {"titulo": "rapidos y furioso 1", "director": "rob cohen", "año": 2001 },
        {"titulo": "jhon wick", "director": "chad stahelski", "año":2014 }
    ],
    "ciencia ficcion": [
        {"titulo": "mad max fury road", "director": "george miller", "año": 2015 },
        {"titulo": "intelestellar", "director": "christopher nolan", "año": 2014 }
    ],
    "amor": [
        {"titulo": "como perder a un hombre en 10 dias", "director": "donald peterson", "año": 2003 },
        {"titulo": "la propuesta", "director": "anne fletcher", "año": 2009}
    ]
}

def mostrar_biblioteca():
    for genero, peliculas in biblioteca.items():
        print(f"\n======genero: {genero}======")
        for pelicula in peliculas:
            print(f"titulo: {pelicula['titulo']}, director: {pelicula['director']}, año: {pelicula['año']}")
          
def agregar_pelicula(genero, titulo, director, año):
    if genero not in biblioteca: 
            biblioteca[genero] = []
    biblioteca[genero].append({"titulo": titulo, "director": director, "año": año})  
    print(f"pelicula {titulo} agregada al genero {genero}")

def buscar_pelicula(titulo): 
    for genero, peliculas in biblioteca.items():
          for peliculas in peliculas:    
               if peliculas['titulo'].lower() == titulo.lower():
                   return peliculas, genero 
    return None, None 

def eliminar_pelicula(titulo):
     pelicula, genero = buscar_pelicula(titulo)
     if pelicula:
          biblioteca[genero].remove(pelicula)
          print(f"pelicula {titulo} eliminada del genero {genero}")
          return True
     else:
          print("pelicula no encontrada")
          return False
     
def eliminar_genero(genero):
     genero = genero.strip().lower()
    
     if genero in biblioteca:
        del biblioteca[genero]
        print(f"Género '{genero}' eliminado correctamente")
        return True
     else:
        print("Género no encontrado")
        return False
     
def menu():
    opcion = ""
    while opcion != "6":
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Mostrar biblioteca ")
        print("2. Agregar pelicula ")
        print("3. Buscar pelicula")
        print("4. Eliminar pelicula")
        print("5. Eliminar género")
        print("6. Salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            mostrar_biblioteca()
        elif opcion == "2":
            genero = input("genero: " )
            titulo = input("titulo: ")
            director = input("director: ")
            año = int(input("año: "))
            agregar_pelicula(genero, titulo, director, año)
        elif opcion == "3": 
            titulo = input("Título a buscar: ")
            pelicula, genero = buscar_pelicula(titulo)
            if pelicula:
                print(f"Encontrado: {pelicula} en sección '{genero}'\n")
            else:
                print("pelicula no encontrado.\n")
        elif opcion  == "4":
            titulo = input("titulo a eliminar: ")
            eliminar_pelicula(titulo)
        elif opcion == "5":
             genero = input("Género a eliminar: ")
             eliminar_genero(genero)
        elif opcion == "6":
            print("saliendo.......")
menu()
