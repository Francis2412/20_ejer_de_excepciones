import os
def Precioproducto():
    os.system("cls")
    #Solicita el precio de un producto y conviértelo a float. 
    #Controla ValueError y muestra un mensaje adecuado cuando la entrada no sea numérica.
    try:
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")
    else:
        print(f"Precio: {precio}")
    

def Cantidadproductos():
    os.system("cls")
    #Solicita la cantidad de unidades que una persona desea comprar.
    #Controla entradas que no puedan convertirse a entero.
    try:
        cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))
    except ValueError:
        print("¡Oops! Debe ingresar un número entero...")


def Calificacion():
    os.system("cls")
    #Solicita una calificación numérica.
    #Controla ValueError y, si la conversión funciona, indica si la calificación está entre 0 y 100.
    while True:
        try:
            calif = float(input("Ingrese la calificación: "))
            if calif > 0 and calif <100:
                print("La calificación está entre 0 y 100")
                break
            else:
                print("La calificación debe entre 0 y 100")
        except ValueError:
            print("¡Oops! Debe ingresar un valor numérico...")


def Edadregistro():
    os.system("cls")
    #Solicita la edad. 
    #Controla ValueError y evita que el programa continúe con una edad que no sea válida.
    try:
        edad = input(int("Ingrese su edad: "))
    except ValueError:
        print("¡Oops! Debe ingresar un número entero...")
    
def Tresconsecutivas():
    os.system("cls")
    #Solicita nombre, edad y salario. 
    #Controla únicamente las conversiones que pueden producir excepciones
    #y muestra qué dato debe corregirse.
    nombre = input("Ingrese su nombre: ")

    while True:

        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("¡Oops! Debe ingresar un número entero...")
            

    while True:

        try:
            salario = float(input("Ingrese su salario: "))
            break
        except ValueError:
            print("¡Oops! Debe ingresar un valor numérico...")
    print("\n")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario: {salario}")
            
        
    
        

            