""" Requisitos para la entrega:
1. Crear un menú interactivo
Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados. 
2. Agregar productos al inventario
Implementar la funcionalidad para agregar productos a una lista: 
Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.
3. Mostrar el inventario
Mostrar los productos ingresados: 
Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el momento. """


def registrar_productos():
    print(f'\nElegiste la opcion {choose} - "Agregar productos al inventario"\n')
    prod_name = input("Ingrese el nombre del producto: ")
    prod_qty = int(input(f"Ingrese la cantidad del producto {prod_name}: "))
    products.append([prod_name, prod_qty])
    
        
def mostrar_productos():
    print(f'\nElegiste la opcion {choose} - "Mostrar productos registrados"\n')
    
    for i, product in enumerate(products):
        print(f'Producto {i+1}: {products[i]}')

def actualizar_productos():
    print("Actualizacion de productos")

def eliminar_productos():
    print("Eliminacion de productos")


# Inicializacion de las variables
choose = "" 
products = []
prod_name = ""
prod_qty = 0

while choose != "5":   
    print("\n----------------------------------------")
    print("               INVENTARIO                  ")
    print("----------------------------------------")
    print("1. Registrar productos en el inventario")
    print("2. Actualizar productos del inventario")
    print("3. Eliminar productos del inventario")
    print("4. Mostrar productos registrados")
    print("5. Salir")
    print("----------------------------------------\n")

    choose = input("Elija una opcion del menu: ")

    if choose == "1":
        registrar_productos()
    elif choose == "2":
        actualizar_productos()
    elif choose == "3":
        eliminar_productos()
    elif choose == "4":
        mostrar_productos()
    elif choose == "5":
        print(f'\nElegiste la opcion {choose}, saliendo del sistema, hasta luego!\n')
    else:
        print(f'\nLa opcion "{choose}" no es una eleccion correcta, intenta nuevamente!')
