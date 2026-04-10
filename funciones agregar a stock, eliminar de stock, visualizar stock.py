#TRABAJO PRÁCTICO OBLIGATORIO - PROGRAMACIÓN I - PRIMER CUATRIMESTRE 2026
# GRUPO 4 - BICHUTE MATEO, BRITEZ MARTINA AYLEN, CALLEJON JULIETA ROCIO, RONCHI AGUSTIN, TEPER AYALA SOFIA
#PROFESORES - ESCANDELL GUSTAVO MANUEL, SELLES MELINDA LUJAN

#funciones stock
def agregar_a_stock(stock, producto, cantidad):
    producto = int(input("Ingrese el producto a agregar al stock: "))
    cantidad = int(input("Ingrese la cantidad a agregar al stock: "))
    if producto in stock:
        stock[producto] += cantidad
    else:
        stock[producto] = cantidad
    print(producto, "agregado al stock. Cantidad actual:", stock[producto])

def eliminar_de_stock(stock, producto, cantidad):
    producto = int(input("Ingrese el producto a eliminar del stock: "))
    cantidad = int(input("Ingrese la cantidad a eliminar del stock: "))
    if producto in stock:
        stock[producto] -= cantidad
        print( cantidad, "unidades de", producto, "fueron eliminadas. Cantidad actual:", stock[producto])
    else:
        print("No hay suficiente stock para eliminar esa cantidad.")

def imprimir_stock(stock):
    print("Stock actual:")
    for producto, cantidad in stock.items():
        print("Producto:", producto, "Cantidad:", cantidad)




