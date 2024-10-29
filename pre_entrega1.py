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

# Inicializacion de las variables
choose = "" 
products = []
prod_name = ""
prod_qty = 0

# Ciclo while se valida que la eleccion del usuario sea distinta de salir (3)
while choose != "3":
# Menu inicial     
    print("\n=============== INVENTARIO ===============")
    print("1. Agregar prodcutos al inventario")
    print("2. Mostrar productos registrados")
    print("3. Salir")
    print("==========================================\n")
# No se agrega la funcion int al input para no romper el codigo si el usuario usa un caracter.
    choose = input("Elija una opcion del menu (1, 2 o 3): ")
# El if verifica que seleccionamos en el menu el numero 1.
    if choose == "1":
        print(f'\nElegiste la opcion {choose} - "Agregar prodcutos al inventario"\n')
# Se requiere el nombre de producto y cantidad, se guardan los mismos como un array dentro de la lista.
        prod_name = input("Ingrese el nombre del producto: ")
        prod_qty = int(input(f"Ingrese la cantidad del prodcuto {prod_name}: "))
        products.append([prod_name, prod_qty])
# Elif verifica que seleccionamos en el menu el numero 2 y usamos un while con un contador para recorrer el array.
    elif choose == "2":
        print(f'\nElegiste la opcion {choose} - "Mostrar productos registrados"\n')
        index = 0
        while index < len(products):
            print(f'El producto {index+1} es: {products[index]}\n')
            index += 1
# Elif verifica que seleccionamos en el menu el numero 3, dando un mensaje de despedida del sistema.
    elif choose == "3":
        print(f'\nElegiste la opcion {choose}, saliendo del sistema, hasta luego!\n')
# El else se usa para validar que ingresa un valor correcto para el menu.
    else:
        print(f'\nLa opcion "{choose}" no es una eleccion correcta, intenta nuevamente!\n')
