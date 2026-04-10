# Sistema de compra de Videojuegos
def ingreso(usuarios):
    isUser = False

    while isUser == False:
        nombre = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese contraseña: ")

        for i in range(len(usuarios[0])):
            if usuarios[0][i] == nombre and usuarios[1][i] == clave:
                isUser = True
            else:
                print("El usuario ingresado es incorrecto. Intente nuevamente")

def menu():
    ingreso(usuarios)
    print("\nBienvenido al sistema de venta de videojuegos")
    n = -1

    while n != 0:
        print("Este es el menu de opciones")
        print(
            "\n1) Revisar el catalogo de juegos"
            "\n2) Que juegos estan sin stock"
            "\n3)"
        )

        n = int(input("\nQue le gustaria hacer ahora? (0 para salir del programa): "))

        if n == 1:
            print("\nLista de nuestro catalogo de juegos:")
            print(list(map(lambda x: x[0], juegos)))
            print()


#Main
usuarios = [
    ["ag"], #nombre
    ["123"] #Contraseña
]

juegos = [ #nombre - descripcion - precio - stock - oferta - categoria
    ["Hollow Knight", "Metroidvania tipo soulslike 2D", 5, 15, True, "metroidvania"],
    ["CupHead"]
]
menu()
