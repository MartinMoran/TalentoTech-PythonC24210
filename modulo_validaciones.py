import sqlite3 as sql
from colorama import init, Back, Fore

init(autoreset=True)

def solicitar_id():
    while True:
        try:
            id = int(input("Ingrese el id del producto: "))
            conn = sql.connect("inventario.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            resultado = cursor.fetchone()
            if resultado:
                return id
            else:
                print(Back.YELLOW+Fore.BLACK+f"\nEl id {id} no fue encontrado en el inventario"+Back.RESET+Fore.RESET+"\n")
        except ValueError:
            print(Back.RED+"\nDebe ingresar un id correcto!"+Back.RESET+"\n")
        except sql.Error:
            print(Back.BLUE+"\nError al conectarse a la base de datos"+Back.RESET+"\n")

def solicitar_nombre(): 
    while True: 
        nombre = input("Ingrese el nombre del producto: ") 
        if nombre: 
            return nombre 
        print(Back.RED+"\nEl nombre no puede estar vacío!"+Back.RESET+"\n")

def solicitar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad >= 0:
                return cantidad
        except ValueError:
            print(Back.RED+"\nDebe ingresar un número entero!"+Back.RESET+"\n")
            
def solicitar_precio_unitario():
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario >= 0:
                return precio_unitario
        except ValueError:
            print(Back.RED+"\nDebe ingresar un número valido!"+Back.RESET+"\n")

def solicitar_categoria():
    while True:
        categoria = input(f"Ingrese la categoria del producto: ")
        if categoria: 
            return categoria
        print(Back.RED+"\nLa categoría no puede estar vacía!"+Back.RESET+"\n")

def solicitar_descripcion():
    while True:
        descripcion = input("Ingrese la descripción del producto: ")
        if descripcion: 
            return descripcion
        print(Back.RED+"\nLa descripción del producto no puede estar vacía!"+Back.RESET+"\n")
        
def solicitar_limite():
    while True:
        limite = int(input("\nIngrese el valor limite de stock para emitir el reporte: "))
        if limite: 
            return limite
        print(Back.RED+"\nDebe ingresar un número válido!"+Back.RESET+"\n")