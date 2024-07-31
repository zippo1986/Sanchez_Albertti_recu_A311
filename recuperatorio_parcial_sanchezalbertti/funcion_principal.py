from lib_archivos import *
from lib_validaciones import *
from lib_mostrar import *
from lib_mapper import *
from lib_asignaciones import *
from lib_filtrado import *
from lib_ordenamiento import *
from lib_calculos import *
import sys


def main ():
    
    
    bandera_carga = False
    
    
    lista_productos= []
    
    nombre_correcto_archivo = "productos"
    
    confirmacion = "s"
    while confirmacion == "s":
            mostrar_mensaje("""Menu de opciones
                        1)cargar archivo csv
                        2)imprimir lista
                        3) Asignar valores
                        4) filtrar por masvendido
                        5)filtrar por menor
                        6)informar promedio de precios
                        7) ordenar alfabeticamente por producto
                        8) mostrar pproducto mas vendido
                        9)Exit""")
            
            opcion = input("Ingrese opcion: ")
            while not validar_entero(opcion):
                opcion= input("Ingrese opcion")
            match (opcion):
                case "1":
                    nombre_archivo = input("Ingrese el nombre del archivo a cargar(Sin extension): ").lower()
                    while nombre_archivo != nombre_correcto_archivo:
                        nombre_archivo = input("Ingrese el nombre del archivo a cargar: ").lower()
                        
                    lista_productos= archivo_a_lista(f"{nombre_archivo}.csv")
                    
                    
                    mostrar_mensaje("El archivo se ha cargado correctamente")
                    
                    
                    bandera_carga = True
                case "2":
                       
                    if not bandera_carga:
                        mostrar_mensaje("No se puede mostrar la lista sin cargarla primero")
                    else:

                        mostrar_productos(lista_productos)
                case "3":
                    if bandera_carga:
                        mapper(lista_productos,asignar_precio)
                        mapper(lista_productos,asignar_unidades)
                        mapper(lista_productos,asignar_stock)
                        mostrar_productos(lista_productos)
                    else:
                        mostrar_mensaje("no se puede sin cargar")
                case "4":
                    if bandera_carga:
                        productos_mas_vendidos = filtrar_datos_mayor(lista_productos,50,"unidades_vendidas")
                        
                        guardar_csv(productos_mas_vendidos,"productosmasvendidos.csv")
                        mostrar_mensaje("El archivo se guardo correctamente")
                    else:
                        mostrar_mensaje("No se puede sin cargar")
                case "5":
                    if bandera_carga:
                        productos_menor_stock = filtrar_datos_menor(lista_productos, 200,"stock")
                        guardar_csv(productos_menor_stock,"productosmenorstock.csv")
                        mostrar_mensaje("se guardo correctamente")
                case "6":
                    if bandera_carga:
                        promedio_productos = sacar_promedio_precio(lista_productos)
                        mostrar_mensaje (f'el promedio de precios es "{promedio_productos}"')
                    else: mostrar_mensaje("no se puede realizar la operacion sin cargar antes")
                case "7":
                    if bandera_carga:
                        ordenar_alfabeticamente(lista_productos,"producto.json")
                        mostrar_mensaje("Se guardo correc")
                
                        guardar_json (lista_productos,"archivo_ordenado")
                case "8":
                    if bandera_carga:
                        producto_mas_vendido =calcular_maximo(lista_productos, "unidades_vendidas")
                        mostrar_producto_mas_vendido(producto_mas_vendido,"producto","precio")
                case "9":
                    sys.exit()



                      
main()                