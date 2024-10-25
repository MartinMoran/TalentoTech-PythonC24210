""" Requisitos para la entrega:
1. Crear un menú interactivo
Crear un menú interactivo utilizando bucles while y condicionales if-elif-else: 
El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos. 
Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados. """

# Inicializacion de la variable
choose = "" 

# Menu inicial
print("\n=============== INVENTARIO ===============")
print("1. Agregar prodcutos al inventario")
print("2. Mostrar productos registrados")
print("3. Salir")
print("==========================================\n")

# Ciclo while se valida que la eleccion del usuario sea distinta de salir (3)
while choose != "3":
# No se agrega la funcion int al input para no romper el codigo si el usuario usa un caracter.
    choose = input("Elija una opcion del menu (1, 2 o 3): ")
# El if verifica que selecciona en el menu el numero 1 y modifica el valor de la variable para salir del ciclo y sistema.
    if choose == "1":
        print(f'\nElegiste la opcion: {choose} "Agregar prodcutos al inventario"\n')
        choose = "3"
# Elif verifica que selecciona en el menu el numero 2 y modifica el valor de la variable para salir del ciclo y sistema.
    elif choose == "2":
        print(f'\nElegiste la opcion: {choose} "Mostrar productos registrados"\n')
        choose = "3"
# Elif verifica que selecciona en el menu el numero 3, dando un mensaje de la salida del ciclo y sistema.
    elif choose == "3":
        print(f'\nElegiste opcion: {choose}, para salir del sistema, hasta luego!\n')
# El else se usa para validar que ingresa un valor correcto y se ofrece nuevamente el menu.
    else:
        print(f'\nLa opcion "{choose}" no es una eleccion correcta, intenta nuevamente!\n')
        
        print("=============== INVENTARIO ===============")
        print("1. Agregar prodcutos al inventario")
        print("2. Mostrar productos registrados")
        print("3. Salir")
        print("==========================================\n")