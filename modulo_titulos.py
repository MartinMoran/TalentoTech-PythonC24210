from colorama import init, Fore

def titulo_menu():#43
    print(Fore.CYAN+"\n+-----------------------------------------+")
    print(Fore.CYAN+"|               INVENTARIO                |")
    print(Fore.CYAN+"+-----------------------------------------+")
    print("| 1. Registrar productos en el inventario |")
    print("| 2. Actualizar productos del inventario  |")
    print("| 3. Eliminar productos del inventario    |")
    print("| 4. Mostrar productos                    |")
    print("| 5. Reporte de bajo stock                |")
    print("| 6. Buscar productos                     |")
    print("| 7. Salir                                |")
    print(Fore.CYAN+"+-----------------------------------------+\n")

def titulo_registrar_prod():#29
    print(Fore.CYAN+"\n+---------------------------+")
    print(Fore.CYAN+"|    REGISTRAR PRODUCTOS    |")
    print(Fore.CYAN+"+---------------------------+\n")  

def titulo_actualizar_prod():#30
    print(Fore.GREEN+"\n+----------------------------+")
    print(Fore.GREEN+"|    ACTUALIZAR PRODUCTOS    |")
    print(Fore.GREEN+"+----------------------------+\n")    

def titulo_eliminar_prod():#30
    print(Fore.RED+"\n+----------------------------+")
    print(Fore.RED+"|     ELIMINAR PRODUCTOS     |")
    print(Fore.RED+"+----------------------------+")

def titulo_mostrar_prod():#29
    print(Fore.BLUE+"\n+---------------------------+")
    print(Fore.BLUE+"|     MOSTRAR PRODUCTOS     |")
    print(Fore.BLUE+"+---------------------------+")

def titulo_reporte_prod():#29
    print(Fore.YELLOW+"\n+---------------------------+")
    print(Fore.YELLOW+"|   REPORTE DE BAJO STOCK   |")
    print(Fore.YELLOW+"+---------------------------+")

def titulo_buscar_prod():#30
    print(Fore.MAGENTA+"\n+----------------------------+")
    print(Fore.MAGENTA+"|      BUSCAR PRODUCTOS      |")
    print(Fore.MAGENTA+"+----------------------------+\n")
    
def subtitulo_lista_prod():
    print(Fore.BLUE+"\n+-------+---------------+----------+-----------------+------------------+-----------------------+")
    print(Fore.BLUE+"| ID\t| Nombre\t| Cantidad | Precio Unitario | Categoria\t| Descripcion\t\t|")
    print(Fore.BLUE+"+-------+---------------+----------+-----------------+------------------+-----------------------+")
    
init(autoreset=True)
