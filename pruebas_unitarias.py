# TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
# PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

import re
import json

ARCHIVO_DATOS = "datos_tienda.json"

# ==================== FUNCIONES DE ARCHIVOS ====================

def datos_iniciales():
    """Devuelve los datos iniciales del sistema si no existe el archivo."""
    usuarios_iniciales = [
        {"id": 1, "nombre": "ag", "email": "agu@mail.com", "clave": "123", "rol": "administrador"},
        {"id": 2, "nombre": "martina", "email": "martina@mail.com", "clave": "123", "rol": "administrador"}
    ]

    stock_inicial = [
        {"nombre": "Hollow Knight", "descripcion": "Metroidvania tipo soulslike 2D", "precio": 4.99, "cantidad": 8, "categoria": "metroidvania", "oferta": True},
        {"nombre": "CupHead", "descripcion": "Plataformero de accion clasico 2D", "precio": 19.99, "cantidad": 10, "categoria": "plataformas", "oferta": True}
    ]

    ventas_iniciales = []
    transacciones_iniciales = []

    return usuarios_iniciales, stock_inicial, ventas_iniciales, transacciones_iniciales


def cargar_datos():
    """Carga usuarios, stock, ventas y transacciones desde un archivo JSON."""
    try:
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()

        usuarios_cargados = datos.get("usuarios", [])
        stock_cargado = datos.get("stock", [])
        ventas_cargadas = datos.get("ventas", [])
        transacciones_cargadas = datos.get("transacciones", [])

        emails = [u["email"] for u in usuarios_cargados]
        emails_set = set(emails)
        if len(emails) != len(emails_set):
            print("Advertencia: hay emails duplicados en el archivo de datos.")
        

        print("\nDatos cargados correctamente desde el archivo.")
        return usuarios_cargados, stock_cargado, ventas_cargadas, transacciones_cargadas

    except FileNotFoundError:
        print("\nNo se encontro el archivo de datos. Se inicia el sistema con datos iniciales.")
        return datos_iniciales()


def guardar_datos(usuarios, stock, ventas, transacciones):
    """Guarda usuarios, stock, ventas y transacciones en un archivo JSON."""
    datos = {
        "usuarios": usuarios,
        "stock": stock,
        "ventas": ventas,
        "transacciones": transacciones
    }
    
    try:
        archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        archivo.close()
        return True

    except FileNotFoundError:
            print("\nNo se encontro el archivo de datos. Se inicia el sistema con datos iniciales.")
            return datos_iniciales()


# ==================== FUNCIONES DE VALIDACION Y EXCEPCIONES ====================

def pedir_entero(mensaje):
    """Pide un numero entero y controla el ValueError si el usuario ingresa texto."""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def pedir_float(mensaje):
    """Pide un numero decimal y controla el ValueError si el usuario ingresa texto."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un numero valido. Use punto para decimales.")


def generar_id(lista):
    """Genera un ID nuevo tomando como base el largo de la lista."""
    return len(lista) + 1


# ==================== FUNCIONES DE INICIO DE SESION ====================

def inicio():
    """Este es el menu inicial del programa, el usuario decide entre iniciar sesion o crear usuario."""
    continuar = True

    while continuar:
        print(
            "\n=== Bienvenido al programa ===" \
            "\n1. Iniciar sesion" \
            "\n2. Crear usuario" \
            "\n3. Cerrar el programa"
        )
        n = input("\nElige una opcion: ")

        if n == "1":
            iniciar_sesion(usuarios, stock, ventas, transacciones)

        elif n == "2":
            registrado = registrar_usuario(usuarios)
            if registrado:
                iniciar_sesion(usuarios, stock, ventas, transacciones)

        elif n == "3":
            guardar_datos(usuarios, stock, ventas, transacciones)
            print("\nCerrando el programa")
            continuar = False

        else:
            print("Dato invalido. Intente de nuevo")


# ==================== FUNCIONES DE USUARIOS ====================

def iniciar_sesion(usuarios, stock, ventas, transacciones):
    """Permite iniciar sesion con usuario y contraseña para ingresar al apartado principal."""

    isUser = False
    sesion_activa = None

    print("\n=== Iniciar Sesion ===")

    while not isUser:
        nombre = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese contraseña: ")

        for usuario in usuarios:
            try:
                if usuario["nombre"] == nombre and usuario["clave"] == clave:
                    isUser = True
                    sesion_activa = (usuario["nombre"], usuario["rol"])
            except KeyError:
                print("Error: hay un usuario cargado con datos incompletos.")

        if not isUser:
            print("\nEl usuario ingresado es incorrecto. Intente nuevamente\n")
            opcion_valida = False
            while not opcion_valida:
                reintentar = input("¿Desea intentar iniciar sesion nuevamente? (s/n): ")
                if reintentar == "s" or reintentar == "S":
                    opcion_valida = True
                elif reintentar == "n" or reintentar == "N":
                    opcion_valida = True
                    print("Volviendo al menu principal.")
                    return
                elif reintentar == "":
                    print("Error: no puede dejar el campo vacio.")
                else:
                    print("Opcion invalida. Ingrese s o n.")

    print(f"\nBienvenido {sesion_activa[0]}! Tu rol es: {sesion_activa[1]}")
    menu_principal(stock, ventas, usuarios, transacciones, sesion_activa)
    


def imprimir_usuarios(usuarios):
    """Imprime la lista de usuarios registrados con su ID, nombre, email y rol."""

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\n=== Usuarios registrados ===")
    print(f"{'ID':<5} {'Nombre':<15} {'Email':<25}{'Rol':<15}")
    print("-" * 60)

    try:
        lista = list(map(lambda x: f"{x['id']:<5} {x['nombre']:<15} {x['email']:<25} {x.get('rol', 'cliente'):<15}", usuarios))

        for elemento in lista:
            print(elemento)

    except KeyError:
        print("Error: no se pudieron imprimir los usuarios porque falta un dato obligatorio.")


def registrar_usuario(usuarios):
    """Registra un nuevo usuario con un ID distinto a los existentes, nombre, email, clave y rol."""

    print("\nRegistro de nuevo usuario")

    nombre = input("Nombre del usuario: ").strip()
    email = input("Email del usuario: ").strip()
    clave = input("Contraseña del usuario: ").strip()

    if nombre == "" or email == "" or clave == "":
        print("Error: los datos no pueden estar vacios.")
        return False

    if re.match(r"^[\w\.]+@[\w\.]+\.[a-z]{2,}$", email):
        if email in emails_registrados:
            print("Ya existe un usuario registrado con ese email.")
            return False
    else:
        print("El email no es valido.")
        return False

    clave_existente = list(filter(lambda usuario: usuario["clave"] == clave, usuarios))
    if clave_existente:
        print("La contraseña es invalida porque ya esta siendo utilizada.")
        return False

    id_usuario = generar_id(usuarios)
    usuarios.append({
        "id": id_usuario,
        "nombre": nombre,
        "email": email,
        "clave": clave,
        "rol": "cliente"
    })

    emails_registrados.add(email)
    guardar_datos(usuarios, stock, ventas, transacciones)

    print(f"Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.\n")
    return True

def prueba_generar_id_lista_vacia():
    resultado = generar_id([])
    if resultado == 1:
        print("prueba_generar_id_lista_vacia: PRUEBA EXITOSA")
    else:
        print(f"prueba_generar_id_lista_vacia: ERROR (se esperaba 1, se obtuvo {resultado})")

def prueba_generar_id_con_elementos():
    resultado = generar_id([1, 2, 3])
    if resultado == 4:
        print("prueba_generar_id_con_elementos: PRUEBA EXITOSA")
    else:
        print(f"prueba_generar_id_con_elementos: ERROR (se esperaba 4, se obtuvo {resultado})")

def email_valido(email):
    """Verifica si un email tiene un formato valido."""
    if re.match(r"^[\w\.]+@[\w\.]+\.[a-z]{2,}$", email):
        return True
    else:
        return False

def prueba_email_valido_correcto():
    resultado = email_valido("agu@mail.com")
    if resultado == True:
        print("prueba_email_valido_correcto: PRUEBA EXITOSA")
    else:
        print("prueba_email_valido_correcto: ERROR")

def prueba_email_sin_arroba():
    resultado = email_valido("agumail.com")
    if resultado == False:
        print("prueba_email_sin_arroba: PRUEBA EXITOSA")
    else:
        print("prueba_email_sin_arroba: ERROR")

def prueba_email_vacio():
    resultado = email_valido("")
    if resultado == False:
        print("prueba_email_vacio: PRUEBA EXITOSA")
    else:
        print("prueba_email_vacio: ERROR")
# ==================== FUNCIONES DE MANEJO DE STOCK ====================

def lista_productos(stock):
    """Imprime la lista actual de productos."""

    if not stock:
        print("\nEl stock esta vacio.")
        return

    print("\n=== Stock actual ===")
    print(f"{'Producto':<20} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 42)

    try:
        lista = list(map(lambda x: f"{x['nombre']:<20} {x['cantidad']:>10} {x['precio']:>10.2f}", stock))

        for elemento in lista:
            print(elemento)

    except KeyError:
        print("Error: hay productos cargados con datos incompletos.")

    except TypeError:
        print("Error: hay precios o cantidades con tipos de datos incorrectos.")


def agregar_stock(stock, transacciones):
    """Agrega un producto a la lista o actualiza la cantidad si ya existe.
    Si el producto es nuevo, registra automaticamente un egreso por el costo total."""

    print("\n=== Agregar stock a un producto ===\n")

    producto = input("Nombre del producto: ").strip()
    cantidad = pedir_entero("Cantidad: ")

    if producto == "":
        print("Error: el nombre del producto no puede estar vacio.")
        return

    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor a cero.")
        return

    for item in stock:
        if item["nombre"].lower() == producto.lower():
            item["cantidad"] += cantidad
            guardar_datos(usuarios, stock, ventas, transacciones)
            print(f"Se ha aumentado el stock de '{item['nombre']}'. La cantidad actual es de: {item['cantidad']}")
            return

    desc = input("Descripcion del producto: ").strip()
    precio = pedir_float("Precio unitario: $")
    categoria = input("Categoria del producto: ").strip()

    if precio <= 0:
        print("Error: el precio debe ser mayor a cero.")
        return

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
    id_transaccion = generar_id(transacciones)
    transacciones.append({
        "id": id_transaccion,
        "tipo": "egreso",
        "monto": monto_egreso,
        "descripcion": f"Compra de {cantidad}x {producto}",
        "fecha": fecha_egreso
    })

    guardar_datos(usuarios, stock, ventas, transacciones)

    print(f"'{producto}' ha sido agregado a la lista de productos. La cantidad actual es de: {cantidad}")
    print(f"  Egreso registrado : ${monto_egreso:.2f}")


def eliminar_stock(stock):
    """Elimina una cantidad de stock al producto existente, y solo si hay suficiente cantidad."""

    print("\n=== Eliminar stock a un producto ===\n")

    producto = input("Nombre del producto: ").strip()
    cantidad = pedir_entero("Cantidad a eliminar: ")

    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor a cero.")
        return

    for item in stock:
        if item["nombre"].lower() == producto.lower():
            if item["cantidad"] < cantidad:
                print(f"Stock insuficiente. Hay {item['cantidad']} unidades disponibles.")
                return

            item["cantidad"] -= cantidad
            guardar_datos(usuarios, stock, ventas, transacciones)
            print(f"{cantidad} unidades de '{item['nombre']}' fueron eliminadas. Cantidad actual: {item['cantidad']}")
            return

    print(f"'{producto}' no se encuentra en la lista de productos.")


def buscar_producto(stock):
    """Busca un producto en la lista y muestra toda su informacion, avisa si no existe."""

    producto = input("\nNombre del producto a buscar: ").strip()

    resultado = list(filter(lambda x: x["nombre"].lower() == producto.lower(), stock))

    if resultado:
        item = resultado[0]
        try:
            print(f"\nProducto: {item['nombre']} \nDescripcion: {item['descripcion']} \nPrecio: {item['precio']} \nCantidad: {item['cantidad']} \nCategoria: {item['categoria']}")
        except KeyError:
            print("Error: el producto existe, pero tiene datos incompletos.")
    else:
        print(f"El producto '{producto}' no se encuentra en la lista.")


def ofertas(stock):
    """Muestra la lista de productos que estan en oferta y muestra el precio de oferta."""

    print("\n=== Juegos en oferta ===")
    print(f"{'Producto':<20} {'Stock':>10} {'Precio':>10} {'Oferta':>10}")
    print("-" * 55)

    hay_ofertas = False

    try:
        for item in stock:
            if item["oferta"] == True:
                hay_ofertas = True
                precio_original = item["precio"]
                precio_oferta = precio_original * 0.8  # 20% de descuento

                print(f"{item['nombre']:<20} {item['cantidad']:>10} {precio_original:>10.2f} {precio_oferta:>10.2f}")

        if not hay_ofertas:
            print("No hay juegos en oferta")

    except KeyError:
        print("Error: hay productos cargados con datos incompletos.")

def mostrar_categorias_y_sin_oferta(stock):
    """Muestra las categorias disponibles y los productos sin oferta de cada categoria."""

    if not stock:
        print("\nEl stock esta vacio.")
        return
    
    try:
        categorias = set()
        for item in stock:
            categorias = categorias | {item["categoria"]}
        
        todos = set(item["nombre"] for item in stock)
        en_oferta = set(item["nombre"] for item in stock if item["oferta"] == True)
        sin_oferta = todos - en_oferta

        print("\n=== Informacion de categorias y ofertas ===")
        print(f"Categorias disponibles: {categorias}")
        
        if sin_oferta:
            print(f"Productos sin oferta  : {sin_oferta}")
        else:
            print("Productos sin oferta  : No hay productos sin oferta.")

    except KeyError:
        print("Error: hay productos cargados con datos incompletos.")

    except TypeError:
        print("Error: hay productos con tipos de datos incorrectos.")

def calcular_precio_oferta(precio):
    """Calcula el precio con el 20% de descuento de oferta."""
    return precio * 0.8

def prueba_precio_oferta_normal():
    resultado = calcular_precio_oferta(100)
    if resultado == 80.0:
        print("prueba_precio_oferta_normal: PRUEBA EXITOSA")
    else:
        print(f"prueba_precio_oferta_normal: ERROR (se esperaba 80.0, se obtuvo {resultado})")

def prueba_precio_oferta_con_decimales():
    resultado = round(calcular_precio_oferta(19.99), 2)
    if resultado == 15.99:
        print("prueba_precio_oferta_con_decimales: PRUEBA EXITOSA")
    else:
        print(f"prueba_precio_oferta_con_decimales: ERROR (se esperaba 15.99, se obtuvo {resultado})")

# ==================== FUNCIONES DE VENTAS ====================

def registrar_venta(stock, ventas, transacciones):
    """Registra una nueva venta. Pide el producto y la cantidad, verifica stock
    y aplica descuento si esta en oferta. Guarda la venta en la lista
    y registra automaticamente la transaccion de ingreso correspondiente."""

    print("\n=== Registrar nueva venta ===\n")

    lista_productos(stock)

    producto = input("\nNombre del producto a vender: ").strip()

    resultado = list(filter(lambda x: x["nombre"].lower() == producto.lower(), stock))

    if not resultado:
        print(f"El producto '{producto}' no se encuentra en el stock.")
        return

    item = resultado[0]

    if item["cantidad"] == 0:
        print(f"No hay unidades disponibles de '{item['nombre']}'.")
        return

    cantidad = pedir_entero(f"Cantidad a vender (disponibles: {item['cantidad']}): ")

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
        return

    if item["cantidad"] < cantidad:
        print(f"Stock insuficiente. Hay {item['cantidad']} unidades disponibles.")
        return

    precio_unitario = item["precio"]

    if item["oferta"] == True:
        precio_unitario = precio_unitario * 0.8
        print("(Precio con descuento de oferta aplicado)")

    total = precio_unitario * cantidad

    item["cantidad"] -= cantidad

    id_venta = generar_id(ventas)
    ventas.append({
        "id": id_venta,
        "producto": item["nombre"],
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    })

    fecha_venta = input("Fecha de la venta (dd/mm/aaaa): ")
    id_transaccion = generar_id(transacciones)
    transacciones.append({
        "id": id_transaccion,
        "tipo": "ingreso",
        "monto": total,
        "descripcion": f"Venta de {cantidad}x {item['nombre']}",
        "fecha": fecha_venta
    })

    guardar_datos(usuarios, stock, ventas, transacciones)

    print(f"\nVenta registrada exitosamente.")
    print(f"  Producto : {item['nombre']}")
    print(f"  Cantidad : {cantidad}")
    print(f"  Precio   : ${precio_unitario:.2f} por unidad")
    print(f"  Total    : ${total:.2f}")


def resumen_ventas(ventas):
    """Muestra un resumen general: cantidad de ventas, producto mas vendido y total recaudado."""

    if not ventas:
        print("\nNo hay ventas para mostrar en el resumen.")
        return

    try:
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
        print(f"  Producto mas vendido: {mas_vendido} ({mayor_cantidad} unidades)")
        print(f"  Total recaudado     : ${total_recaudado:.2f}")

    except KeyError:
        print("Error: hay ventas con datos incompletos.")

def sumar_totales(ventas):
    """Suma el campo 'total' de una lista de ventas."""
    return sum(map(lambda x: x["total"], ventas))

def prueba_sumar_totales_normal():
    ventas = [{"total": 100}, {"total": 200}, {"total": 50}]
    resultado = sumar_totales(ventas)
    if resultado == 350:
        print("prueba_sumar_totales_normal: PRUEBA EXITOSA")
    else:
        print(f"prueba_sumar_totales_normal: ERROR (se esperaba 350, se obtuvo {resultado})")

def prueba_sumar_totales_lista_vacia():
    ventas = []
    resultado = sumar_totales(ventas)
    if resultado == 0:
        print("prueba_sumar_totales_lista_vacia: PRUEBA EXITOSA")
    else:
        print(f"prueba_sumar_totales_lista_vacia: ERROR (se esperaba 0, se obtuvo {resultado})")

# ==================== FUNCIONES DE TRANSACCIONES ====================

def registrar_transaccion(transacciones):
    """Registra manualmente una transaccion de ingreso o egreso con monto y descripcion."""

    print("\n=== Registrar nueva transaccion ===\n")

    tipo = input("Tipo de transaccion (ingreso/egreso): ").strip().lower()

    if tipo not in ["ingreso", "egreso"]:
        print("Tipo invalido. Debe ser 'ingreso' o 'egreso'.")
        return

    descripcion = input("Descripcion: ").strip()
    monto = pedir_float("Monto: $")

    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        return

    fecha = input("Fecha (dd/mm/aaaa): ")

    id_transaccion = generar_id(transacciones)
    transacciones.append({
        "id": id_transaccion,
        "tipo": tipo,
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha
    })

    guardar_datos(usuarios, stock, ventas, transacciones)

    print(f"\nTransaccion registrada exitosamente.")
    print(f"  Tipo        : {tipo}")
    print(f"  Descripcion : {descripcion}")
    print(f"  Monto       : ${monto:.2f}")
    print(f"  Fecha       : {fecha}")


def resumen_transacciones(transacciones):
    """Muestra el total de ingresos, egresos y el balance final."""

    if not transacciones:
        print("\nNo hay transacciones para mostrar en el resumen.")
        return

    try:
        ingresos = list(filter(lambda x: x["tipo"] == "ingreso", transacciones))
        egresos  = list(filter(lambda x: x["tipo"] == "egreso",  transacciones))

        total_ingresos = sum(map(lambda x: x["monto"], ingresos))
        total_egresos  = sum(map(lambda x: x["monto"], egresos))
        balance        = total_ingresos - total_egresos

        print("\n=== Resumen de transacciones ===")
        print(f"  Ingresos totales : ${total_ingresos:.2f}")
        print(f"  Egresos totales  : ${total_egresos:.2f}")
        print(f"  Balance          : ${balance:.2f}")

    except KeyError:
        print("Error: hay transacciones con datos incompletos.")

def balance_transacciones(transacciones):
    """Calcula el balance (ingresos - egresos) de una lista de transacciones."""
    ingresos = sum(x["monto"] for x in transacciones if x["tipo"] == "ingreso")
    egresos = sum(x["monto"] for x in transacciones if x["tipo"] == "egreso")
    return ingresos - egresos

def prueba_balance_positivo():
    transacciones = [
        {"tipo": "ingreso", "monto": 500},
        {"tipo": "egreso",  "monto": 200}
    ]
    resultado = balance_transacciones(transacciones)
    if resultado == 300:
        print("prueba_balance_positivo: PRUEBA EXITOSA")
    else:
        print(f"prueba_balance_positivo: ERROR (se esperaba 300, se obtuvo {resultado})")

def prueba_balance_negativo():
    transacciones = [
        {"tipo": "ingreso", "monto": 100},
        {"tipo": "egreso",  "monto": 400}
    ]
    resultado = balance_transacciones(transacciones)
    if resultado == -300:
        print("prueba_balance_negativo: PRUEBA EXITOSA")
    else:
        print(f"prueba_balance_negativo: ERROR (se esperaba -300, se obtuvo {resultado})")

def prueba_balance_sin_transacciones():
    resultado = balance_transacciones([])
    if resultado == 0:
        print("prueba_balance_sin_transacciones: PRUEBA EXITOSA")
    else:
        print(f"prueba_balance_sin_transacciones: ERROR (se esperaba 0, se obtuvo {resultado})")


# ==================== MENUS ====================

def menu_ventas(stock, ventas, transacciones):
    """Muestra el menu de gestion de ventas y transacciones."""

    continuar = True

    while continuar:
        print(
            "\n=== Menu de ventas ===" \
            "\n1. Registrar nueva venta" \
            "\n2. Ver resumen de ventas" \
            "\n3. Registrar transaccion manual" \
            "\n4. Ver resumen de transacciones" \
            "\n5. Volver al menu principal"
        )

        opcion = input("\nIngrese una opcion: ")

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
            print("Opcion invalida.")


def menu_stock(stock, transacciones):
    """Muestra el menu de manejo de los productos."""
    continuar = True

    while continuar:
        print(
            "\n=== Menu de manejo de stock ===" \
            "\n1. Ver la lista de productos completa" \
            "\n2. Eliminar unidades" \
            "\n3. Agregar producto" \
            "\n4. Buscar producto" \
            "\n5. Ver juegos en oferta" \
            "\n6. Mostrar categorias disponibles" \
            "\n7. Volver al menu principal"
        )

        opcion = input("\nIngrese una opcion: ")

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
            mostrar_categorias_y_sin_oferta(stock)

        elif opcion == "7":
            continuar = False

        else:
            print("Opcion invalida.")


def menu_usuarios(usuarios):
    """Muestra el menu de manejo de usuarios."""
    continuar = True

    while continuar:
        print(
            "\n=== Menu de usuarios ===" \
            "\n1. Ver usuarios registrados" \
            "\n2. Registrar nuevo usuario" \
            "\n3. Volver al menu principal"
        )

        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            imprimir_usuarios(usuarios)

        elif opcion == "2":
            registrar_usuario(usuarios)

        elif opcion == "3":
            continuar = False

        else:
            print("Opcion invalida.")

def menu_pruebas_unitarias():
    """Muestra el menu de pruebas unitarias para las funciones más importantes del programa."""

    continuar = True

    while continuar:
        print(
            "\n=== Menú de pruebas unitarias ===" \
            "\n1. Generar ID" \
            "\n2. Ventas" \
            "\n3. Ofertas" \
            "\n4. Transacciones" \
            "\n5. Email válido" \
            "\n6. Volver al menú principal"
        )
        opcion = input("\nIngrese una opción: ")
        if opcion == "1":
            prueba_generar_id_lista_vacia()
            prueba_generar_id_con_elementos()
        elif opcion == "2":
            prueba_sumar_totales_normal()
            prueba_sumar_totales_lista_vacia()
        elif opcion == "3":
            prueba_precio_oferta_normal()
            prueba_precio_oferta_con_decimales()
        elif opcion == "4":
            prueba_balance_positivo()
            prueba_balance_negativo()
            prueba_balance_sin_transacciones()
        elif opcion == "5":
            prueba_email_valido_correcto()
            prueba_email_sin_arroba()
            prueba_email_vacio()
        elif opcion == "6":
            continuar = False
        else:
            print("Opción inválida.")
            

def menu_principal(stock, ventas, usuarios, transacciones, sesion_activa):
    """Menu principal donde el usuario decide si gestionar productos, usuarios o ventas."""

    nombre_usuario, rol_usuario = sesion_activa

    print("\nBienvenido al sistema de venta de videojuegos")
    print(f"Usuario: {nombre_usuario} | Rol: {rol_usuario}")

    continuar = True

    while continuar:
        print(
            "\n=============================" \
            "\nSISTEMA DE GESTION - GRUPO 4" \
            "\n=============================" \
            "\n1. Gestion de Productos" \
            "\n2. Gestion de Usuarios" \
            "\n3. Gestion de Ventas" \
            "\n4. Realizar pruebas unitarias" \
            "\n5. Cerrar sesion"
        )

        n = input("\nIngrese una de las opciones: ")

        if n == "1":
            menu_stock(stock, transacciones)

        elif n == "2":
            menu_usuarios(usuarios)

        elif n == "3":
            menu_ventas(stock, ventas, transacciones)

        elif n == "4":
            menu_pruebas_unitarias()

        elif n == "5":
            guardar_datos(usuarios, stock, ventas, transacciones)
            print("\nCerrando sesion.\n")
            continuar = False

        else:
            print("Numero invalido. Ingrese una opcion valida.")


# ==================== MAIN ====================

usuarios, stock, ventas, transacciones = cargar_datos()
emails_registrados = set(u["email"] for u in usuarios)

try:
    inicio()
except KeyboardInterrupt:
    guardar_datos(usuarios, stock, ventas, transacciones)
    print("\n\nPrograma interrumpido. Los datos fueron guardados antes de cerrar.")