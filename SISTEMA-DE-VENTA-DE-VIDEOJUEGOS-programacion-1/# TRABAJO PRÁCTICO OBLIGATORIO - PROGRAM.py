# TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
# PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

# ==================== FUNCIONES DE USUARIOS ====================

def iniciar_sesion(usuarios):
    isUser = False

    print = ("Iniciar Sesion")

    while isUser == False:
        nombre = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese contraseña: ")

        for usuario in usuarios:
            if usuario[1] == nombre and usuario[3] == clave:
                isUser = True
            else:
                print("\nEl usuario ingresado es incorrecto. Intente nuevamente\n")

def imprimir_usuarios(usuarios):
    """Imprime la lista de usuarios registrados con su ID, nombre, email y rol."""

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\n=== Usuarios registrados ===")
    print(f"{'ID':<5} {'Nombre':<10} {'Email':<20}{'Rol':<10}")
    print("-" * 66)

    lista = list(map(lambda x: f"{x[0]:<5} {x[1]:<10} {x[2]:<20} {x[4]:<10}", usuarios))
    print("\n".join(lista))

def buscar_usuario(usuarios):
    """Busca un usuario por email y retorna sus datos si existe."""

    email = input("Ingrese el email del usuario a buscar: ")

    for u in usuarios:
        if u[2] == email:
            print(f"\nID: {u[0]}, Nombre: {u[1]}, Email: {u[2]}, Rol: {u[4]}")
            return

    print("No se encontró un usuario con ese email.")

def registrar_usuario(usuarios):
    """Registra un nuevo usuario con un ID distinto a los existentes, nombre, email y rol."""

    print("\nRegistro de nuevo usuario")

    nombre = input("Nombre del usuario: ")
    email = input("Email del usuario: ")
    clave = input("Contraseña del usuario: ")
    rol = input("Rol del usuario (cliente/administrador): ")

    email_existente = list(filter(lambda usuario: usuario[2] == email, usuarios))
    if email_existente:
        print("Ya existe un usuario registrado con ese email.")
        return

    clave_existente = list(filter(lambda usuario: usuario[3] == clave, usuarios))
    if clave_existente:
        print("Contraseña inválida.")
        return

    id_usuario = len(usuarios) + 1
    usuarios.append([id_usuario, nombre, email, clave, rol])
    print(f"Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.")

# ==================== FUNCIONES DE MANEJO DE STOCK ====================

def lista_productos(stock):
    """Imprime el stock actual de productos."""

    if not stock:
        print("\nEl stock está vacío.")
        return

    print("\n=== Stock actual ===")
    print(f"{'Producto':<20} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 42)

    lista = list(map(lambda x: f"{x[0]:<20} {x[3]:>10} {x[2]:>10.2f}", stock))
    print("\n".join(lista))

def agregar_stock(stock):
    """Agrega un producto al stock o actualiza la cantidad si ya existe."""

    print("\n=== Agregar stock a un producto ===\n")

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    for item in stock:
        if item[0] == producto:
            item[3] += cantidad
            print(f"Se ha aumentado el stock de '{producto}'. La cantidad actual es de: {item[3]}")
            return

    desc = input("Descripcion del producto")
    precio = float(input("Precio unitario: $"))
    categoria = input("Categoria del producto: ")

    stock.append([producto, desc, precio, cantidad, categoria, False])
    print(f"'{producto}' ha sigo agregado a la lista de productos. La cantidad actual es de: {cantidad}")

def eliminar_stock(stock):
    """Elimina una cantidad de un producto del stock si existe y hay suficiente cantidad."""

    print("\n=== Eliminar stock a un producto ===\n")

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad a eliminar: "))

    for item in stock:
        if item[0] == producto:
            if item[3] < cantidad:
                print(f"Stock insuficiente. Hay {item[3]} unidades disponibles.")
                return

            item[3] -= cantidad
            print(f"{cantidad} unidades de '{producto}' fueron eliminadas. Cantidad actual: {item[3]}")
            return

    print(f"'{producto}' no se encuentra en la lista de productos.")

def buscar_producto(stock):
    """Busca un producto en la lista y muestra toda su información si, avisa sí no este."""

    producto = input("\nNombre del producto a buscar: ")

    resultado = list(filter(lambda x: x[0] == producto, stock))

    if resultado:
        item = resultado[0]
        print(f"\nProducto: {item[0]} \nDescripcion: {item[1]} \nPrecio: {item[2]} \nCantidad: {item[3]} \nCategoria: {item[4]}")

    else:
        print(f"El producto '{producto}' no se encuentra en la lista.")

# ==================== MENÚS ====================

def menu_stock(stock):
    """Muestra el menú de manejo de stock."""

    while True:
        print(
            "\n=== Menú de manejo de stock ===" \
            "\n1. Ver la lista de productos completa" \
            "\n2. Eliminar unidades" \
            "\n3. Agregar producto" \
            "\n4. Buscar producto" \
            "\n5. Volver al menú principal"
        )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            lista_productos(stock)

        elif opcion == "2":
            agregar_stock(stock)

        elif opcion == "3":
            eliminar_stock(stock)

        elif opcion == "4":
            buscar_producto(stock)

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")

def menu_usuarios(usuarios):
    """Muestra el menú de manejo de usuarios."""

    while True:
        print(
            "\n=== Menú de usuarios ===" \
            "\n1. Ver usuarios registrados" \
            "\n2. Buscar usuario por email" \
            "\n3. Registrar nuevo usuario" \
            "\n4. Volver al menú principal"
            )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            imprimir_usuarios(usuarios)

        elif opcion == "2":
            buscar_usuario(usuarios)

        elif opcion == "3":
            registrar_usuario(usuarios)

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")

def menu_principal():
    iniciar_sesion(usuarios)
    print("\nBienvenido al sistema de venta de videojuegos")

    while True:
        print(
            "\n=============================" \
            "\nSISTEMA DE GESTIÓN - GRUPO 4" \
            "\n=============================" \
            ""
            "\n1. Gestion de Stock" \
            "\n2. Gestion de Usuarios" \
            "\n3. Salir"
        )

        n = input("\nIngrese una de las opciones: ")

        if n == "1":
            menu_stock(stock)

        elif n == "2":
            menu_usuarios(usuarios)

        elif n == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Número inválido. Ingrese una opción válida.")

#Función para registrar ventas
def registrar_ventas(cantidad):
    juegos = []
    precios = []
    
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del videojuego: ")
        valor = int(input("Ingrese el precio del juego: "))
        
        juegos.append(nombre)
        precios.append(valor)
        
    return juegos, precios

#Función para calcular suma total
def calcular_total(lista_precios):
    total = 0  #0 para sumar
    
    for precio in lista_precios:
        total = total + precio
        
    return total

#Programa principal
suma = int(input("¿Cuántas ventas vas a registrar?: "))
lista_juegos, lista_precios = registrar_ventas(suma)
ingreso = calcular_total(lista_precios)

print("\n--- RESUMEN DE VENTAS ---")
print("Videojuegos vendidos:", lista_juegos)
print("Precios registrados:", lista_precios)
print("Total recaudado: $", ingreso)

#==================== MAIN ====================
usuarios = [ #ID - usuario - email - contraseña - rol
    [1, "ag", "agu@mail", "123", "administrador"]
]

stock = [ #nombre - descripcion - precio - stock - categoria - oferta
    ["Hollow Knight", "Metroidvania tipo soulslike 2D", 4.99, 8, "metroidvania", False],
    ["CupHead", "Plataformero de acción clasico 2D", 19.99, 10, "plataformas", True]
]

menu_principal()