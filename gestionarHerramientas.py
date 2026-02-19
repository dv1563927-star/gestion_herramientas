from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido

HERRAMIENTAS="herramientas.json"

def guardar_herramienta():
    herramientas=cargar(HERRAMIENTAS)

    nombre=input("Ingrese el nombre de la herramienta: ")
    while nombre_valido(nombre)==False or existe_herramienta(nombre)==True:
        nombre=input("Error, intente nuevamente: ")
        
    estado_herramienta=validarMenu('''
                        Elija un estado para la herramienta
                        1.  Buen estado
                        2.  Mal estado
                            ''',1,2)
    if estado_herramienta==1:
            estado_herramienta="Buen estado"
    elif estado_herramienta==2:
            estado_herramienta="Mal estado"

    categoria_herramienta=validarMenu('''
                    Elija una categoria para la 
                    1.  Carpinteria
                    2.  Construccion
                    3.  Jardineria
                        ''',1,3)
    match(categoria_herramienta):
            case 1:
                categoria_herramienta="Carpiniteria"
            case 2:
                categoria_herramienta="Construccion"
            case 3:
                categoria_herramienta="Jardineria"
            case _:
                categoria_herramienta:None 

    stock_herramienta=validarEntero('Ingrese el stock de la herramienta: ')
    while (stock_herramienta==None):
        stock_herramienta=validarEntero('Error, intente nuevamente: ')

    nueva_herramienta={
            "id":generar_id(herramientas),
            "nombre":nombre,
            "estado de la herramienta":estado_herramienta,
            "categoria":categoria_herramienta,
            "stock":stock_herramienta
        }

    herramientas.append(nueva_herramienta)
    guardar(HERRAMIENTAS, herramientas)
    print("Herramienta guardada correctamente!")

def listar_herramienta():
    herramientas=cargar(HERRAMIENTAS)

    if not herramientas:
        print("No hay herramientas.")
        return
    
    for elemento in herramientas:
        print(f'''
            ====================================================
            ID:         {elemento["id"]}
            Nombre:     {elemento["nombre"]}
            Estado:     {elemento["estado de la herramienta"]}
            Categoria:  {elemento["categoria"]}
            Stock:      {elemento["stock"]}
            ====================================================
                ''')
    print()

def existe_herramienta(herramienta):
    herramientas=cargar(HERRAMIENTAS)

    for elemento in herramientas:
        if herramienta.lower()==elemento["nombre"].lower():
            return True
    return False

def actualizar_herramienta():
    herramientas=cargar(HERRAMIENTAS)
    listar_herramienta()
    id_herramienta=validarEntero('Ingrese un ID a actualizar: ')
    while(id_herramienta==None):
        id_herramienta=validarEntero('Error, intentelo nuevamente: ')

    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            while(True):
                op=validarMenu('''
                        Porfavor elija un atributo a modificar
                        1.  Nombre de la herramienta
                        2.  Estado de la herramienta
                        3.  Categoria de la herramienta
                        4.  Stock
                        5.  Salir
                        ''',1,5)
                match(op):
                    case 1:
                        nombre_herramienta=input("Ingrese el nuevo nombre de la herramienta: ")
                        while nombre_valido(nombre_herramienta)==False:
                            nombre_herramienta=input("Error, intente nuevamente: ")
                        elemento["nombre"]=nombre_herramienta
                    case 2:
                        estado_herramienta=validarMenu('''
                                                    Ingrese la nueva categoria de la herramienta
                                                    1.  Buen estado
                                                    2.  Mal estado
                                                    ''',1,2)
                        if estado_herramienta==1:
                            estado_herramienta="Buen estado"
                        elif estado_herramienta==2:
                            estado_herramienta="Mal estado"
                        elemento["estado de la herramienta"]=estado_herramienta
                    case 3:
                        categoria_herramienta=validarMenu('''
                                                    Ingrese la nueva categoria de la herramienta
                                                    1.  Carpinteria
                                                    2.  Construccion
                                                    3.  Jardineria
                                                    ''',1,3)
                        match(categoria_herramienta):
                            case 1:
                                categoria_herramienta="Carpinteria"
                            case 2:
                                categoria_herramienta="Construccion"
                            case 3:
                                categoria_herramienta="Jardineria"
                            case _:
                                print("Opcion no valida")
                        elemento["categoria"]=categoria_herramienta
                    case 4:
                        stock_herramienta=validarEntero('Ingrese el nuevo stock de la herramienta: ')
                        while(stock_herramienta==None):
                            stock_herramienta=validarEntero('Error, intentelo de nuevo: ')
                        elemento["stock"]=stock_herramienta
                    case 5:
                        print("...")
                    case _:
                        print("Opcion no valida")
                if op==5:
                    break
            guardar(HERRAMIENTAS, herramientas)
            print("Herramienta actualizada correctamente!")
            return
        print("Herramienta no encontrada.")


def eliminar_herramienta():
    contador_aux=0
    herramientas=cargar(HERRAMIENTAS)
    listar_herramienta()
    id_herramienta=validarEntero('Ingrese el id a actualizar: ')
    while (id_herramienta==None):
        id_herramienta=validarEntero('Error, intentelo nuevamente: ')

    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(HERRAMIENTAS, herramientas)
            print("Se ha eliminado la herramienta correctamente!")
            return
        contador_aux+=1
    print("Herramienta no encontrada.")
         


