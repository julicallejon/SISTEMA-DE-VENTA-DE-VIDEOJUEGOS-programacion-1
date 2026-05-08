#TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
#PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

#funciones stock
def agregar_a_stock(stock, producto, cantidad):
    if producto in stock:
        stock[producto] += cantidad
    else:
        stock[producto] = cantidad
    print(cantidad, "unidades de", producto, "agregadas. Cantidad actual:", stock[producto])

def eliminar_de_stock(stock, producto, cantidad):
    if producto not in stock:
        print("El producto", producto, "no se encuentra en stock.")
    elif stock[producto] < cantidad:
        print("Stock insuficiente. Cantidad actual de", producto, ":", stock[producto])
    else:
        stock[producto] -= cantidad
        print(cantidad, "unidades de", producto, "eliminadas. Cantidad actual:", stock[producto])
        if stock[producto] == 0:
            del stock[producto]
            print(producto, "eliminado.")

def imprimir_stock(stock):
    if not stock:
        print("El stock está vacío.")
        return
    else:
        print("Stock actual:")
        for producto in stock:
            print("Producto:", producto, "--- Cantidad:", stock[producto])

def buscar_en_stock(stock, producto):
    if producto in stock:
        print("Producto:", producto, "--- Cantidad:", stock[producto])
    else:
        print("El producto", producto, "no se encuentra en stock.")

#main
stock= {}

while True:
    print("Menu de manejo de stock:")
    print("1. Agregar producto al stock")
    print("2. Eliminar producto del stock")
    print("3. Visualizar stock")
    print("4. Buscar producto en stock")

    numero_menu_stock = input("Ingrese una opción: ")

    if numero_menu_stock == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        agregar_a_stock(stock, producto, cantidad)

    elif numero_menu_stock == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a eliminar: "))
        eliminar_de_stock(stock, producto, cantidad)

    elif numero_menu_stock == "3":
        imprimir_stock(stock)

    elif numero_menu_stock == "4":
        producto = input("Ingrese el nombre del producto: ")
        buscar_en_stock(stock, producto)

    else:
        print("Número inválido. Ingrese una opción válida.")