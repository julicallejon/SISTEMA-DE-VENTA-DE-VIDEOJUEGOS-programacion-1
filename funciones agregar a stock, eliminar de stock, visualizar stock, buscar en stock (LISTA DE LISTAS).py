#TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
#PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

#funciones stock
def agregar_a_stock(stock, producto, cantidad):
    for item in stock:
        if item[0] == producto:
            item[1] += cantidad
            print(producto, "agregado al stock. Cantidad actual:", item[1])
            return
    stock.append([producto, cantidad])
    print(producto, "agregado al stock. Cantidad actual:", cantidad)

def eliminar_de_stock(stock, producto, cantidad):
    for item in stock:
        if item[0] == producto:
            if item[1] < cantidad:
                print("Stock insuficiente. Hay", item[1], "unidades disponibles.")
                return
            item[1] -= cantidad
            print(cantidad, "unidades de", producto, "fueron eliminadas. Cantidad actual:", item[1])
            return
    print("El producto", producto, "no se encuentra en stock.")

def imprimir_stock(stock):
    if not stock:
        print("El stock está vacío.")
        return
    else:
        print("Stock actual:")
        for item in stock:
            print("Producto:", item[0], "--- Cantidad:", item[1])

def buscar_en_stock(stock, producto):
    for item in stock:
        if item[0] == producto:
            print("Producto:", item[0], "--- Cantidad:", item[1])
            return
    print("El producto", producto, "no se encuentra en stock.")

#main
stock= []

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
