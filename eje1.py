# ------------------- INVENTARIO EN MEMORIA -------------------

# Lista de productos, cada producto es un diccionario
inventario = []

# ------------------- FUNCIONES DEL INVENTARIO -------------------

def agregar_producto(nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"{nombre} agregado al inventario.\n")

def mostrar_inventario():
    """Muestra todos los productos del inventario"""
    if not inventario:
        print("Inventario vacío.\n")
        return
    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print()

def buscar_producto(nombre):
    """Busca un producto por nombre"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto"""
    p = buscar_producto(nombre)
    if not p:
        print("Producto no encontrado.\n")
        return False
    if nuevo_precio is not None:
        p["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        p["cantidad"] = nueva_cantidad
    print(f"{nombre} actualizado.\n")
    return True

def eliminar_producto(nombre):
    """Elimina un producto del inventario"""
    global inventario
    inicial_len = len(inventario)
    inventario = [p for p in inventario if p["nombre"].lower() != nombre.lower()]
    if len(inventario) < inicial_len:
        print(f"{nombre} eliminado del inventario.\n")
        return True
    print("Producto no encontrado.\n")
    return False

def calcular_estadisticas():
    """Calcula estadísticas del inventario"""
    if not inventario:
        print("Inventario vacío.\n")
        return
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"]*p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)\n")

# ------------------- MENÚ PRINCIPAL -------------------

def menu():
    opcion = ""
    while opcion != "6":
        print("=== MENÚ ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas / Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(nombre, precio, cantidad)

            elif opcion == "2":
                mostrar_inventario()

            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                p = buscar_producto(nombre)
                if p:
                    print(f"Encontrado: {p}\n")
                else:
                    print("Producto no encontrado.\n")

            elif opcion == "4":
                nombre = input("Producto a actualizar: ")
                precio = input("Nuevo precio (enter para omitir): ")
                cantidad = input("Nueva cantidad (enter para omitir): ")
                precio = float(precio) if precio else None
                cantidad = int(cantidad) if cantidad else None
                actualizar_producto(nombre, precio, cantidad)

            elif opcion == "5":
                nombre = input("Producto a eliminar: ")
                eliminar_producto(nombre)

            elif opcion == "6":
                calcular_estadisticas()
                print("Saliendo...\n")
                break

            else:
                print("Opción inválida. Intente nuevamente.\n")

        except ValueError:
            print("Entrada inválida. Use números para precio y cantidad.\n")

# ------------------- EJECUTAR MENÚ -------------------

menu()