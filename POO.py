class Producto():
 # Atributos
 Nombre=""
 Precio=0.0
 def __init__(self, nombre, precio):
 self.Nombre=nombre.upper()
 self.Precio=precio
 
 def Subtotal(self):
 return self.Precio/1.16

 def Impuesto(self):
 return (self.Precio/1.16)*0.16

 def MostrarInfo(self):
 print("-"*50)
 print(self.Nombre)
 print(self.Subtotal)
 print(self.Impuesto)
 print(self.Precio)
 
pastelillo=Producto("Cachito Tortuga",80.50)
pastelillo.MostrarInfo()
pastelillo.Precio=100
pastelillo.MostrarInfo()