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