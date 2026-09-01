import os
from resueltos import Conversionedad, Divisionsegura, Accesolista, Consultacliente, Cierregarantizado
from entradas import Precioproducto, Cantidadproductos, Calificacion, Edadregistro, Tresconsecutivas
from operaciones import Promedioventas, Descuentoproporcional, Conversionmoneda, Tiposincompatibles, Calculocomision
from estructuras import Indiceinventario, Diccionarioempleados, Menuopciones
from recursos import Archivoreportes, Importacioncontrolada

def main():
    os.system("cls")
    print("*********** MENU DE LOS EJERCICOS ***********")
    print("                                             ")
    print("*********** Resueltos mejorados *************")
    print("1..........................Conversión de edad")
    print("2.............................División segura")
    print("3..........................Acceso a una lista")
    print("4.........................Consulta de cliente")
    print("5..........................Cierre garantizado")
    print("                                             ")
    print("*************** Enntradas *******************")
    print("6.......................Precio de un producto")
    print("7.......................Cantidad de productos")
    print("8................................Calificación")
    print("9..........................Edad para registro")
    print("10.................Tres entradas consecutivas")
    print("                                             ")
    print("************** Operaciones ******************")
    print("11.........................Promedio de ventas")
    print("12.....................Descuento proporcional")
    print("13.......................Conversión de moneda")
    print("14........................Tipos incompatibles")
    print("15........................Cálculo de comisión")
    print("                                             ")
    print("***************Estructuras*******************")
    print("16.......................Índice de inventario")
    print("17...................Diccionario de empleados")
    print("18...........................Menú de opciones")
    print("                                             ")
    print("**************** Recursos *******************")
    print("19........................Archivo de reportes")
    print("20.....................Importación controlada")

    opc = int(input("Ingrese el número del ejercicio que desea ejecutar: "))
    match opc:
        case 1:
            Conversionedad()
        case 2: 
            Divisionsegura()
        case 3: 
            Accesolista()
        case 4:
            Consultacliente()
        case 5: 
            Cierregarantizado()
        case 6: 
            Precioproducto()
        case 7:
            Cantidadproductos()
        case 8:
            Calificacion()
        case 9:
            Edadregistro()
        case 10:
            Tresconsecutivas()
        case 11:
            Promedioventas()
        case 12:
            Descuentoproporcional()
        case 13:
            Conversionmoneda()
        case 14:
            Tiposincompatibles()
        case 15:
            Calculocomision()
        case 16:
            Indiceinventario()
        case 17:
            Diccionarioempleados()
        case 18:
            Menuopciones()
        case 19:
            Archivoreportes()
        case 20:
            Importacioncontrolada()
    
main()
    