# Ejercicio N° 1 del  Parcial N° 2 - Optativo.
# Alumno: Elias Franco Duarte - C.I: 6.167.356

class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock =  stock

    @property    
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precioIntroducido):
        if precioIntroducido >= 1000:
            self._precio = precioIntroducido
            print("El precio que introdujiste está bien, debe de ser mayor a 1000")
        else:
            raise ValueError("El precio que ingresa debe de ser mayor a 1000, por favor introduce otro número. Muchas gracias!!")
        
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stockIntroducido):
        if stockIntroducido >= 0:
            self._stock = stockIntroducido
        else: 
            raise ValueError("El stock no puede ser negativo en cantidad, intente otra cantidad")
        
    def venderProductos(self, cantidadVendida):
        if cantidadVendida < 0:
            raise ValueError("La cantidad vendida no puede ser 0, tiene que ser mayor a 0.")
        elif cantidadVendida > self._stock:
            raise ValueError("La cantidad que desea vender es mayor a nuestro stock, no tenemos esa cantidad de stock.")
        else:
            self.stock -= cantidadVendida
            print(f"La venta ha sido exitosa. Se ha vendido la cantidad de {cantidadVendida} | Producto: {self.nombre} | En stock quedan {self.stock}")
            
    def reponerProductos(self, reponerStock):
        if reponerStock < 0: 
            raise ValueError("La cantidad de stock que desea reponer debe ser mayor a 0. Intente de nuevo")
        else:
            self._stock += reponerStock
            print(f"Se repusieron la cantidad de {reponerStock} | Producto: {self.nombre} | Cantidad Actual: {self.stock}")
            
    def stockAgotado(self):
        return self.stock == 0
    
    def mostrarDetalles(self) :
        return f"Nombre del Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}"
    
    def __str__(self):
        return self.mostrarDetalles()
        
listaProductos = [
    Producto("Coca Cola", 12000, 10),
    Producto("Pepsi", 8000, 15),
    Producto("Harina", 6000, 5),
    Producto("Kampito", 4500, 0),
    Producto("Frugos Sabor Naranja", 10000, 8),
    Producto("Pulp", 11000, 0)
]
            
for producto in listaProductos:
    if producto.stockAgotado():
        print(f"El producto: '{producto.nombre}'está vacío | Sin Stock!!")
        print(producto)
print("\n") 
print("Productos")
for producto in listaProductos:
    print(producto)