from inventario import registrar_producto

while True:

    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Registrar producto")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")