from random import randint
def asignar_precio(i, max= 300, min=100):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    i["precio"] = randint(min, max)

def asignar_unidades(i, max= 100, min=1):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    i["unidades_vendidas"] = randint(min, max)
def asignar_stock(i, max= 300, min=50):
    """asigna un valor random

    Args:
        i (dict): diccionario de la lista
        max (int): numero maximo
        min (int): numero minimo
    """
    i["stock"] = randint(min, max)