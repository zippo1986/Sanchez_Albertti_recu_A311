
def mostrar_mensaje(mensaje):
    print(mensaje)
    
def mostrar_productos(lista):
    
    print("ID          producto       precio    U vendidas    stock ")

    for producto in lista:
        mostrar_producto(producto)        

def mostrar_producto(producto) -> None:
    """Muestra las peliculas por aatributo

    Args:
        pelicula (dict): diccionario de pelicula
    """
    print(
        f"{producto['id']:3}| "
        f"{producto['producto']:29}| "
        f"{producto['precio']:15}| "
        f"{producto['unidades_vendidas']:6}|"
        f"{producto['stock']:6}|"

    )

def mostrar_producto_mas_vendido(lista,clave_uno,clave_dos):
    """Muestra el nombre y e tiempo

    Args:
        lista (list): lista de bicis
        clave_uno (str): tipo de bicicleta
        clave_dos (str): tiempo
    """
    print("---------------------------------")
    print(f"{clave_uno}                  {clave_dos}")
    print("---------------------------------")
    
    for elemento in lista:
        print(f" {elemento[clave_uno]:15}   {elemento[clave_dos]}")    