# Sistema de Inventario Inteligente

## Descripción

Este proyecto fue realizado en **Python** utilizando **Programación Orientada a Objetos (POO)**. El objetivo es simular un sistema de inventario para una tienda, donde se pueden registrar productos, realizar ventas y llevar un control del stock mediante un menú interactivo.

## ¿Qué puede hacer el programa?

* Registrar nuevos productos.
* Mostrar todos los productos registrados.
* Vender productos.
* Cancelar una venta y recuperar el stock.
* Mostrar el producto más vendido.
* Mostrar los productos agotados.
* Ordenar los productos por precio, stock o número de ventas.

## Reglas que sigue el sistema

* No permite vender más productos de los que hay en existencia.
* Si después de una venta el stock baja de 5 unidades, muestra una alerta para reabastecer el producto.
* Al cancelar una venta, el stock y las ventas se actualizan automáticamente.

## Archivos del proyecto

* **main.py:** contiene el menú principal del programa.
* **inventario.py:** contiene las funciones del sistema de inventario.
* **producto.py:** contiene la clase `Producto`.
* **datos_productos.xlsx:** archivo Excel con 50 productos de ejemplo (solo referencia)

## Cómo ejecutar el programa

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

```bash
python main.py
```

3. Elegir la opción que se desee desde el menú.

## Herramientas utilizadas

* Python 3
* Visual Studio Code
* Git
* GitHub

## Autor

**Juan Pablo**

Proyecto realizado como práctica para la materia de ALGORITMOS Y ESTRUCTURA DE DATOS.

