from gestionarHerramientas import guardar_herramienta, actualizar_herramienta, eliminar_herramienta, listar_herramienta
from gestionarUsuarios import actualizar_usuario, eliminar_usuario, listar_usuarios, crear_admin_predeterminado, guardar_usuario, login_admin
from validaciones import *
from gestionarPrestamos import gestion_prestamos_admin, crear_solicitud_prestamo, verificar_vencidos, listar_prestamos, devolver_prestamo

def menuInicio():
    crear_admin_predeterminado()
    while(True):
        op0=validarMenu('''
            Escoja porfavor una opcion
            1.  Ingresar como administrador
            2.  Ingresar como usuario
            3.  Salir    
            ''',1,3)
        match(op0):
            case 1:
                if login_admin():
                    print("Acceso concedido!")
                    menu_admin()
                else:
                    print("Acceso denegado!")
            case 2:
                menu_usuario()
            case 3:
                print("...")
            case _:
                print("Opcion no valida")
        if op0==3:
            break

def menu_admin():

    while(True):
        op1=validarMenu('''
                    Escoja la opcion a realizar:
                    1.  Gestionar herramientas
                    2.  Gestionar usuarios
                    3.  Gestionar prestamos
                    4.  Salir
                    ''',1,4)
        match(op1):
            case 1:
                menu_gestion_herramientas()
            case 2:
                menu_gestion_usuarios()
            case 3:
                menu_gestion_prestamo()
            case 4:
                print("...")
            case _:
                print("Opcion no valida")
        if op1==4:
            break

def menu_gestion_herramientas():
    while(True):
        op2=validarMenu('''
                    Ingrese una accion a realizar:
                    1.  Agregar una herramienta
                    2.  Listar las herramientas
                    3.  Actualizar una herramienta
                    4.  Eliminar una herramienta
                    5.  Salir
                    ''',1,5)
        match(op2):
            case 1:
                guardar_herramienta()
            case 2:
                listar_herramienta()
            case 3:
                actualizar_herramienta()
            case 4:
                eliminar_herramienta()
            case 5:
                print("...")
            case _:
                print("Opcion no valida")
        if op2==5:
            break
    
def menu_gestion_usuarios():
    while(True):
        op3=validarMenu('''
                    Ingrese una accion a realizar:
                    1.  Agregar un usuario
                    2.  Listar los usuarios
                    3.  Actualizar un usuario
                    4.  Eliminar un usuario
                    5.  Salir
                        ''',1,5)
        match(op3):
            case 1:
                guardar_usuario()
            case 2:
                listar_usuarios()
            case 3:
                actualizar_usuario()
            case 4:
                eliminar_usuario()
            case 5: 
                print("...")
            case _:
                print("Opcion no valida")
        if op3==5:
            break

def menu_gestion_prestamo():
    while(True):
        op4=validarMenu('''
                    Escoja una de las opciones
                    1.  Aprobacion de prestamos
                    2.  Listar prestamos
                    3.  Salir
                    ''',1,3)
        match(op4):
            case 1:
                gestion_prestamos_admin()
            case 2:
                listar_prestamos()
            case 3:
                print("...")
            case _:
                print("Opcion no valida")
        if op4==3:
            break

def menu_usuario():
    while(True):
        op5=validarMenu('''
                    Escoja una de las acciones a realizar
                    1.  Crear una solicitud
                    2.  Devolver un prestamo
                    3.  Listar prestamos
                    4.  Salir
                    ''',1,4)
        match(op5):
            case 1:
                crear_solicitud_prestamo()
            case 2:
                devolver_prestamo()
            case 3:
                listar_prestamos()
            case 4:
                print("...")
            case _:
                print("Opcion no valida")
        if op5==4:
            break
        

    
    