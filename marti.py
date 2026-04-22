# TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
# PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

import re

# ==================== FUNCIONES DE INICIO DE SESION ====================

def inicio():
    """Este es el menu inicial del programa, el usuario decide entre iniciar sesion o crear usuario."""

    while True:
        print(
            "=== Bienvenido al programa ==="
            "\n1. Iniciar sesión" \
            "\n2. Crear usuario" \
            "\n3. Cerrar el programa"
            )
        n = input("\nElige una opción: ")

        if n == "1":
            iniciar_sesion(usuarios)
        
        elif n == "2":
            registrar_usuario(usuarios)
            iniciar_sesion(usuarios)
        
        elif n == "3":
            print("\nCerrando el programa")
            break
        
        else:
            print("Dato invalido. Intente de nuevo")

# ==================== FUNCIONES DE USUARIOS ====================

def iniciar_sesion(usuarios):
    """Permite iniciar sesion con usuario y contraseña para ingresar al apartado principal"""
    
    isUser = False

    print("\n=== Iniciar Sesion ===")

    while isUser == False:
        
        nombre = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese contraseña: ")

        for usuario in usuarios:
            if usuario[1] == nombre and usuario[3] == clave:
                isUser = True
                break
        if not isUser:
            print("\nEl usuario ingresado es incorrecto. Intente nuevamente\n")
    
    menu_principal()

def imprimir_usuarios(usuarios):
    """Imprime la lista de usuarios registrados con su ID, nombre, email y rol."""

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return
    
    print("\n=== Usuarios registrados ===")
    print(f"{'ID':<5} {'Nombre':<10} {'Email':<20}{'Rol':<10}")
    print("-" * 66)

    lista = list(map(lambda x: f"{x[0]:<5} {x[1]:<10} {x[2]:<20} {x[4]:<10}", usuarios))
    
    for elemento in lista:
        print(elemento)

def registrar_usuario(usuarios):
    """Registra un nuevo usuario con un ID distinto a los existentes, nombre, email, clave y rol."""

    print("\nRegistro de nuevo usuario")

    nombre = input("Nombre del usuario: ")
    email = input("Email del usuario: ")
    clave = input("Contraseña del usuario: ")
    rol = input("Rol del usuario (cliente/administrador): ")

    if re.match(r"^[\w\.]+@[\w\.]+\.[a-z{2,}$]", email):
        email_existente = list(filter(lambda usuario: usuario[2] == email, usuarios))
    
        if email_existente:
            print("Ya existe un usuario registrado con ese email.")
            return
    else:
        print("El email no es valido")
        return
    
    clave_existente = list(filter(lambda usuario: usuario[3] == clave, usuarios))
    if clave_existente:
        print("La contraseña es inválida.")
        return
        
    id_usuario = len(usuarios) + 1
    usuarios.append([id_usuario, nombre, email, clave, rol])
    print(f"Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.\n")

# ==================== FUNCIONES DE MANEJO DE STOCK ====================

def lista_productos(stock):
    """Imprime la lista actual de productos."""

    if not stock:
        print("\nEl stock está vacío.")
        return
    
    print("\n=== Stock actual ===")
    print(f"{'Producto':<20} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 42)

    lista = list(map(lambda x: f"{x[0]:<20} {x[3]:>10} {x[2]:>10.2f}", stock))
    
    for elemento in lista:
        print(elemento)

def agregar_stock(stock):
    """Agrega un producto a la lista o solo actualiza la cantidad de stock si ya existe."""

    print("\n=== Agregar stock a un producto ===\n")

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    for item in stock:
        if item[0] == producto:
            item[3] += cantidad
            print(f"Se ha aumentado el stock de '{producto}'. La cantidad actual es de: {item[3]}")
            return
    
    desc = input("Descripcion del producto: ")
    precio = float(input("Precio unitario: $"))
    categoria = input("Categoria del producto: ")

    stock.append([producto, desc, precio, cantidad, categoria, False])
    print(f"'{producto}' ha sigo agregado a la lista de productos. La cantidad actual es de: {cantidad}")

def eliminar_stock(stock):
    """Elimina una cantidad de stock al producto existente, y solo si hay suficiente cantidad."""
    
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
    """Busca un producto en la lista y muestra toda su información, avisa sí no existe."""
    
    producto = input("\nNombre del producto a buscar: ")

    resultado = list(filter(lambda x: x[0] == producto, stock))

    if resultado:
        item = resultado[0]
        print(f"\nProducto: {item[0]} \nDescripcion: {item[1]} \nPrecio: {item[2]} \nCantidad: {item[3]} \nCategoria: {item[4]}")

    else:
        print(f"El producto '{producto}' no se encuentra en la lista.")
    
def ofertas(stock):
    """Muestra la lista de productos que estan en oferta y muestra el precio de oferta"""

    print("\n=== Juegos en oferta ===")
    print(f"{'Producto':<20} {'Stock':>10} {'Precio':>10} {'Oferta':>10}")
    print("-" * 55)

    hay_ofertas = False

    for item in stock:
        if item[5] == True:
            hay_ofertas = True
            precio_original = item[2]
            precio_oferta = precio_original * 0.8 #20% de descuento

            print(f"{item[0]:<20} {item[3]:>10} {precio_original:>10.2f} {precio_oferta:>10.2f}")
    
    if not hay_ofertas:
        print("No hay juegos en oferta")

# ==================== FUNCIONES DE VENTAS ====================

def registrar_venta(stock, ventas):
    """Registra una nueva venta. Pide el producto y la cantidad, verifica stock
    y aplica descuento si está en oferta. Guarda la venta en la lista."""

    print("\n=== Registrar nueva venta ===\n")

    lista_productos(stock)

    producto = input("\nNombre del producto a vender: ")
    
    resultado = list(filter(lambda x: x[0] == producto, stock))

    if not resultado:
        print(f"El producto '{producto}' no se encuentra en el stock.")
        return

    item = resultado[0]

    if item[3] == 0:
        print(f"No hay unidades disponibles de '{producto}'.")
        return

    cantidad = int(input(f"Cantidad a vender (disponibles: {item[3]}): "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        return

    if item[3] < cantidad:
        print(f"Stock insuficiente. Hay {item[3]} unidades disponibles.")
        return

    precio_unitario = item[2]
    if item[5] == True:
        precio_unitario = precio_unitario * 0.8
        print(f"(Precio con descuento de oferta aplicado)")

    total = precio_unitario * cantidad

    item[3] -= cantidad

    id_venta = len(ventas) + 1
    ventas.append([id_venta, producto, cantidad, precio_unitario, total])

    print(f"\nVenta registrada exitosamente.")
    print(f"  Producto : {producto}")
    print(f"  Cantidad : {cantidad}")
    print(f"  Precio   : ${precio_unitario:.2f} por unidad")
    print(f"  Total    : ${total:.2f}")

def resumen_ventas(ventas):
    """Muestra un resumen general: cantidad de ventas, producto más vendido y total recaudado."""

    if not ventas:
        print("\nNo hay ventas para mostrar en el resumen.")
        return

    total_recaudado = sum(map(lambda x: x[4], ventas))
    cantidad_ventas = len(ventas)

    productos = []
    cantidades = []

    for v in ventas:
        encontrado = False
        for i in range(len(productos)):
            if productos[i] == v[1]:
                cantidades[i] += v[2]
                encontrado = True
                break
        if not encontrado:
            productos.append(v[1])
            cantidades.append(v[2])

    mas_vendido = None
    mayor_cantidad = 0

    for i in range(len(productos)):
        if cantidades[i] > mayor_cantidad:
            mayor_cantidad = cantidades[i]
            mas_vendido = productos[i]

    print("\n=== Resumen de ventas ===")
    print(f"  Ventas realizadas  : {cantidad_ventas}")
    print(f"  Producto más vendido: {mas_vendido} ({mayor_cantidad} unidades)")
    print(f"  Total recaudado    : ${total_recaudado:.2f}")

# ==================== MENÚS ====================

def menu_ventas(stock, ventas):
    """Muestra el menú de gestión de ventas."""

    while True:
        print(
            "\n=== Menú de ventas ===" \
            "\n1. Registrar nueva venta" \
            "\n2. Ver resumen de ventas" \
            "\n3. Volver al menú principal"
        )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            registrar_venta(stock, ventas)

        elif opcion == "2":
            resumen_ventas(ventas)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")

def menu_stock(stock):
    """Muestra el menú de manejo de los productos."""

    while True:
        print(
            "\n=== Menú de manejo de stock ===" \
            "\n1. Ver la lista de productos completa" \
            "\n2. Eliminar unidades" \
            "\n3. Agregar producto" \
            "\n4. Buscar producto" \
            "\n5. Ver juegos en oferta" \
            "\n6. Volver al menú principal"
        )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            lista_productos(stock)

        elif opcion == "2":
            eliminar_stock(stock)

        elif opcion == "3":
            agregar_stock(stock)

        elif opcion == "4":
            buscar_producto(stock)

        elif opcion == "5":
            ofertas(stock)

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")

def menu_usuarios(usuarios):
    """Muestra el menú de manejo de usuarios."""

    while True:
        print(
            "\n=== Menú de usuarios ===" \
            "\n1. Ver usuarios registrados" \
            "\n2. Registar nuevo usuario" \
            "\n3. Volver al menú principal"
            )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            imprimir_usuarios(usuarios)

        elif opcion == "2":
            registrar_usuario(usuarios)

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")

def menu_principal():
    """Menu principal donde el usuario decide si gestionar los productos, usuarios o ventas."""

    print("\nBienvenido al sistema de venta de videojuegos")

    while True:
        print(
            "\n=============================" \
            "\nSISTEMA DE GESTIÓN - GRUPO 4" \
            "\n=============================" \
            "\n1. Gestion de Productos" \
            "\n2. Gestion de Usuarios" \
            "\n3. Gestion de Ventas" \
            "\n4. Cerrar sesión"
        )

        n = input("\nIngrese una de las opciones: ")

        if n == "1":
            menu_stock(stock)

        elif n == "2":
            menu_usuarios(usuarios)

        elif n == "3":
            menu_ventas(stock, ventas)

        elif n == "4":
            print("\nCerrando sesión.\n")
            break

        else:
            print("Número inválido. Ingrese una opción válida.")

#==================== MAIN ====================

usuarios = [ #ID - usuario - email - contraseña - rol
    [1, "ag", "agu@mail", "123", "administrador"]
]

stock = [ #nombre - descripcion - precio - stock - categoria - oferta
    ["Hollow Knight", "Metroidvania tipo soulslike 2D", 4.99, 8, "metroidvania", True],
    ["CupHead", "Plataformero de acción clasico 2D", 19.99, 10, "plataformas", True]
]

ventas = [] #ID - producto - cantidad - precio_unitario - total

inicio()