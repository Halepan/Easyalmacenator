import json


def Save_archivo(productos):
  """Guarda información de productos en un archivo JSON.

  Args:
    productos: Un diccionario donde las claves son los nombres de los productos y 
    los valores son instancias de clases de producto.
    retorn:"guardado con exito"
  """

  datos_productos = []
  for nombre_producto, producto in productos.items():
    datos_producto = {"tipo": type(producto).__name__, nombre_producto: producto.dict()}
    
    producto.dict()

    datos_productos.append(datos_producto)

  with open("Productos del almacen.txt", "w") as archivo:
    json.dump(datos_productos, archivo, indent=4)
  archivo.close()
  return "Guardado con exito"


class Control():
  def __init__(self,productos={}):
   self.productos = productos

  def AggProductos (self,producto):
   self.productos[producto.nombre] = producto
   return Save_archivo(self.productos)
    
  def FindProduct(self,nombre):
   if nombre in self.productos:
      return self.productos[nombre]
   else:
      return None

  def Look_diccionary_product(self):
   return self.productos

  def Look_list_product(self):
   productos= (self.productos.keys())
   return productos

  def Actualizacion(self,actual):
   self.productos[actual.nombre] = actual
   return Save_archivo(self.productos)
  
  def Borrar_product(self,nombre):
   self.productos.pop(nombre)
   Save_archivo(self.productos)
   return True