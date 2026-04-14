#Función para validar cupón de descuento
def validar_cupon(total_compra):
    cupon = "MOJANG2026"
    
    print("\n--- VALIDACIÓN DE CUPÓN ---")
    ingresado = input("¿Tenes un cupón de descuento? (Si no tenes, presiona Enter): ")
    
    if ingresado == cupon:
        descuento = total_compra * 0.10
        total_final = total_compra - descuento
        print("¡Descuento aplicado! El total de tu compra es de: $", descuento)
        return total_final
    else:
        if ingresado != "":
            print("Cupón rechazado.")
        return total_compra

#Programa principal
ingreso_final = validar_cupon(ingreso)
print("Monto total a pagar: $", ingreso_final)