import os
def Archivoreportes():
    os.system("cls")
    #Intenta abrir un archivo llamado reportes.txt.
    #Controla FileNotFoundError y utiliza finally para mostrar que la operación terminó.
    try:
        archivo = open("reporte.txt", "r", encoding="utf-8")
        contenido = archivo.read()
    except FileNotFoundError:
        print("No se encontró el archivo de reporte.")
    else:
        print(contenido)
    finally:
        print("Funcion terminada...") 

def Importacioncontrolada():
    os.system("cls")
    #Simula la importación de un módulo que no existe y controla ModuleNotFoundError.
    #El mensaje debe explicar qué debe revisar la persona desarrolladora.
    try:
        import modulo_ejemplo
        
    except ModuleNotFoundError:
        print("Modulo no encontrado")
        print("Por favor revisa si el nombre escrito es el correcto...")