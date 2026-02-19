from gestionarJson import guardar, cargar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido

USUARIOS="usuarios.json"

def guardar_usuario():
    usuarios=cargar(USUARIOS)

    nombre_usuario=input("Ingrese porfavor el nombre del usuario: ")
    while nombre_valido(nombre_usuario)==False or existe_usuario(nombre_usuario)==True:
        nombre_usuario=input("Error, intente nuevamente: ")

    apellido_usuario=input("Ingrese porfavor el apellido del usuario: ")
    while nombre_valido(apellido_usuario)==False or existe_usuario(apellido_usuario)==True:
        apellido_usuario=input("Error, intente nuevamente: ")
    
    telefono_usuario=input("Ingrese el numero telefonico del usuario: ")
    while nombre_valido(telefono_usuario)==False:
        telefono_usuario=input("Error, intentelo nuevamente")

    direccion_usuario=input("Ingrese porfavor su direccion: ")
    while existe_usuario(direccion_usuario)==True:
        direccion_usuario=input("Error, intente nuevamente: ")

    nuevo_usuario={
        "id":generar_id(usuarios),
        "nombre":nombre_usuario,
        "apellido":apellido_usuario,
        "telefono":telefono_usuario,
        "direccion":direccion_usuario,
        "tipo de usuario":"usuario"
    }
    usuarios.append(nuevo_usuario)
    guardar(USUARIOS, usuarios)
    print("Persona guardada correctamente!")

def listar_usuarios():
    usuarios=cargar(USUARIOS)

    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    for elemento in usuarios:
        print(f'''
            ======================================
            ID: {elemento["id"]}
            Nombre: {elemento["nombre"]}
            Apellido: {elemento["apellido"]}
            Telefono: {elemento["telefono"]}
            Direccion: {elemento["direccion"]}
            ======================================
                ''')
    print()

def existe_usuario(usuario):
    usuarios=cargar(USUARIOS)

    for elemento in usuarios:
        if usuario.lower()==elemento["nombre"].lower():
            return True
    return False

def actualizar_usuario():
    usuarios=cargar(USUARIOS)
    listar_usuarios()
    id_usuario=validarEntero('Ingrese un ID a actualizar: ')
    while(id_usuario==None):
        id_usuario=validarEntero('Error, intentelo nuevamente: ')
    
    for elemento in usuarios:
        if id_usuario==elemento["id"]:
            while(True):
                op=validarMenu('''
                            Porfavor escoja un atributo a modificar
                            1.  Nombre del usuario
                            2.  Apellido del usuario
                            3.  Telefono del usuario
                            4.  Direccion del usuario
                            5.  Salir
                            ''',1,5)
                match(op):
                    case 1:
                        nombre_usuario=input("Ingrese el nuevo nombre del usuario: ")
                        while nombre_valido(nombre_usuario)==False:
                            nombre_usuario=input("Error, intente nuevamente: ")
                        elemento["nombre"]=nombre_usuario
                    case 2:
                        apellido_usuario=input("Ingrese el nuevo apellido del usuario: ")
                        while nombre_valido(apellido_usuario)==False:
                            apellido_usuario=input("Error, intente nuevamente: ")
                        elemento["apellido"]=apellido_usuario
                    case 3:
                        telefono=input("Ingrese el nuevo numero del usuario: ")
                        while nombre_valido(telefono)==False:
                            telefono=input("Error, intentelo nuevamente")
                        elemento["telefono"]=telefono
                    case 4:
                        direccion=input("Ingrese porfavor la nueva direccion del usuario: ")
                        while nombre_valido(direccion)==False:
                            direccion=input("Error, intentelo de nuevo: ")
                        elemento["direccion"]=direccion
                    case 5:
                        print("...")
                    case _:
                        print("Error, opcion no valida.")
                if op==5:
                    break
            guardar(USUARIOS, usuarios)
            print("Usuario actualizado con exito!")
            return
    print("Usuario no encontrado.\n")

def eliminar_usuario():
    contador_aux=0
    usuarios=cargar(USUARIOS)
    listar_usuarios()
    id_usuario=validarEntero("Ingrese el ID a eliminar: ")
    while (id_usuario==None):
        id_usuario=validarEntero("Error, intentelo nuevamnente: ")

    for elemento in usuarios:
        if id_usuario==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(USUARIOS, usuarios)
            print("Se ha eliminado al usuario correctamente!")
            return
        contador_aux+=1
    print("Usuario no encontrado.")

def crear_admin_predeterminado():
    usuarios=cargar(USUARIOS)

    for elemento in usuarios:
        if elemento["tipo"] == "administrador":
            return
    
    admin={
        "id": 0,
        "nombre": "Admin",
        "apellido": "Principal",
        "telefono": "0000000000",
        "direccion": "Oficina Junta",
        "tipo": "administrador",
        "clave": 1234
    }

    usuarios.append(admin)
    guardar(USUARIOS, usuarios)
    print ("Administrador creado por defecto.")

def login_admin():
    usuarios=cargar(USUARIOS)

    id_ingresada=validarEntero('Ingrese la ID del usuario: ')
    while id_ingresada==None:
        id_ingresada=validarEntero('Error, intentelo nuevamente: ')

    clave_ingresada=validarEntero('Ingrese su clave: ')
    while clave_ingresada==None:
        clave_ingresada=('Error, ingrese un valor valido: ')

    for usuario in usuarios:
        if (
            usuario["id"]== id_ingresada and
            usuario["clave"]== clave_ingresada and
            usuario["tipo"]=="administrador"
        ):
            return True
    return False