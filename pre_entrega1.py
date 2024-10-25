""" Requisitos para la entrega:
1. Crear un menú interactivo
Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados. """

choose = 0

products_list = []


while choose != 3:
    print("\n=============== INVENTARIO ===============")
    print("1. Agregar prodcutos al inventario")
    print("2. Mostrar productos registrados")
    print("3. Salir")
    print("==========================================\n")
    
    choose = int(input("Elija una opcion del menu (1, 2 o 3): "))

    if choose == 1:
        print(f'\nElegiste la opcion {choose} "Agregar prodcutos al inventario"\n')
    elif choose == 2:
        print(f'\nElegiste la opcion {choose} "Mostrar productos registrados"\n')
    else:
        print(f'\nElegiste opcion {choose} para salir del sistema, hasta luego!\n')