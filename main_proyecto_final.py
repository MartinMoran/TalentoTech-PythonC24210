import sqlite3 as sql
import modulo_bbdd
import modulo_validaciones
import modulo_titulos
from colorama import init, Fore, Back, Style

init(autoreset=True)

def mostrar_menu():
    opcion = ""
    while opcion != "7":   
        modulo_titulos.titulo_menu()
        opcion = input(Fore.YELLOW+"Elija una opcion del menu: ")

        match opcion:
            case "1":
                registrar_productos()
            case "2":
                actualizar_productos()
            case "3":
                eliminar_productos()
            case "4":
                mostrar_productos()
            case "5":
                reporte_bajo_stock()
            case "6":
                buscar_productos()
            case "7":
                print(Fore.GREEN+Style.BRIGHT+f'\nOpcion {opcion}, Saliendo... Gracias por usar nuestro sistema!'+Fore.RESET+'\n')
            case _:
                print(Fore.RED+Style.BRIGHT+f'\nLa opcion "{opcion}", no es un numero del menu, intenta nuevamente!'+Fore.RESET)

def registrar_productos():
    while True:
        modulo_titulos.titulo_registrar_prod()        
        # SOLICITAMOS LOS DATOS CON EL MODULO VALIDACIONES
        nombre = modulo_validaciones.solicitar_nombre()
        cantidad = modulo_validaciones.solicitar_cantidad()
        precio_unitario = modulo_validaciones.solicitar_precio_unitario()
        categoria = modulo_validaciones.solicitar_categoria()
        descripcion = modulo_validaciones.solicitar_descripcion()
    
        try:
            # CONEXION A LA BASE DE DATOS Y EJECUCION DEL REGISTRO EN BBDD       
            conn = sql.connect("inventario.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO productos (nombre, cantidad, precio_unitario, categoria, descripcion) 
                        VALUES(?, ?, ?, ?, ?)''', (nombre, cantidad, precio_unitario, categoria, descripcion))
            conn.commit()
            print("")
            print(Fore.GREEN+f"Producto {nombre.upper()} agregado correctamente"+Fore.RESET)
            # VALIDAMOS SI EL USUARIO QUIERE CONTINUAR AGREGANDO REGISTROS    
            continuar = input(Fore.YELLOW+"\nDesea continuar agregando productos? (s/n): "+Fore.RESET).lower()
            if continuar == "s":
                continue
            elif continuar == "n":
                print("\nVolviendo al menu principal...")
                break
            else:
                print(Fore.RED+"\nDebe ingresar una respuesta valida!"+Fore.RESET)
                print("...")
                print("Volviendo al menu principal...")
                break
        except Exception as e:
            print(Back.RED+f"Error inesperado {e}"+Back.RESET)
            
        finally:
            if conn:
                conn.close()

def actualizar_productos():
    modulo_titulos.titulo_actualizar_prod()
    # SE PRESENTAN LOS PRODUCTOS PARA VER EL LISTADO GENERAL
    mostrar_productos()
    print("")

    # SOLICITAMOS LOS DATOS AL USUARIO CON INPUT Y MODULO VALIDACIONES
    id = modulo_validaciones.solicitar_id()
    cantidad = modulo_validaciones.solicitar_cantidad()
    
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE productos SET cantidad=? WHERE id=?",(cantidad, id))
    conn.commit()
    
    print(Fore.GREEN+"\nProducto actualizado correctamente!\n"+Fore.RESET)
    print("Volviendo al menu principal...")
    
    conn.close()
 
def eliminar_productos():
    while True:
        modulo_titulos.titulo_eliminar_prod()      
        mostrar_productos()
        print("")
        
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        
        id = modulo_validaciones.solicitar_id()
        confirmar = input(Fore.YELLOW+"\nEsta seguro de borrar el registro? (s/n): "+Fore.RESET).lower()
        
        # VALIDAMOS LA ELIMINACION CON UNA SEGUNDA CONSULTA
        if confirmar == "s":
            cursor.execute("DELETE FROM productos WHERE id=?",(id,))
            conn.commit()
            print(Fore.GREEN+f"\nProducto eliminado correctamente"+Fore.RESET)
            print("...")
            print("Volviendo al menu principal...")
            break
        # VALIDAMOS SI EL USUARIO QUIERE SALIR AL MENU PRINCIPAL O CONTINUAR ELIMINANDO
        elif confirmar == "n":
            continuar = input(Fore.YELLOW+"\nDesea volver al menu principal? (s/n): "+Fore.RESET).lower()
            if continuar == "s":
                print("...")
                print("Volviendo al menu principal...")
                break
            elif continuar == "n":
                print("...")
                print("\nVolviendo a eliminar productos...")
                continue
            else:
                print(Fore.RED+"\nDebe ingresar una respuesta valida!"+Fore.RESET)
                print("...")
                print("\nVolviendo a eliminar productos...")
                continue
        else:
            print(Fore.RED+"\nDebe ingresar una respuesta valida!"+Fore.RESET)
            print("...")
            print("\nVolviendo a eliminar productos...")
        
        conn.close()           
        
def mostrar_productos():
    modulo_titulos.titulo_mostrar_prod()    
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    resultado = cursor.fetchall()
    modulo_titulos.subtitulo_lista_prod()
    # RECORREMOS EL RESULTADO CON UN CICLO PARA IMPRIMIR EN PANTALLA
    for productos in resultado:
        print("| ",productos[0],"\t|", productos[1],"\t|", productos[2], 
              "\t   |",productos[3],"\t     |",productos[4],"\t|",productos[5],"\t\t|")
    print("\n...")
    
    conn.close()

def reporte_bajo_stock():
    modulo_titulos.titulo_reporte_prod()
    try:
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        # SE SOLICITA EL VALOR AL USUARIO PARA EJECUTAR LA QUERY AL SERVIDOR
        limite = modulo_validaciones.solicitar_limite()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        resultado = cursor.fetchall()
        
        if not resultado:
            print(Fore.YELLOW+"\nNo se encontraron productos con stock inferior o igual a", limite)
            print("\nVolviendo al menu pricipal...")
        else:
            print(Fore.YELLOW+"\nLa siguiente lista de productos tiene bajo stock!")
            modulo_titulos.subtitulo_lista_prod()    
            for productos in resultado:
                print("| ",productos[0],"\t|", productos[1],"\t|", productos[2], "\t   |",
                      productos[3],"\t     |",productos[4],"\t|",productos[5],"\t\t|")
            print("\nVolviendo al menu principal...")     
    except ValueError:
        print(Fore.RED+"\nPor favor, ingrese un valor valido para el limite de stock!"+Fore.RESET)
        print("\nVolviendo al menu pricipal...")
    finally:
        if conn:
            conn.close()
    
def buscar_productos():
    modulo_titulos.titulo_buscar_prod()
    try:
        # CONEXION A LA BBDD
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        # LA BUSQUEDA ES VIA NOMBRE Y REUTILIZAMOS EL MODULO VALIDACIONES
        nombre = modulo_validaciones.solicitar_nombre()
        # SE EJECUTA LA PETICION A LA BBDD
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
        resultado = cursor.fetchall()
        # VALIDACION Y PRESENTACION DEL RESULTADO
        if not resultado:
            print(Fore.YELLOW+"\nNo se encontraron productos con el nombre", nombre.upper())
            print("\nVolviendo al menu pricipal...")
        else:    
            modulo_titulos.subtitulo_lista_prod()    
            for productos in resultado:
                print("| ",productos[0],"\t|", productos[1],"\t|", productos[2], "\t   |",
                      productos[3],"\t     |",productos[4],"\t|",productos[5],"\t\t|")
            print("\nVolviendo al menu principal...") 
    finally:
        # CERRAMOS CONEXION A LA BBDD
        if conn:
            conn.close()
    

# INICIALIZACION
modulo_bbdd.crearDB()
modulo_bbdd.crearTabla()
mostrar_menu()

