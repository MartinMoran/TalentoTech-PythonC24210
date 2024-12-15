import sqlite3 as sql

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
                print(f"\nEl id {id} no fue encontrado en el inventario!\n")
        except ValueError:
            print("\nDebe ingresar un id correcto!\n")
        except sql.Error:
            print("\nError al conectarse a la base de datos\n")

def solicitar_nombre(): 
    while True: 
        nombre = input("Ingrese el nombre del producto: ") 
        if nombre: 
            return nombre 
        print("\nEl nombre no puede estar vacío!\n")

def solicitar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad >= 0:
                return cantidad
        except ValueError:
            print("\nDebe ingresar un número entero!\n")
            
def solicitar_precio_unitario():
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario >= 0:
                return precio_unitario
        except ValueError:
            print("\nDebe ingresar un número válido!\n")

def solicitar_categoria():
    while True:
        categoria = input(f"Ingrese la categoria del producto: ")
        if categoria: 
            return categoria
        print("\nLa categoría no puede estar vacía!\n")

def solicitar_descripcion():
    while True:
        descripcion = input("Ingrese la descripción del producto: ")
        if descripcion: 
            return descripcion
        print("\nLa descripción del producto no puede estar vacía!\n")