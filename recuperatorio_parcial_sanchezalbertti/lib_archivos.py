import json
def get_path_actual(nombre_archivo):
    """_summary_
        Consigue el directorio actual

    Args:
        nombre_archivo (str): el  nombre del archivo 

    Returns:
        path: retorna una instancia de la clase os que tiene el atributo "path" que es un string y lo une al nombre del archivo con el metodo join que tienen los str
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)
def archivo_a_lista(archivo_csv):
    """_summary_
        toma un archivo_csv y convierte en una lista de diccionarios
    

    Args:
        archivo_csv (str): el nombre del archivo

    Returns:
        list: una lista de diccionarios
    """
    with open(get_path_actual(archivo_csv), "r", encoding="utf-8") as archivo:
        lista = []
        archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            bicicleta = {}
            linea = linea.strip("\n").split(",")
            id, producto, precio, unidades_vendidas,stock = linea
            
            bicicleta["id"] = int(id)
            bicicleta["producto"] = producto
            bicicleta["precio"] = int(precio)
            bicicleta["unidades_vendidas"] = int(unidades_vendidas)
            bicicleta["stock"] = int(stock)
            
            lista.append(bicicleta)
        
        
    return lista

def guardar_csv(lista: list, nombre_archivo: str):
    """
        guarda los elementos de la lista en un archivo .csv

    Args:
        lista (list): lista de diccionarios
        nombre_archivo (str): nombre del archivo
    """
    if not lista:
        return  
    encabezado = list(lista[0].keys())

    
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        
        archivo.write(",".join(encabezado) + "\n")
        
        
        for bicicleta in lista:
            linea = ",".join(str(bicicleta[key]) for key in encabezado)
            archivo.write(linea + "\n")

def guardar_json(lista: list, nombre_archivo: str):
    
    """Guarda una lista de diccionarios en un archivo .json
    """
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        
        json.dump(lista, archivo, ensure_ascii=False, indent=4)