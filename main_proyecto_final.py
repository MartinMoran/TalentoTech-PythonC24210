import sqlite3 as sql
import modulos_bbdd
import modulos_validaciones

def mostrar_menu():
    opcion = ""
    while opcion != "7":   
        print("\n----------------------------------------")
        print("               INVENTARIO                  ")
        print("----------------------------------------")
        print("1. Registrar productos en el inventario")
        print("2. Actualizar productos del inventario")
        print("3. Eliminar productos del inventario")
        print("4. Mostrar productos")
        print("5. Reporte de bajo stock")
        print("6. Buscar productos")
        print("7. Salir")
        print("----------------------------------------\n")

        opcion = input("Elija una opcion del menu: ")

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
                print(f'\nElegiste la opcion {opcion}, saliendo del sistema, hasta luego!\n')
            case _:
                print(f'\nLa opcion "{opcion}" no es una eleccion correcta, intenta nuevamente!')


def registrar_productos():
    while True:
        print("\n----------------------------------------")
        print("           REGISTRAR PRODUCTOS        ")
        print("----------------------------------------\n")
        
        # SOLICITAMOS LOS DATOS CON EL MODULO VALIDACIONES
        nombre = modulos_validaciones.solicitar_nombre()
        cantidad = modulos_validaciones.solicitar_cantidad()
        precio_unitario = modulos_validaciones.solicitar_precio_unitario()
        categoria = modulos_validaciones.solicitar_categoria()
        descripcion = modulos_validaciones.solicitar_descripcion()
    
        try:
            # CONEXION A LA BASE DE DATOS Y EJECUCION DEL REGISTRO EN BBDD       
            conn = sql.connect("inventario.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO productos (nombre, cantidad, precio_unitario, categoria, descripcion) 
                        VALUES(?, ?, ?, ?, ?)''', (nombre, cantidad, precio_unitario, categoria, descripcion))
            conn.commit()
            print("")
            print(f"Producto {nombre.upper()} agregado correctamente")
            # VALIDAMOS SI EL USUARIO QUIERE CONTINUAR AGREGANDO REGISTROS    
            continuar = input("\nDesea continuar agregando productos? (s/n): ").lower()
            if continuar == "s":
                continue
            elif continuar == "n":
                print("\nVolviendo al menu principal")
                break
            else:
                print("\nDebe ingresar una respuesta valida!")
                print("...")
                print("Volviendo al menu principal")
                break
        except Exception as e:
            print(f"Error inesperado {e}")
            
        finally:
            if conn:
                conn.close()
        
        
def mostrar_productos():
    print("\n----------------------------------------")
    print("     MOSTRAR PRODUCTOS REGISTRADOS     ")
    print("----------------------------------------\n")
    
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    resultado = cursor.fetchall()
    
    # RECORREMOS EL RESULTADO CON UN CICLO PARA IMPRIMIR EN PANTALLA
    for productos in resultado:
        print("ID:", productos[0], "- Nombre:", productos[1], "- Cantidad:", 
              productos[2], "- Precio unitario:", productos[3], "- Categoria:", 
              productos[4], "- Descripcion:", productos[5])
    
    conn.close()


def actualizar_productos():
    print("\n----------------------------------------")
    print("          ACTUALIZAR PRODUCTOS         ")
    print("----------------------------------------")
    # SE PRESENTAN LOS PRODUCTOS PARA VER EL LISTADO GENERAL
    mostrar_productos()
    print("")

    # SOLICITAMOS LOS DATOS AL USUARIO CON INPUT Y MODULO VALIDACIONES
    id = modulos_validaciones.solicitar_id()
    cantidad = modulos_validaciones.solicitar_cantidad()
    
    conn = sql.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE productos SET cantidad=? WHERE id=?",(cantidad, id))
    conn.commit()
    
    print("\nProducto actualizado correctamente!\n")
    print("Volviendo al menu principal")
    
    conn.close()


def eliminar_productos():
    while True:
        print("\n----------------------------------------")
        print("          ELIMINAR PRODUCTOS         ")
        print("----------------------------------------")
        
        mostrar_productos()
        print("")
        
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        
        id = modulos_validaciones.solicitar_id()
        confirmar = input("\nEsta seguro de borrar el registro? (s/n): ").lower()
        
        # VALIDAMOS LA ELIMINACION CON UNA SEGUNDA CONSULTA
        if confirmar == "s":
            cursor.execute("DELETE FROM productos WHERE id=?",(id,))
            conn.commit()
            print(f"\nProducto eliminado correctamente")
            print("...")
            print("Volviendo al menu principal")
            break
        # VALIDAMOS SI EL USUARIO QUIERE SALIR AL MENU PRINCIPAL O CONTINUAR ELIMINANDO
        elif confirmar == "n":
            continuar = input("\nDesea volver al menu principal? (s/n): ").lower()
            if continuar == "s":
                print("...")
                print("Volviendo al menu principal")
                break
            elif continuar == "n":
                print("...")
                print("\nVolviendo a eliminar productos")
                continue
            else:
                print("\nDebe ingresar una respuesta valida!")
                print("...")
                print("\nVolviendo a eliminar productos")
                continue
        else:
            print("\nDebe ingresar una respuesta valida!")
            print("...")
            print("\nVolviendo a eliminar productos")
        
        conn.close()


def reporte_bajo_stock():
    print("\n----------------------------------------")
    print("         REPORTE DE BAJO STOCK         ")
    print("----------------------------------------")
    
    try:
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        # SE SOLICITA EL VALOR AL USUARIO PARA EJECUTAR LA QUERY AL SERVIDOR
        limite = int(input("\nIngrese el valor limite de stock para emitir el reporte: "))
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        resultado = cursor.fetchall()
        if not resultado:
            print("\nNo se encontraron productos con stock inferior o igual a", limite)
        else:
            print("")    
            for productos in resultado:
                print("ID:", productos[0], "- Nombre:", productos[1], "- Cantidad:", 
                      productos[2], "- Precio unitario:", productos[3], "- Categoria:", 
                      productos[4], "- Descripcion:", productos[5])        
    except ValueError:
        print("\nPor favor, ingrese un valor valido para el limite de stock!")
    finally:
        if conn:
            conn.close()
    

def buscar_productos():
    print("\n----------------------------------------")
    print("            BUSCAR PRODUCTOS            ")
    print("----------------------------------------\n")

    try:
        # CONEXION A LA BBDD
        conn = sql.connect("inventario.db")
        cursor = conn.cursor()
        # LA BUSQUEDA ES VIA NOMBRE Y REUTILIZAMOS EL MODULO VALIDACIONES
        nombre = modulos_validaciones.solicitar_nombre()
        # SE EJECUTA LA PETICION A LA BBDD
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        resultado = cursor.fetchall()
        # VALIDACION Y PRESENTACION DEL RESULTADO
        if not resultado:
            print("\nNo se encontraron productos con el nombre", nombre.upper())
        else:    
            print("")  
            for productos in resultado:
                print("ID:", productos[0], "- Nombre:", productos[1], "- Cantidad:", 
                      productos[2], "- Precio unitario:", productos[3], "- Categoria:", 
                      productos[4], "- Descripcion:", productos[5])
    finally:
        # CERRAMOS CONEXION A LA BBDD
        if conn:
            conn.close()
    

# INICIALIZACION
modulos_bbdd.crearDB()
modulos_bbdd.crearTabla()
mostrar_menu()

