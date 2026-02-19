def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None
    
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Campo vacio")
        return False
    return True

