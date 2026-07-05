from inventario import registrar_producto, mostrar_productos, vender_producto, cancelar_venta, producto_mas_vendido, ordenar_productos, mostrar_agotados

while True:

    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Vender producto")
    print("4. Cancelar venta")
    print("5. Producto más vendido")
    print("6. Ordenar productos")
    print("7. Mostrar productos agotados")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        vender_producto()

    elif opcion == "4":
        cancelar_venta()

    elif opcion == "5":
        producto_mas_vendido()

    elif opcion == "6":
        ordenar_productos()

    elif opcion == "7":
        mostrar_agotados()

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")