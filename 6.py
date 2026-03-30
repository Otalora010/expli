banco = {
    "cuentas": []
}

# -------- VALIDACIONES --------

def texto_valido(texto):
    return len(texto.strip()) > 0

def numero_valido(valor):
    return valor.isdigit()

def monto_valido(valor):
    return valor.isdigit() and int(valor) > 0


# -------- CREAR CUENTA --------

def crear_cuenta():
    nombre = input("Nombre del cliente: ")
    while not texto_valido(nombre):
        nombre = input("Error. Nombre: ")

    saldo = input("Saldo inicial: ")
    while not monto_valido(saldo):
        saldo = input("Error. Saldo inicial: ")

    nuevo_id = len(banco["cuentas"]) + 1

    banco["cuentas"].append({
        "id": nuevo_id,
        "nombre": nombre.lower(),
        "saldo": int(saldo)
    })

    print("Cuenta creada correctamente")


# -------- MOSTRAR CUENTAS --------

def mostrar_cuentas():
    print("\n=== CUENTAS ===")
    for c in banco["cuentas"]:
        print(f"ID: {c['id']} | Cliente: {c['nombre']} | Saldo: {c['saldo']}")


# -------- BUSCAR CUENTA --------

def buscar_cuenta(id_buscar):
    for c in banco["cuentas"]:
        if c["id"] == id_buscar:
            return c
    return None


# -------- DEPOSITAR --------

def depositar():
    mostrar_cuentas()
    id_cuenta = input("ID cuenta: ")

    if not numero_valido(id_cuenta):
        print("ID inválido")
        return

    cuenta = buscar_cuenta(int(id_cuenta))

    if not cuenta:
        print("Cuenta no existe")
        return

    monto = input("Monto a depositar: ")

    if not monto_valido(monto):
        print("Monto inválido")
        return

    cuenta["saldo"] += int(monto)
    print("Depósito exitoso")


# -------- RETIRAR --------

def retirar():
    mostrar_cuentas()
    id_cuenta = input("ID cuenta: ")

    if not numero_valido(id_cuenta):
        print("ID inválido")
        return

    cuenta = buscar_cuenta(int(id_cuenta))

    if not cuenta:
        print("Cuenta no existe")
        return

    monto = input("Monto a retirar: ")

    if not monto_valido(monto):
        print("Monto inválido")
        return

    monto = int(monto)

    if cuenta["saldo"] < monto:
        print("Fondos insuficientes")
        return

    cuenta["saldo"] -= monto
    print("Retiro exitoso")


# -------- TRANSFERENCIA --------

def transferir():
    print("\n--- Cuenta ORIGEN ---")
    mostrar_cuentas()
    origen_id = input("ID cuenta origen: ")

    if not numero_valido(origen_id):
        return

    origen = buscar_cuenta(int(origen_id))
    if not origen:
        print("Cuenta origen no existe")
        return

    print("\n--- Cuenta DESTINO ---")
    destino_id = input("ID cuenta destino: ")

    if not numero_valido(destino_id):
        return

    destino = buscar_cuenta(int(destino_id))
    if not destino:
        print("Cuenta destino no existe")
        return

    monto = input("Monto a transferir: ")

    if not monto_valido(monto):
        print("Monto inválido")
        return

    monto = int(monto)

    if origen["saldo"] < monto:
        print("Fondos insuficientes")
        return

    # transferencia
    origen["saldo"] -= monto
    destino["saldo"] += monto

    print("Transferencia realizada")


# -------- MENU --------

def menu():
    opcion = ""

    while opcion != "5":
        print("\n=== BANCO ===")
        print("1. Crear cuenta")
        print("2. Ver cuentas")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Transferir")
        print("6. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            crear_cuenta()

        elif opcion == "2":
            mostrar_cuentas()

        elif opcion == "3":
            depositar()

        elif opcion == "4":
            retirar()

        elif opcion == "5":
            transferir()

        elif opcion == "6":
            print("Saliendo...")


menu()