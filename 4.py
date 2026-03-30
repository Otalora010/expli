tienda = {
    "productos": [
        {"id": 1, "nombre": "laptop", "precio": 3000, "stock": 5},
        {"id": 2, "nombre": "mouse", "precio": 50, "stock": 10}
    ],
    "clientes": [],
    "ventas": []
}

# -------- VALIDACIONES --------

def es_numero_positivo(valor):
    return valor.isdigit() and int(valor) > 0

def texto_valido(texto):
    return len(texto.strip()) > 0


# -------- MOSTRAR --------

def mostrar_productos():
    print("\n=== PRODUCTOS ===")
    for p in tienda["productos"]:
        print(f"ID: {p['id']} | {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")


def mostrar_clientes():
    print("\n=== CLIENTES ===")
    for c in tienda["clientes"]:
        print(f"ID: {c['id']} | Nombre: {c['nombre']}")


def mostrar_ventas():
    print("\n=== VENTAS ===")
    for v in tienda["ventas"]:
        print(f"Cliente: {v['cliente']} | Producto: {v['producto']} | Cantidad: {v['cantidad']}")


# -------- AGREGAR --------

def agregar_producto():
    nombre = input("Nombre producto: ")
    while not texto_valido(nombre):
        nombre = input("Error. Nombre producto: ")

    precio = input("Precio: ")
    while not es_numero_positivo(precio):
        precio = input("Error. Precio: ")

    stock = input("Stock: ")
    while not es_numero_positivo(stock):
        stock = input("Error. Stock: ")

    nuevo_id = len(tienda["productos"]) + 1

    tienda["productos"].append({
        "id": nuevo_id,
        "nombre": nombre.lower(),
        "precio": int(precio),
        "stock": int(stock)
    })

    print("Producto agregado")


def agregar_cliente():
    nombre = input("Nombre cliente: ")
    while not texto_valido(nombre):
        nombre = input("Error. Nombre cliente: ")

    nuevo_id = len(tienda["clientes"]) + 1

    tienda["clientes"].append({
        "id": nuevo_id,
        "nombre": nombre.lower()
    })

    print("Cliente agregado")


# -------- BUSCAR --------

def buscar_producto(id_buscar):
    for p in tienda["productos"]:
        if p["id"] == id_buscar:
            return p
    return None


def buscar_cliente(id_buscar):
    for c in tienda["clientes"]:
        if c["id"] == id_buscar:
            return c
    return None


# -------- VENDER (PRÉSTAMO) --------

def realizar_venta():
    mostrar_productos()
    id_producto = input("ID producto: ")

    if not es_numero_positivo(id_producto):
        print("ID inválido")
        return

    producto = buscar_producto(int(id_producto))
    if not producto:
        print("Producto no existe")
        return

    mostrar_clientes()
    id_cliente = input("ID cliente: ")

    if not es_numero_positivo(id_cliente):
        print("ID inválido")
        return

    cliente = buscar_cliente(int(id_cliente))
    if not cliente:
        print("Cliente no existe")
        return

    cantidad = input("Cantidad: ")
    if not es_numero_positivo(cantidad):
        print("Cantidad inválida")
        return

    cantidad = int(cantidad)

    if producto["stock"] < cantidad:
        print("No hay suficiente stock")
        return

    # descontar stock
    producto["stock"] -= cantidad

    # registrar venta
    tienda["ventas"].append({
        "cliente": cliente["nombre"],
        "producto": producto["nombre"],
        "cantidad": cantidad
    })

    print("Venta realizada")


# -------- ELIMINAR --------

def eliminar_producto():
    mostrar_productos()
    id_eliminar = input("ID producto a eliminar: ")

    if not es_numero_positivo(id_eliminar):
        return

    producto = buscar_producto(int(id_eliminar))

    if producto:
        tienda["productos"].remove(producto)
        print("Producto eliminado")
    else:
        print("No encontrado")


# -------- MENU --------

def menu():
    opcion = ""

    while opcion != "8":
        print("\n=== TIENDA ===")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Agregar cliente")
        print("4. Ver clientes")
        print("5. Realizar venta")
        print("6. Ver ventas")
        print("7. Eliminar producto")
        print("8. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            agregar_producto()

        elif opcion == "3":
            agregar_cliente()

        elif opcion == "4":
            mostrar_clientes()

        elif opcion == "5":
            realizar_venta()

        elif opcion == "6":
            mostrar_ventas()

        elif opcion == "7":
            eliminar_producto()

        elif opcion == "8":
            print("Saliendo...")


menu()