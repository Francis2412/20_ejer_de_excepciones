import os 
def Indiceinventario():
    os.system("cls")
    #Crea una lista de productos y solicita una posición. 
    #Controla IndexError y ValueError con mensajes diferentes.
    lista = ["Pepino", "Lechuga", "Queso", "Tomate", "Té Hi-C"]
    try:
        posicion = int(input("Ingrese la posicion: "))
        print(lista[posicion])
    except ValueError:
        print("¡Oops! Debe ingresar un valor numérico...")
    except IndexError:
        print ("La posición no existe.")
    
     
def Diccionarioempleados():
    os.system("cls")
    #Consulta información de un empleado mediante una clave.
    #Controla KeyError y considera si get() podría ser una alternativa.
    
    empleado = {
            "telefono" : "6660-6660", 
            "nombre" : "Daykoo_08"
        }
    
    try:
        clave= input("Dato a consultar: ")
        print(empleado[clave]) #empleado.get(clave, "No hay información registrada...")
    except KeyError:
        print("No hay clave registrada...")

    


def Menuopciones():
    os.system("cls")
    # Solicita una opción numérica para un menú. Controla ValueError y 
    #usa else para ejecutar la lógica solamente cuando la conversión haya sido exitosa.
    try: 
        num = float(input("Ingresa un número: "))
    except ValueError:
        print("Ehhh... Tienes que ingresar un valor numérico...")
    else:
        print(f"Gracias, el número ingresado fue {num}")
