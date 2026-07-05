from producto import Producto

# Lista donde se guardarán todos los productos
inventario = []

def registrar_producto():

    id = input("ID del producto: ")

    # Verificar que el ID no exista
    for producto in inventario:
        if producto.id == id:
            print("Error: ese ID ya existe.")
            return

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    nuevo_producto = Producto(id, nombre, categoria, precio, stock)

    inventario.append(nuevo_producto)

    print("Producto registrado correctamente.")

def mostrar_productos():

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")

    for producto in inventario:
        print(f"ID: {producto.id}")
        print(f"Nombre: {producto.nombre}")
        print(f"Categoría: {producto.categoria}")
        print(f"Precio: {producto.precio}")
        print(f"Stock: {producto.stock}")
        print(f"Ventas: {producto.ventas_totales}")
        print("----------------------")

def vender_producto():

    id = input("ID del producto a vender: ")

    for producto in inventario:

        if producto.id == id:

            cantidad = int(input("Cantidad a vender: "))

            #Bloqueo por stock insuficiente
            if cantidad > producto.stock:
                print("Error: Stock insuficiente.")
                return

            #Bloqueo si no hay stock
            if producto.stock <= 0:
                print("Error: Producto agotado.")
                return

            #Actualizar stock
            producto.stock -= cantidad

            #Sumar ventas
            producto.ventas_totales += cantidad

            print("Venta realizada correctamente.")

            #Alerta de reabastecimiento
            if producto.stock < 5:
                print("ALERTA: Stock bajo, reabastecer producto.")

            return

    print("Error: Producto no encontrado.")

def cancelar_venta():

    id = input("ID del producto: ")

    for producto in inventario:

        if producto.id == id:

            cantidad = int(input("Cantidad a cancelar: "))

            # validar que no cancele más de lo vendido
            if cantidad > producto.ventas_totales:
                print("Error: No puedes cancelar más de lo vendido.")
                return

            # revertir ventas
            producto.ventas_totales -= cantidad

            # regresar stock
            producto.stock += cantidad

            print("Venta cancelada correctamente.")

            return

    print("Error: Producto no encontrado.")

def producto_mas_vendido():

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    mas_vendido = inventario[0]

    for producto in inventario:

        if producto.ventas_totales > mas_vendido.ventas_totales:
            mas_vendido = producto

    print("\n--- PRODUCTO MÁS VENDIDO ---")
    print(f"ID: {mas_vendido.id}")
    print(f"Nombre: {mas_vendido.nombre}")
    print(f"Categoría: {mas_vendido.categoria}")
    print(f"Precio: {mas_vendido.precio}")
    print(f"Stock: {mas_vendido.stock}")
    print(f"Ventas: {mas_vendido.ventas_totales}")

def ordenar_productos():

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    print("\n--- ORDENAR PRODUCTOS ---")
    print("1. Por precio (menor a mayor)")
    print("2. Por stock (mayor a menor)")
    print("3. Por ventas (mayor a menor)")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        ordenados = sorted(inventario, key=lambda p: p.precio)

    elif opcion == "2":
        ordenados = sorted(inventario, key=lambda p: p.stock, reverse=True)

    elif opcion == "3":
        ordenados = sorted(inventario, key=lambda p: p.ventas_totales, reverse=True)

    else:
        print("Opción no válida.")
        return

    print("\n--- PRODUCTOS ORDENADOS ---")

    for p in ordenados:
        print(f"ID: {p.id}")
        print(f"Nombre: {p.nombre}")
        print(f"Precio: {p.precio}")
        print(f"Stock: {p.stock}")
        print(f"Ventas: {p.ventas_totales}")
        print("----------------------")

def mostrar_agotados():

    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    print("\n--- PRODUCTOS AGOTADOS ---")

    encontrado = False

    for producto in inventario:

        if producto.stock == 0:

            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Categoría: {producto.categoria}")
            print(f"Precio: {producto.precio}")
            print(f"Ventas: {producto.ventas_totales}")
            print("----------------------")

            encontrado = True

    if not encontrado:
        print("No hay productos agotados.")