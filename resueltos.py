import os

def Conversionedad():
    os.system("cls")
    #Una aplicación solicita la edad. 
    #Si la persona escribe texto que no representa un entero,
    #debe mostrar un mensaje claro y continuar sin finalizar abruptamente.
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("¡Oops! Usted debe ingresar un número entero")
    else:
        print (f"Usted tiene {edad} años")


def Divisionsegura():
    os.system("cls")
    #Un sistema calcula una división.
    # Debe controlar tanto entradas no numéricas como el intento de dividir entre cero.
    try: 
        dividendo = float(input("Ingresa el número que quieres dividir: "))
        divisor = float(input("Ingresa el número por el cual quieres que sea dividio el número anterior: "))
        resulado = dividendo / divisor
    except ValueError:
        print("Tienes que ingresar un número...")
    except ZeroDivisionError:
        print("¡ERROR! No se puede dividir entre cero")
    else:
        print(f"El resultado es: {resulado} ")


def Accesolista():
    os.system("cls")
    #Una aplicación guarda nombres en una lista y solicita una posición. 
    #Controla el caso en que la posición no exista.
    nombres = ["Yuri", "Natsuki", "Sayori"]

    try: 
        posicion = int(input("Posicion: "))
        print(nombres[posicion])
    except ValueError:
        print("La posición debe ser un entero.")
    except IndexError:
        print("La posición no existe.")

    
def Consultacliente():
    os.system("cls")
    #Un diccionario contiene nombre y teléfono.
    # Solicita una clave y controla el caso en que la clave no exista.
    cliente = {
        "telefono" : "1234-1234", "nombre" : "Petunia"
    }
    try:
        clave= input("Dato a consultar: ")
        print(cliente[clave])
    except KeyError:
        print("No hay contraseña registrada...")


def Cierregarantizado():
    os.system("cls")
    #Simula una operación que puede fallar y utiliza finally
    #para mostrar un mensaje que siempre debe aparecer al terminar el proceso.
    try: 
        dividendo = float(input("Ingresa el número que quieres dividir: "))
        divisor = float(input("Ingresa el número por el cual quieres que sea dividio el número anterior: "))
        resulado = dividendo / divisor
    except ValueError:
        print("Tienes que ingresar un número...")
    except ZeroDivisionError:
        print("¡ERROR! No se puede dividir entre cero")
    else:
        print(f"El resultado es: {resulado} ")
    finally:
        print("Operación finalizada")