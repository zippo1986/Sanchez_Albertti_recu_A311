def ordenar_alfabeticamente(lista_diccionarios, clave):
    """
    Ordena una lista de diccionarios por una clave específica en orden alfabético
    utilizando el algoritmo de ordenación por burbuja.

     lista_diccionarios: Lista de diccionarios a ordenar.
     La clave por la cual ordenar los diccionarios.
     Lista de diccionarios ordenada.
    """
    n = len(lista_diccionarios)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar dos elementos adyacentes
            if lista_diccionarios[j].get(clave, 'producto') > lista_diccionarios[j + 1].get(clave, ):
                # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
                lista_diccionarios[j], lista_diccionarios[j + 1] = lista_diccionarios[j + 1], lista_diccionarios[j]
    
    return lista_diccionarios
    