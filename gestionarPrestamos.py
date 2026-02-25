from gestionarJson import guardar, cargar, generar_id
from datetime import datetime, timedelta, date
from gestionarUsuarios import listar_usuarios
from gestionarHerramientas import listar_herramienta
from validaciones import validarEntero, validarMenu
from logs import guardarLog

PRESTAMOS="prestamos.json"
HERRAMIENTAS="herramientas.json"
USUARIOS="usuarios.json"

def crear_solicitud_prestamo():
    prestamos = cargar(PRESTAMOS)
    herramientas = cargar(HERRAMIENTAS)

    print("\n--- USUARIOS DISPONIBLES ---")
    listar_usuarios()

    id_usuario = validarEntero('Ingrese el ID del usuario: ')
    while id_usuario is None:
        guardarLog("ID de usuario no valida", "ID_NO_VALIDA", "Se intento ingresear una ID no valida")
        id_usuario = validarEntero('Error, intentelo nuevamente: ')

    print('\n--- HERRAMIENTAS DISPONIBLES ---')
    listar_herramienta()

    id_herramienta = validarEntero('Ingrese el ID de la herramienta: ')
    while id_herramienta is None:
        guardarLog("ID de herramienta no valida", "ID_NO_VALIDA", "Se intento ingresear una ID no valida")
        id_herramienta = validarEntero('Error, intentelo nuevamente: ')

    herramienta_encontrada = None
    for herramienta in herramientas:
        if herramienta["id"] == id_herramienta:
            herramienta_encontrada = herramienta
            break

    if herramienta_encontrada is None:
        print("Herramienta no encontrada.")
        guardarLog("Herramienta no encontrada", "HERRAMIENTA_NO_VALIDA", "Se intento ingresar una herramienta no valida")
        return

    if herramienta_encontrada["estado de la herramienta"] == "mal estado":
        print("La herramienta esta dañada y no esta disponible.")
        guardarLog("Herramienta dañada", "HERRAMIENTA_DAÑADA", "Se intento pedir prestada una herramienta en mal estado")
        return

    cantidad_solicitada = validarEntero("Ingrese la cantidad que necesita: ")
    while cantidad_solicitada is None or cantidad_solicitada <= 0:
        guardarLog("Stock no valido", "STOCK_NO_VALIDO", "Se intento ingresear una cantidad no valida")
        cantidad_solicitada = validarEntero("Error, ingrese una cantidad valida: ")

    if herramienta_encontrada["stock"] < cantidad_solicitada:
        print("No hay suficiente stock para realizar la solicitud.")
        guardarLog("Stock insuficiente", "STOCK_NO_VALIDO", "Se intento ingresar una cantidad no valida")
        return

    dias = validarEntero('Ingrese la cantidad de dias que necesita la herramienta: ')
    while dias is None or dias <= 0:
        guardarLog("Fecha", "FECHA_NO_VALIDA", "Se intento ingresear una fecha no valida")
        dias = validarEntero('Error, intentelo nuevamente: ')

    fecha_inicio = datetime.now()
    fecha_fin = fecha_inicio + timedelta(days=dias)

    nuevo_prestamo = {
        "id": generar_id(prestamos),
        "id_usuario": id_usuario,
        "id_herramienta": id_herramienta,
        "cantidad": cantidad_solicitada,
        "fecha_inicio": str(fecha_inicio.isoformat()),
        "fecha_fin": str(fecha_fin.isoformat()),
        "estado": "pendiente",
        "reporte":[]
    }

    prestamos.append(nuevo_prestamo)
    guardar(PRESTAMOS, prestamos)
    guardarLog("Guardado","GUARDAR_SOLICITUD_PRESTAMO","Se realizo la creacion de una solicitud de prestamo para ser revisada por un admin")

    print("Solicitud de prestamo creada con exito!")

def listar_prestamos():
    prestamos=cargar(PRESTAMOS)
    usuarios=cargar(USUARIOS)
    herramientas=cargar(HERRAMIENTAS)

    if not prestamos:
        print("No hay prestamos guardados.")
        guardarLog("Listar prestamos inexistentes", "LISTAR_FALLIDO", "Se intento listar los prestamos que no existen")
        return
    
    for prestamo in prestamos:
        nombre_usuario="Desconocido"
        nombre_herramienta="Desconocido"

    for usuario in usuarios:
        if usuario["id"]==prestamo["id_usuario"]:
            nombre_usuario=usuario["nombre"]
            break

    for herramienta in herramientas:
        if herramienta["id"]==prestamo["id_herramienta"]:
            nombre_herramienta=herramienta["nombre"]
            break

    for elemento in prestamos:
        print(f'''
            =============================================
            ID Prestamo: {elemento["id"]}
            ID Usuario: {nombre_usuario} ID: {elemento["id"]}
            ID Herramienta: {nombre_herramienta} ID: {elemento["id_herramienta"]}
            Fecha inicio: {elemento["fecha_inicio"]}
            Fecha fin: {elemento["fecha_fin"]}
            Estado: {elemento["estado"]}
            Reporte: {elemento["reporte"]}
            =============================================
            ''')
        
def devolver_prestamo():
    prestamos=cargar(PRESTAMOS)
    herramientas=cargar(HERRAMIENTAS)
    usuarios=cargar(USUARIOS)
    
    prestamos_activos=[]

    for prestamo in prestamos:
        if prestamo["estado"]=="activo":
            prestamos_activos.append(prestamo)
    
    if not prestamos_activos:
        print("No hay prestamos activos para devolver.")
        guardarLog("Prestamo inexistente", "PRESTAMO_NO_VALIDO", "Se intento ingresear devolver un prestamo que no existe")
        return
    
    print("Prestamos activos: ")
    for prestamo in prestamos_activos:

        nombre_usuario= "Desconocido"
        nombre_herramienta="Desconocida"

        for usuario in usuarios:
            if usuario["id"]==prestamo["id_usuario"]:
                nombre_usuario = usuario["nombre"]
                break

        for herramienta in herramientas:
            if herramienta["id"]==prestamo["id_herramienta"]:
                nombre_herramienta = herramienta["nombre"]
                break

        print(f''' 
                =============================================== 
                ID: {prestamo["id"]}
                Usuario: {nombre_usuario} ID: {prestamo["id_usuario"]}
                Herramienta: {nombre_herramienta} ID: {prestamo["id_herramienta"]}
                Cantidad: {prestamo["cantidad"]}
                Reporte: {prestamo["reporte"]}
                ===============================================
                ''')

    id_prestamo=validarEntero('Ingrese el ID del prestamo a devolver: ')
    while id_prestamo==None:
        guardarLog("ID no valida", "ID_NO_VALIDA", "Se intento ingresear una ID no valida")
        id_prestamo=validarEntero('Error, intentelo nuevamente: ')

    for prestamo in prestamos_activos:
        if prestamo["id"]== id_prestamo:
            
            print(f'Cantidad prestada: {prestamo["cantidad"]}')
            cantidad_devuelta=validarEntero('Ingrese la cantidad de herramientas que va a devolver: ')
            while cantidad_devuelta is None or cantidad_devuelta <=0 or cantidad_devuelta>prestamo["cantidad"]:
                guardarLog("Cantidad devuelta no valida", "CANTIDAD_NO_VALIDA", "Se intento ingresar una cantidad no valida")
                cantidad_devuelta=validarEntero(f"Error, ingrese un numero valido (max {prestamo['cantidad']}): ")

            estado_entregado=validarMenu('''
                        Ingrese el estado en el que devuelve la herramienta
                        1.  Buen estado
                        2.  Mal estado
                        ''',1,2)
            for herramienta in herramientas:
                if herramienta["id"]==prestamo["id_herramienta"]:

                    if estado_entregado==1:
                        herramienta["estado"]="buen estado"
                        herramienta["stock"]+= cantidad_devuelta
                    if estado_entregado==2:
                        herramienta["estado"]="mal estado"
                        herramienta["stock"]+=cantidad_devuelta
                    break
            for herramienta in herramientas:
                if herramienta["id"] == prestamo["id_herramienta"]:
                    reporte_nuevo=validarMenu('''
                                Desea añadir un reporte para la herramienta?
                                1.  Si
                                2.  No
                            ''',1,2)
                    match(reporte_nuevo):
                        case 1:
                            reporte_nuevo=input("Porfavor, escriba aqui su reporte: ")
                            prestamo["reporte"].append(reporte_nuevo)
                        case 2:
                            break

            prestamo["cantidad"]-=cantidad_devuelta
            if prestamo["cantidad"]==0:
                prestamo["estado"]="devuelto"

            guardar(PRESTAMOS, prestamos)
            guardar(HERRAMIENTAS, herramientas)
            guardarLog("Devolucion","DEVOLUCION_PRESTAMO","Se realizo la devolucion de una herramienta prestada")

            print(f'Prestamo actualizado correctamente. Cantidad restante: {prestamo["cantidad"]}')
            return
    print('Prestamo no encontrado o ya devuelto.')

def verificar_vencidos():
    prestamos=cargar(PRESTAMOS)
    hoy=datetime.today().date()

    for elemento in prestamos:
        fecha_fin = datetime.fromisoformat(elemento["fecha_fin"]).date()

        if elemento["estado"]=="activo" and hoy>fecha_fin:
            print(f'El prestamo {elemento["id"]} esta VENCIDO.')

def gestion_prestamos_admin():
    prestamos=cargar(PRESTAMOS)
    herramientas=cargar(HERRAMIENTAS)
    usuarios=cargar(USUARIOS)

    pendientes=[]

    for prestamo in prestamos:
        if prestamo["estado"]=="pendiente":
            pendientes.append(prestamo)

    if not pendientes:
        print('No hay prestamos pendientes.')
        return
    
    for prestamo in prestamos:
        nombre_usuario=""
        nombre_herramienta=""

    for usuario in usuarios:
        if usuario["id"]==prestamo["id_usuario"]:
            nombre_usuario=usuario["nombre"]
            break

    for herramienta in herramientas:
        if herramienta["id"]==prestamo["id_herramienta"]:
            nombre_herramienta=herramienta["nombre"]
            break

    print("---PRESTAMOS PENDIENTES---")
    for prestamo in pendientes:
        if prestamo["estado"]=="pendiente":
            print(f'''
                =================================================================
                ID: {prestamo["id"]}
                Usuario: {nombre_usuario} ID: {prestamo["id_usuario"]}
                Herramienta: {nombre_herramienta} ID: {prestamo["id_herramienta"]}
                Cantidad: {prestamo["cantidad"]}
                Fecha fin: {prestamo["fecha_fin"]}
                Estado: {prestamo["estado"]}
                =================================================================       
                ''')
        else:
            print("No hay prestamos pendientes.")
        
    id_prestamo=validarEntero('Ingrese el ID del prestamo a gestionar: ')
    while id_prestamo==None:
        guardarLog("ID de prestamo no valida", "ID_NO_VALIDA", "Se intento ingresear una ID no valida")
        id_prestamo=validarEntero('Error, intentelo nuevamente: ')

    for prestamo in pendientes:
        if prestamo["id"]==id_prestamo and prestamo["estado"]=="pendiente":
            op=validarMenu('''  
                    Porfavor esoja una opcion para el prestamo
                    1.  Aprobar prestamo
                    2.  Rechazar prestamo
                        ''',1,2)
            if op==1:
                for herramienta in herramientas:
                    if herramienta["id"]==prestamo["id_herramienta"]:
                        if herramienta.get("estado") == "mal estado":
                            print("La herramienta no puede prestarse (mal estado).")
                            prestamo["estado"] = "rechazado"
                            guardar(PRESTAMOS, prestamos)
                            return
                        
                        if herramienta["stock"] < prestamo["cantidad"]:
                            print("No hay stock suficiente")
                            prestamo["estado"]="rechazado"
                            guardar(PRESTAMOS, prestamos)
                            return
                        
                        herramienta["stock"] -= prestamo["cantidad"]
                        prestamo["estado"] = "activo"
                        print("Prestamo aprobado con exito!")
                        guardar(PRESTAMOS, prestamos)
                        guardar(HERRAMIENTAS, herramientas)
                        return
            elif op==2:
                prestamo["estado"]="rechazado"
                print("Prestamo rechazado")

            guardar(PRESTAMOS, prestamos)
            guardar(HERRAMIENTAS, herramientas)
            guardarLog("Gestion","GESTION_PRESTAMO","Se realizo la gestion de un prestamo, sea aprobado o rechazado")
            return
    print("Prestamo no encontrado.")


def herramientas_menos_stock():
    herramientas=cargar(HERRAMIENTAS)

    if not herramientas:
        print("No hay herramientas registradas.")
        return
    
    # Ordeno de menor a mayor stock
    herramientas_ordenadas= sorted(herramientas, key=lambda h: h["stock"])

    print("\n--- HERRAMIENTAS CON MENOS STOCK ---")
    for herramienta in herramientas_ordenadas:
        print(f'''
            =================================
            ID:     {herramienta["id"]}
            Nombre: {herramienta["nombre"]}
            Stock:  {herramienta["stock"]}
            =================================
            ''') 
    guardarLog("Consulta", "CONSULTAR_STOCK_BAJO", "Se consulto sobre las herramientas con menos stock") 
    
          
def herramientas_mas_prestadas():
    herramientas=cargar(HERRAMIENTAS)
    prestamos=cargar(PRESTAMOS)

    if not herramientas:
        print("No hay herramientas registradas.")
        return

    if not prestamos:
        print("No hay prestamos.")
        return
    
    # Contador de solicitudes por herramienta
    contador={}

    for prestamo in prestamos:
        id_herramienta=prestamo["id_herramienta"]

        if id_herramienta in contador:
            contador[id_herramienta]+=1
        else:
            contador[id_herramienta] = 1

    # Ordenar herramientas segun cantidad de solicitudes (de mayor a menor)
    herramientas_ordenadas=sorted(
        herramientas,
        key=lambda h: contador.get(h["id"], 0),
        reverse=True
    )

    print("\n--- HERRAMIENTAS MAS SOLICITADAS ---")

    for herramienta in herramientas_ordenadas:
        print(f'''
            ==============================
            ID: {herramienta["id"]}
            Nombre: {herramienta["nombre"]}
            Solicitudes: {contador.get(herramienta["id"], 0)}
            ==============================
            ''')

    guardarLog("Consulta", "CONSULTAR_PRESTAMOS_FRECUENTES", "Se consulto sobre la cantidad de prestamos de las herramientas")

def ver_reportes_herramienta(herramientas, prestamos):
    print("\n--- REPORTES POR HERRAMIENTA ---")

    for herramienta in herramientas:
        tiene_reporte = False

        for prestamo in prestamos:
            if (prestamo["id_herramienta"]==herramienta["id"]
                and "reporte" in prestamo
                and prestamo["reporte"] != ""):

                if not tiene_reporte:
                    print(f'''
                        ======================================
                        Herramienta:    {herramienta["nombre"]}
                        ID:             {herramienta["id"]}
                        ======================================
                            ''')
                    tiene_reporte = True

                print(f' - {prestamo["reporte"]}')    

