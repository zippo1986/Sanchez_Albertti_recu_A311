def calcular_maximo(lista, atributo):
    """Calcula los  maximos de determinado atributo dentro de una lista de diccionarios

    Args:
        lista (list):lista de heroes
        atributo (str): la clave del diccionario de la que se quiere sacar el maximo

    Returns:
        list: retorna una lista de diccionarios que contiene los heroes del maximo en determinado atributo
    """
    bandera = True
    numero_minimo = None
    bicicleta_ganador = []
    for i in lista:
        if  (bandera ==True)or(int(i[atributo]) >(numero_minimo)) :
            
            numero_minimo =int(i[atributo])
            bandera= False
    
    for i in lista:
        if int(i[atributo])== numero_minimo:
            bicicleta_ganador.append(i)
    return bicicleta_ganador


def sacar_promedio_precio(lista_diccionarios):
    # Crear un conjunto de tipos únicos
    promedio = 0
    contador = 0
    
    
    suma_precio = 0
    for producto in lista_diccionarios:
        suma_precio = suma_precio+ producto["precio"] 
        contador = contador+1
    
    promedio = suma_precio / contador

    return promedio
    
                     
    