from gestionarJson import guardar, cargar, generar_id
from datetime import datetime


def guardarLog(usuario, accion, descripcion):
    LOG="log.json"

    historial=cargar(LOG)

    nuevo_registro={
        "id":generar_id(historial),
        "usuario":usuario,
        "accion":accion,
        "descripcion":descripcion,
        "fecha":str(datetime.now()) 
    }

    historial.append(nuevo_registro)
    guardar(LOG, historial)
    

def listarLog():
    LOG="log.json"
    historial=cargar(LOG)

    for elemento in historial:
        print(f'''
            =============================================
            ID LOG: {elemento["id"]}
            USUARIO: {elemento["usuario"]}
            ACCION REALIZADA: {elemento["accion"]}
            DESCRIPCION: {elemento["descripcion"]}
            FECHA: {elemento["fecha"]}
            =============================================
            ''')

