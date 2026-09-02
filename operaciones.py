import os
def Promedioventas():
    os.system("cls")
    #Solicita tres ventas y calcula su promedio.
    #Controla ValueError y ZeroDivisionError aunque inicialmente parezca improbable dividir entre cero.
    suma = 0
    try:
        for i in range (3):
         ventas = float(input(f"Ingrese la venta #{i+1}: "))
         suma += ventas

        promedio = suma / 3
        print(f"El promedio es igual a: {promedio}")
        
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")
    except ZeroDivisionError:
        print("¡ERROR! No se puede dividir entre cero...")

    

def Descuentoproporcional():
    os.system("cls")
    # Calcula un porcentaje a partir de un monto y una base.
    # Controla entradas no numéricas y una base igual a cero.
    try:
        monto = float(input("Ingrese el monto: "))
        base = float(input("Ingrese la base: "))
        porcentaje = (monto / base) * 100
        print(f"El porcentaje es igual a: {porcentaje}%")
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")
    except ZeroDivisionError:
        print("¡ERROR! No se puede dividir entre cero...")

    
def Conversionmoneda():
    os.system("cls")
    #Solicita monto y tasa de cambio. 
    #Calcula el equivalente y controla los errores de conversión
    try:
        monto = float(input("Ingrese el monto: ")) 
        tasa = float(input("Ingrese tasa de cambio: "))
        equivalente = monto * tasa
    
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")

    print(f"El equivalente es igual a: {equivalente}")


def Tiposincompatibles():
    os.system("cls")
    #Construye un pequeño programa que provoque TypeError
    #y después corrígelo mediante una conversión o una validación apropiada. Explica por qué ocurrió.
    try:
        name = input("Ingresa un nombre: ")
        edad = int(input("Ingresa una edad: "))
        total = name + edad
    except TypeError:
        print("Oops... Algo salio mal...")
    totalxd = name + str(edad)
    print(totalxd)


def Calculocomision():
    os.system("cls")
    #Calcula una comisión a partir de ventas y porcentaje. 
    # Usa try/except para controlar datos no numéricos
    # y documenta qué excepción esperas.
    try:
        venta = float(input("Ingresa la venda: "))
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")
