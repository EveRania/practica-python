## Gestión de Inventario de Tienda Online
Implementar un sistema para gestionar el inventario de productos en un e-commerce, incluyendo la entrada y salida de stock.

### Requisitos:
- Cada producto tiene un nombre, un precio unitario, una categoría y una cantidad en stock. El producto puede darse de alta con stock o sin stock ( = 0).
- Se debe poder registrar la entrada de stock para un producto existente (incrementa la cantidad en stock).
- Se debe poder registrar la salida de stock para un producto (decrece la cantidad en stock) por venta del mismo.
- Cada producto tiene un "stock mínimo". Si la cantidad en stock de un producto cae por debajo de su stock mínimo, sólo se puede vender de a 1 unidad por venta.
- Los productos en inventario se organizan en centros de distribución de los cuales se conoce su código (alfanumérico) y su dirección. 
- Se puede calcular el valor total de los productos del centro de distribución, total, total por categoría, total por producto.