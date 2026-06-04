# TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
# PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

import re

# ==================== FUNCIONES DE INICIO DE SESION ====================

def inicio():
    """Este es el menu inicial del programa, el usuario decide entre iniciar sesion o crear usuario."""
    continuar = True

    while continuar:
        print(
            "=== Bienvenido al programa ===" \
            "\n1. Iniciar sesión" \
            "\n2. Crear usuario" \
            "\n3. Cerrar el programa"
        )
        n = input("\nElige una opción: ")

        if n == "1":
            iniciar_sesion(usuarios, stock, ventas, transacciones)

        elif n == "2":
            registrar_usuario(usuarios)
            iniciar_sesion(usuarios, stock, ventas, transacciones)

        elif n == "3":
            print("\nCerrando el programa")
            continuar = False

        else:
            print("Dato invalido. Intente de nuevo")

# ==================== FUNCIONES DE USUARIOS ====================

def iniciar_sesion(usuarios, stock, ventas, transacciones):
    """Permite iniciar sesion con usuario y contraseña para ingresar al apartado principal"""

    isUser = False

    print("\n=== Iniciar Sesion ===")

    while isUser == False:

        nombre = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese contraseña: ")

        for usuario in usuarios:
            if usuario["nombre"] == nombre and usuario["clave"] == clave:
                isUser = True
        if not isUser:
            print("\nEl usuario ingresado es incorrecto. Intente nuevamente\n")

    menu_principal(stock, ventas, usuarios, transacciones)

def imprimir_usuarios(usuarios):
    """Imprime la lista de usuarios registrados con su ID, nombre, email y rol."""

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\n=== Usuarios registrados ===")
    print(f"{'ID':<5} {'Nombre':<10} {'Email':<20}{'Rol':<10}")
    print("-" * 66)

    lista = list(map(lambda x: f"{x['id']:<5} {x['nombre']:<10} {x['email']:<20} {x['rol']:<10}", usuarios))

    for elemento in lista:
        print(elemento)

def registrar_usuario(usuarios):
    """Registra un nuevo usuario con un ID distinto a los existentes, nombre, email, clave y rol."""

    print("\nRegistro de nuevo usuario")

    nombre = input("Nombre del usuario: ")
    email = input("Email del usuario: ")
    clave = input("Contraseña del usuario: ")

    if re.match(r"^[\w\.]+@[\w\.]+\.[a-z]{2,}$", email):
        if email in emails_registrados:
            print("Ya existe un usuario registrado con ese email.")
            return
    else:
        print("El email no es valido")
        return

    clave_existente = list(filter(lambda usuario: usuario["clave"] == clave, usuarios))
    if clave_existente:
        print("La contraseña es inválida.")
        return

    id_usuario = len(usuarios) + 1
    usuarios.append({
        "id": id_usuario,
        "nombre": nombre,
        "email": email,
        "clave": clave
    })
    emails_registrados.add(email)
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

    lista = list(map(lambda x: f"{x['nombre']:<20} {x['cantidad']:>10} {x['precio']:>10.2f}", stock))

    for elemento in lista:
        print(elemento)

def agregar_stock(stock, transacciones):
    """Agrega un producto a la lista o solo actualiza la cantidad de stock si ya existe.
    Si el producto es nuevo, registra automaticamente un egreso por el costo total."""

    print("\n=== Agregar stock a un producto ===\n")

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    for item in stock:
        if item["nombre"] == producto:
            item["cantidad"] += cantidad
            print(f"Se ha aumentado el stock de '{producto}'. La cantidad actual es de: {item['cantidad']}")
            return

    desc = input("Descripcion del producto: ")
    precio = float(input("Precio unitario: $"))
    categoria = input("Categoria del producto: ")

    stock.append({
        "nombre": producto,
        "descripcion": desc,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
        "oferta": False
    })

    monto_egreso = precio * cantidad
    fecha_egreso = input("Fecha de la compra (dd/mm/aaaa): ")
    id_transaccion = len(transacciones) + 1
    transacciones.append({
        "id": id_transaccion,
        "tipo": "egreso",
        "monto": monto_egreso,
        "descripcion": f"Compra de {cantidad}x {producto}",
        "fecha": fecha_egreso
    })

    print(f"'{producto}' ha sido agregado a la lista de productos. La cantidad actual es de: {cantidad}")
    print(f"  Egreso registrado : ${monto_egreso:.2f}")

def eliminar_stock(stock):
    """Elimina una cantidad de stock al producto existente, y solo si hay suficiente cantidad."""

    print("\n=== Eliminar stock a un producto ===\n")

    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad a eliminar: "))

    for item in stock:
        if item["nombre"] == producto:
            if item["cantidad"] < cantidad:
                print(f"Stock insuficiente. Hay {item['cantidad']} unidades disponibles.")
                return

            item["cantidad"] -= cantidad
            print(f"{cantidad} unidades de '{producto}' fueron eliminadas. Cantidad actual: {item['cantidad']}")
            return

    print(f"'{producto}' no se encuentra en la lista de productos.")

def buscar_producto(stock):
    """Busca un producto en la lista y muestra toda su información, avisa sí no existe."""

    producto = input("\nNombre del producto a buscar: ")

    resultado = list(filter(lambda x: x["nombre"] == producto, stock))

    if resultado:
        item = resultado[0]
        print(f"\nProducto: {item['nombre']} \nDescripcion: {item['descripcion']} \nPrecio: {item['precio']} \nCantidad: {item['cantidad']} \nCategoria: {item['categoria']}")

    else:
        print(f"El producto '{producto}' no se encuentra en la lista.")

def ofertas(stock):
    """Muestra la lista de productos que estan en oferta y muestra el precio de oferta"""

    print("\n=== Juegos en oferta ===")
    print(f"{'Producto':<20} {'Stock':>10} {'Precio':>10} {'Oferta':>10}")
    print("-" * 55)

    hay_ofertas = False

    for item in stock:
        if item["oferta"] == True:
            hay_ofertas = True
            precio_original = item["precio"]
            precio_oferta = precio_original * 0.8  # 20% de descuento

            print(f"{item['nombre']:<20} {item['cantidad']:>10} {precio_original:>10.2f} {precio_oferta:>10.2f}")

    if not hay_ofertas:
        print("No hay juegos en oferta")

# ==================== FUNCIONES DE VENTAS ====================

def registrar_venta(stock, ventas, transacciones):
    """Registra una nueva venta. Pide el producto y la cantidad, verifica stock
    y aplica descuento si está en oferta. Guarda la venta en la lista
    y registra automáticamente la transacción de ingreso correspondiente."""

    print("\n=== Registrar nueva venta ===\n")

    lista_productos(stock)

    producto = input("\nNombre del producto a vender: ")

    resultado = list(filter(lambda x: x["nombre"] == producto, stock))

    if not resultado:
        print(f"El producto '{producto}' no se encuentra en el stock.")
        return

    item = resultado[0]

    if item["cantidad"] == 0:
        print(f"No hay unidades disponibles de '{producto}'.")
        return

    cantidad = int(input(f"Cantidad a vender (disponibles: {item['cantidad']}): "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        return

    if item["cantidad"] < cantidad:
        print(f"Stock insuficiente. Hay {item['cantidad']} unidades disponibles.")
        return

    precio_unitario = item["precio"]

    if item["oferta"] == True:
        precio_unitario = precio_unitario * 0.8
        print(f"(Precio con descuento de oferta aplicado)")

    total = precio_unitario * cantidad

    item["cantidad"] -= cantidad

    id_venta = len(ventas) + 1
    ventas.append({
        "id": id_venta,
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    })

    fecha_venta = input("Fecha de la venta (dd/mm/aaaa): ")
    id_transaccion = len(transacciones) + 1
    transacciones.append({
        "id": id_transaccion,
        "tipo": "ingreso",
        "monto": total,
        "descripcion": f"Venta de {cantidad}x {producto}",
        "fecha": fecha_venta
    })

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

    total_recaudado = sum(map(lambda x: x["total"], ventas))
    cantidad_ventas = len(ventas)

    productos = []
    cantidades = []

    for v in ventas:
        encontrado = False
        i = 0
        while i < len(productos) and not encontrado:
            if productos[i] == v["producto"]:
                cantidades[i] += v["cantidad"]
                encontrado = True
            i += 1
        if not encontrado:
            productos.append(v["producto"])
            cantidades.append(v["cantidad"])

    mas_vendido = None
    mayor_cantidad = 0

    for i in range(len(productos)):
        if cantidades[i] > mayor_cantidad:
            mayor_cantidad = cantidades[i]
            mas_vendido = productos[i]

    print("\n=== Resumen de ventas ===")
    print(f"  Ventas realizadas   : {cantidad_ventas}")
    print(f"  Producto más vendido: {mas_vendido} ({mayor_cantidad} unidades)")
    print(f"  Total recaudado     : ${total_recaudado:.2f}")

# ==================== FUNCIONES DE TRANSACCIONES ====================

def registrar_transaccion(transacciones):
    """Registra manualmente una transacción de ingreso o egreso con monto y descripción."""

    print("\n=== Registrar nueva transacción ===\n")

    tipo = input("Tipo de transacción (ingreso/egreso): ")

    if tipo not in ["ingreso", "egreso"]:
        print("Tipo inválido. Debe ser 'ingreso' o 'egreso'.")
        return

    descripcion = input("Descripción: ")
    monto = float(input("Monto: $"))

    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        return

    fecha = input("Fecha (dd/mm/aaaa): ")

    id_transaccion = len(transacciones) + 1
    transacciones.append({
        "id": id_transaccion,
        "tipo": tipo,
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha
    })

    print(f"\nTransacción registrada exitosamente.")
    print(f"  Tipo        : {tipo}")
    print(f"  Descripción : {descripcion}")
    print(f"  Monto       : ${monto:.2f}")
    print(f"  Fecha       : {fecha}")

def resumen_transacciones(transacciones):
    """Muestra el total de ingresos, egresos y el balance final."""

    if not transacciones:
        print("\nNo hay transacciones para mostrar en el resumen.")
        return

    ingresos = list(filter(lambda x: x["tipo"] == "ingreso", transacciones))
    egresos  = list(filter(lambda x: x["tipo"] == "egreso",  transacciones))

    total_ingresos = sum(map(lambda x: x["monto"], ingresos))
    total_egresos  = sum(map(lambda x: x["monto"], egresos))
    balance        = total_ingresos - total_egresos

    print("\n=== Resumen de transacciones ===")
    print(f"  Ingresos totales : ${total_ingresos:.2f}")
    print(f"  Egresos totales  : ${total_egresos:.2f}")
    print(f"  Balance          : ${balance:.2f}")

# ==================== MENÚS ====================

def menu_ventas(stock, ventas, transacciones):
    """Muestra el menú de gestión de ventas y transacciones."""

    continuar = True

    while continuar:
        print(
            "\n=== Menú de ventas ===" \
            "\n1. Registrar nueva venta" \
            "\n2. Ver resumen de ventas" \
            "\n3. Registrar transacción manual" \
            "\n4. Ver resumen de transacciones" \
            "\n5. Volver al menú principal"
        )

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            registrar_venta(stock, ventas, transacciones)

        elif opcion == "2":
            resumen_ventas(ventas)

        elif opcion == "3":
            registrar_transaccion(transacciones)

        elif opcion == "4":
            resumen_transacciones(transacciones)

        elif opcion == "5":
            continuar = False

        else:
            print("Opción inválida.")

def menu_stock(stock, transacciones):
    """Muestra el menú de manejo de los productos."""
    continuar = True

    while continuar:
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
            agregar_stock(stock, transacciones)

        elif opcion == "4":
            buscar_producto(stock)

        elif opcion == "5":
            ofertas(stock)

        elif opcion == "6":
            continuar = False

        else:
            print("Opción inválida.")

def menu_usuarios(usuarios):
    """Muestra el menú de manejo de usuarios."""
    continuar = True

    while continuar:
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
            continuar = False

        else:
            print("Opción inválida.")

def menu_principal(stock, ventas, usuarios, transacciones):
    """Menu principal donde el usuario decide si gestionar los productos, usuarios o ventas."""

    print("\nBienvenido al sistema de venta de videojuegos")

    continuar = True

    while continuar:
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
            menu_stock(stock, transacciones)

        elif n == "2":
            menu_usuarios(usuarios)

        elif n == "3":
            menu_ventas(stock, ventas, transacciones)

        elif n == "4":
            print("\nCerrando sesión.\n")
            continuar = False

        else:
            print("Número inválido. Ingrese una opción válida.")

# ==================== MAIN ====================

usuarios = [  # claves: id, nombre, email, clave, rol
    {"id": 1, "nombre": "ag", "email": "agu@mail", "clave": "123", "rol": "administrador"},
    {"id": 2, "nombre": "martina", "email": "martina@mail", "clave": "123", "rol": "administrador"}
]

emails_registrados = set(u["email"] for u in usuarios)

stock = [  # claves: nombre, descripcion, precio, cantidad, categoria, oferta
    {"nombre": "Hollow Knight", "descripcion": "Metroidvania tipo soulslike 2D", "precio": 4.99, "cantidad": 8, "categoria": "metroidvania", "oferta": True},
    {"nombre": "CupHead", "descripcion": "Plataformero de acción clasico 2D", "precio": 19.99, "cantidad": 10, "categoria": "plataformas", "oferta": True}
]

ventas = []           # claves: id, producto, cantidad, precio_unitario, total
transacciones = []    # claves: id, tipo, monto, descripcion, fecha

inicio()
