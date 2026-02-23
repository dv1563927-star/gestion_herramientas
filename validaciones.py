def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    while(True):
        try:
            dato=int(input(mensaje))
            if minimo<=dato<=maximo:
                return dato
            else:
                print(f'Error, ingrese una opcion entre {minimo} y {maximo}: ')
        except:
            print("Error, ingrese un numero valido")
            
    
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Campo vacio")
        return False
    return True

