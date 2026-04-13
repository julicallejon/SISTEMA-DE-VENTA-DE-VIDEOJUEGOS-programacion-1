# TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
# PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN


# ==================== FUNCIONES DE MANEJO DE STOCK ====================

def agregar_a_stock(stock, producto, cantidad, precio):
    """Agrega un producto al stock o actualiza la cantidad si ya existe."""
    for item in stock:
        if item[0] == producto:
            item[1] += cantidad
            print(producto, "agregado al stock. Cantidad actual:", item[1])
            return
    stock.append([producto, cantidad, precio])
    print(producto, "agregado al stock. Cantidad actual:", cantidad)

def eliminar_de_stock(stock, producto, cantidad):
    """Elimina una cantidad de un producto del stock si existe y hay suficiente cantidad."""
    for item in stock:
        if item[0] == producto:
            if item[1] < cantidad:
                print("Stock insuficiente. Hay", item[1], "unidades disponibles.")
                return False
            item[1] -= cantidad
            print(cantidad, "unidades de", producto, "fueron eliminadas. Cantidad actual:", item[1])
            return True
    print("El producto", producto, "no se encuentra en stock.")
    return False

def imprimir_stock(stock):
    """Imprime el stock actual de productos."""
    if not stock:
        print("El stock está vacío.")
        return
    print("\n=== Stock actual ===")
    print(f"{'Producto':<20} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 42)
    for item in stock:
        print(f"{item[0]:<20} {item[1]:>10} {item[2]:>10.2f}")

def buscar_en_stock(stock, producto):
    """Busca un producto en el stock y muestra su información si se encuentra."""
    for item in stock:
        if item[0] == producto:
            print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio: {item[2]:.2f}")
            return item
    print("El producto", producto, "no se encuentra en stock.")
    return None

def obtener_precio_producto(stock, producto):
    """Obtiene el precio de un producto en el stock."""
    for item in stock:
        if item[0] == producto:
            return item[2]
    print("El producto", producto, "no se encuentra en stock.")
    return None


# ==================== FUNCIONES DE USUARIOS ====================

def registrar_usuario(usuarios, nombre, email, rol="cliente"):
    """Registra un nuevo usuario con un ID distinto a los existentes, nombre, email y rol."""
    for u in usuarios:
        if u[2] == email:
            print("Ya existe un usuario registrado con ese email.")
            return
    id_usuario = len(usuarios) + 1
    usuarios.append([id_usuario, nombre, email, rol])
    print(f"Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.")

def imprimir_usuarios(usuarios):
    """Imprime la lista de usuarios registrados con su ID, nombre, email y rol."""
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\n=== Usuarios registrados ===")
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<30} {'Rol':<10}")
    print("-" * 66)
    for u in usuarios:
        print(f"{u[0]:>5} {u[1]:<20} {u[2]:<30} {u[3]:<10}")

def buscar_usuario(usuarios, email):
    """Busca un usuario por email y retorna sus datos si existe."""
    for u in usuarios:
        if u[2] == email:
            return u
    print("No se encontró un usuario con ese email.")
    return None

#def eliminar_usuario(usuarios, email): estaria bueno gregar esta funcion


# ==================== MENÚS ====================

def menu_stock(stock):
    """Muestra el menú de manejo de stock."""
    while True:
        # FIX: el bloque print estaba fuera del while por indentación incorrecta
        print("\n=== Menú de manejo de stock ===")
        print("1. Agregar producto")
        print("2. Eliminar unidades")
        print("3. Ver el stock completo")
        print("4. Buscar producto")
        print("5. Volver al menú principal")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: $"))
            agregar_a_stock(stock, producto, cantidad, precio)
        elif opcion == "2":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a eliminar: "))
            eliminar_de_stock(stock, producto, cantidad)
        elif opcion == "3":
            imprimir_stock(stock)
        elif opcion == "4":
            producto = input("Nombre del producto: ")
            buscar_en_stock(stock, producto)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_usuarios(usuarios):
    """Muestra el menú de manejo de usuarios."""
    while True:
        print("\n=== Menú de usuarios ===")
        print("1. Registrar nuevo usuario")
        print("2. Buscar usuario por email")
        print("3. Ver usuarios registrados")  
        print("4. Volver al menú principal")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            email = input("Email del usuario: ")
            rol = input("Rol del usuario (cliente/administrador): ")
            registrar_usuario(usuarios, nombre, email, rol)
        elif opcion == "2":
            email = input("Ingrese el email del usuario a buscar: ")
            u = buscar_usuario(usuarios, email)
            if u:
                print(f"ID: {u[0]}, Nombre: {u[1]}, Email: {u[2]}, Rol: {u[3]}")
        elif opcion == "3":
            imprimir_usuarios(usuarios)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


# ==================== MAIN ====================

stock = []
usuarios = []

while True:
    print("\n=============================")
    print("  SISTEMA DE GESTIÓN - GRUPO 4")
    print("=============================")
    print("1. Gestion de Stock")
    print("2. Gestion de Usuarios")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        menu_stock(stock)
    elif opcion == "2":
        menu_usuarios(usuarios)
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Número inválido. Ingrese una opción válida.")