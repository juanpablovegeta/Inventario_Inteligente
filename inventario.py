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