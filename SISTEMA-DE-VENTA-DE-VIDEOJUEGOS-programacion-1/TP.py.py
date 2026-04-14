#Función para saber si un juego existe en la lista
def buscar_videojuego(lista_juegos):
    investigar = input("¿Qué juego querés revisar?: ")
    encontrado = False

    for juego in lista_juegos:
        if juego == investigar:
            encontrado = True
    
    return encontrado

#Programa principal
if buscar_videojuego(lista_juegos):
    print("El juego se vendió hoy")
else:
    print("No hubo ventas de ese juego")